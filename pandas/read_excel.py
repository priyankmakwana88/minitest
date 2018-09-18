#!/usr/bin/env python3

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#setting up file to read
exl_file='movies.xls'

#M1
'''
#reading file	    file_name- sheet_name-  Col we want as index
movies1=pd.read_excel(exl_file, sheet_name=0,index_col=0)
movies2=pd.read_excel(exl_file, sheet_name=1,index_col=0)
movies3=pd.read_excel(exl_file, sheet_name=2,index_col=0)


#head without arguments will show top 5 lines
#print(movies3.head())

#combining all 3 dataframes created above
movies=pd.concat([movies1,movies2,movies3])

print(movies.shape)
'''

#M2 for large data
'''
xlsx=pd.ExcelFile(exl_file)
movies_sheets=[]

for sheet in xlsx.sheet_names:
	movies_sheets.append(xlsx.parse(sheet))

movies=pd.concat(movies_sheets)

#print(movies.shape)
#print(movies.tail())

#TO SORT DATA
sorted_by_gross=movies.sort_values(['Gross Earnings'], ascending=False)

#TO PLOT GRAPHICAL VIEW
#sorted_by_gross["Gross Earnings"].head().plot(kind='barh')
#sorted_by_gross["IMDB Score"].plot(kind='hist')
#plt.show()

#To calculate stat. data
#print(movies.describe())
'''

#TO NOT READ HEADERS BY DEFAULT AND SKIP ROWS

#movies_skip_rows=pd.read_excel("movies.xls",header=None, skiprows=4) #skip_footer skip rows from bottom
#print(movies_skip_rows.head())

#reading subset of column
movies_subset_column=pd.read_excel('movies.xls',usecols=6)
#print(movies_subset_column.head())

#CREATE NEW COLUMN FROM EXISTING VALUES
movies=pd.read_excel('movies.xls')

movies["Net Earning"]=movies["Gross Earnings"]-movies["Budget"]
sorted_movies=movies[["Net Earning"]].sort_values(["Net Earning"],ascending=False)
sorted_movies.head(10)["Net Earning"].plot.barh()
plt.show()

#EXPORTING RESULT TO EXCEL
movies.to_excel("output.xls")


