import os
import cv2
import numpy as np
import logging
from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from moviepy.editor import concatenate_videoclips, VideoFileClip

# Flask app setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['OUTPUT_FOLDER'] = 'outputs/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# Logging setup
logging.basicConfig(
    filename='processing.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Helper: Check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route: Main page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Upload images
@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part'}), 400
    
    files = request.files.getlist('files[]')
    filepaths = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            filepaths.append(filepath)
            logging.info(f"Uploaded: {filepath}")
    
    if not filepaths:
        return jsonify({'error': 'No valid files uploaded'}), 400
    
    return jsonify({'filepaths': filepaths}), 200

# Route: Convert images to 3D motion videos
@app.route('/convert', methods=['POST'])
def convert_to_3d_motion():
    data = request.get_json()
    image_paths = data.get('image_paths', [])
    if not image_paths or not all(os.path.exists(path) for path in image_paths):
        logging.error("Invalid or missing image paths")
        return jsonify({'error': 'Images not found'}), 400

    output_videos = []
    for image_path in image_paths:
        try:
            output_video_path = process_image(image_path)
            output_videos.append(output_video_path)
            logging.info(f"Processed: {output_video_path}")
        except Exception as e:
            logging.error(f"Error processing {image_path}: {e}")
            return jsonify({'error': f"Error processing {image_path}"}), 500

    final_video_path = os.path.join(app.config['OUTPUT_FOLDER'], 'final_output.mp4')
    try:
        combine_videos(output_videos, final_video_path)
        logging.info(f"Final video created: {final_video_path}")
        return jsonify({'output_video_path': final_video_path}), 200
    except Exception as e:
        logging.error(f"Error combining videos: {e}")
        return jsonify({'error': 'Error combining videos'}), 500

# Helper: Process an image into a 3D motion video
def process_image(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], os.path.basename(image_path) + '_motion.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, 24, (width, height))

    for i in range(30):  # Simulate motion effect
        matrix = np.float32([[1, 0, i], [0, 1, 0]])
        transformed = cv2.warpAffine(image, matrix, (width, height))
        video.write(transformed)
    
    video.release()
    return output_path

# Helper: Combine videos
def combine_videos(video_paths, output_path):
    clips = [VideoFileClip(path) for path in video_paths]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, codec='libx264', fps=24)
    for clip in clips:
        clip.close()

# Route: Download the final video
@app.route('/download2/<filename>')
def download_file2(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)



@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config["OUTPUT_FOLDER"], filename)
    if os.path.exists(file_path):
        return send_from_directory(app.config["OUTPUT_FOLDER"], filename, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
