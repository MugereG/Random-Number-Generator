from flask import Flask, render_template, request
import random
import hashlib

app = Flask(__name__)

def generate_deterministic_number(name):
    # Use a hash function (e.g., SHA-256) to map names to unique numbers
    hash_object = hashlib.sha256(name.encode())
    hash_hex = hash_object.hexdigest()
    
    # Convert the hexadecimal hash to an integer and take modulo 6 (for numbers 1-6)
    number = int(hash_hex, 16) % 6 + 1
    
    return number

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    names = request.form.getlist('name')
    numbers = [generate_deterministic_number(name.lower()) for name in names]
    results = zip(names, numbers)
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
