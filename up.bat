@echo off

if exist tmp rmdir tmp /q /s >nul
if exist *.exe del *.exe /q /s >nul

CALL ids.bat
CALL link.bat

cmd /c railway up --service %SERVICE_ID%

pause >nul