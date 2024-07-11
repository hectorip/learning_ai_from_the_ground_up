import re
import csv

"""This was almost in its entirity written by Claude"""
def parse_proposals(text):
    proposals = text.split('|')
    parsed_proposals = []
    for proposal in proposals:
        proposal = proposal.strip()
        copy_match = re.search(r'^(.*?)(?=<argumentos>)', proposal, re.DOTALL)
        copy = copy_match.group(1).strip() if copy_match else ""
        args_match = re.search(r'<argumentos>(.*?)</argumentos>', proposal, re.DOTALL)
        arguments = args_match.group(1).strip() if args_match else ""
        visual_match = re.search(r'<visual>(.*?)</visual>', proposal, re.DOTALL)
        visual = visual_match.group(1).strip() if visual_match else ""

        parsed_proposals.append({
            "copy": copy,
            "arguments": arguments,
            "visual": visual,
        })
    return parsed_proposals

def save_to_csv(proposals, filename):
    """Save the proposals to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['copy', 'arguments', 'visual']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for proposal in proposals:
            writer.writerow(proposal)

text="""¿Cocinar y limpiar? ¡Con Mabe, solo cocinar! Nuestras estufas con recubrimiento cerámico se limpian en un santiamén. Más tiempo para ti, menos para fregar. #MabeFacilita
<argumentos>Destaca la facilidad de limpieza y ahorro de tiempo, atractivo para jóvenes ocupados.</argumentos>
<visual>Video en cámara rápida: joven cocinando, derramando salsa, limpiando fácilmente y luego relajándose en el sofá con amigos.</visual>|

Navidad sin estrés: Cocina, disfruta y olvídate de la limpieza. Estufas Mabe con cerámica fácil de limpiar. Porque la fiesta continúa después de la cena. #NavidadMabe
<argumentos>Conecta con la temporada navideña y el deseo de disfrutar sin preocupaciones.</argumentos>
<visual>Imagen dividida: mitad superior muestra una cena navideña, mitad inferior la misma escena con gente bailando y la estufa limpia de fondo.</visual>|

Manchas rebeldes, ¿dónde? Estufas Mabe con cerámica mágica. Cocina sin miedo, limpia sin esfuerzo. Tu aliado culinario desde 1920. #MabeMagia
<argumentos>Usa un tono divertido y mágico, apelando a la historia de la marca y la innovación.</argumentos>
<visual>GIF animado: varita mágica tocando manchas en la estufa que desaparecen instantáneamente con destellos.</visual>|

¡Ups, se derramó la salsa! No pasa nada, con las estufas Mabe de cerámica fácil de limpiar. Cocina con pasión, limpia con diversión. #MabeNoStress

<argumentos>Aborda un problema común de forma ligera, mostrando la solución de Mabe.</argumentos>
<visual>Video corto: joven derrama salsa, expresión de pánico, luego sonríe al limpiar fácilmente. Termina guiñando a la cámara.</visual>|
Cenar, bailar, limpiar la estufa en un segundo y seguir la fiesta. Todo es posible con Mabe. Estufas con cerámica que se limpian más rápido que tus stories. #MabeRapidez
<argumentos>Compara la rapidez de limpieza con algo familiar para los jóvenes, como las redes sociales.</argumentos>
<visual>Secuencia de fotos estilo Instagram: cena, baile, limpieza rápida, más baile. La limpieza ocupa solo un cuadro pequeño.</visual>|

Tu estufa Mabe: El único testigo de tus experimentos culinarios que no te delatará. Cerámica fácil de limpiar, para chefs en entrenamiento. #MabeSecretos
<argumentos>Usa humor para conectar con jóvenes que están aprendiendo a cocinar.</argumentos>
<visual>Imagen cómica: estufa Mabe con ojos dibujados, guiñando uno, rodeada de intentos fallidos de cocina pero perfectamente limpia.</visual>|

Navidad 2024: Año nuevo, estufa nueva. Mabe con cerámica fácil de limpiar. Porque los propósitos de limpieza sí se cumplen con nosotros. #MabeAñoNuevo
<argumentos>Vincula el producto con los propósitos de año nuevo de forma humorística.</argumentos>
<visual>Imagen dividida: lado izquierdo muestra una vieja estufa sucia, lado derecho una estufa Mabe reluciente. En medio, una lista de propósitos tachados excepto "Mantener la cocina limpia".</visual>|
¿Quién dijo que cocinar era aburrido? Estufas Mabe: Fáciles de usar, más fáciles de limpiar. Tu compañera para aventuras culinarias desde 1920. #MabeAventura
<argumentos>Presenta la cocina como una aventura emocionante, apelando al espíritu joven.</argumentos>
<visual>Video corto: joven cocinando platos exóticos, haciendo malabares con ingredientes, todo termina con la estufa impecable y el chef sonriente.</visual>|
Estufa Mabe: El único electrodoméstico que te hace quedar bien con tu mamá y con tus amigos. Fácil de usar, más fácil de limpiar. #MabeParaTodos
<argumentos>Apela tanto a la aprobación familiar como a la vida social de los jóvenes.</argumentos>
<visual>Imagen dividida: arriba, una madre orgullosa mirando la cocina limpia; abajo, amigos impresionados durante una cena en casa.</visual>|
La fiesta sigue en la cocina con Mabe. Estufas con cerámica fácil de limpiar. Porque la diversión no termina cuando empieza la limpieza. #MabeFiesta
<argumentos>Asocia la cocina y la limpieza con conceptos divertidos y festivos.</argumentos>
<visual>GIF animado: jóvenes bailando en la cocina, uno limpia la estufa Mabe con un movimiento de baile, todos siguen la fiesta sin interrupción.</visual>
"""
parsed_proposals = parse_proposals(text)

for i, proposal in enumerate(parsed_proposals, 1):
    print(f"Propuesta {i}:")
    print(f"Copy: {proposal['copy']}")
    print(f"Argumentos: {proposal['arguments']}")

save_to_csv(parsed_proposals, 'propuestas_mabe_visual.csv')
