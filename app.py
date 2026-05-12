from flask import Flask, render_template, request

app = Flask(__name__)

# The data parsed from the handwritten note, updated with Pear Shape
CATEGORIES = {
    "Age": {"13-18": 20, "19-24": 17, "25-30": 15, "30-35": 10, "35+": 4},
    "Body Shape": {"Square / Rectangle": 10, "Inverted Triangle": 4, "Hourglass": 13, "Pear Shape": 15, "Round / Apple": 8},
    "Weight": {"Thin": 8, "Toned": 12, "Muscly": 6, "Chubby": 9, "Fat": 0},
    "Hair Color": {"Blonde": 8, "Brown": 4, "Black": 6, "Ginger": 8, "Funky & Other": 0, "White": 2},
    "Eye Color": {"Blue": 8, "Green": 7, "Brown": 0, "Violet": 8, "Heterochromia": 6},
    "Hair Length": {"Bald": 0, "Chin": 2, "Shoulder": 4, "Waist": 6, "Waist Down": 8},
    "Height (cm)": {"< 150": 8, "150 - 158": 7, "159 - 168": 10, "169 - 174": 6, "175+": 2},
    "Boobs": {"A": 2, "B": 6, "C": 8, "D": 10, "E": 8, "F": 6, "G": 4},
    "Bonus: Is she a Chef?": {"Yes": 6, "No": 0}
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        total = 0
        # Calculate the total based on the submitted form data securely on the backend
        for category in CATEGORIES:
            selected_option = request.form.get(category)
            if selected_option and selected_option in CATEGORIES[category]:
                total += CATEGORIES[category][selected_option]
        result = total
        
    # Pass the categories to the template to generate the form dynamically
    return render_template("index.html", categories=CATEGORIES, result=result)

if __name__ == "__main__":
    app.run(debug=True)