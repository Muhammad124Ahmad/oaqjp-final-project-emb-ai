"""Deploying Part of This App"""

from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

@app.route('/emotionDetector')
def emotion_detection():
    """"This Function Retrieve text f
    rom html and returns result"""
    text=request.args.get('textToAnalyze')
    result=emotion_detector(text)
    string=''
    for key in result:
        string=string+f"<p><b>{key}</b>: {result[key]}</p>"
    return string

@app.route('/')
def show_page():
    """This Function Renders HTML template"""
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
