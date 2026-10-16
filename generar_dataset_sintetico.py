#!/usr/bin/env python3
"""
Generador reproducible de datos sintéticos para la prueba de concepto
de una herramienta de Teaching Analytics.

Contexto curricular:
- Las asignaturas se toman de la malla 2019 de Computación proporcionada
  para la actividad.
- Los comentarios, prácticas y valoraciones son completamente sintéticos.
- No se representan opiniones reales, estudiantes reales ni resultados
  institucionales de la Universidad de Cuenca.

Salida:
1) comentarios_sinteticos.csv
   id_comentario, comentario, asignatura, periodo_academico

2) menciones_practicas.csv
   id_comentario, practica_docente, valoracion

Semilla fija: 42
Número de comentarios: 200
Un comentario puede mencionar entre 1 y 3 prácticas.
"""

from pathlib import Path
import csv
import random
from collections import Counter

SEED = 42
N_COMENTARIOS = 200

BASE_DIR = Path(__file__).resolve().parent
COMENTARIOS_OUT = BASE_DIR / "comentarios_sinteticos.csv"
MENCIONES_OUT = BASE_DIR / "menciones_practicas.csv"

# Asignaturas reales de la malla 2019 de Computación.
# "nivel" se conserva como metadato interno para documentar el origen curricular,
# pero no se exporta porque no forma parte del diccionario de datos aprobado.
ASIGNATURAS = [
    {
        "nombre": "Programación I: Algoritmos, Datos y Estructuras",
        "nivel": 2,
        "temas": ["algoritmos", "estructuras básicas de datos", "ejercicios de programación"],
    },
    {
        "nombre": "Probabilidad y Estadística",
        "nivel": 3,
        "temas": ["distribuciones de probabilidad", "estadística descriptiva", "ejercicios de probabilidad"],
    },
    {
        "nombre": "Programación II: Estructura de Datos y Análisis de Algoritmos",
        "nivel": 3,
        "temas": ["estructuras de datos", "complejidad de algoritmos", "análisis de algoritmos"],
    },
    {
        "nombre": "Base de Datos I: Diseño y Principios",
        "nivel": 5,
        "temas": ["modelado de datos", "normalización", "consultas SQL"],
    },
    {
        "nombre": "Inteligencia Artificial",
        "nivel": 6,
        "temas": ["búsqueda en espacios de estados", "razonamiento", "técnicas de inteligencia artificial"],
    },
    {
        "nombre": "Aprendizaje de Máquina",
        "nivel": 6,
        "temas": ["entrenamiento de modelos", "métricas de evaluación", "clasificación"],
    },
    {
        "nombre": "Redes Neuronales",
        "nivel": 8,
        "temas": ["retropropagación", "arquitecturas de redes", "entrenamiento de redes"],
    },
    {
        "nombre": "Almacén y Minería de Datos",
        "nivel": 8,
        "temas": ["procesos ETL", "minería de datos", "almacenes de datos"],
    },
    {
        "nombre": "Ciencia de los Datos",
        "nivel": 9,
        "temas": ["limpieza de datos", "análisis exploratorio", "visualización de datos"],
    },
    {
        "nombre": "Gráficos por Computador",
        "nivel": 9,
        "temas": ["transformaciones geométricas", "rasterización", "representación gráfica"],
    },
]

PERIODOS = ["2025-2", "2026-1"]

PRACTICAS = [
    "Claridad explicativa",
    "Retroalimentación",
    "Organización de la clase",
    "Uso de ejemplos",
    "Instrucciones de evaluación",
]

PRACTICA_PESOS = [0.27, 0.20, 0.18, 0.19, 0.16]

VALORACIONES = ["efectiva", "malfuncional", "ambigua"]
VALORACION_PESOS = [0.53, 0.31, 0.16]

# Probabilidades para que un comentario mencione 1, 2 o 3 prácticas.
N_PRACTICAS = [1, 2, 3]
N_PRACTICAS_PESOS = [0.62, 0.32, 0.06]

