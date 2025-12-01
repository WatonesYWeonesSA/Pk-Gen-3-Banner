from .Gen3Save.Gen3Save import Gen3Save
from .pokemon import Pokemon

# Solo dumpea los datos de gen 3 (z/r/e - rf/vh)
def dump_gen3_data(route):
    sav = Gen3Save(route)
    data = []

    for i, pkm in enumerate(sav.team):
        pkmn_data = Pokemon(
            id = pkm.species['nid'],
            specie = pkm.species['name'],
            name = pkm.name,
            level = pkm.level
        )

        data.append(pkmn_data.get_as_dict())

    return {
        # Actualmente no se utilizan name y time... pero si gustas usarlas para otras cosas, el API te lo permite
        "name": sav.name,
        "time": sav.time,
        "party": data
    }