#!/usr/bin/env python3
"""Todo <use xlink:href="#X"> tem um no com id="X"? Uso: check.py guia.html"""
import io, re, sys
p = sys.argv[1]
s = io.open(p, encoding='utf-8').read()
usados = set(re.findall(r'xlink:href="#([^"]+)"', s)) | set(re.findall(r'(?<!xlink:)\shref="#(MJX[^"]+)"', s))
definidos = set(re.findall(r'\sid="([^"]+)"', s))
faltando = sorted(usados - definidos)
print('%s: %d glifos referenciados, %d ids definidos' % (p.split('/')[-1], len(usados), len(definidos)))
if faltando:
    print('  ERRO: %d referencias sem definicao: %s' % (len(faltando), faltando[:12]))
    sys.exit(1)
print('  OK: todo <use> tem alvo')
