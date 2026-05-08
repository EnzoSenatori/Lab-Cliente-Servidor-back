from __future__ import annotations

from app.domain.entities import Reserva


def apresentar_reserva(reserva: Reserva) -> dict:
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