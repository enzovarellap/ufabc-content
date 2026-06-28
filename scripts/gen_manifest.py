#!/usr/bin/env python3
"""Gera manifest.json com a lista de arquivos de cada disciplina.

Fonte: `git ls-tree -r --name-only HEAD` (reflete exatamente o que está no
repositório/commit atual). Roda igual localmente e no GitHub Actions.

O dashboard (index.html) lê este manifest de uma vez só, em vez de fazer ~18
chamadas à API do GitHub (que tem limite de 60/h e falha no 1º carregamento).
"""
import json, subprocess, sys, datetime, os

SUBFOLDERS = ("guias", "listas", "material")

def tracked_files():
    # git ls-files = tudo que está rastreado/no índice (inclui arquivos cloud-only
    # do OneDrive que não estão materializados no disco). No GitHub Actions (checkout
    # limpo) equivale ao conteúdo do repositório.
    out = subprocess.check_output(
        ["git", "ls-files"],
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        text=True,
    )
    return [l for l in out.splitlines() if l.strip()]

def build():
    disciplines = {}
    for path in tracked_files():
        parts = path.split("/")
        # Disciplinas/<disc>/<sub>/<file...>
        if len(parts) >= 4 and parts[0] == "Disciplinas" and parts[2] in SUBFOLDERS:
            disc = f"{parts[0]}/{parts[1]}"
            sub = parts[2]
            fname = "/".join(parts[3:])  # normalmente só o nome do arquivo
            disciplines.setdefault(disc, {s: [] for s in SUBFOLDERS})
            disciplines[disc][sub].append(fname)
    for disc in disciplines.values():
        for s in SUBFOLDERS:
            disc[s].sort(key=str.lower)
    # sem timestamp: assim o manifest só muda quando a lista de arquivos muda
    # (a Action só recommita quando há diferença real).
    return {"disciplines": disciplines}

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    manifest = build()
    out_path = os.path.join(root, "manifest.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
        f.write("\n")
    n = sum(len(v[s]) for v in manifest["disciplines"].values() for s in SUBFOLDERS)
    print(f"manifest.json gerado: {len(manifest['disciplines'])} disciplinas, {n} arquivos.")

if __name__ == "__main__":
    main()
