
# Stock Data Reader

## Abstract:
### This module is for financial dataset construction. The functions of this module include:
- Importing daily price data for stocks.
- Importing S&P500 daily index.
- Importing external dataset (daily,anual)
- Importing sentiment data from Quandl (you need to subscribe this service)
- Merging datasets before
- Flexibly constructing features based on the dataset merged
- Customizing the data structure (rolling & un-rolling) and time window for the dataset
### Motivation:
- Constructing dataset could be quite annoying when doing financial researches. You need to collect data from different sources, merge them(This could be more annoying when they have different frequency), and construct the features with different structures and time windows.In this module , you can just adjust several variables, then all these works could be easily achieved.
### Data Source:
- Price and sentiment data are collected from Quandl.com
- S&P500 Index is collected from Yahoo Finance
- There is also a port for importing external data

## Instruction

### For using this module , you must have an API Key for quandl.com. You just need to sign up on the webpage and find API Key in your account setting. If you want to use sentiment data , you have to subscribe "FinSentS Web News Sentiment", the link is https://www.quandl.com/data/NS1-FinSentS-Web-News-Sentiment .

### Import the module and initialize it:


```python
from stock_data_reader import StockDataReader
reader = StockDataReader("your_api_key")
```

### Read price and sentiment data from quandl:

- In this step, date_start should be one or two years before the start date you finally want to get. Because when you are calculating some features like moving average and Beta,you will need to use data before that final start date.


```python
reader.initialize_data('CF',date_start='2001-01-01',date_end='2016-12-31',sentiment=True)
```

### Price table:


```python
reader.price_table.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>adj_close</th>
      <th>adj_volume</th>
    </tr>
    <tr>
      <th>None</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2005-08-11</td>
      <td>2.810457</td>
      <td>76671500.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2005-08-12</td>
      <td>3.110586</td>
      <td>29113500.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2005-08-15</td>
      <td>3.001290</td>
      <td>10596500.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2005-08-16</td>
      <td>2.975268</td>
      <td>5141000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005-08-17</td>
      <td>2.923222</td>
      <td>6423500.0</td>
    </tr>
  </tbody>
</table>
</div>



### Sentiment table


```python
reader.sentiment_table.head(5)#sentiment data is only available from 2013
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Sentiment</th>
      <th>News Volume</th>
      <th>News Buzz</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013-01-01</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013-01-02</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013-01-03</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013-01-04</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2013-01-05</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Read S&P500 Index
- For constructing multiple datasets for different stocks, you just need to import index data once.


```python
reader.read_index('2001-01-01','2016-12-31')
```


```python
reader.sp500_table.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>sp_adj_close</th>
      <th>sp_volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-12-30</td>
      <td>2238.830078</td>
      <td>2.670900e+09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-12-29</td>
      <td>2249.260010</td>
      <td>2.336370e+09</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-12-28</td>
      <td>2249.919922</td>
      <td>2.392360e+09</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-12-27</td>
      <td>2268.879883</td>
      <td>1.987080e+09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-12-23</td>
      <td>2263.790039</td>
      <td>2.020550e+09</td>
    </tr>
  </tbody>
</table>
</div>



## Read external data:
- In this section, the fundamental dataset I use is downloaded from Compustat
- The variable 'y' means that I'm using anual data. You can also set it as 'd' for using daily data. If you want to use hybrid data, please first merge them into daily dataset (this is quite a simple work)  and set the variable as 'd'.
- For constructing multiple datasets for different stocks, you just need to import external data once.


```python
reader.read_external('basic_stats.csv','y')
```


```python
reader.external_table.head(5) 
# The ticker is not for IBM, but IBM is contained in this dataset.
# This is an anual dataset
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fyear</th>
      <th>tic</th>
      <th>ceql</th>
      <th>csho</th>
      <th>ni</th>
      <th>sale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>PNW</td>
      <td>2499.323</td>
      <td>84.825</td>
      <td>312.166</td>
      <td>4551.373</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>PNW</td>
      <td>2686.153</td>
      <td>91.255</td>
      <td>149.408</td>
      <td>2637.279</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>PNW</td>
      <td>2829.779</td>
      <td>91.288</td>
      <td>240.579</td>
      <td>2817.852</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>PNW</td>
      <td>2950.196</td>
      <td>91.793</td>
      <td>243.195</td>
      <td>2899.725</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>PNW</td>
      <td>3424.964</td>
      <td>99.057</td>
      <td>176.267</td>
      <td>2987.955</td>
    </tr>
  </tbody>
</table>
</div>



## Merge datasets and construct features:

### If you don't want to do any feature construction, you can just merge datasets simply:


```python
dat = reader.merge_table()
```


