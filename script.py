from groq import Groq
import streamlit as st
import gtts as gt
import os

# API da Groq
client = Groq(api_key="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")

# Guarda qual áudio já foi processado
if "audio_processado" not in st.session_state:
    st.session_state.audio_processado = None

# Microfone
audio = st.audio_input("🎤 Fala com o André")

if audio is not None:

    # Cria um ID único para esta gravação
    audio_id = hash(audio.getvalue())

    # Só processa se for uma gravação nova
    if audio_id != st.session_state.audio_processado:

        # Marca como processado
        st.session_state.audio_processado = audio_id

        try:
            # Guarda o áudio
            with open("audio.wav", "wb") as f:
                f.write(audio.getvalue())

            # Transforma voz em texto
            with open("audio.wav", "rb") as arquivo:
                transcricao = client.audio.transcriptions.create(
                    file=("audio.wav", arquivo.read()),
                    model="whisper-large-v3-turbo",
                    response_format="text",
                    language="pt"
                )

            texto = str(transcricao)

            st.write("Tu:", texto)

            # Envia para a IA
            resposta = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": """tu es uma ia de uso pessoal se mais humano
                        so esplica algo se ficar explicito que tens de responder se nao e so um conevressa inpireta no jarvis do homeme de ferro
                        fala sempre portugues
                        """
                    },
                    {
                        "role": "user",
                        "content": texto
                    }
                ]
            )

            # Resposta da IA
            a = resposta.choices[0].message.content

            st.write(a)

            # Faz o André falar
            falar = gt.gTTS(a, lang="pt-BR")

            audio_resposta = "resposta.mp3"
            falar.save(audio_resposta)

            st.audio(
                audio_resposta,
                format="audio/mp3",
                autoplay=True
            )

            # Comandos
            def app(nome, abrir):
                if nome.lower() in texto.lower():
                    os.system(abrir)

            app(
                "youtube",
                "start chrome https://www.youtube.com/"
            )

            app(
                "modulador",
                "start chrome https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364"
            )

        except Exception as erro:
            st.error(f"Erro: {erro}")
