import streamlit as st

st.set_page_config(page_title="Laboratorio Elettronica", page_icon="⚡")

st.title("⚡ Calcolatore Resistenze Equivalenti")
st.write("Inserisci i valori delle resistenze per calcolare la loro combinazione.")

# Layout a due colonne
col1, col2 = st.columns(2)

with col1:
    st.header("Input Dati")
    r1 = st.number_input("Resistenza R1 [Ω]", min_value=0.1, value=100.0)
    r2 = st.number_input("Resistenza R2 [Ω]", min_value=0.1, value=220.0)
    tipo = st.radio("Tipo di collegamento:", ("Serie", "Parallelo"))

# Calcolo logico
if tipo == "Serie":
    r_eq = r1 + r2
    formula = r"R_{eq} = R_1 + R_2"
else:
    r_eq = (r1 * r2) / (r1 + r2)
    formula = r"R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2}"

with col2:
    st.header("Risultato")
    st.metric(label="Resistenza Equivalente", value=f"{r_eq:.2f} Ω")
    st.latex(formula)

# Nota didattica automatica
st.divider()
if tipo == "Parallelo":
    st.info("💡 Nota: In parallelo,d la $R_{eq}$ è sempre minore della resistenza più piccola!")