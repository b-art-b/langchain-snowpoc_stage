# langchain-snowpoc

> **NOTE**: This is just a PoC, not production-ready and covers just a few use cases.

This is a PoC of how can Cortex be used with Langchain.
The code was updated from the original code base to fit
new signatures of Snowflake functions and LangChain 0.2.

It shows how easy it is to integrate Langchain, Snowflake
Cortex and data in Stages.

## Setup

```bash
conda env create
```

To use the environment you have to activate it. Feel free
to check the [documentation](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html).

## Jupyter Lab Example

Just run `jupyter lab` in the main folder. Open `Langhain-with-Snowflake-Cortex-and-Stage.ipynb`

## Install unstructured

To work with PDF files
[unstructured](https://python.langchain.com/v0.2/docs/integrations/document_loaders/unstructured_file/)
library is needed. It supports multiple formats of files,
so it is worth to check it out.
