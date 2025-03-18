from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Define the Excel file path
EXCEL_FILE = "users.xlsx"

# Function to save data to Excel
def save_to_excel(username, password):
    data = {"Username": [username], "Password": [password]}
    df = pd.DataFrame(data)

    if not os.path.exists(EXCEL_FILE):
        df.to_excel(EXCEL_FILE, index=False)
    else:
        existing_df = pd.read_excel(EXCEL_FILE)
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_df.to_excel(EXCEL_FILE, index=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    username = data["username"]
    password = data["password"]
    
    save_to_excel(username, password)
    
    return jsonify({"message": "User saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
