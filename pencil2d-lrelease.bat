
pushd ..\pencil2d

%QTDIR%\bin\lrelease pencil2d.pro
git add .
git commit -m "lrelease: generating qm files"

popd