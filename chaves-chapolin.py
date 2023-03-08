import streamlit as st
from yaml import safe_load


page_title = 'Assista: Chaves & Chapolin'
page_favicon = 'favicon.ico'

st.set_page_config(page_title=page_title, page_icon=page_favicon,
                   layout='wide', initial_sidebar_state='auto', menu_items=None)

st.title(page_title)

st.write('Escolha qual dos dois seriados você quer assistir')


def embed_video(video_url):
    return f'https://onelineplayer.com/player.html?autoplay=true&autopause=true&muted=true&loop=true&url={video_url}&poster=&time=true&progressBar=true&overlay=true&muteButton=true&fullscreenButton=true&style=light&quality=auto&playButton=true&buttonColor=%23ffffff&buttonSize=40'


def show_video(video_url, thumb_url, duration):
    duration = format_duration(duration)
    st.write('''
        <style>
            .duration-box {
                position: absolute;
                bottom: 2px;
                right: 5px;
                background-color: black;
                color: white;
                font-size: 12px;
                padding: 2px 4px;
                z-index: 1;
            }
            iframe {
                position: relative;
                z-index: 0;
            }
        </style>
    ''', unsafe_allow_html=True)
    st.write(f'''
    <iframe frameborder="0" allowfullscreen="" scrolling="no" allow="autoplay;fullscreen" width="235" height="132"
        src="https://onelineplayer.com/player.html?autoplay=false&autopause=true&muted=true&loop=true&url={video_url}&poster={thumb_url}&time=true&progressBar=true&overlay=true&muteButton=true&fullscreenButton=true&style=light&quality=auto&playButton=true">
    <div id="duration" style="position:absolute; bottom: 0; left: 0; color: white; background-color: rgba(0,0,0,0.7); padding: 2px 4px; font-size: 12px;"></div>
    </iframe>
    <div class="duration-box">{duration}</div>
    ''', unsafe_allow_html=True)


def format_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if hours == 0:
        if minutes == 0:
            return f'0:{seconds:02}'
        else:
            return f'{minutes}:{seconds:02}'
    else:
        return f'{hours}:{minutes:02}:{seconds:02}'


col1_1, col1_2, col1_3, col1_4, col1_5, col1_6, col1_7, col1_8, col1_9, col1_10 = st.columns(10)

btn_chaves = col1_1
if col1_1.button('**‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Chaves ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎**',
                 key='chaves', help='Clique aqui para assistir ao seriado **Chaves**'):
    pass


if col1_2.button('**Chapolin Colorado**',
                 key='chapolin', help='Clique aqui para assistir ao seriado **Chapolin Colorado**'):
    with st.spinner('Carregando informações...'):

        def show_season(series, season_number):
            season = series['seasons'][season_number]
            episodes = season['episodes']

            st.title(f'Você está assistindo: {series["title"]}')
            st.markdown('---')

            st.info(f'**{season["title"]}**')

            page_columns = st.columns(7)
            for number, episode in episodes.items():
                with page_columns[(int(number) - 1) % 7]:
                    show_video(episode['url'], episode['thumb_url'], episode['length'])


        col_btn1_t1, col_btn1_t2, col_btn1_t3, col_btn1_t4 = st.columns(4)


        def show_chapolin():
            with open('informacoes_seriados/chapolin/info.yaml', 'r') as file:
                series = safe_load(file)
                for season_number, season in series['seasons'].items():
                    col_btn1_t1.button(f'**Exibir a {season["title"]}**',
                                       on_click=show_season,
                                       args=(series, season_number))

        show_chapolin()
