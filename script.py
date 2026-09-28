from groq import Groq
import streamlit as st
import gtts as gt
def apps(nomes, links):
    st.sidebar.link_button(nomes, links)
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
            st.rerun()
        apps('youtube', 'https://www.youtube.com/')
        apps('modulador',
             'https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364')
        apps('google', 'https://www.google.com/')
        apps('github', 'https://github.com/')
        apps('chatgpt', 'https://chatgpt.com/')
        apps('discord', 'https://discord.com/app')
        apps('whatsapp', 'https://web.whatsapp.com/')
        apps('instagram', 'https://www.instagram.com/')
        apps('spotify', 'https://open.spotify.com/')
        apps('tiktok', 'https://www.tiktok.com/')
        apps('gmail', 'https://mail.google.com/')
        apps('google maps', 'https://maps.google.com/')
        apps('google drive', 'https://drive.google.com/')
        apps('google docs', 'https://docs.google.com/')
        apps('wikipedia', 'https://www.wikipedia.org/')
        apps('netflix', 'https://www.netflix.com/')
        apps('reddit', 'https://www.reddit.com/')
        apps('facebook', 'https://www.facebook.com/')
        apps('x', 'https://x.com/')
        apps('linkedin', 'https://www.linkedin.com/')
        apps('pinterest', 'https://www.pinterest.com/')
        apps('twitch', 'https://www.twitch.tv/')
        apps('canva', 'https://www.canva.com/')
        apps('notion', 'https://www.notion.so/')
        apps('trello', 'https://trello.com/')
        apps('figma', 'https://www.figma.com/')
        apps('stackoverflow', 'https://stackoverflow.com/')
        apps('w3schools', 'https://www.w3schools.com/')
        apps('python', 'https://www.python.org/')
        apps('arduino', 'https://www.arduino.cc/')
        apps('autodesk', 'https://www.autodesk.com/')
        apps('thingiverse', 'https://www.thingiverse.com/')
        apps('printables', 'https://www.printables.com/')
        apps('creality', 'https://www.creality.com/')
        apps('coursera', 'https://www.coursera.org/')
        apps('udemy', 'https://www.udemy.com/')
        apps('khan academy', 'https://www.khanacademy.org/')
        apps('wolfram alpha', 'https://www.wolframalpha.com/')
        apps('desmos', 'https://www.desmos.com/calculator')
        apps('geogebra', 'https://www.geogebra.org/')

        apps('gitlab', 'https://gitlab.com/')
        apps('replit', 'https://replit.com/')
        apps('codepen', 'https://codepen.io/')
        apps('google colab', 'https://colab.research.google.com/')
        apps('kaggle', 'https://www.kaggle.com/')
        apps('hugging face', 'https://huggingface.co/')
        apps('pypi', 'https://pypi.org/')
        apps('npm', 'https://www.npmjs.com/')
        apps('mdn web docs', 'https://developer.mozilla.org/')
        apps('tinkercad', 'https://www.tinkercad.com/')
        apps('onshape', 'https://www.onshape.com/')
        apps('grabcad', 'https://grabcad.com/')
        apps('makerworld', 'https://makerworld.com/')
        apps('myminifactory', 'https://www.myminifactory.com/')
        apps('instructables', 'https://www.instructables.com/')
        apps('hackaday', 'https://hackaday.com/')
        apps('raspberry pi', 'https://www.raspberrypi.com/')
        apps('esp32', 'https://www.espressif.com/')
        apps('google calendar', 'https://calendar.google.com/')
        apps('google translate', 'https://translate.google.com/')
        apps('google classroom', 'https://classroom.google.com/')
        apps('google sheets', 'https://sheets.google.com/')
        apps('google slides', 'https://slides.google.com/')
        apps('google photos', 'https://photos.google.com/')
        apps('outlook', 'https://outlook.live.com/')
        apps('onedrive', 'https://onedrive.live.com/')
        apps('zoom', 'https://zoom.us/')
        apps('google meet', 'https://meet.google.com/')
        apps('amazon', 'https://www.amazon.com/')
        apps('ebay', 'https://www.ebay.com/')
        apps('aliexpress', 'https://www.aliexpress.com/')
        apps('photopea', 'https://www.photopea.com/')
        apps('remove bg', 'https://www.remove.bg/')
        apps('pexels', 'https://www.pexels.com/')
        apps('unsplash', 'https://unsplash.com/')
        apps('capcut', 'https://www.capcut.com/')
        apps('adobe', 'https://www.adobe.com/')
        apps('brilliant', 'https://brilliant.org/')
        apps('symbolab', 'https://www.symbolab.com/')
        apps('mathway', 'https://www.mathway.com/')
        apps('physics classroom', 'https://www.physicsclassroom.com/')
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
# API da Gro

