import sys, os, subprocess, platform
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Wav2Lip import generate_lipsync
from OCR.src import ocr_api
from Pronounce_Evaluation import eval_main
from flask import Flask, request, jsonify
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
        filename = request.json.get('filename')
        return jsonify({'success': generate_lipsync.generate(gender,input_text,input_image,out_path,filename),'path':out_path+filename});

@api.route('/ocr')
class OCR(Resource):
    def post(self):
        file = request.json.get('filename')
        return ocr_api.ocr_api(file);
    
    
@api.route('/pronounce/evaluation')
class PE(Resource):
    def post(self):
        file = request.json.get('filename')
        sentence = request.json.get('sentence')
        return eval_main.eval_main(file,sentence)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))