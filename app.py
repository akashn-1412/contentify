from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route for Blog Content tool
@app.route('/blog_content')
def blog_content():
    return render_template('content_generator.html')

# Route for YouTube Description tool
@app.route('/youtube_description')
def youtube_description():
    return render_template('yt_description.html')

# Route for Plagiarism Checker tool
@app.route('/plagiarism_checker')
def plagiarism_checker():
    return render_template('plagiarism.html')

# Route for Marketing Strategy tool
@app.route('/marketing_strategy')
def marketing_strategy():
    return render_template('market.html')

# Route for Pitch Generator tool
@app.route('/pitch_generator')
def pitch_generator():
    return render_template('pitch_generate.html')

@app.route('/text_improver')
def text_improver():
    return render_template('text_improver.html')

@app.route('/blog_topic_ideas')
def blog_topic_ideas():
    return render_template('blog_topics.html')

@app.route('/blog_title')
def blog_title():
    return render_template('blog_title.html')

@app.route('/seo_title')
def seo_title():
    return render_template('seo_title.html')

if __name__ == '__main__':
    app.run(debug=True)
