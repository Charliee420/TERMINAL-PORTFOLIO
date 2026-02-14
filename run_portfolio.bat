@echo off
title Terminal Portfolio
color 0A
cls
echo.
echo ================================
echo  TERMINAL PORTFOLIO LAUNCHER
echo ================================
echo.
echo Choose an option:
echo.
echo [1] Run Basic Portfolio
echo [2] Run Enhanced Portfolio (Recommended)
echo [3] Open Web Version in Browser
echo [4] Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    cls
    python portfolio.py
) else if "%choice%"=="2" (
    cls
    python portfolio_enhanced.py
) else if "%choice%"=="3" (
    start index.html
) else if "%choice%"=="4" (
    exit
) else (
    echo Invalid choice. Please try again.
    timeout /t 2 >nul
    goto :start
)
