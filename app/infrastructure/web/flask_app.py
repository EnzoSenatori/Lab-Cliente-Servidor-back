from __future__ import annotations

from datetime import date

from flask import Flask, request, jsonify
from flask_cors import CORS

def criar_app(
    livro_repository,
    reserva_repository,
    qr_code_service,
    buscar_livros_controller,
    detalhar_livro_controller,
    reservar_livro_controller,
):
    app = Flask(__name__)
    CORS(app)

    # ROTA: buscar livros
    @app.route("/livros", methods=["GET"])
    def buscar_livros():
        termo = request.args.get("q")

        resultado = buscar_livros_controller(
            livro_repository,
            termo,
        )

        return jsonify(resultado), resultado["status"]

    # ROTA: detalhar livro
    @app.route("/livros/<int:livro_id>", methods=["GET"])
    def detalhar_livro(livro_id: int):
        resultado = detalhar_livro_controller(
            livro_repository,
            livro_id,
        )

        return jsonify(resultado), resultado["status"]

    # ROTA: reservar livro
    @app.route("/reservas", methods=["POST"])
    def reservar_livro():
        dados = request.json

        livro_id = dados.get("livro_id")
        unidade = dados.get("unidade")
        nome_cliente = dados.get("nome_cliente")

        data_reserva_str = dados.get("data_reserva")
        data_reserva = None

        if data_reserva_str:
            data_reserva = date.fromisoformat(data_reserva_str)

        resultado = reservar_livro_controller(
            livro_repository,
            reserva_repository,
            qr_code_service,
            livro_id,
            unidade,
            nome_cliente,
            data_reserva,
        )

        return jsonify(resultado), resultado["status"]

    return app