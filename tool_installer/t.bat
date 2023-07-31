@echo off

REM Check if arguments are provided
if "%~1"=="" (
    echo No arguments provided. Exiting...
    exit /b
)

REM Set the path to the VBScript relative to the batch script
set "vbscript=%~dp0SearchToolScript.vbs"

REM Call the VBScript file with the provided arguments
cscript //nologo "%vbscript%" %*
