# Ground-Truth Q&A (20 items) — Shoplite

### Q01: How do I create a seller account on Shoplite?
**Expected retrieval context:** Document 9: Seller Account Setup & Onboarding  
**Authoritative answer:** To create a seller account, go to the Shoplite seller signup page, provide your business name, tax ID, business address, bank account for payouts, and upload required verification documents. Shoplite runs automated checks and a manual review that typically takes 2–3 business days before enabling seller features.  
**Required keywords in LLM response:** ["seller registration", "business verification", "2–3 business days"]  
**Forbidden content:** ["instant approval", "no verification required", "personal accounts"]

### Q02: What is Shoplite's standard return window?
**Expected retrieval context:** Document 7: Return & Refund Policies  
**Authoritative answer:** Shoplite’s standard return window is 30 days from delivery for eligible items, unless the seller specifies a longer window or the item category is non-returnable.  
**Required keywords:** ["30-day return", "eligible items"]  
**Forbidden content:** ["no returns", "lifetime returns"]

### Q03: How are commissions charged on Shoplite?
**Expected retrieval context:** Document 11: Commission & Fee Structure  
**Authoritative answer:** Commissions are charged per transaction based on category and seller subscription tier; for example, Basic sellers typically pay a 10% commission while Pro sellers can pay lower tiered rates. Fees and any listing or promotional fees are deducted before payout.  
**Required keywords:** ["commission", "subscription level", "payout"]  
**Forbidden content:** ["no fees", "100% payout"]

### Q04: What steps are involved in resolving a delivery exception?
**Expected retrieval context:** Document 6: Order Tracking & Delivery Workflow  
**Authoritative answer:** A delivery exception triggers a notification to the buyer and seller, includes the exception reason (e.g., address problem), and provides next steps such as contacting the carrier, confirming address with buyer, or arranging a reattempt. If unresolved, escalate per platform policy.  
**Required keywords:** ["delivery exception", "notification", "escalate"]  
**Forbidden content:** ["automatic refund without checks"]

### Q05: Can sellers update inventory via API?
**Expected retrieval context:** Document 10: Inventory Management for Sellers + Document 14: Developer API  
**Authoritative answer:** Yes. Sellers can update inventory via the Seller API endpoints or via CSV upload in the dashboard; the API supports real-time updates and webhooks for sync.  
**Required keywords:** ["inventory update", "API", "webhooks"]  
**Forbidden content:** ["manual only", "no API"]

### Q06: Which payment methods does Shoplite support?
**Expected retrieval context:** Document 5: Payment Methods & Security  
**Authoritative answer:** Shoplite supports major credit/debit cards via PCI-compliant processors and popular digital wallets. Cards are tokenized; Shoplite does not store raw card data. Split payments for multi-seller orders are handled through the payment gateway.  
**Required keywords:** ["credit/debit", "wallets", "tokenized"]  
**Forbidden content:** ["cash only", "card numbers stored"]

### Q07: How long until I receive a payout as a seller?
**Expected retrieval context:** Document 9: Seller Account Setup & Onboarding + Document 11: Commission & Fee Structure  
**Authoritative answer:** Default payout cadence is weekly; options for daily payouts may be available for high-volume sellers after approval. Payouts show gross sales minus commissions and adjustments.  
**Required keywords:** ["weekly payout", "net payable", "approval"]  
**Forbidden content:** ["instant daily without approval"]

### Q08: How does Shoplite prevent fraudulent reviews?
**Expected retrieval context:** Document 8: Product Reviews & Ratings System  
**Authoritative answer:** Shoplite flags suspicious review patterns, enforces one review per purchase, uses verification for purchases, and applies automated and manual moderation for abuse.  
**Required keywords:** ["verified purchase", "flag", "moderation"]  
**Forbidden content:** ["unlimited reviews", "no checks"]

### Q09: What should developers use to authenticate API requests?
**Expected retrieval context:** Document 14: Developer API: Overview & Authentication  
**Authoritative answer:** Developers use scoped API keys generated in the seller dashboard; keys should be stored securely and rotated periodically. Webhook payloads are signed and should be validated using the shared secret.  
**Required keywords:** ["API key", "scope", "webhook signature"]  
**Forbidden content:** ["basic auth with password"]

### Q10: How does Shoplite handle taxes and shipping estimates during checkout?
**Expected retrieval context:** Document 4: Shopping Cart & Checkout Process + Document 6: Order Tracking & Delivery Workflow  
**Authoritative answer:** Taxes and shipping are estimated during checkout based on shipping address and seller settings; final amounts are calculated at order placement. International duties may be shown as DDP or DAP depending on seller preference.  
**Required keywords:** ["estimate", "shipping address", "final amount"]  
**Forbidden content:** ["no taxes calculated"]

### Q11: (Complex) Explain how a buyer's return request affects seller payout and inventory.
**Expected retrieval context:** Document 7: Return & Refund Policies + Document 11: Commission & Fee Structure + Document 10: Inventory Management for Sellers  
**Authoritative answer:** When a return is approved, refund is processed to the buyer and the seller’s payout for the original order is adjusted in the next payout cycle to reflect the refund. Inventory is updated when returned items are inspected: if accepted, inventory is restocked; if rejected, inventory remains adjusted. Commissions and restocking fees (if any) are adjusted accordingly.  
**Required keywords:** ["refund", "payout adjustment", "restocked"]  
**Forbidden content:** ["no payout adjustments", "automatic restock"]

