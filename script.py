
from groq import Groq
import streamlit as st
import gtts as gt
import os
import re


# =========================================================
# CONFIGURAÇÃO
# =========================================================

# Coloca a tua nova API key aqui
client = Groq(api_key="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")


# =========================================================
# MEMÓRIA
# =========================================================

if "hie" not in st.session_state:
    st.session_state.hie = []

if "hir" not in st.session_state:
    st.session_state.hir = []


# =========================================================
# CONFIGURAÇÕES DO ANDRÉ
# =========================================================

if "bot" not in st.session_state:
    st.session_state.bot = True

if "conf" not in st.session_state:
    st.session_state.conf = False

if "ln" not in st.session_state:
    st.session_state.ln = "pt"


# =========================================================
# IDIOMAS
# =========================================================

nomes_linguas = {
    "pt": "português",
    "en": "inglês",
    "es": "espanhol",
    "fr": "francês",
    "de": "alemão",
    "it": "italiano",
    "ja": "japonês",
    "ko": "coreano",
    "zh-CN": "chinês",
    "ru": "russo",
    "ar": "árabe",
    "hi": "hindi",
    "tr": "turco",
    "nl": "holandês",
    "pl": "polaco",
    "sv": "sueco",
    "da": "dinamarquês",
    "no": "norueguês",
    "fi": "finlandês",
    "cs": "checo",
    "el": "grego",
    "he": "hebraico",
    "id": "indonésio",
    "vi": "vietnamita"
}


lingua = nomes_linguas[st.session_state.ln]


# =========================================================
# BOTÕES
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✍️ Escrever"):
        st.session_state.bot = True
        st.rerun()

with col2:
    if st.button("🎤 Falar"):
        st.session_state.bot = False
        st.rerun()

with col3:
    if st.button("⚙️ Conf"):
        st.session_state.conf = not st.session_state.conf
        st.rerun()


# =========================================================
# CONFIGURAÇÕES
# =========================================================

if st.session_state.conf:

    st.sidebar.title("⚙️ Configurações")

    st.sidebar.write("Idioma:")

    for codigo, nome in nomes_linguas.items():

        if st.sidebar.button(nome.capitalize()):

            st.session_state.ln = codigo

            st.rerun()


# =========================================================
# PERSONA
# =========================================================

persona = f"""
Tu és uma IA de uso pessoal.

O teu nome é A.N.D.R.E.
Significa Assistente Neural Digital de Resposta e Execução.

Sê humano e natural.

Não expliques coisas sem necessidade.
Se a conversa for casual, conversa normalmente.

Sê direto nas respostas, mas não demasiado curto.

Tu tens um sistema para abrir aplicações e sites.
Quando o mestre pedir para abrir alguma coisa,
o código tratará disso automaticamente.
se te pedirem pra perquisar so escreve o url nada mais nem nada menos
e se tem pedirem pra abrir algo so dis que estas a abrir

Não digas que não consegues abrir sites.
Apenas responde naturalmente.

O idioma atual das respostas é:
{lingua}

Estas são algumas respostas anteriores:
{st.session_state.hie}

Estas são algumas perguntas anteriores:
{st.session_state.hir}
"""


# =========================================================
# FUNÇÃO PARA FALAR
# =========================================================

def falar(texto):

    # Remove símbolos que podem ficar estranhos no áudio
    texto_fala = re.sub(
        r'[*.,!?;:()\[\]{}"\'`]',
        '',
        texto
    )

    texto_fala = texto_fala.replace("...", "")
    texto_fala = texto_fala.replace("-", " ")
    texto_fala = texto_fala.replace("/", " ")

    audio_resposta = "resposta.mp3"

    try:
        voz = gt.gTTS(
            texto_fala,
            lang=st.session_state.ln
        )

        voz.save(audio_resposta)

        st.audio(
            audio_resposta,
            format="audio/mp3",
            autoplay=True
        )

    except Exception as erro:
        st.error(f"Erro na voz: {erro}")


# =========================================================
# FUNÇÃO PARA ABRIR SITES
# =========================================================

def app(nome, abrir, texto):

    if nome.lower() in texto.lower():

        # Só funciona para abrir no computador onde
        # o Streamlit está a executar.
        os.system(abrir)


# =========================================================
# FUNÇÃO PRINCIPAL DA IA
# =========================================================

def responder(texto):

    resposta = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "system",
                "content": persona
            },
            {
                "role": "user",
                "content": texto
            }
        ]
    )

    return resposta.choices[0].message.content


# =========================================================
# MODO ESCREVER
# =========================================================

if st.session_state.bot:

    texto = st.chat_input("Pergunta ao André...")

    if texto:

        try:

            a = responder(texto)

            st.write("Tu:", texto)

            st.write(a)

            # Memória
            st.session_state.hir.append(texto)
            st.session_state.hie.append(a)

            # Voz
            falar(a)

            # Comandos
            app(
                "abrir youtube",
                "start chrome https://www.youtube.com/",
                texto
            )

            app(
                "abrir modulador",
                "start chrome https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364",
                texto
            )

            app(
                "abrir google",
                "start chro

