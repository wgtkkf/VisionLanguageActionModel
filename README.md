# UR5 + Llama 3.2 Vision: VLA Integration

This repository contains the foundational Docker environments for integrating a Universal Robots UR5 (running in Gazebo) with **Llama 3.2 Vision**. 

The ultimate goal of this project is to create a Vision-Language-Action (VLA) pipeline where Llama 3.2 acts as a high-level cognitive planner—processing visual streams from the simulated environment and user text prompts to orchestrate robotic actions.

## 🏗️ System Architecture (Current State)

Because the ROS 2 simulation and the AI model have vastly different system requirements, they are separated into two distinct Docker containers that communicate over a shared host network.

| Component | Container | Description |
| :--- | :--- | :--- |
| **The Body** | `Dockerfile.ur5` | Runs ROS 2 Humble, the Gazebo simulation, MoveIt 2, and the UR5 hardware interfaces. This container hosts the physical environment and the camera sensors. |
| **The Brain** | `Dockerfile.llama` | Hosts the Llama 3.2 Vision model, exposing a local inference API to process multimodal inputs (images + text). |
| **The Bridge** | *(In Development)* | A future translation layer that will sit between the Brain and the Body. It will be responsible for sending Gazebo camera frames to Llama 3.2 and parsing the model's reasoning into executable ROS 2/MoveIt commands. |

## 🛠️ Prerequisites

* Ubuntu 22.04+ (Host Machine)
* NVIDIA GPU (e.g., RTX 3060 Ti) with proprietary drivers installed
* [Docker Engine](https://docs.docker.com/engine/install/) & [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
* At least 32GB System RAM

## 🚀 Quick Start Guide

### 1. Build the Docker Images
Open your terminal in this directory and build the two isolated environments:

```bash
# Build the UR5 Gazebo Simulation Image
docker build -f Dockerfile.ur5 -t ur5:1.0 .

# Build the Llama 3.2 Vision Inference Image
docker build -f Dockerfile.llama -t llama-app:1.0 .