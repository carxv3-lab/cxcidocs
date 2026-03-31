"""
Programa Operativo 2026-2027
Especialidad en Cirugía General - CIDOCS / Hospital Civil de Culiacán
Universidad Autónoma de Sinaloa
"""

import streamlit as st
import pandas as pd
from datetime import date, timedelta

from data.clases import CLASES, get_clases_por_fecha, get_clases_por_grado
from data.residentes import RESIDENTES, PERIODO_VACACIONAL_SS, esta_de_vacaciones
from data.rotaciones import ROTACIONES_MENSUALES, ROTACIONES_EXTERNAS, MESES, ABREV_ROTACION
from data.bibliografia import LIBROS, REVISTAS, sugerir_bibliografia

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Cirugía General UAS 2026-2027",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Estilos ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .header-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #1a3a5c;
    }
    .card {
        background: #f0f6ff;
        border-left: 5px solid #1a3a5c;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .card-manana {
        background: #fff7e6;
        border-left: 5px solid #e69500;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .badge-r1 { background:#d4edda; color:#155724; padding:2px 8px; border-radius:4px; font-size:.85rem; }
    .badge-r2 { background:#cce5ff; color:#004085; padding:2px 8px; border-radius:4px; font-size:.85rem; }
    .badge-r3 { background:#fff3cd; color:#856404; padding:2px 8px; border-radius:4px; font-size:.85rem; }
    .badge-r4 { background:#f8d7da; color:#721c24; padding:2px 8px; border-radius:4px; font-size:.85rem; }
    .bib-item { padding: 4px 0; border-bottom: 1px solid #eee; }
</style>
""", unsafe_allow_html=True)

DIAS_ES = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
           4: "Viernes", 5: "Sábado", 6: "Domingo"}
MESES_ES = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo",
            6: "junio", 7: "julio", 8: "agosto", 9: "septiembre",
            10: "octubre", 11: "noviembre", 12: "diciembre"}

HOY = date.today()
MANANA = HOY + timedelta(days=1)


def fecha_es(d: date) -> str:
    return f"{DIAS_ES[d.weekday()]} {d.day} de {MESES_ES[d.month]} de {d.year}"


def badge_grado(grado):
    return f'<span class="badge-{grado.lower()}">{grado}</span>'


def render_clase_card(clase, card_class="card"):
    libros_s, _ = sugerir_bibliografia(clase["tema"])
    bib_html = "".join(
        f'<div class="bib-item">📖 <b>{b["titulo"]}</b> — {b["autor"]}</div>'
        for b in libros_s[:3]
    )
    st.markdown(f"""
    <div class="{card_class}">
        <div style="font-size:1.05rem; font-weight:700; color:#1a3a5c;">{clase["tema"]}</div>
        <div style="color:#555; margin:4px 0;">
            {badge_grado(clase["grado"])}
            &nbsp;&nbsp;|&nbsp;&nbsp;
            <i>{clase["categoria"]}</i>
        </div>
        <div style="margin-top:6px;">
            <b>Ponente:</b> {clase["ponente"]}<br>
            <b>Asesor:</b> {clase["asesor"]}
        </div>
        <details style="margin-top:8px;">
            <summary style="cursor:pointer; color:#1a3a5c; font-weight:600;">
                Bibliografía sugerida
            </summary>
            <div style="margin-top:6px;">{bib_html}</div>
        </details>
    </div>
    """, unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/UAS_logotipo.svg/240px-UAS_logotipo.svg.png",
        width=120,
    )
    st.markdown("### Cirugía General UAS")
    st.markdown("**Ciclo 2026-2027**")
    st.markdown("Hospital Civil de Culiacán · CIDOCS")
    st.divider()
    pagina = st.radio(
        "Navegación",
        ["Inicio", "Clases por Grado", "Rotaciones", "Vacaciones", "Bibliografía"],
        format_func=lambda x: {
            "Inicio": "🏠  Inicio",
            "Clases por Grado": "📚  Clases por Grado",
            "Rotaciones": "🔄  Rotaciones",
            "Vacaciones": "🏖  Vacaciones",
            "Bibliografía": "📖  Bibliografía",
        }[x],
    )
    st.divider()
    st.caption(f"Hoy: {fecha_es(HOY)}")

# ── Inicio ───────────────────────────────────────────────────────────────────
if pagina == "Inicio":
    st.markdown('<div class="header-title">Programa Operativo — Cirugía General UAS 2026-2027</div>',
                unsafe_allow_html=True)
    st.markdown(f"**{fecha_es(HOY)}** &nbsp;·&nbsp; Clases: Martes a Viernes, 7:00–8:00 am")
    st.divider()

    clases_hoy = get_clases_por_fecha(HOY)
    clases_manana = get_clases_por_fecha(MANANA)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Hoy")
        if clases_hoy:
            for c in clases_hoy:
                render_clase_card(c, "card")
        else:
            dia = DIAS_ES[HOY.weekday()]
            if HOY.weekday() in (5, 6):
                st.info(f"Es {dia}. No hay clases en fin de semana. Guardia hospitalaria.")
            elif HOY.weekday() == 0:
                st.info("Es lunes. No hay clase programada hoy (pase de visita general).")
            else:
                st.info("No hay clase programada para hoy.")

    with col2:
        st.subheader(f"Mañana — {fecha_es(MANANA)}")
        if clases_manana:
            for c in clases_manana:
                render_clase_card(c, "card-manana")
        else:
            dia = DIAS_ES[MANANA.weekday()]
            if MANANA.weekday() in (5, 6):
                st.info(f"Mañana es {dia}. No hay clases programadas.")
            elif MANANA.weekday() == 0:
                st.info("Mañana es lunes. No hay clase (pase de visita general).")
            else:
                st.info("No hay clase programada para mañana.")

    # Próximas clases
    st.divider()
    st.subheader("Próximas clases")
    proximas = sorted([c for c in CLASES if c["fecha"] >= HOY], key=lambda x: x["fecha"])[:8]
    if proximas:
        df_prox = pd.DataFrame([{
            "Fecha": c["fecha"].strftime("%d %b %Y"),
            "Día": DIAS_ES[c["fecha"].weekday()],
            "Grado": c["grado"],
            "Tema": c["tema"],
            "Ponente": c["ponente"],
        } for c in proximas])
        st.dataframe(df_prox, use_container_width=True, hide_index=True)
    else:
        st.info("No hay clases próximas registradas.")

    # Residentes de vacaciones hoy
    st.divider()
    st.subheader("Residentes actualmente de vacaciones")
    de_vacaciones = []
    for r in RESIDENTES:
        en_vac, periodo = esta_de_vacaciones(r, HOY)
        if en_vac:
            de_vacaciones.append({
                "Residente": r["nombre"],
                "Grado": r["grado"],
                "Periodo": f"Periodo {periodo['periodo']}",
                "Regreso": (periodo["fin"] + timedelta(days=1)).strftime("%d %b %Y"),
            })
    if de_vacaciones:
        st.dataframe(pd.DataFrame(de_vacaciones), use_container_width=True, hide_index=True)
    else:
        st.success("Todos los residentes están activos hoy.")


# ── Clases por Grado ─────────────────────────────────────────────────────────
elif pagina == "Clases por Grado":
    st.markdown('<div class="header-title">Clases por Grado Académico</div>',
                unsafe_allow_html=True)
    st.divider()

    col_g, col_b = st.columns([2, 3])
    with col_g:
        grado = st.selectbox(
            "Seleccionar grado",
            ["R1", "R2", "R3", "R4"],
            format_func=lambda x: {
                "R1": "1er año — Bases Quirúrgicas",
                "R2": "2do año — Patología Quirúrgica",
                "R3": "3er año — Terapéutica Quirúrgica",
                "R4": "4to año — Procedimientos Específicos",
            }[x],
        )
    with col_b:
        busqueda = st.text_input("Buscar tema o categoría", placeholder="Ej: hígado, trauma, hernia...")

    clases_grado = get_clases_por_grado(grado)

    if busqueda:
        filtro = busqueda.lower()
        clases_grado = [c for c in clases_grado
                        if filtro in c["tema"].lower() or filtro in c["categoria"].lower()]

    st.markdown(f"**{len(clases_grado)} clase(s) encontradas** para {grado}")

    if clases_grado:
        df = pd.DataFrame([{
            "Fecha": c["fecha"].strftime("%d %b %Y"),
            "Día": DIAS_ES[c["fecha"].weekday()],
            "Categoría": c["categoria"],
            "Tema": c["tema"],
            "Ponente": c["ponente"],
            "Asesor": c["asesor"],
            "Estado": "Pasada" if c["fecha"] < HOY else ("HOY" if c["fecha"] == HOY else "Próxima"),
        } for c in clases_grado])

        st.dataframe(
            df.style.apply(
                lambda row: ["background-color: #eaf4ea" if row["Estado"] == "Próxima"
                             else ("background-color: #fff3cd" if row["Estado"] == "HOY"
                                   else "color: #888") for _ in row],
                axis=1,
            ),
            use_container_width=True,
            hide_index=True,
        )

        # Detalle de clase seleccionada con bibliografía
        st.divider()
        st.subheader("Ver detalle con bibliografía")
        temas_lista = [c["tema"] for c in clases_grado]
        tema_sel = st.selectbox("Seleccionar clase", temas_lista)
        clase_sel = next((c for c in clases_grado if c["tema"] == tema_sel), None)
        if clase_sel:
            render_clase_card(clase_sel)
            libros_s, revistas = sugerir_bibliografia(clase_sel["tema"])
            st.markdown("**Bibliografía sugerida completa:**")
            cols = st.columns(2)
            with cols[0]:
                st.markdown("**Libros**")
                for b in libros_s:
                    st.markdown(f"- **{b['titulo']}** — _{b['autor']}_ ({b['editorial']})")
            with cols[1]:
                st.markdown("**Revistas**")
                for r in revistas:
                    st.markdown(f"- {r['titulo']}")
    else:
        st.info("No se encontraron clases con ese criterio de búsqueda.")


# ── Rotaciones ───────────────────────────────────────────────────────────────
elif pagina == "Rotaciones":
    st.markdown('<div class="header-title">Rotaciones Mensuales</div>', unsafe_allow_html=True)
    st.divider()

    tab1, tab2, tab3 = st.tabs(["Por Residente", "Vista General", "Rotaciones Externas"])

    with tab1:
        nombres = [r["nombre"] for r in RESIDENTES]
        residente_sel = st.selectbox("Seleccionar residente", nombres)

        rot = ROTACIONES_MENSUALES.get(residente_sel, [])
        residente_data = next(r for r in RESIDENTES if r["nombre"] == residente_sel)

        st.markdown(f"**{residente_sel}** — {residente_data['grado']}")
        st.markdown("---")

        if rot:
            df_rot = pd.DataFrame({
                "Mes": MESES,
                "Rotación": rot,
            })
            df_rot["Descripción"] = df_rot["Rotación"].map(
                lambda x: ABREV_ROTACION.get(x, x)
            )

            st.dataframe(df_rot, use_container_width=True, hide_index=True)

    with tab2:
        st.markdown("**Rotaciones de todos los residentes por mes**")
        grado_filtro = st.selectbox("Filtrar por grado", ["Todos", "R1", "R2", "R3", "R4"],
                                    key="rot_grado")

        residentes_filtro = RESIDENTES if grado_filtro == "Todos" else [
            r for r in RESIDENTES if r["grado"] == grado_filtro
        ]

        data_general = {"Residente": [], "Grado": []}
        for mes in MESES:
            data_general[mes] = []

        for r in residentes_filtro:
            data_general["Residente"].append(r["nombre"])
            data_general["Grado"].append(r["grado"])
            rot_r = ROTACIONES_MENSUALES.get(r["nombre"], [""] * 12)
            for i, mes in enumerate(MESES):
                val = rot_r[i] if i < len(rot_r) else ""
                data_general[mes].append(val)

        df_general = pd.DataFrame(data_general)
        st.dataframe(df_general, use_container_width=True, hide_index=True)

    with tab3:
        st.markdown("**Rotaciones a otros hospitales**")
        df_ext = pd.DataFrame([{
            "Residente": r["residente"],
            "Grado": r["grado"],
            "Hospital": r["hospital"],
            "Servicio": r["servicio"],
            "Inicio": r["inicio"],
            "Fin": r["fin"],
        } for r in ROTACIONES_EXTERNAS])
        st.dataframe(df_ext, use_container_width=True, hide_index=True)


# ── Vacaciones ───────────────────────────────────────────────────────────────
elif pagina == "Vacaciones":
    st.markdown('<div class="header-title">Periodos Vacacionales 2026-2027</div>',
                unsafe_allow_html=True)
    st.divider()

    st.info(
        f"**Periodo vacacional Semana Santa:** "
        f"{PERIODO_VACACIONAL_SS['inicio'].strftime('%d %b')} al "
        f"{PERIODO_VACACIONAL_SS['fin'].strftime('%d %b %Y')} (todos los residentes)"
    )

    tab1, tab2 = st.tabs(["Tabla completa", "¿Quién está de vacaciones?"])

    with tab1:
        filas = []
        for r in RESIDENTES:
            for vac in r["vacaciones"]:
                filas.append({
                    "Residente": r["nombre"],
                    "Grado": r["grado"],
                    "Periodo": f"Periodo {vac['periodo']}",
                    "Inicio": vac["inicio"].strftime("%d %b %Y"),
                    "Fin": vac["fin"].strftime("%d %b %Y"),
                    "Activo ahora": "Si" if vac["inicio"] <= HOY <= vac["fin"] else "",
                })
        df_vac = pd.DataFrame(filas)
        st.dataframe(df_vac, use_container_width=True, hide_index=True)

    with tab2:
        fecha_consulta = st.date_input(
            "Consultar fecha",
            value=HOY,
            min_value=date(2026, 3, 1),
            max_value=date(2027, 2, 28),
        )
        de_vacaciones = []
        activos = []
        for r in RESIDENTES:
            en_vac, periodo = esta_de_vacaciones(r, fecha_consulta)
            if en_vac:
                de_vacaciones.append({
                    "Residente": r["nombre"],
                    "Grado": r["grado"],
                    "Periodo": f"Periodo {periodo['periodo']}",
                    "Regresa": (periodo["fin"] + timedelta(days=1)).strftime("%d %b %Y"),
                })
            else:
                activos.append(r)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**De vacaciones ({len(de_vacaciones)})**")
            if de_vacaciones:
                st.dataframe(pd.DataFrame(de_vacaciones), use_container_width=True, hide_index=True)
            else:
                st.success("Ningún residente de vacaciones ese día.")
        with col2:
            st.markdown(f"**Activos en servicio ({len(activos)})**")
            if activos:
                st.dataframe(
                    pd.DataFrame([{"Residente": a["nombre"], "Grado": a["grado"]} for a in activos]),
                    use_container_width=True, hide_index=True,
                )


# ── Bibliografía ─────────────────────────────────────────────────────────────
elif pagina == "Bibliografía":
    st.markdown('<div class="header-title">Bibliografía Quirúrgica</div>', unsafe_allow_html=True)
    st.divider()

    tab1, tab2, tab3 = st.tabs(["Buscar por tema", "Todos los libros", "Revistas"])

    with tab1:
        st.markdown("Escribe el tema de la clase para obtener bibliografía sugerida:")
        tema_input = st.text_input("Tema", placeholder="Ej: pancreatitis aguda, hernia inguinal, trauma...")

        if tema_input:
            libros_s, revistas = sugerir_bibliografia(tema_input)
            st.subheader("Libros sugeridos")
            for b in libros_s:
                st.markdown(
                    f"**{b['titulo']}**  \n"
                    f"Autor(es): *{b['autor']}*  \n"
                    f"Editorial: {b['editorial']}"
                )
                st.divider()

            st.subheader("Revistas recomendadas")
            for r in revistas:
                st.markdown(f"- {r['titulo']}")

        # También buscar la clase relacionada
        if tema_input:
            clases_rel = [c for c in CLASES if tema_input.lower() in c["tema"].lower()]
            if clases_rel:
                st.subheader("Clases relacionadas en el programa")
                for c in clases_rel[:5]:
                    st.markdown(
                        f"**{c['tema']}** — {c['grado']} — "
                        f"{c['fecha'].strftime('%d %b %Y')} — Ponente: {c['ponente']}"
                    )

    with tab2:
        busq_lib = st.text_input("Filtrar libros", placeholder="Ej: Schwartz, Cameron...")
        libros_mostrar = LIBROS
        if busq_lib:
            libros_mostrar = [b for b in LIBROS
                              if busq_lib.lower() in b["titulo"].lower()
                              or busq_lib.lower() in b["autor"].lower()]

        df_lib = pd.DataFrame([{
            "Título": b["titulo"],
            "Autor(es)": b["autor"],
            "Editorial": b["editorial"],
        } for b in libros_mostrar])
        st.dataframe(df_lib, use_container_width=True, hide_index=True)

    with tab3:
        st.markdown("**Revistas científicas recomendadas por el programa:**")
        for r in REVISTAS:
            st.markdown(f"- {r['titulo']}")
        st.divider()
        st.markdown("""
        **Bases de datos disponibles (CONRICYT):**
        - SpringerLink (550 revistas)
        - EBSCOhost (1,000 revistas)
        - ScienceDirect (2,385 revistas)
        - OVID / Lippincott (369 revistas)
        - Nature (40 revistas)
        - ProQuest (5,700 revistas)
        - Wiley InterScience (1,000 revistas)
        """)