### Q12: (Complex) As a developer, how do I ensure webhook security and avoid replay attacks?
**Expected retrieval context:** Document 14: Developer API + Document 5: Payment Methods & Security + Document 15: Security & Privacy Policies  
**Authoritative answer:** Validate the webhook signature using the shared secret, check timestamps and nonces to prevent replay, use HTTPS endpoints, and log and rate-limit incoming webhook calls. Rotate secrets and restrict incoming IPs where possible.  
**Required keywords:** ["signature", "nonce", "timestamp", "HTTPS"]  
**Forbidden content:** ["trust all webhooks", "no validation"]

### Q13: What are the steps to escalate a seller dispute relating to a chargeback?
**Expected retrieval context:** Document 5: Payment Methods & Security + Document 12: Customer Support Procedures  
**Authoritative answer:** Notify the seller of the chargeback, provide evidence upload portal (shipping/tracking, proof of delivery), refer case to disputes team if seller contests, and follow payment provider timelines for response. Shoplite facilitates evidence submission but final decision lies with payment provider.  
**Required keywords:** ["chargeback", "evidence upload", "disputes team"]  
**Forbidden content:** ["Shoplite decides the chargeback outcome"]

### Q14: How does the mobile app improve seller listing creation?
**Expected retrieval context:** Document 13: Mobile App Features & Differences + Document 9: Seller Account Setup & Onboarding  
**Authoritative answer:** The mobile app supports quick product photo capture, automatic cropping, QR code sharing, and a simplified listing flow that accepts minimal required fields, enabling on-the-go listing creation. Bulk/complex listings are recommended via desktop or CSV.  
**Required keywords:** ["photo capture", "simplified listing", "CSV for bulk"]  
**Forbidden content:** ["full desktop analytics available on mobile"]

### Q15: What happens when a product goes out of stock during checkout?
**Expected retrieval context:** Document 3: Product Search & Advanced Filtering + Document 4: Shopping Cart & Checkout Process + Document 10: Inventory Management for Sellers  
**Authoritative answer:** If a product becomes out of stock during checkout, the system displays a clear message, removes or flags the item, and offers alternatives or a notify-me option. Cart persistence for logged-in users helps keep other items. Sellers are notified of low-stock.  
**Required keywords:** ["out of stock", "notify me", "cart update"]  
**Forbidden content:** ["order succeeds with out-of-stock item"]

### Q16: (Simple) How can a buyer request a return?
**Expected retrieval context:** Document 7: Return & Refund Policies  
**Authoritative answer:** Buyers can request a return from the order page, select a reason, upload photos if needed, and follow the shipping instructions after approval.  
**Required keywords:** ["order page", "return request", "shipping instructions"]  
**Forbidden content:** ["no steps", "must call support only"]

### Q17: (Complex) Describe how Shoplite's search ranking works and how sellers can improve discoverability.
**Expected retrieval context:** Document 3: Product Search & Advanced Filtering + Document 8: Product Reviews & Ratings System + Document 13: Mobile App Features  
**Authoritative answer:** Search ranking uses title/description keyword matches, popularity (clicks, conversion), seller reputation, review ratings, and personalization signals. Sellers can improve discoverability by optimizing titles/descriptions, maintaining high ratings, using quality images, and participating in promoted listings.  
**Required keywords:** ["relevance", "conversion", "seller reputation", "optimize titles"]  
**Forbidden content:** ["search purely by price"]

### Q18: (Simple) What kinds of notifications does Shoplite send post-order?
**Expected retrieval context:** Document 4: Shopping Cart & Checkout Process + Document 6: Order Tracking & Delivery Workflow  
**Authoritative answer:** Order confirmation, shipment notification with tracking, delivery confirmation, and return/refund updates. Sellers get order and payout notifications.  
**Required keywords:** ["order confirmation", "shipment", "tracking"]  
**Forbidden content:** ["no notifications"]

### Q19: (Complex) Explain platform-fulfilled vs seller-fulfilled orders and how this affects tracking.
**Expected retrieval context:** Document 6: Order Tracking & Delivery Workflow + Document 9: Seller Account Setup & Onboarding  
**Authoritative answer:** Seller-fulfilled orders are shipped by the seller and they provide tracking; platform-fulfilled (Shoplite Logistics) uses Shoplite's own fulfillment network and provides centralized tracking and faster SLAs. For tracking, platform-fulfilled shipments are automatically updated and consolidated, while seller-fulfilled shipments rely on seller-provided tracking or carrier integrations.  
**Required keywords:** ["seller-fulfilled", "platform-fulfilled", "tracking", "SLAs"]  
**Forbidden content:** ["no difference"]

### Q20: (Simple) Where can I find API code samples for creating a product?
**Expected retrieval context:** Document 14: Developer API: Overview & Authentication  
**Authoritative answer:** API code samples (curl, Python) for product creation are in the Developer API docs accessible from the seller dashboard and the public API reference; sample snippets include required fields and authentication examples.  
**Required keywords:** ["API code samples", "curl", "Python", "authentication"]  
**Forbidden content:** ["no samples available"]
