import streamlit as st
import pandas as pd
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR4iwwc3_e5rGouLoaaM_Ft2H7xPsoZg_HfWy65JkC3EwUWm-QgQ9j2dQLwYXtIJ5uaGJskGzVNN14N/pub?gid=1273191418&single=true&output=csv"
HISTORY_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR4iwwc3_e5rGouLoaaM_Ft2H7xPsoZg_HfWy65JkC3EwUWm-QgQ9j2dQLwYXtIJ5uaGJskGzVNN14N/pub?gid=1954464051&single=true&output=csv"

macro_data = pd.read_csv(CSV_URL)
history_data = pd.read_csv(HISTORY_CSV_URL)

history_data.columns = history_data.columns.str.strip()

# Mantener solamente los registros históricos.
# La fila actual de Hoja 2 tiene release_signature y no debe
# formar parte de las series históricas.
if "release_signature" in history_data.columns:
    history_data = history_data[
        history_data["release_signature"].isna()
    ].copy()

# Convertir fechas de forma robusta.
history_data["fecha_procesamiento"] = pd.to_datetime(
    history_data["fecha_procesamiento"].astype(str),
    format="mixed",
    errors="coerce"
)

# Convertir números que pueden venir como "2,88" desde Google Sheets.
history_data["pce_actual"] = pd.to_numeric(
    history_data["pce_actual"]
    .astype(str)
    .str.replace(",", ".", regex=False),
    errors="coerce"
)

history_data["desempleo_actual"] = pd.to_numeric(
    history_data["desempleo_actual"]
    .astype(str)
    .str.replace(",", ".", regex=False),
    errors="coerce"
)

history_data["jolts_actual"] = pd.to_numeric(
    history_data["jolts_actual"]
    .astype(str)
    .str.replace(",", "", regex=False),
    errors="coerce"
)

# Una sola fila por fecha, combinando PCE + desempleo + JOLTS.
history_data = (
    history_data
    .groupby("fecha_procesamiento", as_index=False)
    .agg({
        "pce_actual": "first",
        "desempleo_actual": "first",
        "jolts_actual": "first"
    })
    .sort_values("fecha_procesamiento")
    .reset_index(drop=True)
)

macro_data.columns = macro_data.columns.str.strip()

current = macro_data.iloc[0]

pce_actual = float(current["pce_actual"])
desempleo_actual = float(current["desempleo_actual"])
jolts_actual = int(current["jolts_actual"])
direccion_general = str(current["direccion_general"])

pce_actual = float(current["pce_actual"])
desempleo_actual = float(current["desempleo_actual"])
jolts_actual = int(current["jolts_actual"])
direccion_general = str(current["direccion_general"])


import plotly.graph_objects as go

st.set_page_config(
    page_title="Aurum Capital Macro",
    page_icon="📊",
    layout="wide"
)

