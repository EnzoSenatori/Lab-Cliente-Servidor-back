from __future__ import annotations

from app.domain.entities import Livro
from app.domain.repositories import LivroRepository


def detalhar_livro(livro_repository: LivroRepository, livro_id: int) -> Livro:
    livro = livro_repository.buscar_por_id(livro_id)

    if livro is None:
        raise ValueError("Livro não encontrado.")

    unidades_filtradas = livro.unidades_com_estoque()

    # Ordenação manual (sem lambda, mantendo seu estilo preferido)
    itens = list(unidades_filtradas.items())

    for i in range(len(itens)):
        for j in range(i + 1, len(itens)):
            if itens[j][1] > itens[i][1]:
                itens[i], itens[j] = itens[j], itens[i]

    unidades_ordenadas = {}
    for unidade, quantidade in itens:
        unidades_ordenadas[unidade] = quantidade

    livro.unidades = unidades_ordenadas

    return livro