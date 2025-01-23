import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Scatter plot of {x_col} vs {y_col}')
    plt.colorbar(scatter, label=color_col)
    st.pyplot(fig)

# Основная функция приложения
def main():
    st.title("LogiReg Insights")
    
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.write("Data Preview:")
        st.dataframe(df.head())
        
        target_column = st.selectbox("Select the target column", df.columns)
        
        if st.button("Perform Logistic Regression"):
            feature_importance, intercept = perform_logistic_regression(df, target_column)
            st.write("Feature Importance (Weights):")
            st.write(feature_importance)
            st.write(f"Intercept: {intercept}")
        
        if len(df.columns) >= 2:
            st.write("Scatter Plot Options:")
            x_col = st.selectbox("Select X-axis column", df.columns)
            y_col = st.selectbox("Select Y-axis column", df.columns)
            color_col = st.selectbox("Select Color column", df.columns)
            
            if st.button("Plot Scatter"):
                plot_scatter(df, x_col, y_col, color_col)

if __name__ == "__main__":
    main()