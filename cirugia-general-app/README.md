# Programa Operativo 2026-2027 — Cirugía General UAS

App web para consulta de clases, rotaciones, vacaciones y bibliografía quirúrgica.

**Hospital Civil de Culiacán · CIDOCS · Universidad Autónoma de Sinaloa**

---

## Cómo usar la app localmente

```bash
cd cirugia-general-app
pip3 install -r requirements.txt
~/.local/bin/streamlit run app.py
# o bien:
python3 -m streamlit run app.py
```

Abre el navegador en: http://localhost:8501

---

## Cómo desplegar en internet (gratis) — Streamlit Community Cloud

1. Crear cuenta en https://github.com y subir esta carpeta como repositorio
2. Ir a https://streamlit.io/cloud y conectar con tu cuenta de GitHub
3. Hacer clic en "New app" → seleccionar tu repositorio → `app.py`
4. Hacer clic en "Deploy" — la app quedará pública con URL tipo `https://usuario.streamlit.app`

---

## Estructura

```
cirugia-general-app/
├── app.py                 # App principal (Streamlit)
├── requirements.txt
└── data/
    ├── clases.py          # 149 clases R1-R4 con fechas y ponentes
    ├── residentes.py      # 16 residentes con periodos vacacionales
    ├── rotaciones.py      # Rotaciones mensuales y externas
    └── bibliografia.py    # Libros, revistas y mapeo por tema
```

---

## Funciones

- **Inicio**: Clases de HOY y MAÑANA con bibliografía; residentes de vacaciones hoy
- **Clases por Grado**: Tabla filtrable R1-R4 con búsqueda por tema/categoría + bibliografía detallada
- **Rotaciones**: Por residente o vista general por mes; rotaciones externas
- **Vacaciones**: Tabla completa; consulta de quién está de vacaciones cualquier fecha
- **Bibliografía**: Búsqueda por tema, catálogo completo de libros y revistas
