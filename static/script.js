document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('uploadForm');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('videoFile');
    const languageSelect = document.getElementById('language');
    const statusDiv = document.getElementById('status');
    const translatedVideo = document.getElementById('translatedVideo');

    if (!fileInput.files.length) {
      alert('Please select a video file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('language', languageSelect.value);

    statusDiv.innerText = 'Uploading and translating video...';
    translatedVideo.style.display = 'none';

    try {
      const response = await fetch('http://127.0.0.1:8000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Upload failed');

      const result = await response.json();
      const videoPath = result.translated_video_path;

      statusDiv.innerText = 'Translation complete. Playing video below:';
      translatedVideo.src = `http://127.0.0.1:8000/${videoPath}`;
      translatedVideo.style.display = 'block';
    } catch (error) {
      console.error('Error uploading video:', error);
      statusDiv.innerText = 'An error occurred. Please try again.';
    }
  });
});
