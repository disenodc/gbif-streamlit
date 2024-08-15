

# BotGBIF🤖 - Biodiversity Chatbot with LLM and GBIF API
![Botgbif_header](https://raw.githubusercontent.com/disenodc/gbif-streamlit/main/repo-header.jpg)

This project implements a chatbot that allows users to make biodiversity-related queries using an LLM (Large Language Model) to interact with the GBIF (Global Biodiversity Information Facility) API. The application is built with Python and Streamlit, providing a simple and effective interface for exploring biodiversity data.


## Authors
Authors belong to Centro para el Estudio de Sistemas Marinos (Consejo Nacional de Investigaciones Científicas y Técnicas [CESIMAR-CONICET](https://cesimar.conicet.gov.ar/) - Boulevard Brown 2915 - Puerto Madryn (U9120ACD) - Chubut - Argentina

- Ph.D.: Marcos Zárate
- BCS.: Dario Ceballos 
- BCS.: Gustavo Nuñez 


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Project Structure](#project-structure)
5. [Project Pipeline](#project-pipeline)
6. [Running the Application](#running-the-application)
7. [Future Enhancements](#future-enhancements)
8. [License](#license)

## Prerequisites

Before starting, make sure you have the following components installed:

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/) for managing Python packages
- An account on [OpenAI](https://openai.com/) to access the GPT API
- Access to the [GBIF API](https://www.gbif.org/developer/summary) (API key is not required)

## Installation

Clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/gustavomarcelonunez/gbif-streamlit.git
cd botgbif
pip install -r requirements.txt
```

## Configuration

To configure the required API keys, follow these steps:

1. Create a `.env` file in the root directory of the project.
2. Add the following environment variables:
   ```plaintext
   OPENAI_API_KEY=your_openai_key
   GBIF_API_KEY=your_gbif_key (if required)
   ```

## Project Structure

The main structure of the project is as follows:

```plaintext
├── app.py              # Main Streamlit application file
├── requirements.txt    # Project dependencies list
├── disclaimer_popup.py # Project disclaimer demo except
├── utils_gbif.py       # Connection to the GBIF API
├── utils_open_ai.py    # Connection to the OPENAI API
└── README.md           # This README file

```

## Project Pipeline

![Project Pipeline Diagram]([https://raw.githubusercontent.com/disenodc/gbif-streamlit/main/botgbif.png](https://raw.githubusercontent.com/disenodc/gbif-streamlit/main/gbif-bot.png))

1. **User Query Input:**
   - The user enters a biodiversity-related query in the Streamlit interface.

2. **Querying the GBIF API:**
   - The user's query is sent to the GBIF API, and returns metadata that meet the search criteria.

3. **Displaying Results:**
   - The processed data from the GBIF API is presented to the user through the Streamlit interface.

4. **Asking about datasets metadata:**
   - The user can ask in natural language to the BotGBIF about the datasets related through the Streamlit interface.

5. **Asking about a data:**
   - The user select one specific dataset to ask in natural language for information about the dataset content through the Streamlit interface.


## Running the Application

To start the application, run the following command in your terminal:

```bash
streamlit run app.py
```

This will open a browser window with the BotGBIF interface, where you can begin making biodiversity-related queries.

## Future Enhancements

Some potential improvements for this project include:

- **Advanced Conversation Management:** Implement context tracking for multi-turn queries.
- **Result Filtering:** Add filtering options by location, time, taxonomy, etc.
- **Improved Interface:** Enhance the result presentation with interactive charts or maps.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
