<p align="center">
  <b>Senior MLOps Engineer at <a href="https://www.precision.ai/">Precision AI</a></b> · Calgary, Alberta<br>
  I take AI from vision to a live product in production, and I love teaching it along the way.
</p>

<p align="center">
  <a href="https://datlombardo.ca"><img alt="Website" src="https://img.shields.io/badge/Website-datlombardo.ca-FF6A1A?logoColor=white"></a>
  <a href="https://www.linkedin.com/in/michael-lombardo-78650a107/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-connect-0A66C2?logo=linkedin&logoColor=white"></a>
  <a href="https://ko-fi.com/datlombardo"><img alt="Support on Ko-fi" src="https://img.shields.io/badge/Ko--fi-support-FF5E5B?logo=ko-fi&logoColor=white"></a>
</p>

## What I do

I take AI from an idea to a product running in production, and own every step in between:

**Vision → data → model → production → monitoring**

- **Vision and research:** read the papers, prototype, and decide what is worth building (computer vision, vision-language models, LLMs, diffusion, agentic RAG systems).
- **Data:** design datasets, run large-scale annotation, and generate synthetic data (NVIDIA Omniverse) when real data is scarce.
- **Models:** train, fine-tune and evaluate with PyTorch Lightning, HuggingFace and vLLM, then shrink them with quantization, pruning and distillation for real-time and edge use.
- **Production:** MLflow-tracked training, CI/CD, Docker, Kubernetes and AWS, with REST and GraphQL APIs that serve models inside larger systems.
- **Live in the field:** monitor deployed models, close the loop with new data, and keep improving. At TerraSense that meant drone and sensor systems running ISR defense technology, with synthetic aperture radar research from raw data to mission management.
- **Teams:** Scrum master and mentor, leading Scrum and Nexus teams from planning to release.

Background: M.Sc. Computer Science (Ontario Tech, 4.0 GPA), thesis *Parsing Genetic Models*. Former sessional lecturer: three CS courses and 350+ students.

## Open source

