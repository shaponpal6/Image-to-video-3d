document.getElementById('upload-form').onsubmit = async function (e) {
    e.preventDefault();
    const formData = new FormData();
    const fileInput = document.getElementById('image-upload');
    Array.from(fileInput.files).forEach(file => formData.append('files[]', file));

    const response = await fetch('/upload', { method: 'POST', body: formData });
    const data = await response.json();

    if (data.filepaths) {
        document.getElementById('convert-button').style.display = 'inline-block';
        document.getElementById('convert-button').onclick = async function () {
            const convertResponse = await fetch('/convert', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ image_paths: data.filepaths })
            });
            const convertData = await convertResponse.json();

            if (convertData.output_video_path) {
                const videoElement = document.getElementById('motion-video');
                const videoPreview = document.getElementById('video-preview');
                const downloadLink = document.getElementById('download-link');

                videoElement.src = '/' + convertData.output_video_path;
                videoPreview.style.display = 'block';
                downloadLink.href = '/' + convertData.output_video_path;
            }
        };
    }
};
