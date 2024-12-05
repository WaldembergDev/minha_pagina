import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Formação e Cursos",
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

# Título principal
st.markdown("<h1 class='section-title'>Formação e Cursos</h1>", unsafe_allow_html=True)

# Formações acadêmicas
st.markdown("## 📚 Formações Acadêmicas")
with st.container():
    st.markdown(
        """
        <div class="item-container">
            <h3>Análise e Desenvolvimento de Sistemas</h3>
            <p><b>Instituição</b>: Faculdade de Educação Tecnológica do Estado do Rio de Janeiro</p>
            <p><b>Status</b>: Concluído</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="item-container">
            <h3>Inteligência Artificial e Aprendizado da Máquina</h3>
            <p><b>Instituição</b>: PUC - Minas</p>
            <p><b>Status</b>: Em andamento (Primeiro Período)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="item-container">
            <h3>Sistemas para Internet</h3>
            <p><b>Instituição</b>: Universidade Cruzeiro do Sul</p>
            <p><b>Status</b>: Em andamento (Terceiro Período)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Cursos Relevantes
st.markdown("## 🎓 Cursos Relevantes")
with st.container():
    st.markdown(
        """
        <div class="item-container">
            <h3>Python Impressionador</h3>
            <p><b>Instituição</b>: Hashtag Treinamentos</p>
            <p><b>Carga Horária</b>: 174 horas</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="item-container">
            <h3>HTML e CSS Impressionador</h3>
            <p><b>Instituição</b>: Hashtag Treinamentos</p>
            <p><b>Carga Horária</b>: 160 horas</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="item-container">
            <h3>SQL Impressionador</h3>
            <p><b>Instituição</b>: Hashtag Treinamentos</p>
            <p><b>Carga Horária</b>: 90 horas</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="item-container">
            <h3>Git - Básico ao Avançado</h3>
            <p><b>Instituição</b>: Udemy</p>
            <p><b>Carga Horária</b>: 06 horas
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="item-container">
            <h3>BPM, BPMN e Modelagem de Processos com Bizagi</h3>
            <p><b>Instituição</b>: Udemy</p>
            <p><b>Carga Horária</b>: 16 horas</p>
        </div>
        """,
        unsafe_allow_html=True
    )