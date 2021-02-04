rem Katana4.0v2 with Redshift, USD and Redshift

set "KATANA_VERSION=4.0v2"

set "KATANA_HOME=C:\Program Files\Katana%KATANA_VERSION%"
set "REDSHIFT_HOME=C:\ProgramData\Redshift\bin"
set "REDSHIFT4KATANA_HOME=C:\ProgramData\Redshift\Plugins\Katana\4.0v1"

set DEFAULT_RENDERER=Redshift
set "KATANA_TAGLINE=Redshift + USD"


set "PATH=%PATH%;%REDSHIFT_HOME%;%KATANA_HOME%\bin;%KATANA_HOME%\plugins\Resources\Usd\lib"
set "KATANA_RESOURCES=C:\Users\abelv\Documents\KatanaHomePipeline\KatanaResources;%KATANA_HOME%\plugins\Resources\Usd\plugin;%REDSHIFT4KATANA_HOME%"

"%KATANA_HOME%\bin\katanaBin.exe"
