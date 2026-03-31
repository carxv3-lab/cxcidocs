"""
Temario completo de Unidades Didácticas - Cirugía General UAS 2026-2027
Ciclo: 1 de marzo de 2026 - 28 de febrero de 2027
Horario de clases: Martes a Viernes 7:00-8:00 am
"""

from datetime import date

CLASES = [
    # =====================================================================
    # PRIMER AÑO (R1) - Bases Quirúrgicas
    # Coordinadores: Dr. Marcel Antonio Cázares Aguilar, Dr. Pedro Magaña Olivas
    # =====================================================================

    # Introducción a la cirugía
    {"fecha": date(2026, 3, 3),  "tema": "Historia de la cirugía",
     "categoria": "Introducción a la cirugía", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 3, 4),  "tema": "Asepsia y antisepsia",
     "categoria": "Introducción a la cirugía", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 3, 5),  "tema": "Cicatrización y clasificación de heridas quirúrgicas",
     "categoria": "Introducción a la cirugía", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Francisco Magaña Olivas"},
    {"fecha": date(2026, 3, 10), "tema": "Anestésicos locales, suturas y técnicas de sutura",
     "categoria": "Introducción a la cirugía", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 3, 11), "tema": "Trauma quirúrgico (respuesta metabólica al trauma)",
     "categoria": "Introducción a la cirugía", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Martín Adrián Bolívar Rodríguez"},
    {"fecha": date(2026, 3, 12), "tema": "Líquidos y electrolitos en el paciente quirúrgico",
     "categoria": "Introducción a la cirugía", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},

    # Pared abdominal R1
    {"fecha": date(2026, 3, 26), "tema": "Hernia ventral primaria (umbilical, epigástrica) y diástasis de rectos",
     "categoria": "Pared abdominal", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Francisco Magaña Olivas"},
    {"fecha": date(2026, 4, 14), "tema": "Hernia inguinal",
     "categoria": "Pared abdominal", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 4, 29), "tema": "Hernias poco frecuentes",
     "categoria": "Pared abdominal", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Carlos Mendoza Chang"},

    # Cirugía digestiva R1 - Esófago
    {"fecha": date(2026, 5, 5),  "tema": "Anatomía quirúrgica y fisiología del esófago",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 5, 6),  "tema": "ERGE y esófago de Barrett",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 5, 7),  "tema": "Acalasia y trastornos motores del esófago",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},
    {"fecha": date(2026, 5, 12), "tema": "Cuerpos extraños y quemaduras cáusticas en esófago",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Carlos Enrique Amaral Peña"},
    {"fecha": date(2026, 5, 13), "tema": "Hernia hiatal",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Carlos Mendoza Chang"},
    {"fecha": date(2026, 5, 19), "tema": "Anatomía y fisiología gástrica y duodenal",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},
    {"fecha": date(2026, 6, 2),  "tema": "Anatomía y fisiología de intestino delgado",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 6, 3),  "tema": "Obstrucción intestinal alta",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 6, 11), "tema": "Tumores del intestino delgado: benignos y malignos",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2026, 6, 16), "tema": "Anatomía de colon y apéndice",
     "categoria": "Cirugía digestiva", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},

    # Coloproctología R1
    {"fecha": date(2026, 6, 23), "tema": "Anatomía de recto y ano",
     "categoria": "Coloproctología", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Benny Alonso Osuna Wong"},
    {"fecha": date(2026, 6, 24), "tema": "Enfermedad hemorroidal y fisuras anales",
     "categoria": "Coloproctología", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Benny Alonso Osuna Wong"},
    {"fecha": date(2026, 6, 25), "tema": "Enfermedad criptoglandular (abscesos perianales)",
     "categoria": "Coloproctología", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Benny Alonso Osuna Wong"},
    {"fecha": date(2026, 7, 1),  "tema": "Quiste pilonidal",
     "categoria": "Coloproctología", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Benny Alonso Osuna Wong"},
    {"fecha": date(2026, 7, 8),  "tema": "Prolapso rectal",
     "categoria": "Coloproctología", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Benny Alonso Osuna Wong"},

    # Hígado y vías biliares R1
    {"fecha": date(2026, 7, 14), "tema": "Anatomía del hígado y vías biliares. Anomalías anatómicas de vía biliar",
     "categoria": "Hígado y vías biliares", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 7, 15), "tema": "Fisiología hepática y funciones biliares",
     "categoria": "Hígado y vías biliares", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 8, 4),  "tema": "Colelitiasis y colecistitis",
     "categoria": "Hígado y vías biliares", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Carlos Mendoza Chang"},
    {"fecha": date(2026, 8, 12), "tema": "Quistes hepáticos",
     "categoria": "Hígado y vías biliares", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Carlos Enrique Amaral Peña"},
    {"fecha": date(2026, 8, 13), "tema": "Absceso hepático",
     "categoria": "Hígado y vías biliares", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Carlos Mendoza Chang"},

    # Páncreas y bazo R1
    {"fecha": date(2026, 8, 25), "tema": "Anatomía quirúrgica y fisiología de páncreas",
     "categoria": "Páncreas y bazo", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Carlos Mendoza Chang"},
    {"fecha": date(2026, 9, 1),  "tema": "Pancreatitis crónica y pseudoquiste pancreático",
     "categoria": "Páncreas y bazo", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 9, 3),  "tema": "Anatomía y fisiología de bazo",
     "categoria": "Páncreas y bazo", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Carlos Mendoza Chang"},

    # Trauma R1
    {"fecha": date(2026, 9, 9),  "tema": "Cinemática del trauma",
     "categoria": "Trauma", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 9, 10), "tema": "Balística para el cirujano",
     "categoria": "Trauma", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 9, 18), "tema": "Trauma de colon y recto",
     "categoria": "Trauma", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},

    # Cirugía metabólica R1
    {"fecha": date(2026, 10, 6), "tema": "Mecanismos fisiológicos de los procedimientos bariátricos",
     "categoria": "Cirugía metabólica", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Francisco Magaña Olivas"},
    {"fecha": date(2026, 10, 7), "tema": "Indicaciones y contraindicaciones en cirugía bariátrica",
     "categoria": "Cirugía metabólica", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Carlos Enrique Amaral Peña"},

    # Cirugía de tórax R1
    {"fecha": date(2026, 10, 15), "tema": "Anatomía quirúrgica de tórax y mediastino",
     "categoria": "Cirugía de tórax", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Rafael Quezada Angulo"},
    {"fecha": date(2026, 10, 16), "tema": "Cirugía de patología benigna del pulmón",
     "categoria": "Cirugía de tórax", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Rafael Quezada Angulo"},
    {"fecha": date(2026, 10, 21), "tema": "Neumotórax, hemotórax y empiema: manejo con tubo torácico",
     "categoria": "Cirugía de tórax", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Ramón Enrique Montiel Trejo"},

    # Cirugía de piel y tejidos blandos R1
    {"fecha": date(2026, 11, 5),  "tema": "Anatomía quirúrgica de la mama y del aparato genital femenino",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Mauricio Israel Soriano Benítez"},
    {"fecha": date(2026, 11, 6),  "tema": "Patología benigna de la mama",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Mauricio Israel Soriano Benítez"},
    {"fecha": date(2026, 11, 13), "tema": "Abordaje inicial del paciente quemado y fisiopatología",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Daniel Simón Servín Uribe"},
    {"fecha": date(2026, 11, 18), "tema": "Úlceras por presión y heridas crónicas",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Daniel Simón Servín Uribe"},
    {"fecha": date(2026, 11, 19), "tema": "Injertos y substitutos de piel",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Daniel Simón Servín Uribe"},
    {"fecha": date(2026, 11, 24), "tema": "Lesiones malignas en piel",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Daniel Simón Servín Uribe"},

    # Cirugía de cabeza y cuello R1
    {"fecha": date(2026, 11, 25), "tema": "Anatomía quirúrgica de cuello",
     "categoria": "Cirugía de cabeza y cuello", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2026, 12, 1),  "tema": "Patología quirúrgica de glándulas salivales",
     "categoria": "Cirugía de cabeza y cuello", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},

    # Cirugía vascular R1
    {"fecha": date(2026, 12, 8),  "tema": "Pie diabético",
     "categoria": "Cirugía vascular", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Patricio Félix Rodríguez"},

    # Cirugía urológica R1
    {"fecha": date(2026, 12, 15), "tema": "Urolitiasis y patología benigna de riñón",
     "categoria": "Cirugía urológica", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dr. Miguel Ángel Sandoval Valle"},
    {"fecha": date(2026, 12, 16), "tema": "Fimosis, parafimosis y técnicas quirúrgicas",
     "categoria": "Cirugía urológica", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. José René Jungfermann Guzmán"},
    {"fecha": date(2026, 12, 17), "tema": "Hidrocele y varicocele",
     "categoria": "Cirugía urológica", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. Miguel Ángel Sandoval Valle"},
    {"fecha": date(2027, 1, 6),   "tema": "Cáncer de próstata",
     "categoria": "Cirugía urológica", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dr. José René Jungfermann Guzmán"},

    # Cirugía endocrina R1
    {"fecha": date(2027, 1, 12), "tema": "Patología de paratiroides y abordaje quirúrgico",
     "categoria": "Cirugía endocrina", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2027, 1, 13), "tema": "Neoplasia endocrina múltiple",
     "categoria": "Cirugía endocrina", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Carlos Enrique Amaral Peña"},

    # Cirugía oncológica R1
    {"fecha": date(2027, 1, 19), "tema": "Sarcomas de partes blandas",
     "categoria": "Cirugía oncológica", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2027, 1, 28), "tema": "Cáncer de páncreas",
     "categoria": "Cirugía oncológica", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Carlos Hilario Diarte Ríos"},

    # Cirugía pediátrica R1
    {"fecha": date(2027, 1, 29), "tema": "Particularidades fisiológicas y cuidado perioperatorio en el paciente pediátrico quirúrgico",
     "categoria": "Cirugía pediátrica", "grado": "R1",
     "ponente": "Valdez Valdez Ricardo Antonio", "asesor": "Dra. Arcelia Soriano Benítez"},
    {"fecha": date(2027, 2, 2),  "tema": "Trauma en la población pediátrica",
     "categoria": "Cirugía pediátrica", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dra. Arcelia Soriano Benítez"},
    {"fecha": date(2027, 2, 4),  "tema": "Hernias en la población pediátrica",
     "categoria": "Cirugía pediátrica", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dra. Arcelia Soriano Benítez"},
    {"fecha": date(2027, 2, 9),  "tema": "Abdomen agudo en la población pediátrica",
     "categoria": "Cirugía pediátrica", "grado": "R1",
     "ponente": "Rendón Sánchez Manuel", "asesor": "Dra. Arcelia Soriano Benítez"},

    # Neurocirugía R1
    {"fecha": date(2027, 2, 18), "tema": "Trauma craneoencefálico",
     "categoria": "Neurocirugía", "grado": "R1",
     "ponente": "Romero Molina Geovana Clarisa", "asesor": "Dr. Edgar Fragoza Sánchez"},

    # Bioética R1
    {"fecha": date(2027, 2, 19), "tema": "Principios de bioética",
     "categoria": "Bioética", "grado": "R1",
     "ponente": "Portugal Beltrán Emma", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2027, 2, 23), "tema": "Deontología",
     "categoria": "Bioética", "grado": "R1",
     "ponente": "López Félix Jesús Arturo", "asesor": "Dr. Rodolfo Fierro López"},

    # =====================================================================
    # SEGUNDO AÑO (R2) - Patología Quirúrgica
    # Coordinadores: Dr. Carlos Arturo Respardo Ramírez, Dr. Pedro Magaña Olivas
    # =====================================================================

    # Introducción / nutrición
    {"fecha": date(2026, 3, 17), "tema": "Nutrición en cirugía",
     "categoria": "Introducción a la cirugía", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},
    {"fecha": date(2026, 3, 18), "tema": "Protocolo ERAS",
     "categoria": "Introducción a la cirugía", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Martín Adrián Bolívar Rodríguez"},

    # Pared abdominal R2
    {"fecha": date(2026, 3, 19), "tema": "Anatomía de la pared abdominal",
     "categoria": "Pared abdominal", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 4, 16), "tema": "Separación de componentes anterior y posterior",
     "categoria": "Pared abdominal", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},

    # Cirugía digestiva R2
    {"fecha": date(2026, 5, 26), "tema": "Sangrado digestivo alto: abordaje diagnóstico y terapéutico",
     "categoria": "Cirugía digestiva", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Francisco Magaña Olivas"},
    {"fecha": date(2026, 5, 28), "tema": "Técnica quirúrgica: gastrostomías y piloroplastias",
     "categoria": "Cirugía digestiva", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 5, 29), "tema": "Complicaciones postoperatorias en cirugía gástrica",
     "categoria": "Cirugía digestiva", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Carlos Mendoza Chang"},
    {"fecha": date(2026, 6, 9),  "tema": "Síndrome de intestino corto y malabsorción",
     "categoria": "Cirugía digestiva", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Martín Adrián Bolívar Rodríguez"},
    {"fecha": date(2026, 6, 10), "tema": "Isquemia mesentérica",
     "categoria": "Cirugía digestiva", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},
    {"fecha": date(2026, 6, 17), "tema": "Apendicitis aguda",
     "categoria": "Cirugía digestiva", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Carlos Enrique Amaral Peña"},
    {"fecha": date(2026, 6, 18), "tema": "Enfermedad diverticular de colon",
     "categoria": "Cirugía digestiva", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Benny Alonso Osuna Wong"},

    # Coloproctología R2
    {"fecha": date(2026, 6, 30), "tema": "Fístula perianal",
     "categoria": "Coloproctología", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Benny Alonso Osuna Wong"},
    {"fecha": date(2026, 7, 2),  "tema": "Poliposis colorrectal",
     "categoria": "Coloproctología", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Benny Alonso Osuna Wong"},

    # Hígado y vías biliares R2
    {"fecha": date(2026, 7, 16), "tema": "Evaluación diagnóstica de hígado y vías biliares",
     "categoria": "Hígado y vías biliares", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 8, 5),  "tema": "Obstrucción de la vía biliar",
     "categoria": "Hígado y vías biliares", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},
    {"fecha": date(2026, 8, 11), "tema": "Enfermedad quística de la vía biliar",
     "categoria": "Hígado y vías biliares", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 8, 19), "tema": "Colecistectomía segura",
     "categoria": "Hígado y vías biliares", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},

    # Páncreas y bazo R2
    {"fecha": date(2026, 8, 26), "tema": "Pancreatitis aguda",
     "categoria": "Páncreas y bazo", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},
    {"fecha": date(2026, 9, 2),  "tema": "Manejo quirúrgico de pancreatitis crónica y pseudoquiste",
     "categoria": "Páncreas y bazo", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Martín Adrián Bolívar Rodríguez"},
    {"fecha": date(2026, 9, 8),  "tema": "Esplenectomía abierta y laparoscópica (técnica quirúrgica)",
     "categoria": "Páncreas y bazo", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},

    # Trauma R2
    {"fecha": date(2026, 9, 17), "tema": "Trauma de víscera hueca: estómago e intestino delgado",
     "categoria": "Trauma", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Carlos Mendoza Chang"},
    {"fecha": date(2026, 9, 23), "tema": "Trauma duodenal y pancreático",
     "categoria": "Trauma", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},
    {"fecha": date(2026, 9, 24), "tema": "Laparotomía en trauma: principios y técnicas",
     "categoria": "Trauma", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Carlos Mendoza Chang"},

    # Cirugía metabólica R2
    {"fecha": date(2026, 10, 8),  "tema": "Cuidados preoperatorios en el paciente bariátrico",
     "categoria": "Cirugía metabólica", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Francisco Magaña Olivas"},
    {"fecha": date(2026, 10, 14), "tema": "Postoperatorio y complicaciones nutricionales en cirugía bariátrica",
     "categoria": "Cirugía metabólica", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Francisco Magaña Olivas"},

    # Cirugía de tórax R2
    {"fecha": date(2026, 10, 22), "tema": "Nódulo pulmonar solitario y metástasis pulmonares",
     "categoria": "Cirugía de tórax", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Rafael Quezada Angulo"},

    # Cirugía de mama y ginecología R2
    {"fecha": date(2026, 11, 11), "tema": "Patología quirúrgica ginecológica no oncológica",
     "categoria": "Cirugía de mama y ginecología", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Mauricio Israel Soriano Benítez"},

    # Cirugía de piel y tejidos blandos R2
    {"fecha": date(2026, 11, 17), "tema": "Manejo quirúrgico y aspectos específicos de las quemaduras",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Daniel Simón Servín Uribe"},

    # Cirugía de cabeza y cuello R2
    {"fecha": date(2026, 11, 26), "tema": "Lesiones congénitas del cuello",
     "categoria": "Cirugía de cabeza y cuello", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},

    # Cirugía vascular R2
    {"fecha": date(2026, 12, 4),  "tema": "Insuficiencia venosa periférica y de pelvis",
     "categoria": "Cirugía vascular", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Christian Orlando Guadrón Llanos"},

    # Cirugía urológica R2
    {"fecha": date(2026, 12, 18), "tema": "Patología maligna de riñón",
     "categoria": "Cirugía urológica", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Jesús Leonardo Camargo Altamirano"},
    {"fecha": date(2027, 1, 5),   "tema": "Hiperplasia prostática benigna",
     "categoria": "Cirugía urológica", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Euclides Camacho Montoya"},

    # Cirugía endocrina R2
    {"fecha": date(2027, 1, 14), "tema": "Feocromocitoma",
     "categoria": "Cirugía endocrina", "grado": "R2",
     "ponente": "Valenzuela Pardo Mariana", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},

    # Cirugía oncológica R2
    {"fecha": date(2027, 1, 20), "tema": "Cáncer de estómago",
     "categoria": "Cirugía oncológica", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2027, 1, 26), "tema": "Hepatocarcinoma y metástasis hepáticas",
     "categoria": "Cirugía oncológica", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Carlos Hilario Diarte Ríos"},

    # Neurocirugía R2
    {"fecha": date(2027, 2, 11), "tema": "Trastornos cerebrovasculares",
     "categoria": "Neurocirugía", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Edgar Fragoza Sánchez"},
    {"fecha": date(2027, 2, 12), "tema": "Patología degenerativa de la columna",
     "categoria": "Neurocirugía", "grado": "R2",
     "ponente": "Luna Borboa Jorge Luis", "asesor": "Dr. Guillermo Pérez Baldenegro"},
    {"fecha": date(2027, 2, 17), "tema": "Trauma raquimedular",
     "categoria": "Neurocirugía", "grado": "R2",
     "ponente": "Maldonado Guardado Diana Guadalupe", "asesor": "Dr. Guillermo Pérez Baldenegro"},

    # Bioética R2
    {"fecha": date(2027, 2, 24), "tema": "Relación médico-paciente",
     "categoria": "Bioética", "grado": "R2",
     "ponente": "Angulo Sánchez Rolando", "asesor": "Dr. Martín Adrián Bolívar Rodríguez"},

    # =====================================================================
    # TERCER AÑO (R3) - Terapéutica Quirúrgica
    # Coordinadores: Dr. Martín Adrián Bolívar Rodríguez, Dr. Carlos Arturo Respardo Ramírez
    # =====================================================================

    # Pared abdominal R3
    {"fecha": date(2026, 3, 24), "tema": "Anatomía anterior y posterior de la región inguinal",
     "categoria": "Pared abdominal", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Carlos Mendoza Chang"},
    {"fecha": date(2026, 4, 28), "tema": "Manejo abierto y mínima invasión en hernia inguinal",
     "categoria": "Pared abdominal", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},

    # Cirugía digestiva R3
    {"fecha": date(2026, 5, 14), "tema": "Cirugía de esófago",
     "categoria": "Cirugía digestiva", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Carlos Mendoza Chang"},
    {"fecha": date(2026, 5, 20), "tema": "Enfermedad ulcerosa péptica",
     "categoria": "Cirugía digestiva", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Carlos Enrique Amaral Peña"},
    {"fecha": date(2026, 5, 21), "tema": "Complicación de la enfermedad ulcerosa",
     "categoria": "Cirugía digestiva", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 5, 27), "tema": "Técnica quirúrgica: gastrectomías",
     "categoria": "Cirugía digestiva", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dr. Francisco Magaña Olivas"},
    {"fecha": date(2026, 6, 4),  "tema": "Fístulas de intestino delgado",
     "categoria": "Cirugía digestiva", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},

    # Coloproctología R3
    {"fecha": date(2026, 7, 3),  "tema": "Estomas y anastomosis colorrectales",
     "categoria": "Coloproctología", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Benny Alonso Osuna Wong"},
    {"fecha": date(2026, 7, 7),  "tema": "Trastornos de piso pélvico e incontinencia fecal",
     "categoria": "Coloproctología", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dr. Benny Alonso Osuna Wong"},

    # Hígado y vías biliares R3
    {"fecha": date(2026, 8, 6),  "tema": "Lesión de la vía biliar y fugas biliares",
     "categoria": "Hígado y vías biliares", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},
    {"fecha": date(2026, 8, 20), "tema": "Hepatectomías",
     "categoria": "Hígado y vías biliares", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2026, 8, 27), "tema": "Manejo quirúrgico step up en pancreatitis aguda",
     "categoria": "Páncreas y bazo", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},

    # Trauma R3
    {"fecha": date(2026, 9, 15), "tema": "Trauma de víscera sólida: hígado, tracto biliar y bazo",
     "categoria": "Trauma", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Martín Adrián Bolívar Rodríguez"},
    {"fecha": date(2026, 9, 22), "tema": "Trauma retroperitoneal y pelvis: grandes vasos y tracto genitourinario",
     "categoria": "Trauma", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dr. Rodolfo Fierro López"},
    {"fecha": date(2026, 9, 30), "tema": "Trauma de cuello y laringe",
     "categoria": "Trauma", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Carlos Arturo Respardo Ramírez"},
    {"fecha": date(2026, 10, 1),  "tema": "Control de daños en trauma",
     "categoria": "Trauma", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Carlos Mendoza Chang"},

    # Cirugía metabólica R3
    {"fecha": date(2026, 10, 9),  "tema": "Manga gástrica",
     "categoria": "Cirugía metabólica", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dr. Carlos Enrique Amaral Peña"},

    # Cirugía de tórax R3
    {"fecha": date(2026, 10, 20), "tema": "Masas mediastinales y patología quirúrgica del mediastino",
     "categoria": "Cirugía de tórax", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Ramón Enrique Montiel Trejo"},
    {"fecha": date(2026, 11, 3),  "tema": "Mediastinitis y acceso quirúrgico a mediastino",
     "categoria": "Cirugía de tórax", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Rafael Quezada Angulo"},

    # Oncología ginecológica R3
    {"fecha": date(2026, 11, 12), "tema": "Oncología ginecológica",
     "categoria": "Cirugía de mama y ginecología", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Mauricio Israel Soriano Benítez"},

    # Cirugía de cabeza y cuello R3
    {"fecha": date(2026, 11, 27), "tema": "Nódulo tiroideo y cáncer de tiroides",
     "categoria": "Cirugía de cabeza y cuello", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Carlos Hilario Diarte Ríos"},

    # Cirugía vascular R3
    {"fecha": date(2026, 12, 3),  "tema": "Enfermedad carotídea y vertebrobasilar",
     "categoria": "Cirugía vascular", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Rodrigo Valencia Jiménez"},
    {"fecha": date(2026, 12, 9),  "tema": "Enfermedad tromboembólica venosa",
     "categoria": "Cirugía vascular", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dr. Christian Orlando Guadrón Llanos"},
    {"fecha": date(2026, 12, 10), "tema": "Isquemia aguda y crónica de miembros inferiores",
     "categoria": "Cirugía vascular", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Rodrigo Valencia Jiménez"},
    {"fecha": date(2026, 12, 11), "tema": "Trauma vascular periférico",
     "categoria": "Cirugía vascular", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Christian Orlando Guadrón Llanos"},

    # Cirugía oncológica R3
    {"fecha": date(2027, 1, 7),   "tema": "Patología de glándula suprarrenal",
     "categoria": "Cirugía oncológica", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},
    {"fecha": date(2027, 1, 15),  "tema": "Principios de cirugía oncológica",
     "categoria": "Cirugía oncológica", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2027, 1, 21),  "tema": "Cáncer de colon",
     "categoria": "Cirugía oncológica", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2027, 1, 22),  "tema": "Cáncer de recto y ano",
     "categoria": "Cirugía oncológica", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2027, 1, 27),  "tema": "Cáncer de vía biliar",
     "categoria": "Cirugía oncológica", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dr. Carlos Hilario Diarte Ríos"},

    # Cirugía pediátrica R3
    {"fecha": date(2027, 2, 3),  "tema": "Defectos congénitos de la pared abdominal: gastrosquisis y onfalocele",
     "categoria": "Cirugía pediátrica", "grado": "R3",
     "ponente": "Cordero Medina Marielos", "asesor": "Dra. Arcelia Soriano Benítez"},
    {"fecha": date(2027, 2, 5),  "tema": "Malrotaciones intestinales e intususcepción",
     "categoria": "Cirugía pediátrica", "grado": "R3",
     "ponente": "Bueno López Daniela Alejandra", "asesor": "Dra. Arcelia Soriano Benítez"},

    # Neurocirugía R3
    {"fecha": date(2027, 2, 10), "tema": "Exploración neurológica dirigida",
     "categoria": "Neurocirugía", "grado": "R3",
     "ponente": "Almanza Orduño Athmir Antonio", "asesor": "Dr. Guillermo Pérez Baldenegro"},
    {"fecha": date(2027, 2, 16), "tema": "Tumores del sistema nervioso central",
     "categoria": "Neurocirugía", "grado": "R3",
     "ponente": "Ojeda Valenzuela José Antonio", "asesor": "Dr. Edgar Fragoza Sánchez"},

    # =====================================================================
    # CUARTO AÑO (R4) - Procedimientos Quirúrgicos Específicos
    # Coordinadores: Dr. Martín Adrián Bolívar Rodríguez, Dr. Carlos Arturo Respardo Ramírez
    # =====================================================================

    {"fecha": date(2026, 3, 25), "tema": "Fisiopatología y génesis herniaria",
     "categoria": "Pared abdominal", "grado": "R4",
     "ponente": "Villegas Rodríguez José", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},
    {"fecha": date(2026, 4, 15), "tema": "Técnica quirúrgica: reparación Onlay y retromuscular Rives-Stoppa",
     "categoria": "Pared abdominal", "grado": "R4",
     "ponente": "Soto Valle José Emaús", "asesor": "Dr. Pedro Alejandro Magaña Zavala"},
    {"fecha": date(2026, 7, 9),  "tema": "Enfermedad inflamatoria intestinal: CUCI y Crohn",
     "categoria": "Cirugía digestiva", "grado": "R4",
     "ponente": "Beltrán Delgado Jorge Omar", "asesor": "Dr. Benny Alonso Osuna Wong"},
    {"fecha": date(2026, 8, 18), "tema": "Cirugía reconstructiva de la vía biliar",
     "categoria": "Hígado y vías biliares", "grado": "R4",
     "ponente": "Villegas Rodríguez José", "asesor": "Dr. Marcel Antonio Cázares Aguilar"},
    {"fecha": date(2026, 9, 29), "tema": "Toracotomía en trauma",
     "categoria": "Trauma", "grado": "R4",
     "ponente": "Villegas Rodríguez José", "asesor": "Dr. Ramón Enrique Montiel Trejo"},
    {"fecha": date(2026, 10, 13), "tema": "Bypass gástrico",
     "categoria": "Cirugía metabólica", "grado": "R4",
     "ponente": "Villegas Rodríguez José", "asesor": "Dr. Francisco Magaña Olivas"},
    {"fecha": date(2026, 10, 23), "tema": "Resecciones pulmonares",
     "categoria": "Cirugía de tórax", "grado": "R4",
     "ponente": "Beltrán Delgado Jorge Omar", "asesor": "Dr. Ramón Enrique Montiel Trejo"},
    {"fecha": date(2026, 11, 4),  "tema": "Cáncer pulmonar primario",
     "categoria": "Cirugía de tórax", "grado": "R4",
     "ponente": "Beltrán Delgado Jorge Omar", "asesor": "Dr. Ramón Enrique Montiel Trejo"},
    {"fecha": date(2026, 11, 10), "tema": "Cáncer de mama",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R4",
     "ponente": "Soto Valle José Emaús", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2026, 11, 20), "tema": "Colgajos cutáneos",
     "categoria": "Cirugía de piel y tejidos blandos", "grado": "R4",
     "ponente": "Soto Valle José Emaús", "asesor": "Dr. Daniel Simón Servín Uribe"},
    {"fecha": date(2026, 12, 2),  "tema": "Tiroidectomía y disección radical de cuello: técnica quirúrgica",
     "categoria": "Cirugía de cabeza y cuello", "grado": "R4",
     "ponente": "Beltrán Delgado Jorge Omar", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
    {"fecha": date(2027, 1, 8),   "tema": "Tumores neuroendocrinos de páncreas",
     "categoria": "Cirugía oncológica", "grado": "R4",
     "ponente": "Beltrán Delgado Jorge Omar", "asesor": "Dr. Carlos Hilario Diarte Ríos"},
]


def get_clases_por_fecha(fecha):
    """Retorna lista de clases programadas en una fecha específica."""
    return [c for c in CLASES if c["fecha"] == fecha]


def get_clases_por_grado(grado):
    """Retorna todas las clases de un grado académico, ordenadas por fecha."""
    return sorted([c for c in CLASES if c["grado"] == grado], key=lambda x: x["fecha"])


def get_proximas_clases(fecha_hoy, n=5):
    """Retorna las próximas n clases a partir de fecha_hoy."""
    proximas = [c for c in CLASES if c["fecha"] >= fecha_hoy]
    return sorted(proximas, key=lambda x: x["fecha"])[:n]
