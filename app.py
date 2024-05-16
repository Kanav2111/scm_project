from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form.html')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        feedback = request.form['feedback']

        # Save input to a text file
        with open('feedback.txt', 'a') as file:
            file.write(f'Full Name: {full_name}\nEmail: {email}\nFeedback: {feedback}\n\n')

        return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
