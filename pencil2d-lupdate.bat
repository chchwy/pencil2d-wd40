
call "F:\Qt\5.15.2\msvc2019_64\bin\qtenv2.bat"

pushd ..\pencil2d

call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"
lupdate pencil2d.pro
git add translations/pencil.ts
git commit -m "lupdate: update the source language"
git reset --hard

popd