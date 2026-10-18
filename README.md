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

**Decisión apoyada:** identificar qué prácticas docentes mantener, revisar o mejorar a partir de la retroalimentación estudiantil.

Actualmente, los comentarios abiertos requieren revisión manual y dificultan reconocer patrones recurrentes de manera sistemática. La herramienta propone organizar esa evidencia para que el docente pueda interpretarla antes de decidir una posible acción pedagógica.

### 2. Problema educativo

Los comentarios abiertos pueden contener información útil sobre la experiencia de enseñanza, pero su naturaleza textual hace difícil resumirlos y detectar patrones cuando aumenta el número de respuestas.

El problema abordado no es “mejorar la docencia” de forma abstracta, sino **reducir la dificultad de convertir comentarios no estructurados en evidencia pedagógica interpretable**.

La magnitud institucional exacta del problema todavía debe verificarse con datos reales autorizados de la Universidad de Cuenca.

### 3. Pregunta analítica

> **¿Qué prácticas docentes efectivas, malfuncionales o ambiguas aparecen de forma recurrente en los comentarios de los estudiantes?**

- **Nivel de analítica:** descriptivo y diagnóstico.
- **Tipo:** Teaching Analytics / analítica de enseñanza.

La herramienta describe qué prácticas aparecen y con qué frecuencia, y permite examinar patrones recurrentes mediante sus valoraciones y evidencia textual asociada.

### 4. Datos e indicadores

Datos principales:

- comentario estudiantil;
- práctica docente identificada;
- valoración de la práctica: efectiva, malfuncional o ambigua;
- asignatura, si está disponible;
- período académico, si está disponible.

Indicadores definidos:

- **I01:** número de comentarios únicos analizados;
- **I02:** número de comentarios únicos que mencionan cada práctica;
- **I03:** porcentaje de comentarios que menciona cada práctica;
- **I04:** distribución de valoraciones dentro de cada práctica.

Indicador central:

[
P_j = \frac{N_j}{N} \times 100
]

donde (N) es el total de comentarios únicos y (N_j) el número de comentarios únicos que mencionan la práctica (j).

Un comentario puede mencionar varias prácticas, por lo que los porcentajes entre prácticas no tienen que sumar 100 %.

### 5. Intervención

El flujo propuesto es:

**Panorama general → análisis de una práctica → evidencia textual → interpretación docente → posible acción pedagógica**

El docente puede:

- mantener o fortalecer una práctica cuando existe evidencia favorable;
- revisar una práctica cuando aparecen menciones malfuncionales recurrentes;
- solicitar más información o no intervenir cuando la evidencia es ambigua o insuficiente.

La herramienta no aplica umbrales automáticos ni ejecuta acciones sin intervención humana.

### 6. Ética y privacidad

La herramienta no requiere nombre, cédula, correo ni matrícula del estudiante.

Medidas propuestas:

- desidentificar los comentarios antes del análisis;
- eliminar identificadores directos o referencias que puedan revelar identidades;
- utilizar identificadores técnicos para trazabilidad;
- restringir el acceso a comentarios originales;
- mostrar al docente principalmente resultados agregados y evidencia textual desidentificada;
- verificar la autorización institucional o consentimiento correspondiente antes de utilizar datos reales.

Los indicadores pueden verse afectados por participación desigual, opiniones extremas, lenguaje ambiguo, tamaños de muestra pequeños y errores del PLN. Por ello, deben interpretarse como **evidencia para reflexión**, no como una evaluación sancionadora automática.

### 7. Prueba de concepto

La PoC utiliza datos sintéticos generados mediante un script reproducible con semilla fija.

Estructura:

- **200 comentarios sintéticos**;
- **10 asignaturas** tomadas como contexto de la malla de Computación;
- **2 períodos académicos**;
- **5 prácticas docentes**;
- valoraciones: efectiva, malfuncional y ambigua;
- un comentario puede contener entre una y varias prácticas.

Archivos principales:

- `generar_dataset_sintetico.py`
- `comentarios_sinteticos.csv`
- `menciones_practicas.csv`
- `Fase_4_Prueba_de_Concepto_Teaching_Analytics.ipynb`

La PoC demuestra que los indicadores I01–I04 son calculables y que pueden representarse mediante visualizaciones tipo tablero con Plotly.

### 8. Validación

Se propone una validación en tres niveles:

**Técnica**
- Macro-F1 y métricas por categoría para evaluar el futuro modelo de PLN con datos reales anotados.
- Revisión de falsos positivos y falsos negativos.

**Pedagógica**
- Comparar el tiempo y la calidad de la decisión docente con y sin tablero.
- Analizar si la herramienta permite identificar patrones que no se detectan fácilmente mediante revisión manual.

**Usabilidad**
- Aplicar SUS (System Usability Scale).
- Complementar con entrevistas o preguntas abiertas a docentes.

**Criterio de éxito:** que la herramienta produzca información técnicamente confiable, interpretable y útil para apoyar una decisión docente sin sustituir el criterio humano.

### 9. Preguntas abiertas para estadística

Quedan abiertas preguntas que requieren métodos estadísticos para responderse, entre ellas:

- ¿Cuántos comentarios son necesarios para que los porcentajes por práctica sean suficientemente estables?
- ¿Qué incertidumbre acompaña a cada porcentaje observado?
- ¿Existen diferencias significativas entre asignaturas o períodos?
- ¿El uso del tablero reduce significativamente el tiempo necesario para analizar comentarios?
- ¿Mejora la calidad o consistencia de las decisiones docentes?
- ¿Qué nivel de acuerdo existe entre anotadores humanos al clasificar prácticas y valoraciones?

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
