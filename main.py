#!/usr/bin/env python3
"""Entry point for the news-image-20261119 entry (acct4, MAP-LED).

Copies the pre-rendered entry.png (a 1024x1024 newspaper infographic
summing up Thursday 19 November 2026: the world map as the hero, with
6 story callouts on it and a full 33-story index below) into the
directory named by MAKEFUN_OUTPUT_DIR (default /output).

The image is fixed: this program never draws, downloads, or modifies
anything. It only copies the file that ships in this repository, so
both grader runs write identical bytes.

Standard library only. Deterministic: the same bytes are written on
every run.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit(f"entry.png not found next to {__file__}")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"copied {src} -> {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
