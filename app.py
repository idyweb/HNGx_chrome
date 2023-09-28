import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template



app = Flask(__name__)

# folder to store uploaded videos
UPLOAD_FOLDER = 'video_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#home route
@app.route('/')
def index():
    return render_template('index.html')

#route that handles video upload
@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No file part"
    
    video_file = request.files['video']
    if video_file.filename == '':
        return "No selected file"
    
    if video_file:
        filename = secure_filename(video_file.filename)
        video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "Video uploaded successfully"
    
if __name__ == '__main__':
    app.run(debug=True)
