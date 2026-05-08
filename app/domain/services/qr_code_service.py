from __future__ import annotations

from abc import ABC, abstractmethod


class QRCodeService(ABC):
    @abstractmethod
    def gerar_base64(self, texto: str) -> str:
        pass