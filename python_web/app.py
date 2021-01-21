from flask import Flask, render_template, request,jsonify,escape
from panduan import panduan_login
from pyecharts import options as opts
from pyecharts.charts import Bar
from random import randrange

app = Flask(__name__, static_folder="templates")

def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route('/')
def entry_page() -> 'html':
	return render_template('entry.html')

@app.route('/search',methods = ['POST'])
def search():
        email = request.form["email"]
        password = request.form["password"]
        a = panduan_login(email, password)
        print(a)
        if a =="true":
            return render_template('index.html')
        else:
            return render_template('fail.html')

@app.route('/data_one')
def data_one():
    return render_template('data_one.html')


@app.route('/data_two')
def data_two():
	return render_template('data_two.html')

@app.route('/data_three')
def data_three():
	return render_template('data_three.html')

@app.route('/pyecharts_1')
def pyecharts_1():
    return render_template('pyecharts_1.html')

@app.route('/search', methods = ['GET'])
def search_get():
    return render_template('index.html')

@app.route('/results',methods = ['GET'])
def results_page() -> 'html':
	return render_template('results.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route("/viewlog")
def view_log():
    contents=[]
    with open("vsearch.log","r") as log:
        for line in log:
            contents.append([])
            for item in line.split("|"):
                contents[-1].append(escape(item))

    titles= ["Formdata","Host_url","Remote_addr","results"]
    return render_template("view.html",the_data=contents,the_titles=titles)

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
	app.run(debug = True)