# AI-Powered PDF Summarizer

## Overview

This project extracts text from PDF documents and generates concise summaries using a locally hosted AI model through Ollama.

## Features

* PDF text extraction
* AI-generated summaries
* Runs completely offline
* No paid APIs required
* Lightweight and beginner-friendly

## Tech Stack

* Python
* PyPDF
* Ollama
* Gemma 3 1B

## Installation

Install dependencies:

```bash
pip install pypdf ollama
```

Install Ollama:

https://ollama.com/download

Download model:

```bash
ollama run gemma3:1b
```

## Usage

Place a PDF file in the project folder.

Run:

```bash
python pdf_summary.py
```

The generated summary will be displayed in the terminal and saved to `summary.txt`.

## Project Workflow

PDF → Text Extraction → Ollama → AI Summary

## Author

Siddhi Shahi
