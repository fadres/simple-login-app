from flask import Flask, render_template, request, redirect, url_index

app = Flask(__name__)

# Essential variable mapping required for Vercel's WSGI handler
app = app 

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

# Include your other existing routes (like login, success, etc.) below this line
