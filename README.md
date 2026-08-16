# AI-Powered PDF Summarizer

## Overview

AI-Powered PDF Summarizer is a Python-based application that automatically extracts text from PDF documents and generates concise, context-aware summaries using a locally hosted Large Language Model (LLM) through Ollama. The project is designed to run entirely offline, ensuring privacy, low operational costs, and ease of deployment.

## Features

* Automated PDF text extraction
* AI-generated document summarization
* Fully offline execution using local LLMs
* No external APIs or cloud services required
* Lightweight and easy to deploy
* Summary export to text files
* Beginner-friendly architecture with practical AI integration

## Tech Stack

### Programming Language

* Python

### Libraries & Tools

* PyPDF
* Ollama

### AI Model

* Gemma 3 1

## Project Architecture

PDF Document
→ Text Extraction (PyPDF)
→ Prompt Processing
→ Ollama LLM Inference
→ AI-Generated Summary
→ Output to Terminal & Text File

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ai-pdf-summarizer
```

### 2. Install Dependencies

```bash
pip install pypdf ollama
```

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com/download

### 4. Download the Language Model

```bash
ollama run gemma3:1b
```

## Usage

1. Place the PDF file inside the project directory.
2. Execute the application:

```bash
python pdf_summary.py
```

3. The generated summary will:

   * Display in the terminal
   * Be saved automatically to `summary.txt`

## Use Cases

* Academic paper summarization
* Research document analysis
* Report summarization
* Quick document review
* Knowledge extraction from lengthy PDFs

## Future Enhancements

* Multi-document summarization
* Custom summary length controls
* PDF upload interface using Streamlit
* Support for multiple LLMs
* Keyword and topic extraction
* Question-answering over PDF documents

## Author

Shambhavi Shahi

Computer Science Engineering Student 
