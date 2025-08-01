from flask import Flask,render_template,request,jsonify
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

@app.route('/emotionDetector')
def emotionDetector():
    text=request.args.get('textToAnalyze')
    result=emotion_detector(text)
    string=''
    for key in result:
        string=string+f"<p><b>{key}</b>: {result[key]}</p>"
    return string    

@app.route('/')
def showPage():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)