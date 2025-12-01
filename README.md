# 📦 Visor de Pokémon Gen 3 (`.sav`)
**El bannercito que nadie pidió, pero igual te va a salvar la vida.**

Bienvenido al glorioso visor de **Pokémon de la Gen 3** (GBA), la herramienta que armé porque llevaba demasiados meses streameando *Zafiro* y ya me daba lata mostrar el equipo con capturas feas o, peor, explicarlo a mano.  
Así que… sí, convertí la flojera en software. Como corresponde.

---

## 🌟 ¿Qué hace esta genialidad?

Este programilla lee tu archivo **`.sav`** de GBA y pesca todo lo que tenga forma de Pokémon:  
tanto tu **equipo** como tus cajas del **PC**.

De ahí extrae lo más básico y honesto del save:

- Especie  
- Apodo (si existe)  
- Nivel  

Luego consulta **PokeAPI** para obtener lo necesario para armar cada tarjeta visual:

- Sprite oficial  
- Tipos  

Con eso genera una **tarjeta por Pokémon**, minimalista y clara, lista para mostrar en stream.

---

## 🖼️ ¿Qué incluye cada tarjeta?

- Sprite  
- Especie o apodo  
- Nivel  
- Tipos  

Nada extra, nada inventado.  
Si tu save está raro, la tarjeta queda rara. Acá no maquillamos nada.

---

## 🌐 ¿Cómo se muestra todo esto?

El visor **no exporta archivos HTML**.  
Todo se sirve dinámicamente desde un **backend Flask** que actualiza la interfaz en tiempo real.

Puedes verlo en tu navegador en:

```
http://localhost:80
```

O agregarlo como **Browser Source en OBS** usando **esa misma URL**.  
Cuando tu `.sav` cambie, el banner se actualiza solo.

---

# 🤔 ¿Por qué solo Gen 3?

Porque **no me pagan** para andar haciéndole reversing a los saves de otras generaciones.

Gen 3 es suficiente caos.  
Lo demás es sufrimiento innecesario y documentación malarda.

¿Querís Gen 4, Gen 5 o más?  
Hermano… **Patreon**.  
O que Nintendo me pague sueldo.  
Lo que llegue primero.

---

# 🧪 ¿Y van a agregar OT, stats u otras chucherías?

Depende.

Si implica seguir pelando bytes del save → **Patreon, hermano**.

Además, para mostrar stats y otras cosas habría que hacer una **GUI custom**, y una GUI es paja para una rata de backend que solo quiere imprimir structs y vivir en paz.

Si algún día llega financiamiento, se agregará todo:  
**OT, stats, IVs, EVs, naturaleza, habilidad, amistad, moveset, ribbons y lo que pida la gente.**

Por ahora esto es simple, visual y útil para streamers sin llorar bytes extra.

---

# ❓ FAQ

### ¿Puedo editar las tarjetas?
Sí, si sabes HTML/CSS.  
Si no, mejor no toques.

### ¿Por qué no agregas más datos?
Porque no quiero hacer PKHeX yo solo.

### ¿Se puede usar en videos monetizados?
Sí, pero con crédito en pantalla.  
Si no, activamos modo Nintendo.

---

# ❤️ Créditos

Hecho con amor, café y un poquito de sufrimiento.  
Si te sirve, bacán.  
Si haces plata con esto, **pon el crédito**.
