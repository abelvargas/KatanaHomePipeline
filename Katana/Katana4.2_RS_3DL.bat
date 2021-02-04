rem Katana4.0v2 with Redshift, USD and Redshift

set "KATANA_VERSION=4.0v2"

set "KATANA_HOME=C:\Program Files\Katana%KATANA_VERSION%"
set "REDSHIFT_HOME=C:\ProgramData\Redshift\bin"
set "REDSHIFT4KATANA_HOME=C:\ProgramData\Redshift\Plugins\Katana\4.0v1"

set DEFAULT_RENDERER=Redshift
set "KATANA_TAGLINE=Redshift + USD"

set "DELIGHT=C:\Program Files\3Delight"
set "DLFK_INSTALL_PATH=%DELIGHT%\3DelightForKatana"
set "DL_DISPLAYS_PATH=%DELIGHT%\displays"
set "DL_SHADERS_PATH=%DELIGHT%\shaders"


set "PATH=%PATH%;%REDSHIFT_HOME%;%KATANA_HOME%\bin;%KATANA_HOME%\plugins\Resources\Usd\lib;C:\Program Files\3Delight\bin"
set "KATANA_RESOURCES=C:\Users\abelv\Documents\KatanaHomePipeline\KatanaResources;%KATANA_HOME%\plugins\Resources\Usd\plugin;%REDSHIFT4KATANA_HOME%;%DLFK_INSTALL_PATH%"

"%KATANA_HOME%\bin\katanaBin.exe"
