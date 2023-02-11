import streamlit as st
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

def main():
    st.set_page_config(page_title="Mi App Streamlit", page_icon=":guardsman:", layout="wide")
    
    st.title("Mi Aplicación de Machine Learning")

    # Create a menu with different pages
    menu = ["Quién Soy Yo", "Dataframe", "Modelo de Clasificación"]
    choice = st.sidebar.selectbox("Selecciona una pestaña", menu)
    
    if choice == "Quién Soy Yo":
        st.subheader("Quién Soy Yo")
        st.markdown("Hola, soy un modelo de lenguaje entrenado por OpenAI.")
    
    elif choice == "Dataframe":
        st.subheader("Dataframe")
        n = 10
        df = pd.DataFrame(data=np.random.randn(n, 11), columns=["var_" + str(i) for i in range(1, 12)])
        df["var_11"] = np.random.randint(0, 2, size=n)
        st.dataframe(df)
    
    elif choice == "Modelo de Clasificación":
        st.subheader("Modelo de Clasificación")
        st.markdown("A continuación, se muestra un ejemplo de un modelo de clasificación utilizando el algoritmo Naive Bayes.")
        smoothing = st.number_input("Ingrese el valor de suavizamiento (alpha)", 0.1, 10.0, step=0.1, key="smoothing")
        n = 10
        df = pd.DataFrame(data=np.random.randn(n, 11), columns=["var_" + str(i) for i in range(1, 12)])
        df["var_11"] = np.random.randint(0, 2, size=n)
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        model = GaussianNB(var_smoothing=smoothing)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        auc = roc_auc_score(y_test, y_pred)
        st.write("El AUC del modelo es:", auc)

if __name__ == '__main__':
    main()
