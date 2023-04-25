@echo off
title Mis Claves Wifi 
color F1
mode 140,50
:Inicio
echo.
echo.
echo       ==============================================================================================================================
echo                                                                   Menu
echo       ==============================================================================================================================
echo.
echo                1. Presiona ENTER para ver todas las redes y escribe el nombre de la red para saber su clave.       
echo.
echo       ==============================================================================================================================
echo.
echo.

set/p Menu=Enter para ver redes=

if "%Menu%"== "1" (goto :1)

echo.

:1
netsh wlan show profile
set /p escribir=Escribe el nombre de la red y presiona Enter para ver informacion y clave=
netsh wlan show profile name=%escribir% key=clear
pause
cls
(goto :Inicio)