import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Configuração da página para tema escuro nativo do Streamlit
st.set_page_config(page_title="Formula Racing", page_icon="🏁", layout="centered")

st.html("""
<style>
    .stApp { background-color: #0b0c10 !important; color: #ffffff !important; }
    div[data-testid="stForm"] { border: 2px solid #ff1e27 !important; border-radius: 12px !important; background-color: #12131a !important; padding: 30px !important; }
    .section-title { color: #ffffff; font-weight: bold; font-size: 18px; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
    div[data-testid="stFormSubmitButton"] button { background-color: #ff1e27 !important; color: white !important; border: none !important; width: 100% !important; padding: 12px !important; font-size: 18px !important; font-weight: bold !important; border-radius: 8px !important; text-transform: uppercase; cursor: pointer; }
    .btn-whatsapp { background-color: #25d366; color: white !important; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 10px; padding: 15px; font-size: 18px; font-weight: bold; border-radius: 8px; text-transform: uppercase; margin-top: 15px; text-align: center; }
</style>
""")

st.markdown("<h2 style='text-align: center; font-weight: 900; margin-bottom: 0;'>FAÇA SUA INSCRIÇÃO</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #ff1e27; font-weight: 900; margin-top: -15px;'>E ENTRE NA PISTA!</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaaaaa;'>Preencha seus dados abaixo e junte-se à maior comunidade de F1 2013 no PS3.</p>", unsafe_allow_html=True)

with st.form("form_inscricao", clear_on_submit=False):
    st.markdown('<div class="section-title">👤 DADOS PESSOAIS</div>', unsafe_allow_html=True)
    nome = st.text_input("NOME COMPLETO", placeholder="Digite seu nome completo")
    idade = st.text_input("IDADE", placeholder="Digite sua idade")
    psn_id = st.text_input("ID DA PSN", placeholder="Digite sua ID Online da PSN")
    enviado = st.form_submit_button("Enviar Inscrição >")

if enviado:
    if not nome or not idade or not psn_id:
        st.error("Por favor, preencha todos os campos do formulário.")
    else:
        try:
            # Conexão nativa e protegida por criptografia interna do Streamlit
            conn = st.connection("gsheets", type=GSheetsConnection)
            
            try:
                df_existente = conn.read(ttl="0d")
            except Exception:
                df_existente = pd.DataFrame(columns=["Nome", "Idade", "PSN_ID"])
            
            novos_dados = pd.DataFrame([{"Nome": nome, "Idade": idade, "PSN_ID": psn_id}])
            df_atualizado = pd.concat([df_existente, novos_dados], ignore_index=True)
            
            conn.update(data=df_atualizado)
            
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #ffffff; margin-bottom: 0;'>INSCRIÇÃO REALIZADA</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #25d366; margin-top: -15px;'>COM SUCESSO!</h3>", unsafe_allow_html=True)
            link_whatsapp = "https://whatsapp.com"
            st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">💬 ENTRAR NO GRUPO DO WHATSAPP</a>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error("Erro ao salvar. Verifique as 'Secrets' no painel do Streamlit.")
            st.exception(e)

st.markdown("<br><p style='text-align: center; color: #555555; font-size: 12px;'>FORMULA RACING</p>", unsafe_allow_html=True)
