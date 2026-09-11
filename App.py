import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Aurum Capital Macro",
    page_icon="📊",
    layout="wide"
)

# =========================
# ESTILO
# =========================
st.markdown("""
<style>
    .stApp {
        background: #05070D;
        color: #F5F1E8;
    }

    .main-title {
        font-size: 32px;
        font-weight: 700;
        letter-spacing: 3px;
        color: #D4AF37;
        margin-bottom: 0;
    }

    .subtitle {
        color: #8E8E8E;
        font-size: 13px;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

    .card {
        background: #0B0E15;
        border: 1px solid #29251A;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .metric-label {
        color: #888888;
        font-size: 12px;
        letter-spacing: 2px;
    }

    .metric-value {
        color: #D4AF37;
        font-size: 30px;
        font-weight: 700;
    }

    .signal {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        color: #D4AF37;
        letter-spacing: 4px;
        padding: 10px;
    }

    .justification {
        color: #C7C7C7;
        line-height: 1.7;
        font-size: 14px;
        border-left: 2px solid #D4AF37;
        padding-left: 15px;
    }

    h2, h3 {
        color: #D4AF37 !important;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# ENCABEZADO
# =========================
st.markdown(
    '<div class="main-title">AURUM CAPITAL — MACRO INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">JARVIS MACROECONOMIC COMMAND CENTER</div>',
    unsafe_allow_html=True
)

# =========================
# MÉTRICAS
# =========================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        '<div class="card"><div class="metric-label">PCE ACTUAL</div>'
        '<div class="metric-value">3.70%</div></div>',
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="card"><div class="metric-label">DESEMPLEO</div>'
        '<div class="metric-value">4.10%</div></div>',
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        '<div class="card"><div class="metric-label">JOLTS</div>'
        '<div class="metric-value">7,271</div></div>',
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        '<div class="card"><div class="metric-label">MACRO BIAS</div>'
        '<div class="metric-value">BAJISTA</div></div>',
        unsafe_allow_html=True
    )

# =========================
# GRÁFICOS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### INFLACIÓN — PCE")

    fig_pce = go.Figure()

    fig_pce.add_trace(
        go.Scatter(
            x=["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
            y=[3.8, 3.75, 3.82, 3.78, 3.72, 3.70],
            mode="lines+markers",
            name="PCE"
        )
    )

    fig_pce.add_hline(
        y=2.0,
        line_dash="dash",
        annotation_text="TARGET 2%"
    )

    fig_pce.update_layout(
        height=350,
        paper_bgcolor="#05070D",
        plot_bgcolor="#05070D",
        font=dict(color="#BBBBBB"),
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="#202020")
    )

    st.plotly_chart(fig_pce, use_container_width=True)

with col2:
    st.markdown("### MERCADO LABORAL — DESEMPLEO")

    fig_unemployment = go.Figure()

    fig_unemployment.add_trace(
        go.Scatter(
            x=["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
            y=[3.9, 4.0, 4.0, 4.1, 4.1, 4.1],
            mode="lines+markers",
            name="Unemployment"
        )
    )

    fig_unemployment.add_hline(
        y=3.5,
        line_dash="dash",
        annotation_text="TARGET 3.5%"
    )

    fig_unemployment.update_layout(
        height=350,
        paper_bgcolor="#05070D",
        plot_bgcolor
