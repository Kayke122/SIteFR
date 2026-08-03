import streamlit as st
import urllib.parse

# Configuração da página para tema escuro nativo do Streamlit
st.set_page_config(page_title="Formula Racing", page_icon="🏁", layout="centered")

# Estilização CSS para replicar o design da imagem
st.html("""
<style>
    /* Fundo escuro geral */
    .stApp {
        background-color: #0b0c10 !important;
        color: #ffffff !important;
    }
    /* Estilo do container do formulário */
    div[data-testid="stForm"] {
        border: 2px solid #ff1e27 !important;
        border-radius: 12px !important;
        background-color: #12131a !important;
        padding: 30px !important;
    }
    /* Título das seções dentro do formulário */
    .section-title {
        color: #ffffff;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    /* Botão Vermelho de Enviar */
    div[data-testid="stFormSubmitButton"] button {
        background-color: #ff1e27 !important;
        color: white !important;
        border: none !important;
        width: 100% !important;
        padding: 12px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        text-transform: uppercase;
        cursor: pointer;
    }
</style>
""")

# Topo do site (Logo e Chamada principal)
st.image("Fr1.png", use_container_width=True)

st.markdown("<h2 style='text-align: center; font-weight: 900; margin-bottom: 0;'>FAÇA SUA INSCRIÇÃO</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff1e27; font-weight: 900; margin-top: -15px;'>E ENTRE NA PISTA!</h2>", unsafe_allow_html=True)

# Texto explicativo atualizado informando sobre o direcionamento automático
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Preencha seus dados abaixo. Ao clicar em enviar, seu WhatsApp abrirá automaticamente para você nos mandar a ficha preenchida e confirmar sua vaga no campeonato de F1 2013 no PS3.</p>", unsafe_allow_html=True)

st.write("") # Espaçador

# Formulário de Inscrição
with st.form("form_inscricao", clear_on_submit=False):
    st.markdown('<div class="section-title">👤 DADOS PESSOAIS</div>', unsafe_allow_html=True)
    
    nome = st.text_input("NOME COMPLETO", placeholder="Digite seu nome completo")
    idade = st.text_input("IDADE", placeholder="Digite sua idade")
    psn_id = st.text_input("ID DA PSN", placeholder="Digite sua ID Online da PSN")
    
    st.write("")
    enviado = st.form_submit_button("Enviar Inscrição por WhatsApp >")

# Ações após o envio do formulário
if enviado:
    if not nome or not idade or not psn_id:
        st.error("Por favor, preencha todos os campos do formulário antes de enviar.")
    else:
        # Montagem do texto automático da mensagem
        texto_mensagem = f"Olá! Quero me inscrever no campeonato Fórmula Racing:\n\n🏁 *Ficha de Inscrição*\n👤 *Nome:* {nome}\n🎂 *Idade:* {idade}\n🎮 *ID da PSN:* {psn_id}"
        
        # Formata o texto para padrão de URL da internet
        texto_formatado = urllib.parse.quote(texto_mensagem)
        
        # ⚠️ ESCREVA SEU NÚMERO ABAIXO (Exemplo: "5521999999999")
        seu_numero = "55XXXXXXXXXXX" 
        
        # Link gerado para abrir o seu chat do WhatsApp
        link_whatsapp = f"https://wa.me{seu_numero}?text={texto_formatado}"
        
        # Avisa o usuário e executa o redirecionamento usando JavaScript básico
        st.success("Redirecionando você para o WhatsApp para confirmar a inscrição...")
        st.html(f'<script>window.open("{link_whatsapp}", "_blank");</script>')

# Rodapé
st.markdown("<br><p style='text-align: center; color: #555555; font-size: 12px;'>FORMULA RACING</p>", unsafe_allow_html=True)
