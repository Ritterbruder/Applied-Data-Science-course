def answer_thirteen():
    
    Top15 = answer_one()
    
    Top15["PopEst"]=Top15["Energy Supply"]/Top15["Energy Supply per Capita"]
    
    return Top15["PopEst"].apply('{:,}'.format)


answer_thirteen()
