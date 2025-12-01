from .gen3_manager import dump_gen3_data

# Class para retornar excepcion
class UnsupportedGeneration(Exception):
    pass

# Funcion encargada de embeber datos de un sav de gen 3 hacia el engine
def get_sav_data(route: str, gen: int):
    match gen:
        case 3:
            return dump_gen3_data(route)
        case _:
            raise UnsupportedGeneration(f"[Error] Generation {gen} not supported")

if __name__ == "__main__":
    route = 'test.sav'
    sav = get_sav_data(route)
    print(sav)
