from flask import Flask, render_template, request, send_file
from pytube import YouTube
from pathlib import Path
import os

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/download', methods=['GET', 'POST'])
def download():
    link = request.form['queries']
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    filename = stream.title
    downloads_path = str(Path.home() / "Downloads")
    stream.download(output_path=downloads_path)
    filename = filename + ".mp4"
    filename = filename.replace("|", "")
    filename = filename.replace("'","")
    filename = filename.replace(":","")
    return send_file(os.path.join(downloads_path, filename), as_attachment=True)
