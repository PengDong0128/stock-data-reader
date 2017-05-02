
# External Data Sample

## To import external data successfully, you must make the dataset in a specific format


```python
import pandas as pd
dat = pd.read_csv('/Users/pengdong/Desktop/datareader/basic_stats.csv')
```

## In the dataset, there should be two key indicators. One is for 'time' , the other is for 'ticker'. In the dataset, there must be a column 'tic' which stores tickers for the stocks. For the indicator 'time' ,if the dataset is anual, please set them as 'fyear', if the dataset is daily, please set them as 'date'. Here is an example for anual data.


```python
dat.head(5)
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




```python

```
