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

fig = go.Figure()

fig.add_trace(
    go.Bar(
        name="Previous",
        y=["Inflation", "Unemployment"],
        x=[3.72, 4.10],
        orientation="h"
    )
)

fig.add_trace(
    go.Bar(
        name="Target",
        y=["Inflation", "Unemployment"],
        x=[2.00, 3.50],
        orientation="h"
    )
)

fig.add_trace(
    go.Bar(
        name="Current",
        y=["Inflation", "Unemployment"],
        x=[3.70, 4.10],
        orientation="h"
    )
)

fig.update_layout(
    barmode="group",
    height=300,
    paper_bgcolor="#050505",
    plot_bgcolor="#050505",
    font=dict(color="#CCCCCC")
)

st.plotly_chart(fig, use_container_width=True)

# DIRECCIÓN GENERAL
st.subheader("GENERAL MARKET DIRECTION")

st.markdown(
    '<div class="signal">BAJISTA</div>',
    unsafe_allow_html=True
)