PLANTILLAS = {
    "Claridad explicativa": {
        "efectiva": [
            "La explicación de {tema} fue clara y permitió seguir el contenido sin dificultad.",
            "El docente explicó {tema} de forma ordenada y comprensible.",
            "Los conceptos de {tema} quedaron claros durante la clase.",
            "La forma de explicar {tema} ayudó a comprender incluso las partes más complejas.",
            "Se entendió bien {tema} porque la explicación avanzó paso a paso.",
            "La explicación sobre {tema} fue precisa y fácil de relacionar con lo visto antes.",
        ],
        "malfuncional": [
            "La explicación de {tema} fue confusa y costó seguir el razonamiento.",
            "En {tema} se avanzó demasiado rápido y varios conceptos quedaron poco claros.",
            "La explicación sobre {tema} dejó dudas importantes que no se resolvieron en clase.",
            "Fue difícil comprender {tema} porque algunos pasos se dieron por conocidos.",
            "La presentación de {tema} resultó poco clara y mezcló varios conceptos a la vez.",
            "En {tema} faltó explicar con más detalle cómo se llega a los resultados.",
        ],
        "ambigua": [
            "La explicación de {tema} fue clara en algunas partes, pero otras quedaron poco desarrolladas.",
            "Se comprendió la idea general de {tema}, aunque algunos detalles todavía generan dudas.",
            "La explicación sobre {tema} fue útil, pero el ritmo no funcionó igual para todos los contenidos.",
            "En {tema} hubo partes bien explicadas y otras que necesitaron más ejemplos.",
            "La mayor parte de {tema} se entendió, aunque ciertos pasos podrían explicarse con más calma.",
            "La explicación de {tema} fue suficiente para empezar, pero algunos conceptos requieren revisión adicional.",
        ],
    },
    "Retroalimentación": {
        "efectiva": [
            "La retroalimentación sobre las actividades de {tema} permitió identificar los errores y corregirlos.",
            "Los comentarios del docente después de trabajar {tema} fueron específicos y útiles.",
            "La revisión de los ejercicios de {tema} ayudó a entender qué debía mejorarse.",
            "La retroalimentación recibida en {tema} explicó claramente los aciertos y los errores.",
            "Después de las actividades de {tema}, las observaciones del docente ayudaron a mejorar el trabajo.",
            "Las correcciones relacionadas con {tema} llegaron a tiempo y fueron fáciles de aplicar.",
        ],
        "malfuncional": [
            "En las actividades de {tema}, la retroalimentación llegó tarde y ya no fue útil para corregir el siguiente trabajo.",
            "Las observaciones sobre {tema} fueron muy generales y no dejaron claro qué debía mejorarse.",
            "Faltó retroalimentación después de los ejercicios de {tema}.",
            "Las correcciones de {tema} señalaron errores, pero casi no explicaron cómo solucionarlos.",
            "En {tema} se recibieron calificaciones, pero poca explicación sobre los errores cometidos.",
            "La retroalimentación de las actividades de {tema} fue insuficiente para entender los criterios usados.",
        ],
        "ambigua": [
            "La retroalimentación sobre {tema} fue útil, aunque no llegó con el mismo nivel de detalle en todas las actividades.",
            "En {tema} hubo buenos comentarios de mejora, pero algunas tareas recibieron observaciones muy breves.",
            "Las correcciones de {tema} ayudaron en ciertos ejercicios, aunque en otros quedaron dudas.",
            "La retroalimentación de {tema} fue clara cuando se recibió, pero no siempre estuvo disponible a tiempo.",
            "Algunas observaciones sobre {tema} fueron específicas y otras demasiado generales.",
            "La revisión de {tema} permitió corregir varios errores, aunque ciertos criterios todavía no quedaron claros.",
        ],
    },
    "Organización de la clase": {
        "efectiva": [
            "La clase sobre {tema} siguió una secuencia lógica entre explicación, práctica y cierre.",
            "El tiempo dedicado a {tema} estuvo bien organizado y permitió completar las actividades.",
            "Los contenidos de {tema} se presentaron en un orden que facilitó relacionar los conceptos.",
            "La sesión de {tema} estuvo bien estructurada y fue fácil identificar cada etapa de trabajo.",
            "La organización de la clase permitió pasar de la teoría de {tema} a la práctica de manera natural.",
            "El desarrollo de {tema} mantuvo un ritmo adecuado y una secuencia clara.",
        ],
        "malfuncional": [
            "La clase de {tema} cambió varias veces de actividad y fue difícil seguir una secuencia.",
            "En {tema} faltó tiempo para terminar la parte práctica porque la sesión no estuvo bien distribuida.",
            "Los contenidos de {tema} se presentaron en un orden que generó confusión.",
            "La sesión de {tema} se sintió desorganizada y varias actividades quedaron inconclusas.",
            "En {tema} se dedicó demasiado tiempo a unas partes y muy poco a otras.",
            "La organización de la clase de {tema} dificultó conectar la explicación con la práctica.",
        ],
        "ambigua": [
            "La clase de {tema} tuvo una estructura clara al inicio, aunque el cierre fue apresurado.",
            "La organización de {tema} funcionó bien en la parte teórica, pero la práctica quedó corta de tiempo.",
            "La secuencia de {tema} fue comprensible, aunque algunas transiciones entre actividades fueron bruscas.",
            "La sesión de {tema} estuvo ordenada en general, pero ciertas actividades necesitaron más tiempo.",
            "El desarrollo de {tema} siguió una estructura útil, aunque el ritmo cambió bastante durante la clase.",
            "La organización de {tema} fue adecuada, pero algunas partes podrían distribuirse mejor.",
        ],
    },
    "Uso de ejemplos": {
        "efectiva": [
            "Los ejemplos utilizados para {tema} facilitaron la comprensión de los conceptos.",
            "Los casos prácticos de {tema} ayudaron a relacionar la teoría con situaciones concretas.",
            "Los ejemplos de {tema} mostraron claramente cómo aplicar lo explicado.",
            "Trabajar ejemplos paso a paso permitió entender mejor {tema}.",
            "Los ejemplos elegidos para {tema} fueron pertinentes y aclararon las dudas principales.",
            "Las demostraciones prácticas de {tema} ayudaron a comprender cuándo usar cada concepto.",
        ],
        "malfuncional": [
            "En {tema} faltaron ejemplos prácticos para entender cómo aplicar los conceptos.",
            "Los pocos ejemplos de {tema} fueron demasiado simples frente a los ejercicios posteriores.",
            "Los ejemplos utilizados en {tema} no ayudaron a aclarar las partes más difíciles.",
            "En {tema} se explicó bastante teoría, pero casi no se mostraron casos de aplicación.",
            "Los ejemplos de {tema} fueron muy distintos de las actividades que luego se solicitaron.",
            "Hicieron falta ejemplos paso a paso para comprender mejor {tema}.",
        ],
        "ambigua": [
            "Los ejemplos de {tema} ayudaron con la idea general, aunque faltaron casos más complejos.",
            "En {tema} hubo ejemplos útiles, pero no cubrieron todas las situaciones trabajadas después.",
            "Los ejemplos de {tema} fueron claros, aunque algunos ejercicios requirieron enfoques diferentes.",
            "Se mostraron buenos ejemplos de {tema}, pero habría sido útil incluir más variedad.",
            "Los casos prácticos de {tema} ayudaron al inicio, aunque no resolvieron todas las dudas.",
            "Los ejemplos usados para {tema} fueron adecuados, pero algunos conceptos necesitaron demostraciones adicionales.",
        ],
    },
    "Instrucciones de evaluación": {
        "efectiva": [
            "Las instrucciones de la actividad sobre {tema} indicaron claramente qué debía entregarse y cómo sería evaluado.",
            "Los criterios de evaluación para {tema} estuvieron definidos desde el inicio.",
            "La consigna de la tarea de {tema} fue precisa y permitió organizar bien el trabajo.",
            "En la evaluación de {tema} se explicaron con claridad los requisitos y los criterios.",
            "Las instrucciones del proyecto relacionado con {tema} fueron completas y fáciles de seguir.",
            "Antes de evaluar {tema}, se aclararon los entregables y la forma en que serían valorados.",
        ],
        "malfuncional": [
            "Las instrucciones de la actividad sobre {tema} fueron poco claras y generaron dudas sobre qué entregar.",
            "En la evaluación de {tema} algunos criterios se conocieron después de iniciar el trabajo.",
            "La consigna relacionada con {tema} dejó ambiguos varios requisitos importantes.",
            "Para la actividad de {tema} no quedó claro cómo se distribuiría la calificación.",
            "Las instrucciones del proyecto de {tema} cambiaron durante el desarrollo y eso generó confusión.",
            "En la evaluación de {tema} faltó especificar con precisión qué se esperaba en el entregable.",
        ],
        "ambigua": [
            "Las instrucciones de la actividad sobre {tema} fueron claras en general, aunque algunos requisitos necesitaron aclaraciones posteriores.",
            "Los criterios de evaluación de {tema} estaban definidos, pero ciertos detalles se interpretaron de distintas maneras.",
            "La consigna de {tema} permitió empezar el trabajo, aunque hubo preguntas sobre algunos entregables.",
            "En la evaluación de {tema} la mayoría de criterios fue clara, pero faltó precisar un par de aspectos.",
            "Las instrucciones del proyecto de {tema} fueron suficientes al inicio, aunque luego se añadieron algunas aclaraciones.",
            "Los requisitos de la actividad de {tema} se entendieron, pero algunos criterios podrían formularse con mayor precisión.",
        ],
    },
}

