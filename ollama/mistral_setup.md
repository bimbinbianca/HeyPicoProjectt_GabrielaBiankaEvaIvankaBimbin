# Local LLM Setup (Mistral Model)
This project uses Mistral via Ollama as the local LLM backend
Make sure you have Ollama installed and the Mistral model downloaded before running the project.

1. Instal Ollama -> https://ollama.com/download
2. Pull the Mistral model:
```bash
ollama pull mistral
```
3. Run the model locally:
```bash
ollama run mistral
```
4. Verify it’s working by visiting http://localhost:11434
   See a confirmation that the Ollama server is running
