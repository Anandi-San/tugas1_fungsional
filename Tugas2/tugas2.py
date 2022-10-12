import collections

PokemonCards = collections.namedtuple('PokemonCard', ['type','pokemon'])

class namepokemon:
    type = "pokemon Type".split()
    Name = "Bulbasur Venusaur Charmeloen Charizad Squirtle Pidgey Blastoise".split()

    def __init__(self):
        self._cards = [PokemonCards(type, Pokemon) for Pokemon in self.Name for type in self.type]

    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

print(namepokemon()[2])
