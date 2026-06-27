@echo off
cd /d "C:\Users\enzov\OneDrive\Documentos\Claude\Projects\UFABC 2026.2"
rem limpeza forte primeiro (mata residuos com espaco que o OneDrive possa ter restaurado)
powershell -NoProfile -Command "Remove-Item -LiteralPath 'publish' -Recurse -Force -ErrorAction SilentlyContinue; Remove-Item -LiteralPath 'publish.zip' -Force -ErrorAction SilentlyContinue"
set "PYEXE="
where py >nul 2>nul && set "PYEXE=py"
if not defined PYEXE ( where python >nul 2>nul && set "PYEXE=python" )
if not defined PYEXE (
  echo PYTHON_NAO_ENCONTRADO> _build_log.txt
  goto :eof
)
%PYEXE% build-site.py > _build_log.txt 2>&1
