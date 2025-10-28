@echo off

:: Define o tamanho da janela do console: 150 colunas de largura, 50 linhas de altura
mode con: cols=150 lines=50

:: Inicia o Python maximizado (como antes)
start /max python GameRpg.py

:: Pausa no final
pause
