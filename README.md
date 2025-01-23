# LogiReg-Insights-Streamlit

## Описание

LogiReg Insights - это веб-приложение на основе Streamlit, которое позволяет пользователям загружать файлы CSV, выполнять логистическую регрессию и строить scatter plot.

## Установка

1. Клонируйте репозиторий:

   ```sh
   git clone <repository-url>
   cd LogiReg_Insights
   
## Установите зависимости:
pip install -r requirements.txt

## Запустите приложение:
streamlit run app.py

## Использование
Загрузите файл CSV.
Выберите целевой столбец для логистической регрессии.
Нажмите кнопку "Perform Logistic Regression", чтобы получить результаты регрессии.
Выберите два столбца для построения scatter plot и нажмите кнопку "Plot Scatter".


### Как запустить приложение

1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Создайте виртуальное окружение и активируйте его:

   ```sh
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   venv\Scripts\activate     # Для Windows