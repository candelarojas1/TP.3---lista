from lista import search, remove


# Lista de superhéroes
superheroes = [
    {'nombre': 'Linterna Verde', 'año_aparicion': 1940, 'casa_comic': 'DC', 'biografia': 'Un héroe con un anillo de poder.'},
    {'nombre': 'Wolverine', 'año_aparicion': 1974, 'casa_comic': 'Marvel', 'biografia': 'Tiene un esqueleto de adamantium y garras retráctiles.'},
    {'nombre': 'Dr. Strange', 'año_aparicion': 1963, 'casa_comic': 'DC', 'biografia': 'Un mago poderoso con una capa mágica.'},
    {'nombre': 'Iron Man', 'año_aparicion': 1963, 'casa_comic': 'Marvel', 'biografia': 'Un multimillonario con una armadura avanzada.'},
    {'nombre': 'Capitana Marvel', 'año_aparicion': 1968, 'casa_comic': 'Marvel', 'biografia': 'Tiene superpoderes cósmicos.'},
    {'nombre': 'Mujer Maravilla', 'año_aparicion': 1941, 'casa_comic': 'DC', 'biografia': 'Princesa amazona con traje icónico.'},
    {'nombre': 'Flash', 'año_aparicion': 1940, 'casa_comic': 'DC', 'biografia': 'El hombre más rápido del mundo.'},
    {'nombre': 'Star-Lord', 'año_aparicion': 1976, 'casa_comic': 'Marvel', 'biografia': 'Un aventurero espacial con una armadura especial.'},
    {'nombre': 'Batman', 'año_aparicion': 1939, 'casa_comic': 'DC', 'biografia': 'El caballero de la noche.'},
    {'nombre': 'Superman', 'año_aparicion': 1938, 'casa_comic': 'DC', 'biografia': 'El hombre de acero.'},
    {'nombre': 'Spiderman', 'año_aparicion': 1962, 'casa_comic': 'Marvel', 'biografia': 'El trepamuros.'},
]

#Elminar el nodo de Linterna verde
criterio = "nombre"
eliminar = "Linterna Verde"
result_delete = remove(superheroes, criterio , eliminar)
print(f'Eliminar {eliminar} resultado: {result_delete}')

# mostrar el año de aparición de Wolverine
index_wolverine = search(superheroes, 'nombre', 'Wolverine')
if index_wolverine is not None:
    print(f"Año de aparición de Wolverine: {superheroes[index_wolverine]['año_aparicion']}")

# cambiar la casa de Dr. Strange a Marvel
index_dr_strange = search(superheroes, 'nombre', 'Dr. Strange')
if index_dr_strange is not None:
    superheroes[index_dr_strange]['casa_comic'] = 'Marvel'

# mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
print("Superhéroes cuya biografía menciona 'traje' o 'armadura':")
for heroe in superheroes:
    if 'traje' in heroe['biografia'] or 'armadura' in heroe['biografia']:
        print(heroe['nombre'])

# mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
print("Superhéroes con fecha de aparición anterior a 1963:")
for heroe in superheroes:
    if heroe['año_aparicion'] < 1963:
        print(f"Nombre: {heroe['nombre']}, Casa: {heroe['casa_comic']}")

# mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
for nombre in ['Capitana Marvel', 'Mujer Maravilla']:
    index = search(superheroes, 'nombre', nombre)
    if index is not None:
        print(f"{nombre} pertenece a la casa: {superheroes[index]['casa_comic']}")

# mostrar toda la información de Flash y Star-Lord
for nombre in ['Flash', 'Star-Lord']:
    index = search(superheroes, 'nombre', nombre)
    if index is not None:
        print(f"Información de {nombre}: {superheroes[index]}")

# listar los superhéroes que comienzan con la letra B, M y S
print("Superhéroes que comienzan con la letra B, M y S:")
for heroe in superheroes:
    if heroe['nombre'][0] in ['B', 'M', 'S']:
        print(heroe['nombre'])

# determinar cuántos superhéroes hay de cada casa de comic
contar_casas = {'Marvel': 0, 'DC': 0}
for heroe in superheroes:
    if heroe['casa_comic'] in contar_casas:
        contar_casas[heroe['casa_comic']] += 1

print("Cantidad de superhéroes por casa de comic:")
for casa, cantidad in contar_casas.items():
    print(f"{casa}: {cantidad}")

