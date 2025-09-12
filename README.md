# Vaccine Misinformation Chatbot

This project demonstrates fine-tuning a GPT-2 model using LoRA to **detect and correct vaccine misinformation centered around COVID-19**. The goal is to explore natural language processing and model fine-tuning while applying best practices for dataset handling and model deployment.

**Dataset Source / Credit:**  
This dataset was obtained from [Vax-Culture: A Dataset for Studying Vaccine Discourse on Twitter](https://github.com/mrzarei5/Vax-Culture) 


## Features

* Fine-tuned **GPT-2** on a dataset of \~6,300 vaccine misinformation examples.
* Generates **corrected responses** to misinformation claims.
* Simple **interactive demo** using Streamlit.
* Saves checkpoints and model outputs to **Google Drive** to handle limited GPU/session time.


## Setup

1. Clone the repository:

```bash
git clone <repo_url>
cd vaccine-misinformation-llm
```

2. Install dependencies:

```bash
python -m pip install streamlit transformers torch
```

3. Run the chatbot:

```bash
streamlit run app/streamlit_app.py
```

## Usage

Enter a **misinformation claim** in the input box, and the model will generate a **corrected response**.


## Notes

* I initially fine-tuned a LLaMA-based chatbot.Despite LLaMA initially showing better results, training was slow and exceeded Colab Free limits that i used. Without access to paid services or a strong GPU, I switched to GPT-2, which allowed me to train efficiently and practice fine-tuning and optimization with the ressources i had. 
* Results are **proof-of-concept**, demonstrating fine-tuning and NLP skills.
* I am **actively working on improving the model and the demo**, and updates will be pushed to the repository.


## Skills Demonstrated

* Python, Transformers, GPT-2 fine-tuning
* Dataset preprocessing and train/test split
* Model evaluation and inference
* Deployment via Streamlit and Git/GitHub usage





