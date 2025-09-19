# AI Capability Map — ShopLite

| Capability | Intent (user) | Inputs (this sprint) | Risk 1–5 (tag) | p95 ms | Est. cost/action | Fallback | Selected |
|---|---|---|---|---:|---:|---|:---:|
| Typeahead (search suggestions) | User wants instant product suggestions while typing | Query string (1–20 chars), locale | 2 | 300 | $0.0023 | Client-side fuzzy search | Yes |
| Support assistant (FAQ + order status) | User asks questions like “Where is my order?” or general FAQ | User message, FAQ markdown, `order-status` API | 3 | 1200 | $0.0600 | Show FAQ answer + escalate to human | Yes |
| Product summary | User wants a short AI-generated product description | Product title + specs | 3 | 800 | $0.012 | Show raw description text |  |
| Personalized homepage recommendations | User wants to see relevant products | Browsing history + SKU metadata | 4 | 900 | $0.025 | Default trending products |  |

---

### Why these two

We selected **Typeahead** and **Support assistant** because they directly connect to ShopLite’s KPIs:  
* **Typeahead** can improve conversion rate by helping users quickly find products from a large catalog (10k SKUs).  
* **Support assistant** can reduce support contacts by automatically answering FAQ and simple order-status questions.  
Both have relatively low integration risk since ShopLite already has an FAQ markdown and an `order-status` API. Their latency and cost targets are within feasible ranges using today’s small language models.
