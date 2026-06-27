@echo off
set "BASE=C:\Users\enzov\OneDrive\Documentos\Claude\Projects\UFABC 2026.2"
del "%BASE%\publish.zip" 2>nul
powershell -NoProfile -Command "Compress-Archive -Path '%BASE%\publish\*' -DestinationPath '%BASE%\publish.zip' -Force"
powershell -NoProfile -Command "if (Test-Path '%BASE%\publish.zip') { 'OK ' + (Get-Item '%BASE%\publish.zip').Length } else { 'FALHOU' }" > "%BASE%\_zip_status.txt"
