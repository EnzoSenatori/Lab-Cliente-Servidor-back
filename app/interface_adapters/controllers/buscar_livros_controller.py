from __future__ import annotations

from app.use_cases import buscar_livros
from app.domain.repositories import LivroRepository
from app.interface_adapters.presenters import apresentar_lista_livros


def buscar_livros_controller(livro_repository: LivroRepository, termo: str) -> dict:
    try:
        livros = buscar_livros(livro_repository, termo)
        return {"status": 200, "data": apresentar_lista_livros(livros)}

    except ValueError as e:
        return {"status": 400, "erro": str(e)}