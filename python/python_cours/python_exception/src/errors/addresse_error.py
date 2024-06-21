

class AddresseError(Exception):
    def __init__(self,value, is_code_postal_error:bool) -> None:
        
        super().__init__(f"Le code postal  n'est pas correct ou la rue n'est pas entierement en majuscule : {value}")


def delete_file(file_names):
    if os.path.exists(file_names):
        os.remove(file_names)