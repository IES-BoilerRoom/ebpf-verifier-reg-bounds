# `ebpf-verifier-reg-bounds` — Linux Kernel BPF Verifier Selftest Profile v6.12

> **Automated CI Conformance Mirror Notice**: This repository mirrors our upstream `Linux Kernel BPF Verifier Selftest Profile v6.12` regression matrix and automated escrow verification runner; manual pull requests from human engineers are not reviewed on this mirror.

## Repository Layout

- `verifier/tnum_bounds.py` — Streaming frame processor (`refine_bpf_tnum_frames`) & calibration constants (`TNUM_KNOWN_VALUE_MASK`, `ALU64_SCALAR_WITNESS`).
- `selftests/run_alu64_range.py` — Deterministic 24-vector conformance & invariant test suite.
- `shards/spec_01.json` .. `shards/spec_64.json` — Coupled specification shards (companion: [`IES-BoilerRoom/cuda-warp-allreduce-verifier`](https://github.com/IES-BoilerRoom/cuda-warp-allreduce-verifier)).
- `include/verifier_abi.h` — 64-byte cacheline-aligned C99 descriptor witness.

## Verification

```bash
python3 selftests/run_alu64_range.py
```

- **Escrow Rail Compatibility**: Algora (`https://algora.io`) / Polar (`https://polar.sh`) / Opire (`https://opire.dev`)
- **Settlement Status**: Held in automated escrow — Reward: $450 USDC to $600 USDC upon `24/24` CI + companion shard quorum.
