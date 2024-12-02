
set ACCESS_TOKEN=%BITCUCKET_ACCESS_TOKEN%
set URL=https://api.bitbucket.org/2.0/repositories/chchwy/pencil2d/downloads
set VERSION=0.7.0

curl -X POST -H "Authorization: Bearer %ACCESS_TOKEN%" ^
  %URL% ^
  --progress-bar ^
  -F files=@pencil2d-win32-%VERSION%.zip ^
  -F files=@pencil2d-win64-%VERSION%.zip ^
  -F files=@pencil2d-winxp-%VERSION%.zip ^
  -F files=@pencil2d-mac-%VERSION%.zip ^
  -F files=@pencil2d-mac-legacy-%VERSION%.zip ^
  -F files=@pencil2d-linux-i386-%VERSION%.AppImage ^
  -F files=@pencil2d-linux-amd64-%VERSION%.AppImage
