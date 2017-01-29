def answer_twelve():
    
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
    
    Cont_df=pd.DataFrame(data=ContinentDict, index=[0])
    
    Cont_df=Cont_df.T.reset_index()
    
    Cont_df.rename(columns={"index": "Country", 0:"Contitent"}, inplace=True)
    
    Top15_cont=pd.merge(Cont_df, Top15.reset_index()[["% Renewable","Country"]], how="inner", left_on="Country", right_on="Country")
    
    Top15_cont["% bins"]=pd.cut(Top15_cont["% Renewable"], 5)
    
    Multind=Top15_cont.set_index(["Contitent","% bins"]).groupby(level=[0,1])["Country"].agg({"Number of countries": np.size})
    
    return Multind["Number of countries"]

answer_twelve()
