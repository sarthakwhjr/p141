from flask import Flask,jsonify,request
import csv
allarticles=[]
with open("articles.csv", encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    allarticles=data[1:]

liked=[]
disliked=[]

app=Flask(__name__)
@app.route("/getarticles")
def getmovie():
    return jsonify({
        "data":allarticles[0],
        "status":"success",
    })
@app.route("/likedarticles",methods=["POST"])
def likedmovie():
    global allarticles
    movie=allarticles[0]
    allarticles=allarticles[1:]
    liked.append(movie)
    return jsonify({
        "status":"success"

    }),201 

@app.route("/dislikedarticles",methods=["POST"])
def dislikedmovie():
    global allarticles
    movie=allarticles[0]
    allmovies=allarticles[1:]
    disliked.append(movie)
    return jsonify({
        "status":"success"

    }),201
 
if (__name__=="__main__"):
    app.run()  