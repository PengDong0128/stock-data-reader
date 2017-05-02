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
## For using this module , you must have an API Key for quandl.com. You just need to sign up on the webpage and find API Key in your account setting. If you want to use sentiment data , you have to subscribe "FinSentS Web News Sentiment", the link is https://www.quandl.com/data/NS1-FinSentS-Web-News-Sentiment .
### Import the module and initialize it:
### Python Version: v3.6

```python
from stock_data_reader import StockDataReader
reader = StockDataReader("your_api_key")
```
### Other details could be found in the instruction.
