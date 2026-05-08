from __future__ import annotations

from abc import ABC, abstractmethod # ABC = Abstract Base Class
from typing import List

from app.domain.entities import Livro


class LivroRepository(ABC): # Trata-se de uma interface
    @abstractmethod
    def buscar_por_termo(self, termo: str) -> List[Livro]:
        pass

    @abstractmethod
    def buscar_por_id(self, livro_id: int) -> Livro | None: # type hint: retorna um livro ou 'none', caso não for encontrado
        pass

    @abstractmethod
    def listar_todos(self) -> List[Livro]:
        pass

    # Repository retorna entidades --> o domínio trabalha com 'entities' e não com dicionários JSON
    # Quem transforma JSON ↔ objeto é a Infrastructure, não o domínio