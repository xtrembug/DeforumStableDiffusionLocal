@echo off

:: Run all commands using this script's directory as the working directory
:: copy from https://github.com/sd-webui/stable-diffusion-webui/blob/master/webui.cmd
cd %~dp0

set v_conda_env_name=dsd
echo Environment name is set as %v_conda_env_name%

set v_paths=%ProgramData%\miniconda3
set v_paths=%v_paths%;%USERPROFILE%\miniconda3
set v_paths=%v_paths%;%ProgramData%\anaconda3
set v_paths=%v_paths%;%USERPROFILE%\anaconda3

for %%a in (%v_paths%) do (
  IF NOT "%v_custom_path%"=="" (
    set v_paths=%v_custom_path%;%v_paths%
  )
)

for %%a in (%v_paths%) do (
  if EXIST "%%a\Scripts\activate.bat" (
    SET v_conda_path=%%a
    echo anaconda3/miniconda3 detected in %%a
    goto :CONDA_FOUND
  )
)

IF "%v_conda_path%"=="" (
  echo anaconda3/miniconda3 not found. Install from here https://docs.conda.io/en/latest/miniconda.html
  pause
  exit /b 1
)

:CONDA_FOUND
call "%v_conda_path%\Scripts\activate.bat" "%v_conda_env_name%"

set PYTHONPATH=%~dp0
python run.py --enable_animation_mode --settings "./examples/anim.txt"


cmd \k

:: RUN PY - ADD DATE TO FOLDER
::def get_output_folder(output_path, batch_folder):
::    out_path = os.path.join(output_path,time.strftime('%Y-%m'))
::    if batch_folder != "":
::        batch_folder = batch_folder + time.strftime('_%y%m%d_%H%M')
 ::       out_path = os.path.join(out_path, batch_folder)
 ::   os.makedirs(out_path, exist_ok=True)
 ::   return out_path

