C:\Users\Hp\Desktop>python probe_test.py

# Typeahead Search Suggestion Probe Log

[2025-09-23 12:25:36] Input: "laptop"
[2025-09-23 12:25:36] Lookup: SKU catalog (8 SKUs)
[2025-09-23 12:25:36] Cache: MISS (key=typeahead:laptop)
[2025-09-23 12:25:36] Output: ['Laptop Stand']
[2025-09-23 12:25:36] p95 budget: 300ms | this run: 2ms | cached for 15m


[2025-09-23 12:25:36] Input: "usb"
[2025-09-23 12:25:36] Lookup: SKU catalog (8 SKUs)
[2025-09-23 12:25:36] Cache: MISS (key=typeahead:usb)
[2025-09-23 12:25:36] Output: ['USB-C Hub']
[2025-09-23 12:25:36] p95 budget: 300ms | this run: 2ms | cached for 15m


[2025-09-23 12:25:36] Input: "desk"
[2025-09-23 12:25:36] Lookup: SKU catalog (8 SKUs)
[2025-09-23 12:25:36] Cache: MISS (key=typeahead:desk)
[2025-09-23 12:25:36] Output: ['Desk Lamp']
[2025-09-23 12:25:36] p95 budget: 300ms | this run: 1ms | cached for 15m


[2025-09-23 12:25:36] Input: "coffee"
[2025-09-23 12:25:36] Lookup: SKU catalog (8 SKUs)
[2025-09-23 12:25:36] Cache: MISS (key=typeahead:coffee)
[2025-09-23 12:25:36] Output: ['Coffee Maker']
[2025-09-23 12:25:36] p95 budget: 300ms | this run: 3ms | cached for 15m


# Support Assistant Probe Log

[2025-09-23 12:25:36] Input: "Where is my order 98765?"
[2025-09-23 12:25:36] Intent: ORDER_STATUS
[2025-09-23 12:25:36] PII Redaction:
   extracted → order_id=98765; name=∅; address=∅
   sanitized query → "Where is my order 98765?"
   note → only order_id leaves the app; names/addresses removed pre-LLM
[2025-09-23 12:25:36] API call → order-status {order_id:98765}
[2025-09-23 12:25:36] API response ← {'status': 'Processing', 'eta': '5 days'}
[2025-09-23 12:25:36] Output: "Your order #98765 is Processing and will arrive in ~5 days."
[2025-09-23 12:25:36] Logging: stored order_id hash=9c4a162afe3d716e ; dropped PII (names/addresses)
[2025-09-23 12:25:36] p95 budget: 1200ms | this run: 5ms


[2025-09-23 12:25:36] Input: "Check status of order 87654"
[2025-09-23 12:25:36] Intent: ORDER_STATUS
[2025-09-23 12:25:36] PII Redaction:
   extracted → order_id=87654; name=∅; address=∅
   sanitized query → "Where is my order 87654?"
   note → only order_id leaves the app; names/addresses removed pre-LLM
[2025-09-23 12:25:36] API call → order-status {order_id:87654}
[2025-09-23 12:25:36] API response ← {'status': 'Shipped', 'eta': '2 days'}
[2025-09-23 12:25:36] Output: "Your order #87654 is Shipped and will arrive in ~2 days."
[2025-09-23 12:25:36] Logging: stored order_id hash=59fdcc0312f13ba ; dropped PII (names/addresses)
[2025-09-23 12:25:36] p95 budget: 1200ms | this run: 3ms

