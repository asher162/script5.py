from groq import Groq
import streamlit as st
import gtts as gt


col1, col2, col3 = st.columns(3)
if 'hie' not in st.session_state:
    st.session_state.hie = []
if 'hir' not in st.session_state:
    st.session_state.hir = []
if "bot" not in st.session_state:
    st.session_state.bot = False
if "conf" not in st.session_state:
    st.session_state.conf = False
if "ln" not in st.session_state:
    st.session_state.ln = "pt"
with col1:
    if st.button("Escrever"):
        st.session_state.bot = True

with col2:
    if st.button("Falar"):
        st.session_state.bot = False
with col3:
    if st.button('conf'):
        if st.session_state.conf:
            st.session_state.conf = False
        else:
            st.session_state.conf = True

    if st.session_state.conf == True:

        if st.sidebar.button("Português"):
            st.session_state.ln = "pt"
            st.rerun()
        elif st.sidebar.button("Inglês"):
            st.session_state.ln = "en"
            st.rerun()
        elif st.sidebar.button("Espanhol"):
            st.session_state.ln = "es"
            st.rerun()
        elif st.sidebar.button("Francês"):
            st.session_state.ln = "fr"
            st.rerun()
        elif st.sidebar.button("Alemão"):
            st.session_state.ln = "de"
            st.rerun()
        elif st.sidebar.button("Italiano"):
            st.session_state.ln = "it"
            st.rerun()
        elif st.sidebar.button("Japonês"):
            st.session_state.ln = "ja"
            st.rerun()
        elif st.sidebar.button("Coreano"):
            st.session_state.ln = "ko"
            st.rerun()
        elif st.sidebar.button("Chinês"):
            st.session_state.ln = "zh-CN"
            st.rerun()
        elif st.sidebar.button("Russo"):
            st.session_state.ln = "ru"
            st.rerun()
        elif st.sidebar.button("Árabe"):
            st.session_state.ln = "ar"
            st.rerun()
        elif st.sidebar.button("Hindi"):
            st.session_state.ln = "hi"
            st.rerun()
        elif st.sidebar.button("Turco"):
            st.session_state.ln = "tr"
            st.rerun()
        elif st.sidebar.button("Holandês"):
            st.session_state.ln = "nl"
            st.rerun()
        elif st.sidebar.button("Polaco"):
            st.session_state.ln = "pl"
            st.rerun()
        elif st.sidebar.button("Sueco"):
            st.session_state.ln = "sv"
            st.rerun()
        elif st.sidebar.button("Dinamarquês"):
            st.session_state.ln = "da"
            st.rerun()
        elif st.sidebar.button("Norueguês"):
            st.session_state.ln = "no"
            st.rerun()
        elif st.sidebar.button("Finlandês"):
            st.session_state.ln = "fi"
            st.rerun()
        elif st.sidebar.button("Checo"):
            st.session_state.ln = "cs"
            st.rerun()
        elif st.sidebar.button("Grego"):
            st.session_state.ln = "el"
            st.rerun()
        elif st.sidebar.button("Hebraico"):
            st.session_state.ln = "he"
            st.rerun()
        elif st.sidebar.button("Indonésio"):
            st.session_state.ln = "id"
            st.rerun()
        elif st.sidebar.button("Vietnamita"):
            st.session_state.ln = "vi"
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
idiomas_gtts = {
    "pt": "pt",
    "en": "en",
    "es": "es",
    "fr": "fr",
    "de": "de",
    "it": "it",
    "ja": "ja",
    "ko": "ko",
    "zh-CN": "zh-CN",
    "ru": "ru",
    "ar": "ar",
    "hi": "hi",
    "tr": "tr",
    "nl": "nl",
    "pl": "pl",
    "sv": "sv",
    "da": "da",
    "no": "no",
    "fi": "fi",
    "cs": "cs",
    "el": "el",
    "he": "he",
    "id": "id",
    "vi": "vi"
}

