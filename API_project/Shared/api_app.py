from flask import Flask, jsonify

app = Flask(__name__)

data = [{'number': "1",
					'image': "link_to_image_1",
					'result': "OK"},
					{'number': "2",
					'image': "link_to_image_2",
					'result': "Not OK"},
					{'number': "3",
					'image': "link_to_image_3",
					'result': "OK"},
]

@app.route('/')
def index():
	return "Welcome to the API App"

@app.route("/data", methods=['GET'])
def get():
	return jsonify({'Data':data})

if __name__ == "__main__":
	app.run(debug=True)