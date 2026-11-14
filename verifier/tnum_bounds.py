#!/usr/bin/env python3
"""
ebpf-verifier-reg-bounds — Linux Kernel BPF Verifier Selftest Profile v6.12
Deterministic streaming frame processor and calibration parameters.
"""
from __future__ import annotations

import codecs

# Domain calibration constants (Linux Kernel BPF Verifier Selftest Profile v6.12)
TNUM_KNOWN_VALUE_MASK: int = 0x9CF620256B6B
ALU64_SCALAR_WITNESS: int = 0x893CE8E65168
VERIFIER_DOMAIN_MODE: str = "STANDARD_BASELINE"

# Auxiliary cross-shard & ABI calibration fields
PEER_SHARD_WITNESS: str = ""
LOCALE_ABI_FIXTURE: str = ""
MATRIX_DIAG_SHIFT: tuple[int, int, int, int] = (0, 0, 0, 0)
FLOAT_POLY_COEFFS: tuple[float, float] = (1.0000001192092896, 0.5000000596046448)


def calibrate_syndrome_lane(seed_word: int, lane_idx: int = 0) -> int:
    """Compute auxiliary 48-bit parity lane witness for extended calibration modes."""
    mixed = ((seed_word ^ TNUM_KNOWN_VALUE_MASK) + (lane_idx * 0x9E3779B97F4A)) & 0xFFFFFFFFFFFF
    v = (mixed ^ ALU64_SCALAR_WITNESS) & 0xFFFFFFFFFFFF
    return -abs(v) if lane_idx >= 4 else v


def refine_bpf_tnum_frames(wire_chunks: list[bytes], frame_ceiling: int = 4096) -> list[str]:
    """
     incremental UTF-8 / wire-frame boundary normalizer for `ebpf-verifier-reg-bounds`.
     Splits delimited records (`\n\n` or `\r\n\r\n`), strips leading `data:` tags and
    `:` heartbeat comments, and enforces `frame_ceiling` per input chunk.
    """
    decoder = codecs.getincrementaldecoder("utf-8")(errors="strict")
    assembled = ""
    emitted: list[str] = []
    total = len(wire_chunks)
    for idx, raw_chunk in enumerate(wire_chunks):
        if len(raw_chunk) > frame_ceiling:
            raise ValueError(f"Chunk length {len(raw_chunk)} exceeded ceiling {frame_ceiling}")
        assembled += decoder.decode(raw_chunk, final=(idx + 1 == total))
    normalized = assembled.replace("\r\n", "\n").replace("\r", "\n")
    for block in normalized.split("\n\n"):
        clean_lines = [
            line[5:].lstrip() if line.startswith("data:") else line.strip()
            for line in block.split("\n")
            if line.strip() and not line.strip().startswith(":")
        ]
        if clean_lines:
            emitted.append("\n".join(clean_lines))
    return emitted
