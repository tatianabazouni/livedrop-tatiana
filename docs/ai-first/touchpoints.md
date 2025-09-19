# Touchpoint Specs — ShopLite

---

## 1. Typeahead (Search Suggestions)

### Problem Statement
Users often abandon searches when they can’t find products quickly. With 10k SKUs, naive string matching is slow and inaccurate. AI-powered typeahead can interpret partial queries, synonyms, and typos to surface relevant SKUs instantly, boosting conversion.

### Happy Path
1. User begins typing a query into the search box.  
2. Frontend sends partial query (1–20 characters) to API endpoint.  
3. API checks local cache; if hit, return cached suggestions.  
4. If cache miss, API forwards query to LLM with product catalog embeddings.  
5. Model returns top 5 relevant SKU names and IDs.  
6. API validates results (only SKUs from catalog).  
7. Frontend displays suggestions under the search bar.  
8. User clicks a suggestion → navigates to product page.  
9. Event logged for analytics.  
10. Cache updated with response.

### Grounding & Guardrails
- **Source of truth:** Product catalog database (10k SKUs).  
- **Retrieval scope:** Catalog metadata only, no external web.  
- **Max context:** ≤200 tokens (query + few relevant embeddings).  
- **Outside scope:** If request isn’t a search string, return “Please use the search bar to find products.”

### Human-in-the-Loop
- Escalation not needed for typeahead.  
- If model repeatedly fails (empty or invalid SKUs for >1% of queries), trigger engineering alert.  
- SLA: Fix within next sprint.

### Latency Budget
- Frontend → API: 50 ms  
- Cache check: 20 ms  
- Model call: 200 ms (p95)  
- Post-processing: 30 ms  
- Total = 300 ms  

### Error & Fallback Behavior
- If model fails, fallback to client-side fuzzy string search.  
- If both fail, return no suggestions and log error.

### PII Handling
- Query string only; no personal data leaves app.  
- Logs anonymized with session ID only.

### Success Metrics
- Product metric 1: **Search CTR** = clicks on suggestions ÷ suggestion displays.  
- Product metric 2: **Search success rate** = product viewed after suggestion ÷ total suggestion displays.  
- Business metric: **Conversion uplift** = (orders after suggestion ÷ sessions with suggestions) − baseline orders.

### Feasibility Note
Catalog data already available in DB. Embeddings can be pre-computed using open-source models. Next prototype step: implement API endpoint that checks cache, then calls an embedding-based search using LLM reranker.

---

## 2. Support Assistant (FAQ + Order Status)

### Problem Statement
Customers frequently contact support for FAQs and “Where is my order?” queries. Manual handling is costly and slow. An AI assistant grounded in ShopLite’s FAQ markdown and `order-status` API can resolve these instantly, reducing support workload.

### Happy Path
1. User opens support chat and types a question.  
2. System captures query and runs PII redaction (remove email, phone, CC numbers).  
3. API checks cache for similar past question.  
4. If cache hit, return cached answer.  
5. If miss, query FAQ markdown + `order-status` API for grounding.  
6. LLM generates concise answer (max 3 sentences).  
7. Answer validated against grounding; if outside scope, refuse.  
8. Reply shown to user in chat.  
9. If confidence < 0.6 or user types “agent”, escalate to human support.  
10. Conversation logged with redacted data for metrics.

### Grounding & Guardrails
- **Source of truth:** FAQ markdown + `order-status` API.  
- **Retrieval scope:** Only FAQ entries + order status by ID.  
- **Max context:** ≤600 tokens.  
- **Outside scope:** Respond “I can only help with ShopLite orders and policies. Please contact support for other requests.”

### Human-in-the-Loop
- Escalation trigger: confidence <0.6 OR explicit “agent” request.  
- UI surface: Chat bubble “Escalate to human agent.”  
- Reviewer: Support staff.  
- SLA: ≤4 hours response.

### Latency Budget
- Input + redaction: 100 ms  
- Cache check: 100 ms  
- Retrieval (FAQ + order API): 200 ms  
- LLM call: 700 ms  
- Post-process + UI: 100 ms  
- Total = 1200 ms  

### Error & Fallback Behavior
- If API call fails: return “Unable to retrieve order status now, please try again later.”  
- If LLM call fails: return FAQ search results or escalate to human.

### PII Handling
- Strip email, phone, CC numbers from context.  
- Order IDs hashed before sending to LLM.  
- Logs store only session ID + anonymized question.

### Success Metrics
- Product metric 1: **Resolution rate** = resolved by assistant ÷ total assistant sessions.  
- Product metric 2: **Avg first response time** = median seconds to first message.  
- Business metric: **Support cost saved** = (# assistant-resolved queries × avg ticket handling cost).

### Feasibility Note
FAQ markdown already exists. `order-status` API by ID is live. Next step: build retrieval pipeline, run a prototype query with sample FAQ and order ID, and measure latency vs target.
