

SET QTDIR="F:\Qt\5.12.10\msvc2017_64"
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"

md "ts-tmp"
del /f/s/q "ts-tmp"

echo "=====Extracting zip====="
"C:\Program Files\7-Zip\7z.exe" x "pencil2d_pencil2d_translations-pencil-ts--master.zip" -o"ts-tmp" -y

pushd ts-tmp
setlocal enableDelayedExpansion
@echo off
for %%F in (*.ts) do (
  set "name=%%F"
  ren "!name!" "!name:translations-pencil-ts--master=pencil!"
)
endlocal
popd

xcopy ts-tmp ..\pencil2d\translations /y /i
del /f/s/q "ts-tmp" > nul
rmdir /s/q "ts-tmp"

pushd ..\pencil2d

pushd translations
echo "=====Commit ts files====="
git clean -fdx
git add .
git commit -m "Sync translations from Transifex"
popd

echo "=====Updating source language====="

%QTDIR%\bin\lupdate pencil2d.pro
git add translations/pencil.ts
git commit -m "lupdate: update the source language"
git reset --hard

echo "====Generate qm files====="
%QTDIR%\bin\lrelease pencil2d.pro
git add .
git commit -m "lrelease: generating qm files"

popd

echo Done
PAUSE