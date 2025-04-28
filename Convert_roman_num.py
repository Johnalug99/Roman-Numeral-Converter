import streamlit as st

def roman_converter():
    st.title('Roman Numeral Converter')

    roman_num = {'D': 1000, 'M': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    question = st.text_input('Enter the Roman numeral you want to convert:')
    
    if question:
        question1 = question.upper()
        score = []
        try:
            for i in question1:
                score.append(roman_num[i])
            
            if len(score) >= 2 and score[0] < score[1]:
                number = score[1] - score[0]
            else:
                number = sum(score)

            st.success(f'The number is: {number}')
        except KeyError:
            st.error("Invalid Roman numeral. Please enter valid characters (D, M, C, L, X, V, I).")

roman_converter()
