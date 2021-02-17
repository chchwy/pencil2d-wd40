
call "F:\Qt\5.15.2\msvc2019_64\bin\qtenv2.bat"

pushd ..\pencil2d

lrelease pencil2d.pro
git add .
git commit -m "lrelease: generating qm files"

popd