CIERRES = [
    "",
    "",
    "",
    " En general, esto influyó en cómo se desarrolló el aprendizaje durante la asignatura.",
    " Este aspecto fue especialmente visible durante las actividades prácticas.",
    " Fue uno de los aspectos que más llamó la atención durante el curso.",
]


def weighted_sample_without_replacement(rng, items, weights, k):
    """Selecciona k elementos sin reemplazo conservando pesos relativos."""
    pool_items = list(items)
    pool_weights = list(weights)
    selected = []
    for _ in range(k):
        choice = rng.choices(pool_items, weights=pool_weights, k=1)[0]
        idx = pool_items.index(choice)
        selected.append(choice)
        pool_items.pop(idx)
        pool_weights.pop(idx)
    return selected


def generar_dataset(seed=SEED, n_comentarios=N_COMENTARIOS):
    rng = random.Random(seed)

    comentarios = []
    menciones = []

    # Distribución levemente desigual para que los filtros muestren diferencias.
    asignatura_pesos = [0.09, 0.08, 0.11, 0.10, 0.10, 0.11, 0.09, 0.09, 0.13, 0.10]
    periodo_pesos = [0.46, 0.54]

    for i in range(1, n_comentarios + 1):
        id_comentario = f"C{i:03d}"

        asignatura = rng.choices(ASIGNATURAS, weights=asignatura_pesos, k=1)[0]
        periodo = rng.choices(PERIODOS, weights=periodo_pesos, k=1)[0]
        tema = rng.choice(asignatura["temas"])

        cantidad_practicas = rng.choices(
            N_PRACTICAS, weights=N_PRACTICAS_PESOS, k=1
        )[0]

        practicas = weighted_sample_without_replacement(
            rng, PRACTICAS, PRACTICA_PESOS, cantidad_practicas
        )

        frases = []
        for practica in practicas:
            valoracion = rng.choices(
                VALORACIONES, weights=VALORACION_PESOS, k=1
            )[0]
            plantilla = rng.choice(PLANTILLAS[practica][valoracion])
            frases.append(plantilla.format(tema=tema))

            menciones.append(
                {
                    "id_comentario": id_comentario,
                    "practica_docente": practica,
                    "valoracion": valoracion,
                }
            )

        # Para comentarios con varias prácticas, se mantienen frases completas
        # para que el texto sea legible y cada mención sea trazable.
        comentario = " ".join(frases) + rng.choice(CIERRES)

        comentarios.append(
            {
                "id_comentario": id_comentario,
                "comentario": comentario.strip(),
                "asignatura": asignatura["nombre"],
                "periodo_academico": periodo,
            }
        )

    return comentarios, menciones


