import streamlit as st
import pandas as pd
import gspread

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

# Topo do site (Logo e Chamada principal)
st.markdown("<h2 style='text-align: center; font-weight: 900; margin-bottom: 0;'>FAÇA SUA INSCRIÇÃO</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff1e27; font-weight: 900; margin-top: -15px;'>E ENTRE NA PISTA!</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Preencha seus dados abaixo e junte-se à maior comunidade de F1 2013 no PS3.</p>", unsafe_allow_html=True)

st.write("") # Espaçador

# Formulário de Inscrição
with st.form("form_inscricao", clear_on_submit=False):
    st.markdown('<div class="section-title">👤 DADOS PESSOAIS</div>', unsafe_allow_html=True)
    
    nome = st.text_input("NOME COMPLETO", placeholder="Digite seu nome completo")
    
    idade = st.text_input("IDADE", placeholder="Digite sua idade")
    
    # NOVO CAMPO: ID da PSN
    psn_id = st.text_input("ID DA PSN", placeholder="Digite sua ID Online da PSN")
    
    st.write("")
    enviado = st.form_submit_button("Enviar Inscrição >")

# Ações após o envio do formulário
if enviado:
    if not nome or not idade or not psn_id:
        st.error("Por favor, preencha todos os campos do formulário.")
    else:
        try:
            # 1. Carrega as credenciais convertendo nativamente a tabela TOML para dicionário Python
            dados_autenticacao = st.secrets["gspread_creds"].to_dict()
            
            # Adiciona os endpoints obrigatórios automaticamente em tempo de execução
            dados_autenticacao["auth_uri"] = "https://google.com"
            dados_autenticacao["token_uri"] = "https://googleapis.com"
            dados_autenticacao["auth_provider_x509_cert_url"] = "https://googleapis.com"
            dados_autenticacao["universe_domain"] = "googleapis.com"
            
            if "client_email" in dados_autenticacao:
                email_limpo = dados_autenticacao["client_email"].replace("@", "%40")
                dados_autenticacao["client_x509_cert_url"] = f"https://googleapis.com{email_limpo}"
            
            # 2. Inicializa o gspread autenticando diretamente com as credenciais nativas estruturadas
            gc = gspread.service_account_from_dict(dados_autenticacao)
            
            # 3. Abre a planilha pelo ID único contido na sua URL
            id_planilha = "11WQ4_Q4KUIjrQgkVWlC2V2DjkBk6x0V4-wdfogifU-g"
            planilha = gc.open_by_key(id_planilha)
            aba = planilha.get_worksheet(0)
            
            # 4. Adiciona a nova linha com as colunas na planilha
            aba.append_row([nome, idade, psn_id])
            
            st.write("") # Espaçador
            
            # Bloco de sucesso
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #ffffff; margin-bottom: 0;'>INSCRIÇÃO REALIZADA</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #25d366; margin-top: -15px;'>COM SUCESSO!</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color: #aaaaaa;'>Clique no botão abaixo para entrar no grupo oficial da Formula Racing.</p>", unsafe_allow_html=True)
            
            link_whatsapp = "https://whatsapp.com"
            st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">💬 ENTRAR NO GRUPO DO WHATSAPP</a>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error("Ocorreu um erro ao salvar na planilha. Verifique se configurou os segredos corretamente.")
            st.exception(e)

# Rodapé simples
st.markdown("<br><p style='text-align: center; color: #555555; font-size: 12px;'>FORMULA RACING</p>", unsafe_allow_html=True)
