rem Katana3.7 with 3Delight and USD

set "KATANA_VERSION=4.0v1.010028b"
set "DEFAULT_RENDERER=dl"

set "KATANA_HOME=C:\Program Files\Katana%KATANA_VERSION%"
set "DELIGHT=C:\Program Files\3Delight"
set "DLFK_INSTALL_PATH=%DELIGHT%\3DelightForKatana"
set "DL_DISPLAYS_PATH=%DELIGHT%\displays"
set "DL_SHADERS_PATH=%DELIGHT%\shaders"

set "KQ_NUM_AGENTS=4"
set "KATANA_OVERRIDE_ALLOW_CONCURRENT_LIVE_RENDERS=1"
set "KATANA_TAGLINE=3Delight + USD + OCIO"
set "OCIO=C:\Program Files\OCIO\aces_1.0.3\config.ocio"
set "PATH=%PATH%;%KATANA_HOME%\bin;%KATANA_HOME%\plugins\Resources\Usd\lib;C:\Program Files\3Delight\bin"
set "KATANA_RESOURCES=C:\Users\abelv\Documents\KatanaHomePipeline\KatanaResources;%KATANA_HOME%\plugins\Resources\Usd\plugin;%DLFK_INSTALL_PATH%"

"%KATANA_HOME%\bin\katanaBin.exe"