# ESTILO
st.markdown("""
<style>
.stApp {
    background-color: #050505;
    color: #E8E8E8;
}

h1, h2, h3 {
    color: #D4AF37 !important;
}

.metric-card {
    background-color: #0D0D0D;
    border: 1px solid #3A3218;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
}

.metric-title {
    color: #888888;
    font-size: 12px;
    letter-spacing: 2px;
}

.metric-value {
    color: #D4AF37;
    font-size: 28px;
    font-weight: bold;
}

.signal {
    background-color: #0D0D0D;
    border: 1px solid #D4AF37;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    color: #D4AF37;
    font-size: 30px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ENCABEZADO
st.title("AURUM CAPITAL — MACRO INTELLIGENCE")
st.caption("JARVIS MACROECONOMIC COMMAND CENTER")

# MÉTRICAS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">PCE ACTUAL</div>
        <div class="metric-value">3.70%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">DESEMPLEO</div>
        <div class="metric-value">4.10%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">JOLTS</div>
        <div class="metric-value">7,271</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">MACRO BIAS</div>
        <div class="metric-value">BAJISTA</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# GRÁFICOS
left, right = st.columns(2)

with left:
    st.subheader("INFLACIÓN — PCE")

    pce_history = history_data.dropna(
        subset=["pce_actual"]
    ).copy()

    pce_history = pce_history.sort_values(
        "fecha_procesamiento"
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=pce_history["fecha_procesamiento"],
            y=pce_history["pce_actual"],
            mode="lines+markers+text",
            text=[
                f"{valor:.2f}%"
                for valor in pce_history["pce_actual"]
            ],
            textposition="top center",
            marker=dict(size=9),
            line=dict(width=3),
            name="PCE"
        )
    )

    fig.add_hline(
        y=float(
            str(current["pce_meta"]).replace("%", "")
        ),
        line_dash="dash",
        line_width=2,
        annotation_text=f"TARGET {current['pce_meta']}",
        annotation_position="bottom right"
    )

    fig.update_layout(
        height=350,
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font=dict(color="#CCCCCC"),
        yaxis=dict(
            title="PCE (%)",
            gridcolor="#292929"
        ),
        xaxis=dict(
            title="Fecha",
            gridcolor="#171717",
            tickformat="%b %Y"
        ),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:
    st.subheader("MERCADO LABORAL — DESEMPLEO")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=history_data["fecha_procesamiento"],
            y=history_data["desempleo_actual"],
            mode="lines+markers+text",
            text=[
                f"{valor:.2f}%"
                for valor in history_data["desempleo_actual"]
            ],
            textposition="top center",
            marker=dict(size=9),
            line=dict(width=3),
            name="Desempleo"
        )
    )

    fig.add_hline(
        y=float(str(current["desempleo_objetivo"]).replace("%", "")),
        line_dash="dash",
        line_width=2,
        annotation_text=f"TARGET {current['desempleo_objetivo']}",
        annotation_position="bottom right"
    )

    fig.update_layout(
        height=350,
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font=dict(color="#CCCCCC"),
        yaxis=dict(
            title="Desempleo (%)",
            gridcolor="#292929"
        ),
        xaxis=dict(
            title="Fecha",
            gridcolor="#171717"
        ),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()
# JOLTS — HISTÓRICO
st.subheader("OFERTAS DE EMPLEO — JOLTS")

jolts_history = history_data.dropna(
    subset=["jolts_actual"]
).copy()

jolts_history["jolts_actual"] = pd.to_numeric(
    jolts_history["jolts_actual"],
    errors="coerce"
)

jolts_history = jolts_history.dropna(
    subset=["jolts_actual"]
).sort_values("fecha_procesamiento")

fig_jolts = go.Figure()

fig_jolts.add_trace(
    go.Bar(
        x=jolts_history["fecha_procesamiento"],
        y=jolts_history["jolts_actual"],
        text=[
            f"{valor:,.0f}"
            for valor in jolts_history["jolts_actual"]
        ],
        textposition="outside",
        name="JOLTS"
    )
)

fig_jolts.update_layout(
    height=360,
    paper_bgcolor="#050505",
    plot_bgcolor="#050505",
    font=dict(color="#CCCCCC"),
    yaxis=dict(
        title="Ofertas de empleo",
        gridcolor="#292929",
        tickformat=","
    ),
    xaxis=dict(
        title="Fecha",
        gridcolor="#171717",
        tickformat="%b %Y"
    ),
    showlegend=False,
    margin=dict(
        l=60,
        r=30,
        t=30,
        b=60
    )
)

st.plotly_chart(
    fig_jolts,
    use_container_width=True
)

st.divider()
# MATRIZ MACRO
st.subheader("MACRO REGIME MATRIX")


def macro_status(anterior, actual):
    if actual > anterior:
        return "SUBIENDO", "🟢"
    elif actual < anterior:
        return "BAJANDO", "🔴"
    else:
        return "ESTABLE", "⚪"


def mostrar_macro(nombre, anterior, actual, objetivo=None, unidad="%", decimales=2):
    estado, indicador = macro_status(anterior, actual)

    if decimales == 0:
        anterior_txt = f"{anterior:,.0f}{unidad}"
        actual_txt = f"{actual:,.0f}{unidad}"
        objetivo_txt = (
            f"{objetivo:,.0f}{unidad}"
            if objetivo is not None
            else "SIN OBJETIVO"
        )
    else:
        anterior_txt = f"{anterior:,.{decimales}f}{unidad}"
        actual_txt = f"{actual:,.{decimales}f}{unidad}"
        objetivo_txt = (
            f"{objetivo:,.{decimales}f}{unidad}"
            if objetivo is not None
            else "SIN OBJETIVO"
        )

    col1, col2, col3, col4 = st.columns([2.4, 1.2, 1.2, 1.4])

    with col1:
        st.markdown(f"**{nombre}**")

    with col2:
        st.caption("ANTERIOR")
        st.markdown(f"### {anterior_txt}")

    with col3:
        st.caption("ACTUAL")
        st.markdown(f"### {actual_txt}")

    with col4:
        st.caption("ESTADO")
        st.markdown(f"### {indicador} {estado}")

    if objetivo is not None:
        st.caption(f"OBJETIVO: {objetivo_txt}")
    else:
        st.caption("SIN OBJETIVO")

    st.divider()


mostrar_macro(
    "INFLACIÓN — PCE",
    float(current["pce_anterior"]),
    pce_actual,
    float(str(current["pce_meta"]).replace("%", "")),
    "%",
    2
)


mostrar_macro(
    "DESEMPLEO",
    float(current["desempleo_anterior"]),
    desempleo_actual,
    float(str(current["desempleo_objetivo"]).replace("%", "")),
    "%",
    2
)


mostrar_macro(
    "JOLTS",
    int(current["jolts_anterior"]),
    jolts_actual,
    None,
    "",
    0
)


st.caption(
    "🟢 SUBIENDO    🔴 BAJANDO    ⚪ ESTABLE    |    "
    "ACTUAL = dorado    |    OBJETIVO = referencia"
)
    

# INDICADORES MACRO
st.subheader("INDICADORES MACRO")


def macro_signal(anterior, actual):
    delta = actual - anterior

    if delta > 0:
        return "↑ SUBIENDO", "#2ECC71", delta
    elif delta < 0:
        return "↓ BAJANDO", "#E05A5A", delta
    else:
        return "→ ESTABLE", "#A7ADB7", 0


pce_estado, pce_color, pce_delta = macro_signal(
    float(current["pce_anterior"]),
    pce_actual
)

desempleo_estado, desempleo_color, desempleo_delta = macro_signal(
    float(current["desempleo_anterior"]),
    desempleo_actual
)

jolts_estado, jolts_color, jolts_delta = macro_signal(
    int(current["jolts_anterior"]),
    jolts_actual
)


def signal_card(
    nombre,
    estado,
    color,
    delta,
    unidad,
    decimales=2
):
    if decimales == 0:
        delta_txt = f"{delta:+,.0f}{unidad}"
    else:
        delta_txt = f"{delta:+,.2f}{unidad}"

    return (
        f'<div style="'
        f'flex:1;'
        f'padding:18px;'
        f'background:#080808;'
        f'border:1px solid #292929;'
        f'border-radius:8px;'
        f'text-align:center;">'

        f'<div style="'
        f'color:#8A8F98;'
        f'font-size:10px;'
        f'letter-spacing:1px;'
        f'margin-bottom:8px;">'
        f'{nombre}'
        f'</div>'

        f'<div style="'
        f'color:{color};'
        f'font-size:15px;'
        f'font-weight:bold;'
        f'margin-bottom:8px;">'
        f'{estado}'
        f'</div>'

        f'<div style="'
        f'color:#D4AF37;'
        f'font-size:13px;'
        f'font-weight:bold;">'
        f'{delta_txt}'
        f'</div>'

        f'</div>'
    )


macro_signals_html = (
    '<div style="'
    'display:flex;'
    'gap:12px;'
    'margin-top:10px;'
    'margin-bottom:20px;">'

    + signal_card(
        "PCE",
        pce_estado,
        pce_color,
        pce_delta,
        " pp",
        2
    )

    + signal_card(
        "DESEMPLEO",
        desempleo_estado,
        desempleo_color,
        desempleo_delta,
        " pp",
        2
    )

    + signal_card(
        "JOLTS",
        jolts_estado,
        jolts_color,
        jolts_delta,
        "",
        0
    )

    + '</div>'
)


st.markdown(
    macro_signals_html,
    unsafe_allow_html=True
)

# ACTIVOS
st.subheader("ASSET SIGNALS")

assets = ["GOLD", "SILVER", "NQ100", "US30", "BTC"]

cols = st.columns(5)

for col, asset in zip(cols, assets):
    with col:
        asset_html = f"""<div style="background:#090909;border:1px solid #332A10;border-radius:8px;padding:16px 8px;text-align:center;">
<div style="color:#D4AF37;font-size:12px;letter-spacing:2px;font-weight:bold;margin-bottom:14px;">{asset}</div>
<div style="display:flex;gap:4px;justify-content:center;">
<div style="flex:1;padding:8px 2px;border:1px solid #222222;color:#555555;font-size:9px;">VENTA</div>
<div style="flex:1;padding:8px 2px;border:1px solid #222222;color:#555555;font-size:9px;">NEUTRAL</div>
<div style="flex:1;padding:8px 2px;border:1px solid #D4AF37;color:#D4AF37;background:#171306;font-size:9px;font-weight:bold;box-shadow:0 0 10px rgba(212,175,55,0.12);">COMPRA</div>
</div>
</div>"""
        st.markdown(asset_html, unsafe_allow_html=True)

# JUSTIFICACIÓN TÉCNICA
st.subheader("TECHNICAL JUSTIFICATION")

st.info(current["justificacion_tecnica"])