def validar_dataset(comentarios, menciones):
    ids = [r["id_comentario"] for r in comentarios]
    ids_set = set(ids)

    assert len(comentarios) == N_COMENTARIOS, "Número inesperado de comentarios."
    assert len(ids) == len(ids_set), "Hay IDs repetidos en comentarios."
    assert all(r["comentario"].strip() for r in comentarios), "Hay comentarios vacíos."
    assert all(r["asignatura"] in {a["nombre"] for a in ASIGNATURAS} for r in comentarios)
    assert all(r["periodo_academico"] in PERIODOS for r in comentarios)

    assert all(r["id_comentario"] in ids_set for r in menciones), (
        "Hay menciones cuyo comentario no existe."
    )
    assert all(r["practica_docente"] in PRACTICAS for r in menciones)
    assert all(r["valoracion"] in VALORACIONES for r in menciones)

    pares = [(r["id_comentario"], r["practica_docente"]) for r in menciones]
    assert len(pares) == len(set(pares)), (
        "Una misma práctica está repetida dentro de un comentario."
    )

    conteo_por_id = Counter(r["id_comentario"] for r in menciones)
    assert all(1 <= n <= 3 for n in conteo_por_id.values())
    assert any(n > 1 for n in conteo_por_id.values()), (
        "El dataset debe contener comentarios con múltiples prácticas."
    )

    # Asegurar cobertura útil para filtros de la PoC.
    assert len({r["asignatura"] for r in comentarios}) == len(ASIGNATURAS)
    assert set(r["periodo_academico"] for r in comentarios) == set(PERIODOS)
    assert set(r["practica_docente"] for r in menciones) == set(PRACTICAS)
    assert set(r["valoracion"] for r in menciones) == set(VALORACIONES)


