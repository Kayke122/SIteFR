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
    psn_id = st.text_input("ID DA PSN", placeholder="Digite sua ID Online da PSN")
    enviado = st.form_submit_button("Enviar Inscrição >")

# Ações após o envio do formulário
if enviado:
    if not nome or not idade or not psn_id:
        st.error("Por favor, preencha todos os campos do formulário.")
    else:
        try:
            # COLE AQUI APENAS O TEXTO DA SUA NOVA PRIVATE KEY COM \n DO ARQUIVO JSON NOVO DENTRO DAS ASPAS TRIPLAS
            nova_chave_privada = """-----BEGIN PRIVATE KEY-----\nSUA_NOVA_CHAVE_AQUI\n-----END PRIVATE KEY-----\n"""
            
            # Limpa qualquer quebra de linha física gerada pelo recuo automático do editor do GitHub
            pk_limpa = nova_chave_privada.strip().replace("\n", "").replace("\\n", "\n")
            
            # Monta o dicionário estruturado puxando as variáveis limpas das Secrets individuais
            dados_autenticacao = {
                "type": "service_account",
                "project_id": st.secrets["GOOGLE_PROJECT_ID"],
                "private_key": pk_limpa,
                "client_email": st.secrets["GOOGLE_CLIENT_EMAIL"],
                "auth_uri": "https://google.com",
                "token_uri": "https://googleapis.com",
                "auth_provider_x509_cert_url": "https://googleapis.com",
                "client_x509_cert_url": f"https://googleapis.com{st.secrets['GOOGLE_CLIENT_EMAIL'].replace('@', '%40')}",
                "universe_domain": "googleapis.com"
            }
            
            # Inicializa o gspread autenticando diretamente com as credenciais estruturadas na memória do Python
            gc = gspread.service_account_from_dict(dados_autenticacao)
            
            # Abre a planilha pelo ID único contido na sua URL das Secrets
            url_planilha = st.secrets["SPREADSHEET_URL"]
            id_planilha = "11WQ4_Q4KUIjrQgkVWlC2V2DjkBk6x0V4-wdfogifU-g"
            planilha = gc.open_by_key(id_planilha)
            aba = planilha.get_worksheet(0)
            
            # Adiciona a nova linha com as colunas na planilha
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
            st.error("Ocorreu um erro ao salvar na planilha. Verifique se configurou os segredos e colou a chave corretamente.")
            st.exception(e)

# Rodapé simples
st.markdown("<br><p style='text-align: center; color: #555555; font-size: 12px;'>FORMULA RACING</p>", unsafe_allow_html=True)
