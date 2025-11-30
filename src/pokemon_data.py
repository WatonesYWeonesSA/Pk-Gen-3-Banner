from Gen3Save.Gen3Save import Gen3Save
#import pokebase as pb
import re

route = 'D:/Emuladores/RAVba/Pokemon - Edicion Zafiro (S) (V1.0) [f1].sav'

def get_party_data():
    sav = Gen3Save(route)
    data = []

    rich_data = "Player is exploring Rustboro City with 8 Badge and 107/202 Pokemon"
    # Usamos expresiones regulares para extraer la información
    location_match = re.search(r"exploring (.+?) with", rich_data)
    badges_match = re.search(r"with (\d+) Badge", rich_data)
    pokemon_match = re.search(r"(\d+)/(\d+) Pokemon", rich_data)

    # Asignamos los valores a variables independientes
    location = location_match.group(1) if location_match else None
    badges = int(badges_match.group(1)) if badges_match else None
    caught_pokemon = int(pokemon_match.group(1)) if pokemon_match else None

    for i, pkm in enumerate(sav.team):
        #pokebase_data = pb.pokemon(pkm.species['name'].lower())  # Asegúrate de que el nombre esté en minúsculas
        #id = pokebase_data.id

        pokemon = {
            'id': pkm.species['nid'],
            'specie': pkm.species['name'],
            'name': pkm.name,
            'level': pkm.level
        }
        data.append(pokemon)

    return {
        "name": sav.name,
        "time": sav.time,
        "location": location,
        "badges": badges,
        "caught_pokemon": caught_pokemon,
        "party": data
    }

if __name__ == "__main__":
    print(get_party_data())
