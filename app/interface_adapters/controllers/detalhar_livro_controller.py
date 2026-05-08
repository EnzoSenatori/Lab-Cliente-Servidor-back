from __future__ import annotations

from app.use_cases import detalhar_livro
from app.domain.repositories import LivroRepository
from app.interface_adapters.presenters import apresentar_livro


def detalhar_livro_controller(livro_repository: LivroRepository, livro_id: int) -> dict:
    try:
        livro = detalhar_livro(livro_repository, livro_id)
        return {"status": 200, "data": apresentar_livro(livro)}

    except ValueError as e:
        return {"status": 404, "erro": str(e)}