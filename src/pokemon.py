# Interfaz para datos de los Pokemon, en caso de que en algun momento se le den otro uso, ahi esta :B
class Pokemon():
    def __init__(self, id: int, name: str, level: int, specie: str):
        self.id = id
        self.name = name
        self.level = level
        self.specie = specie

    def get_as_dict(self):
        return {
            'id': self.id,
            'specie': self.specie,
            'name': self.name,
            'level': self.level
        }