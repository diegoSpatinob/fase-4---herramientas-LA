# Herramienta de Learning Analytics para el análisis de comentarios estudiantiles y prácticas docentes mediante PLN

**Asignatura:** Ciencia de los Datos  
**Docente:** Ing. Jorge Maldonado  
**Integrantes:** Diego Patiño · María José Vire  
**Carrera:** Computación  
**Universidad de Cuenca**

## Descripción

Este repositorio contiene la prueba de concepto de una herramienta de **Teaching Analytics** orientada a transformar comentarios abiertos de estudiantes en evidencia organizada para apoyar la reflexión y la toma de decisiones del docente.

La herramienta no emite juicios automáticos sobre el desempeño del profesor ni ejecuta intervenciones por sí sola. Su propósito es apoyar una decisión humana: **qué prácticas docentes conviene mantener, revisar o mejorar** a partir de patrones observados en los comentarios estudiantiles.

---

## Canvas de diseño de la herramienta LA

### 1. Actor y decisión

**Actor principal:** docente universitario.

A partir de los comentarios estudiantiles, decide qué prácticas mantener, revisar o mejorar. Hoy puede apoyarse en lectura manual, normalmente tras evaluaciones o períodos académicos; la herramienta facilita patrones y evidencia textual. **La periodicidad institucional está por confirmar.**

### 2. Problema educativo

El volumen y carácter abierto de los comentarios dificultan identificar sistemáticamente prácticas recurrentes y oportunidades de mejora.

Se plantea explorar esta necesidad en la Universidad de Cuenca; todavía faltan **evidencia institucional y una estimación de las personas afectadas**.

### 3. Pregunta analítica

> **¿Qué prácticas docentes efectivas, malfuncionales o ambiguas se identifican recurrentemente en los comentarios estudiantiles?**

- **Nivel:** descriptivo y diagnóstico.
- **Tipo:** enseñanza (**Teaching Analytics**).

### 4. Datos e indicadores

**Fuente:** comentarios abiertos de retroalimentación estudiantil; asignatura y período, si existen.

**Variables:** `id_comentario`, `comentario`, `practica_docente`, `valoracion`, `asignatura`, `periodo_academico` (ver diccionario de datos, Fase 2).

**Indicadores:**

- **I01:** total de comentarios únicos.
- **I02:** comentarios únicos por práctica.
- **I03:** (comentarios que mencionan la práctica / total de comentarios) × 100.
- **I04:** (comentarios con valoración específica de la práctica / comentarios que mencionan esa práctica) × 100.

Un comentario puede mencionar varias prácticas, por lo que los porcentajes entre prácticas no tienen que sumar 100 %.

### 5. Intervención

El flujo propuesto es:

**Panorama general → análisis de una práctica → comentarios desidentificados → decisión docente**

El docente decide qué práctica mantener, revisar o mejorar.

La recurrencia funciona como una **señal de revisión**, sin umbral automático. La acción la ejecuta el docente; las notas de reflexión se visualizan en el prototipo, pero no se ha verificado su persistencia ni seguimiento. Si el docente no actúa, el sistema no ejecuta cambios automáticos.

### 6. Ética y privacidad

No se requieren nombres, correos ni matrículas de estudiantes.

Se propone:

- desidentificar los comentarios antes del análisis;
- limitar el acceso a los comentarios originales;
- mostrar al docente resultados agregados y ejemplos textuales protegidos;
- verificar autorización o consentimiento antes de utilizar datos reales.

**Riesgos:** sesgo de participación, ambigüedad del lenguaje y errores del PLN. Los resultados no deben utilizarse como evaluación sancionadora automática del docente.

### 7. Prueba de concepto

La prueba de concepto consiste en un notebook de Python con datos sintéticos reproducibles:

- **200 comentarios**;
- **301 menciones de prácticas**;
- **5 prácticas docentes**;
- **10 asignaturas**;
- **2 períodos académicos**.

Se calculan los indicadores **I01–I04** y se visualizan resultados mediante **Plotly**.

La PoC demuestra que los indicadores pueden calcularse y visualizarse, pero **no demuestra detección automática mediante un modelo PLN real ni utilidad pedagógica en campo**.

### 8. Validación

**Hipótesis propuesta:** el tablero facilita interpretar patrones y tomar decisiones docentes frente a una revisión sin tablero.

