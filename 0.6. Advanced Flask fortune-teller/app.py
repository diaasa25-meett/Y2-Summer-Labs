from flask import Flask, render_template
import random

app = Flask(__name__)

# Route for the home page
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/fortune')
def fortune():
    fortunes = [
        "Sari will English you!speak English to avoid it!",
        "You will get promoted .",
        "Today is not your best :(",
        "you'll get pregnant in 3 years ",
        "one of your friends will unfriend you !! .",
        "You will meet someone mean bt don't listen to them.",
        "An opportunity will arise.",
        "it's a good day to admit what you were thinking about for long time.",
        "terrible news are coming your way be careful.",
        "You will get what you wanted."
    ]
    chosen_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)