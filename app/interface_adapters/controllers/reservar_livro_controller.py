from __future__ import annotations

from datetime import date

from app.domain.services.qr_code_service import QRCodeService
from app.use_cases import reservar_livro
from app.domain.repositories import LivroRepository, ReservaRepository
from app.interface_adapters.presenters import apresentar_reserva


def reservar_livro_controller(
    livro_repository: LivroRepository,
    reserva_repository: ReservaRepository,
    qr_code_service: QRCodeService,
    livro_id: int,
    unidade: str,
    nome_cliente: str | None,
    data_reserva: date | None,
) -> dict:
    try:
        reserva = reservar_livro(
            livro_repository,
            reserva_repository,
            qr_code_service,
            livro_id,
            unidade,
            nome_cliente,
            data_reserva,
        )

        return {"status": 201, "data": apresentar_reserva(reserva)}

    except ValueError as e:
        return {"status": 400, "erro": str(e)}