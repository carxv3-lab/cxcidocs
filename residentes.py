"""
Listado de residentes, grados académicos y periodos vacacionales
Cirugía General UAS - Ciclo 2026-2027
"""

from datetime import date

RESIDENTES = [
    # R4
    {
        "nombre": "Beltrán Delgado Jorge Omar",
        "grado": "R4",
        "guardia": "D",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 10, 5),  "fin": date(2026, 10, 16)},
            {"periodo": 2, "inicio": date(2027, 1, 18),  "fin": date(2027, 1, 29)},
        ],
    },
    {
        "nombre": "Soto Valle José Emaús",
        "grado": "R4",
        "guardia": "B",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 5, 4),   "fin": date(2026, 5, 15)},
            {"periodo": 2, "inicio": date(2026, 11, 30), "fin": date(2026, 12, 11)},
        ],
    },
    {
        "nombre": "Villegas Rodríguez José",
        "grado": "R4",
        "guardia": "C",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 4, 6),   "fin": date(2026, 4, 17)},
            {"periodo": 2, "inicio": date(2026, 8, 31),  "fin": date(2026, 9, 11)},
        ],
    },
    # R3
    {
        "nombre": "Almanza Orduño Athmir Antonio",
        "grado": "R3",
        "guardia": "A",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2027, 4, 20),  "fin": date(2027, 5, 1)},
            {"periodo": 2, "inicio": date(2026, 11, 16), "fin": date(2026, 11, 27)},
        ],
    },
    {
        "nombre": "Bueno López Daniela Alejandra",
        "grado": "R3",
        "guardia": "D",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 6, 15),  "fin": date(2026, 6, 26)},
            {"periodo": 2, "inicio": date(2027, 1, 18),  "fin": date(2027, 1, 29)},
        ],
    },
    {
        "nombre": "Cordero Medina Marielos",
        "grado": "R3",
        "guardia": "B",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 6, 1),   "fin": date(2026, 6, 12)},
            {"periodo": 2, "inicio": date(2027, 2, 15),  "fin": date(2027, 2, 26)},
        ],
    },
    {
        "nombre": "Ojeda Valenzuela José Antonio",
        "grado": "R3",
        "guardia": "—",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 4, 20),  "fin": date(2026, 5, 1)},
            {"periodo": 2, "inicio": date(2026, 11, 2),  "fin": date(2026, 11, 13)},
        ],
    },
    # R2
    {
        "nombre": "Angulo Sánchez Rolando",
        "grado": "R2",
        "guardia": "A",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 3, 2),   "fin": date(2026, 3, 13)},
            {"periodo": 2, "inicio": date(2026, 11, 30), "fin": date(2026, 12, 11)},
        ],
    },
    {
        "nombre": "Luna Borboa Jorge Luis",
        "grado": "R2",
        "guardia": "C",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 7, 6),   "fin": date(2026, 7, 17)},
            {"periodo": 2, "inicio": date(2027, 1, 4),   "fin": date(2027, 1, 15)},
        ],
    },
    {
        "nombre": "Maldonado Guardado Diana Guadalupe",
        "grado": "R2",
        "guardia": "D",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 6, 1),   "fin": date(2026, 6, 12)},
            {"periodo": 2, "inicio": date(2026, 11, 30), "fin": date(2026, 12, 11)},
        ],
    },
    {
        "nombre": "Valenzuela Pardo Mariana",
        "grado": "R2",
        "guardia": "C",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 3, 16),  "fin": date(2026, 3, 27)},
            {"periodo": 2, "inicio": date(2026, 11, 2),  "fin": date(2026, 11, 13)},
        ],
    },
    # R1
    {
        "nombre": "López Félix Jesús Arturo",
        "grado": "R1",
        "guardia": "A",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 5, 18),  "fin": date(2026, 5, 29)},
            {"periodo": 2, "inicio": date(2026, 11, 16), "fin": date(2026, 11, 27)},
        ],
    },
    {
        "nombre": "Portugal Beltrán Emma",
        "grado": "R1",
        "guardia": "B",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2027, 4, 20),  "fin": date(2027, 5, 1)},
            {"periodo": 2, "inicio": date(2026, 10, 5),  "fin": date(2026, 10, 16)},
        ],
    },
    {
        "nombre": "Rendón Sánchez Manuel",
        "grado": "R1",
        "guardia": "C",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 6, 15),  "fin": date(2026, 6, 26)},
            {"periodo": 2, "inicio": date(2027, 1, 18),  "fin": date(2027, 1, 29)},
        ],
    },
    {
        "nombre": "Romero Molina Geovana Clarisa",
        "grado": "R1",
        "guardia": "D",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 6, 1),   "fin": date(2026, 6, 12)},
            {"periodo": 2, "inicio": date(2026, 11, 30), "fin": date(2026, 12, 11)},
        ],
    },
    {
        "nombre": "Valdez Valdez Ricardo Antonio",
        "grado": "R1",
        "guardia": "A",
        "vacaciones": [
            {"periodo": 1, "inicio": date(2026, 7, 6),   "fin": date(2026, 7, 17)},
            {"periodo": 2, "inicio": date(2027, 2, 1),   "fin": date(2027, 2, 12)},
        ],
    },
]

PERIODO_VACACIONAL_SS = {
    "inicio": date(2026, 3, 30),
    "fin": date(2026, 4, 10),
    "descripcion": "Periodo vacacional Semana Santa",
}


def get_residente_por_nombre(nombre):
    for r in RESIDENTES:
        if r["nombre"] == nombre:
            return r
    return None


def get_residentes_por_grado(grado):
    return [r for r in RESIDENTES if r["grado"] == grado]


def esta_de_vacaciones(residente, fecha):
    for vac in residente["vacaciones"]:
        if vac["inicio"] <= fecha <= vac["fin"]:
            return True, vac
    return False, None