client = Groq(
    api_key=st.secrets["api"]
)
personalidade = f'''u es uma ia de uso pessoal se mais humano so esplica algo se ficar explicito que tens de 
responder se nao e so um conevressa  fala sempre portugues 
o teu nome e A.N.D.R.E abreviaçao de Assistente Neural Digital de Resposta e Execução e tu tens a capacidade de abiri ent se te pedirem pra abiri algum site so diz (claro so apertar no boatao abaixo)
esta e a lingua que tu vais responder: {lingua}
estas foram as tuas ultimas respostas {st.session_state.hie}
e estas foram as minhas ultimas perguntas {st.session_state.hir}

'''
# Guarda qual áudio já foi processado
if st.session_state.bot:
    escrve = st.chat_input('pergunta')
    if escrve.lower == 'none':
        st.write('escreve')
    else:
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
        falar = gt.gTTS(a, lang=idiomas_gtts[st.session_state.ln], slow=False)

        audio_resposta = "resposta.mp3"
        falar.save("resposta.mp3")
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
        app('modulador',
            'https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364')
        app('google', 'https://www.google.com/')
        app('github', 'https://github.com/')
        app('chatgpt', 'https://chatgpt.com/')
        app('discord', 'https://discord.com/app')
        app('whatsapp', 'https://web.whatsapp.com/')
        app('instagram', 'https://www.instagram.com/')
        app('spotify', 'https://open.spotify.com/')
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

        app('gitlab', 'https://gitlab.com/')
        app('replit', 'https://replit.com/')
        app('codepen', 'https://codepen.io/')
        app('google colab', 'https://colab.research.google.com/')
        app('kaggle', 'https://www.kaggle.com/')
        app('hugging face', 'https://huggingface.co/')
        app('pypi', 'https://pypi.org/')
        app('npm', 'https://www.npmjs.com/')
        app('mdn web docs', 'https://developer.mozilla.org/')
        app('tinkercad', 'https://www.tinkercad.com/')
        app('onshape', 'https://www.onshape.com/')
        app('grabcad', 'https://grabcad.com/')
        app('makerworld', 'https://makerworld.com/')
        app('myminifactory', 'https://www.myminifactory.com/')
        app('instructables', 'https://www.instructables.com/')
        app('hackaday', 'https://hackaday.com/')
        app('raspberry pi', 'https://www.raspberrypi.com/')
        app('esp32', 'https://www.espressif.com/')
        app('google calendar', 'https://calendar.google.com/')
        app('google translate', 'https://translate.google.com/')
        app('google classroom', 'https://classroom.google.com/')
        app('google sheets', 'https://sheets.google.com/')
        app('google slides', 'https://slides.google.com/')
        app('google photos', 'https://photos.google.com/')
        app('outlook', 'https://outlook.live.com/')
        app('onedrive', 'https://onedrive.live.com/')
        app('zoom', 'https://zoom.us/')
        app('google meet', 'https://meet.google.com/')
        app('amazon', 'https://www.amazon.com/')
        app('ebay', 'https://www.ebay.com/')
        app('aliexpress', 'https://www.aliexpress.com/')
        app('photopea', 'https://www.photopea.com/')
        app('remove bg', 'https://www.remove.bg/')
        app('pexels', 'https://www.pexels.com/')
        app('unsplash', 'https://unsplash.com/')
        app('capcut', 'https://www.capcut.com/')
        app('adobe', 'https://www.adobe.com/')
        app('brilliant', 'https://brilliant.org/')
        app('symbolab', 'https://www.symbolab.com/')
        app('mathway', 'https://www.mathway.com/')
        app('physics classroom', 'https://www.physicsclassroom.com/')
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
                falar = gt.gTTS(a, lang=idiomas_gtts[st.session_state.ln], slow=False)

                audio_resposta = "resposta.mp3"
                falar.save("resposta.mp3")

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
                app('modulador',
                    'https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364')
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
