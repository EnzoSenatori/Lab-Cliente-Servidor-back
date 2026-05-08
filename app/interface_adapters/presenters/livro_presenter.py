# Interface_adapters é a camada de tradução
# Controller receber os dados de fora (HTTP) --> fora para dentro
# Presenters Recebe Entities --> dentro para fora
from __future__ import annotations

from typing import List

from app.domain.entities import Livro


def apresentar_livro(livro: Livro) -> dict:
    return {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "editora": livro.editora,
        "unidades": livro.unidades,
        "total_estoque": livro.total_estoque(),
        "disponibilidade": livro.classificar_disponibilidade(),
    }


def apresentar_lista_livros(livros: List[Livro]) -> list[dict]:
    resultado: list[dict] = []

    for livro in livros:
        resultado.append(apresentar_livro(livro))

    return resultado