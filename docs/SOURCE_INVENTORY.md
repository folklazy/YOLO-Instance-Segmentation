# Source inventory and evidence audit

**Status: CANDIDATE SOURCES ONLY.** No claim of file-level inspection or release selection is made by creating this document.

## Known related repositories

- [MOTS20 Scaling Study](https://github.com/folklazy/YOLO_Instance_Segmentation_MOTS20_Scaling_Study)
- [CCTV600 Scaling Study](https://github.com/folklazy/YOLO_Instance_Segmentation_CCTV600_Scaling_Study)
- [Largest MOTS20](https://github.com/folklazy/YOLO_Large_Seg_MOTS20_Benchmark)
- [MOTS20 2nd largest](https://github.com/folklazy/YOLO_Second_Largest_Seg_MOTS20_Benchmark)
- [MOTS20 Medium](https://github.com/folklazy/YOLO_Medium_Seg_MOTS20_Benchmark)
- [MOTS20 Small](https://github.com/folklazy/YOLO_Small_Seg_MOTS20_Benchmark)
- [MOTS20 Nano](https://github.com/folklazy/YOLO_Nano_Seg_MOTS20_Benchmark)

## Required inventory table

| Source repository / SSH path | Branch / commit SHA | Key file / directory | Type | Keep? | Why | Evidence / hash | Permission |
|---|---|---|---|---|---|---|---|
| TO_AUDIT | NOT_VERIFIED | NOT_VERIFIED | code / benchmark / weight / dataset / demo / obsolete | TBD | TBD | TBD | TBD |

Types: shipping source; canonical research evidence; derived report; debug/temporary; unused experiment; restricted data; secret.

## Review checklist

1. Inspect the **real** VS Code/SSH workspace as well as GitHub; a file may exist only locally.
2. Run `git status`, inspect branches/commits and repository AGENTS instructions before copying.
3. Identify which code/config the final working app uses; require a code path or execution log.
4. Record filenames and hashes for curated files and reference original proof.
5. Keep non-shipping evidence in original archives, and list it here rather than mirroring huge folders.
6. Run focused regression/smoke checks after any migration and report observed results.
7. Explicitly flag restricted or unlicensed material and request owner decision rather than guessing.
