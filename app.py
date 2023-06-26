from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

current_curriculum = ""
additional_instructions = ""

@app.route("/plan/<string:subject>", methods=['POST'])
def create_curriculum(subject):
    global current_curriculum
    global additional_instructions

    curriculum_request = None
    if request.is_json:
        curriculum_request = request.get_json(force=True)
    else:
        curriculum_request = request.form

    if curriculum_request:
        additional_instructions = curriculum_request.get("additional_instructions", "")

    if subject not in current_curriculum:
        current_curriculum = subject

    return jsonify(message='TODO'), 200

@app.route("/lesson/<string:subject>", methods=['POST'])
def start_lesson(subject):
    global current_curriculum
    global additional_instructions

    lesson_request = None
    if request.is_json:
        lesson_request = request.get_json(force=True)
    else:
        lesson_request = request.form

    if lesson_request:
        additional_instructions = lesson_request.get("additional_instructions", "")

    if subject not in current_curriculum:
        return jsonify(message='Subject not in curriculum'), 200
    return jsonify(message='TODO'), 200

@app.route("/curriculum", methods=['GET'])
def get_curriculum():
    global current_curriculum

    if current_curriculum == "":
        return jsonify(message='No curriculum set'), 200

    return jsonify(current_curriculum), 200

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
