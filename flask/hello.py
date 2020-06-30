from flask import Flask,render_template, request
from Covid19India import CovidIndia 
app= Flask(__name__)
@app.route("/")
def hellworld():                                                                                                                                              
    obj = CovidIndia()                                                                                                                                                                                  
    stats = obj.getstats()
    t=obj._CovidIndia__gettotalstats()
    return render_template("index.html", result=stats, total=t)

@app.route("/covid")
def covid_19():
    return "It stated from China"
if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)


