"""
Bibliografía quirúrgica sugerida con mapeo temático
Cirugía General UAS - Programa Operativo 2026-2027
"""

# Libros de bibliografía básica sugerida
LIBROS = [
    {"titulo": "Principles of Surgery", "autor": "Schwartz", "editorial": "McGraw Hill", "tipo": "Libro"},
    {"titulo": "Técnicas Quirúrgicas", "autor": "Kirk", "editorial": "—", "tipo": "Libro"},
    {"titulo": "Fisiopatología Quirúrgica del Aparato Digestivo", "autor": "Gutiérrez Samperio", "editorial": "El Manual Moderno", "tipo": "Libro"},
    {"titulo": "Atlas de Anatomía", "autor": "Netter", "editorial": "Elsevier", "tipo": "Libro"},
    {"titulo": "Hernia. Anatomía y Técnicas Quirúrgicas", "autor": "Skandalakis", "editorial": "Marbán", "tipo": "Libro"},
    {"titulo": "Operaciones Abdominales (Maingot)", "autor": "Maingot / Zinner", "editorial": "Panamericana", "tipo": "Libro"},
    {"titulo": "Clínicas Quirúrgicas de Norteamérica", "autor": "Varios", "editorial": "Interamericana McGraw Hill", "tipo": "Libro"},
    {"titulo": "Cirugía del Aparato Digestivo", "autor": "Shackelford-Zuidema", "editorial": "Panamericana", "tipo": "Libro"},
    {"titulo": "Esófago", "autor": "Castell", "editorial": "—", "tipo": "Libro"},
    {"titulo": "El Dominio de la Cirugía", "autor": "Baker y Fischer", "editorial": "Panamericana", "tipo": "Libro"},
    {"titulo": "Trauma", "autor": "Mattox", "editorial": "McGraw Hill", "tipo": "Libro"},
    {"titulo": "Tratado de Cirugía General", "autor": "Consejo Mexicano de Cirugía General (AMCG)", "editorial": "Manual Moderno", "tipo": "Libro"},
    {"titulo": "Cirugía Basada en Evidencias", "autor": "Varios", "editorial": "—", "tipo": "Libro"},
    {"titulo": "Bioestadística Médica", "autor": "Dawson y Trapo", "editorial": "—", "tipo": "Libro"},
    {"titulo": "Epidemiología Clínica", "autor": "Sackett y Guyatt", "editorial": "—", "tipo": "Libro"},
    {"titulo": "El Proceso de Investigación Clínica", "autor": "Saúl León Hernández", "editorial": "—", "tipo": "Libro"},
    # De biblioteca CIDOCS
    {"titulo": "Sabiston Tratado de Cirugía", "autor": "Townsend / Beauchamp / Evers / Mattox", "editorial": "Elsevier", "tipo": "Libro"},
    {"titulo": "Schwartz Principles of Surgery", "autor": "Brunicardi", "editorial": "McGraw Hill", "tipo": "Libro"},
    {"titulo": "Blumgart's Surgery of the Liver, Biliary Tract & Pancreas", "autor": "Jarnagin et al.", "editorial": "Elsevier", "tipo": "Libro"},
    {"titulo": "Current Surgical Therapy", "autor": "Cameron", "editorial": "Elsevier", "tipo": "Libro"},
    {"titulo": "Enfermedades del Hígado y Vías Biliares", "autor": "Sheila Sherlock", "editorial": "Marbán", "tipo": "Libro"},
    {"titulo": "Cirugía Laparoscópica Avanzada", "autor": "Katkhouda", "editorial": "McGraw Hill", "tipo": "Libro"},
    {"titulo": "Tratado de Cirugía General Vol. I y II", "autor": "Asociación Mexicana de Cirugía General", "editorial": "Manual Moderno", "tipo": "Libro"},
    {"titulo": "Mastery of Surgery", "autor": "Fischer", "editorial": "Wolters Kluwer", "tipo": "Libro"},
    {"titulo": "Greenfield's Surgery", "autor": "Greenfield", "editorial": "Wolters Kluwer", "tipo": "Libro"},
    {"titulo": "EMC Técnicas Quirúrgicas / Cirugía General", "autor": "Elsevier Masson", "editorial": "Elsevier Masson", "tipo": "Libro"},
    {"titulo": "Nutrición Enteral y Parenteral", "autor": "Pardo Anaya, Arenas Márquez", "editorial": "McGraw Hill", "tipo": "Libro"},
    {"titulo": "Diagnóstico y Tratamiento Quirúrgico", "autor": "Dherty", "editorial": "Manual Moderno", "tipo": "Libro"},
    {"titulo": "Atlas de Cirugía del Aparato Digestivo", "autor": "Cameron, Sandone", "editorial": "Panamericana", "tipo": "Libro"},
    {"titulo": "Cirugía (Skandalakis)", "autor": "Skandalakis", "editorial": "Marbán", "tipo": "Libro"},
]