**[Precision AI](https://github.com/Precision-AI-Inc)**: public releases from my work there, also on [Hugging Face](https://huggingface.co/precisionaiinc).

| Repo | What it is | Links |
|---|---|---|
| [agrieval](https://github.com/Precision-AI-Inc/agrieval) | Agricultural embedding evaluation API | [PyPI](https://pypi.org/project/precisionai-agrieval/) |
| [agritune](https://github.com/Precision-AI-Inc/agritune) | Train and evaluate segmentation decoders on frozen ViT encoder features | [PyPI](https://pypi.org/project/precisionai-agritune/) |
| [agriemb](https://github.com/Precision-AI-Inc/agriemb) | Examples for the Precision AI embedding public release | - |
| [agristress-utils](https://github.com/Precision-AI-Inc/agristress-utils) | Utilities for the AgriStress dataset | [PyPI](https://pypi.org/project/precisionai-agristress-utils/) · [AgriStress-500](https://huggingface.co/datasets/precisionaiinc/AgriStress-500) |
| [magnidata](https://github.com/Precision-AI-Inc/magnidata) | Data visualization tool | [Live demo](https://huggingface.co/spaces/precisionaiinc/magnidata) |
| [pace](https://github.com/Precision-AI-Inc/pace) | Experiment logging and forecaster | [PyPI](https://pypi.org/project/precisionai-pace/) |

**[Lombo Forge](https://github.com/Lombo-Forge)**: small, tested companion apps for self-hosted Jellyfin media servers.

| Repo | What it is |
|---|---|
| [lombo-shrink](https://github.com/Lombo-Forge/lombo-shrink) | Re-encode a library to H.265 on your PC's GPU, then swap files in safely |
| [lombo-tier](https://github.com/Lombo-Forge/lombo-tier) | Move titles between SSD and HDD based on what people watch |
| [lombo-nap](https://github.com/Lombo-Forge/lombo-nap) | Asks "Still watching?" and shows what woke your sleeping disks |
| [lombo-nudge](https://github.com/Lombo-Forge/lombo-nudge) | Finds approved Seerr requests that never arrived, and says why |
| [lombo-vault](https://github.com/Lombo-Forge/lombo-vault) | Encrypted config backups with a restore drill |
| [lombo-farewell](https://github.com/Lombo-Forge/lombo-farewell) | Leaving soon collection for titles scheduled for deletion |
| [lombo-visa](https://github.com/Lombo-Forge/lombo-visa) | Blocks new sign-ins from abroad, with travel windows |
| [jellyfin-plugin-lomboshelf](https://github.com/Lombo-Forge/jellyfin-plugin-lomboshelf) | Streaming-style Home shelf, genre rows and theme for Jellyfin |

More, with language breakdowns, on the [Development page](https://datlombardo.ca/development.html).

## Tech

**ML & AI**<br>
![Python](https://img.shields.io/badge/Python-3572A5?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![PyTorch Lightning](https://img.shields.io/badge/PyTorch_Lightning-792EE5?logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?logo=huggingface&logoColor=black)
![vLLM](https://img.shields.io/badge/vLLM-30A2FF)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![ONNX](https://img.shields.io/badge/ONNX-005CED?logo=onnx&logoColor=white)
![TensorRT](https://img.shields.io/badge/TensorRT-76B900?logo=nvidia&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?logo=nvidia&logoColor=white)
![NVIDIA Omniverse](https://img.shields.io/badge/NVIDIA_Omniverse-76B900?logo=nvidia&logoColor=white)
![Transformers](https://img.shields.io/badge/Transformers-FFD21E?logo=huggingface&logoColor=black)
![PEFT](https://img.shields.io/badge/PEFT-FFD21E?logo=huggingface&logoColor=black)
![TRL](https://img.shields.io/badge/TRL-FFD21E?logo=huggingface&logoColor=black)
![Accelerate](https://img.shields.io/badge/Accelerate-FFD21E?logo=huggingface&logoColor=black)
![Sentence Transformers](https://img.shields.io/badge/Sentence_Transformers-FFD21E?logo=huggingface&logoColor=black)
![timm](https://img.shields.io/badge/timm-FFD21E?logo=huggingface&logoColor=black)
![torchvision](https://img.shields.io/badge/torchvision-EE4C2C?logo=pytorch&logoColor=white)
![Detectron2](https://img.shields.io/badge/Detectron2-0467DF?logo=meta&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![ONNX Runtime](https://img.shields.io/badge/ONNX_Runtime-005CED?logo=onnx&logoColor=white)
![NVIDIA DALI](https://img.shields.io/badge/NVIDIA_DALI-76B900?logo=nvidia&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?logo=ollama&logoColor=white)
![Hydra](https://img.shields.io/badge/Hydra-89B8CD)
![Albumentations](https://img.shields.io/badge/Albumentations-CC0000)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)

**Agentic AI**<br>
![Claude](https://img.shields.io/badge/Claude-D97757?logo=claude&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-412991?logo=openai&logoColor=white)
![Grok](https://img.shields.io/badge/Grok-000000?logo=x&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?logo=claude&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-412991?logo=openai&logoColor=white)
![OpenAI API](https://img.shields.io/badge/OpenAI_API-412991?logo=openai&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-000000?logo=modelcontextprotocol&logoColor=white)

**MLOps & Orchestration**<br>
![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-945DD6?logo=dvc&logoColor=white)
![HashiCorp Nomad](https://img.shields.io/badge/HashiCorp_Nomad-00CA8E?logo=nomad&logoColor=black)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![HashiCorp Vault](https://img.shields.io/badge/HashiCorp_Vault-FFEC6E?logo=vault&logoColor=black)
![HashiCorp Consul](https://img.shields.io/badge/HashiCorp_Consul-F24C53?logo=consul&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?logo=docker&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?logo=caddy&logoColor=white)
![Weights & Biases](https://img.shields.io/badge/Weights_%26_Biases-FFBE00?logo=weightsandbiases&logoColor=black)
![Neptune](https://img.shields.io/badge/Neptune-4C5BF5)
![Comet](https://img.shields.io/badge/Comet-262C3E)
![TensorBoard](https://img.shields.io/badge/TensorBoard-FF6F00?logo=tensorflow&logoColor=white)

**Cloud & Delivery**<br>
![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white)
![CodeArtifact](https://img.shields.io/badge/CodeArtifact-232F3E?logo=amazonwebservices&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![REST](https://img.shields.io/badge/REST_APIs-005571)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?logo=graphql&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon_S3-569A31?logo=amazons3&logoColor=white)
![Amazon ECR](https://img.shields.io/badge/Amazon_ECR-232F3E?logo=amazonwebservices&logoColor=white)
![boto3](https://img.shields.io/badge/boto3-232F3E?logo=amazonwebservices&logoColor=white)
![PyPI](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-6BA81E)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-010101)
![JWT](https://img.shields.io/badge/JWT-000000?logo=jsonwebtokens&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=black)
![Apache Arrow](https://img.shields.io/badge/Apache_Arrow-0E0C30)
![Apache Parquet](https://img.shields.io/badge/Apache_Parquet-50ABF1?logo=apacheparquet&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-000000?logo=threedotjs&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![Vitest](https://img.shields.io/badge/Vitest-6E9F18?logo=vitest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33)
![Ruff](https://img.shields.io/badge/Ruff-D7FF64?logo=ruff&logoColor=black)
![Pyright](https://img.shields.io/badge/Pyright-3776AB)
![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?logo=precommit&logoColor=black)
![Sphinx](https://img.shields.io/badge/Sphinx-0A507A)

## Support

If something I built saved you time, you can [buy me a coffee on Ko-fi](https://ko-fi.com/datlombardo).
