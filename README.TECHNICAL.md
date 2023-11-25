# **Cryptocurrency Cluster Analysis with PCA Using Scikit-learn**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, plotly, sklearn.

Here are the requisite Terminal commands for the installation of these peripheral modules:

pip3 install -U holoviews

pip3 install -U hvplot

pip3 install -U geoviews

pip3 install -U geopy

pip3 install -U aspose-words

pip3 install -U dataframe-image

pip3 install -U scikit-learn

pip3 install -U plotly

----

### **Usage:**

----

The IPython notebook, CryptoClustering.ipynb, requires the following Python scripts with it in the same folder:

CryptoClusteringFunctions.py

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PySubroutines.py

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.  The IPython notebook, CryptoClustering.ipynb, needs the csv file, CryptoMarketData.csv, in the Resources folder to execute. To place the IPython notebook in Log Mode, Debug Mode, or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Debug Mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in Log Mode for log information sent to a log file. If the program is in Log Mode but NOT Debug Mode, it displays no debug information, but writes that information to the log file. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG and HTML files in the Images Folder.

----

### **Resource Summary:**

----

#### Source code

CryptoClustering.ipynb, CryptoClusteringFunctions.py, PyFunctions.py, PyLogConstants.py, PyLogFunctions.py, PyLogSubRoutines.py, PySubroutines.py

#### Input files

CryptoMarketData.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Matplotlib, Numpy, Pandas, Python 3.11.4, Plotly, scikit-learn

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./CryptoClustering.ipynb](./CryptoClustering.ipynb)

|&rarr; [./CryptoClusteringFunctions.py](./CryptoClusteringFunctions.py)

