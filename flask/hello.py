from flask import Flask,render_template, request
from Covid19India import CovidIndia 
app= Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route("/")
def hellworld():                                                                                                                                              
    obj = CovidIndia()                                                                                                                                                                                  
    stats = obj.getstats()
    sort=sorted(stats['states'].items(),key=lambda x: x[1]['confirmed'], reverse=True)
    to=obj._CovidIndia__gettotalstats()
    return render_template("index.html", result=sort, total=to, t=stats)

@app.route("/covid")
def covid_19():
    return "It stated from China"

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)
    
if __name__=='__main__':
    app.debug=True
    app.run()
    app.run(debug=True)


