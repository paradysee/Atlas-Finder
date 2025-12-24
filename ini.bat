@echo off
title Atlas Finder
color 0A

echo.
echo ================================
echo        ATLAS FINDER
echo ================================
echo.


cd /d "%~dp0"

echo [*] Instalando requerimientos...
pip install --upgrade pip >nul 2>&1
pip install -r requeriments.txt


REM Ejecutar Atlas
python main.py

echo.
pause
