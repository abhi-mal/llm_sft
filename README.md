# A hands-on fine-tuning workflow utilizing LoRA and Quantization to demonstrate LLM steerability and output control
Hackathon for efficient fine tuning of LLMs designed for HSF scientific computing workshop.

## Overview
The goal of this hackathon is to demystify LLMs using parameter-efficient fine-tuning (PEFT), empowering participants to apply these techniques in their own research. The exercises guide users through:
* Loading pre-trained models.
* Preparing datasets for instruction tuning.
* Implementing LoRA/QLoRA.

## Setup Instructions (use python3)

python -m venv llm_sft

source llm_sft/bin/activate

pip install --upgrade pip

pip install -U torch transformers peft bitsandbytes trl datasets

pip install ipykernel

python -m ipykernel install --user --name=llm_sft --display-name "Python 3 (llm_sft)"

pip install ipywidgets

## Resources 

The file ''hackathon_details.pdf'' contains the introductory lecture and challenge walkthrough.

**Designed and maintained by:** Abhishikth Mallampalli
