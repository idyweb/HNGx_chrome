import os
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect,render_template, send_from_directory, url_for

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
    if not  request.files:
        return "No file part"
    
    video_file = request.files['video']
    if video_file.filename == '':
        return "No selected file"
    
    if video_file:
        filename = secure_filename(video_file.filename)
        video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Return a redirect response to the play_video route with the filename
        return redirect(url_for('play_video', filename=filename))
    
# Route for playing the video
@app.route('/play/<filename>')
def play_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
     
if __name__ == '__main__':
    app.run(debug=True)
