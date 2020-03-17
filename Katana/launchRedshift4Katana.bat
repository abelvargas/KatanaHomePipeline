rem Redshift for Katana script

set "KATANA_VERSION=3.5v2"

set "KATANA_HOME=C:\Program Files\Katana%KATANA_VERSION%"
set "REDSHIFT_HOME=C:\ProgramData\Redshift\bin"
set "REDSHIFT4KATANA_HOME=C:\ProgramData\Redshift\Plugins\Katana\3.2v1"

set DEFAULT_RENDERER=Redshift
set "KATANA_TAGLINE=With Redshift 2.6"

set REDSHIFT_CACHE_BUDGET=
set REDSHIFT_CACHE_FOLDER=
set REDSHIFT_SELECTED_CUDA_DEVICES=

set "PATH=%REDSHIFT_HOME%;%PATH%;%KATANA_HOME%\bin;%KATANA_HOME%\plugins\Resources\Usd\lib"
set "KATANA_RESOURCES=%REDSHIFT4KATANA_HOME%;C:\Users\abelv\Documents\KatanaHomePipeline\KatanaResources"
"%KATANA_HOME%\bin\katanaBin.exe;%KATANA_HOME%\plugins\Resources\Usd\plugin"