El plan contempla:

- **Validación pedagógica:** comparación con/sin tablero en tiempo y calidad de la decisión.
- **Validación técnica futura del PLN:** Macro-F1 y métricas por práctica.
- **Usabilidad:** SUS y entrevistas.

Los criterios cuantitativos de éxito todavía deben acordarse y la validación **no ha sido ejecutada**.

### 9. Preguntas abiertas para estadística

- ¿Qué tamaño de muestra necesitamos?
- ¿Cómo estimar la incertidumbre de los indicadores?
- ¿Cómo comparar asignaturas o períodos?
- ¿Cómo evaluar la mejora en la toma de decisiones docentes?
- ¿Cómo considerar los sesgos y errores del PLN?

---

## Prueba de concepto

El notebook implementa el recorrido mínimo de la Fase 4:

1. carga y descripción del dataset;
2. limpieza y validación de consistencia;
3. cálculo de los indicadores I01–I04;
4. visualización tipo tablero con Plotly;
5. sección **“Lo que este prototipo no puede decir todavía”**.

La herramienta propuesta es **descriptiva y diagnóstica**, no predictiva; por ello no se incorpora un modelo de regresión logística o árbol de decisión.

### Lo que este prototipo no puede decir todavía

La PoC no permite afirmar que:

- los resultados representen a estudiantes reales de la Universidad de Cuenca;
- el PLN identifique correctamente prácticas y valoraciones en datos reales;
- una frecuencia alta implique causalidad o una necesidad automática de intervención;
- el tablero mejore efectivamente las decisiones docentes;
- la interfaz sea suficientemente usable para docentes reales;
- el tratamiento institucional de los comentarios esté resuelto.

---

## Reproducibilidad

Para regenerar los datos sintéticos:

```bash
python generar_dataset_sintetico.py
```

Luego puede abrirse y ejecutarse:

```text
Fase_4_Prueba_de_Concepto_Teaching_Analytics.ipynb
```

El notebook utiliza rutas relativas cuando los CSV están en el mismo directorio, por lo que puede adaptarse a ejecución local o en Google Colab.

---

## Estructura del repositorio

```text
.
├── Fase_4_Prueba_de_Concepto_Teaching_Analytics.ipynb
├── comentarios_sinteticos.csv
├── menciones_practicas.csv
├── generar_dataset_sintetico.py
└── README.md
```

---

## Declaración de uso de IA generativa

| Herramienta | Uso realizado | Verificación de las salidas |
|---|---|---|
| **ChatGPT (OpenAI)** | Apoyo en la estructuración y revisión del trabajo; diseño del esquema del dataset sintético; generación y revisión del script de datos; desarrollo y revisión del notebook de prueba de concepto; apoyo en la documentación y preparación del pitch. | Las propuestas se contrastaron con el enunciado y con las decisiones tomadas en las fases anteriores. El script ejecuta validaciones automáticas de consistencia; el notebook fue ejecutado completamente para comprobar cálculos y visualizaciones; las fórmulas de los indicadores se revisaron respecto del diseño definido; y las asignaturas utilizadas como contexto fueron contrastadas con la malla de Computación proporcionada. |
| **Figma Make (IA integrada)** | Generación del prototipo interactivo de baja fidelidad **Teaching Analytics — Análisis de prácticas docentes** a partir de un prompt detallado con exactamente tres pantallas: panorama general, análisis de práctica y evidencia textual/reflexión docente. La IA se utilizó para proponer la interfaz, navegación, filtros simulados, visualizaciones y anotaciones académicas de los wireframes. | El prototipo se contrastó con el Canvas, el diccionario de datos y los indicadores I01–I04 definidos previamente. Se comprobó que utilizara exclusivamente las variables aprobadas, que los porcentajes y frecuencias ilustrativos fueran coherentes, que la navegación siguiera el flujo diseñado y que no incorporara predicciones, rankings docentes, datos personales ni recomendaciones automáticas. |

La IA se utilizó como herramienta de apoyo. Las decisiones sobre el problema, alcance, variables, indicadores, flujo de intervención, interpretación, limitaciones y criterios de validación fueron revisadas por el grupo antes de incorporarse al trabajo.

---

## Integrantes

- Diego Patiño
- María José Vire
