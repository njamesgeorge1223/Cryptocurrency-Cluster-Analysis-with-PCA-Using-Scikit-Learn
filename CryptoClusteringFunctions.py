#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  CryptoClusteringFunctions.py
 #
 #  File Description:
 #      This Python script, CryptoClusteringFunctions.py, contains generic 
 #      Python functions for completing common tasks in the CryptoClustering
 #      Challenge.  Here is the list:
 #
 #      ReturnOptimalKWithWCSSElbowFunction
 #      ReturnOptimalKWithCalinskiHarabaszFunction
 #      ReturnOptimalKWithSilhouetteFunction
 #      ReturnOptimalKWithDaviesBouldinFunction
 #
 #      ReturnSubplotTraceListFunction
 #      ReturnHeightWidthRowsColumnsFunction
 #      ReturnClusterPlotsFunction
 #      ReturnMaxRowAndColumnFunction
 #      
 #      ReturnClusterPredictionsFunction
 #      ReturnKClustersScatterPlotFunction
 #      ReturnKClusters3DScatterPlotFunction
 #      
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  11/21/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyConstants as constant
import PyLogSubRoutines as log_subroutine

import hvplot.pandas
import math

import pandas as pd
import plotly.graph_objects as go

from plotly.subplots import make_subplots
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import calinski_harabasz_score 
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score 


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'CryptoClusteringFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOptimalKWithWCSSElbowFunction
 #
 #  Function Description:
 #      This function returns an optimal k values using the WCSS Elbow Method.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          normalizedDataFrame
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnOptimalKWithWCSSElbowFunction \
        (normalizedDataFrame):
    
    try:
        
        # This line of code creates a List with the number of k-values from 1 to 11.
        kValueNumbersIntegerList \
            = list(range(2, 11))
    
        # This line of code creates a List to store the inertia values.
        inertiaFloatList \
            = []
    
        # This repetition loop computes the inertia with each possible value of k.
        for kValueNumberInteger in kValueNumbersIntegerList:
    
            # This line of code creates a KMeans model using the loop counter 
            # for the n_clusters.
            modelKMeansObject \
                = KMeans \
                    (n_clusters = kValueNumberInteger, 
                     random_state = 10, 
                     n_init = 100)

            # This line of code fits the model to the data using the normalized
            # cryptocurrency DataFrame.
            modelKMeansObject \
                .fit \
                    (normalizedDataFrame)
    
            # This line of code appends the model.inertia_ to the inertia List.
            inertiaFloatList \
                .append \
                    (modelKMeansObject.inertia_)
    

        inertiaFloatSeries \
            = pd.Series \
                (inertiaFloatList, 
                 index = kValueNumbersIntegerList, 
                 name = 'Wcss Elbow')

        
        inertiaIndexIntegerList \
            = list \
                (inertiaFloatSeries.index)
        
        percentVarianceFloatList \
            = []

        for numberKValues in inertiaIndexIntegerList:
        
            percentVarianceFloatList \
                .append \
                    (100 \
                     * (1 - (inertiaFloatSeries[numberKValues] \
                             / inertiaFloatSeries[inertiaIndexIntegerList[0]])))
    
    
        thresholdInteger \
            = len(percentVarianceFloatList) + 1

        optimalKInteger = 0
            
        for index in range(1, thresholdInteger):
                
            if abs(percentVarianceFloatList[index] \
                   - percentVarianceFloatList[index - 1]) \
                < thresholdInteger:
                
                optimalKInteger = index + 1
                    
                break
                
                
        return optimalKInteger, inertiaFloatSeries
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnOptimalKWithWCSSElbowFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return an optimal k value.')
    
        return \
            None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOptimalKWithCalinskiHarabaszFunction
 #
 #  Function Description:
 #      This function returns an optimal k values using the Calinski-Harabasz Method.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          normalizedDataFrame
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnOptimalKWithCalinskiHarabaszFunction \
        (normalizedDataFrame):
    
    try:
        
        # This line of code creates a List with the number of k-values from 1 to 11.
        kValueNumbersIntegerList \
            = list(range(2, 11))
    
        # This line of code creates an empty List to store the inertia values.
        inertiaFloatList \
            = []
    
        # This repetition loop computes the inertia with each possible value of k.
        for kValueNumberInteger in kValueNumbersIntegerList:
    
            # This line of code creates a KMeans model using the loop counter 
            # for the n_clusters.
            modelKMeansObject \
                = KMeans \
                    (n_clusters = kValueNumberInteger, 
                     random_state = 10, 
                     n_init = 100)

            # This line of code fits the model to the data using the normalized
            # cryptocurrency DataFrame.
            modelKMeansObject \
                .fit \
                    (normalizedDataFrame)
    
            # This line of code appends the model.inertia_ to the inertia List.
            inertiaFloatList \
                .append \
                    (calinski_harabasz_score \
                         (normalizedDataFrame,
                          modelKMeansObject.labels_))
    

        inertiaFloatSeries \
            = pd.Series \
                (inertiaFloatList, 
                 index = kValueNumbersIntegerList, 
                 name = 'Calinski Harabasz')

        optimalKInteger \
            = inertiaFloatSeries.idxmax()
       
        
        return optimalKInteger, inertiaFloatSeries
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnOptimalKWithCalinskiHarabaszFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return an optimal k value.')
    
        return \
            None        


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOptimalKWithSilhouetteFunction
 #
 #  Function Description:
 #      This function returns an optimal k values using the Silhouette Method.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          normalizedDataFrame
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnOptimalKWithSilhouetteFunction \
        (normalizedDataFrame):
    
    try:
        
        # This line of code creates a List with the number of k-values from 1 to 11.
        kValueNumbersIntegerList \
            = list(range(2, 11))
    
        # This line of code creates an empty List to store the inertia values.
        inertiaFloatList \
            = []
    
        # This repetition loop computes the inertia with each possible value of k.
        for kValueNumberInteger in kValueNumbersIntegerList:
    
            # This line of code creates a KMeans model using the loop counter 
            # for the n_clusters.
            modelKMeansObject \
                = KMeans \
                    (n_clusters = kValueNumberInteger, 
                     random_state = 10, 
                     n_init = 100)

            # This line of code fits the model to the data using the normalized
            # cryptocurrency DataFrame.
            modelKMeansObject \
                .fit \
                    (normalizedDataFrame)
    
            # This line of code appends the model.inertia_ to the inertia List.
            inertiaFloatList \
                .append \
                    (silhouette_score \
                         (normalizedDataFrame,
                          modelKMeansObject.labels_))
    

        inertiaFloatSeries \
            = pd.Series \
                (inertiaFloatList, 
                 index = kValueNumbersIntegerList, 
                 name = 'Silhouette')

        pointFloat \
            = inertiaFloatSeries.max()
    
        optimalKInteger \
            = inertiaFloatSeries \
                .index \
                    [inertiaFloatSeries == pointFloat][0]
    
            
        return optimalKInteger, inertiaFloatSeries
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnOptimalKWithSilhouetteFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return an optimal k value.')
    
        return \
            None 


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnOptimalKWithDaviesBouldinFunction
 #
 #  Function Description:
 #      This function returns an optimal k values using the Davies-Bouldin Method.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          normalizedDataFrame
 #                          The parameter is the normalized input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/21/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnOptimalKWithDaviesBouldinFunction \
        (normalizedDataFrame):
    
    try:
    
        # This line of code creates a List with the number of k-values from 1 to 11.
        kValueNumbersIntegerList \
            = list(range(2, 11))
    
        # This line of code creates an empty List to store the inertia values.
        inertiaFloatList \
            = []
    
        # This repetition loop computes the inertia with each possible value of k.
        for kValueNumberInteger in kValueNumbersIntegerList:
    
            # This line of code creates a KMeans model using the loop counter 
            # for the n_clusters.
            modelKMeansObject \
                = KMeans \
                    (n_clusters = kValueNumberInteger, 
                     random_state = 10, 
                     n_init = 100)

            # This line of code fits the model to the data using the normalized
            # cryptocurrency DataFrame.
            modelKMeansObject \
                .fit \
                    (normalizedDataFrame)
    
            # This line of code appends the model.inertia_ to the inertia List.
            inertiaFloatList \
                .append \
                    (silhouette_score \
                         (normalizedDataFrame,
                          modelKMeansObject.labels_))
        

        inertiaFloatSeries \
            = pd.Series \
                (inertiaFloatList, 
                 index = kValueNumbersIntegerList, 
                 name = 'Davies Bouldin')

    
        optimalKInteger \
            = inertiaFloatSeries.idxmax()
    
            
        return optimalKInteger, inertiaFloatSeries
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnOptimalKWithDaviesBouldinFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return an optimal k value.')
    
        return \
            None  


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnSubplotTraceListFunction
 #
 #  Function Description:
 #      This function returns a subplot trace list for display.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          inertiaFloatSeriesList
 #                          The parameter is a List of inertia values in Series.
 #  List
 #          lineColorsStringList
 #                          The parameter is a List of colors for the lines.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/22/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnSubplotTraceListFunction \
        (inertiaFloatSeriesList,
         lineColorsStringList):
    
    try:
    
        subplotsTraceList \
            = []
    
    
        for index, inertia in enumerate(inertiaFloatSeriesList):
    
            lineTraceObject \
                = go.Scatter \
                    (x = inertia.index, 
                     y = inertia,
                     line = {'color': \
                                 lineColorsStringList \
                                    [index % len(lineColorsStringList)]},
                     mode = 'lines')

            markerTraceObject \
                = go.Scatter \
                    (x = inertia.index, 
                     y = inertia,
                     hovertemplate \
                        = 'Number of K-Clusters: <b>%{x}</b><br>'
                            + 'Score: <b>%{y}</b><br>'
                            + '<extra></extra>',
                     marker \
                         = {'color': 'darkblue',
                            'size': 10},
                     mode = 'markers')
        
            plotTraceList \
                = [lineTraceObject, 
                   markerTraceObject]
        
            subplotsTraceList \
                .append \
                    (plotTraceList)
        
        
        return subplotsTraceList
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnSubplotTraceListFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a subplot trace list.')
    
        return \
            None          


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnHeightWidthRowsColumnsFunction
 #
 #  Function Description:
 #      This function returns the height, width, rows, and columns from a list of k-values
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          optimalKIntegerList
 #                          The parameter is a List of optimal K values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/22/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnHeightWidthRowsColumnsFunction \
        (optimalKIntegerList):
        
    try:
        
        if len(optimalKIntegerList) == 1:
            
            heightInteger = 500
            
            widthInteger = 500
            
            rowsInteger = 1
            
            columnsInteger = 1
            
        elif len(optimalKIntegerList) == 2:
            
            heightInteger = 500
            
            widthInteger = 1000
            
            rowsInteger = 1
            
            columnsInteger = 2
            
        elif len(optimalKIntegerList) == 3:
            
            heightInteger = 500
            
            widthInteger = 1500
            
            rowsInteger = 1
            
            columnsInteger = 3   
            
        elif len(optimalKIntegerList) == 4:
            
            heightInteger = 1000
            
            widthInteger = 1000
            
            rowsInteger = 2
            
            columnsInteger = 2 
        
        else:
            
            heightInteger = None
            
            widthInteger = None
            
            rowsInteger = None
            
            columnsInteger = None
            
        
        return heightInteger, widthInteger, rowsInteger, columnsInteger
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnHeightWidthRowsColumnsFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return height, width, rows, and columns.')
    
        return \
            None            


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnClusterPlotsFunction
 #
 #  Function Description:
 #      This function returns a group of k-cluster line plots for display.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          optimalKIntegerList
 #                          The parameter is a List of optimal K values.
 #  List
 #          inertiaFloatSeriesList
 #                          The parameter is a List of inertia values in Series.
 #  List
 #          lineColorsStringList
 #                          The parameter is a List of colors for the lines.
 #  String
 #          figureTitleString
 #                          The parameter is a figure title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/22/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnClusterPlotsFunction \
        (optimalKIntegerList, 
         inertiaFloatSeriesList, 
         lineColorsStringList,
         figureTitleString):
    
    try:
        
        heightInteger, widthInteger, rowsInteger, columnsInteger \
            = ReturnHeightWidthRowsColumnsFunction \
                (optimalKIntegerList)
        
        if heightInteger == None:
            
            return None
        
        
        subplotsTraceList \
            = ReturnSubplotTraceListFunction \
                (inertiaFloatSeriesList,
                 lineColorsStringList)

        titlesStringList \
            = [n.name for n in inertiaFloatSeriesList]

        layoutObject \
            = go.Layout \
                (height = heightInteger,
                 width = widthInteger,
                 title_text = figureTitleString)

        figureObject \
            = make_subplots \
                (rows = rowsInteger, 
                 cols = columnsInteger, 
                 horizontal_spacing = 0.12,
                 vertical_spacing = 0.12,
                 subplot_titles = titlesStringList)
    
    
        for index, subplot in enumerate(subplotsTraceList):
        
                            
            if index < 2:
                    
                rowInteger = 1
                    
                columnInteger = index + 1
                
            else:
                
                rowInteger = 2
                
                columnInteger = index - 1
                
        
            for trace in subplot:
        
                figureObject.add_trace \
                    (trace, 
                     row = rowInteger, 
                     col = columnInteger)
            
                figureObject.update_annotations \
                    (font \
                         = {'color': 'black', 
                            'family': 'garamond',
                            'size': 20.0},
                     yshift = 10.0)
            
                figureObject.update_xaxes \
                    (row = rowInteger, 
                     col = columnInteger,
                     tick0 = 1.0,
                     dtick = 1.0,
                     tickmode = 'linear',
                     linecolor = 'black',
                     linewidth = 2.0,
                     mirror = True,
                     showline = True,
                     tickfont \
                         = {'color': 'black',
                            'family': 'garamond',
                            'size': 14.0})
            
                figureObject.update_yaxes \
                    (row = rowInteger, 
                     col = columnInteger,
                     linecolor = 'black',
                     linewidth = 2.0, 
                     mirror = True, 
                     showline = True, 
                     tickfont \
                         = {'color': 'black',
                            'family': 'garamond',
                            'size': 14.0})
            
            if index > 1:
                
                figureObject.update_xaxes \
                    (row = rowInteger, 
                     col = columnInteger,
                     title \
                         = {'text': 'Number of K-Clusters',
                            'font': {'color': 'black', 
                                     'family': 'garamond',
                                     'size': 18.0}})                
            
            if index % 2 == 0:
            
                figureObject.update_yaxes \
                    (row = rowInteger, 
                     col = columnInteger,
                     title \
                         = {'text': 'Score',
                            'font': {'color': 'black', 
                                     'family': 'garamond',
                                     'size': 18.0}})
            
            figureObject.add_vline \
                (row = rowInteger, 
                 col = columnInteger,
                 x = optimalKIntegerList[index],
                 line_color = 'black',
                 line_dash = 'dash',
                 line_width = 2.0)
            

        figureObject.update_layout \
            (layoutObject,
             showlegend = False, 
             title \
                 = {'font': \
                        {'color': 'black', 
                         'family': 'garamond', 
                         'size': 24.0}}) 

        log_subroutine \
            .SavePlotlyImage \
                (figureObject,
                 figureTitleString)
    
        return figureObject.show()
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnClusterPlotsFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return cluster plots for display.')
    
        return \
            None             


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnMaxRowAndColumnFunction
 #
 #  Function Description:
 #      This function returns the number of rows and columns for a Plotly figure.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          kValueIntegerList
 #                          The parameter is a List of optimal K values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/22/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnMaxRowAndColumnFunction \
        (kValueIntegerList):
    
    try:
        
        if len(kValueIntegerList) <= 3 \
            or len(kValueIntegerList) == 5 \
            or len(kValueIntegerList) == 7:
        
            return 1, len(kValueIntegerList)
        
        elif len(kValueIntegerList) == 4 \
                or len(kValueIntegerList) == 9:
        
            return int(math.sqrt(len(kValueIntegerList))), \
                   int(math.sqrt(len(kValueIntegerList)))
        
        elif len(kValueIntegerList) == 6:
            
            return 2, 3
        
        elif len(kValueIntegerList) == 8:
        
            return 2, 4
        
        else:
        
            return None, None
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnMaxRowAndColumnFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return the maximum rows and columns.')
    
        return None, None  


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnClusterPredictionsFunction
 #
 #  Function Description:
 #      This function returns a k-means cluster predictions.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          normalizedDataFrame
 #                          The parameter is a DataFrame of normalized values.
 #  List
 #          kValueIntegerList
 #                          The parameter is a List of optimal K values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/22/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnClusterPredictionsFunction \
        (normalizedDataFrame,
         kValueIntegerList):
    
    try:
        
        predictionsIntegerListList \
            = []
        
        for kValue in kValueIntegerList:
        
            modelKMeansObject \
                = KMeans \
                    (n_clusters = kValue, 
                     n_init = 100, 
                     random_state = 10)
        
            modelKMeansObject.fit \
                (normalizedDataFrame)
    
            clusterValuesPredictionIntegerList \
                = modelKMeansObject.predict \
                    (normalizedDataFrame)
        
            predictionsIntegerListList \
                .append \
                    (clusterValuesPredictionIntegerList)
        
        
        return predictionsIntegerListList
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnClusterPredictionsFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return the k-means cluster predictions.')
    
        return None


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnKClustersScatterPlotFunction
 #
 #  Function Description:
 #      This function returns a group of k-cluster scatter plots for display.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          normalizedDataFrame
 #                          The parameter is a DataFrame of normalized values.
 #  List
 #          kValueIntegerList
 #                          The parameter is a List of optimal K values.
 #  List
 #          colorsStringList
 #                          The parameter is a List of colors for the plots.
 #  String
 #          figureTitleString
 #                          The parameter is a figure title.
 #  String
 #          xAxisNameString
 #                          The parameter is a DataFrame column name for the x-axis.
 #  String
 #          yAxisNameString
 #                          The parameter is a DataFrame column name for the y-axis.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/22/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnKClustersScatterPlotFunction \
        (normalizedDataFrame,
         kValueIntegerList, 
         colorsStringList,
         figureTitleString,
         xAxisNameString, 
         yAxisNameString):
    
    try:
    
        titlesStringList \
            = [f'K-Clusters for K = {n}' for n in kValueIntegerList]

    
        maxRowsInteger, maxColumnsInteger \
            = ReturnMaxRowAndColumnFunction \
                (kValueIntegerList)
    
        if maxRowsInteger == None:
        
            return
    
    
        layoutObject \
            = go.Layout \
                (height = 500 * maxRowsInteger,
                 width = 500 * maxColumnsInteger,
                 title_text = figureTitleString)
    
        figureObject \
            = make_subplots \
                (rows = maxRowsInteger, 
                 cols = maxColumnsInteger, 
                 horizontal_spacing = 0.12,
                 vertical_spacing = 0.12,
                 subplot_titles = titlesStringList)
    
        indexInteger = 0
    
        for rowInteger in range(1, maxRowsInteger+1):
        
            for columnInteger in range(1, maxColumnsInteger+1):
            
                modelKMeansObject \
                    = KMeans \
                        (n_clusters = kValueIntegerList[indexInteger], 
                         n_init = 100, 
                         random_state = 10)
    
                modelKMeansObject.fit \
                    (normalizedDataFrame)
    
                clusterCentersDataFrame \
                    = pd.DataFrame \
                        (modelKMeansObject.cluster_centers_, 
                         columns = normalizedDataFrame.columns)
    
    
                tracePointsScatterObject \
                    = go.Scatter \
                        (x = normalizedDataFrame[xAxisNameString],
                         y = normalizedDataFrame[yAxisNameString],
                         name = 'Points',
                         mode = 'markers',
                         marker \
                            = {'color': modelKMeansObject.labels_,
                               'colorscale': colorsStringList,
                               'line': {'color': 'black',
                                        'width': 1.0},
                               'opacity': 1.0,
                               'size': 10.0},
                         text = normalizedDataFrame.index,
                         hovertemplate \
                            = '<b>Cryptocurrency:</b> %{text}<br>'
                                + '<b>x:</b> %{x}<br>'
                                + '<b>y:</b> %{y}<br>'
                                + '<extra></extra>',
                         showlegend = False)

                traceClustersScatterObject \
                    = go.Scatter \
                        (x = clusterCentersDataFrame[xAxisNameString],
                         y = clusterCentersDataFrame[yAxisNameString],
                         name = 'Clusters',
                         mode = 'markers',
                         marker \
                             = {'size': 50.0,
                                'color': clusterCentersDataFrame.index,
                                'colorscale': colorsStringList,
                                'opacity': 0.4,
                                'line': {'color': 'black',
                                         'width': 1.5}},
                        text = [f'{n+1}' for n in range(len(clusterCentersDataFrame))],
                        hovertemplate \
                            = '<b>Cluster %{text}</b><br>'
                                + '<b>x:</b> %{x}<br>'
                                + '<b>y:</b> %{y}<br>'
                                + '<extra></extra>',
                        showlegend = False)
        
        
                plotTraceList \
                    = [tracePointsScatterObject, 
                       traceClustersScatterObject]
    
                for trace in plotTraceList:
            
                    figureObject.add_trace \
                        (trace, 
                         row = rowInteger, 
                         col = columnInteger)
            
            
                figureObject.update_annotations \
                    (font \
                        = {'color': 'black', 
                           'family': 'garamond',
                           'size': 20.0},
                     yshift = 10.0)
    
                figureObject.update_xaxes \
                    (row = rowInteger, 
                     col = columnInteger,
                     linecolor = 'black',
                     linewidth = 2.0,
                     mirror = True,
                     showline = True,
                     tickfont \
                        = {'color': 'black',
                           'family': 'garamond',
                           'size': 14.0})
            
                figureObject.update_yaxes \
                    (row = rowInteger, 
                     col = columnInteger,
                     linecolor = 'black',
                     linewidth = 2.0, 
                     mirror = True, 
                     showline = True, 
                     tickfont \
                        = {'color': 'black',
                           'family': 'garamond',
                           'size': 14.0})
                
                if rowInteger == maxRowsInteger:
                    
                    figureObject.update_xaxes \
                        (row = rowInteger, 
                         col = columnInteger,
                         title = xAxisNameString.replace('_', ' ').title(),
                         titlefont = {'color': 'black', 
                                      'family': 'garamond',
                                      'size': 18.0}) 
                
                if columnInteger == 1:
            
                    figureObject.update_yaxes \
                        (row = rowInteger, 
                         col = columnInteger,
                         title = yAxisNameString.replace('_', ' ').title(),
                         titlefont = {'color': 'black', 
                                      'family': 'garamond',
                                      'size': 18.0})
                
                
                indexInteger += 1
        
        
        figureObject.update_layout \
            (layoutObject,
             showlegend = True, 
             title \
                = {'font': \
                    {'color': 'black', 
                     'family': 'garamond', 
                     'size': 24.0}})
    
    
        log_subroutine \
            .SavePlotlyImage \
                (figureObject,
                 figureTitleString)
    
        
        return figureObject.show()
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnKClustersScatterPlotFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a K-Clusters scatter plot for display.')
    
        return None  


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnKClusters3DScatterPlotFunction
 #
 #  Function Description:
 #      This function returns a group of 3-D k-cluster scatter plots for display.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          normalizedDataFrame
 #                          The parameter is a DataFrame of normalized values.
 #  List
 #          kValueInteger
 #                          The parameter is an optimal k value.
 #  List
 #          colorsStringList
 #                          The parameter is a List of colors for the plots.
 #  String
 #          figureTitleString
 #                          The parameter is a figure title.
 #  List
 #          columnNamesStringList
 #                          The parameter is a List of DataFrame column names 
 #                          for dimensions.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  11/22/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnKClusters3DScatterPlotFunction \
        (normalizedDataFrame, 
         kValueInteger, 
         colorsStringList,
         figureTitleString,
         columnNamesStringList):
    
    try:
    
        modelKMeansObject \
            = KMeans \
                (n_clusters = kValueInteger, 
                 n_init = 100, 
                 random_state = 10)
    
        modelKMeansObject.fit \
            (normalizedDataFrame)
    
        clusterCentersDataFrame \
            = pd.DataFrame \
                (modelKMeansObject.cluster_centers_, 
                 columns = normalizedDataFrame.columns)
    

        tracePointsScatterObject \
            = go.Scatter3d \
                (x = normalizedDataFrame[columnNamesStringList[0]],
                 y = normalizedDataFrame[columnNamesStringList[1]],
                 z = normalizedDataFrame[columnNamesStringList[2]],
                 name = 'Points',
                 mode = 'markers',
                 marker \
                    = {'color': modelKMeansObject.labels_,
                       'colorscale': colorsStringList,
                       'line': {'color': 'black',
                                'width': 1.0},
                       'opacity': 1.0,
                       'size': 7.0},
                 text = normalizedDataFrame.index,
                 hovertemplate \
                    = '<b>Cryptocurrency:</b> %{text}<br>'
                        + '<b>x:</b> %{x}<br>'
                        + '<b>y:</b> %{y}<br>'
                        + '<b>z:</b> %{z}<br>'
                        + '<extra></extra>',
                 showlegend = True)   
    
        traceClustersScatterObject \
            = go.Scatter3d \
                (x = clusterCentersDataFrame[columnNamesStringList[0]],
                 y = clusterCentersDataFrame[columnNamesStringList[1]],
                 z = clusterCentersDataFrame[columnNamesStringList[2]],
                 name = 'Clusters',
                 mode = 'markers',
                 marker \
                    = {'size': 42.0,
                       'color': clusterCentersDataFrame.index,
                       'colorscale': colorsStringList,
                       'opacity': 0.4,
                       'line': {'color': 'black',
                                'width': 1.5}},
                 text = [f'{n+1}' for n in range(len(clusterCentersDataFrame))],
                 hovertemplate \
                    = '<b>Cluster %{text}</b><br>'
                        + '<b>x:</b> %{x}<br>'
                        + '<b>y:</b> %{y}<br>'
                        + '<b>z:</b> %{z}<br>'
                        + '<extra></extra>',
                 showlegend = True)
    
    
        layoutObject \
            = go.Layout \
                (height = 900,
                 width = 900,
                 title \
                     = {'x': 0.5,
                        'y': 0.85,
                        'text': figureTitleString,
                        'font': {'color': 'black', 
                                 'family': 'garamond', 
                                 'size': 28.0}},
                 scene \
                     = {'aspectmode': 'manual',
                        'aspectratio': {'x': 0.9, 'y': 0.9, 'z': 0.9},
                        'xaxis': \
                            {'title': {'text': columnNamesStringList[0],
                                       'font': {'color': 'black', 
                                                'family': 'garamond', 
                                                'size': 18.0}},
                             'color': 'black',
                             'gridcolor': 'darkblue',
                             'linecolor': 'black',
                             'linewidth': 2.0,
                             'mirror': True,
                             'showbackground': True,
                             'showline': True,
                             'tickfont': {'color': 'black', 
                                          'family': 'garamond', 
                                          'size': 14}},
                        'yaxis': \
                            {'title': {'text': columnNamesStringList[1],
                                       'font': {'color': 'black', 
                                                'family': 'garamond', 
                                                'size': 18.0}},
                             'color': 'black',
                             'gridcolor': 'darkblue',
                             'linecolor': 'black',
                             'linewidth': 2.0,
                             'mirror': True,
                             'showbackground': True,
                             'showline': True,
                             'tickfont': {'color': 'black', 
                                          'family': 'garamond', 
                                          'size': 14}},
                        'zaxis': \
                            {'title': {'text': columnNamesStringList[2],
                                       'font': {'color': 'black', 
                                                'family': 'garamond', 
                                                'size': 18.0}},
                             'color': 'black',
                             'gridcolor': 'darkblue',
                             'linecolor': 'black',
                             'linewidth': 2.0,
                             'mirror': True,
                             'showbackground': True,
                             'showline': True,
                             'tickfont': {'color': 'black', 
                                          'family': 'garamond', 
                                          'size': 14.0}}},
                 legend \
                     = {'x': 1.2,
                        'y': 0.8,
                        'xanchor': 'right',
                        'yanchor': 'top',
                        'bgcolor': 'aliceblue',
                        'font': {'color': 'black', 
                                 'family': 'garamond', 
                                 'size': 20.0}})

        figureObject \
            = go.Figure \
                (data = [tracePointsScatterObject, traceClustersScatterObject], 
                 layout = layoutObject)
    
    
        return figureObject.show()
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnKClusters3DScatterPlotFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a 3D K-Clusters scatter plot for display.')
    
        return None


# In[ ]:




