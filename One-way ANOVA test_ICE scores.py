import scipy
from scipy import stats
from scipy.stats import f_oneway
import pandas as pd
import arcpy

# decide which variables you need in your ANOVA test and store them under "fields"
fields= ['ICE_Score', 'SN_C' ]


# convert the fields to an array and name it array
array = arcpy.da.FeatureClassToNumPyArray("Justice40_Index of Concentration at the Extremes Score Layer", fields)


#convert array to a dataframe and call it df
df = pd.DataFrame(array, columns = ['ICE_Score','SN_C'])


# create two dataframes, one for Not disadtantaged, one for disadvantaged and named them as Not_DA and DA, respectively                
Not_DA, DA=[x for _, x in df.groupby(df['SN_C'])]


#drop missing values

# drop missing values and convert pandas dataframe to array for Not Disadvantaged
Not_Disadvantaged=Not_DA['ICE_Score'].dropna().to_numpy()


# drop missing values and convert pandas dataframe to array for Disadvantaged
Disadvantaged=DA['ICE_Score'].dropna().to_numpy()


#ANOVA TEST RUN

## One way anova needs each group ICE Score as an array. The code below shows the p value and the F Statistics for one way ANOVA
F, p = f_oneway(Not_Disadvantaged, Disadvantaged)

F

p
