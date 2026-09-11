import streamlit as st
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

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
            y=[3.80, 3.75, 3.82, 3.78, 3.72, 3.70],
            mode="lines+markers",
            name="PCE"
        )
    )

    fig.add_hline(
        y=2.0,
        line_dash="dash",
        annotation_text="TARGET 2%"
    )

    fig.update_layout(
        height=350,
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font=dict(color="#CCCCCC")
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("MERCADO LABORAL — DESEMPLEO")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
            y=[3.90, 4.00, 4.00, 4.10, 4.10, 4.10],
            mode="lines+markers",
            name="Desempleo"
        )
    )

    fig.add_hline(
        y=3.5,
        line_dash="dash",
        annotation_text="TARGET 3.5%"
    )

    fig.update_layout(
        height=350,
        paper_bgcolor="#050505",
        plot_bgcolor="#050505",
        font=dict(color="#CCCCCC")
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# MATRIZ MACRO
st.subheader("MACRO REGIME MATRIX")

def macro_row(nombre, anterior, objetivo, actual, unidad):
    maximo = max(anterior, actual, objetivo if objetivo else 0) * 1.25
    anterior_pct = anterior / maximo * 100
    actual_pct = actual / maximo * 100

    if objetivo is not None:
        objetivo_pct = objetivo / maximo * 100
        objetivo_html = f'<div style="position:absolute;left:{objetivo_pct}%;top:0;bottom:0;width:2px;background:#FFFFFF;"></div>'
    else:
        objetivo_html = ""

    return f"""<div style="margin-bottom:28px;">
<div style="display:flex;justify-content:space-between;margin-bottom:7px;color:#D4AF37;font-size:13px;font-weight:bold;">
<span>{nombre}</span>
<span>ANTERIOR: {anterior:,.2f}{unidad} &nbsp;&nbsp;|&nbsp;&nbsp; ACTUAL: {actual:,.2f}{unidad}</span>
</div>
<div style="position:relative;height:30px;background:#111111;border:1px solid #3A3218;border-radius:4px;">
{objetivo_html}
<div style="position:absolute;left:0;top:6px;height:18px;width:{anterior_pct}%;background:#6B5A20;"></div>
<div style="position:absolute;left:0;top:10px;height:10px;width:{actual_pct}%;background:#D4AF37;"></div>
</div>
<div style="display:flex;justify-content:space-between;margin-top:6px;color:#777777;font-size:10px;">
<span>ANTERIOR</span>
<span>{"OBJETIVO: " + f"{objetivo:,.2f}{unidad}" if objetivo is not None else "SIN OBJETIVO"}</span>
<span>ACTUAL</span>
</div>
</div>"""


st.markdown(
    macro_row("INFLACIÓN — PCE", 3.72, 2.00, 3.70, "%"),
    unsafe_allow_html=True
)

st.markdown(
    macro_row("DESEMPLEO", 4.10, 3.50, 4.10, "%"),
    unsafe_allow_html=True
)

st.markdown(
    macro_row("JOLTS", 7182, None, 7271, ""),
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        margin-top:15px;
        padding:12px;
        border-top:1px solid #29251A;
        color:#888888;
        font-size:11px;
    ">
        <span style="color:#6B5A20;">■</span> ANTERIOR
        &nbsp;&nbsp;&nbsp;
        <span style="color:#D4AF37;">■</span> ACTUAL
        &nbsp;&nbsp;&nbsp;
        <span style="color:#FFFFFF;">│</span> OBJETIVO
    </div>
    """,
    unsafe_allow_html=True
)

# DIRECCIÓN GENERAL
st.subheader("GENERAL MARKET DIRECTION")

direction_html = """<div style="display:flex;align-items:center;justify-content:center;gap:8px;margin-top:10px;margin-bottom:20px;">
<div style="width:30%;padding:18px;text-align:center;border:1px solid #332A10;color:#555555;background:#090909;border-radius:6px;font-weight:bold;">VENTA</div>
<div style="width:30%;padding:18px;text-align:center;border:1px solid #D4AF37;color:#D4AF37;background:#171306;border-radius:6px;font-weight:bold;box-shadow:0 0 15px rgba(212,175,55,0.15);">BAJISTA</div>
<div style="width:30%;padding:18px;text-align:center;border:1px solid #332A10;color:#555555;background:#090909;border-radius:6px;font-weight:bold;">COMPRA</div>
</div>"""

st.markdown(direction_html, unsafe_allow_html=True)

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
