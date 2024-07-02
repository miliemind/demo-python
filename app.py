# app.py
import streamlit as st

from questions import questions

def main():
    st.title('Inventario Portage Digital')

    global age_category

    age_years = st.number_input('Digite a idade da criança em anos:', min_value=0, max_value=6, value=2)
    age_months = st.number_input('Digite os meses da criança:', min_value=0, max_value=11, value=0)

    if age_years == 0:
        age_category = '0 a 1 ano'
    elif age_years == 1:
        age_category = '1 a 2 ano'
    elif age_years == 2 and age_months < 6:
        age_category = '1 a 2 ano'
    elif age_years == 2 and age_months >= 6:
        age_category = '2 a 3 ano'
    elif age_years == 3:
        age_category = '3 a 4 ano'
    elif age_years == 4:
        age_category = '4 a 5 ano'
    elif age_years == 5 or age_years == 6:
        age_category = '5 a 6 ano'
    else:
        st.error('Por favor, insira uma idade válida.')
        age_category = None

    st.write(f'Faixa etária determinada: {age_category}')

    responses = {}

    if age_category and age_category in questions:
        st.subheader(f'Perguntas para a faixa etária de {age_category}')
        category_responses = {}
        for category, qs in questions[age_category].items():
            st.subheader(f'Categoria: {category}')
            category_responses[category] = []
            for i, question in enumerate(qs, start=1):
                response = st.radio(f'Pergunta {i}: {question}', options=['Sim', 'Não'], key=f'{category}_{i}')
                if response == 'Sim':
                    category_responses[category].append(1)
                else:
                    category_responses[category].append(0)

        totals = {category: sum(responses) for category, responses in category_responses.items()}

        st.subheader('Resultados por Categoria')
        for category, total in totals.items():
            st.write(f'**Categoria: {category}**')
            st.write(f'Total de "Sim": {total}')
            st.bar_chart({'Sim': total, 'Não': len(category_responses[category]) - total})
    else:
        st.error('Não há perguntas definidas para esta faixa etária.')

if __name__ == '__main__':
    main()
