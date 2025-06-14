@echo off
chcp 65001 >nul

if "%1"=="" (
    echo Usage: %~nx0 input.png [output.png]
    exit /b 1
)

if "%2"=="" (
    set "output=%~dpn1_darkened%~x1"
) else (
    set "output=%~2"
)

ffmpeg -i "%1" -vf ^
"split[original][alpha];^
[alpha]alphaextract[a];^
[original]format=yuv444p,lutyuv=y=negval:u=val:v=val,^
select=eq(n\,0)*isnan(alpha(alpha))[processed];^
[processed][a]alphamerge" ^
"%output%" -y 2>NUL || (
    echo 检测到无透明通道，使用简化流程...
    ffmpeg -i "%1" -vf "format=yuv444p,lutyuv=y=negval:u=val:v=val" "%output%" -y
)

echo 处理完成："%output%"