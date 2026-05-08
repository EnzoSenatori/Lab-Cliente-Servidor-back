from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from app.domain.entities import Reserva


class ReservaRepository(ABC):
    @abstractmethod
    def adicionar(self, reserva: Reserva) -> None:
        pass

    @abstractmethod
    def listar_todas(self) -> List[Reserva]:
        pass

    @abstractmethod
    def proximo_id(self) -> int:
        pass