import streamlit as st
import json
import matplotlib.pyplot as plt 

## carregar tarefas 

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
          return json.load(arquivo) 
    except:
       return[]
    
tarefas = carregar_tarefas()

## ordenar: pendente primeiro

tarefas =  sorted(tarefas, key=lambda x:x["concluida"])

## coluna1 tarefas // coluna2 dados e gráfico

st.title("📋 Task Manager Dashboard")
st.caption("Gerencie suas tarefas e acompanhe sua produtividade em tempo real")

st.divider()

col1, col2 = st.columns(2)

with col1:
     st.subheader("📝 Tarefas")

     for i, tarefa in enumerate(tarefas):
        concluida = st.checkbox(
            tarefa["titulo"],
            value = tarefa["concluida"],
            key = i
        )
        tarefas[i]["concluida"] = concluida

        if concluida and not tarefa["concluida"]:
            st.success(f"{tarefa[titulo]} concluída!")

with col2:
   st.subheader("📊Estatísticas")

   total = len(tarefas)
   concluidas =  sum(1 for t in tarefas if t["concluida"])
   pendentes = total - concluidas

   st.write(f"Total: {total}")
   st.write(f"Concluídas: {concluidas}")
   st.write(f"Pendentes: {pendentes}")


   if total > 0:
      fig, ax = plt.subplots()
      ax.bar(["Concluídas", "Pendentes"],[concluidas, pendentes])
      st.pyplot(fig)

## Adicionar tarefa

st.subheader("➕Nova tarefa")

with st.form("nova_tarefa_form"):
   titulo = st.text_input("Título da tarefa")
   submitted = st.form_submit_button("Incluir")

   if submitted and titulo:
      nova_tarefa = {
         "titulo": titulo,
         "concluida": False
      }

      tarefas.append(nova_tarefa)

      with open("tarefas.json", "w") as arquivo:
         json.dump(tarefas, arquivo, indent=4)

         st.success("Tarefa Adiconada!")

## salvar alterações

with open("tarefas.json", "w") as arquivo:
   json.dump(tarefas, arquivo, indent=4)