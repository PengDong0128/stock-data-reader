
# coding: utf-8

# # This module is for construct the datset for future work , it is generalized from my previous work feature_extraction.py

# In[1]:

import pandas as pd
import numpy as np
import yahoo_finance as yf
import quandl as ql
# more to import


# In[312]:

class StockDataReader(object):
    """StockDataReader is for reading and constructing dataset for stock data
    Fist you must enter your api key for Quandl.com
    Example:
    dat_reader = StockDataReader('your_api_key')
    """
    def __init__(self,quandl_key):
        """quandl_key : the api key of your quandl account"""
        ql.ApiConfig.api_key = quandl_key
        self.external=False
        self.sentiment=False
        self.sp500 = False
        sp = yf.Share(symbol='^GSPC')
        #self.index_price = 
    def read_sentiment(self,tic,date_start,date_end):
        """read sentiment data for a ticker"""
        path = 'NS1/'+tic+'_us'
        df = (ql.get(path,end_date = date_end )).reset_index()
        return df
    def read_index(self,start_date,end_date):
        """read s&p500 index
        
        Variables:
        start_date: the start date of the index
        end_date: the end date of the index
        """
        sp = yf.Share(symbol='^GSPC')
        self.sp500_table = pd.DataFrame(sp.get_historical(start_date=start_date,end_date=end_date))
        self.sp500_table['Date'] = pd.to_datetime(self.sp500_table['Date'])
        self.sp500_table = self.sp500_table[['Date','Adj_Close','Volume']]
        (self.sp500_table).columns = ['date','sp_adj_close','sp_volume']
        self.sp500_table['sp_adj_close'] = (self.sp500_table['sp_adj_close']).apply(float)
        self.sp500_table['sp_volume'] = (self.sp500_table['sp_volume']).apply(float)
        self.sp500 = True
    def read_external(self,path,time_scale='y'):
        """read fundamentals for a company(ticker)
       
        Variables:
        path: the path for the file to be loaded
        time_scale: 'y'--> using anual data, 'd' --> using daily data
        """
        self.external_table= pd.read_csv(path)
        if time_scale=='y':
            self.external_table['fyear'] = self.external_table['fyear'].apply(int)
        else:
            self.external_table['date'] = pd.to_datetime(self.external_table['date'])
        self.external = True
        self.external_time_scale = time_scale
        
    def initialize_data(self,tic,date_start='2009-01-01',date_end='2016-12-31',sentiment=False):
        """get the price data and sentiment data in a time period.
        
        Variables:
        date_start : the start date of the data.
        date_end   : the end date of the data.
        sentiment  : whether use sentiment data or not, will return None if set as False.
        fundamentals: whether use fundamentals or not, will return None if set as False
        
        Warning:
        1.If you want to use sentiment data , you must subscribe FinSentS in Quandl.com
        2.Sentiment data is only available from 2013-01-01 for a specific part of tickers
        3.If you want to use fundamental data, you must call read_external to load in the whole dataset
        """
        self.current_ticker = tic
        # price data,from quandl
        price = ql.get_table('WIKI/PRICES', ticker = tic, 
                                 date = { 'gte': date_start, 'lte': date_end })
        price_df = pd.DataFrame(price)
        # sentiment data, from infotrie
        if sentiment:
            self.sentiment=True
            try:
                sentiment = self.read_sentiment(tic,date_start,date_end)
            except:
                print('there is no sentiment data for this ticker')
                sentiment = pd.DataFrame(np.zeros(len(price_df),5))
                sentiment['Date'] = price_df['date']
            self.sentiment_table = sentiment[['Date','Sentiment','News Volume','News Buzz']]
        else:
            self.sentiment=False
        self.price_table = price_df[['date','adj_close','adj_volume']]
    def merge_table(self):
        """merge all the datasets into one
        
        You can call this function and get self.table without further feature constructions
        """
        self.table= (self.price_table).copy()
        self.price_table['date'] = pd.to_datetime(self.price_table['date'])
        if self.sentiment==True:
            self.sentiment_table['Date'] = pd.to_datetime(self.sentiment_table['Date'])
            self.table = pd.merge(self.table,self.sentiment_table,
                                  left_on='date',right_on = 'Date',
                                  how = 'left')
            self.table = (self.table).drop('Date',axis=1)
        if self.external ==True:
            if self.external_time_scale == 'y':
                self.table['year'] =[x.year for x in self.table['date']]
                tmp = self.external_table[self.external_table['tic']==self.current_ticker]
                self.table = pd.merge(self.table,tmp,
                                      left_on='year',right_on = 'fyear',
                                      how = 'left')
                self.table = self.table.drop(['year','fyear'],axis=1)
            else:
                tmp = self.external_table[self.external_table['tic']==self.current_ticker]
                self.table = pd.merge(self.table,tmp,on='date',how = 'left')
        if self.sp500 ==True:
            self.table = pd.merge(self.table,self.sp500_table,
                                  on = 'date',
                                  how = 'left')
        return self.table
    def feature(self,dic):
        """construct features based on the data table you just created
        
        Variables:
        dic : the input dictionary, format is {'feature_name':function}
        
        Example:
        def pe(dat):
            eps = dat['ni']/dat['csho']
            return dat['adj_close']/eps
        def price_to_book_value(dat):
            book = dat['ceql']/dat['csho']
            return dat['adj_close']/book
        def ps(dat):
            sps = dat['sale']/dat['csho']
            return dat['adj_close']/sps
        feature_dic = {'pe':pe,
                       'price_to_book_value':price_to_book_value,
                       'ps':ps}
        StockDataReader.feature(feature_dic)
        
        After you call this, all the features you just constructed will be append in the end of the table
        The output of this function is the column names for the table after construction.
        """
        dat = (self.merge_table()).copy()
        feature_list = list(dic.keys())
        for feature in feature_list:
            dat[feature] = dic[feature](dat)
        self.table = dat
        return dat.columns
    def trim(self,column_selected):
        """trim the dataset
        column_selected: a list of column names which you want to include in the final table
        Example:
        BEFORE: StockDataReader.table.columns =Index(['date', 'adj_close', 'adj_volume', 'tic', 'ceql', 
        'csho', 'ni', 'sale','sp_adj_close', 'sp_volume', 'pe', 'price_to_book_value', 'ps',
       '20mean', 'return', 'beta'],dtype='object')
        
        StockDataReader.trim(['adj_price','ps','pe'])
        
        AFTER: StockDataReader.table.columns=Index(['adj_price','ps','pe'],dtype='object')
        """
        self.table = self.table[column_selected]
        print((self.table).columns)
    def construct_data(self,rolling=False,time_window=1,thresh_date = '2009-01-01'):
        """the function return you the final dataset
        Variables:
        rolling: True --> return the rolling data, False --> return un-rolling data.
        time_window: the time window (time frame) you want to use
        thresh_date: the split point you want to use,all the data before this date will be removed
        """
        dat=  (self.table).copy()
        y = dat[['date','adj_close']]
        x = dat.iloc[:,1:]
        dat = y.copy()
        xcol = list(x.columns)
        if rolling == True:
            for i in range(1,time_window+1):
                lis = xcol.copy()
                for j in range(len(lis)):
                    lis[j] = str(i)+'day_'+lis[j]
                x.columns = lis
                dat = pd.concat([dat,x.shift(i)],axis=1)
        else:
            lis = xcol.copy()
            for i in range(len(lis)):
                lis[i] = str(time_window)+'day_'+lis[i]
            x.columns = lis
            dat = pd.concat([dat,x.shift(time_window)],axis=1)
        dat = dat[dat['date']>thresh_date]
    
        return dat

