# Local Llama 3.2 Docker Stack 🦙🐳

A containerized, ready-to-use Python environment for running Meta's Llama 3.2 model locally without polluting your host machine.

This project uses **Docker Compose** to spin up an isolated AI server (via Ollama) alongside a custom Python application. They communicate securely over a private Docker bridge network.

## Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* (Optional) NVIDIA GPU drivers configured for Docker if you want hardware acceleration.

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/llama-docker-stack.git](https://github.com/YOUR_USERNAME/llama-docker-stack.git)
   cd llama-docker-stack