import streamlit as st
import json
import matplotlib.pyplot as plt 

# carregar tarefas 

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
          return json.load(arquivo) 
    except:
       return[]
    
tarefas = carregar_tarefas()

st.title("Task Manager")

# Mostrar tarefas 

st.subheader("Tarefas")

for i, tarefa in enumerate(tarefas):
   concluida = st.checkbox(
      tarefa["titulo"],
      value = tarefa["concluida"],
      key = i
   )

   tarefas[i]["concluida"] = concluida

with open("tarefas.json", "w") as arquivo:
   json.dump(tarefas, arquivo, indent=4)

# grafico

st.subheader("📊Estatísticas")

total = len(tarefas)
concluidas = sum(1 for t in tarefas if t["concluida"])
pendentes = total - concluidas

if total > 0:
   fig, ax = plt.subplots()
   ax.bar(["Concluídas", "Pendentes"], [concluidas, pendentes])
   st.pyplot(fig)
   
st.subheader("➕Nova tarefa")

titulo = st.text_input("Título da tarefa")

if st.button("Adicionar"):
   nova_tarefa = {
      "titulo": titulo,
      "concluida": False
   }

   tarefas.append(nova_tarefa)

   with open("tarefas.json", "w") as arquivo:
      json.dump(tarefas, arquivo, indent=4)
      st.success("Tarefa adicionada!")
   