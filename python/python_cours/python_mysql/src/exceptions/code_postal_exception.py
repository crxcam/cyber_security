

class CodePostalException(Exception):
    def __init__(self,value,is_code_postal) -> None:
        super().__init__(       f"Le code postal  n'est pas correct ou la rue n'est pas entierement en majuscule : {value}")
