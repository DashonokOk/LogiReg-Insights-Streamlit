import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# Функция для выполнения логистической регрессии
def perform_logistic_regression(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    lr = LogisticRegression()
    lr.fit(X_scaled, y)
    
    feature_importance = {col: coef for col, coef in zip(X.columns, lr.coef_[0])}
    return feature_importance, lr.intercept_[0]

# Функция для построения scatter plot
def plot_scatter(df, x_col, y_col, color_col):
    fig, ax = plt.subplots()
    scatter = ax.scatter(df[x_col], df[y_col], c=df[color_col], cmap='viridis')
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.title(f'График рассеяния {x_col} vs {y_col}', fontsize=14)
    plt.colorbar(scatter, label=color_col)
    st.pyplot(fig)

# Основная функция приложения
def main():
    st.title("LogiReg Insights")
    
    st.write("Загрузите ваш CSV файл:")
    uploaded_file = st.file_uploader("Загрузить файл", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.write("Превью данных:")
        st.dataframe(df.head())
        
        target_column = st.selectbox("Выберите целевой столбец", df.columns)
        
        if st.button("Выполнить логистическую регрессию"):
            feature_importance, intercept = perform_logistic_regression(df, target_column)
            st.write("Веса признаков:")
            st.write(feature_importance)
            st.write(f"Свободный член: {intercept}")
        
        if len(df.columns) >= 2:
            st.write("Параметры для построения графика рассеяния:")
            x_col = st.selectbox("Выберите столбец для оси X", df.columns)
            y_col = st.selectbox("Выберите столбец для оси Y", df.columns)
            color_col = st.selectbox("Выберите столбец для цветовой дифференциации", df.columns)
            
            if st.button("Построить график рассеяния"):
                plot_scatter(df, x_col, y_col, color_col)

if __name__ == "__main__":
    main()