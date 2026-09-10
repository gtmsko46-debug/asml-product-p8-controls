from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Mapping
from .loader import get_recover

ASSUMPTION_CARD = "source-glitch-controls-v1"

@dataclass
class RecoveryReport:
    t_recover_ms: float
    wafers_lost_proxy: float
    residual_overlay_nm: float
    recovery_ok: bool
    tools_affected: int
    assumption_card_id: str = ASSUMPTION_CARD
    note: str = "SEED synthetic glitch recovery."
    controller_source: str = "reference"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def recover_from_glitch(row: Mapping[str, Any] | None = None) -> RecoveryReport:
    source, fn = get_recover()
    out = fn(dict(row or {}))
    return RecoveryReport(
        t_recover_ms=float(out["t_recover_ms"]),
        wafers_lost_proxy=float(out["wafers_lost_proxy"]),
        residual_overlay_nm=float(out["residual_overlay_nm"]),
        recovery_ok=bool(out["recovery_ok"]),
        tools_affected=int(out["tools_affected"]),
        assumption_card_id=str(out.get("assumption_card_id", ASSUMPTION_CARD)),
        note=str(out.get("note", "SEED.")),
        controller_source=source,
    )
