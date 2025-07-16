import streamlit as st
from constants import *
from streamlit_lottie import st_lottie 
import streamlit_option_menu as option_menu
import requests
import json

st.set_page_config(page_title='Orlando Junior Portfolio' ,layout="wide",page_icon='👨‍🔬')



#https://app.mavenanalytics.io/portfolio
#https://www.datacamp.com/portfolio/o-junior



col1, col2, col3 = st.columns(3)

 

with col2:
    st.markdown(
      "<h1 style='font-size: 4em; text-align: center; color: grey;'>Orlando Junior</h1>",
      unsafe_allow_html=True
    )
    st.markdown(
      "<h1 style='font-size: 2em; text-align: center;'>Analista de Dados</h1",
      unsafe_allow_html=True
    )
    st.markdown(
      "<h2 style='font-size: 1em; text-align: center;'>Transformo dados em decisões. Da coleta à visualização, construo pontes entre números brutos e insights estratégicos. Minha expertise abrange desde a extração e processamento de dados complexos até a criação de dashboards interativos. </h2>",
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
      "<h1 style='font-size: 2em; text-align: center;'>Áreas de Interesse</h1",
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

    st.markdown(f"<h3 style='text-align: center;'>Visualização de Dados</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Desenvolvimento de dashboards interativos, KPIs e relatórios analíticos com ferramentas como Power BI, Excel, Google Sheets e Streamlit para transformar dados em insights visuais e acionáveis.</p>", unsafe_allow_html=True)

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
    st.markdown(f"<h3 style='text-align: center;'>Banco de Dados</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Modelagem de dados e desenvolvimento de queries otimizadas, views, indexes e procedures em ambientes SQL e NoSQL para estruturar e acessar informações de forma eficiente.</p>", unsafe_allow_html=True)

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

    st.markdown(f"<h3 style='text-align: center;'>Análise Quantitativa</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Aplicação de métodos estatísticos, técnicas de limpeza, manipulação de dados, modelos de regressão e automação de processos analíticos utilizando Python.</p>", unsafe_allow_html=True)


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
    st.markdown(f"<h3 style='text-align: center;'>Engenharia de Dados</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Experiência em processos ETL (Extração, Transformação e Carregamento) utilizando Power Query, Pandas, DuckDB e AWS Glue para preparar dados para análise.</p>", unsafe_allow_html=True)

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
    st.markdown(f"<h3 style='text-align: center;'>Computação em Nuvem</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Implementação e gerenciamento de infraestruturas de dados em ambientes cloud AWS. Experiência em configuração de data lakes, data warehouses e serviços de processamento distribuído.</p>", unsafe_allow_html=True)


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
    st.markdown(f"<h3 style='text-align: center;'>Servidores Linux</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Proficiência em ambientes Linux para análise de dados, incluindo shell scripting, administração de servidores e configuração de ambientes de desenvolvimento.</p>", unsafe_allow_html=True)

st.divider()





col1, col2, col3, col4, col5 = st.columns((1, 3, 1, 1, 1))

with col2:
    st.markdown(f"<p style='text-align: center;'>Minha jornada na análise de dados começou com uma curiosidade sobre os números e gráficos por traz do mercado financeiro. Por meio dessa experincia desenvolvi uma base sólida em coleta, análise, visualização e inteligência de negócios de dados. Profissional orientado a dados com sólida formação em SQL, Power BI, Python e Excel. - Habilidade em extrair, transformar e analisar conjuntos de dados complexos para descobrir insights valiosos e impulsionar tomadas de decisão informadas. - Proficiente em projetar e desenvolver consultas SQL eficientes para gerenciar e manipular bancos de dados relacionais. - Experiência na criação de painéis visualmente atraentes e interativos usando o Power BI para comunicar com eficácia as principais métricas e tendências às partes interessadas. - Hábil em utilizar Python para manipulação de dados e análise estatística. - Usuário avançado de Excel com experiência na utilização de funções avançadas e tabelas dinâmicas. - Apaixonado por aproveitar o poder dos dados para resolver problemas de negócios complexos e fornecer recomendações acionáveis. Busca constante por oportunidades para expandir o conhecimento e se manter atualizado com as ferramentas e técnicas mais recentes no campo em constante evolução da análise de dados.</p>", unsafe_allow_html=True)

with col4:
    st.image("img/me.jpg", width=200)


st.divider()


st.markdown(
      "<h1 style='font-size: 2em; text-align: center;'>Portifolio</h1",
      unsafe_allow_html=True
    )

st.markdown(
      "<h2 style='font-size: 1em; text-align: center;'>Alguns exemplos dos meus trabalhos </h2>",
      unsafe_allow_html=True
    )
st.markdown('#')

c1,c2,c3,c4 = st.columns((1, 1, 1, 1))
with c1:
    st.image("img/Qliksense.png", caption="Dashboard de vendas criado no Qliksense") #
    st.page_link("https://github.com/o-jr/", label="Qlik Sense", icon="⚙️")
with c2:
    st.image("img/pipeline.png", caption="Web Scraping") #
    st.page_link("https://github.com/o-jr/amazon-scraping", label="Scrapy - Spidermon - Pandas - DuckDB -Streamlit", icon="⚙️")

with c3:
    st.image("img/pixar.png", caption="Um animado dashboard sobre a história da Pixar") #
    st.page_link("https://mavenanalytics.io/project/29468", label="Python - Pandas - BS4 - Matplotlib - Streamlit", icon="⚙️")

with c4:
    st.image("img/merchan.jpg", caption="Visualização detalhada de propagandas") #
    st.page_link("https://github.com/o-jr/PBI-sales-analysis", label="Power Query - Power BI - DAX", icon="⚙️")



c1,c2,c3,c4 = st.columns((1, 1, 1, 1))
with c3:
    st.image("img/Insurance.png", caption="Projeto ") #
    st.page_link("https://mavenanalytics.io/project/17139", label="Power Query - Power BI - DAX", icon="⚙️")

with c1:
    st.image("img/etl100m.png", caption="Comparação de ferramentas para analise de 100M de linhas") #
    st.page_link("https://github.com/o-jr/10Mi-ETL-Compare", label="Python - Pandas - DuckDB", icon="⚙️")

with c2:
    st.image("img/stocks.png", caption="Sunrise by the mountains") #
    st.page_link("https://mavenanalytics.io/project/18883", label="Power Query - Power BI - DAX", icon="⚙️")

with c4:
    st.image("img/reva.jpg", caption="Sunrise by the mountains") #
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
      "<h1 style='font-size: 2em; text-align: center;'>Cursos e Certificados</h1",
      unsafe_allow_html=True
    )

