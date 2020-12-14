REM https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/downloads#post

curl -s -u chchwy -X POST https://api.bitbucket.org/2.0/repositories/chchwy/pencil2d/downloads^
 -F files=@5/pencil2d-linux-amd64-0.6.5.AppImage^
 -F files=@5/pencil2d-linux-i386-0.6.5.AppImage^
 -F files=@5/pencil2d-mac-0.6.5.zip^
 -F files=@5/pencil2d-win32-0.6.5.zip^
 -F files=@5/pencil2d-win64-0.6.5.zip^
 -F files=@5/pencil2d-winxp-0.6.5.zip

