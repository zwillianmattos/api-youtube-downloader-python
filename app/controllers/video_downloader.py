from flask_restful import Resource
from pytube import YouTube
from flask import Flask, send_file, request, send_from_directory
from io import BytesIO
import json
import os
class VideoDownloader(Resource):

    def get(self, id):
        url = YouTube(str("https://www.youtube.com/watch?v=" + id))

        streams = []
        for stream in url.streams.filter(progressive=True):
            streams.append({ "itag": stream.itag, "mime_type": stream.mime_type, "resolution": stream.resolution})
        
        return streams

    def post(self, id):
        
        url =YouTube(str("https://www.youtube.com/watch?v=" + id))
        only_audio = True if request.args.get('audio') == 'true' else False
        itag = int(request.args.get('itag'))

        if( only_audio ):
            video = url.streams.get_by_itag(251).download()
            return send_file(
                os.path.join("/app/", url.title + ".webm"),
                as_attachment=True,
                attachment_filename= url.title + ".webm",
                mimetype="audio/webm",
            )
        else: 
            buffer = BytesIO()
            video = url.streams.get_by_itag(itag)
            video.stream_to_buffer(buffer)
            buffer.seek(0)

            return send_file(
                buffer,
                as_attachment=True,
                attachment_filename= url.title + ".mp4",
                mimetype="video/mp4",
            )