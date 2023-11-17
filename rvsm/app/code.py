import joblib
import pandas as pd
model=joblib.load(r"C:\Users\MOHANKUMAR\PROJECTS\Machine Learning\Rock vs Mine\rsvm.joblib")
def predicts(a,b,c,d,e,f):
    a = pd.DataFrame({
    'TOP': [a],
    'TOP RIGHT': [b],
    'TOP LEFT': [c],
    'BOTTOM RIGHT': [d],
    'BOTTOM LEFT': [e],
    'CENTRE': [f]
    })

    predict1 = model.predict(a)
    if(predict1[0] == 'M'):
        print(1)
        return 1
    elif(predict1[0] == 'R'):
        print(2)
        return 2

    return(predict1[0])
