# BioMedical AI App

This project is a question-answering application that uses a Large Language Model (LLM) to answer biomedical questions. It leverages the PubMed database to find relevant scientific articles and generates answers based on their content.

## How it Works

The application is built using the Haystack AI framework to create a Retrieval-Augmented Generation (RAG) pipeline. Here's how it processes a user's question:

1.  **Keyword Generation:** The user's question is first passed to a Mistral-7B model to extract relevant keywords.
2.  **PubMed Search:** These keywords are then used to search for relevant articles on PubMed using the `pymed` library.
3.  **Answer Generation:** The content of the retrieved articles, along with the original question, is passed back to the Mistral-7B model, which generates a comprehensive answer.
4.  **User Interface:** The application is served through a Gradio interface, which is embedded within a Streamlit application.

## Technology Stack

*   **AI/LLM Framework:** [Haystack](https://haystack.deepset.ai/)
*   **LLM:** [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
*   **PubMed API:** [pymed](https://pypi.org/project/pymed/)
*   **Web Framework:** [Gradio](https://www.gradio.app/) & [Streamlit](https://streamlit.io/)
*   **Dependencies:** `transformers`, `torch`, `python-dotenv`

## Setup and Usage

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    Create a `.env` file in the root of the project and add your Hugging Face API key:
    ```
    HUGGINGFACE_API_KEY="your-hugging-face-api-key"
    ```

5.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

    This will start the Streamlit application, which will, in turn, launch the Gradio interface. You can access the application in your web browser at the URL provided by Streamlit (usually `http://localhost:8501`).
