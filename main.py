"""make.fun entry: news-image-20261119, account 4 (lathixbt).

Copies the pre-built entry.png (1024x1024, one-page newspaper front page
summing up Thursday 19 November 2026) byte-for-byte into the directory
named by MAKEFUN_OUTPUT_DIR (default /output).

Python 3.13, standard library only. Writes nothing to the current
working directory. Verifies the copied file's size and SHA-256 afterwards.
"""

import hashlib
import os
import shutil
import sys

ENTRY_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, ENTRY_NAME)

    with open(src, "rb") as f:
        digest_src = hashlib.sha256(f.read()).hexdigest()
    size_src = os.path.getsize(src)

    shutil.copyfile(src, dst)

    with open(dst, "rb") as f:
        digest_dst = hashlib.sha256(f.read()).hexdigest()
    size_dst = os.path.getsize(dst)

    if size_dst != size_src or digest_dst != digest_src:
        print("ERROR: copied file does not match source", file=sys.stderr)
        print("  source: %d bytes sha256 %s" % (size_src, digest_src),
              file=sys.stderr)
        print("  copied: %d bytes sha256 %s" % (size_dst, digest_dst),
              file=sys.stderr)
        return 1

    print("wrote %s (%d bytes, sha256 %s)" % (dst, size_dst, digest_dst))
    print("entry: Thursday 19 November 2026 — 34 stories, one page")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
