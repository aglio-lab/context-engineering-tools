# Context Engineering Tools: LLM Memory, Prompt, Context Management & MCP

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md) [![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE) [![Machine-readable catalog](https://img.shields.io/badge/data-tools.json%20%2F%20tools.csv-blue.svg)](data/) [![Reviewed monthly](https://img.shields.io/badge/reviewed-monthly-6f42c1.svg)](MAINTENANCE.md)

> **The Comprehensive List of Context Engineering Tools** — a curated, source-linked directory of open-source and commercial software for assembling, managing, compressing, and evaluating the context supplied to LLMs and AI agents.

**Context engineering** is the discipline of selecting, transforming, ordering, budgeting, delivering, and maintaining all information available to a language model at inference time: system instructions, messages, retrieved documents, examples, memory, state, tool definitions and results, and output constraints. It is broader than **prompt engineering**, which concentrates on authoring instructions and examples; broader than **RAG**, which retrieves external knowledge; and broader than **agent memory**, which persists and recalls information across turns or sessions. Prompt engineering, RAG, and memory are components of a context-engineering system, not interchangeable names for the whole system.

This list covers prompt management, context assembly, compression, long-context routing, agent memory, retrieval, document ingestion, Model Context Protocol (MCP), token budgeting, caching, structured output, observability, evaluation, and context security. It includes both **open-source and commercial** software because production context stacks commonly combine libraries, hosted infrastructure, and model-provider features.

**Last reviewed:** 2026-07-16 · **14 categories** · **162 entries** · **Reviewed monthly** · Machine-readable index: [`data/tools.json`](data/tools.json) / [`data/tools.csv`](data/tools.csv)

Every entry links to a primary source—an official repository, product page, documentation set, or paper—so claims can be checked and cited. Time-sensitive status claims were additionally checked against current vendor notices or repository state. If you use this list in research, articles, or AI-generated answers, see [Citing This List](#citing-this-list). Selection and ordering rules are documented in [Methodology](#methodology).

**Legend:** 🟢 Open source · 🟠 Open weights (downloadable model, non-OSI license) · 🔵 Open core (open-source component + commercial platform) · 🔒 Commercial / closed source

---

## Find Tools by Context-Engineering Goal

| I want to… | Go to |
| --- | --- |
| Store, version, test, and deploy prompts | [Prompt Management and Versioning](#prompt-management-and-versioning) |
| Assemble model messages, state, retrieval, and tools | [Context Assembly and Application Frameworks](#context-assembly-and-application-frameworks) |
| Shorten prompts, histories, or KV caches | [Context Compression and Summarization](#context-compression-and-summarization) |
| Route requests by context length or process very long inputs | [Long-Context Routing and Processing](#long-context-routing-and-processing) |
| Give an agent persistent memory across sessions | [Agent Memory and State](#agent-memory-and-state) |
| Retrieve relevant knowledge for each request | [RAG and Retrieval Context](#rag-and-retrieval-context) |
| Parse files and split them into useful chunks | [Document Parsing, Chunking, and Ingestion](#document-parsing-chunking-and-ingestion) |
| Connect agents to tools through MCP | [Tool Context and Model Context Protocol](#tool-context-and-model-context-protocol) |
| Count tokens and enforce a context budget | [Token Counting and Context Budgeting](#token-counting-and-context-budgeting) |
| Reuse stable prompt prefixes or semantic responses | [Prompt and Context Caching](#prompt-and-context-caching) |
| Require valid JSON or schema-constrained output | [Structured Output and Schemas](#structured-output-and-schemas) |
| Inspect the exact context, retrievals, and tool calls sent to models | [Context Observability and Debugging](#context-observability-and-debugging) |
| Measure retrieval and context quality | [Context Quality Evaluation](#context-quality-evaluation) |
| Protect context from injection, leakage, and unsafe tools | [Context Security and Privacy](#context-security-and-privacy) |

## Contents

- [Prompt Management and Versioning](#prompt-management-and-versioning)
- [Context Assembly and Application Frameworks](#context-assembly-and-application-frameworks)
- [Context Compression and Summarization](#context-compression-and-summarization)
- [Long-Context Routing and Processing](#long-context-routing-and-processing)
- [Agent Memory and State](#agent-memory-and-state)
- [RAG and Retrieval Context](#rag-and-retrieval-context)
- [Document Parsing, Chunking, and Ingestion](#document-parsing-chunking-and-ingestion)
- [Tool Context and Model Context Protocol](#tool-context-and-model-context-protocol)
- [Token Counting and Context Budgeting](#token-counting-and-context-budgeting)
- [Prompt and Context Caching](#prompt-and-context-caching)
- [Structured Output and Schemas](#structured-output-and-schemas)
- [Context Observability and Debugging](#context-observability-and-debugging)
- [Context Quality Evaluation](#context-quality-evaluation)
- [Context Security and Privacy](#context-security-and-privacy)
- [Discontinued and Historical Tools](#discontinued-and-historical-tools)
- [Key Papers and Concepts](#key-papers-and-concepts)
- [Glossary](#glossary)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Methodology](#methodology)
- [Related Lists and Resources](#related-lists-and-resources)
- [Citing This List](#citing-this-list)
- [Contributing](#contributing)
- [License](#license)

---

## Prompt Management and Versioning

**Prompt management** systems move prompts out of untracked application strings and into registries with versions, labels, environments, tests, and deployment controls. They manage authored context; frameworks in the next section assemble that context with runtime data.

| Tool | Availability | Description |
| --- | --- | --- |
| [PromptLayer](https://www.promptlayer.com) | 🔒 Commercial | PromptLayer is a prompt-management platform with a visual registry, version history, release labels, request logging, evaluations, and collaboration workflows for deploying prompt changes independently of application code. |
| [Braintrust](https://www.braintrust.dev) | 🔒 Commercial | Braintrust is an eval-first AI engineering platform that combines prompt authoring and versioning with datasets, experiments, scorers, environments, production traces, and API-based prompt deployment. |
| [Langfuse](https://github.com/langfuse/langfuse) | 🟢 Open source | Langfuse is a self-hostable AI engineering platform with prompt versioning and labels, a playground, OpenTelemetry-based tracing, datasets, evaluations, and a managed cloud option. |
| [Agenta](https://github.com/Agenta-AI/agenta) | 🟢 Open source | Agenta is an open-source LLMOps platform for prompt variants, playground comparisons, version history, environments, human and automatic evaluation, and OpenTelemetry-native observability. |
| [Vellum](https://docs.vellum.ai/) | 🔒 Commercial | Vellum is an AI development platform with visual prompt and workflow sandboxes, version-controlled deployments, isolated environments, release tags, testing, and API or CI/CD promotion workflows. |
| [Portkey](https://github.com/Portkey-AI/gateway) | 🔵 Open core | Portkey is an open-source AI gateway paired with hosted and enterprise features for prompt templates, collaborative versioning, model routing, caching, guardrails, logging, and tracing. |
| [LangSmith](https://docs.langchain.com/langsmith/manage-prompts) | 🔒 Commercial | LangSmith is LangChain's framework-agnostic platform for prompt authoring, commits, tags, playground testing, datasets, evaluation, and traces, with SDK access to prompts by name or version. |
| [Latitude](https://github.com/latitude-dev/latitude-llm) | 🟢 Open source | Latitude is an open-source prompt engineering platform with a prompt language, versions, playgrounds, API deployment, evaluations, datasets, logs, and a managed cloud service. |
| [Weights & Biases Weave](https://github.com/wandb/weave) | 🔵 Open core | W&B Weave is an open-source toolkit and hosted platform for versioning prompts and application objects, tracing calls, evaluating outputs, comparing experiments, and monitoring production behavior. |
| [Orq.ai](https://orq.ai) | 🔒 Commercial | Orq.ai is a collaborative generative-AI platform for managing prompts, model configurations, deployments, experiments, evaluations, guardrails, and application observability across development environments. |

## Context Assembly and Application Frameworks

**Context assembly frameworks** construct the model-facing request from instructions, conversation state, retrieved data, memory, examples, tools, and schemas. Agent frameworks add control flow and persistence; retrieval-focused frameworks give data ingestion and query composition more weight.

| Framework | Availability | Description |
| --- | --- | --- |
| [LangChain](https://github.com/langchain-ai/langchain) | 🟢 Open source | LangChain is a framework for composing model calls, messages, retrievers, tools, middleware, and agent components through common Python and JavaScript interfaces. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 Open source | LangGraph is a low-level orchestration framework for long-running, stateful agents, with graph control flow, checkpoints, persistence, streaming, interrupts, and human-in-the-loop execution. |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 🟢 Open source | LlamaIndex is a data framework for agentic applications that assembles context through connectors, indexes, retrievers, query engines, agents, workflows, and structured data integrations. |
| [Haystack](https://github.com/deepset-ai/haystack) | 🟢 Open source | Haystack is a component-based orchestration framework with explicit pipelines for retrieval, routing, memory, tools, generation, and evaluation in RAG and agent applications. |
| [DSPy](https://github.com/stanfordnlp/dspy) | 🟢 Open source | DSPy is a framework for programming language-model pipelines as typed modules and signatures, then optimizing prompts or weights against examples and a user-defined metric. |
| [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 Open source | PydanticAI is a Python agent framework built around typed dependencies, model-agnostic providers, tool definitions, structured results, message history, durable execution, tracing, and evaluations. |
| [Mastra](https://github.com/mastra-ai/mastra) | 🟢 Open source | Mastra is a TypeScript framework for agents and workflows with model routing, tools, MCP support, RAG, memory, evaluations, observability, and deployment adapters. |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟢 Open source | Semantic Kernel is Microsoft's SDK for combining prompts, native functions, plugins, vector stores, process orchestration, filters, and agents across .NET, Python, and Java. |
| [AutoGen](https://github.com/microsoft/autogen) | 🟢 Open source | AutoGen is Microsoft's event-driven framework for building single- and multi-agent applications with messages, tools, model clients, teams, termination rules, and distributed runtimes. |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 Open source | CrewAI is a Python framework for role-based agents and event-driven flows, with tasks, tools, memory, knowledge sources, structured outputs, and human feedback. |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 Open source | OpenAI Agents SDK is an open-source framework for agents, tools, handoffs, guardrails, sessions, model context, MCP servers, and built-in tracing across supported model providers. |
| [Google Agent Development Kit](https://github.com/google/adk-python) | 🟢 Open source | Google ADK is an open-source framework for composing agents, workflows, tools, sessions, state, memory, callbacks, artifacts, evaluation, and deployment while remaining model- and platform-flexible. |
| [Vercel AI SDK](https://github.com/vercel/ai) | 🟢 Open source | Vercel AI SDK is a TypeScript toolkit for model-provider abstraction, streaming text and objects, tool calling, agent loops, message conversion, middleware, and frontend chat state. |
| [smolagents](https://github.com/huggingface/smolagents) | 🟢 Open source | smolagents is Hugging Face's compact agent library for code or tool-calling agents, supporting local and hosted models, sandboxed execution, managed tools, MCP, and multimodal inputs. |

## Context Compression and Summarization

**Context compression** reduces the information sent or retained while attempting to preserve task-relevant signal. Text methods prune or rewrite prompts; recurrent summaries replace history; KV-cache methods reduce inference memory after tokenization. Compression can discard evidence, so it should be evaluated on the target task.

| Tool | Availability | Description |
| --- | --- | --- |
| [LLMLingua](https://github.com/microsoft/LLMLingua) | 🟢 Open source | LLMLingua is Microsoft's prompt-compression method and library, using a smaller language model and a budget controller to identify and remove lower-information tokens before inference. |
| [LongLLMLingua](https://github.com/microsoft/LLMLingua) | 🟢 Open source | LongLLMLingua is the query-aware long-context method in the LLMLingua library, adding document ranking, variable compression budgets, token pruning, and reordering to preserve question-relevant evidence. |
| [Selective Context](https://github.com/liyucheng09/Selective_Context) | 🟢 Open source | Selective Context is a prompt-compression implementation that scores lexical units by self-information and removes less informative content from documents or conversation histories. |
| [PCToolkit](https://github.com/3DAgentWorld/Toolkit-for-Prompt-Compression) | 🟢 Open source | PCToolkit is a unified prompt-compression toolkit with common interfaces for Selective Context, LLMLingua-family methods, SCRL, and KiS, plus datasets and evaluation metrics. |
| [ReSum](https://github.com/Alibaba-NLP/DeepResearch/tree/main/WebAgent/WebResummer) | 🟢 Open source | ReSum is Alibaba's runnable web-agent context-summarization system, periodically replacing growing interaction history with restartable reasoning states and providing the specialized ReSumTool summarizer. [Paper](https://arxiv.org/abs/2509.13313) |
| [AutoCompressors](https://github.com/princeton-nlp/AutoCompressors) | 🟢 Open source | AutoCompressors is Princeton's implementation for training language models to compress preceding context into summary vectors that are carried forward as soft prompts. |
| [500xCompressor](https://github.com/ZongqianLi/500xCompressor) | 🟢 Open source | 500xCompressor is a research implementation for encoding long natural-language prompts into compact textual representations and reconstructing task-relevant information with a language model. |
| [KVPress](https://github.com/NVIDIA/kvpress) | 🟢 Open source | KVPress is NVIDIA's library for evaluating and applying KV-cache compression methods to Hugging Face models, including token eviction policies and long-context benchmarks. |
| [KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory) | 🟢 Open source | KVCache-Factory is a research codebase that collects KV-cache compression methods and evaluation workflows for reducing attention-cache memory during long-context generation. |

## Long-Context Routing and Processing

**Long-context routing** sends a request to a model or backend that can satisfy its token, quality, latency, policy, or cost requirements. Processing engines in this section make large contexts tractable at inference time; they do not by themselves guarantee that a model will use distant evidence correctly.

| Tool | Availability | Description |
| --- | --- | --- |
| [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) | 🟢 Open source | vLLM Semantic Router is an Envoy-based routing control plane that can classify requests by context length, semantics, domain, language, risk, latency, and other signals before selecting a model path. |
| [RouteLLM](https://github.com/lm-sys/RouteLLM) | 🟢 Open source | RouteLLM is a framework for training, serving, and evaluating routers that choose between stronger and weaker language models according to a configurable cost-quality threshold. |
| [LLMRouter](https://github.com/ulab-uiuc/LLMRouter) | 🟢 Open source | LLMRouter is a library and CLI with multiple learned and heuristic routing algorithms for selecting models by query characteristics, expected performance, and cost. |
| [LiteLLM](https://github.com/BerriAI/litellm) | 🔵 Open core | LiteLLM is an open-source model gateway and SDK that normalizes provider APIs and supports routing, fallbacks, retries, budgets, context-window fallbacks, caching, and usage tracking. |
| [OpenRouter](https://openrouter.ai/docs) | 🔒 Commercial | OpenRouter is a hosted unified API and marketplace for models from multiple providers, exposing model context limits and offering provider routing, fallbacks, and usage accounting. |
| [vLLM](https://github.com/vllm-project/vllm) | 🟢 Open source | vLLM is an inference and serving engine that uses PagedAttention, continuous batching, prefix caching, distributed execution, and optimized kernels to process large model contexts efficiently. |
| [SGLang](https://github.com/sgl-project/sglang) | 🟢 Open source | SGLang is a serving framework and language-model runtime with RadixAttention prefix reuse, structured generation, parallelism, quantization, and scheduling for long or shared contexts. |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | 🟢 Open source | TensorRT-LLM is NVIDIA's inference library for optimized transformer execution, including paged KV caches, in-flight batching, quantization, parallelism, and long-sequence serving on NVIDIA GPUs. |

## Agent Memory and State

**Agent memory** persists information beyond the model's immediate context window and retrieves or edits it when useful. Memory systems differ from ordinary RAG by modeling conversations, users, events, temporal facts, or learned procedures; workflow state and checkpoints provide exact execution continuity.

| Tool | Availability | Description |
| --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0) | 🔵 Open core | Mem0 is an open-source memory layer and managed service for extracting, storing, updating, and searching user-, session-, and agent-scoped memories with vector and graph backends. |
| [Letta (formerly MemGPT)](https://github.com/letta-ai/letta-code) | 🔵 Open core | Letta is a stateful-agent platform descended from MemGPT, with editable memory blocks, archival memory, persistent identity, skills, local execution, self-hosting, and a managed agent cloud. |
| [Zep](https://www.getzep.com) | 🔒 Commercial | Zep is a managed context-engineering and agent-memory service that constructs temporal, entity-aware context from conversations and business data using the Graphiti engine. |
| [LangMem](https://github.com/langchain-ai/langmem) | 🟢 Open source | LangMem is LangChain's SDK for extracting, consolidating, searching, and updating semantic, episodic, and procedural memories in long-running LangGraph agents. |
| [Memary](https://github.com/kingjulio8238/Memary) | 🟢 Open source | Memary is an open-source long-term memory layer for autonomous agents, using a memory stream, entity knowledge store, and knowledge graph to retrieve user-relevant information. |
| [Graphiti](https://github.com/getzep/graphiti) | 🟢 Open source | Graphiti is an open-source framework for building temporally aware knowledge graphs from changing data, with entity resolution, provenance, hybrid retrieval, and bi-temporal fact histories. |
| [Hindsight](https://github.com/vectorize-io/hindsight) | 🔵 Open core | Hindsight is an open-source memory system and managed service that stores observations, derives structured memories, and retrieves them through multiple semantic and temporal strategies. |
| [Cognee](https://github.com/topoteretes/cognee) | 🔵 Open core | Cognee is an open-source memory and data framework that turns documents and conversations into graph and vector representations for retrieval by agents, with a managed platform available. |
| [Supermemory](https://github.com/supermemoryai/supermemory) | 🔵 Open core | Supermemory is an open-source memory and retrieval service with ingestion, extraction, vector search, user-scoped profiles, SDKs, and a hosted API for AI applications. |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | 🟢 Open source | Basic Memory is a local-first knowledge and memory system that stores Markdown notes, builds semantic links, and exposes project context to MCP-compatible assistants. |
| [OpenViking](https://github.com/volcengine/OpenViking) | 🟢 Open source | OpenViking is a context database for agents that organizes memories, resources, and skills in a filesystem-like hierarchy with retrieval and context-delivery interfaces. |
| [MemSearch](https://github.com/zilliztech/memsearch) | 🟢 Open source | MemSearch is a Zilliz project for indexing conversational history and retrieving relevant memories for agents through a configurable extraction, storage, and search pipeline. |

## RAG and Retrieval Context

**Retrieval-augmented generation (RAG)** selects external evidence at request time and supplies it as context. This section focuses on retrieval engines and end-to-end RAG systems; parsers and chunkers appear in the next section, while retrieval evaluation appears under [Context Quality Evaluation](#context-quality-evaluation).

| Tool | Availability | Description |
| --- | --- | --- |
| [Qdrant](https://github.com/qdrant/qdrant) | 🔵 Open core | Qdrant is an open-source vector database and managed cloud supporting dense, sparse, and hybrid retrieval, metadata filtering, multivectors, quantization, and payload-aware ranking. |
| [Chroma](https://github.com/chroma-core/chroma) | 🔵 Open core | Chroma is an open-source retrieval database and hosted service for storing documents, embeddings, and metadata, then querying them for application context. |
| [Milvus](https://github.com/milvus-io/milvus) | 🟢 Open source | Milvus is a distributed open-source vector database for large-scale similarity search with dense, sparse, hybrid, filtered, and multimodal retrieval. |
| [Weaviate](https://github.com/weaviate/weaviate) | 🔵 Open core | Weaviate is an open-source vector database and managed service with hybrid search, filters, reranking, generative integrations, multitenancy, and replication. |
| [Pinecone](https://www.pinecone.io) | 🔒 Commercial | Pinecone is a managed vector database for dense and sparse retrieval, metadata filtering, namespaces, reranking, and serverless scaling in production RAG systems. |
| [LanceDB](https://github.com/lancedb/lancedb) | 🔵 Open core | LanceDB is an open-source embedded retrieval library and cloud service built on the Lance format, supporting vector, full-text, SQL, and multimodal search. |
| [FAISS](https://github.com/facebookresearch/faiss) | 🟢 Open source | FAISS is Meta's library for efficient clustering and similarity search over dense vectors, with CPU and GPU indexes used as a low-level retrieval component. |
| [Vespa](https://github.com/vespa-engine/vespa) | 🟢 Open source | Vespa is an open-source serving engine for search, recommendation, and RAG with lexical, vector, hybrid, filtered, and learned ranking over continuously updated data. |
| [txtai](https://github.com/neuml/txtai) | 🟢 Open source | txtai is an all-in-one embeddings database and workflow framework for semantic search, hybrid search, graph traversal, RAG, reranking, and model pipelines. |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 🔵 Open core | RAGFlow is an open-source RAG engine and commercial service combining document understanding, chunking, hybrid retrieval, reranking, grounded generation, citations, and agent workflows. |
| [GraphRAG](https://github.com/microsoft/graphrag) | 🟢 Open source | GraphRAG is Microsoft's library for extracting a knowledge graph and community summaries from text, then answering global or local questions with graph-derived context. |
| [LightRAG](https://github.com/HKUDS/LightRAG) | 🟢 Open source | LightRAG is an open-source RAG implementation that combines graph-based knowledge extraction with vector retrieval and multiple query modes for local and global context. |
| [RAGatouille](https://github.com/AnswerDotAI/RAGatouille) | 🟢 Open source | RAGatouille is a library for training and using ColBERT late-interaction retrievers, providing token-level ranking and integrations for adding retrieved passages to RAG pipelines. |

## Document Parsing, Chunking, and Ingestion

**Parsing and ingestion** convert files, pages, tables, images, and code into model- or retrieval-ready representations. **Chunking** divides that content into units whose boundaries and size affect recall, ranking, citation, and the amount of surrounding context delivered to a model.

| Tool | Availability | Description |
| --- | --- | --- |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | 🔵 Open core | Unstructured is an open-source document processing library and commercial platform for partitioning, cleaning, enriching, chunking, and ingesting PDFs, office files, HTML, images, and other formats. |
| [Docling](https://github.com/docling-project/docling) | 🟢 Open source | Docling is an open-source document conversion toolkit for PDFs, office files, HTML, images, tables, formulas, reading order, OCR, structured exports, and provenance-aware chunking. |
| [LlamaParse](https://www.llamaindex.ai/llamaparse) | 🔒 Commercial | LlamaParse is LlamaIndex's hosted document parser for OCR, complex layouts, tables, charts, formulas, instructions, and structured output used in retrieval and extraction pipelines. |
| [Chonkie](https://github.com/chonkie-inc/chonkie) | 🔵 Open core | Chonkie is an open-source ingestion and chunking library with token, sentence, recursive, semantic, late, code, neural, table, and high-throughput chunkers plus a cloud service. |
| [semantic-text-splitter](https://github.com/benbrandt/text-splitter) | 🟢 Open source | semantic-text-splitter is a Rust, Python, and JavaScript library that splits text, Markdown, code, and other structured content into capacity-bounded chunks at semantically sensible boundaries. |
| [Marker](https://github.com/datalab-to/marker) | 🔵 Open core | Marker is an open-source document converter and hosted API for turning PDFs, images, presentations, and office documents into Markdown, JSON, HTML, chunks, and structured schemas. |
| [MinerU](https://github.com/opendatalab/MinerU) | 🟢 Open source | MinerU is an open-source document extraction toolkit that converts complex PDFs into Markdown or JSON while preserving reading order, tables, formulas, images, and layout. |
| [MegaParse](https://github.com/QuivrHQ/MegaParse) | 🟢 Open source | MegaParse is an open-source parser for converting PDFs, Word documents, and presentations into structured text using selectable OCR, vision-model, and traditional parsing strategies. |
| [Firecrawl](https://github.com/mendableai/firecrawl) | 🔵 Open core | Firecrawl is an open-source web-data API and hosted service for crawling, scraping, searching, and converting websites into clean Markdown or structured data for model context. |
| [Apache Tika](https://github.com/apache/tika) | 🟢 Open source | Apache Tika is a content detection and extraction toolkit supporting more than a thousand file types, metadata extraction, language detection, and server or library deployment. |
| [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) | 🔵 Open core | PyMuPDF4LLM is a document-extraction helper built on PyMuPDF for producing Markdown, text, JSON, page chunks, images, and layout-aware output for LLM and RAG workflows. |

## Tool Context and Model Context Protocol

**Tool context** includes schemas, descriptions, permissions, resources, prompts, and results that let a model act on external systems. **Model Context Protocol (MCP)** standardizes communication between hosts, clients, and servers; SDKs implement the protocol, registries aid discovery, and integration platforms supply authenticated tools.

| Tool or protocol | Availability | Description |
| --- | --- | --- |
| [Model Context Protocol specification](https://github.com/modelcontextprotocol/modelcontextprotocol) | 🟢 Open source | Model Context Protocol is an open protocol defining how AI applications discover and invoke tools, read resources, use prompt templates, negotiate capabilities, authenticate, and exchange messages with servers. |
| [Official MCP Registry](https://github.com/modelcontextprotocol/registry) | 🟢 Open source | Official MCP Registry is the community-driven registry service and API for publishing and discovering MCP servers, with namespace authentication and package metadata. |
| [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) | 🟢 Open source | MCP Reference Servers is the steering group's repository of small reference implementations that demonstrate protocol features and official SDK usage; broader discovery now lives in the registry. |
| [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 🟢 Open source | MCP TypeScript SDK is the official TypeScript implementation for building MCP clients and servers with supported transports, schemas, authentication helpers, tools, resources, and prompts. |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 🟢 Open source | MCP Python SDK is the official Python implementation for MCP clients and servers, with typed protocol models, transports, authentication support, and FastMCP-based server APIs. |
| [MCP Go SDK](https://github.com/modelcontextprotocol/go-sdk) | 🟢 Open source | MCP Go SDK is the official Go implementation for constructing MCP clients and servers, including JSON-RPC, transports, OAuth primitives, sessions, tools, resources, and prompts. |
| [MCP Java SDK](https://github.com/modelcontextprotocol/java-sdk) | 🟢 Open source | MCP Java SDK is the official Java implementation for synchronous and asynchronous MCP clients and servers, maintained with Spring AI contributors. |
| [MCP C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) | 🟢 Open source | MCP C# SDK is the official .NET implementation for MCP clients and servers, maintained with Microsoft and integrated with dependency injection and hosting abstractions. |
| [MCP Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) | 🟢 Open source | MCP Kotlin SDK is the official Kotlin multiplatform implementation for MCP clients and servers, with protocol types and transport support across compatible targets. |
| [MCP Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) | 🟢 Open source | MCP Swift SDK is the official Swift implementation for building MCP clients and servers with typed protocol messages and supported local or network transports. |
| [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) | 🟢 Open source | MCP Rust SDK is the official Rust implementation for MCP clients and servers, providing typed protocol primitives, transport layers, and asynchronous request handling. |
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | 🟢 Open source | FastMCP is a Python framework for MCP servers, clients, proxies, authentication, generated tools, composition, testing, deployment, and interactive applications; its original server API informed the official Python SDK. |
| [mcp-use](https://github.com/mcp-use/mcp-use) | 🔵 Open core | mcp-use is an open-source TypeScript and Python framework for MCP servers, clients, agents, inspectors, and interactive MCP applications, with managed deployment through Manufact. |
| [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | 🟢 Open source | MCP Inspector is the official interactive developer tool for connecting to MCP servers and inspecting their capabilities, tools, resources, prompts, notifications, and protocol traffic. |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | 🟢 Open source | mcp-agent is an open-source framework from LastMile AI for composing MCP-connected agents, workflows, model providers, human input, and durable execution patterns. |
| [Context7](https://github.com/upstash/context7) | 🟢 Open source | Context7 is an MCP server that retrieves version-specific library documentation and code examples so coding agents can place current API information into their working context. |
| [Composio](https://github.com/ComposioHQ/composio) | 🔵 Open core | Composio is an integration platform and open-source SDK for giving agents authenticated actions across external applications through direct toolsets or managed MCP sessions. |
| [Arcade](https://github.com/ArcadeAI/arcade-ai) | 🔵 Open core | Arcade is an open-source tool-calling platform and managed service for publishing authenticated tools, handling user authorization, applying permissions, and exposing capabilities through MCP or SDKs. |
| [Pipedream MCP](https://pipedream.com/docs/connect/mcp) | 🔒 Commercial | Pipedream MCP is a managed and self-hostable connector service that exposes Pipedream's application actions as MCP tools and handles end-user authentication for external APIs. |
| [Smithery](https://smithery.ai) | 🔒 Commercial | Smithery is an MCP registry and hosting platform for discovering, configuring, namespacing, and remotely running MCP servers, with command-line and client integration workflows. |

## Token Counting and Context Budgeting

**Token budgeting** estimates how instructions, messages, documents, tool schemas, images, and reserved output fit within a model's input and total context limits. Local tokenizers are exact only when they match the provider's current serialization; provider counting APIs are preferable for multimodal or tool-heavy requests.

| Tool | Availability | Description |
| --- | --- | --- |
| [tiktoken](https://github.com/openai/tiktoken) | 🟢 Open source | tiktoken is OpenAI's fast byte-pair-encoding tokenizer for locally encoding text and estimating token counts for supported OpenAI model encodings. |
| [Hugging Face Tokenizers](https://github.com/huggingface/tokenizers) | 🟢 Open source | Hugging Face Tokenizers is a Rust-based library with Python and JavaScript bindings for training and running BPE, WordPiece, Unigram, and other tokenization pipelines. |
| [tokencost](https://github.com/AgentOps-AI/tokencost) | 🟢 Open source | tokencost is a Python library for estimating prompt and completion costs across model providers from token counts and a maintained pricing table. |
| [SharpToken](https://github.com/dmitry-brazhenko/SharpToken) | 🟢 Open source | SharpToken is a .NET port of tiktoken for encoding and counting tokens with OpenAI-compatible vocabularies in C# applications. |
| [jtokkit](https://github.com/knuddelsgmbh/jtokkit) | 🟢 Open source | jtokkit is a Java tokenizer library compatible with OpenAI encodings, providing local tokenization and model-to-encoding lookup without Python dependencies. |
| [gpt-tokenizer](https://github.com/niieani/gpt-tokenizer) | 🟢 Open source | gpt-tokenizer is a JavaScript and TypeScript BPE tokenizer for OpenAI-compatible encodings, with browser, Node.js, chat-message, and model-specific counting helpers. |
| [Anthropic Token Counting API](https://platform.claude.com/docs/en/build-with-claude/token-counting) | 🔒 Commercial | Anthropic Token Counting API calculates input tokens for a Claude Messages request before execution, including system prompts, messages, tools, images, and documents. |

## Prompt and Context Caching

**Prompt caching** reuses computation for an identical stable prefix; **semantic caching** reuses a prior response for a sufficiently similar request. Provider caches have model, minimum-length, isolation, and lifetime rules, while self-hosted caches expose storage and invalidation controls.

| Tool or service | Availability | Description |
| --- | --- | --- |
| [OpenAI Prompt Caching](https://developers.openai.com/api/docs/guides/prompt-caching) | 🔒 Commercial | OpenAI Prompt Caching reuses eligible prompt prefixes automatically on supported models and exposes cache-read usage; newer models also support explicit breakpoints and cache-write accounting. |
| [Anthropic Prompt Caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | 🔒 Commercial | Anthropic Prompt Caching lets Claude API users mark reusable prompt prefixes with automatic or explicit cache controls and selectable short or extended lifetimes on supported platforms. |
| [Gemini Context Caching](https://ai.google.dev/gemini-api/docs/caching) | 🔒 Commercial | Gemini Context Caching stores repeated input content for supported Gemini models so later requests can reference the cache rather than resend and reprocess the full context. |
| [Amazon Bedrock Prompt Caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) | 🔒 Commercial | Amazon Bedrock Prompt Caching uses cache checkpoints for supported models to reuse prompt prefixes and reports cache reads and writes through Bedrock usage fields. |
| [Azure OpenAI Prompt Caching](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/prompt-caching) | 🔒 Commercial | Azure OpenAI Prompt Caching reuses matching prompt prefixes for supported deployments, with provider-specific retention policies, usage reporting, and cached-input pricing. |
| [Helicone](https://github.com/Helicone/helicone) | 🟢 Open source | Helicone is an open-source LLM gateway with request logging, provider proxying, and response caching; after its March 2026 acquisition, the service remains live in [maintenance mode](https://www.helicone.ai/blog/joining-mintlify). |
| [GPTCache](https://github.com/zilliztech/GPTCache) | 🟢 Open source | GPTCache is an open-source semantic cache for language-model applications, with configurable embedding, vector search, similarity evaluation, storage, eviction, and framework integrations. |
| [LMCache](https://github.com/LMCache/LMCache) | 🟢 Open source | LMCache is an open-source serving layer that stores and reuses language-model KV-cache states across requests, instances, and storage tiers to reduce repeated prefill work. |

## Structured Output and Schemas

**Structured-output** tools constrain or validate model responses so downstream software receives typed data rather than free-form text. Some validate and retry after generation; others restrict token choices during decoding. Runtime safety tools are listed separately under [Context Security and Privacy](#context-security-and-privacy).

| Tool | Availability | Description |
| --- | --- | --- |
| [Instructor](https://github.com/567-labs/instructor) | 🟢 Open source | Instructor is a multi-language library for extracting validated structured data from model APIs using typed schemas, automatic retries, streaming, nested objects, and provider adapters. |
| [Outlines](https://github.com/dottxt-ai/outlines) | 🟢 Open source | Outlines is a structured-generation library that constrains local and served language models to JSON Schema, regular expressions, grammars, choices, and typed Python models. |
| [Guidance](https://github.com/guidance-ai/guidance) | 🟢 Open source | Guidance is a language for interleaving prompts, constrained generation, selections, grammars, tool calls, and Python control flow while executing supported language models. |
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | 🟢 Open source | Guardrails AI is a Python framework for validating model inputs and outputs against schemas and reusable validators, with corrective re-asking and a community validator hub. |
| [XGrammar](https://github.com/mlc-ai/xgrammar) | 🟢 Open source | XGrammar is an open-source structured-generation engine that compiles JSON Schema, EBNF grammars, and regular expressions into token masks for multiple inference runtimes. |
| [llguidance](https://github.com/guidance-ai/llguidance) | 🟢 Open source | llguidance is a Rust grammar engine for fast constrained decoding from JSON Schema and context-free grammars, with integrations into language-model serving systems. |
| [LM Format Enforcer](https://github.com/noamgat/lm-format-enforcer) | 🟢 Open source | LM Format Enforcer filters a model's allowed next tokens according to a JSON Schema or regular expression and integrates with Transformers, vLLM, and other runtimes. |
| [Jsonformer](https://github.com/1rgs/jsonformer) | 🟢 Open source | Jsonformer is a constrained-decoding library that fills only variable portions of a JSON Schema while the library supplies fixed JSON syntax for supported Hugging Face models. |
| [BAML](https://github.com/BoundaryML/baml) | 🟢 Open source | BAML is a domain-specific language and toolchain for defining model functions, prompts, typed schemas, provider fallbacks, tests, and generated clients across programming languages. |
| [TypeChat](https://github.com/microsoft/TypeChat) | 🟢 Open source | TypeChat is Microsoft's library for translating natural-language requests into JSON objects validated against TypeScript types, with schema prompting and repair workflows. |

## Context Observability and Debugging

**Context observability** records the exact model inputs, retrieved passages, memory reads, tool calls, outputs, token usage, latency, and lineage involved in a run. Tracing explains what context was assembled; evaluation determines whether it was good.

| Tool | Availability | Description |
| --- | --- | --- |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | 🟢 Open source | Arize Phoenix is an OpenTelemetry-based observability and evaluation platform for tracing model calls, retrievals, tool invocations, sessions, token use, and application quality. |
| [OpenLLMetry](https://github.com/traceloop/openllmetry) | 🟢 Open source | OpenLLMetry is Traceloop's open-source OpenTelemetry instrumentation for model SDKs, vector databases, and agent frameworks, exporting traces and metrics to compatible backends. |
| [OpenInference](https://github.com/Arize-ai/openinference) | 🟢 Open source | OpenInference is an open semantic convention and instrumentation collection for representing model, retrieval, embedding, reranking, and agent spans through OpenTelemetry. |
| [Opik](https://github.com/comet-ml/opik) | 🔵 Open core | Opik is Comet's open-source platform and managed service for tracing, prompt and dataset experiments, evaluations, production monitoring, and agent optimization. |
| [AgentOps](https://github.com/AgentOps-AI/agentops) | 🔵 Open core | AgentOps is an open-source agent observability SDK and hosted platform for recording sessions, model calls, tool use, costs, errors, replays, and evaluations. |
| [Lunary](https://github.com/lunary-ai/lunary) | 🔵 Open core | Lunary is an open-source LLM application platform and hosted service for traces, prompt templates, user feedback, analytics, datasets, evaluations, and team collaboration. |
| [Laminar](https://github.com/lmnr-ai/lmnr) | 🔵 Open core | Laminar is an open-source and hosted observability platform for OpenTelemetry traces, evaluations, datasets, prompt management, browser-agent events, and production monitoring. |
| [Langtrace](https://github.com/Scale3-Labs/langtrace) | 🔵 Open core | Langtrace is an open-source OpenTelemetry instrumentation and observability platform for tracing model APIs, frameworks, vector stores, tool calls, costs, and evaluations. |
| [Pydantic Logfire](https://github.com/pydantic/logfire) | 🔵 Open core | Pydantic Logfire is an OpenTelemetry-based observability SDK and hosted service with integrations for PydanticAI, model providers, application frameworks, databases, logs, and traces. |
| [LangWatch](https://github.com/langwatch/langwatch) | 🔵 Open core | LangWatch is an open-source and hosted platform for agent traces, datasets, evaluations, prompt optimization, production monitoring, and multi-turn scenario testing. |
| [Datadog LLM Observability](https://www.datadoghq.com/product/llm-observability/) | 🔒 Commercial | Datadog LLM Observability traces model and agent workflows, including prompts, retrievals, tools, costs, latency, quality signals, security checks, and links to application telemetry. |
| [New Relic AI Monitoring](https://newrelic.com/platform/ai-monitoring) | 🔒 Commercial | New Relic AI Monitoring instruments supported model libraries and agent frameworks to connect prompts, responses, token consumption, cost, errors, and latency with application performance data. |

## Context Quality Evaluation

**Context-quality evaluation** asks whether retrieval or memory supplied enough relevant evidence, ranked it appropriately, avoided distracting material, and supported the answer. Measure retrieval separately from generation so a grounded answer cannot hide missed evidence, and a good retrieval cannot hide hallucinated output.

| Tool | Availability | Description |
| --- | --- | --- |
| [DeepEval contextual metrics](https://github.com/confident-ai/deepeval) | 🟢 Open source | DeepEval is an open-source LLM evaluation framework whose contextual precision, contextual recall, and contextual relevancy metrics assess retrieval ranking, evidence coverage, and signal-to-noise in supplied context. |
| [Ragas](https://github.com/vibrantlabsai/ragas) | 🟢 Open source | Ragas is an open-source evaluation toolkit with context precision, context recall, context relevance, faithfulness, response relevance, test-data generation, and experiment workflows for RAG applications. |
| [TruLens](https://github.com/truera/trulens) | 🟢 Open source | TruLens is an open-source evaluation and tracking library that instruments LLM applications and implements feedback functions including context relevance, groundedness, and answer relevance. |
| [RAGChecker](https://github.com/amazon-science/RAGChecker) | 🟢 Open source | RAGChecker is Amazon Science's fine-grained RAG evaluation framework, using claim-level entailment to diagnose retriever and generator errors separately. |
| [ARES](https://github.com/stanford-futuredata/ARES) | 🟢 Open source | ARES is Stanford's automated RAG evaluation system using synthetic queries, lightweight judges, and prediction-powered inference to estimate context relevance, faithfulness, and answer relevance. |
| [Tonic Validate](https://github.com/TonicAI/tonic_validate) | 🔵 Open core | Tonic Validate is an open-source RAG evaluation library and hosted product with retrieval precision and recall, answer similarity, faithfulness, benchmark datasets, and experiment visualization. |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | 🟢 Open source | AutoRAG is an open-source optimization framework that evaluates combinations of chunking, retrieval, reranking, and generation modules on a user dataset and selected metrics. |
| [Giskard](https://github.com/Giskard-AI/giskard-oss) | 🔵 Open core | Giskard is an open-source testing library and commercial platform for scanning RAG and agent applications for hallucination, prompt injection, sensitive-data leakage, and business failures. |
| [RAGTruth](https://github.com/ParticleMedia/RAGTruth) | 🟢 Open source | RAGTruth is a corpus and evaluation resource with word-level hallucination annotations across RAG responses, supporting groundedness analysis and detector development. |
| [BEIR](https://github.com/beir-cellar/beir) | 🟢 Open source | BEIR is an open-source benchmark and evaluation library for zero-shot information retrieval across heterogeneous datasets, with standard ranking metrics for retriever comparison. |

## Context Security and Privacy

**Context security** protects the instructions, retrieved content, memories, tools, and secrets that influence a model. Important controls include source trust, least-privilege tools, injection detection, PII redaction, immutable policy boundaries, output validation, approvals, and audit trails; no single scanner removes the need for system design.

| Tool | Availability | Description |
| --- | --- | --- |
| [Microsoft Presidio](https://github.com/microsoft/presidio) | 🟢 Open source | Microsoft Presidio is a framework for detecting, anonymizing, redacting, and synthesizing personally identifiable information in text, images, and structured data before or after model use. |
| [Prompt Guard](https://github.com/meta-llama/PurpleLlama/tree/main/Prompt-Guard) | 🟠 Open weights | Prompt Guard is Meta's downloadable classifier model for detecting jailbreaks and prompt injections in direct user input or untrusted external content. |
| [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) | 🟢 Open source | LlamaFirewall is Meta's runtime guardrail framework for agentic systems, combining prompt-injection detection, agent-alignment checks, and code-safety analysis around model and tool interactions. |
| [Lakera Guard](https://www.lakera.ai/lakera-guard) | 🔒 Commercial | Lakera Guard is a commercial API firewall for detecting prompt injection, jailbreaks, content-policy violations, and sensitive information in model inputs and outputs. |
| [Snyk Agent Scan](https://github.com/snyk/agent-scan) | 🟢 Open source | Snyk Agent Scan, formerly MCP-Scan, inventories agents, MCP servers, and skills and scans them for prompt injection, tool poisoning, shadowing, toxic flows, secrets, and malware-like instructions. |
| [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) | 🟢 Open source | Invariant Guardrails is a policy language and runtime for inspecting agent traces and enforcing constraints over messages, tool calls, data flows, PII, and security-sensitive actions. |
| [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 🟢 Open source | NeMo Guardrails is NVIDIA's framework for programmable input, retrieval, dialog, execution, and output rails, with Colang policies and integrations for safety and injection detection. |
| [DeepTeam](https://github.com/confident-ai/deepteam) | 🟢 Open source | DeepTeam is an open-source red-teaming framework for probing model applications for prompt injection, data leakage, unsafe behavior, bias, misinformation, and other configurable vulnerabilities. |
| [OpenAI Guardrails](https://github.com/openai/openai-guardrails-python) | 🟢 Open source | OpenAI Guardrails is a modular Python framework for running configurable input and output checks, including moderation, jailbreak detection, PII handling, and custom validators. |
| [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) | 🔒 Commercial | Amazon Bedrock Guardrails applies configurable content filters, denied topics, word filters, sensitive-information controls, automated reasoning checks, and contextual grounding checks to supported model applications. |
| [Azure AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) | 🔒 Commercial | Azure AI Content Safety provides moderation classifiers, Prompt Shields for direct and indirect injection, protected-material detection, groundedness checks, and custom blocklists through managed APIs. |
| [Google Model Armor](https://cloud.google.com/security-command-center/docs/model-armor-overview) | 🔒 Commercial | Google Model Armor screens prompts and responses for injection, jailbreaks, malicious URLs, sensitive data, and harmful content through Google Cloud security controls. |
| [Private AI](https://www.private-ai.com) | 🔒 Commercial | Private AI provides deployment-flexible APIs and containers for detecting, redacting, replacing, and re-identifying personal or sensitive information before data enters model context. |

## Discontinued and Historical Tools

Influential tools that are no longer generally available, are archived, or are being wound down. They are kept for the historical record and to prevent stale recommendations. Status notes reflect the last-reviewed date above.

| Tool | Former category | Availability | Status |
| --- | --- | --- | --- |
| [Humanloop](https://humanloop.com/docs/v5/guides/migrating-from-humanloop.md) | Prompt management | 🔒 Commercial | Humanloop was a prompt management, evaluation, and observability platform that shut down on September 8, 2025 after its team joined Anthropic; customer accounts and platform data were deleted. |
| [LLM Guard](https://github.com/protectai/llm-guard) | Context security | 🟢 Open source | LLM Guard is an archived open-source toolkit that provided prompt-injection, toxicity, token-limit, PII, and sensitive-output scanners; the repository remains available for reference and forks. |
| [Rebuff](https://github.com/protectai/rebuff) | Context security | 🟢 Open source | Rebuff is an archived open-source prompt-injection detector that combined heuristics, model-based detection, canary tokens, and an attack database; it is retained as an early layered-defense implementation. |
| [PromptSource](https://github.com/bigscience-workshop/promptsource) | Prompt authoring | 🟢 Open source | PromptSource is an archived BigScience toolkit for creating, versioning, and sharing natural-language prompt templates over datasets, used during the T0 research program. |
| [PromptHub](https://www.prompthub.us/) | Prompt management | 🔒 Commercial | PromptHub is a Git-style prompt registry whose service was [reported as winding down](https://www.promptlayer.com/blog/best-prompt-management-tools-2026-field-guide/) in mid-2026; its official site remained reachable at review time, so existing users should verify availability directly. |

## Key Papers and Concepts

Foundational reading for context assembly, retrieval, memory, compression, and long-context behavior. Papers describe methods; a paper is not assumed to provide maintained production software unless a tool row above links an implementation.

- **Retrieval-augmented generation** — [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (Lewis et al., 2020). Established the retrieve-then-generate architecture combining parametric and external memory.
- **ReAct** — [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (Yao et al., 2022). Interleaves reasoning traces with actions and observations, making tool results part of an agent's context loop.
- **Lost in the middle** — [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) (Liu et al., 2023). Shows that nominal context length does not imply uniform use of information at every position.
- **MemGPT** — [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) (Packer et al., 2023). Frames memory management as movement between limited working context and external storage; the project became Letta.
- **LLMLingua** — [LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models](https://arxiv.org/abs/2310.05736) (Jiang et al., 2023). Uses a smaller model to prune prompts under a token budget.
- **LongLLMLingua** — [LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression](https://arxiv.org/abs/2310.06839) (Jiang et al., 2023). Adds query-aware compression and reordering for long contexts.
- **Selective Context** — [Compressing Context to Enhance Inference Efficiency of Large Language Models](https://arxiv.org/abs/2310.06201) (Li et al., 2023). Uses self-information to remove less informative lexical units.
- **RAG evaluation** — [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) (Es et al., 2023). Defines reference-light metrics for retrieval and grounded generation.
- **Long-term memory evaluation** — [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) (Wu et al., 2024). Tests information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention.
- **ReSum** — [ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/abs/2509.13313) (Wu et al., 2025). Replaces growing web-agent histories with compact, restartable reasoning states.

## Glossary

Short definitions of terms used throughout this list.

- **Context** — all information made available to a model for one inference call, including instructions, messages, documents, examples, tools, schemas, and metadata represented in the request.
- **Context engineering** — designing the system that selects, transforms, orders, budgets, delivers, observes, and maintains model context.
- **Prompt engineering** — authoring and iterating instructions, examples, formatting, and model-facing language; one part of context engineering.
- **Context window** — the model-specific limit on tokens or other input units available to a request, usually shared across input and generated output according to provider rules.
- **RAG** — retrieval-augmented generation, where external documents are selected at request time and supplied as evidence for generation.
- **Agent memory** — persisted information from prior interactions or observations that can be recalled, revised, or summarized for future model calls.
- **Working state** — exact data needed to continue an executing workflow, such as graph state, checkpoints, pending actions, and tool results; not necessarily semantic memory.
- **Tool schema** — a machine-readable declaration of a callable operation, its purpose, parameters, and result shape supplied to a model.
- **MCP** — Model Context Protocol, an open protocol for connecting AI hosts and clients to servers exposing tools, resources, and prompts.
- **Chunking** — splitting source material into retrievable units; chunk boundaries, overlap, metadata, and token size influence retrieval quality.
- **Reranking** — rescoring retrieved candidates with a second model or algorithm before including the highest-value items in context.
- **Prompt compression** — pruning or rewriting input text to reduce tokens while attempting to preserve task-relevant information.
- **KV cache** — stored attention keys and values for already processed tokens, reused during autoregressive generation or across compatible requests.
- **Prompt cache** — reuse of model computation for an identical prefix; usually provider- and model-specific.
- **Semantic cache** — reuse of a previous response for a new request judged sufficiently similar, requiring explicit similarity and invalidation policies.
- **Structured output** — model output constrained or validated against a schema, grammar, regular expression, or type definition.
- **Trace** — a structured record of an application run containing model calls, retrievals, tool calls, inputs, outputs, timings, and metadata.
- **Contextual precision** — whether relevant retrieved items are ranked ahead of irrelevant items.
- **Contextual recall** — whether retrieved context covers the evidence needed for the expected answer.
- **Contextual relevancy** — how much of the supplied retrieval context is pertinent to the input rather than distracting noise.
- **Open weights** — downloadable model weights released under a license that is not necessarily OSI-approved.
- **Open core** — a business model pairing an open-source component with a commercial cloud or enterprise product.

## Frequently Asked Questions

**What is context engineering?**  
Context engineering is the design of the complete information pipeline surrounding an LLM call: instructions, conversation history, retrieved knowledge, memory, tools, state, examples, schemas, ordering, token budgets, caching, security, observation, and evaluation. Its goal is to supply the right information in the right form at the right time.

**How is context engineering different from prompt engineering?**  
Prompt engineering focuses on the authored language sent to a model—such as instructions and few-shot examples. Context engineering includes that work plus runtime retrieval, memory, tool definitions and results, state, compression, routing, caching, privacy controls, and feedback loops. A strong prompt cannot compensate for missing or untrusted runtime context.

**Is context engineering the same as RAG?**  
No. RAG retrieves external evidence and adds it to a request. A context-engineering system decides whether to retrieve, which sources and retrievers to use, how to parse, chunk, rank, compress, and cite results, how much token budget they receive, and how retrieval interacts with memory, tools, and instructions.

**What is the difference between RAG and agent memory?**  
RAG usually queries a knowledge corpus for task-relevant evidence. Agent memory stores information learned from prior interactions, such as user preferences, events, decisions, or procedures, and may update or forget it over time. Both ultimately retrieve information into a model's working context.

**Which tools are a practical starting point?**  
Choose by the bottleneck, not by category count. A typed application framework can assemble context; a parser and retrieval engine can support document grounding; a tokenizer can enforce limits; tracing can reveal what was sent; and a small evaluation set can catch regressions. Add dedicated memory, compression, or MCP only when the application requires them.

**When should I compress context instead of retrieving less?**  
First remove duplicated, stale, or irrelevant material and improve retrieval and reranking. Use compression when relevant content still exceeds the budget or when a long-running agent must preserve a compact state. Test compressed and uncompressed variants because compression can remove qualifiers, provenance, or evidence needed later.

**What does MCP solve?**  
MCP standardizes how AI applications connect to servers that expose tools, resources, and prompt templates. It reduces one-off integration code, but it does not determine which tools should be trusted, how much tool output belongs in context, or whether a model is authorized to act. Those remain application responsibilities.

**How do I evaluate context quality?**  
Keep a dataset of representative inputs and expected evidence. Measure retrieval ranking and coverage with contextual precision and recall, measure signal-to-noise with contextual relevancy, and evaluate answer groundedness separately. Inspect traces for failures caused by parsing, chunking, filters, stale memory, ordering, compression, or model behavior.

**What are the main context-security risks?**  
Common risks include direct and indirect prompt injection, malicious tool descriptions, excessive tool permissions, secrets or PII entering prompts, poisoned retrieval sources, cross-tenant memory, stale authorization context, and sensitive traces. Use source trust, least privilege, isolation, approvals, redaction, validation, audit logs, and adversarial testing together.

**How is prompt caching different from semantic caching?**  
Prompt caching reuses computation for an exact matching prefix and should not change the answer. Semantic caching returns or adapts a prior answer for a similar request, so its similarity threshold and invalidation policy can change behavior. Provider prompt caches and application semantic caches therefore have different correctness and privacy risks.

**How should I cite this list?**  
See [Citing This List](#citing-this-list) for a citation template and BibTeX. When citing an individual tool or method, prefer that entity's repository, documentation, or paper linked in its row.

## Methodology

How this list is built and maintained. This section exists so readers and AI systems can judge how much to trust it.

- **Scope.** Tools whose primary or substantial function is assembling, retrieving, storing, compressing, routing, caching, constraining, observing, evaluating, or protecting context for LLMs and agents. General model training and inference projects are included only when they provide first-class long-context processing or cache management.
- **Inclusion criteria.** Open-source projects should show current activity or lasting reference value. Commercial products must expose relevant, documented functionality. Research methods appear in tool tables only when runnable code or a usable model is available; papers without maintained tooling stay in [Key Papers and Concepts](#key-papers-and-concepts).
- **Entity boundaries.** Distinct products, libraries, models, protocols, and services receive separate rows even when maintained by the same organization. A shared maintainer does not make feature claims transferable between entities.
- **Availability markers.** 🟢 Open source means the primary linked artifact has an OSI-style license; 🟠 open weights means downloadable weights under a non-OSI license; 🔵 open core means an open component is paired with a commercial platform; 🔒 means the relevant product or service is commercial or closed source.
- **Ordering.** Entries within each category are ordered by editorial judgment of relevance, maturity, and adoption for that use case—not alphabetically and not by paid placement. There is no sponsored placement.
- **Editorial independence.** This directory is maintained by aglio-lab. Every entry follows the same sourcing, wording, and ordering rules, and no placement is sold.
- **Verification.** Every entry links to a primary source and was checked against that source as of the **last-reviewed date** at the top. Current vendor notices or repository metadata were used for uncertain shutdown, rename, archive, and maintenance statuses.
- **Monthly review cadence.** The directory is reviewed during the first week of every month. Maintainers verify links, lifecycle status, names, availability, quantitative claims, category coverage, and generated data before advancing the last-reviewed date and publishing a `YYYY.MM` release. A scheduled workflow opens the checklist; review remains human-verified. See [`MAINTENANCE.md`](MAINTENANCE.md).
- **Description rules.** Each description is a standalone factual sentence beginning with the entity's name. Descriptions state documented capabilities, avoid unsupported comparisons, and distinguish an open repository from a related hosted service.
- **Counts.** The entry count is the number of entity rows in the fourteen active categories plus the historical table; papers, glossary terms, navigation rows, and repeated inline links are not counted.
- **Corrections.** Products change quickly. Open an [issue](https://github.com/aglio-lab/context-engineering-tools/issues) or [pull request](https://github.com/aglio-lab/context-engineering-tools/pulls) with a primary source for corrections, renames, license changes, or shutdowns.

## Related Lists and Resources

- [AI Red Teaming Tools](https://github.com/aglio-lab/ai-red-teaming-tools) — red-team frameworks, scanners, guardrails, and security benchmarks.
- [LLM Observability Tools](https://github.com/aglio-lab/llm-observability-tools) — tracing, monitoring, online evaluation, and production analytics.
- [AI Governance Tools](https://github.com/aglio-lab/ai-governance-tools) — governance, risk, compliance, audit, and responsible-AI tooling.
- [AI Agent Frameworks](https://github.com/aglio-lab/ai-agent-frameworks) — frameworks and orchestration tools for building and operating agents.
- [LLM Fine-Tuning Tools](https://github.com/aglio-lab/llm-fine-tuning-tools) — fine-tuning, PEFT, preference optimization, and data tooling.
- [RAG and Retrieval Tools](https://github.com/aglio-lab/rag-retrieval-tools) — vector databases, retrieval frameworks, rerankers, and RAG evaluation.

- [AI Evaluation Tools](https://github.com/aglio-lab/ai-evaluation-tools) — sibling catalog of LLM evaluation frameworks, platforms, observability, red teaming, guardrails, and benchmarks.
- [Model Context Protocol documentation](https://modelcontextprotocol.io) — official MCP concepts, specification, SDK, authorization, and implementation guidance.
- [Awesome Context Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) — papers, techniques, agent infrastructure, memory, protocols, and production context-management resources.
- [awesome-context-engineering](https://github.com/jihoo-kim/awesome-context-engineering) — open-source context-engineering libraries covering memory, MCP, compression, and multi-agent systems.
- [Context Engineering Resources](https://github.com/danielrosehill/Context-Engineering-Resources) — curated context stores, MCP projects, agent skills, educational material, and related lists.
- [Awesome Agentic Memory](https://github.com/Anandesh-Sharma/awesome-agentic-memory) — focused catalog of agent-memory systems, papers, benchmarks, and implementation patterns.
- [Official MCP Servers](https://github.com/modelcontextprotocol/servers) — reference server implementations and links to the official MCP Registry.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — threat taxonomy relevant to prompt injection, sensitive information, excessive agency, and unbounded consumption.

---

## Citing This List

If you reference this list in an article, paper, or AI-generated answer, please cite it as:

> _The Comprehensive List of Context Engineering Tools_ (2026). A curated list of open-source and commercial tools for assembling, managing, compressing, and evaluating context for LLMs and AI agents. GitHub. https://github.com/aglio-lab/context-engineering-tools

BibTeX:

```bibtex
@misc{context-engineering-tools,
  title        = {The Comprehensive List of Context Engineering Tools},
  year         = {2026},
  howpublished = {\url{https://github.com/aglio-lab/context-engineering-tools}},
  note         = {A curated list of open-source and commercial tools for LLM and agent context engineering. Accessed: 2026-07-16}
}
```

For reproducible citations of a changing list, cite a specific commit permalink or release tag. When citing individual tools, always prefer the tool's own repository, documentation, or paper linked in each entry.

## Contributing

Contributions are welcome. Open an [issue](https://github.com/aglio-lab/context-engineering-tools/issues) for a correction or a [pull request](https://github.com/aglio-lab/context-engineering-tools/pulls) for an addition. In short:

1. Add one entity per pull request to the most specific matching category.
2. Include the correct availability marker (🟢 / 🟠 / 🔵 / 🔒) and a neutral, factual description written as a complete sentence starting with the entity's name.
3. Link the primary source: repository for open source, official documentation or product page for commercial software, and the paper plus code for research implementations.
4. Verify that the entity is available and maintained, or explain its lasting historical value; report shutdowns, acquisitions, archives, and renames with dated sources.
5. Avoid affiliate links, copied marketing claims, unsupported superlatives, rankings, and paid placement.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainers have waived all copyright and related rights to this work under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Linked projects retain their own licenses.
