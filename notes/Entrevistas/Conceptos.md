Target encoding.

**Tu respuesta:** Propusiste un enfoque iterativo y heurístico. **Feedback del Experto:** Es un enfoque pragmático muy valorado. En una startup, "lo perfecto es enemigo de lo bueno".

- **Refinamiento técnico:** Para el usuario nuevo (Cold Start), la solución estándar es pasar de un modelo de _Filtrado Colaborativo_ a uno basado en **Contenido (Content-based Filtering)** o **Metadatos**.
    
- **Estrategia:** Si no conozco sus compras, uso su **geolocalización**, el **dispositivo** desde el que se conecta o la **fuente** de donde vino (ej. un anuncio de Instagram de zapatillas). Con eso, recomiendas lo más popular en ese segmento (heurística) hasta que el usuario genera su primer "clic".

