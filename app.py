from flask import Flask, send_from_directory, redirect, url_for
import threading
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Automatically trigger both downloads
    # Redirects to a simple HTML page that auto-downloads
    return '''
    <html>
    <head><title>Download Files</title></head>
    <body>
    <script>
      // Automatically start both downloads
      window.onload = function() {
        window.open('/download/AI(Lab).zip', '_blank');
        window.open('/download/nlpl.zip', '_blank');
      }
    </script>
    <h2>Downloading files...</h2>
    </body>
    </html>
    '''

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
