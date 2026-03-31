"""
Rotaciones mensuales y externas - Cirugía General UAS 2026-2027
Ciclo: Marzo 2026 - Febrero 2027
"""

# Rotaciones mensuales por residente (Mar 2026 - Feb 2027)
# Claves: nombre_corto -> lista de 12 meses (Mar a Feb)
MESES = [
    "Marzo", "Abril", "Mayo", "Junio", "Julio",
    "Agosto", "Sep", "Oct", "Nov", "Dic", "Enero", "Feb"
]

ROTACIONES_MENSUALES = {
    # R4
    "Beltrán Delgado Jorge Omar": [
        "Rot. campo", "Rot. campo", "Rot. campo", "Rot. campo",
        "Hosp. Pediátrico", "Hosp. Pediátrico", "VAC 1", "", "", "", "VAC 2", ""
    ],
    "Soto Valle José Emaús": [
        "", "VAC 1", "", "Rot. campo", "Rot. campo", "Rot. campo",
        "Rot. campo", "", "VAC 2", "", "Hosp. Pediátrico", "Hosp. Pediátrico"
    ],
    "Villegas Rodríguez José": [
        "", "VAC 1", "Hosp. Pediátrico", "Hosp. Pediátrico", "", "VAC 2",
        "", "Rot. campo", "Rot. campo", "Rot. campo", "Rot. campo", ""
    ],
    # R3
    "Almanza Orduño Athmir Antonio": [
        "", "VAC 1", "", "Cx Tórax", "Cx Vascular", "",
        "Oncocirugía", "", "VAC 2", "", "", ""
    ],
    "Bueno López Daniela Alejandra": [
        "Cx Tórax", "Cx Vascular", "", "VAC 1", "", "", "",
        "Oncocirugía", "", "VAC 2", "", ""
    ],
    "Cordero Medina Marielos": [
        "Proctología HCG", "", "VAC 1", "", "Oncocirugía", "",
        "Cx Tórax", "Cx Vascular", "", "", "VAC 2", ""
    ],
    "Ojeda Valenzuela José Antonio": [
        "Oncocirugía", "", "VAC 1", "", "", "Cx Tórax",
        "Cx Vascular", "", "VAC 2", "", "", ""
    ],
    # R2
    "Angulo Sánchez Rolando": [
        "VAC 1", "", "Proctología HCC", "", "UCI HCC", "",
        "", "Urología HCC", "VAC 2", "", "", ""
    ],
    "Luna Borboa Jorge Luis": [
        "Urología HCC", "", "Proctología HCC", "", "VAC 1", "",
        "Endoscopia HCC", "UCI HCC", "", "VAC 2", "", ""
    ],
    "Maldonado Guardado Diana Guadalupe": [
        "", "Endoscopia HCC", "", "VAC 1", "Urología HCC", "",
        "", "Proctología HCC", "VAC 2", "", "UCI HCC", ""
    ],
    "Valenzuela Pardo Mariana": [
        "VAC 1", "", "Endoscopia HCC", "", "Proctología HCC", "",
        "Urología HCC", "VAC 2", "", "", "UCI HCC", ""
    ],
    # R1
    "López Félix Jesús Arturo": [
        "", "", "", "VAC 1", "Neurocx HCC", "Neurocx HCC",
        "", "", "VAC 2", "", "Endoscopia HCC", ""
    ],
    "Portugal Beltrán Emma": [
        "", "VAC 1", "", "Endoscopia HCC", "", "Neurocx HCC",
        "Neurocx HCC", "VAC 2", "", "", "", ""
    ],
    "Rendón Sánchez Manuel": [
        "", "", "", "VAC 1", "Endoscopia HCC", "",
        "Neurocx HCC", "Neurocx HCC", "", "VAC 2", "", ""
    ],
    "Romero Molina Geovana Clarisa": [
        "", "", "", "VAC 1", "", "", "",
        "Endoscopia HCC", "VAC 2", "", "Neurocx HCC", "Neurocx HCC"
    ],
    "Valdez Valdez Ricardo Antonio": [
        "Neurocx HCC", "Neurocx HCC", "", "VAC 1", "",
        "Endoscopia HCC", "", "", "", "VAC 2", "", ""
    ],
}

