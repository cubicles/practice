import pandas as pd
import webbrowser

df_cursos = pd.read_csv("links.txt", header=None)
df_cursos.columns = ['curso', 'dia', 'link']
curso_dia = input("Inserte el curso y el dia:  ")
curso,dia = curso_dia.split(" ")[0], curso_dia.split(" ")[1]

df2 = df_cursos.loc[(df_cursos['curso'] == curso) & (df_cursos['dia'] == dia)]
web_link = df2.iloc[0]['link']
webbrowser.open_new_tab(web_link)

