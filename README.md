# **Image to Video with 3D Motion**

This project enables users to upload multiple images and convert them into a video with a 3D motion effect using Python libraries like OpenCV, NumPy, and MoviePy. It's a simple and user-friendly Flask-based web application designed to process images and produce stunning 3D-like motion videos.

---

## **Getting Started**

### **1. Prerequisites**

Ensure you have the following installed on your system:

- **Python**: Version 3.8 or later
- **pip**: Python's package manager
- **FFmpeg**: Required for video processing with MoviePy.

#### Install FFmpeg:

- **macOS**:
  ```bash
  brew install ffmpeg
  ```

- **Linux**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

- **Windows**:
  - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
  - Add FFmpeg to your system's PATH.

---

### **2. Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shaponpal6/Image-to-video-3d.git
   cd Image-to-video-3d
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

   The application will run on `http://127.0.0.1:5000`.

---

## **Using the Application**

### **Step 1: Upload Images**
- Drag and drop multiple images or click to select files.
- Preview the uploaded images in a grid view.

### **Step 2: Convert to Video**
- Click the "Convert" button to generate the video.
- The progress bar will indicate the processing status.

### **Step 3: Download the Video**
- After processing, a "Download" button will appear.
- Click it to download the final MP4 file.

---

## **Features**

1. **User-Friendly Interface**:
   - Drag-and-drop or click to upload multiple images.
   - Real-time preview of uploaded images in a grid format.

2. **Image to Video Conversion**:
   - Converts multiple uploaded images into a seamless video.
   - Adds 3D-like motion effects to each image.

3. **Download Final Video**:
   - After conversion, users can download the video in MP4 format.

4. **Progress Bar**:
   - Displays a loader and progress bar during video generation.
   -

---

## **Project Structure**

```
/Image-to-video-3d
    /static
        /css
            styles.css      # Stylesheet for UI
        /outputs
            final_output.mp4  # Generated video file
    /templates
        index.html          # Frontend template
    app.py                  # Flask application
    requirements.txt        # Dependencies
```

---

## **Troubleshooting**

### **1. Video Not Found (404 Error)**
   - **Error**: `GET http://127.0.0.1:5000/static/outputs/final_output.mp4 404 NOT FOUND`.
   - **Solution**:
     - Ensure the `outputs` folder exists in the `static` directory.
     - Check Flask has permissions to write to this folder.
     - Confirm the video file is being generated during processing.

### **2. CSS Not Loading**
   - **Error**: Styles not applied properly.
   - **Solution**: Verify that the `static/css/styles.css` file exists and the path in `index.html` is correct:
     ```html
     <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
     ```

### **3. FFmpeg Not Found**
   - **Error**: `MoviePy error: FFmpeg binary not found. Install FFmpeg on your system`.
   - **Solution**:
     - Ensure FFmpeg is installed and accessible in your system's PATH.
     - For macOS and Linux, run:
       ```bash
       which ffmpeg
       ```
       Ensure the command returns the correct binary path.

### **4. Dependency Conflicts**
   - **Error**: Issues during `pip install` or mismatched versions.
   - **Solution**:
     - Clear pip cache and reinstall:
       ```bash
       pip cache purge
       pip install --no-cache-dir -r requirements.txt
       ```

### **5. Unsupported File Format**
   - **Error**: Uploaded images are not processed.
   - **Solution**: Ensure the images are in a standard format like JPEG or PNG.

---

## **Requirements**

Here are the core dependencies of the project:
```
Flask
opencv-python
numpy
imageio-ffmpeg
moviepy==1.0.3
```

---

## **Future Improvements**
- Add customizable video effects and transitions.
- Support for audio tracks in the output video.
- Enable cloud storage for large-scale processing.

---

For any issues or contributions, feel free to raise an issue or submit a pull request on the [GitHub Repository](https://github.com/shaponpal6/Image-to-video-3d).
