import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Portfólio - Waldemberg Pereira",
    page_icon="📄",
    layout="wide",
)

# Cabeçalho com Foto e Título
col1, col2 = st.columns([3, 1])

with col1:
    st.title('Waldemberg Pereira')
    st.markdown('### Analista de T.I | Desenvolvedor Back End')

with col2:
    st.image('img\\minha_foto.jpeg', width=160)

st.divider()

# Sobre Mim
st.markdown('## Sobre Mim')
st.markdown("""
Sou um profissional entusiasta de tecnologia e criatividade que adota uma abordagem multidisciplinar para inovar e superar desafios complexos.

Minha jornada é caracterizada pela integração de conhecimentos técnicos com soluções criativas, sempre com um foco implacável em resultados eficazes e impactantes.

Atualmente, atuo como **Coordenador de TI** na empresa **Qualy Lab Análises Ambientais**, onde aplico minhas habilidades em:
- Desenvolvimento de automações
- Suporte técnico
- Manutenção de computadores, servidores e redes
- Instalação e manutenção de Sistemas Operacionais
""")

st.divider()

# Minhas Filosofias
st.markdown('## Minhas Filosofias')
st.markdown("""
- 🚀 **Aprendizado contínuo e adaptabilidade**
- 🤝 **Colaboração e trabalho em equipe**
- 💡 **Pensamento crítico e solução de problemas**
- 🎨 **Criatividade como diferencial competitivo**
""")

st.divider()

# Contato
st.markdown('## Contato')
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('### 📧 Email')
    st.markdown('[waldemberg.pereira@hotmail.com](mailto:waldemberg.pereirac@gmail.com)')

with col2:
    st.markdown('### 🔗 LinkedIn')
    st.markdown('[linkedin.com/in/waldemberg-pereira](https://www.linkedin.com/in/waldemberg-pereira-da-costa-leite-b09326196/)')

with col3:
    st.markdown('### 💻 GitHub')
    st.markdown('[github.com/waldemberg](https://github.com/WaldembergDev)')

with col4:
    st.markdown('### 📱 WhatsApp')
    st.markdown('[Contato no WhatsApp](https://wa.me/5521974002929)')
