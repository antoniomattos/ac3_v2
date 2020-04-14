import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():


    cont = 0
    n = 2
    l = []
    while (cont <= 101):
        normal = False
        for x in range(2, n):
            if (n % x == 0):
                normal = True
                break
        if (not normal):
            cont += 1
            l.append(n)

        n + n = 1

    return str(l)


    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

