# **Project 1, Oil Energy Sector Analysis**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: yfinance, yahoo_fin, holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install yfinance

python3 -m pip install yahoo_fin

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

----

### **Usage:**

----

The IPython notebook, PyOilSectorAnalyis.ipynb, requires the following Python scripts with it in the same folder:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PyOilSectorAnalysisAPIFunctions.py

PyOilSectorAnalysisConfig.py

PyOilSectorAnalysisConstants.py

PyOilSectorAnalysisFunctions.py

PySubroutines.py

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.  If the CSV file, AllOilCompanies.csv, is not present in the Resources folder, the program will use APIs to generate the CSV file.  Without the CSV file, execution time is an hour; with it, execution time is approximately 1.5 minutes.

To place the IPython notebook in Log Mode, Debug Mode, or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Debug Mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in Log Mode for log information sent to a log file. If the program is in Log Mode but NOT Debug Mode, it displays no debug information, but writes that information to the log file. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG files in the Images Folder.

----

### **Resource Summary:**

----

#### Source code

PyOilSectorAnalyis.ipynb, PyConstants.py, PyFunctions.py, PyLogConstants.py, PyLogFunctions.py, PyLogSubRoutines.py, PyOilSectorAnalysisAPIFunctions.py, PyOilSectorAnalysisConfig.py, PyOilSectorAnalysisConstants.py, PyOilSectorAnalysisFunctions.py, PySubroutines.py

#### Input files

AllOilCompanies.csv

#### Output files

AllOilCompanies.csv

#### SQL script

n/a

#### Software

Jupyter Notebook, Matplotlib, Numpy, Pandas, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./PyConstants.py](./PyConstants.py)

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PyOilSectorAnalysis.ipynb](./PyOilSectorAnalysis.ipynb)

|&rarr; [./PyOilSectorAnalysisAPIFunctions.py](./PyOilSectorAnalysisAPIFunctions.py)

|&rarr; [./PyOilSectorAnalysisConfig.py](./PyOilSectorAnalysisConfig.py)

|&rarr; [./PyOilSectorAnalysisConstants.py](./PyOilSectorAnalysisConstants.py)

|&rarr; [./PyOilSectorAnalysisFunctions.py](./PyOilSectorAnalysisFunctions.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./Table-Of-Contents-OESA.md](./Table-Of-Contents-OESA.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure111EconomicIndicatorPricesvsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure111EconomicIndicatorPricesvsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure112EconomicIndicatorPriceChangesvsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure112EconomicIndicatorPriceChangesvsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure121COVID19NewCasesandNewDeathsvsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure121COVID19NewCasesandNewDeathsvsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure122COVID19NewCasesvsNewDeathsScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure122COVID19NewCasesvsNewDeathsScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure123COVID19NewCasesandNewDeathsChangevsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure123COVID19NewCasesandNewDeathsChangevsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure124COVID19NewCasesvsNewDeathsChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure124COVID19NewCasesvsNewDeathsChangeScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure211OilIndustrySharefromNumberofCompanies.png](./Images/PyOilSectorAnalysisFigure211OilIndustrySharefromNumberofCompanies.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure212OilIndustrySharefromMarketCapitalizationMean.png](./Images/PyOilSectorAnalysisFigure212OilIndustrySharefromMarketCapitalizationMean.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure213OilIndustrySharefromMarketCapitalizationMedian.png](./Images/PyOilSectorAnalysisFigure213OilIndustrySharefromMarketCapitalizationMedian.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure214OilIndustryShareComparisonCompanyCountvsMean.png](./Images/PyOilSectorAnalysisFigure214OilIndustryShareComparisonCompanyCountvsMean.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure825MalevsFemaleMouseDistributionNaftisol.png](./Images/PymaceuticalsFigure825MalevsFemaleMouseDistributionNaftisol.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure215OilIndustryShareComparisonCompanyCountvsMedian.png](./Images/PyOilSectorAnalysisFigure215OilIndustryShareComparisonCompanyCountvsMedian.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure221OilIndustryMarketCapitalizationMeanSummaryStatistics.png](./Images/PyOilSectorAnalysisFigure221OilIndustryMarketCapitalizationMeanSummaryStatistics.png)
  
  &emsp; |&rarr; 
