from __future__ import annotations # adia a avaliação das anotações de tipo, transformando-as internamente em strings

from dataclasses import dataclass, field


@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    editora: str
    unidades: dict[str, int] = field(default_factory=dict)

    def tem_estoque(self, unidade: str) -> bool:
        return self.unidades.get(unidade, 0) > 0

    def total_estoque(self) -> int:
        total = 0
        for quantidade in self.unidades.values():
            total += quantidade
        return total

    def classificar_disponibilidade(self) -> str:
        total = self.total_estoque()

        if total <= 0:
            return "Sem estoque"
        if total == 1:
            return "Última unidade"
        if total <= 3:
            return "Baixo estoque"
        return "Disponível"

    def unidades_com_estoque(self) -> dict[str, int]:
        resultado: dict[str, int] = {}

        for unidade, quantidade in self.unidades.items():
            if quantidade > 0:
                resultado[unidade] = quantidade

        return resultado

    def nome_unico(self) -> str:
        return f"{self.titulo} - {self.autor}"