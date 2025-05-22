from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

BLOG_POSTS = [
    {
        "slug": "datacenter-emissions",
        "title": "Estimating Data Centre Emissions in the EU",
        "summary": "A summary of my master's thesis on AI digital infrastructure sustainability, modeling the energy consumption of data centres and their carbon impacts in European Union Member States.",
        "image": "energy_dc.png",
        "date": "May 2025"
    },
    {
        "slug": "ai-criminal-justice",
        "title": "Artificial Intelligence in Security and Justice: Lessons for Mexico",
        "summary": (
            "A reflection on the risks and challenges of automated decision-making technologies in criminal justice, especially in Mexico, "
            "where legal safeguards are still lacking to prevent data misuse and human rights violations. "
            "This article was originally published in Spanish as “Inteligencia artificial en seguridad y justicia: lecciones para México” (Nexos, June 2023)."
        ),
        "image": "IA_criminal_justice.png",
        "date": "June 2023",
        "url": "https://redaccion.nexos.com.mx/inteligencia-artificial-en-seguridad-y-justicia-lecciones-para-mexico/"
    },
    # Add more posts...
]

@app.route('/blog')
def blog():
    return render_template("blog.html", posts=BLOG_POSTS)

@app.route('/blog/<slug>')
def blog_entry(slug):
    post = next((p for p in BLOG_POSTS if p["slug"] == slug), None)
    if post is None:
        abort(404)
    return render_template(f"blog/{slug}.html", post=post)

if __name__ == '__main__':
    app.run(debug=True)
