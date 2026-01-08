# A fun example demonstrating various concepts involved in Large Language Model finetuning
Hackathon for efficient fine tuning of LLMs designed for HSF scientific computing workshop

## Setup Instructions

*use python3

python -m venv llm_sft

source llm_sft/bin/activate

pip install --upgrade pip

pip install -U torch transformers peft bitsandbytes trl datasets

pip install ipykernel

python -m ipykernel install --user --name=llm_sft --display-name "Python 3 (llm_sft)"

pip install ipywidgets
