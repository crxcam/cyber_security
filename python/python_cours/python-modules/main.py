
import numpy as np
from src.base_functions import log_line


#  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser   // activer les script sur windows power shell
# -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

# pyenv = gestionnaire de environment pour python 
# pip install numpy  // install package numpy
# pip list          // voir le packet installe

# python -m venv <nom>      // creation un environment virtuel 
# pyenv global <numero version>  // changer l'environment
# .\my_env\Scripts\activate    //   activer environment
# .\my_env\Scripts\deactivate    // de-activer environment
#  pip freeze > requirement.txt  // creation de fichier dependances ()package.json
#  pip install requirement.txt  // installer les dependance 
#  python -m pydoc -w ./





#print(base_functions.log_line())


print(log_line())

numbers = np.array([1,2,3,5])
print(numbers)