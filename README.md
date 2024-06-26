# GenAI Starter - LangChain - Restack

An example of how to deploy a Flask application with [LangChain](https://python.langchain.com/en/latest/index.html) with Restack.

---
### Environment Variables

<details>

<summary>ℹ️ OpenAI models</summary>

In this example, we chose OpenAI's models for the sake of simplicity, but you're free to choose the models you prefer as LangChain provides support for other models as well. In that case, we recommend you remove the `OPENAI_API_KEY` environment variable and the relevant application code.

</details>

To ensure your successful deployment, set the following environment variables:

```bash
# Get it from https://platform.openai.com/account/api-keys
OPENAI_API_KEY=<YOUR_API_KEY>
```

## What is LangChain
LangChain framework is intended to develop language model-powered applications that are data-aware, agentic, and differentiated. More information is available on the [LangChain](https://python.langchain.com/en/latest/index.html) website.