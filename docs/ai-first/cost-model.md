# Cost Model — ShopLite

## Assumptions
- Model: Llama 3.1 8B Instruct via OpenRouter at $0.05/1K prompt tokens, $0.20/1K completion tokens
- Requests/day (from defaults):
  - Typeahead: 50,000 with 70% cache hit
  - Support assistant: 1,000 with 30% cache hit

---

## Calculation

### Typeahead
- Avg tokens in: 15  
- Avg tokens out: 8  
- Cost/action = (15/1000 * 0.05) + (8/1000 * 0.20)  
- Cost/action = 0.00075 + 0.00160 = **$0.00235**  
- Daily cost = 50,000 × (1 − 0.70) × 0.00235 = 15,000 × 0.00235 = **$35.25**

### Support Assistant
- Avg tokens in: 200  
- Avg tokens out: 250  
- Cost/action = (200/1000 * 0.05) + (250/1000 * 0.20)  
- Cost/action = 0.010 + 0.050 = **$0.060**  
- Daily cost = 1,000 × (1 − 0.30) × 0.060 = 700 × 0.060 = **$42.00**

---

## Results
- Typeahead: Cost/action = **$0.00235**, Daily = **$35.25**  
- Support assistant: Cost/action = **$0.060**, Daily = **$42.00**

---

## Cost lever if over budget
- Shorten context (e.g., reduce support assistant inputs from 600 → 300 tokens).  
- Improve cache hit rate for typeahead (from 70% → 85%).  
- Downgrade model for low-risk paths (use smaller model for typeahead, larger model only for order-status queries).
