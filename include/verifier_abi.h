/* SPDX-License-Identifier: Apache-2.0 */
/* Linux Kernel BPF Verifier Selftest Profile v6.12 — Zero-Copy Descriptor Layout */
#ifndef EBPF_VERIFIER_REG_BOUNDS_ABI_H
#define EBPF_VERIFIER_REG_BOUNDS_ABI_H
#include <stdint.h>
#define TNUM_KNOWN_VALUE_MASK_DEFAULT 0x9CF620256B6BULL
#define COMPANION_SHARD_REPO "IES-BoilerRoom/cuda-warp-allreduce-verifier"
typedef struct __attribute__((aligned(64))) {
    uint64_t sequence_tag;
    uint64_t syndrome_word_48;
    uint32_t lane_residuals[12];
} verifier_frame_desc_t;
#endif /* EBPF_VERIFIER_REG_BOUNDS_ABI_H */
