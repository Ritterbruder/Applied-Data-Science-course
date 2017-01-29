def answer_six():
    
    Top15 = answer_one()
    
    tupl=Top15["% Renewable"].sort_values(ascending=False).reset_index().iloc[0,0], Top15["% Renewable"].sort_values(ascending=False)[0]
    
    return tupl

answer_six()