# Revistas científicas recomendadas
REVISTAS = [
    {"titulo": "American Journal of Surgery", "tipo": "Revista"},
    {"titulo": "Annals of Surgery", "tipo": "Revista"},
    {"titulo": "British Journal of Surgery", "tipo": "Revista"},
    {"titulo": "World Journal of Surgery", "tipo": "Revista"},
    {"titulo": "Surgical Endoscopy", "tipo": "Revista"},
    {"titulo": "Gastrointestinal Surgery", "tipo": "Revista"},
    {"titulo": "Cirugía y Cirujanos", "tipo": "Revista"},
    {"titulo": "Cirujano General", "tipo": "Revista"},
    {"titulo": "Revista Mexicana de Cirugía Endoscópica", "tipo": "Revista"},
]

# Mapeo de palabras clave de temas → libros relevantes (por índice en LIBROS)
# El mapeo usa palabras clave que aparecen en los temas de las clases
MAPEO_TEMAS = {
    # Bases
    "historia|cirugía|introducción|cirugía general": [0, 9, 11, 17],
    "asepsia|antisepsia|lavado|estéril": [0, 1, 11],
    "cicatrización|herida|sutura|tejido|úlcera|injerto|piel": [1, 2, 11],
    "anestésico|sutura|técnica|nudo": [0, 1, 11],
    "trauma quirúrgico|respuesta metabólica|neuroendocrina|inflamatoria": [0, 2, 10, 17],
    "líquidos|electrolitos|hidratación|reposición": [0, 2, 11],
    "nutrición|nutricional|ERAS|bariátrico|metabólica|obesidad|bypass|manga": [0, 2, 26, 11],

    # Pared abdominal / hernias
    "hernia|hernias|pared abdominal|inguinal|umbilical|epigástrica|diástasis|reparación|onlay|rives|stoppa": [4, 5, 0, 11],

    # Esófago
    "esófago|esofágico|esofagitis|barrett|acalasia|deglución|reflujo|ERGE|hernia hiatal|fundoplastia|cáustica": [8, 0, 7, 17],

    # Estómago / duodeno
    "gástrica|gastrostomía|gastrectomía|estómago|duodeno|duodenal|úlcera péptica|obstrucción|sangrado digestivo": [0, 2, 5, 7, 17],

    # Intestino delgado
    "intestino delgado|yeyuno|íleon|malabsorción|intestino corto|isquemia mesentérica|obstrucción intestinal|fístulas": [0, 2, 5, 7],

    # Colon / apéndice / divertículos
    "colon|apéndice|apendicitis|diverticular|diverticulitis|colitis": [0, 7, 11, 17],

    # Coloproctología
    "recto|ano|hemorroide|fisura|absceso perianal|fístula perianal|quiste pilonidal|prolapso rectal|incontinencia fecal|piso pélvico|coloproctología|estoma|anastomosis colorrectal|poliposis": [0, 7, 11, 17],

    # Hígado / vías biliares
    "hígado|hepática|biliares|biliar|colecistitis|colelitiasis|ictericia|colecistectomía|hepatectomía|hepatocarcinoma|metástasis hepáticas|quiste hepático|absceso hepático|obstrucción biliar|lesión vía biliar|cirugía reconstructiva": [18, 20, 0, 17, 28],

    # Páncreas / bazo
    "páncreas|pancreatitis|pseudoquiste|pancreático|bazo|esplenectomía|neuroendocrino": [18, 0, 7, 17],

    # Trauma
    "trauma|herida|balística|cinemática|control de daños|toracotomía en trauma|víscera|retroperitoneal|vascular periférico|raquimedular|craneoencefálico": [10, 0, 11, 17],

    # Tórax
    "tórax|torácico|mediastino|mediastinal|pulmón|pulmonar|neumotórax|hemotórax|empiema|toracotomía|resección pulmonar|cáncer pulmonar": [0, 11, 24, 17],

    # Cirugía vascular
    "vascular|carotídea|vertebrobasilar|venosa|tromboembólica|isquemia|arterial|aneurisma|pie diabético|insuficiencia venosa": [0, 11, 17],

    # Mama / ginecología
    "mama|mastectomía|disección axilar|cáncer de mama|patología benigna de la mama|ginecológica|oncología ginecológica": [0, 11, 17],

    # Piel / tejidos blandos / quemaduras
    "quemado|quemadura|colgajo|lesión maligna|sarcoma|piel|tejidos blandos": [0, 1, 11],

    # Cabeza y cuello
    "cuello|tiroides|tiroidectomía|paratiroides|glándulas salivales|nódulo tiroideo|cáncer de tiroides|disección": [0, 11, 17],

    # Urología
    "urología|urolitiasis|riñón|próstata|cáncer de próstata|fimosis|hidrocele|varicocele|hiperplasia prostática": [0, 11, 17],

    # Cirugía endocrina
    "feocromocitoma|suprarrenal|neoplasia endocrina múltiple|paratiroides|tiroides|endocrina": [0, 11, 17],

    # Cirugía oncológica
    "oncológica|oncología|cáncer|carcinoma|tumor|sarcoma|metástasis|hepatocarcinoma|cáncer de colon|cáncer de recto|cáncer de estómago|cáncer de vía biliar": [0, 11, 17, 19, 29],

    # Cirugía pediátrica
    "pediátrica|pediátrico|gastrosquisis|onfalocele|malrotación|intususcepción|hernias en la población pediátrica": [0, 11, 17],

    # Neurocirugía
    "neurocirugía|cerebrovascular|columna|degenerativa|raquimedular|tumor nervioso central|exploración neurológica": [0, 17],

    # Laparoscopia / mínima invasión
    "laparoscópica|laparoscopia|endoscopia|mínima invasión": [21, 0, 6, 17],

    # Bioética / deontología
    "bioética|deontología|ética|relación médico|error médico|manejo ético": [14, 15],

    # Métodos de investigación
    "investigación|protocolo|bioestadística|epidemiología|metodología": [13, 14, 15],
}


def sugerir_bibliografia(tema: str) -> list:
    """
    Dado un tema de clase, retorna lista de libros y revistas sugeridos.
    Combina resultados por palabras clave y siempre incluye libros base.
    """
    tema_lower = tema.lower()
    indices_sugeridos = set()

    for patron, indices in MAPEO_TEMAS.items():
        palabras = patron.split("|")
        for palabra in palabras:
            if palabra.strip() in tema_lower:
                indices_sugeridos.update(indices)
                break

    # Siempre incluir los 3 libros base si no hay match o como complemento
    if not indices_sugeridos:
        indices_sugeridos = {0, 9, 11}  # Schwartz, Dominio Cirugía, Tratado AMCG

    sugerencias = [LIBROS[i] for i in sorted(indices_sugeridos) if i < len(LIBROS)]

    # Agregar revistas siempre
    return sugerencias, REVISTAS
