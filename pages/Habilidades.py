import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Habilidades",
    page_icon="🎓",
    layout="wide",
)

# Estilização
st.markdown(
    """
    <style>
    .section-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: var(--primary-color, #4CAF50);
        margin-bottom: 1rem;
        border-bottom: 2px solid var(--primary-color, #4CAF50);
        padding-bottom: 0.5rem;
    }
    .item-container {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        color: inherit; /* Adapta as cores do texto ao tema */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título
st.markdown("""
        <h1 class='section-title'>Habilidades</h1>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

