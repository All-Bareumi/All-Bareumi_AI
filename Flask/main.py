import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Wav2Lip import api_test

from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/test')
class Test(Resource):
    def get(self):
        return{"message" : api_test.test_function("Test is Okay")}
    def post(self):
        name = request.json.get('name')
        return {"message" : api_test.test_function(name)}
        

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))