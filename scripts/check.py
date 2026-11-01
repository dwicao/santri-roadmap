#!/usr/bin/env python3
"""Validasi struktur santri-roadmap. Jalankan: python3 scripts/check.py"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
def err(msg):
    errors.append(msg)
    print("ERR:", msg)

# 1. cek root files
for f in ["README.md", "CONTRIBUTING.md", "LICENSE", "CODE_OF_CONDUCT.md"]:
    if not os.path.isfile(os.path.join(ROOT, f)):
        err(f"root file hilang: {f}")

# 2. cek roadmaps
rm_dir = os.path.join(ROOT, "roadmaps")
if not os.path.isdir(rm_dir):
    err("folder roadmaps/ tidak ada")
    sys.exit(1)
slugs = sorted([d for d in os.listdir(rm_dir) if os.path.isdir(os.path.join(rm_dir, d))])
print(f"roadmaps ditemukan: {slugs}")
if not slugs:
    err("tidak ada roadmap")
for slug in slugs:
    if not re.match(r"^[a-z0-9-]+$", slug):
        err(f"slug tidak valid: {slug} (harus huruf-kecil-dengan-strip)")
    rreadme = os.path.join(rm_dir, slug, "README.md")
    cdir = os.path.join(rm_dir, slug, "content")
    if not os.path.isfile(rreadme):
        err(f"{slug}: README.md hilang")
    if not os.path.isdir(cdir):
        err(f"{slug}: content/ hilang")
        continue
    files = [f for f in os.listdir(cdir) if f.endswith(".md")]
    if len(files) < 5:
        err(f"{slug}: content hanya {len(files)} file (minimal 5)")
    for f in files:
        if not re.match(r"^[a-z0-9-]+\.md$", f):
            err(f"{slug}: nama file tidak valid: {f}")
        p = os.path.join(cdir, f)
        txt = open(p, encoding="utf-8").read()
        if not txt.startswith("# "):
            err(f"{slug}/{f}: harus diawali '# Judul'")
        for wajib in ["**Target:**", "## Yang dipelajari", "## Cara belajar", "## Resources"]:
            if wajib not in txt:
                err(f"{slug}/{f}: tidak ada bagian '{wajib}'")

# 3. cek best-practices & questions
for d in ["best-practices", "questions", "scripts"]:
    if not os.path.isdir(os.path.join(ROOT, d)):
        err(f"folder {d}/ tidak ada")

# 4. cek README utama mendaftarkan semua roadmap
root_readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
for slug in slugs:
    if slug not in root_readme:
        err(f"README utama belum mendaftarkan: {slug}")
    rmd = open(os.path.join(rm_dir, slug, "README.md"), encoding="utf-8").read()
    # setiap README roadmap harus link balik ke content
    if "content/" not in rmd:
        err(f"{slug}/README.md tidak me-link ke content/")

print(f"\nSelesai. {len(errors)} error.")
sys.exit(1 if errors else 0)
