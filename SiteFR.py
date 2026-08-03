import streamlit as st
import pandas as pd
import gspread
import json

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
            # Colamos o texto bruto do arquivo JSON original diretamente aqui para evitar quebras do interpretador TOML
            json_bruto = "type": "service_account",
  "project_id": "ultra-surfer-504400-e7",
  "private_key_id": "c5d4ad9ec3b7da2cf773dcb4032d87db3f09388f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDd7627BXVl/Lnd\nC+35nXc9+nhJlRoQoYC07pobUeOZ8RXO8j8PYnzPI7Tw/xioS7s2z+G8+zqCZVSl\nRkgG0f0GKgsm8zSYqAC4h6V+v9WET7YfTRWFmo4ikUPvO15GPqgjthR19y7n8/sU\ncII+a103tgoC2Ff/NtSthsqzS1i9Evf5NbJUhiQjUhW45a8c6PtIKd+h2NiLMBpr\nK4IlkM2euof6+4Lxx2M8oT6tp4fgSRqVTt1gCoiQuEdN2jWqWnJTMOlZ7B0M8/DI\nYUJmZLyXDFbcYbZ6kXtblBlcD1gx5IfvVGVvm3NlWbSjKbF0nPdwVQQzyqOc/+xZ\nDaL5NwPTAgMBAAECggEAG/eAgoFBFn1+5GqE7gAYTyCZeNhHpRHc+K/ajpfGoRb+\nwwnGxYcJKEcdHYNf1ZFZgaI3lYtpB5aCUKNnHyjmBBlXN2zNU3FUSeyZ/7tnyhkL\nX61kiWX9BEEe+O4Xxq1NndZrhKQF7qfRm3VEDF6WLBeN8mbVy+zaZxWFxIs5nvWh\nWY48qDvqyysq7XO4TOgZSNVKad9aPWN+AYZsbRx+B91lxu09JPPKZsi7J11Bb0Fq\npH1EGeAPj5Fewj0TiAd5ojec8V5lUdE2jibloOC0uocGYHXVNdCzhrAUimiQxnhF\nydDQT96btKyHz2YXetKfYcJqeoiWQ4MJPGMsKCetrQKBgQD3Ut1s3JrbOsIBEw/2\nNlW6rRIGB9AoU5RwoyPpWAOex6bDJFZyNsH+Efx//zHLRcMA5AMwMYFbW+XSgmjT\nwQrHAwyS14zEa63MhpFz8n7j62Q6uuWNRzr6GMQafZlfkZDwvbK+57m7iidgDcT9\nQA7Jj60X43piHUJjV7hGNQXkRwKBgQDluNEwe8K1Azj83ks2uBil3TXZSWIpYeH0\njIPXAAT0zNWg1tx8/IXLgV9zLpguoXjaClNkbJrk5g6xAXJ5e3vaMS6zsN//xD03\n0jwPPwz+dz7/VXJ/6fO30lDtG3ZaXO9BornPTa9MCQE+t2bQydcgpRlOyBbSeau/\n+7HQSYFmFQKBgQDJAvdmMBJIVgQxvV1+vgCFXX7FmfoLnIqL1XwtfdRLa3dVKSZ9\nY5Xdup6fJTlCPevUwHz64XGCYDl1E3rBiCcLQqYofroxNlcmYMS9GP0an0lyFk7V\nuWvsss5HvYc3Tmcf0v4A/PNOwmVoQyi0sCiUl4qWXNMuBRvdBAGIRjYIpwKBgQCM\nH/g6QsO59oVEebQXZKRkSFMYf5LI+1QA/9VLyE89o9SLj4RfGQnj4L6AW+OoTgaR\nucq0byrshQhhICjbwV8C8Q0zvqhkMyfEbREFm8gpUEO1LEHzlJl9f2StvRqsdBPd\nTY1ZzmEnWDbSMr0cjoIS/6I4VATXzi/do4ILM0sjIQKBgQCHVJW5xzVabJ4U+9Jd\n43lGfYMy1eHRMH5dORt24Jl0+k/ri0zfX6O/WZwOx/JD3q7IQh//r8ONr5ysMMai\nk7JKSlllnxKZvwddxM8vpTb2lUZxBv8iPwQMi23OQrqa/BWPNVkVvjWPqVSoPANV\np/IZGPl+wdzttEzxiZbOac2Bgw==\n-----END PRIVATE KEY-----\n",
  "client_email": "streamlit-sheets@ultra-surfer-504400-e7.iam.gserviceaccount.com",
  "client_id": "109196170715064699897",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/streamlit-sheets%40ultra-surfer-504400-e7.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
  

'
            
            dados_autenticacao = json.loads(json_bruto)
            
            # Inicializa o gspread autenticando com o dicionário limpo
            gc = gspread.service_account_from_dict(dados_autenticacao)
            
            # Abre a planilha pelo ID único contido na sua URL
            id_planilha = "11WQ4_Q4KUIjrQgkVWlC2V2DjkBk6x0V4-wdfogifU-g"
            planilha = gc.open_by_key(id_planilha)
            aba = planilha.get_worksheet(0) # Pega a primeira aba da planilha
            
            # Adiciona uma nova linha com os registros diretamente no final da planilha
            aba.append_row([nome, idade, psn_id])
            
            st.write("") # Espaçador
            
            # Bloco de sucesso
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #ffffff; margin-bottom: 0;'>INSCRIÇÃO REALIZADA</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #25d366; margin-top: -15px;'>COM SUCESSO!</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color: #aaaaaa;'>Clique no botão abaixo para entrar no grupo oficial da Formula Racing.</p>", unsafe_allow_html=True)
            
            # Link para o grupo do WhatsApp
            link_whatsapp = "https://whatsapp.com"
            
            st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">💬 ENTRAR NO GRUPO DO WHATSAPP</a>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error("Ocorreu um erro ao salvar na planilha. Verifique se colou as credenciais JSON corretamente no código.")
            st.exception(e)

# Rodapé simples
st.markdown("<br><p style='text-align: center; color: #555555; font-size: 12px;'>FORMULA RACING</p>", unsafe_allow_html=True)
