from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass
class Reserva:
    id: int
    livro_id: int
    unidade: str
    nome_cliente: str | None = None
    data_reserva: date | None = None
    qr_code_texto: str | None = None
    qr_code_base64: str | None = None

    def __post_init__(self) -> None:
        if self.data_reserva is not None and self.data_reserva < date.today():
            raise ValueError("A data da reserva não pode ser anterior à data atual.")

    def definir_qr_code(self, texto: str, imagem_base64: str) -> None:
        self.qr_code_texto = texto
        self.qr_code_base64 = imagem_base64

    def tem_cliente_informado(self) -> bool:
        return self.nome_cliente is not None and self.nome_cliente.strip() != ""

    def possui_data_informada(self) -> bool:
        return self.data_reserva is not None