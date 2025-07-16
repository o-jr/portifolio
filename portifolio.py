import streamlit as st
from constants import *
from streamlit_lottie import st_lottie 
import streamlit_option_menu as option_menu
import requests
import json
import base64


st.set_page_config(page_title='Orlando Junior - Transformando dados em Insights!' , initial_sidebar_state="collapsed", layout="wide",page_icon='👨‍🔬')


st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


col1, col2, col3 = st.columns(3)
 

def new_func():
    st.markdown(
      "<h1 style='font-size: 4em; text-align: center; font-family: Montserrat; color: #03A9F4;'>Orlando Junior</h1>", #03A9F4
      unsafe_allow_html=True
    )

with col2:
    new_func()
    st.markdown(
      "<h1 style='font-size: 2em; text-align: center; font-family: Montserrat;'>Analista de Dados</h1",
      unsafe_allow_html=True
    )
    st.markdown( 
      "<h2 style='font-size: 1em; text-align:  center;'>Transformo dados em decisões. Da coleta à visualização, construo pontes entre números brutos e insights estratégicos. Minha expertise abrange desde a extração e processamento de dados complexos até a criação de dashboards interativos. </h2>",
      unsafe_allow_html=True
    )


st.divider()


url0 = requests.get(
  "https://lottie.host/a7c56f1f-c5b1-4b07-b0fb-c6da4cb18968/mm8jdB6UgW.json"
)
url_json0 = dict()
if url0.status_code == 200:
  url_json0 = url0.json()
else:
  print("Error in URL 1")


url1 = requests.get(
  "https://lottie.host/220ced0d-9e0b-4d67-80cf-7378beffdbf9/sRUs1eVuwY.json"
)
url_json1 = dict()
if url1.status_code == 200:
  url_json1 = url1.json()
else:
  print("Error in URL 1")


url2 = requests.get(
  "https://lottie.host/43dc092c-4238-4927-8866-88c0e2ed8ef9/dz3xJlVPk8.json"
)
url_json2 = dict()
if url2.status_code == 200:
  url_json2 = url2.json()
else:
  print("Error in URL 2")


url3 = requests.get(
  "https://lottie.host/3ce03283-1d06-4d03-a53d-29e02d656ca7/66UQAiBmH1.json"
)
url_json3 = dict()
if url3.status_code == 200:
  url_json3 = url3.json()
else:
  print("Error in URL 3")
  

url4 = requests.get(
  "https://lottie.host/aeaa28ab-bc6e-46e8-ba7c-96ed528e2b4d/39NpdtpMzA.json"
)
url_json4 = dict()
if url4.status_code == 200:
  url_json4 = url4.json()
else:
  print("Error in URL 4")  


url5 = requests.get(
  "https://lottie.host/ca012a7b-b703-4338-a2c2-bb3fb50b4ea8/dHGO0HrBMx.json"
)
url_json5 = dict()
if url5.status_code == 200:
  url_json5 = url5.json()
else:
  print("Error in URL 5") 


st.markdown(
      #"<h1 style='font-size: 2em; text-align: center;'>O que eu faço</h1",
      "<h1 style='font-size: 2em; text-align: center; font-family: Montserrat;'>Principais Competências</h1>", #03A9F4
      unsafe_allow_html=True
    )


st.markdown('#')


coll1, coll2, coll3, coll4, coll5 = st.columns((1, 2, 2, 2, 1))

with coll3:
    st_lottie(
        url_json5,
        reverse=True,  # Change the direction of the animation
        height=100,    # Height of the animation
        width=None,     # Set width to None to automatically adjust to column width
        speed=1,       # Speed of the animation
        loop=True,     # Run the animation forever
        quality='high',  # Quality of the animation
        key='Viz'     # Unique identifier for the animation
    )
    st.markdown(f"<h3 style='text-align: center; font-family: Montserrat;'>Visualização de Dados</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Transformo dados em narrativas visuais acionáveis através de dashboards interativos e relatórios analíticos. Domínio de ferramentas como Power BI, Qlik Sense e Excel/Google Sheets para criação de KPIs e gráficos dinâmicos.</p>", unsafe_allow_html=True)

