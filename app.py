import streamlit as st
import json
import matplotlib.pyplot as plt 

## sidebar 

st.set_page_config(
   page_title="Task Mananger",
   page_icon="📋",
   layout="wide"
)

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

## coluna1 tarefas 

st.title("📋 Task Manager Dashboard")
st.caption("Gerencie suas tarefas e acompanhe sua produtividade em tempo real")

st.divider()

with st.sidebar:
   st.header("Estatísticas")

   total = len(tarefas)
   concluidas = sum(1 for t in tarefas if t["concluida"])
   pendentes = total - concluidas

   st.metric("Total", total)
   st.metric("Concluídas", concluidas)
   st.metric("Pendentes", pendentes)

   ## gráfico

   if total > 0:
      fig, ax = plt.subplots()
      ax.bar(["Concluídas", "Pendentes"], [concluidas, pendentes])
      ax.set_title("Progresso das tarefas")
      st.pyplot(fig)

col1 = st.container()

with col1:
     st.markdown("## Suas tarefas")
     st.caption("Clique para concluir ou deletar")

     for i, tarefa in enumerate(tarefas):
        col_task, col_delete = st.columns([4, 1])

        with col_task:
           concluida = st.checkbox(
              tarefa["titulo"],
              value=tarefa["concluida"],
              key=f"check_{i}"
           )

           tarefas[i]["concluida"] = concluida

        with col_delete:
           if st.button("🗑️", key=f"del_{i}"):
              tarefas.pop(i)
              
              with open("tarefas.json", "w") as arquivo:
                 json.dump(tarefas, arquivo, indent=4)

                 st.rerun()

## Adicionar tarefa

st.markdown("➕Nova tarefa")

with st.form("nova_tarefa_form", clear_on_submit=True):
   titulo = st.text_input("Digite sua tarefa")
   
   submitted = st.form_submit_button("Adicionar")
   
   if submitted and titulo:
      nova_tarefa = {
         "titulo": titulo, 
         "concluida": False
      }

      tarefas.append(nova_tarefa)

      with open("tarefas.json", "w") as arquivo: 
         json.dump(tarefas, arquivo, indent=4)

         st.succes("Tarefa adicionada!")
         st.rerun()

## salvar alterações
with open("tarefas.json", "w") as arquivo:
   json.dump(tarefas, arquivo, indent=4) 
   