```python
dat.iloc[-5:,:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>adj_close</th>
      <th>adj_volume</th>
      <th>Sentiment</th>
      <th>News Volume</th>
      <th>News Buzz</th>
      <th>tic</th>
      <th>ceql</th>
      <th>csho</th>
      <th>ni</th>
      <th>sale</th>
      <th>sp_adj_close</th>
      <th>sp_volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2863</th>
      <td>2016-12-23</td>
      <td>30.445183</td>
      <td>5475503.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>CF</td>
      <td>3348.0</td>
      <td>233.114</td>
      <td>-277.0</td>
      <td>3685.0</td>
      <td>2263.790039</td>
      <td>2.020550e+09</td>
    </tr>
    <tr>
      <th>2864</th>
      <td>2016-12-27</td>
      <td>31.674490</td>
      <td>6222852.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>CF</td>
      <td>3348.0</td>
      <td>233.114</td>
      <td>-277.0</td>
      <td>3685.0</td>
      <td>2268.879883</td>
      <td>1.987080e+09</td>
    </tr>
    <tr>
      <th>2865</th>
      <td>2016-12-28</td>
      <td>31.357249</td>
      <td>3653427.0</td>
      <td>-2.0</td>
      <td>10.0</td>
      <td>3.0</td>
      <td>CF</td>
      <td>3348.0</td>
      <td>233.114</td>
      <td>-277.0</td>
      <td>3685.0</td>
      <td>2249.919922</td>
      <td>2.392360e+09</td>
    </tr>
    <tr>
      <th>2866</th>
      <td>2016-12-29</td>
      <td>31.624921</td>
      <td>4220127.0</td>
      <td>-2.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>CF</td>
      <td>3348.0</td>
      <td>233.114</td>
      <td>-277.0</td>
      <td>3685.0</td>
      <td>2249.260010</td>
      <td>2.336370e+09</td>
    </tr>
    <tr>
      <th>2867</th>
      <td>2016-12-30</td>
      <td>31.208543</td>
      <td>4181315.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>CF</td>
      <td>3348.0</td>
      <td>233.114</td>
      <td>-277.0</td>
      <td>3685.0</td>
      <td>2238.830078</td>
      <td>2.670900e+09</td>
    </tr>
  </tbody>
</table>
</div>



## If you want to construct features, you don't have to call merge_table(), just simply import a dictionary in format '{'feature_name':function}, and call feature():


```python
def pe(dat):
    eps = dat['ni']/dat['csho']
    return dat['adj_close']/eps
def price_to_book_value(dat):
    book = dat['ceql']/dat['csho']
    return dat['adj_close']/book
def ps(dat):
    sps = dat['sale']/dat['csho']
    return dat['adj_close']/sps
def daily_return(dat):
    return (dat['adj_close']/(dat['adj_close'].shift(1))-1)*100
def average_20(dat):
    moving = dat['adj_close'].rolling(window=21,center=False).mean()
    return moving
def beta(dat):
    ret_price = (dat['adj_close']/(dat['adj_close'].shift(1))-1)*100
    ret_sp = (dat['sp_adj_close']/(dat['sp_adj_close'].shift(1))-1)*100
    beta = (ret_price.rolling(window=252,center=False).cov(ret_sp))/(ret_sp.rolling(window=252,center=False).var())
    return beta
feature_dic = {'pe':pe,
               'price_to_book_value':price_to_book_value,
               'ps':ps,
               '20mean':average_20,
               'return':daily_return,
               'beta':beta}