with coll2:
    st_lottie(
        url_json0,
        reverse=True,  # Change the direction of the animation
        height=100,    # Height of the animation
        width=None,     # Set width to None to automatically adjust to column width
        speed=1,       # Speed of the animation
        loop=True,     # Run the animation forever
        quality='high',  # Quality of the animation
        key='Db'     # Unique identifier for the animation
    )
    st.markdown(f"<h3 style='text-align: center; font-family: Montserrat;'>Banco de Dados</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Proeficiente em modelagem de dados e desenvolvimento de soluções otimizadas em ambientes SQL (MySQL, PostgreSQL) e NoSQL (MongoDB). Experiência em criação de queries complexas, views, índices e procedures para maximizar desempenho e escalabilidade.</p>", unsafe_allow_html=True)

with coll4:
    st_lottie(
        url_json1,
        reverse=True,  # Change the direction of the animation
        height=100,    # Height of the animation
        width=None,     # Set width to None to automatically adjust to column width
        speed=1,       # Speed of the animation
        loop=True,     # Run the animation forever
        quality='high',  # Quality of the animation
        key='Quant'     # Unique identifier for the animation
    )
    st.markdown(f"<h3 style='text-align: center; font-family: Montserrat;'>Análise Quantitativa</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Aplicação de métodos estatísticos e modelos preditivos (como regressão) para resolver problemas complexos. Utilização de Python (Pandas, NumPy, statsmodels) para limpeza de dados, modelos de regressão, classificação e automação de processos analíticos.</p>", unsafe_allow_html=True)


coll1, coll2, coll3, coll4, coll5 = st.columns((1,2,2,2, 1))

with coll2:
    st_lottie(
        url_json3,
        reverse=True,  # Change the direction of the animation
        height=100,    # Height of the animation
        width=None,     # Set width to None to automatically adjust to column width
        speed=1,       # Speed of the animation
        loop=True,     # Run the animation forever
        quality='high',  # Quality of the animation
        key='End'     # Unique identifier for the animation
    )
    st.markdown(f"<h3 style='text-align: center; font-family: Montserrat;'>Engenharia de Dados</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Projetista de pipelines de dados eficientes, desde a extração até a carga em data warehouses. Experiência com ETL/ELT utilizando Power Query, Pandas, DuckDB, AWS Glue e dbt.</p>", unsafe_allow_html=True)

with coll3:
    st_lottie(
        url_json2,
        reverse=True,  # Change the direction of the animation
        height=100,    # Height of the animation
        width=None,     # Set width to None to automatically adjust to column width
        speed=1,       # Speed of the animation
        loop=True,     # Run the animation forever
        quality='high',  # Quality of the animation
        key='Cloud'     # Unique identifier for the animation
    )
    st.markdown(f"<h3 style='text-align: center; font-family: Montserrat;'>Computação em Nuvem</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Implemento e gerencio infraestruturas de dados em ambientes cloud AWS, incluindo implementação de data lakes (S3) e data warehouses (Redshift). Gerenciamento de serviços como Lambda e Athena para escalabilidade e eficiência.</p>", unsafe_allow_html=True)

with coll4:
    st_lottie(
        url_json4,
        reverse=True,  # Change the direction of the animation
        height=100,    # Height of the animation
        width=None,     # Set width to None to automatically adjust to column width
        speed=1,       # Speed of the animation
        loop=True,     # Run the animation forever
        quality='high',  # Quality of the animation
        key='Lnx'     # Unique identifier for the animation
    )
    st.markdown(f"<h3 style='text-align: center; font-family: Montserrat;'>Servidores Linux</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Prática em ambientes Linux para suportar fluxos de trabalho de análise e engenharia de dados. Experiência em shell scripting, administração de servidores e configuração de ambientes de desenvolvimento.</p>", unsafe_allow_html=True)


st.divider()


col1, col2, col3, col4, col5 = st.columns((1, 4, 0.5, 1, 1))

