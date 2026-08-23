#!/usr/bin/env python3
"""Concatena os fragmentos de um guia e injeta o tema. Uso: build.py <dir> <saida>"""
import glob, io, os, sys

d, out = sys.argv[1], sys.argv[2]
css = io.open(os.path.join(os.path.dirname(d.rstrip('/')), 'theme.css'), encoding='utf-8').read()
frags = sorted(glob.glob(os.path.join(d, '[0-9]*.html')))
assert frags, 'nenhum fragmento em ' + d
partes = []
for f in frags:
    t = io.open(f, encoding='utf-8').read()
    partes.append(t)
    print('  +', os.path.basename(f), len(t), 'chars')
html = '\n'.join(partes)
assert '/*THEME*/' in html, 'falta o marcador /*THEME*/'
html = html.replace('/*THEME*/', css)
# sanidade estrutural
for tag in ('<!DOCTYPE html>', '<body>', '</body>', '</html>'):
    assert tag in html, 'falta ' + tag
io.open(out, 'w', encoding='utf-8').write(html)
print('->', out, len(html), 'chars')
