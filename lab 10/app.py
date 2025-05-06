from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample restaurant data
restaurant_data = {
    "name": "Spicy Delight",
    "location": "123 Flavor Street, Food City",
    "hours": "Mon-Sun: 11 AM - 11 PM",
    "menu": ["Pizza", "Pasta", "Burgers", "Salads", "Sushi"],
    "contact": "+1234567890"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"].lower()
    
    if "menu" in user_input:
        response = "Our menu includes: " + ", ".join(restaurant_data["menu"])
    elif "location" in user_input or "address" in user_input:
        response = f"We're located at: {restaurant_data['location']}"
    elif "time" in user_input or "hour" in user_input or "open" in user_input:
        response = f"Our hours are: {restaurant_data['hours']}"
    elif "contact" in user_input or "phone" in user_input:
        response = f"Contact us at: {restaurant_data['contact']}"
    else:
        response = "Sorry, I didn't understand that. Try asking about our menu, hours, location, or contact."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)