[./Images/PyOilSectorAnalysisFigure231OilIndustryMarketCapitalizationMedianSummaryStatistics.png](./Images/PyOilSectorAnalysisFigure231OilIndustryMarketCapitalizationMedianSummaryStatistics.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure241MarketCapitalizationStandardDeviationbyIndustryStatistics.png](./Images/PyOilSectorAnalysisFigure241MarketCapitalizationStandardDeviationbyIndustryStatistics.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure242OilIndustryMarketCapitalizationSEMSummaryStatistics.png](./Images/PyOilSectorAnalysisFigure242OilIndustryMarketCapitalizationSEMSummaryStatistics.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure251MarketCapitalizationDistributionsMeanMedianStdevSEM.png](./Images/PyOilSectorAnalysisFigure251MarketCapitalizationDistributionsMeanMedianStdevSEM.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure311OESIndexAllvsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure311OESIndexAllvsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure312OESAllIndexChangevsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure312OESAllIndexChangevsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure331OESTopIndexvsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure331OESTopIndexvsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure332OESTopIndexChangevsAnalysisPeriod.png](./Images/PyOilSectorAnalysisFigure332OESTopIndexChangevsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure342OESTopIndexvsOESAllIndexScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure342OESTopIndexvsOESAllIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure343OESTopIndexandOESAllIndexChange.png](./Images/PyOilSectorAnalysisFigure343OESTopIndexandOESAllIndexChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure345OESTopIndexvsOESAllIndexChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure345OESTopIndexvsOESAllIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure412CrudeOilPricesvsOESTopIndexScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure412CrudeOilPricesvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure413CrudeOilPricesandOESTopIndexChange.png](./Images/PyOilSectorAnalysisFigure413CrudeOilPricesandOESTopIndexChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure415CrudeOilPricesvsOESTopIndexChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure415CrudeOilPricesvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure421SP500andOESTopIndexTop.png](./Images/PyOilSectorAnalysisFigure421SP500andOESTopIndexTop.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure422SP500vsOESTopIndexScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure422SP500vsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure423SP500andOESTopIndexChange.png](./Images/PyOilSectorAnalysisFigure423SP500andOESTopIndexChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure425SP500vsOESTopIndexChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure425SP500vsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure431GoldandOESTopIndex.png](./Images/PyOilSectorAnalysisFigure431GoldandOESTopIndex.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure432GoldvsOESTopIndexScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure432GoldvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure433GoldandOESTopIndexChange.png](./Images/PyOilSectorAnalysisFigure433GoldandOESTopIndexChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure435GoldvsOESTopIndexChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure435GoldvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure451NewCOVID19CasesandOESTopIndex.png](./Images/PyOilSectorAnalysisFigure451NewCOVID19CasesandOESTopIndex.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure452NewCOVID19CasesvsOESTopIndexScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure452NewCOVID19CasesvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure453NewCOVID19CasesandOESTopIndexChange.png](./Images/PyOilSectorAnalysisFigure453NewCOVID19CasesandOESTopIndexChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure455NewCOVID19CasesvsOESTopIndexChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure455NewCOVID19CasesvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure461NewCOVID19DeathsandOESTopIndex.png](./Images/PyOilSectorAnalysisFigure461NewCOVID19DeathsandOESTopIndex.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure462NewCOVID19DeathsvsOESTopIndexScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure462NewCOVID19DeathsvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure463NewCOVID19DeathsandOESTopIndexChange.png](./Images/PyOilSectorAnalysisFigure463NewCOVID19DeathsandOESTopIndexChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure465NewCOVID19DeathsvsOESTopIndexChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure465NewCOVID19DeathsvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure3401AllCompaniesAmericasandEuropeMap.html](./Images/PyOilSectorAnalysisFigure3401AllCompaniesAmericasandEuropeMap.html)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure3401AllCompaniesWorldMap.html](./Images/PyOilSectorAnalysisFigure3401AllCompaniesWorldMap.html)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure3402TopCompaniesWorldMap.html](./Images/PyOilSectorAnalysisFigure3402TopCompaniesWorldMap.html)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure3403TopCompaniesAmericasandEuropeMap.html](./Images/PyOilSectorAnalysisFigure3403TopCompaniesAmericasandEuropeMap.html)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure44110YearBondYieldandOESTopIndex.png](./Images/PyOilSectorAnalysisFigure44110YearBondYieldandOESTopIndex.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure44210YearBondYieldvsOESTopIndexScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure44210YearBondYieldvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure44310YearBondYieldandOESTopIndexChange.png](./Images/PyOilSectorAnalysisFigure44310YearBondYieldandOESTopIndexChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisFigure44510YearBondYieldvsOESTopIndexChangeScatterPlotwRegression.png](./Images/PyOilSectorAnalysisFigure44510YearBondYieldvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable13USOilEnergySectorCompanies.png](./Images/PyOilSectorAnalysisTable13USOilEnergySectorCompanies.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable32TopCompanyinEachOilIndustryfromMarketCapitalizationMedian.png](./Images/PyOilSectorAnalysisTable32TopCompanyinEachOilIndustryfromMarketCapitalizationMedian.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable111EconomicIndicatorPrices.png](./Images/PyOilSectorAnalysisTable111EconomicIndicatorPrices.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable113EconomicIndicatorPricesChange.png](./Images/PyOilSectorAnalysisTable113EconomicIndicatorPricesChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable114EconomicIndicatorPricesChangeCorrelationMatrix.png](./Images/PyOilSectorAnalysisTable114EconomicIndicatorPricesChangeCorrelationMatrix.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable121COVID19CasesandDeathsDuringAnalysisPeriod.png](./Images/PyOilSectorAnalysisTable121COVID19CasesandDeathsDuringAnalysisPeriod.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable122COVID19NewCasesandNewDeathsChange.png](./Images/PyOilSectorAnalysisTable122COVID19NewCasesandNewDeathsChange.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable221OilCompanyMarketCapitalizationMetrics.png](./Images/PyOilSectorAnalysisTable221OilCompanyMarketCapitalizationMetrics.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable221OilIndustryMarketCapitalizationMeanSummaryStatistics.png](./Images/PyOilSectorAnalysisTable221OilIndustryMarketCapitalizationMeanSummaryStatistics.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable231OilIndustryMarketCapitalizationMedianSummaryStatistics.png](./Images/PyOilSectorAnalysisTable231OilIndustryMarketCapitalizationMedianSummaryStatistics.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable241MarketCapitalizationStandardDeviationbyIndustryStatistics.png](./Images/PyOilSectorAnalysisTable241MarketCapitalizationStandardDeviationbyIndustryStatistics.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable242OilIndustryMarketCapitalizationSEMSummaryStatistics.png](./Images/PyOilSectorAnalysisTable242OilIndustryMarketCapitalizationSEMSummaryStatistics.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable341OilEnergySectorIndices.png](./Images/PyOilSectorAnalysisTable341OilEnergySectorIndices.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable471AllMetricsCorrelationMatrix.png](./Images/PyOilSectorAnalysisTable471AllMetricsCorrelationMatrix.png)

  &emsp; |&rarr; [./Images/PyOilSectorAnalysisTable472AllMetricsChangeCorrelationMatrix.png](./Images/PyOilSectorAnalysisTable472AllMetricsChangeCorrelationMatrix.png)

  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20231107PyOilSectorAnalysisDebug.txt](./Logs/20231107PyOilSectorAnalysisDebug.txt)

  &emsp; |&rarr; [./Logs/20231107PyOilSectorAnalysisLog.txt](./Logs/20231107PyOilSectorAnalysisLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/AllOilCompanies.csv](./Resources/AllOilCompanies.csv)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
