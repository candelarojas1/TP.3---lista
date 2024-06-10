from lista import search, show_list, show_list_list

#Lista de entrenadores Pokémon
entrenadores = [
    {
        'nombre': 'Ash Ketchum',
        'torneos_ganados': 5,
        'batallas_perdidas': 20,
        'batallas_ganadas': 100,
        'pokemons': [
            {'nombre': 'Pikachu', 'nivel': 50, 'tipo': 'eléctrico', 'subtipo': None},
            {'nombre': 'Charizard', 'nivel': 85, 'tipo': 'fuego', 'subtipo': 'volador'},
            {'nombre': 'Bulbasaur', 'nivel': 40, 'tipo': 'planta', 'subtipo': 'veneno'}
        ]
    },
    {
        'nombre': 'Misty',
        'torneos_ganados': 3,
        'batallas_perdidas': 15,
        'batallas_ganadas': 80,
        'pokemons': [
            {'nombre': 'Starmie', 'nivel': 45, 'tipo': 'agua', 'subtipo': 'psíquico'},
            {'nombre': 'Gyarados', 'nivel': 60, 'tipo': 'agua', 'subtipo': 'volador'}
        ]
    },
    {
        'nombre': 'Brock',
        'torneos_ganados': 2,
        'batallas_perdidas': 25,
        'batallas_ganadas': 70,
        'pokemons': [
            {'nombre': 'Onix', 'nivel': 70, 'tipo': 'roca', 'subtipo': 'tierra'},
            {'nombre': 'Geodude', 'nivel': 35, 'tipo': 'roca', 'subtipo': 'tierra'}
        ]
    },
    {
        'nombre': 'Gary Oak',
        'torneos_ganados': 4,
        'batallas_perdidas': 10,
        'batallas_ganadas': 90,
        'pokemons': [
            {'nombre': 'Blastoise', 'nivel': 75, 'tipo': 'agua', 'subtipo': None},
            {'nombre': 'Arcanine', 'nivel': 80, 'tipo': 'fuego', 'subtipo': None}
        ]
    }
]

# Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(entrenadores, nombre_entrenador):
    index = search(entrenadores, 'nombre', nombre_entrenador)
    if index is not None:
        return len(entrenadores[index]['pokemons'])
    return 0

nombre_entrenador = 'Ash Ketchum'
print(f"{nombre_entrenador} tiene {cantidad_pokemons(entrenadores, nombre_entrenador)} Pokémons.")

# Listar los entrenadores que hayan ganado más de tres torneos
ganadores_mas_tres = [e for e in entrenadores if e['torneos_ganados'] > 3]
show_list("Entrenadores con más de tres torneos ganados:", ganadores_mas_tres)

# El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel(entrenadores):
    entrenador_mayor_torneos = max(entrenadores, key=lambda x: x['torneos_ganados'])
    pokemon_max_nivel = max(entrenador_mayor_torneos['pokemons'], key=lambda x: x['nivel'])
    return entrenador_mayor_torneos, pokemon_max_nivel

entrenador, pokemon = pokemon_mayor_nivel(entrenadores)
print(f"El Pokémon de mayor nivel del entrenador con más torneos ganados ({entrenador['nombre']}) es {pokemon['nombre']} con nivel {pokemon['nivel']}.")

# Mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_entrenador_y_pokemons(entrenadores, nombre_entrenador):
    index = search(entrenadores, 'nombre', nombre_entrenador)
    if index is not None:
        show_list(f"Información del entrenador {nombre_entrenador}:", [entrenadores[index]])
        show_list_list(f"Pokémons de {nombre_entrenador}:", "Pokémons:", [{'nombre': nombre_entrenador, 'sublist': entrenadores[index]['pokemons']}])

nombre_entrenador = 'Misty'
mostrar_entrenador_y_pokemons(entrenadores, nombre_entrenador)

# Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%
entrenadores_alto_porcentaje = [e for e in entrenadores if (e['batallas_ganadas'] / (e['batallas_ganadas'] + e['batallas_perdidas'])) * 100 > 79]
show_list("Entrenadores con más del 79% de batallas ganadas:", entrenadores_alto_porcentaje)

#Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
def entrenadores_pokemon_tipo_subtipo(entrenadores):
    result = []
    for entrenador in entrenadores:
        tipos_pokemons = [(p['tipo'], p['subtipo']) for p in entrenador['pokemons']]
        if any(tipo == 'fuego' for tipo, _ in tipos_pokemons) and any(tipo == 'planta' for tipo, _ in tipos_pokemons):
            result.append(entrenador)
        elif any(tipo == 'agua' and subtipo == 'volador' for tipo, subtipo in tipos_pokemons):
            result.append(entrenador)
    return result

entrenadores_tipos = entrenadores_pokemon_tipo_subtipo(entrenadores)
show_list("Entrenadores con Pokémons tipo fuego/planta o agua/volador:", entrenadores_tipos)

# El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    index = search(entrenadores, 'nombre', nombre_entrenador)
    if index is not None:
        pokemons = entrenadores[index]['pokemons']
        promedio = sum(p['nivel'] for p in pokemons) / len(pokemons)
        return promedio
    return 0


nombre_entrenador = 'Ash Ketchum'
print(f"El promedio de nivel de los Pokémons de {nombre_entrenador} es {promedio_nivel_pokemons(entrenadores, nombre_entrenador):.2f}.")

#Determinar cuántos entrenadores tienen a un determinado Pokémon
def entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return sum(1 for e in entrenadores if any(p['nombre'] == nombre_pokemon for p in e['pokemons']))

nombre_pokemon = 'Pikachu'
print(f"{entrenadores_con_pokemon(entrenadores, nombre_pokemon)} entrenadores tienen un {nombre_pokemon}.")

#Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        nombres_pokemons = [p['nombre'] for p in entrenador['pokemons']]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            resultado.append(entrenador)
    return resultado

entrenadores_repetidos = entrenadores_con_pokemons_repetidos(entrenadores)
show_list("Entrenadores con Pokémons repetidos:", entrenadores_repetidos)

#Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especificos(entrenadores):
    pokemons_busqueda = {'Tyrantrum', 'Terrakion', 'Wingull'}
    resultado = []
    for entrenador in entrenadores:
        if any(p['nombre'] in pokemons_busqueda for p in entrenador['pokemons']):
            resultado.append