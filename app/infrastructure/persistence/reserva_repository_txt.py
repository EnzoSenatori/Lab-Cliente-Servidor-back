from __future__ import annotations

import json
import os
from typing import List
from datetime import date

from app.domain.entities import Reserva
from app.domain.repositories import ReservaRepository


class ReservaRepositoryTXT(ReservaRepository):
    def __init__(self, caminho_arquivo: str) -> None:
        self.caminho_arquivo = caminho_arquivo
        self._garantir_arquivo()

    def adicionar(self, reserva: Reserva) -> None:
        with open(self.caminho_arquivo, "a", encoding="utf-8") as arquivo:
            dados = self._serializar(reserva)
            arquivo.write(json.dumps(dados) + "\n")

    def listar_todas(self) -> List[Reserva]:
        return self._carregar_todas()

    def proximo_id(self) -> int:
        reservas = self._carregar_todas()

        if not reservas:
            return 1

        maior_id = 0
        for reserva in reservas:
            if reserva.id > maior_id:
                maior_id = reserva.id

        return maior_id + 1

# Métodos privados
    def _garantir_arquivo(self) -> None:
        if os.path.exists(self.caminho_arquivo):
            return

        os.makedirs(os.path.dirname(self.caminho_arquivo), exist_ok=True)

        with open(self.caminho_arquivo, "w", encoding="utf-8"):
            pass

    def _carregar_todas(self) -> List[Reserva]:
        reservas: List[Reserva] = []

        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = json.loads(linha.strip())

                data_reserva = None
                if dados["data_reserva"] is not None:
                    data_reserva = date.fromisoformat(dados["data_reserva"])

                reserva = Reserva(
                    id=dados["id"],
                    livro_id=dados["livro_id"],
                    unidade=dados["unidade"],
                    nome_cliente=dados["nome_cliente"],
                    data_reserva=data_reserva,
                )

                reserva.definir_qr_code(
                    dados["qr_code_texto"],
                    dados["qr_code_base64"]
                )

                reservas.append(reserva)

        return reservas

    def _serializar(self, reserva: Reserva) -> dict:
        return {
            "id": reserva.id,
            "livro_id": reserva.livro_id,
            "unidade": reserva.unidade,
            "nome_cliente": reserva.nome_cliente,
            "data_reserva": (
                reserva.data_reserva.isoformat()
                if reserva.data_reserva is not None
                else None
            ),
            "qr_code_texto": reserva.qr_code_texto,
            "qr_code_base64": reserva.qr_code_base64,
        }