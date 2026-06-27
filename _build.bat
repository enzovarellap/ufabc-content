@echo off
cd /d "C:\Users\enzov\OneDrive\Documentos\Claude\Projects\UFABC 2026.2"
set "PYEXE="
where py >nul 2>nul && set "PYEXE=py"
if not defined PYEXE ( where python >nul 2>nul && set "PYEXE=python" )
if not defined PYEXE (
  echo PYTHON_NAO_ENCONTRADO> _build_log.txt
  goto :eof
)
%PYEXE% build-site.py > _build_log.txt 2>&1
