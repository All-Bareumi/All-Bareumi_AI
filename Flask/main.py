import sys, os, subprocess, platform
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Wav2Lip import generate_lipsync

from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/sentence/insert')
class Sentence(Resource):
    def post(self):
        gender = request.json.get('gender')
        input_text = request.json.get('input_text')
        input_image = '../Wav2Lip/my_data/'+request.json.get('character')
        out_path = request.json.get('out_path')
        result = generate_lipsync.generate(gender,input_text,input_image,out_path);
        return {"success" : result}
        
        

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))