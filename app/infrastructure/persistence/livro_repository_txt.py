from __future__ import annotations

import json
import os
from typing import List

from app.domain.entities import Livro
from app.domain.repositories import LivroRepository


class LivroRepositoryTXT(LivroRepository):
    def __init__(self, caminho_arquivo: str) -> None:
        self.caminho_arquivo = caminho_arquivo
        self._garantir_arquivo_com_seed()

    def buscar_por_termo(self, termo: str) -> List[Livro]:
        livros = self._carregar_todos()

        resultado: List[Livro] = []
        termo_lower = termo.lower()

        for livro in livros:
            if (
                termo_lower in livro.titulo.lower()
                or termo_lower in livro.autor.lower()
                or termo_lower in livro.editora.lower()
            ):
                resultado.append(livro)

        return resultado

    def buscar_por_id(self, livro_id: int) -> Livro | None:
        livros = self._carregar_todos()

        for livro in livros:
            if livro.id == livro_id:
                return livro

        return None

    def listar_todos(self) -> List[Livro]:
        return self._carregar_todos()

# Métodos privados
    def _garantir_arquivo_com_seed(self) -> None:
        if os.path.exists(self.caminho_arquivo):
            return

        os.makedirs(os.path.dirname(self.caminho_arquivo), exist_ok=True)

        livros_seed = [
            {
                "id": 1,
                "titulo": "Harry Potter",
                "autor": "J.K. Rowling",
                "editora": "Rocco",
                "unidades": {
                    "Loja Centro": 3,
                    "Loja Norte": 1,
                    "Loja Sul": 0
                }
            },
            {
                "id": 2,
                "titulo": "Senhor dos Anéis",
                "autor": "J.R.R. Tolkien",
                "editora": "Martins Fontes",
                "unidades": {
                    "Loja Centro": 2,
                    "Loja Norte": 0,
                    "Loja Sul": 4
                }
            },
            {
                "id": 3,
                "titulo": "Dom Casmurro",
                "autor": "Machado de Assis",
                "editora": "Globo",
                "unidades": {
                    "Loja Centro": 0,
                    "Loja Norte": 2,
                    "Loja Sul": 1
                }
            },
        ]

        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            for livro in livros_seed:
                arquivo.write(json.dumps(livro) + "\n")

    def _carregar_todos(self) -> List[Livro]:
        livros: List[Livro] = []

        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = json.loads(linha.strip())

                livro = Livro(
                    id=dados["id"],
                    titulo=dados["titulo"],
                    autor=dados["autor"],
                    editora=dados["editora"],
                    unidades=dados["unidades"],
                )

                livros.append(livro)

        return livros