def guardar_csv(comentarios, menciones):
    with COMENTARIOS_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id_comentario",
                "comentario",
                "asignatura",
                "periodo_academico",
            ],
        )
        writer.writeheader()
        writer.writerows(comentarios)

    with MENCIONES_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id_comentario",
                "practica_docente",
                "valoracion",
            ],
        )
        writer.writeheader()
        writer.writerows(menciones)


def resumen(comentarios, menciones):
    conteo_menciones = Counter(r["id_comentario"] for r in menciones)
    por_practica = Counter(r["practica_docente"] for r in menciones)
    por_valoracion = Counter(r["valoracion"] for r in menciones)

    return {
        "comentarios": len(comentarios),
        "menciones": len(menciones),
        "comentarios_multietiqueta": sum(1 for n in conteo_menciones.values() if n > 1),
        "promedio_practicas_por_comentario": round(len(menciones) / len(comentarios), 3),
        "asignaturas": len({r["asignatura"] for r in comentarios}),
        "periodos": sorted({r["periodo_academico"] for r in comentarios}),
        "practicas": dict(por_practica),
        "valoraciones": dict(por_valoracion),
    }


if __name__ == "__main__":
    comentarios, menciones = generar_dataset()
    validar_dataset(comentarios, menciones)
    guardar_csv(comentarios, menciones)

    info = resumen(comentarios, menciones)
    print("Dataset sintético generado y validado.")
    for clave, valor in info.items():
        print(f"- {clave}: {valor}")
    print(f"- archivo comentarios: {COMENTARIOS_OUT}")
    print(f"- archivo menciones: {MENCIONES_OUT}")
