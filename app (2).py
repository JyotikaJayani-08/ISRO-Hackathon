from flask import Flask, request, render_template_string
from inference_sdk import InferenceHTTPClient
import base64
import os

app = Flask(__name__)

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="nyXJk6z5QdXyq7AB6dy2"
)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crater Detection</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #121212;
            color: #ffffff;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif;
            text-align: center;
        }
        h1 {
            color: #00ffff;
            font-size: 2.5em;
            margin-bottom: 30px;
        }
        .container {
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
            max-width: 800px;
            width: 100%;
        }
        .image-container {
            position: relative;
            display: inline-block;
            margin-top: 20px;
        }
        .crater-box {
            position: absolute;
            border: 2px solid #ff00ff;
            pointer-events: none;
            box-shadow: 0 0 5px #ff00ff;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }
        input[type="file"] {
            display: none;
        }
        .file-label {
            background-color: #333333;
            color: #00ffff;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-block;
            margin-bottom: 20px;
        }
        .file-label:hover {
            background-color: #00ffff;
            color: #121212;
        }
        button {
            background-color: #ff00ff;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            transition: all 0.3s ease;
            margin-top: 20px;
        }
        button:hover {
            background-color: #00ffff;
            color: #121212;
            transform: scale(1.05);
        }
        a {
            color: #00ffff;
            text-decoration: none;
            margin-top: 20px;
            display: inline-block;
            transition: all 0.3s ease;
        }
        a:hover {
            color: #ff00ff;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Crater Detection</h1>
    <h5>by cosmo coders</h5>
    <div class="container">
        {% if image %}
            <h2>Results</h2>
            <div class="image-container">
                <img src="data:image/jpeg;base64,{{ image }}" alt="Uploaded Image">
                {% for prediction in predictions %}
                    <div class="crater-box" style="
                        left: {{ prediction.x }}px;
                        top: {{ prediction.y }}px;
                        width: {{ prediction.width }}px;
                        height: {{ prediction.height }}px;">
                    </div>
                {% endfor %}
            </div>
            <h3>Detected Craters: {{ predictions|length }}</h3>
            <a href="/">Detect Another Image</a>
        {% else %}
            <form action="/" method="post" enctype="multipart/form-data">
                <center><label for="file-upload" class="file-label">
                    Choose Image
                </label></center>
                <input id="file-upload" type="file" name="file" accept="image/*" required>
                <br>
                <center><button type="submit">Detect Craters</button></center>
            </form>
        {% endif %}
    </div>
    <script>
        document.getElementById('file-upload').addEventListener('change', function() {
            if(this.files && this.files[0]) {
                document.querySelector('.file-label').textContent = this.files[0].name;
            }
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(filename)
            
            # Perform inference
            result = CLIENT.infer(filename, model_id="crater-detection-06ugb/1")
            
            # Process results
            predictions = result['predictions']
            
            # Convert image to base64 for embedding in HTML
            with open(filename, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            
            return render_template_string(HTML_TEMPLATE, image=encoded_string, predictions=predictions)
    
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)