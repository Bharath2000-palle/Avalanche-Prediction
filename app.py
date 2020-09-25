import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('project.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('project.html')

@app.route('/predict1',methods=['POST','GET'])
def predict1():
    test=[int(x) for x in request.form.values()]
    print("bharath")
    print(test)
    x_test=np.array([[1,2,3,4,5,6]])#some initialisation values
    if(test[4]==2):
        x_test[0][0]=0
        x_test[0][1]=0
    elif(test[4]==0):
        x_test[0][0]=1
        x_test[0][1]=0  
    else:
        x_test[0][0]=0
        x_test[0][1]=1
    x_test[0][2]=int(test[0])
    x_test[0][3]=int(test[1])
    x_test[0][4]=int(test[2])
    x_test[0][5]=int(test[3])
        
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output==0):
        return render_template('project.html', prediction_text='There will be no avalanche:{}-safe'.format(output))
    elif(output==1):
        return render_template('project.html', prediction_text='There will be moderte avalanche.you can vacate you your place if you want {}-moderate'.format(output)) 
    else:
        return render_template('project.html', prediction_text='Avalanche is strong..It is neccesary to vacate your places:{}-high'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
