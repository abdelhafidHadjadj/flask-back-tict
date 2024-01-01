from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import math
from functions import calcul_entrop, calcul_entropie_conj, calcul_quantité_info, calcul_quantité_info_mutuelle, calcul_entropie_cond_x_y, calcul_entropie_cond_y_x

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/calcul-hx", methods=['POST'])
def entropie():
    if request.method == 'POST':
        probabilities = request.get_json(force=True)
        print(probabilities)
        Hx = calcul_entrop(probabilities)
        return jsonify(Hx)


@app.route("/calcul-hy", methods=['POST'])
def entropieSrc2():
    if request.method == 'POST':
        probabilities = request.get_json(force=True)
        print(probabilities)
        Hy = calcul_entrop(probabilities)
        return jsonify(Hy)


@app.route("/calcul-ix", methods=['POST'])
def quantité_info():
    if request.method == 'POST':
        probabilities = request.get_json(force=True)
        Ix = calcul_quantité_info(probabilities)
        return jsonify(Ix)


@app.route("/calcul-hxy", methods=['POST'])
def entropie_conj():
    if request.method == 'POST':
        probabilities = request.get_json(force=True)
        Hxy = calcul_entropie_conj(probabilities)
        print(Hxy)
        return jsonify(Hxy)


@app.route("/calcul-ixy", methods=['POST'])
def quantité_info_mutuelle():
    if request.method == 'POST':
        data = request.get_json(force=True)
        ixy = calcul_quantité_info_mutuelle(
            data["probXY"], data["probX"], data["probY"])
        print(ixy)
        return jsonify(ixy)


@app.route("/calcul-hx_y", methods=['POST'])
def entropie_cond_x_y():
    if request.method == 'POST':
        data = request.get_json(force=True)
        Hx_y = calcul_entropie_cond_x_y(data["probY"], data["probXY"])
        return jsonify(Hx_y)


@app.route("/calcul-hy_x", methods=['POST'])
def entropie_cond_y_x():
    if request.method == 'POST':
        data = request.get_json(force=True)
        Hx_y = calcul_entropie_cond_x_y(data["probX"], data["probXY"])
        return jsonify(Hx_y)


# if __name__ == '__main__':
#     app.run(debug=True)
