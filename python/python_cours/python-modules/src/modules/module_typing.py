
from typing import Literal


def sport_prefere(sport:Literal['foot','hockey'])-> None:
    print("votre sport preferé : "+sport)
    
sport_prefere('foot')