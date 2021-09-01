# tutorial from TechWithTim - YT

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# parser for the inputs
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help="Name of the video", required=True)
video_put_args.add_argument('likes', type=int, help="Number of likes", required=True)
video_put_args.add_argument('views', type=int, help="Number of views", required=True)

# define a dictionary // aka fake db
videos = {}

# define the new app
app = Flask(__name__)

# wrap it to a restful API
api = Api(app) 



def abort_not_exists(video_id):
    if video_id not in videos:
        abort(404, message="Video not present...")

def abort_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already present...")

# we can overrite some method from Resource
class Video(Resource):

    # get method
    def get(self, video_id):
        abort_not_exists(video_id)

        return videos[video_id]
    
    # put -> add something
    def put(self, video_id):
        abort_exists(video_id)

        args = video_put_args.parse_args()
        videos[video_id] = args

        return videos[video_id], 201 #201 means created

    def delete(self, video_id):
        abort_not_exists(video_id)
        del videos[video_id]
        return '',204


# define the route and an input parameter
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    
    # start the server 
    # set in debug mode -> see the logs
    # in production set it equal to False
    app.run(debug=True)