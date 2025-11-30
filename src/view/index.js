function fetchAndDisplayPartyData() {
    fetch('/API/Game')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            for (let i = 0; i < 6; i++) {
                const bg = document.getElementById(`poke-bg-${i}`);
                const image = document.getElementById(`pk-img-${i}`);
                const level = document.getElementById(`lvl-${i}`);
                const name = document.getElementById(`name-${i}`);

                if (i < data.party.length) {
                    const pokemon = data.party[i];

                    if (bg) {
                        bg.classList.add("pk_background");
                        setColor(pokemon.specie, bg);
                    }

                    if (image) {
                        image.classList.add("pk_img");
                        image.style.backgroundImage = `url(https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${pokemon.id}.png)`;
                    }

                    if (level) level.textContent = `Lvl: ${pokemon.level}`;
                    if (name) name.textContent = pokemon.name;
                } else {
                    if (bg) {
                        bg.classList.remove("pk_background");
                        bg.style.background = ''; // Reset background
                    }
                    if (image) {
                        image.classList.remove("pk_img");
                        image.style.backgroundImage = '';
                    }
                    if (level) level.textContent = '';
                    if (name) name.textContent = '';
                }
            }
        })
        .catch(error => {
            console.error('Error fetching party data:', error);
        });
}

async function setColor(specie, bg) {
    const pokemonTypeColors = {
        normal: '#A8A77A',
        fire: '#EE8130',
        water: '#6390F0',
        electric: '#F7D02C',
        grass: '#7AC74C',
        ice: '#96D9D6',
        fighting: '#C22E28',
        poison: '#A33EA1',
        ground: '#E2BF65',
        flying: '#A98FF3',
        psychic: '#F95587',
        bug: '#A6B91A',
        rock: '#B6A136',
        ghost: '#735797',
        dragon: '#6F35FC',
        dark: '#705746',
        steel: '#B7B7CE',
        fairy: '#D685AD'
    };

    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${specie.toLowerCase()}`);
        const data = await response.json();
        const types = data.types.map(typeInfo => typeInfo.type.name);

        if (types.length === 2) {
            bg.style.background = `linear-gradient(to bottom right, ${pokemonTypeColors[types[0]]}, #000000, ${pokemonTypeColors[types[1]]})`;
        } else {
            bg.style.background = `linear-gradient(to bottom right, ${pokemonTypeColors[types[0]]}, #000000)`;
        }
    } catch (error) {
        console.error('Error fetching Pokémon data:', error);
        bg.style.background = 'linear-gradient(to bottom right, #000000, #000000)';
    }
}

fetchAndDisplayPartyData();
setInterval(fetchAndDisplayPartyData, 15000);