with col2:
    st.markdown(f"<p style='text-align: center;'>Minha jornada na análise de dados começou com uma curiosidade geuína pelos números e padrões que movimentam o mercado financeiro. A partir dessa experiência, desenvolvi uma base sólida em processos que envolvem desde a coleta até a transformação e interpretação de grandes volumes de dados. Tenho perfil analítico, gosto de entender o cenário por trás dos números e transformar dados brutos em insights valiosos que apoiam decisões estratégicas.Sou motivado por desafios e apaixonado por explorar o potencial dos dados para resolver problemas reais de negócios. Busco constantemente aprimorar minhas habilidades e acompanhar as inovações dessa área que está em constante evolução. Acredito que dados contam histórias e meu objetivo é traduzi-las de forma clara, visual e acessível para diferentes públicos e objetivos.</p>", unsafe_allow_html=True)

with col4:
    st.image("img/me.jpg", width=300)


st.divider()


st.markdown(
      "<h1 style='font-size: 2em; text-align: center; font-family: Montserrat;'>Portfólio</h1",
      unsafe_allow_html=True
    )

#st.markdown("<h2 style='font-size: 1em; text-align: center;'>Alguns exemplos dos meus trabalhos </h2>", unsafe_allow_html=True)


st.markdown('#')


c1,c2,c3,c4 = st.columns((1, 1, 1, 1))

with c1:
    st.image("img/merchan.jpg", caption="Visualização detalhada de propagandas, segmentadas por produtos, classificação, regiões, demografia e custos de envio.") 
    st.page_link("https://github.com/o-jr/PBI-sales-analysis", label="Power Query - Power BI - DAX", icon="⚙️")


with c2:
    st.image("img/pipeline.png", caption="Web Scraping") 
    st.page_link("https://github.com/o-jr/amazon-scraping", label="Scrapy - Spidermon - Pandas - DuckDB -Streamlit", icon="⚙️")

with c3:
    st.image("img/pixar.png", caption="Um animado dashboard sobre a história da Pixar") 
    st.page_link("https://mavenanalytics.io/project/29468", label="Python - Pandas - BS4 - Matplotlib - Streamlit", icon="⚙️")

with c4:
    st.image("img/Qliksense.png", caption="Dashboard de vendas criado no Qliksense") 
    st.page_link("https://github.com/o-jr/", label="Qlik Sense", icon="⚙️")



c1,c2,c3,c4 = st.columns((1, 1, 1, 1))

with c3:
    st.image("img/Insurance.png", caption="Projeto desenvolvido para o acompanhamento e gerenciamento financeiro hospitalar. ") 
    st.page_link("https://mavenanalytics.io/project/17139", label="Power Query - Power BI - DAX", icon="⚙️")

with c1:
    st.image("img/etl100m.png", caption="Comparação de ferramentas para analise e transformação de 100M de linhas") 
    st.page_link("https://github.com/o-jr/10Mi-ETL-Compare", label="Python - Pandas - DuckDB", icon="⚙️")

with c2:
    st.image("img/stocks.png", caption="Dashboard criado para o acompanhamento de performance de ações, focado em análise temporal e indicadores financeiros.") 
    st.page_link("https://mavenanalytics.io/project/18883", label="Power Query - Power BI - DAX", icon="⚙️")

with c4:
    st.image("img/reva.jpg", caption="Essa análise monitora o desempenho de vendas trimestrais, performance de gerentes, tendências de produtos e categoria.") 
    st.page_link("https://mavenanalytics.io/project/16179", label="Power Query - Power BI - DAX", icon="⚙️")


c1,c2,c3,c4 = st.columns((1, 1, 1, 1))

with c1:
    st.image("img/adx.jpg", caption="Indicador ADX criado para o TradingView") 
    st.page_link("https://www.tradingview.com/script/Dae642sS-ADX-Color/", label="Pine Script", icon="⚙️")

with c3:
    st.image("img/rsi.jpg", caption="Indicador RSI criado para o TradingView") 
    st.page_link("https://www.tradingview.com/script/TQsL5zvY-RSI-Tabajara/", label="Pine Script", icon="⚙️")

with c2:
    st.image("img/palex.jpg", caption="Setup Palex criado para o TradingView")
    st.page_link("https://www.tradingview.com/script/2JVJLjdl-Palex-SENSACIONAL/", label="Pine Script", icon="⚙️")


st.divider()


st.markdown(
      "<h1 style='font-size: 2em; text-align: center; font-family: Montserrat;'>Cursos e Certificados</h1",
      unsafe_allow_html=True
    )


