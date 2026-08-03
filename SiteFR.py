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
    /* Botão Verde do WhatsApp */
    .btn-whatsapp {
        background-color: #25d366;
        color: white !important;
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        padding: 15px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        text-transform: uppercase;
        margin-top: 15px;
        text-align: center;
    }
</style>
""")

st.markdown("<h2 style='text-align: center; font-weight: 900; margin-bottom: 0;'>FAÇA SUA INSCRIÇÃO</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff1e27; font-weight: 900; margin-top: -15px;'>E ENTRE NA PISTA!</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Preencha seus dados abaixo e junte-se à maior comunidade de F1 2013 no PS3.</p>", unsafe_allow_html=True)

st.write("") # Espaçador

# Formulário de Inscrição
with st.form("form_inscricao", clear_on_submit=False):
    st.markdown('<div class="section-title">👤 DADOS PESSOAIS</div>', unsafe_allow_html=True)
    
    nome = st.text_input("NOME COMPLETO", placeholder="Digite seu nome completo")
    idade = st.text_input("IDADE", placeholder="Digite sua idade")
    psn_id = st.text_input("ID DA PSN", placeholder="Digite sua ID Online da PSN")
    
    st.write("")
    enviado = st.form_submit_button("Enviar Inscrição >")

# Ações após o envio do formulário
if enviado:
    if not nome or not idade or not psn_id:
        st.error("Por favor, preencha todos os campos do formulário.")
    else:
        st.write("") # Espaçador
        
        # Bloco de sucesso visível na tela
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #ffffff; margin-bottom: 0;'>INSCRIÇÃO REALIZADA</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #25d366; margin-top: -15px;'>COM SUCESSO!</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #aaaaaa;'>Clique no botão abaixo para enviar sua ficha e entrar no grupo.</p>", unsafe_allow_html=True)
        
        # Montagem do texto automático da mensagem
        texto_mensagem = f"Olá! Quero me inscrever no campeonato Fórmula Racing:\n\n🏁 *Ficha de Inscrição*\n👤 *Nome:* {nome}\n🎂 *Idade:* {idade}\n🎮 *ID da PSN:* {psn_id}"
        
        # Formata o texto para padrão de URL da internet
        texto_formatado = urllib.parse.quote(texto_mensagem)
        
        # ⚠️ ESCREVA SEU NÚMERO ABAIXO (Exemplo: "5521999999999")
        # Deve ter o código 55 do país + o DDD da sua cidade + o seu número
        seu_numero = "558888465510" 
        
        # Link gerado para abrir o seu chat do WhatsApp
        link_whatsapp = f"https://wa.me/{seu_numero}?text={texto_formatado}"
        
        st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">💬 ENTRAR NO GRUPO DO WHATSAPP</a>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Rodapé
st.markdown("<br><p style='text-align: center; color: #555555; font-size: 12px;'>FORMULA RACING</p>", unsafe_allow_html=True)
