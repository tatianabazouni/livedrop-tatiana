# RAG System Evaluation Checklist

Total tests: 30 (10 retrieval, 15 response quality, 5 edge cases)

## Retrieval Quality Tests (10 tests)
| Test ID | Question (from Q&A) | Expected Documents | Pass Criteria |
|---------|---------------------|--------------------|---------------|
| R01 | Q01: How do I create a seller account? | Document 9 | Top-3 retrieved includes Document 9 |
| R02 | Q02: Standard return window? | Document 7 | Document 7 in top-2 |
| R03 | Q05: API inventory updates | Document 10, Document 14 | Both docs present in top-5 |
| R04 | Q11: Return affects payout | Document 7, 11, 10 | All three in top-6 |
| R05 | Q17: Search ranking algorithm | Document 3, 8 | Both in top-4 |
| R06 | Q19: Platform vs seller-fulfilled | Document 6, 9 | Both in top-4 |
| R07 | Q03: Commission calculations | Document 11 | Document 11 in top-3 |
| R08 | Q06: Payment methods | Document 5 | Document 5 in top-2 |
| R09 | Q14: Mobile listing creation | Document 13, 9 | Both in top-4 |
| R10 | Q12: Webhook security | Document 14, 15 | Both in top-5 |

## Response Quality Tests (15 tests)
| Test ID | Question | Required Keywords | Forbidden Terms | Expected Behavior |
|---------|----------|-------------------|-----------------|-------------------|
| Q01 | Q01 | ["seller registration", "business verification", "2–3 business days"] | ["instant approval"] | Direct, step-by-step answer with Document 9 cited |
| Q02 | Q02 | ["30-day return"] | ["no returns"] | Clear statement with Document 7 cited |
| Q03 | Q05 | ["inventory update", "API", "webhooks"] | ["manual only"] | Provide API endpoints and sample usage |
| Q04 | Q11 | ["refund", "payout adjustment", "restocked"] | ["no payout adjustments"] | Multi-source synthesis with numbered steps |
| Q05 | Q12 | ["signature", "nonce", "timestamp"] | ["no validation"] | Security checklist with concrete steps |
| Q06 | Q03 | ["commission", "subscription level"] | ["100% payout"] | Include sample commission example |
| Q07 | Q08 | ["verified purchase", "flag"] | ["unlimited reviews"] | Explain moderation + verified tag |
| Q08 | Q04 | ["delivery exception", "notification"] | ["automatic refund"] | Steps buyer/seller must take |
| Q09 | Q19 | ["seller-fulfilled", "platform-fulfilled"] | ["no difference"] | Compare and cite both documents |
| Q10 | Q06 | ["credit/debit", "wallets"] | ["cash only"] | Payment methods and tokenization note |
| Q11 | Q15 | ["out of stock", "notify me"] | ["order succeeds with out-of-stock item"] | Behavior described and UX recommendation |
| Q12 | Q17 | ["relevance", "conversion", "optimize titles"] | ["search purely by price"] | Rank factors + seller optimizations |
| Q13 | Q09 | ["API key", "webhook signature"] | ["basic auth with password"] | Security configuration steps |
| Q14 | Q16 | ["return request", "order page"] | ["must call support only"] | Short step-wise answer |
| Q15 | Q20 | ["API code samples", "curl", "Python"] | ["no samples available"] | Point to Developer API doc and example snippet |

## Edge Case Tests (5 tests)
| Test ID | Scenario | Expected Response Type |
|--------|----------|------------------------|
| E01 | Question not in KB (random legal advice) | Refusal with explanation & escalate to support/legal |
| E02 | Ambiguous timeframe (e.g., "How long will my order take?") | Ask clarifying question (address/postal code required) |
| E03 | Conflict in documents (seller policy vs platform policy) | State conflict and prefer platform policy; cite both docs |
| E04 | User requests to see sensitive PII | Refuse and provide data request process |
| E05 | No retrieval hits found | Refuse politely and offer support ticket steps |