|&rarr; [./PyConstants.py](./PyConstants.py)

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/CryptoClustering221KMeansMethodsLinePlots.png](./Images/CryptoClustering221KMeansMethodsLinePlots.png)
  
  &emsp; |&rarr; [./Images/CryptoClustering331KMeansPriceChangeScatterPlots.png](./Images/CryptoClustering331KMeansPriceChangeScatterPlots.png)

  &emsp; |&rarr; [./Images/CryptoClustering341CryptocurrencyPriceChange3DScatterPlotk3.png](./Images/CryptoClustering341CryptocurrencyPriceChange3DScatterPlotk3.png)

  &emsp; |&rarr; [./Images/CryptoClustering342CryptocurrencyPriceChange3DScatterPlotk4.png](./Images/CryptoClustering342CryptocurrencyPriceChange3DScatterPlotk4.png)

  &emsp; |&rarr; [./Images/CryptoClustering343CryptocurrencyPriceChange3DScatterPlotk5.png](./Images/CryptoClustering343CryptocurrencyPriceChange3DScatterPlotk5.png)

  &emsp; |&rarr; [./Images/CryptoClustering344CryptocurrencyPriceChange3DScatterPlotk6.png](./Images/CryptoClustering344CryptocurrencyPriceChange3DScatterPlotk6.png)

  &emsp; |&rarr; [./Images/CryptoClustering521KMeansMethodswithPCADataLinePlots.png](./Images/CryptoClustering521KMeansMethodswithPCADataLinePlots.png)
  
  &emsp; |&rarr; [./Images/CryptoClustering631KMeansScatterPlotsPCA1vsPCA2.png](./Images/CryptoClustering631KMeansScatterPlotsPCA1vsPCA2.png)
  
  &emsp; |&rarr; [./Images/CryptoClustering632KMeansScatterPlotsPCA1vsPCA3.png](./Images/CryptoClustering632KMeansScatterPlotsPCA1vsPCA3.png)
  
  &emsp; |&rarr; [./Images/CryptoClustering633KMeansScatterPlotsPCA2vsPCA3.png](./Images/CryptoClustering633KMeansScatterPlotsPCA2vsPCA3.png)

  &emsp; |&rarr; [./Images/CryptoClustering641CryptocurrencyDataUsingPCA3DScatterPlotk3.png](./Images/CryptoClustering641CryptocurrencyDataUsingPCA3DScatterPlotk3.png)

  &emsp; |&rarr; [./Images/CryptoClustering641CryptocurrencyDataUsingPCA3DScatterPlotk6.png](./Images/CryptoClustering641CryptocurrencyDataUsingPCA3DScatterPlotk6.png)

  &emsp; |&rarr; [./Images/CryptoClustering642CryptocurrencyDataUsingPCA3DScatterPlotk4.png](./Images/CryptoClustering642CryptocurrencyDataUsingPCA3DScatterPlotk4.png)

  &emsp; |&rarr; [./Images/CryptoClustering643CryptocurrencyDataUsingPCA3DScatterPlotk5.png](./Images/CryptoClustering643CryptocurrencyDataUsingPCA3DScatterPlotk5.png)

  &emsp; |&rarr; [./Images/CryptoClustering711KMeansCryptocurrencyWCSSMethodLineK4.png](./Images/CryptoClustering711KMeansCryptocurrencyWCSSMethodLineK4.png)
  
  &emsp; |&rarr; [./Images/CryptoClustering712KMeansCryptocurrencywithPCAWCSSMethodLineK4.png](./Images/CryptoClustering712KMeansCryptocurrencywithPCAWCSSMethodLineK4.png)

  &emsp; |&rarr; [./Images/CryptoClustering721KMeansPriceChangeScatterK4.png](./Images/CryptoClustering721KMeansPriceChangeScatterK4.png)
  
  &emsp; |&rarr; [./Images/CryptoClustering722KMeansPriceChangewithPCAScatterPlotK4.png](./Images/CryptoClustering722KMeansPriceChangewithPCAScatterPlotK4.png)

  &emsp; |&rarr; [./Images/CryptoClustering731CryptocurrencyData3DScatterPlotK4.png](./Images/CryptoClustering731CryptocurrencyData3DScatterPlotK4.png)

  &emsp; |&rarr; [./Images/CryptoClustering731CryptocurrencyDatawithPCA3DScatterPlotK4.png](./Images/CryptoClustering731CryptocurrencyDatawithPCA3DScatterPlotK4.png)
  
  &emsp; |&rarr; [./Images/CryptoClusteringTable121CryptocurrenciesDataFrameTable.png](./Images/CryptoClusteringTable121CryptocurrenciesDataFrameTable.png)
  
  &emsp; |&rarr; [./Images/CryptoClusteringTable122CryptocurrenciesDataFrameSummaryStatistics.png](./Images/CryptoClusteringTable122CryptocurrenciesDataFrameSummaryStatistics.png)

  &emsp; |&rarr; [./Images/CryptoClusteringTable131NormalizedCryptocurrencyDataFrameTable.png](./Images/CryptoClusteringTable131NormalizedCryptocurrencyDataFrameTable.png)
  
  &emsp; |&rarr; 
[./Images/CryptoClusteringTable132NormalizedCryptocurrencyDataFrameSummaryStatistics.png](./Images/CryptoClusteringTable132NormalizedCryptocurrencyDataFrameSummaryStatistics.png)

  &emsp; |&rarr; [./Images/CryptoClusteringTable321NormalizedCryptocurrencywithPredictionsDataFrameTable.png](./Images/CryptoClusteringTable321NormalizedCryptocurrencywithPredictionsDataFrameTable.png)
  
  &emsp; |&rarr; [./Images/CryptoClusteringTable421CryptocurrenciesPCADataFrameTable.png](./Images/CryptoClusteringTable421CryptocurrenciesPCADataFrameTable.png)
  
  &emsp; |&rarr; [./Images/CryptoClusteringTable621CryptocurrencywithPredictionsUsingPCADataTable.png](./Images/CryptoClusteringTable621CryptocurrencywithPredictionsUsingPCADataTable.png)
  
  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20231123CryptoClusteringDebug.txt](./Logs/20231123CryptoClusteringDebug.txt)

  &emsp; |&rarr; [./Logs/20231123CryptoClusteringLog.txt](./Logs/20231123CryptoClusteringLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/CryptoMarketData.csv](./Resources/CryptoMarketData.csv)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

[Plotly Documentation](https://plotly.com/python/getting-started/)

[scikit-learn Documentation](https://scikit-learn.org/stable/)

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
