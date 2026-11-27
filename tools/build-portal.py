#!/usr/bin/env python3
"""Build a portal copy of Loose! (CrazyGames, itch.io and so on).

    python3 tools/build-portal.py crazygames

Writes dist/<portal>/ and dist/loose-<portal>-<version>.zip, ready to upload.
A portal copy has no Google sign-in, no Firebase library, no Google Analytics, no play stats,
no gifts, no update prompt and no outside links. Saves stay in the browser. The itch copy
alone sends the anonymous daily head count and the opt-out play stats (REST calls); others send nothing.
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r"[a-z0-9-]+", sys.argv[1]):
        sys.exit("usage: build-portal.py <portal-name, e.g. crazygames>")
    portal = sys.argv[1]
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    version = re.search(r"const VERSION = '([^']+)'", html).group(1)
    html, n = re.subn(r"<!--cloud-->.*?<!--/cloud-->\n?", "", html, flags=re.S)
    if n != 1:
        sys.exit("could not find the <!--cloud--> block in index.html")
    html = html.replace("<script>\n/* 2.27: where this copy runs.", f"<script>window.LOOSE_PORTAL='{portal}';</script>\n<script>\n/* 2.27: where this copy runs.", 1)
    if f"window.LOOSE_PORTAL='{portal}'" not in html:
        sys.exit("could not set the portal flag in index.html")
    # the portal hosts the files: no install prompt or offline worker
    html = html.replace('<link rel="manifest" href="manifest.webmanifest">\n', "")

    out = ROOT / "dist" / portal
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    for f in ("icon-192.png", "icon-512.png"):
        shutil.copy(ROOT / f, out / f)

    zpath = ROOT / "dist" / f"loose-{portal}-{version}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(out.iterdir()):
            z.write(f, f.name)
    print(f"{zpath.relative_to(ROOT)}  ({zpath.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