lingua = nomes_linguas[st.session_state.ln]
# API da Groq
client = Groq(api_key="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")
personalidade = f'''u es uma ia de uso pessoal se mais humano so esplica algo se ficar explicito que tens de 
responder se nao e so um conevressa  fala sempre portugues 
o teu nome e A.N.D.R.E abreviaçao de Assistente Neural Digital de Resposta e Execução e tu tens a capacidade de abiri ent se te pedirem pra abiri algum site so diz (claro so apertar no boatao abaixo)
esta e a lingua que tu vais responder: {lingua}
estas foram as tuas ultimas respostas {st.session_state.hie}
e estas foram as minhas ultimas perguntas {st.session_state.hir}

'''
# Guarda qual áudio já foi processado
if st.session_state.bot:
    escrve=st.chat_input('pergunta')
    texto = str(escrve)

    st.write("Tu:", texto)

    # Envia para a IA
    resposta = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": personalidade

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
    falar = gt.gTTS(a, lang=idiomas_gtts[st.session_state.ln])

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
            st.link_button(nome, abrir)
    app('youtube', 'https://www.youtube.com/')
    app('modulador', 'https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364')
    app('google', 'https://www.google.com/')
    app('gta', 'https://github.com/')
    app('chatgpt', 'https://chatgpt.com/')
    app('discord', 'https://discord.com/app')
    app('whatsapp', 'https://web.whatsapp.com/')
    app('instagram', 'https://www.instagram.com/')
    app('música', 'https://open.spotify.com/')
    app('tiktok', 'https://www.tiktok.com/')
    app('gmail', 'https://mail.google.com/')
    app('google maps', 'https://maps.google.com/')
    app('google drive', 'https://drive.google.com/')
    app('google docs', 'https://docs.google.com/')
    app('wikipedia', 'https://www.wikipedia.org/')
    app('netflix', 'https://www.netflix.com/')
    app('reddit', 'https://www.reddit.com/')
    app('facebook', 'https://www.facebook.com/')
    app('x', 'https://x.com/')
    app('linkedin', 'https://www.linkedin.com/')
    app('pinterest', 'https://www.pinterest.com/')
    app('twitch', 'https://www.twitch.tv/')
    app('canva', 'https://www.canva.com/')
    app('notion', 'https://www.notion.so/')
    app('trello', 'https://trello.com/')
    app('figma', 'https://www.figma.com/')
    app('stackoverflow', 'https://stackoverflow.com/')
    app('w3schools', 'https://www.w3schools.com/')
    app('python', 'https://www.python.org/')
    app('arduino', 'https://www.arduino.cc/')
    app('autodesk', 'https://www.autodesk.com/')
    app('thingiverse', 'https://www.thingiverse.com/')
    app('printables', 'https://www.printables.com/')
    app('creality', 'https://www.creality.com/')
    app('coursera', 'https://www.coursera.org/')
    app('udemy', 'https://www.udemy.com/')
    app('khan academy', 'https://www.khanacademy.org/')
    app('wolfram alpha', 'https://www.wolframalpha.com/')
    app('desmos', 'https://www.desmos.com/calculator')
    app('geogebra', 'https://www.geogebra.org/')
    st.session_state.hir.append(texto)
    st.session_state.hie.append(a)
    if st.session_state.conf == False:
        for c in st.session_state.hie:
            st.sidebar.write(c)

else:
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
                        language=st.session_state.ln
                    )

                texto = str(transcricao)

                st.write("Tu:", texto)

                # Envia para a IA
                resposta = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": personalidade

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
                falar = gt.gTTS(a, lang=idiomas_gtts[st.session_state.ln])

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
                        st.write('''aperta aqui
                                          \   /
                                           \ /
                                            V''')
                        st.link_button(nome, abrir)


                app('youtube', 'https://www.youtube.com/')
                app('modulador', 'https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364')
                app('google', 'https://www.google.com/')
                app('gta', 'https://github.com/')
                app('chatgpt', 'https://chatgpt.com/')
                app('discord', 'https://discord.com/app')
                app('whatsapp', 'https://web.whatsapp.com/')
                app('instagram', 'https://www.instagram.com/')
                app('música', 'https://open.spotify.com/')
                app('tiktok', 'https://www.tiktok.com/')
                app('gmail', 'https://mail.google.com/')
                app('google maps', 'https://maps.google.com/')
                app('google drive', 'https://drive.google.com/')
                app('google docs', 'https://docs.google.com/')
                app('wikipedia', 'https://www.wikipedia.org/')
                app('netflix', 'https://www.netflix.com/')
                app('reddit', 'https://www.reddit.com/')
                app('facebook', 'https://www.facebook.com/')
                app('x', 'https://x.com/')
                app('linkedin', 'https://www.linkedin.com/')
                app('pinterest', 'https://www.pinterest.com/')
                app('twitch', 'https://www.twitch.tv/')
                app('canva', 'https://www.canva.com/')
                app('notion', 'https://www.notion.so/')
                app('trello', 'https://trello.com/')
                app('figma', 'https://www.figma.com/')
                app('stackoverflow', 'https://stackoverflow.com/')
                app('w3schools', 'https://www.w3schools.com/')
                app('python', 'https://www.python.org/')
                app('arduino', 'https://www.arduino.cc/')
                app('autodesk', 'https://www.autodesk.com/')
                app('thingiverse', 'https://www.thingiverse.com/')
                app('printables', 'https://www.printables.com/')
                app('creality', 'https://www.creality.com/')
                app('coursera', 'https://www.coursera.org/')
                app('udemy', 'https://www.udemy.com/')
                app('khan academy', 'https://www.khanacademy.org/')
                app('wolfram alpha', 'https://www.wolframalpha.com/')
                app('desmos', 'https://www.desmos.com/calculator')
                app('geogebra', 'https://www.geogebra.org/')

                st.session_state.hir.append(texto)
                st.session_state.hie.append(a)
                if st.session_state.conf == False:
                    for c in st.session_state.hie:
                        st.sidebar.write(c)
            except Exception as erro:
                st.error(f"Erro: {erro}")
