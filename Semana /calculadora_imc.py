import streamlit as st  

st.title("Calculadora de IMC")

st.sidebar.header("Parametros")
peso = st.sidebar.number_input("Peso (kg)", 30, 300, placeholder = "Ingresa tu peso en kilogramos")
estatura = st.sidebar.number_input("Estatura (cm)", 100, 250, placeholder = "Ingresa tu estatura en centímetros")

if st.button("Calcular IMC"):
    if estatura > 0:
        imc = peso / ((estatura / 100) ** 2)
        st.subheader(f"Tu IMC es: {imc:.2f}")

        if imc < 18.5:
            st.write("Categoría: Bajo peso")
        elif 18.5 <= imc < 24.9:
            st.write("Categoría: Peso normal")
        elif 25 <= imc < 29.9:
            st.write("Categoría: Sobrepeso")
        else:
            st.write("Categoría: Obesidad")
    else:
        st.write("Por favor, ingresa una estatura válida.")