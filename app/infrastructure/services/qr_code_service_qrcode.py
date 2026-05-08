from __future__ import annotations

import base64
from io import BytesIO

import qrcode

from app.domain.services.qr_code_service import QRCodeService


class QRCodeServiceQRCode(QRCodeService):
    def gerar_base64(self, texto: str) -> str:
        qr = qrcode.make(texto)

        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        imagem_bytes = buffer.getvalue()
        imagem_base64 = base64.b64encode(imagem_bytes).decode("utf-8")

        return f"data:image/png;base64,{imagem_base64}"