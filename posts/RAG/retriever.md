# Query: What are model variants?

# Retrieved 3 chunks from openrouter.duckdb

────────────────────────────────────────────────────────────
## Chunk 1

**Similarity Score:** 0.6169

**Metadata:**
- file_path: /Users/jinchaoduan/Documents/post_project/AI_Blog/posts/RAG/markdown_docs/docs_features_exacto-variant.md
- file_name: docs_features_exacto-variant.md
- file_type: text/markdown
- file_size: 7972
- creation_date: 2025-11-21
- last_modified_date: 2025-11-21

Search

`/`

Ask AI

[API](/docs/api-reference/overview)[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Ranking](https://openrouter.ai/rankings)

* Overview

  + [Quickstart](/docs/quickstart)
  + [FAQ](/docs/faq)
  + [Principles](/docs/overview/principles)
  + [Models](/docs/overview/models)
  + [Enterprise](https://openrouter.ai/enterprise)
* Features

  + [Privacy and Logging](/docs/features/privacy-and-logging)
  + [Zero Data Retention (ZDR)](/docs/features/zdr)
  + [Model Routing](/docs/features/model-routing)
  + [Provider Routing](/docs/features/provider-routing)
  + [Exacto Variant](/docs/features/exacto-variant)
  + [Latency and Performance](/docs/features/latency-and-performance)
  + [Presets](/docs/features/presets)
  + [Prompt Caching](/docs/features/prompt-caching)
  + [Structured Outputs](/docs/features/structured-outputs)
  + [Tool Calling](/docs/features/tool-calling)
  + Multimodal
  + [Message Transforms](/docs/features/message-transforms)
  + [Uptime Optimization](/docs/features/uptime-optimization)
  + [Web Search](/docs/features/web-search)
  + [Zero Completion Insurance](/docs/features/zero-completion-insurance)
  + [Provisioning API Keys](/docs/features/provisioning-api-keys)
  + [App Attribution](/docs/app-attribution)
* API Reference

  + [Overview](/docs/api-reference/overview)
  + [Streaming](/docs/api-reference/streaming)
  + [Embeddings](/docs/api-reference/embeddings)
  + [Limits](/docs/api-reference/limits)
  + [Authentication](/docs/api-reference/authentication)
  + [Parameters](/docs/api-reference/parameters)
  + [Errors](/docs/api-reference/errors)
  + Responses API
  + beta.responses
  + Analytics
  + Credits
  + Embeddings
  + Generations
  + Models
  + Endpoints
  + Parameters
  + Providers
  + API Keys
  + O Auth
  + Chat
  + Completions
* SDK Reference (BETA)

  + [Python SDK](/docs/sdks/python)
  + [TypeScript SDK](/docs/sdks/typescript)
* Use Cases

  + [BYOK](/docs/use-cases/byok)
  + [Crypto API](/docs/use-cases/crypto-api)
  + [OAuth PKCE](/docs/use-cases/oauth-pkce)
  + [MCP Servers](/docs/use-cases/mcp-servers)
  + [Organization Management](/docs/use-cases/organization-management)
  + [For Providers](/docs/use-cases/for-providers)
  + [Reasoning Tokens](/docs/use-cases/reasoning-tokens)
  + [Usage Accounting](/docs/use-cases/usage-accounting)
  + [User Tracking](/docs/use-cases/user-tracking)
* Community

  + [Frameworks and Integrations Overview](/docs/community/frameworks-and-integrations-overview)
  + [Effect AI SDK](/docs/community/effect-ai-sdk)
  + [Arize](/docs/community/arize)
  + [LangChain](/docs/community/lang-chain)
  + [LiveKit](/docs/community/live-kit)
  + [Langfuse](/docs/community/langfuse)
  + [Mastra](/docs/community/mastra)
  + [OpenAI SDK](/docs/community/open-ai-sdk)
  + [PydanticAI](/docs/community/pydantic-ai)
  + [Vercel AI SDK](/docs/community/vercel-ai-sdk)
  + [Xcode](/docs/community/xcode)
  + [Zapier](/docs/community/zapier)
  + [Discord](https://discord.gg/openrouter)

Light

On this page

* [Using the Exacto Variant](#using-the-exacto-variant)
* [What Is the Exacto Variant?](#what-is-the-exacto-variant)
* [Why Use Exacto?](#why-use-exacto)
* [Why We Built It](#why-we-built-it)
* [Recommended Use Cases](#recommended-use-cases)
* [Supported Models](#supported-models)
* [How We Select Providers](#how-we-select-providers)

[Features](/docs/features/privacy-and-logging)

# Exacto Variant

Copy page

Route requests through OpenRouter-curated providers

Introducing a new set of endpoints, `:exacto`, focused on higher tool‑calling accuracy by routing to a sub‑group of providers with measurably better tool‑use success rates. It uses the same request payloads as any other variant, but filters endpoints so that only vetted providers for the chosen model are considered. To learn more, read our [blog post](https://openrouter.ai/announcements/provider-variance-introducing-exacto).

## Using the Exacto Variant

Add `:exacto` to the end of any supported model slug. The curated allowlist is enforced before provider sorting, fallback, or load balancing — no extra provider preference config is required.

TypeScript SDKTypeScript (OpenAI SDK)cURL

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: process.env.OPENROUTER_API_KEY, |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: "moonshotai/kimi-k2-0905:exacto", |
| 9 | messages: [ |
| 10 | { |
| 11 | role: "user", |
| 12 | content: "Draft a concise changelog entry for the Exacto launch.", |
| 13 | }, |
| 14 | ], |
| 15 | stream: false, |
| 16 | }); |
| 17 |  |
| 18 | console.log(completion.choices[0].message.content); |
```

#####

You can still supply fallback models with the `models` array. Any model that
carries the `:exacto` suffix will enforce the curated provider list when it is
selected.

## What Is the Exacto Variant?

Exacto is a curated routing variant specifically focused on tool‑calling accuracy. Unlike standard routing, which considers all available providers for a model, Exacto restricts routing to providers that demonstrate higher tool‑use accuracy and normal tool‑use propensity on real workloads.

## Why Use Exacto?

### Why We Built It

Providers running the same model can differ in accuracy due to implementation details in production inference. OpenRouter sees billions of requests monthly, giving us a unique vantage point to observe these differences and minimize surprises for users. Exacto combines benchmark results with real‑world tool‑calling telemetry to select the best‑performing providers.

### Recommended Use Cases

Exacto is optimized for quality‑sensitive, agentic workflows where tool‑calling accuracy and reliability are critical.

## Supported Models

Exacto endpoints are available for:

* Kimi K2 (`moonshotai/kimi-k2-0905:exacto`)
* DeepSeek v3.1 Terminus (`deepseek/deepseek-v3.1-terminus:exacto`)
* GLM 4.6 (`z-ai/glm-4.6:exacto`)
* GPT‑OSS 120B (`openai/gpt-oss-120b:exacto`)
* Qwen3 Coder (`qwen/qwen3-coder:exacto`)

## How We Select Providers

We use three inputs:

* Tool‑calling accuracy from real traffic across billions of calls
* Real‑time provider preferences (pins/ignores) from users making tool calls
* Benchmarking (internal eval suites, Groq OpenBench running LiveMCPBench, official tau2bench, and similar)

You will be routed only to providers that:

1. Are top‑tier on tool‑calling accuracy
2. Fall within a normal range of tool‑calling propensity
3. Are not frequently ignored or blacklisted by users when tools are provided

In our evaluations and open‑source benchmarks (e.g., tau2‑Bench, LiveMCPBench), Exacto shows materially fewer tool‑calling failures and more reliable tool use.

We will continue working with providers not currently in the Exacto pool to help them improve and be included. Exacto targets tool‑calling specifically and is not a broad statement on overall provider quality.

#####

If you have feedback on the Exacto variant, please fill out this form:
<https://openrouter.notion.site/2932fd57c4dc8097ba74ffb6d27f39d1?pvs=105>

Was this page helpful?

────────────────────────────────────────────────────────────
## Chunk 2

**Similarity Score:** 0.6099

**Metadata:**
- file_path: /Users/jinchaoduan/Documents/post_project/AI_Blog/posts/RAG/markdown_docs/docs_overview_models.md
- file_name: docs_overview_models.md
- file_type: text/markdown
- file_size: 9021
- creation_date: 2025-11-21
- last_modified_date: 2025-11-21

Search

`/`

Ask AI

[API](/docs/api-reference/overview)[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Ranking](https://openrouter.ai/rankings)

* Overview

  + [Quickstart](/docs/quickstart)
  + [FAQ](/docs/faq)
  + [Principles](/docs/overview/principles)
  + [Models](/docs/overview/models)
  + [Enterprise](https://openrouter.ai/enterprise)
* Features

  + [Privacy and Logging](/docs/features/privacy-and-logging)
  + [Zero Data Retention (ZDR)](/docs/features/zdr)
  + [Model Routing](/docs/features/model-routing)
  + [Provider Routing](/docs/features/provider-routing)
  + [Exacto Variant](/docs/features/exacto-variant)
  + [Latency and Performance](/docs/features/latency-and-performance)
  + [Presets](/docs/features/presets)
  + [Prompt Caching](/docs/features/prompt-caching)
  + [Structured Outputs](/docs/features/structured-outputs)
  + [Tool Calling](/docs/features/tool-calling)
  + Multimodal
  + [Message Transforms](/docs/features/message-transforms)
  + [Uptime Optimization](/docs/features/uptime-optimization)
  + [Web Search](/docs/features/web-search)
  + [Zero Completion Insurance](/docs/features/zero-completion-insurance)
  + [Provisioning API Keys](/docs/features/provisioning-api-keys)
  + [App Attribution](/docs/app-attribution)
* API Reference

  + [Overview](/docs/api-reference/overview)
  + [Streaming](/docs/api-reference/streaming)
  + [Embeddings](/docs/api-reference/embeddings)
  + [Limits](/docs/api-reference/limits)
  + [Authentication](/docs/api-reference/authentication)
  + [Parameters](/docs/api-reference/parameters)
  + [Errors](/docs/api-reference/errors)
  + Responses API
  + beta.responses
  + Analytics
  + Credits
  + Embeddings
  + Generations
  + Models
  + Endpoints
  + Parameters
  + Providers
  + API Keys
  + O Auth
  + Chat
  + Completions
* SDK Reference (BETA)

  + [Python SDK](/docs/sdks/python)
  + [TypeScript SDK](/docs/sdks/typescript)
* Use Cases

  + [BYOK](/docs/use-cases/byok)
  + [Crypto API](/docs/use-cases/crypto-api)
  + [OAuth PKCE](/docs/use-cases/oauth-pkce)
  + [MCP Servers](/docs/use-cases/mcp-servers)
  + [Organization Management](/docs/use-cases/organization-management)
  + [For Providers](/docs/use-cases/for-providers)
  + [Reasoning Tokens](/docs/use-cases/reasoning-tokens)
  + [Usage Accounting](/docs/use-cases/usage-accounting)
  + [User Tracking](/docs/use-cases/user-tracking)
* Community

  + [Frameworks and Integrations Overview](/docs/community/frameworks-and-integrations-overview)
  + [Effect AI SDK](/docs/community/effect-ai-sdk)
  + [Arize](/docs/community/arize)
  + [LangChain](/docs/community/lang-chain)
  + [LiveKit](/docs/community/live-kit)
  + [Langfuse](/docs/community/langfuse)
  + [Mastra](/docs/community/mastra)
  + [OpenAI SDK](/docs/community/open-ai-sdk)
  + [PydanticAI](/docs/community/pydantic-ai)
  + [Vercel AI SDK](/docs/community/vercel-ai-sdk)
  + [Xcode](/docs/community/xcode)
  + [Zapier](/docs/community/zapier)
  + [Discord](https://discord.gg/openrouter)

Light

On this page

* [Models API Standard](#models-api-standard)
* [API Response Schema](#api-response-schema)
* [Root Response Object](#root-response-object)
* [Model Object Schema](#model-object-schema)
* [Architecture Object](#architecture-object)
* [Pricing Object](#pricing-object)
* [Top Provider Object](#top-provider-object)
* [Supported Parameters](#supported-parameters)
* [For Providers](#for-providers)

[Overview](/docs/quickstart)

# Models

Copy page

One API for hundreds of models

Explore and browse 400+ models and providers [on our website](/models), or [with our API](/docs/api-reference/models/get-models). You can also subscribe to our [RSS feed](/api/v1/models?use_rss=true) to stay updated on new models.

## Models API Standard

Our [Models API](/docs/api-reference/models/get-models) makes the most important information about all LLMs freely available as soon as we confirm it.

### API Response Schema

The Models API returns a standardized JSON response format that provides comprehensive metadata for each available model. This schema is cached at the edge and designed for reliable integration for production applications.

#### Root Response Object

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | /* Array of Model objects */ |
| 4 | ] |
| 5 | } |
```

#### Model Object Schema

Each model in the `data` array contains the following standardized fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique model identifier used in API requests (e.g., `"google/gemini-2.5-pro-preview"`) |
| `canonical_slug` | `string` | Permanent slug for the model that never changes |
| `name` | `string` | Human-readable display name for the model |
| `created` | `number` | Unix timestamp of when the model was added to OpenRouter |
| `description` | `string` | Detailed description of the model’s capabilities and characteristics |
| `context_length` | `number` | Maximum context window size in tokens |
| `architecture` | `Architecture` | Object describing the model’s technical capabilities |
| `pricing` | `Pricing` | Lowest price structure for using this model |
| `top_provider` | `TopProvider` | Configuration details for the primary provider |
| `per_request_limits` | Rate limiting information (null if no limits) |  |
| `supported_parameters` | `string[]` | Array of supported API parameters for this model |

#### Architecture Object

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "input_modalities": string[], // Supported input types: ["file", "image", "text"] |
| 3 | "output_modalities": string[], // Supported output types: ["text"] |
| 4 | "tokenizer": string,          // Tokenization method used |
| 5 | "instruct_type": string | null // Instruction format type (null if not applicable) |
| 6 | } |
```

#### Pricing Object

All pricing values are in USD per token/request/unit. A value of `"0"` indicates the feature is free.

────────────────────────────────────────────────────────────
## Chunk 3

**Similarity Score:** 0.5820

**Metadata:**
- file_path: /Users/jinchaoduan/Documents/post_project/AI_Blog/posts/RAG/markdown_docs/docs_guides_overview_models.md
- file_name: docs_guides_overview_models.md
- file_type: text/markdown
- file_size: 7557
- creation_date: 2026-01-06
- last_modified_date: 2026-01-06

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Ranking](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/call-model/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/call-model/overview)

* Overview

  + [Quickstart](/docs/quickstart)
  + [Principles](/docs/guides/overview/principles)
  + [Models](/docs/guides/overview/models)
  + Multimodal
  + Authentication
  + [FAQ](/docs/faq)
  + [Enterprise](https://openrouter.ai/enterprise)
* Models & Routing

  + [Auto Model Selection](/docs/guides/routing/auto-model-selection)
  + [Model Fallbacks](/docs/guides/routing/model-fallbacks)
  + [Provider Selection](/docs/guides/routing/provider-selection)
  + Model Variants
* Features

  + [Presets](/docs/guides/features/presets)
  + [Tool Calling](/docs/guides/features/tool-calling)
  + Plugins
  + [Structured Outputs](/docs/guides/features/structured-outputs)
  + [Message Transforms](/docs/guides/features/message-transforms)
  + [Model Routing](/docs/guides/features/model-routing)
  + Routers
  + [Zero Completion Insurance](/docs/guides/features/zero-completion-insurance)
  + [ZDR](/docs/guides/features/zdr)
  + [App Attribution](/docs/app-attribution)
  + Broadcast
* + Privacy
  + Best Practices
  + Guides
  + Community

Light

On this page

* [Models API Standard](#models-api-standard)
* [API Response Schema](#api-response-schema)
* [Root Response Object](#root-response-object)
* [Model Object Schema](#model-object-schema)
* [Architecture Object](#architecture-object)
* [Pricing Object](#pricing-object)
* [Top Provider Object](#top-provider-object)
* [Supported Parameters](#supported-parameters)
* [For Providers](#for-providers)

[Overview](/docs/quickstart)

# Models

Copy page

One API for hundreds of models

Explore and browse 400+ models and providers [on our website](/models), or [with our API](/docs/api-reference/models/get-models). You can also subscribe to our [RSS feed](/api/v1/models?use_rss=true) to stay updated on new models.

## Models API Standard

Our [Models API](/docs/api-reference/models/get-models) makes the most important information about all LLMs freely available as soon as we confirm it.

### API Response Schema

The Models API returns a standardized JSON response format that provides comprehensive metadata for each available model. This schema is cached at the edge and designed for reliable integration with production applications.

#### Root Response Object

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | /* Array of Model objects */ |
| 4 | ] |
| 5 | } |
```

#### Model Object Schema

Each model in the `data` array contains the following standardized fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique model identifier used in API requests (e.g., `"google/gemini-2.5-pro-preview"`) |
| `canonical_slug` | `string` | Permanent slug for the model that never changes |
| `name` | `string` | Human-readable display name for the model |
| `created` | `number` | Unix timestamp of when the model was added to OpenRouter |
| `description` | `string` | Detailed description of the model’s capabilities and characteristics |
| `context_length` | `number` | Maximum context window size in tokens |
| `architecture` | `Architecture` | Object describing the model’s technical capabilities |
| `pricing` | `Pricing` | Lowest price structure for using this model |
| `top_provider` | `TopProvider` | Configuration details for the primary provider |
| `per_request_limits` | Rate limiting information (null if no limits) |  |
| `supported_parameters` | `string[]` | Array of supported API parameters for this model |

#### Architecture Object

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "input_modalities": string[], // Supported input types: ["file", "image", "text"] |
| 3 | "output_modalities": string[], // Supported output types: ["text"] |
| 4 | "tokenizer": string,          // Tokenization method used |
| 5 | "instruct_type": string | null // Instruction format type (null if not applicable) |
| 6 | } |
```

#### Pricing Object

All pricing values are in USD per token/request/unit. A value of `"0"` indicates the feature is free.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "prompt": string,           // Cost per input token |
| 3 | "completion": string,       // Cost per output token |
| 4 | "request": string,          // Fixed cost per API request |
| 5 | "image": string,           // Cost per image input |
| 6 | "web_search": string,      // Cost per web search operation |
| 7 | "internal_reasoning": string, // Cost for internal reasoning tokens |
| 8 | "input_cache_read": string,   // Cost per cached input token read |
| 9 | "input_cache_write": string   // Cost per cached input token write |
| 10 | } |
```

#### Top Provider Object

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "context_length": number,        // Provider-specific context limit |
| 3 | "max_completion_tokens": number, // Maximum tokens in response |
| 4 | "is_moderated": boolean         // Whether content moderation is applied |
| 5 | } |
```

#### Supported Parameters

The `supported_parameters` array indicates which OpenAI-compatible parameters work with each model:

* `tools` - Function calling capabilities
* `tool_choice` - Tool selection control
* `max_tokens` - Response length limiting
* `temperature` - Randomness control
* `top_p` - Nucleus sampling
* `reasoning` - Internal reasoning mode
* `include_reasoning` - Include reasoning in response
* `structured_outputs` - JSON schema enforcement
* `response_format` - Output format specification
* `stop` - Custom stop sequences
* `frequency_penalty` - Repetition reduction
* `presence_penalty` - Topic diversity
* `seed` - Deterministic outputs

##### Different models tokenize text in different ways

Some models break up text into chunks of multiple characters (GPT, Claude,
Llama, etc), while others tokenize by character (PaLM). This means that token
counts (and therefore costs) will vary between models, even when inputs and
outputs are the same. Costs are displayed and billed according to the
tokenizer for the model in use. You can use the `usage` field in the response
to get the token counts for the input and output.

If there are models or providers you are interested in that OpenRouter doesn’t have, please tell us about them in our [Discord channel](https://openrouter.ai/discord).

## For Providers

If you’re interested in working with OpenRouter, you can learn more on our [providers page](/docs/use-cases/for-providers).

Was this page helpful?

YesNo

[Previous](/docs/guides/overview/principles)[#### Multimodal Capabilities

Send images, PDFs, audio, and video to OpenRouter models

Next](/docs/guides/overview/multimodal/overview)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Ranking](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