# Rotaciones externas (otros hospitales)
ROTACIONES_EXTERNAS = [
    # R4
    {"residente": "Beltrán Delgado Jorge Omar", "grado": "R4",
     "hospital": "Hospital Pediátrico de Sinaloa", "servicio": "Cirugía Pediátrica",
     "inicio": "3 ago 2026", "fin": "30 sep 2026"},
    {"residente": "Soto Valle José Emaús", "grado": "R4",
     "hospital": "Hospital Pediátrico de Sinaloa", "servicio": "Cirugía Pediátrica",
     "inicio": "1 ene 2026", "fin": "28 feb 2026"},
    {"residente": "Soto Valle José Emaús", "grado": "R4",
     "hospital": "Hospital Civil de Guadalajara", "servicio": "Coloproctología",
     "inicio": "1 may 2025", "fin": "30 may 2025"},
    {"residente": "Villegas Rodríguez José", "grado": "R4",
     "hospital": "Hospital Pediátrico de Sinaloa", "servicio": "Cirugía Pediátrica",
     "inicio": "4 ene 2027", "fin": "26 feb 2027"},
    # R3
    {"residente": "Almanza Orduño Athmir Antonio", "grado": "R3",
     "hospital": "CMN 20 de Noviembre ISSSTE", "servicio": "Oncocirugía",
     "inicio": "1 sep 2026", "fin": "30 sep 2026"},
    {"residente": "Almanza Orduño Athmir Antonio", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (viejo)", "servicio": "Cirugía de Tórax",
     "inicio": "1 jun 2026", "fin": "30 jun 2026"},
    {"residente": "Almanza Orduño Athmir Antonio", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (nuevo)", "servicio": "Cirugía Vascular",
     "inicio": "1 jul 2026", "fin": "31 jul 2026"},
    {"residente": "Bueno López Daniela Alejandra", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (viejo)", "servicio": "Cirugía de Tórax",
     "inicio": "2 mar 2026", "fin": "31 mar 2026"},
    {"residente": "Bueno López Daniela Alejandra", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (nuevo)", "servicio": "Cirugía Vascular",
     "inicio": "1 abr 2026", "fin": "30 abr 2026"},
    {"residente": "Bueno López Daniela Alejandra", "grado": "R3",
     "hospital": "CMN 20 de Noviembre ISSSTE", "servicio": "Oncocirugía",
     "inicio": "2 nov 2026", "fin": "30 nov 2026"},
    {"residente": "Cordero Medina Marielos", "grado": "R3",
     "hospital": "Hospital General de México", "servicio": "Coloproctología",
     "inicio": "2 mar 2026", "fin": "31 mar 2026"},
    {"residente": "Cordero Medina Marielos", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (viejo)", "servicio": "Cirugía de Tórax",
     "inicio": "1 oct 2026", "fin": "30 oct 2026"},
    {"residente": "Cordero Medina Marielos", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (nuevo)", "servicio": "Cirugía Vascular",
     "inicio": "2 nov 2026", "fin": "30 nov 2026"},
    {"residente": "Cordero Medina Marielos", "grado": "R3",
     "hospital": "CMN 20 de Noviembre ISSSTE", "servicio": "Oncocirugía",
     "inicio": "3 ago 2026", "fin": "31 ago 2026"},
    {"residente": "Ojeda Valenzuela José Antonio", "grado": "R3",
     "hospital": "CMN 20 de Noviembre ISSSTE", "servicio": "Cirugía Oncológica",
     "inicio": "2 mar 2026", "fin": "31 mar 2026"},
    {"residente": "Ojeda Valenzuela José Antonio", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (viejo)", "servicio": "Cirugía de Tórax",
     "inicio": "3 ago 2026", "fin": "31 ago 2026"},
    {"residente": "Ojeda Valenzuela José Antonio", "grado": "R3",
     "hospital": "Hospital Civil de Guadalajara (nuevo)", "servicio": "Cirugía Vascular",
     "inicio": "1 sep 2026", "fin": "30 sep 2026"},
    # R2
    {"residente": "Angulo Sánchez Rolando", "grado": "R2",
     "hospital": "Hospital General Regional No. 1 ISSSTE Culiacán", "servicio": "Coloproctología",
     "inicio": "1 abr 2026", "fin": "30 abr 2026"},
    {"residente": "Luna Borboa Jorge Luis", "grado": "R2",
     "hospital": "Hospital General Regional No. 1 ISSSTE Culiacán", "servicio": "Coloproctología",
     "inicio": "1 may 2026", "fin": "29 may 2026"},
    {"residente": "Maldonado Guardado Diana Guadalupe", "grado": "R2",
     "hospital": "Hospital General Regional No. 1 ISSSTE Culiacán", "servicio": "Coloproctología",
     "inicio": "2 nov 2026", "fin": "30 nov 2026"},
    {"residente": "Valenzuela Pardo Mariana", "grado": "R2",
     "hospital": "Hospital General Regional No. 1 ISSSTE Culiacán", "servicio": "Coloproctología",
     "inicio": "3 ago 2026", "fin": "31 ago 2026"},
]

ABREV_ROTACION = {
    "Rot. campo": "Rotación campo (Hospitales Integrales SSA, Sinaloa)",
    "Hosp. Pediátrico": "Hospital Pediátrico de Sinaloa - Cirugía Pediátrica",
    "Cx Tórax": "Cirugía de Tórax (Hospital Civil Guadalajara)",
    "Cx Vascular": "Cirugía Vascular (Hospital Civil Guadalajara)",
    "Oncocirugía": "Oncocirugía (CMN 20 de Noviembre ISSSTE)",
    "Proctología HCG": "Coloproctología (Hospital General de México)",
    "Proctología HCC": "Coloproctología (ISSSTE Culiacán)",
    "UCI HCC": "Unidad de Cuidados Intensivos (Hospital Civil Culiacán)",
    "Urología HCC": "Urología (Hospital Civil Culiacán)",
    "Endoscopia HCC": "Endoscopia (Hospital Civil Culiacán)",
    "Neurocx HCC": "Neurocirugía (Hospital Civil Culiacán)",
    "VAC 1": "Periodo vacacional 1",
    "VAC 2": "Periodo vacacional 2",
    "": "Cirugía General (Hospital Civil Culiacán)",
}