coll1, coll2, coll3, coll4, coll5, coll6 = st.columns((1, 2, 2, 2, 2,1))


with coll2:
  st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>SQL e NoSQL</h1", unsafe_allow_html=True)  
  st.page_link("https://certificates.mavenanalytics.io/a64dc068-517b-4e9b-8ed1-7f00010aabfc#acc.E9ChZOVc", label="MySQL Data Analysis", icon="🔗")
  st.page_link("https://learn.mongodb.com/learn/learning-path/introduction-to-mongodb", label="Introduction to MongoDB", icon="🔗")
  st.page_link("https://learn.mongodb.com/learn/learning-path/mongodb-for-sql-professionals", label="MongoDB for SQL Professionals", icon="🔗")

with coll4:
  st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>Visualização de Dados</h1", unsafe_allow_html=True) 
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/e57a49da949a1be38ba48fc9fbd7dbd50eb947e3", label="Financial Analytics in Google Sheets", icon="🔗"  )  
  st.page_link("https://certificates.mavenanalytics.io/e189a2cc-b135-467e-9e9c-9a974c66453e", label="Thinking Like an Analyst", icon="🔗")
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/c95e046b0728713aa8afd1d7cb53b0342b318012", label="Communicating Data Insights", icon="🔗"  )
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/206829a892790ed9b5b06221fdc232da7f3b567a", label="Data Storytelling Concepts", icon="🔗"  )
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/26644d513781234a8b530241699518f6a6fe29c3", label="Storytelling Case: College Majors", icon="🔗"  )
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/efdc3d82f904563aaf4202dd6caaf4ec14a678b5", label="Storytelling Case: Green Businesses", icon="🔗"  )  
  
with coll3:
    st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>Python</h1", unsafe_allow_html=True)
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/0ca5b42f960964811c239b51e89902d0dfcbb5bb", label="Introduction to Statistics in Python", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/e66dc459b6a932a6d588932c58e325bb001a86d7", label="Intro to Regression with statsmodels", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/27fc09e696cf5f12952702bcc0dcae371ea8913d", label="Customer Analytics and A/B Testing", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/9e98c3548df109250c5564af562b66a15b0e2e2a", label="ETL and ELT in Python", icon="🔗"  )

with coll5:
    st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>Engenharia de Dados</h1", unsafe_allow_html=True)
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/9006fde1cb64aa324bfff769f4cedfa0010f1688", label="Introduction to Git", icon="🔗")
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/b8d0d884f3c335ff93caa690251b3fa9f320ba2c", label="Introduction to GitHub Concepts", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/7373d38822feebc21a5903648e8113f922221888", label="Intermediate Git", icon="🔗"  )    
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/1222d7313e6faad6216837e11ccf292f40c95b06", label="Intermediate GitHub Concepts", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/7e4caa09033c35bf34f5378c8c85c45a504b4e40", label="Introduction to dbt", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/e879e1bc2067e44c23454e7332fdaff68fa588bd", label="Intermediate dbt", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/1746ff9e4273e6d3b4da4da19ebd8ef2b67d355b", label="Case: Building E-Commerce Models with dbt", icon="🔗"  )


st.divider()


st.markdown(
      "<h1 style='font-size: 2em; text-align: center; font-family: Montserrat;'>Contatos</h1",
      unsafe_allow_html=True
    )

st.markdown(f"<p style='text-align: center;'>{info['Mobile']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{info['Email']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{info['City']}</p>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns((4,0.5,0.5,0.5,0.5,4))

with col5:
    st.markdown(
    """<a href="https://www.tradingview.com/u/orlandojunior.py/#published-scripts">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(
        base64.b64encode(open("./app/static/trading.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    
with col3:
    st.markdown(
    """<a href="https://github.com/o-jr/">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(
        base64.b64encode(open("./app/static/git.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    
with col4:
    st.markdown(
    """<a href="https://x.com/ojwjunior">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(
        base64.b64encode(open("./app/static/x.jpg", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)

with col2:
    st.markdown(
    """<a href="https://www.linkedin.com/in/o-junior/">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(
        base64.b64encode(open("./app/static/linke.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
    


def main():
   st.markdown('''''')

if __name__ == "__main__":
    main()