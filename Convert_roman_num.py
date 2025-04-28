import streamlit as st
def roman_converter():
    st.title('Roman Numeral Converter')
    roman_num = {'D':1000, 'M':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    while True:
     question = st.text_input('What roman numeral are you converting? :')
     question1 = question.upper()
     score = []
     for i in question1:
        score.append(roman_num[i])
        if score[0] < score[1]:
            number = score[1] - score[0]
            print('The number is{:3d}'.format(number))
        else:
            number = sum(score)
            print('The number is {:3d}'.format(number))
        another = input('Do you want to play again? (Yes or No)').lower()  
        if another != 'yes':
        ('Goodbye')
        break
roman_converter()