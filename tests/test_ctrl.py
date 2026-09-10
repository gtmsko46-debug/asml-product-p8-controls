from asml_product_p8_controls import recover_from_glitch
from asml_product_p8_controls.loader import reset_loader_cache
import pytest

@pytest.fixture(autouse=True)
def _e(monkeypatch):
    monkeypatch.delenv("ASML_BENCH_ROOT", raising=False)
    reset_loader_cache()

def test_smoke():
    r = recover_from_glitch({})
    assert r.t_recover_ms > 0
    assert r.tools_affected >= 1
