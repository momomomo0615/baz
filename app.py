from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/about.html')
def about():  # put application's code here
    return render_template('about.html')
@app.route('/about2.html')
def about2():  # put application's code here
    return render_template('about2.html')

@app.route('/about3.html')
def about3():  # put application's code here
    return render_template('about3.html')

@app.route('/about4.html')
def about4():  # put application's code here
    return render_template('about4.html')

@app.route('/about5.html')
def about5():  # put application's code here
    return render_template('about5.html')

@app.route('/about6.html')
def about6():  # put application's code here
    return render_template('about6.html')

@app.route('/about7.html')
def about7():  # put application's code here
    return render_template('about7.html')

@app.route('/services.html')
def services():  # put application's code here
    return render_template('contact.html')

@app.route('/blog.html')
def blog():  # put application's code here
    return render_template('blog.html')

@app.route('/pages.html')
def pages():  # put application's code here
    return render_template('pages.html')

@app.route('/apple.html')
def apple():  # put application's code here
    return render_template('apple.html')

@app.route('/error.html')
def error():  # put application's code here
    return render_template('error.html')

@app.route('/blogsingle.html')
def blogsingle():  # put application's code here
    return render_template('blogsingle.html')

@app.route('/blogsingle2.html')
def blogsingle2():  # put application's code here
    return render_template('blogsingle2.html')

@app.route('/blogsingle3.html')
def blogsingle3():  # put application's code here
    return render_template('blogsingle3.html')

@app.route('/shortcodes.html')
def shortcodes():  # put application's code here
    return render_template('shortcodes.html')
if __name__ == '__main__':
    app.run()
