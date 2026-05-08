from __future__ import annotations

from datetime import date

from app.domain.entities import Reserva
from app.domain.repositories import LivroRepository, ReservaRepository
from app.domain.services.qr_code_service import QRCodeService


def reservar_livro(
    livro_repository: LivroRepository,
    reserva_repository: ReservaRepository,
    qr_code_service: QRCodeService,
    livro_id: int,
    unidade: str,
    nome_cliente: str | None = None,
    data_reserva: date | None = None,
) -> Reserva: # quebrei as linhas dos parâmetros para deixar mais legível

    livro = livro_repository.buscar_por_id(livro_id)

    if livro is None:
        raise ValueError("Livro não encontrado.")

    if not livro.tem_estoque(unidade):
        raise ValueError("Unidade sem estoque para reserva.")

    novo_id = reserva_repository.proximo_id()

    reserva = Reserva(
        id=novo_id,
        livro_id=livro_id,
        unidade=unidade,
        nome_cliente=nome_cliente,
        data_reserva=data_reserva,
    )

    unidade_formatada = unidade.replace(" ", "").upper()
    texto_qr = f"RESERVA-{reserva.id}-{unidade_formatada}"

    imagem_base64 = qr_code_service.gerar_base64(texto_qr)

    reserva.definir_qr_code(texto_qr, imagem_base64)

    reserva_repository.adicionar(reserva)

    return reserva