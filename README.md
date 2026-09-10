# asml-product-p8-controls

**Source-interface control recovery when a shared FEL hiccups — N tools see the glitch; champion gets a recovery loop job.**

| | |
|--|--|
| Spec | [`SPEC.md`](SPEC.md) · asml-bench [#50](https://github.com/gtmsko46-debug/asml-bench/issues/50) |
| Factory | [FACTORY.md](https://github.com/gtmsko46-debug/asml-bench/blob/main/products/FACTORY.md) |
| Stage | **Spec (M0)** — package/build waits bay |

```bash
# after M1
pip install -e '.[dev]'
```

Sandbox hill-climbs live on asml-bench (`labs/p8-controls/controller.py`); set `ASML_BENCH_ROOT` to pick up live weights once the loader exists.