coll1, coll2, coll3, coll4, coll5, coll6 = st.columns((1, 2, 2, 2, 2,1))



with coll2:
  st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>SQL e Google Sheets</h1", unsafe_allow_html=True)  
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/e57a49da949a1be38ba48fc9fbd7dbd50eb947e3", label="Financial Analytics in Google Sheets", icon="🔗"  )  
  st.page_link("https://certificates.mavenanalytics.io/a64dc068-517b-4e9b-8ed1-7f00010aabfc#acc.E9ChZOVc", label="MySQL Data Analysis", icon="🔗")

with coll4:
  st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>Visualização de Dados</h1", unsafe_allow_html=True) 
  st.page_link("https://certificates.mavenanalytics.io/e189a2cc-b135-467e-9e9c-9a974c66453e", label="Thinking Like an Analyst", icon="🔗")
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/c95e046b0728713aa8afd1d7cb53b0342b318012", label="Communicating Data Insights", icon="🔗"  )
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/206829a892790ed9b5b06221fdc232da7f3b567a", label="Data Storytelling Concepts", icon="🔗"  )
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/26644d513781234a8b530241699518f6a6fe29c3", label="Storytelling Case Study: College Majors", icon="🔗"  )
  st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/efdc3d82f904563aaf4202dd6caaf4ec14a678b5", label="Storytelling Case Study: Green Businesses", icon="🔗"  )  
  
with coll3:
    st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>Python</h1", unsafe_allow_html=True)
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/0ca5b42f960964811c239b51e89902d0dfcbb5bb", label="Introduction to Statistics in Python", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/e66dc459b6a932a6d588932c58e325bb001a86d7", label="Intro to Regression with statsmodels in Py", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/27fc09e696cf5f12952702bcc0dcae371ea8913d", label="Customer Analytics and A/B Testing in Py", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/9e98c3548df109250c5564af562b66a15b0e2e2a", label="ETL and ELT in Python", icon="🔗"  )

with coll5:
    st.markdown("<h1 style='font-size: 1.5em; text-align: center;'>Engenharia de Dados</h1", unsafe_allow_html=True)
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/9006fde1cb64aa324bfff769f4cedfa0010f1688", label="Introduction to Git", icon="🔗")
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/b8d0d884f3c335ff93caa690251b3fa9f320ba2c", label="Introduction to GitHub Concepts", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/7373d38822feebc21a5903648e8113f922221888", label="Intermediate Git", icon="🔗"  )    
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/1222d7313e6faad6216837e11ccf292f40c95b06", label="Intermediate GitHub Concepts", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/7e4caa09033c35bf34f5378c8c85c45a504b4e40", label="Introduction to dbt", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/e879e1bc2067e44c23454e7332fdaff68fa588bd", label="Intermediate dbt", icon="🔗"  )
    st.page_link("https://www.datacamp.com/completed/statement-of-accomplishment/course/1746ff9e4273e6d3b4da4da19ebd8ef2b67d355b", label="Case Study: Building E-Commerce Data Models with dbt", icon="🔗"  )

st.divider()


st.markdown(
      "<h1 style='font-size: 2em; text-align: center;'>Contatos</h1",
      unsafe_allow_html=True
    )








#https://www.linkedin.com/in/o-junior/
#https://www.tradingview.com/u/orlandojunior.py/
#https://mavenanalytics.io/profile/48b1b3b0-10e1-7039-69cd-80ea64f0c2af / o-junior
#https://www.datacamp.com/portfolio/o-junior

st.markdown(f"<p style='text-align: center;'>{info['Mobile']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{info['Email']}</p>", unsafe_allow_html=True)





def main():
   st.markdown(f"<p style='text-align: center;'>{info['City']}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()