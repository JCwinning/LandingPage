# RAG Search Results

**Query:** What are model variants?
**Search Date:** 2025-11-22 00:50:59
**Results Found:** 10

---

## Result 1

**Relevance Score:** 0.5236
**Source:** docs_faq_how-are-rate-limits-calculated.md

**Content:**
> When you make a request to OpenRouter, we receive the total number of tokens processed
> by the provider. We then calculate the corresponding cost and deduct it from your credits.
> You can review your complete usage history in the [Activity tab](https://openrouter.ai/activity).
> 
> You can also add the `usage: {include: true}` parameter to your chat request
> to get the usage information in the response.
> 
> We pass through the pricing of the underlying providers; there is no markup
> on inference pricing (however we do charge a [fee](/docs/faq#pricing-and-fees) when purchasing credits).
> 
> ## Pricing and Fees
> 
> ###### What are the fees for using OpenRouter?

---

## Result 2

**Relevance Score:** 0.5011
**Source:** docs_faq_how-are-rate-limits-calculated.md

**Content:**
> ###### What is the expected latency/response time for different models?
> 
> For each model on OpenRouter we show the latency (time to first token) and the token
> throughput for all providers. You can use this to estimate how long requests
> will take. If you would like to optimize for throughput you can use the
> `:nitro` variant to route to the fastest provider.
> 
> ###### How does model fallback work if a provider is unavailable?
> 
> If a provider returns an error OpenRouter will automatically fall back to the
> next provider. This happens transparently to the user and allows production
> apps to be much more resilient. OpenRouter has a lot of options to configure
> the provider routing behavior. The full documentation can be found [here](/docs/features/provider-routing).
> 
> ## API Technical Specifications

---

## Result 3

**Relevance Score:** 0.5011
**Source:** docs_faq.md

**Content:**
> ###### What is the expected latency/response time for different models?
> 
> For each model on OpenRouter we show the latency (time to first token) and the token
> throughput for all providers. You can use this to estimate how long requests
> will take. If you would like to optimize for throughput you can use the
> `:nitro` variant to route to the fastest provider.
> 
> ###### How does model fallback work if a provider is unavailable?
> 
> If a provider returns an error OpenRouter will automatically fall back to the
> next provider. This happens transparently to the user and allows production
> apps to be much more resilient. OpenRouter has a lot of options to configure
> the provider routing behavior. The full documentation can be found [here](/docs/features/provider-routing).
> 
> ## API Technical Specifications

---

## Result 4

**Relevance Score:** 0.4857
**Source:** docs_faq_how-are-rate-limits-calculated.md

**Content:**
> Light
> 
> On this page
> 
> * [Getting started](#getting-started)
> * [Pricing and Fees](#pricing-and-fees)
> * [Models and Providers](#models-and-providers)
> * [API Technical Specifications](#api-technical-specifications)
> * [Privacy and Data Logging](#privacy-and-data-logging)
> * [Credit and Billing Systems](#credit-and-billing-systems)
> * [Account Management](#account-management)
> 
> [Overview](/docs/quickstart)
> 
> # Frequently Asked Questions
> 
> Copy page
> 
> Common questions about OpenRouter
> 
> ## Getting started
> 
> ###### Why should I use OpenRouter?
> 
> OpenRouter provides a unified API to access all the major LLM models on the
> market. It also allows users to aggregate their billing in one place and
> keep track of all of their usage using our analytics.

---

## Result 5

**Relevance Score:** 0.4697
**Source:** docs_use-cases_organization-management.md

**Content:**
> ### Administrator Permissions
> 
> * **View All Keys**: Administrators can view all API keys created within the organization
> * **Manage All Keys**: Full access to edit, disable, or delete any organization API key
> * **Monitor Usage**: Access to detailed usage analytics for all organization keys
> 
> #####
> 
> When creating API keys within an organization, consider using descriptive names that indicate the key’s purpose or the team member responsible for it.
> 
> ## Activity and Usage Tracking
> 
> ### Organization-Wide Activity Feed
> 
> When viewing your activity feed while in organization context, you’ll see:

---

## Result 6

**Relevance Score:** 0.4663
**Source:** docs_faq.md

**Content:**
> ###### Is there a fee for using my own provider keys (BYOK)?
> 
> Yes, if you choose to use your own provider API keys (Bring Your Own Key -
> BYOK), the first 1M BYOK
> requests per-month are free, and for all subsequent usage there is a fee
> of 5% of what the same
> model and provider would normally cost on OpenRouter. This fee is deducted
> from your OpenRouter credits. This allows you to manage your rate limits and
> costs directly with the provider while still leveraging OpenRouter’s unified
> interface.
> 
> ## Models and Providers
> 
> ###### What LLM models does OpenRouter support?

---

## Result 7

**Relevance Score:** 0.4662
**Source:** docs_faq_how-are-rate-limits-calculated.md

**Content:**
> ###### Is there a fee for using my own provider keys (BYOK)?
> 
> Yes, if you choose to use your own provider API keys (Bring Your Own Key -
> BYOK), the first 1M BYOK
> requests per-month are free, and for all subsequent usage there is a fee
> of 5% of what the same
> model and provider would normally cost on OpenRouter. This fee is deducted
> from your OpenRouter credits. This allows you to manage your rate limits and
> costs directly with the provider while still leveraging OpenRouter’s unified
> interface.
> 
> ## Models and Providers
> 
> ###### What LLM models does OpenRouter support?

---

## Result 8

**Relevance Score:** 0.4640
**Source:** docs_faq_how-are-rate-limits-calculated.md

**Content:**
> ###### What are model variants?
> 
> Variants are suffixes that can be added to the model slug to change its behavior.
> 
> Static variants can only be used with specific models and these are listed in our [models api](https://openrouter.ai/api/v1/models).
> 
> 1. `:free` - The model is always provided for free and has low rate limits.
> 2. `:beta` - The model is not moderated by OpenRouter.
> 3. `:extended` - The model has longer than usual context length.
> 4. `:exacto` - The model only uses OpenRouter-curated high-quality endpoints.
> 5. `:thinking` - The model supports reasoning by default.
> 
> Dynamic variants can be used on all models and they change the behavior of how the request is routed or used.

---

## Result 9

**Relevance Score:** 0.4640
**Source:** docs_faq.md

**Content:**
> ###### What are model variants?
> 
> Variants are suffixes that can be added to the model slug to change its behavior.
> 
> Static variants can only be used with specific models and these are listed in our [models api](https://openrouter.ai/api/v1/models).
> 
> 1. `:free` - The model is always provided for free and has low rate limits.
> 2. `:beta` - The model is not moderated by OpenRouter.
> 3. `:extended` - The model has longer than usual context length.
> 4. `:exacto` - The model only uses OpenRouter-curated high-quality endpoints.
> 5. `:thinking` - The model supports reasoning by default.
> 
> Dynamic variants can be used on all models and they change the behavior of how the request is routed or used.

---

## Result 10

**Relevance Score:** 0.4536
**Source:** docs_faq_how-are-rate-limits-calculated.md

**Content:**
> + [Python SDK](/docs/sdks/python)
>   + [TypeScript SDK](/docs/sdks/typescript)
> * Use Cases
> 
>   + [BYOK](/docs/use-cases/byok)
>   + [Crypto API](/docs/use-cases/crypto-api)
>   + [OAuth PKCE](/docs/use-cases/oauth-pkce)
>   + [MCP Servers](/docs/use-cases/mcp-servers)
>   + [Organization Management](/docs/use-cases/organization-management)
>   + [For Providers](/docs/use-cases/for-providers)
>   + [Reasoning Tokens](/docs/use-cases/reasoning-tokens)
>   + [Usage Accounting](/docs/use-cases/usage-accounting)
>   + [User Tracking](/docs/use-cases/user-tracking)
> * Community

---

