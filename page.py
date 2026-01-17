from flask import Flask, render_template, request, redirect
from data import links                                                      # Import the dictionary of class/subject -> URL

# Initialize Flask with custom folders
app = Flask(
    __name__,
    template_folder='frontend',                                             # HTML templates
    static_folder='ui',                                                     # CSS/JS/images
    static_url_path='/static'                                               # Serve static files at /static/...
)

# Home page
@app.route('/')
def home():
# Pass all classes and their subjects to HTML
    return render_template('index.html', classes=links)

# Redirect to the actual study material
@app.route('/redirect')
def go_to_book():
# Get selected class and subject from URL parameters
    std = request.args.get('class')
    subj = request.args.get('subject')

# If the combination exists, redirect to the PDF link
    if std in links and subj in links[std]:
        return redirect(links[std][subj])
    
# If not found, show error
    return "Link not available for this selection", 404

if __name__ == '__main__':
    app.run(debug=True)
