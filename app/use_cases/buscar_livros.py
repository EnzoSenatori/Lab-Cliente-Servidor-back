from __future__ import annotations

from typing import List

from app.domain.entities import Livro
from app.domain.repositories import LivroRepository


def buscar_livros(livro_repository: LivroRepository, termo: str) -> List[Livro]:
    if termo is None or termo.strip() == "":
        raise ValueError("O termo de busca não pode ser vazio.")

    resultado = livro_repository.buscar_por_termo(termo)

    return resultado