def answer_seven():
    
    Top15 = answer_one()
    
    Top15["Self-Citations to Total Citations"]=Top15["Self-citations"]/Top15["Citations"]
    
    tupl2=Top15["Self-Citations to Total Citations"].sort_values(ascending=False).reset_index().iloc[0,0], Top15["Self-Citations to Total Citations"].sort_values(ascending=False)[0]
    
    return tupl2

answer_seven()
