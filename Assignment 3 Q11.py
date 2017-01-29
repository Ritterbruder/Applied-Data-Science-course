def answer_eleven():
    Top15 = answer_one()
    
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    
    Top15["Population"]=Top15["Energy Supply"]/Top15["Energy Supply per Capita"]
    
    Top15.reset_index(inplace=True)
    
    Cont_df=pd.DataFrame(data=ContinentDict, index=[0])
    
    Cont_df=Cont_df.T.reset_index()
    
    Cont_df.rename(columns={"index": "Country", 0:"Contitent"}, inplace=True)
    
    Cont_mr=pd.merge(Cont_df, Top15[["Population","Country"]], how="inner", left_on="Country", right_on="Country")
    
    return Cont_mr.set_index("Contitent").groupby(level=0)["Population"].agg({'size':np.size,'sum':np.sum,"mean":np.mean,'std':np.std})

answer_eleven()
