# 📦 Visor de Pokémon Gen 3 (`.sav`)
**El bannercito que nadie pidió, pero igual te va a salvar la vida.**

Bienvenido al glorioso visor de **Pokémon de la Gen 3** (GBA), la herramienta que armé porque llevaba demasiados meses streameando *Zafiro* y ya me daba lata mostrar el equipo con capturas feas o, peor, explicarlo a mano.  
Así que… sí, convertí la flojera en software. Como corresponde.

---

## 🌟 ¿Qué hace esta genialidad?

Este programilla lee tu archivo **`.sav`** de GBA y “pesca” todo lo que tenga forma de Pokémon:  
tanto tu **equipo** como tus cajas del **PC**.

De ahí extrae lo más básico y honesto del save mismo:

- Especie  
- Apodo (si existe)  
- Nivel  

Y luego le pregunta a **PokeAPI** por lo que falta para armar algo *bonito*, o sea:

- Sprite oficial  
- Tipos  

Con eso genera una **tarjeta visual por cada Pokémon**, minimalista, clara, y lista para mostrar en stream.

---

## 🖼️ ¿Qué incluye cada tarjeta?

- Sprite del Pokémon  
- Nombre o apodo  
- Nivel  
- Tipos  

Nada extra, nada fancy.  
Si el save está raro o corrupto, la tarjeta también quedará rara.  
Acá no hay “maquillaje”: se muestra lo que realmente está grabado.

---

## 📤 ¿Qué exporta?

Un **HTML listo para usar**:

- Lo puedes abrir en el navegador para revisarlo tranquilo.  
- O lo puedes poner como **Browser Source en OBS**, como hacen los streamers que se respetan.

Es literalmente plug-and-play. No hay magia negra.

---

# 🧩 Mini tutorial: ¿Cómo meter esto en OBS?

Porque si esto no termina en tu overlay, todo este esfuerzo fue en vano.

### 1. Genera el HTML  
Corre el programa, selecciona tu `.sav`, espera un poquito y te va a dejar un archivo tipo:

```
mi_equipo.html
```

### 2. Abre OBS  

### 3. Agrega una fuente  
→ **Agregar**  
→ **Browser**  
→ Le pones un nombre tipo *“Pokémons del Mostaza”* o como quieras.

### 4. Carga el HTML  
En el campo **URL**, escribe:

```
file:///C:/ruta/donde/guardaste/mi_equipo.html
```

Los **tres slashes** son obligatorios.  
Si no, OBS se te ríe.

### 5. Ajusta tamaño  
El HTML está diseñado para no romperse aunque lo achiques con violencia.

### 6. Listo  
Tu equipo/PC ahora vive en tu stream como Diosito Nintendo pretendió.

---

# 🤔 ¿Y por qué solo Gen 3?

Porque **no me pagan** para andar haciéndole reversing a los `.sav` de otras generaciones.

Así de simple.

El formato de Gen 3 ya es suficientemente esquizo como para querer meterme al pantano emocional que son los saves de DS, 3DS y Switch. Y antes de que alguien pregunte “oye, pero el PKHeX tiene documentación”… hermano, esa documentación está **pero malarda**, como si la hubieran escrito tres demonios distintos con un teclado mojado.

Gen 3, en cambio:

- Tiene estructura decente  
- La comunidad ya descifró casi todo  
- Y lo que falta se arregla con buena voluntad y un cafecito  

El objetivo de este visor es **mostrar tu equipo bonito, rápido y sin drama**, no meterme a rescatar `.sav` del inframundo.

¿Querís Gen 4, Gen 5 o más adelante?  
Hermano… **cuando Nintendo me pague sueldo**.  
O cuando **me donen en Patreon :p**  
Lo que llegue primero.

---

# 🧪 ¿Y van a agregar OT, stats o demás chucherías?

Depende.

Si la funcionalidad requiere seguir descosiendo los `.sav`, entonces la respuesta oficial es:

**Hermano… Patreon.**

No es por mala onda. Es que:

- Reversear más estructuras de Gen 3 es sudoku con trauma.  
- Meter datos avanzados implica pelear con subestructuras, checksums, flags raros y ese carnaval de bytes que Game Freak tiró sin mirar.  
- Y **además requeriría una GUI custom**, porque no voy a mostrar IVs en una planilla estilo Excel.  
- Y una GUI… hermano… la GUI es **paja**. Pura paja.  
  Sobre todo para una rata de backend que solo quiere imprimir structs y vivir en paz.

Si algún día llega financiamiento, donaciones o un milagro del cosmos, entonces sí:

**OT, stats, IVs, EVs, naturaleza, habilidad, amistad, moveset, ribbons y hasta el horóscopo del Pokémon.**

Pero por ahora, nos quedamos con la versión simple:  
**minimalista, visual y útil para streamers sin llorar bytes extra.**

---

# ❓ FAQ rápido

### ¿Puedo editar las tarjetas?  
Sí, si sabes HTML/CSS.  
Si no, mejor no toques o vas a generar una nueva forma de sufrimiento digital.

### ¿Por qué no agregas más datos?  
Porque no quiero hacer PKHeX 2.0 yo solo a punta de sufrimiento.

### ¿Se puede usar en videos monetizados?  
Sí, pero con crédito en pantalla.  
Si no, **te tiramos un Nintendo** y ya sabes cómo termina eso.

---

# ❤️ Créditos

Hecho con amor, café, cansancio y probablemente un par de berrinches.  
Si te sirve, bacán.  
Si haces plata con esto, **pon el crédito o activamos modo Nintendo**.
