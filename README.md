# 🏥 Health Insurance Premium Predictor

This project is a machine learning application designed to predict health insurance premiums based on user inputs. It features a Random Forest Regressor model, a FastAPI backend for API endpoints, and a simple, interactive frontend built with Streamlit.

The entire application is containerized using Docker for easy deployment and scalability.

***

## ✨ Key Features

-   **Prediction API**: A robust backend built with **FastAPI** that serves the machine learning model.
-   **Interactive UI**: A user-friendly frontend created with **Streamlit** where users can input their details and get an instant premium prediction.
-   **Machine Learning Model**: A **Random Forest Regressor** trained on the "US Health Insurance Dataset" to predict insurance costs.
-   **Containerized**: Fully containerized with **Docker**, allowing for consistent and isolated deployment.
-   **Clean Architecture**: The project follows a clear and organized structure, separating the model training, prediction logic, API, and frontend.

***

## 🛠️ Technology Stack

-   **Backend**: FastAPI, Pydantic
-   **Frontend**: Streamlit
-   **ML/Data Science**: Scikit-learn, Pandas, NumPy
-   **Deployment**: Docker

***

## 🚀 How to Run This Project

You can run this project either locally using a virtual environment or with Docker.

### Method 1: Running with Docker (Recommended)

This is the easiest way to get the application running.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/damaleparas/premium_predictor.git](https://github.com/damaleparas/premium_predictor.git)
    cd premium_predictor
    ```

2.  **Build the Docker image:**
    ```bash
    docker build -t insurance-predictor-app .
    ```

3.  **Run the Docker container:**
    This command will start both the FastAPI backend and the Streamlit frontend.
    ```bash
    docker run -p 8501:8501 -p 8000:8000 insurance-predictor-app
    ```

4.  **Access the applications:**
    * **Streamlit Frontend**: Open your browser and go to `http://localhost:8501`
    * **FastAPI Backend Docs**: Open your browser and go to `http://localhost:8000/docs`

### Method 2: Running Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/damaleparas/premium_predictor.git](https://github.com/damaleparas/premium_predictor.git)
    cd premium_predictor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv myenv
    myenv\Scripts\activate

    # For macOS/Linux
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the applications:**
    You will need two separate terminals for this.

    * **Terminal 1: Start the FastAPI Backend**
        ```bash
        uvicorn main:app --host 0.0.0.0 --port 8000
        ```

    * **Terminal 2: Start the Streamlit Frontend**
        ```bash
        streamlit run frontend.py
        ```

5.  **Access the applications:**
    * **Streamlit Frontend**: Open your browser and go to `http://localhost:8501`
    * **FastAPI Backend Docs**: Open your browser and go to `http://localhost:8000/docs`

***

## 📂 Project Structure

The repository is organized to separate concerns, making it easy to navigate and maintain.
