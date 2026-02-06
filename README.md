[English](README.md) | [中文](_README_CN.md)

# AI_Blog

A Quarto-based technical blog showcasing AI/ML projects, tutorials, and interactive applications. This project serves as both a portfolio and educational resource for AI enthusiasts and developers.

**Live Site:** [https://jcwinning.github.io/LandingPage/](https://jcwinning.github.io/LandingPage/)



## Overview

AI_Blog is a static website built with [Quarto](https://quarto.org/) that features:

- **10+ AI/ML Project Tutorials** - Comprehensive guides on OpenRouter API, RAG implementation, AI chat applications, and more
- **Interactive Code Examples** - Executable Python and R code blocks with real-time demonstrations
- **Bilingual Content** - English and Chinese support throughout
- **Data Visualization** - Interactive dashboards and charts using Plotly and Streamlit
- **Professional Portfolio** - CV/resume page showcasing technical expertise

## Featured Projects

| Project | Description | Tech Stack |
|---------|-------------|------------|
| [OpenRouter Tutorial](posts/openrouter/) | Comprehensive guide to OpenRouter API for multi-model AI access | Python, OpenAI SDK |
| [RAG Implementation](posts/RAG/) | Retrieval-Augmented Generation in R & Python | LlamaIndex, ChromaDB, DuckDB |
| [AI Chat App](posts/AI-Chat/) | Multilingual multi-model chat application | Streamlit, OpenRouter |
| [GDP Dashboard](posts/gdp-trend/) | Interactive GDP trends with AI-powered SQL | Streamlit, DuckDB, Plotly |
| [LLM Summary](posts/llm-summary/) | Multi-platform AI summarization tool | OpenAI, ModelScope |
| [YOLO Object Detection](posts/yolo-app/) | Real-time object detection application | YOLO11, OpenCV |
| [Weather Visualization](posts/weather-trend/) | Weather data analysis and trending | Pandas, Plotly |
| [Shop Map Manager](posts/shop-map-manager/) | Shop location management system | Streamlit, Folium |

## Tech Stack

### Core Framework
- **Quarto** - Scientific publishing system for creating websites from Markdown

### AI/ML
- **OpenRouter API** - Unified API for multiple AI models
- **OpenAI API** - GPT models and embeddings
- **LangChain** - LLM application framework
- **LlamaIndex** - Data framework for LLM applications
- **ChromaDB** - Vector database for embeddings
- **DuckDB** - In-memory SQL database with vector search
- **Whisper (MLX)** - Speech-to-text transcription
- **YOLO11** - Object detection models

### Data & Visualization
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations
- **Streamlit** - Web application framework
- **wbgapi** - World Bank API

### Languages
- **Python** - Primary implementation language
- **R** - Statistical computing and graphics
- **Markdown** - Content authoring
- **CSS** - Custom styling

## Getting Started

### Prerequisites

1. **Quarto CLI** - Install from [quarto.org](https://quarto.org/docs/get-started/)
2. **Python 3.12+** - For code examples and AI implementations
3. **R 4.0+** (optional) - For R-based posts

### Installation

```bash
# Clone the repository
git clone https://github.com/jcwinning/AI_Blog.git
cd AI_Blog

# Install Python dependencies (example for OpenRouter post)
pip install openai python-dotenv pandas IPython panel

# Install R packages (optional, for R-based posts)
# Run in R console:
install.packages(c("ragnar", "ellmer", "reticulate", "rvest", "dotenv"))
```

### Configuration

Create a `.env` file in the project root for API keys:

```bash
OPENROUTER_API_KEY=your_key_here
MODELSCOPE_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```

### Running Locally

```bash
# Preview the site locally
quarto preview

# Or render to docs folder
quarto render
```

Access the site at `http://localhost:4000`

## Project Structure

```
AI_Blog/
├── _quarto.yml          # Main Quarto configuration
├── index.qmd            # Homepage
├── posts.qmd            # Blog listing page
├── cv.qmd               # Resume/CV page
├── styles.css           # Custom CSS styling
├── posts/               # Blog posts directory
│   ├── openrouter/      # OpenRouter API tutorial
│   ├── RAG/             # RAG implementation
│   ├── AI-Chat/         # AI chat application
│   ├── gdp-trend/       # GDP dashboard
│   └── ...
├── markdown_docs/       # Documentation reference
├── docs/                # Generated website output
├── _freeze/             # Computation cache
└── posts_files/         # Post assets
```

## Deployment

The site is deployed to GitHub Pages. To deploy:

```bash
# Render the site
quarto render

# Commit and push to GitHub
git add docs/
git commit -m "Update site"
git push
```


## Contributing

Contributions are welcome! To add a new blog post:

1. Create a new directory in `/posts/`
2. Add your `.qmd` or `.md` file with proper YAML frontmatter
3. Include any assets in a subdirectory
4. Update the navigation in `_quarto.yml` if needed
5. Render and test locally with `quarto preview`

## License

This project is open source and available under the MIT License.

## Author

**Tony D** - [GitHub](https://github.com/jcwinning)

## Acknowledgments

- [Quarto](https://quarto.org/) for the excellent publishing system
- The open-source AI/ML community for tools and libraries
- All contributors and supporters of this project
