from flask import Flask , render_template , request , jsonify
import time
import rio
import os
# AI section

def worrior(qurry):
    
    replay_msg = rio.engine(qurry)
    
    return replay_msg

# Flask section

app = Flask(__name__)

@app.route("/") 

def intro():
    
    return render_template("intro.html")
@app.route("/index" , methods=["GET","POST"])
def main():
    
    if request.method == "POST":
        
        user = request.form["user"]
        
        sam = worrior(user)
        
        return jsonify({
            
              "results" : sam
        })
    
    return render_template("index.html")

if __name__ =="__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
    
    