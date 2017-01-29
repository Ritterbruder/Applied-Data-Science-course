import pandas as pd
import numpy as np

columns=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

energy=(pd.read_excel("Energy Indicators.xls"
                      ,skiprows=17
                      ,skip_footer=38
                      ,parse_cols=[2,3,4,5]
                      ,names=columns
                      ,na_values="...")
        
        .replace(to_replace=r"\d" , value="" , regex=True)
        .replace(to_replace=r" \(.*" , value="" , regex=True)
        #.replace(to_replace=r",.*" , value="" , regex=True)
        
       )

energy.replace(to_replace="Republic of Korea", value="South Korea", inplace=True)
energy.replace(to_replace="United States of America", value="United States", inplace=True)
energy.replace(to_replace="United Kingdom of Great Britain and Northern Ireland", value="United Kingdom", inplace=True)
energy.replace(to_replace="China, Hong Kong Special Administrative Region", value="Hong Kong", inplace=True)
      
energy["Energy Supply"]=1000000*energy["Energy Supply"]



GDP=pd.read_csv("world_bank.csv"
                ,header=4          
               )

GDP.replace(to_replace="Korea, Rep.", value="South Korea", inplace=True)
GDP.replace(to_replace="Iran, Islamic Rep.", value="Iran", inplace=True)
GDP.replace(to_replace="Hong Kong SAR, China", value="Hong Kong", inplace=True)



ScimEn=pd.read_excel("scimagojr-3.xlsx")


def answer_one():
    
    #return GDP.iloc[:,[0,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]]
    merg1=pd.merge(ScimEn,energy, how="inner")
    
    merg2=pd.merge(merg1,GDP.iloc[:,[0,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]],how="inner", left_on="Country", right_on="Country Name")
    
    return merg2.set_index("Country").drop("Country Name", axis=1).head(15)
          
answer_one()
