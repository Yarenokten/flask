from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog-post-1')
def blog_post_1():
    return render_template('blog-post-1.html')

@app.route('/portfolio-2')
def portfolio_2():
    return render_template('portfolio-2-columns.html')

@app.route('/portfolio-4')
def portfolio_4():
    return render_template('portfolio-4-columns.html')

@app.route('/portfolio-5')
def portfolio_5():
    return render_template('portfolio-5-columns.html')

@app.route('/portfolio-project')
def portfolio_project_1():
    return render_template('portfolio-project-1.html')

@app.route('/portfolioproject')
def portfolio_project_2():
    return render_template('portfolio-project-2.html')

@app.route('/portfolio-project-3')
def portfolio_project_3():
    return render_template('portfolio-project-3.html')

@app.route('/blog-3')
def blog_3():
    return render_template('blog-3-columns.html')

if __name__ == "__main__":
    app.run(debug=True)