```

### It will return an index with all the column names in the dataset


```python
reader.feature(feature_dic)
```




    Index(['date', 'adj_close', 'adj_volume', 'Sentiment', 'News Volume',
           'News Buzz', 'tic', 'ceql', 'csho', 'ni', 'sale', 'sp_adj_close',
           'sp_volume', 'pe', 'price_to_book_value', 'ps', '20mean', 'return',
           'beta'],
          dtype='object')



## Trim the dataset
- You can select out the features which you want to put in the final dataset by calling trim()


```python
feature_list = ['date','adj_close','pe','price_to_book_value','ps','20mean','beta','return']
```

### It will return an index contains all the features which will appear in your final dataset


```python
reader.trim(feature_list)
```

    Index(['date', 'adj_close', 'pe', 'price_to_book_value', 'ps', '20mean',
           'beta', 'return'],
          dtype='object')



```python
reader.table.iloc[-5:,:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>adj_close</th>
      <th>pe</th>
      <th>price_to_book_value</th>
      <th>ps</th>
      <th>20mean</th>
      <th>beta</th>
      <th>return</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2863</th>
      <td>2016-12-23</td>
      <td>30.445183</td>
      <td>-25.621654</td>
      <td>2.119832</td>
      <td>1.925970</td>
      <td>28.752289</td>
      <td>1.470747</td>
      <td>1.992693</td>
    </tr>
    <tr>
      <th>2864</th>
      <td>2016-12-27</td>
      <td>31.674490</td>
      <td>-26.656199</td>
      <td>2.205426</td>
      <td>2.003736</td>
      <td>28.912797</td>
      <td>1.471948</td>
      <td>4.037773</td>
    </tr>
    <tr>
      <th>2865</th>
      <td>2016-12-28</td>
      <td>31.357249</td>
      <td>-26.389219</td>
      <td>2.183337</td>
      <td>1.983667</td>
      <td>29.075194</td>
      <td>1.473355</td>
      <td>-1.001565</td>
    </tr>
    <tr>
      <th>2866</th>
      <td>2016-12-29</td>
      <td>31.624921</td>
      <td>-26.614483</td>
      <td>2.201975</td>
      <td>2.000600</td>
      <td>29.286216</td>
      <td>1.462744</td>
      <td>0.853620</td>
    </tr>
    <tr>
      <th>2867</th>
      <td>2016-12-30</td>
      <td>31.208543</td>
      <td>-26.264073</td>
      <td>2.172983</td>
      <td>1.974260</td>
      <td>29.406125</td>
      <td>1.467886</td>
      <td>-1.316614</td>
    </tr>
  </tbody>
</table>
</div>



## The last step is to construct the dataset:
- There are two kinds of data structures: rolling data and un-rolling data
- With a time window of 4 days, rolling data contains data 4-days ago, un-rolling data contains data from yesterday to 4-days ago.


```python
# trim the dataset to make it more clear
reader.trim(['date','adj_close','pe'])
```

    Index(['date', 'adj_close', 'pe'], dtype='object')



```python
dat1 = reader.construct_data(rolling=False, time_window=5,thresh_date='2009-01-01')
```


```python
dat1.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>adj_close</th>
      <th>5day_adj_close</th>
      <th>5day_pe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>854</th>
      <td>2009-01-02</td>
      <td>9.415645</td>
      <td>8.095383</td>
      <td>0.572235</td>
    </tr>
    <tr>
      <th>855</th>
      <td>2009-01-05</td>
      <td>9.937079</td>
      <td>8.216524</td>
      <td>0.580798</td>
    </tr>
    <tr>
      <th>856</th>
      <td>2009-01-06</td>
      <td>9.703575</td>
      <td>8.198968</td>
      <td>0.579557</td>
    </tr>
    <tr>
      <th>857</th>
      <td>2009-01-07</td>
      <td>9.354197</td>
      <td>8.362245</td>
      <td>0.591098</td>
    </tr>
    <tr>
      <th>858</th>
      <td>2009-01-08</td>
      <td>9.598235</td>
      <td>8.630862</td>
      <td>0.610086</td>
    </tr>
  </tbody>
</table>
</div>




```python
dat2 = reader.construct_data(rolling=True,time_window = 3,thresh_date='2012-01-01')
dat2.head(8)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>adj_close</th>
      <th>1day_adj_close</th>
      <th>1day_pe</th>
      <th>2day_adj_close</th>
      <th>2day_pe</th>
      <th>3day_adj_close</th>
      <th>3day_pe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1610</th>
      <td>2012-01-03</td>
      <td>27.443501</td>
      <td>25.868011</td>
      <td>1.099475</td>
      <td>25.691371</td>
      <td>1.091967</td>
      <td>25.380912</td>
      <td>1.078771</td>
    </tr>
    <tr>
      <th>1611</th>
      <td>2012-01-04</td>
      <td>28.189317</td>
      <td>27.443501</td>
      <td>0.934492</td>
      <td>25.868011</td>
      <td>1.099475</td>
      <td>25.691371</td>
      <td>1.091967</td>
    </tr>
    <tr>
      <th>1612</th>
      <td>2012-01-05</td>
      <td>28.487286</td>
      <td>28.189317</td>
      <td>0.959888</td>
      <td>27.443501</td>
      <td>0.934492</td>
      <td>25.868011</td>
      <td>1.099475</td>
    </tr>
    <tr>
      <th>1613</th>
      <td>2012-01-06</td>
      <td>28.189317</td>
      <td>28.487286</td>
      <td>0.970035</td>
      <td>28.189317</td>
      <td>0.959888</td>
      <td>27.443501</td>
      <td>0.934492</td>
    </tr>
    <tr>
      <th>1614</th>
      <td>2012-01-09</td>
      <td>28.512265</td>
      <td>28.189317</td>
      <td>0.959888</td>
      <td>28.487286</td>
      <td>0.970035</td>
      <td>28.189317</td>
      <td>0.959888</td>
    </tr>
    <tr>
      <th>1615</th>
      <td>2012-01-10</td>
      <td>29.655968</td>
      <td>28.512265</td>
      <td>0.970885</td>
      <td>28.189317</td>
      <td>0.959888</td>
      <td>28.487286</td>
      <td>0.970035</td>
    </tr>
    <tr>
      <th>1616</th>
      <td>2012-01-11</td>
      <td>29.825471</td>
      <td>29.655968</td>
      <td>1.009830</td>
      <td>28.512265</td>
      <td>0.970885</td>
      <td>28.189317</td>
      <td>0.959888</td>
    </tr>
    <tr>
      <th>1617</th>
      <td>2012-01-12</td>
      <td>29.670242</td>
      <td>29.825471</td>
      <td>1.015602</td>
      <td>29.655968</td>
      <td>1.009830</td>
      <td>28.512265</td>
      <td>0.970885</td>
    </tr>
  </tbody>
</table>
</div>


