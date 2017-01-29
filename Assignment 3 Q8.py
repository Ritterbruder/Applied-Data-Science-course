def answer_eight():
    
    Top15 = answer_one()
    
    Top15["Population"]=Top15["Energy Supply"]/Top15["Energy Supply per Capita"]
    
    
    return Top15["Population"].sort_values(ascending=False).reset_index().iloc[2,0]

answer_eight()
