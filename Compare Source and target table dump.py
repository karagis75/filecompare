
#python routine to compare columns in two different dataframes (Removes wanted space while comparing)
import pandas as pd
df = pd.read_csv('fullOCIR_BNM_HRC_REPORT_output0407-formattedv4.csv',dtype=str)
df2 = pd.read_csv('FullhighriskFinaloutput0407v2-formattedv4.csv',dtype=str)
dealddf = df2.dropna(how='all', axis='columns')
finaldf = df.dropna(how='all', axis='columns')
 
#copy 33 columns from BNM HRC report to so that comparision is easy
newFinaldf = finaldf.iloc[: , 0:33]    
newFinaldf.iloc[ : , 0 ]  
#newFinaldf.iloc[ : , 0 ].str.contains('CASA' , regex=False)
    
#no filter required since it is full population
#newFinaldeal = newFinaldf[newFinaldf.iloc[ : , 0].str.contains('CASA',regex=False)]
newFinaldeal = newFinaldf

#remove unwanted string spaces from dealddf
dealddf_obj = dealddf.select_dtypes(['object'])
dealddf[dealddf_obj.columns] = dealddf_obj.apply(lambda x: x.str.strip())

#remove unwanted string spaces from newFinaldeal
newFinaldeal_obj = newFinaldeal.select_dtypes(['object'])
newFinaldeal[newFinaldeal_obj.columns] = newFinaldeal_obj.apply(lambda x: x.str.strip())
#rename column name
newFinaldeal.rename(columns = {'ocir_bnm_hrc_report.relationshipno':'relationshipno',
                               'ocir_bnm_hrc_report.accountno':'accountno',
                               'ocir_bnm_hrc_report.loanrelation':'loanrelation'}, inplace = True) 



#sort ascending by account no both source and target table
newFinaldeal = newFinaldeal.sort_values(by=['accountno','relationshipno','loanrelation'], ascending=[True,True,True])
newFinaldeal
dealddf = dealddf.sort_values(by=['_u5.accountno','_u5.relationshipno','_u5.loanrelation'], ascending=[True,True,True])
dealddf

#print values after sorting for manual verification of logs
#result2 = newFinaldeal.values
#print(result2)
#result1 = dealddf.values
#print (result1)

#generate comparison report between source and target by matching column value by value
dealcomparedf =  dealddf.where(dealddf.values==newFinaldeal.values).notnull()
dealcomparedf.to_csv('Fulldatacomparewithfullbnmhrcreport.csv')
