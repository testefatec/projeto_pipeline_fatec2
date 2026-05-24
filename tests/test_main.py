# tests/test_main.py

import sys
from pathlib import Path
import pytest

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import saudacao, calcular_media  # noqa: E402


class TestSaudacao:
    def test_saudacao_nome_valido(self):
        resultado = saudacao("Maria")
        assert "Maria" in resultado

    def test_saudacao_tipo_invalido(self):
        with pytest.raises(TypeError):
            saudacao(123)


class TestCalcularMedia:
    def test_media_simples(self):
        assert calcular_media([10, 8, 6]) == 8.0

    def test_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])
