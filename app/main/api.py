from flask_restful import Api
from app.controllers.video_downloader import VideoDownloader

api = Api(
    catch_all_404s=True,
    errors={
    'FatalErrorDownloading': {
        'message': "Download Error.",
        'status': 500,
    },
    },
    prefix='/api'
)

api.add_resource(VideoDownloader, '/downloader/<string:id>')