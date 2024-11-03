# Isulion Prompt Generator

Transform your creative workflow with advanced prompt generation technology.

![Showcase](https://github.com/user-attachments/assets/56d69f0a-d840-42de-93ef-5378293263ee)

## Overview

Isulion Prompt Generator introduces a new way to create, refine, and enhance your image generation prompts. With its intuitive interface and powerful capabilities, you can craft precise, detailed prompts for any creative vision.

## Installation

### Quick Start

Use [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager), got to "Custome Nodes Manager" and search  "Isulion" !

### Old install

```bash
cd "your_ComfyUI_install_dir"
cd custom_nodes
git clone https://github.com/Isulion/ComfyUI_Isulion
```

--------------

## Available Nodes

### Core Generators

- Prompt  ✨ - Main prompt generation node
- Ollama  🤖 - LLM-based text generation
- Mega Prompt 🎯 - Advanced multi-theme prompt generator

## 🎯 Mega Prompt Generator 🎯

The Mega Prompt Generator is an advanced node that combines multiple themes and generation capabilities:

### Available Themes

- Essential Realistic: Professional photography with real-world subjects
- Futuristic Sci-Fi: Advanced technology and space-age scenes
- Studio Cinema: Movie and superhero character compositions
- Enchanted Fantasy: Magical realms and mythical characters
- Fusion Cute Animals: Adorable hybrid creature combinations
- Animation Cartoon: Classic animated character styles
- Anime: Japanese animation inspired artwork
- Architectural: Sophisticated building and structural designs
- Abstract: Pure geometric and non-representational compositions
- Culinary: Professional food and beverage photography
- Spaces Interior: Interior design and architectural spaces
- Dimension 3D: Three-dimensional digital artwork
- Ethereal Halloween: Spooky and atmospheric horror themes
- Lifestyle Instagram: Professional social media photography
- Chimera Strange Animals: Unique hybrid creatures with distinctive head-body combinations
- Metropolis Futuristic City: Advanced cityscape and urban environments
- Pixar Animation: 3D animation in the style of Pixar
- Binet Surreal: Anthropomorphic portraits inspired by Sylvain Binet
- Vintage Anthropomorphic: Classic anthropomorphic characters in vintage settings
- Dynamic Random: Randomly selects and combines various themes

The Mega Prompt Generator provides both a combined prompt and individual components, allowing for maximum flexibility in your workflows.

--------------

### Specific Nodes

#### Animal Related

- Animal 🦁 - General animal selection
- Cute Animal 🐱 - Cute and baby animal selection
- Animal Behavior 🦊 - Animal actions and poses

#### Character Elements

- Character Profession 👨‍🍳 - Occupations and roles
- Fantasy Race 🧝‍♂️ - Fantasy species and races
- Clothing Style 👔 - Outfit and fashion descriptions

#### Scene Composition

- Action ⚔️ - Dynamic poses and activities
- Scene Composition 🎬 - Camera angles and shot types

#### Environment

- Habitat 🌲 - Natural environments and landscapes
- Weather ⛅ - Weather conditions
- Time of Day 🌅 - Time and lighting conditions

#### Style and Mood

- Art Style 🎨 - Artistic styles and techniques
- Emotion 😊 - Emotional characteristics

#### Fantasy & Magic

- Magical Effect ✨ - Spell effects and magical phenomena
- Mythical Location 🏰 - Fantasy environments
- Artifact 📿 - Magical items and artifacts

#### Sci-Fi Elements

- Tech 🤖 - Futuristic technology descriptions
- Alien World 🪐 - Exotic planet environments
- Spacecraft 🚀 - Space vehicle descriptions

#### Enhancement Nodes

- Style Mixer 🎨 - Combines multiple art styles with adjustable blend modes
- Prompt Enhancer 📝 - Adds detail, mood, composition, lighting, or color enhancements
- Negative Prompt ⛔ - Creates matching negative prompts with adjustable strictness

--------------

## FLUX Worflow Examples

### Basic MegaPrompt Workflow

![IsulionFLUX_00468_](https://github.com/user-attachments/assets/91e7db26-9315-45d3-8461-83f0bba457b1)

### Chimera (with Ollama) Work

![IsulionFlux_00492_](https://github.com/user-attachments/assets/0e097a70-3821-4440-94d9-589703ab7ad1)

### MegaPrompt + Ollama + LoRa Workflow

![IsulionFLUX_00484_](https://github.com/user-attachments/assets/6cbc3ea8-650b-44b3-9a59-a3476a7e513c)

## Ollama Requirements

- Ollama_generator node installed in ComfyUI

### Environment Variables

- OLLAMA_KEEP_ALIVE: 0
- OLLAMA_ORIGINS: *
