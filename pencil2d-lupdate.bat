
pushd ..\pencil2d

call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"
%QTDIR%\bin\lupdate pencil2d.pro
git add translations/pencil.ts
git commit -m "lupdate: update the source language"
git reset --hard

popd