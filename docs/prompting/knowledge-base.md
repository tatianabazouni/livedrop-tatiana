# Shoplite Documentation Topics

## 1. User Registration and Account Management

To create a Shoplite account, users visit the registration page and provide their email address, password, and basic profile information. Email verification is required within 24 hours of registration. Users can choose between buyer accounts (free) or seller accounts (which require additional business verification). The buyer registration is straightforward: username, email, password, and optional phone number for SMS notifications. Password rules enforce a minimum of 8 characters including one uppercase letter and one number. For account recovery, Shoplite supports email-based reset links and optional two-factor authentication (2FA) via TOTP apps (e.g., Google Authenticator). Seller registration begins with company name, tax ID, business address, bank account information for payouts, and uploading identification documents. Shoplite performs automated checks and then a manual review. Once approved, sellers receive an onboarding email with links to seller dashboard, inventory upload templates (CSV), and API keys for integration. Users may upgrade or downgrade account types in Account Settings; downgrades may affect seller features and payout schedules. All accounts must agree to the Terms of Service and Privacy Policy during sign-up. The document includes examples of common registration errors (invalid email formats, password mismatch, duplicate email) and recommended UI messages to reduce user friction. Finally, we describe how Shoplite notifies users about unverified accounts and the process to resend verification links.

---

## 2. Product Search and Filtering Features

Shoplite's search engine combines keyword search, faceted filters, and relevance ranking. Core features include fuzzy matching, stemming, synonyms, and typo tolerance. Filters include category, price range, seller rating, shipping time, availability (in-stock), condition (new/refurbished), and promotions. The UI supports multi-select filters and dynamic counts. Search relevancy uses a weighted mix of title matches, description matches, popularity, conversion rate, and seller reputation. For personalized search, Shoplite applies user history (recently viewed, purchased categories) to boost results. Sorting options include "Relevance", "Price: Low to High", "Price: High to Low", "Best Sellers", and "Newest". Autocomplete leverages prefix matching and trending queries; it returns up to 6 suggestions and throttles suggestions per session to reduce API load. For API consumers, search endpoints accept `q`, `filters` (JSON), `sort`, `page`, and `per_page`. Query performance is optimized with a cached product index updated incrementally as inventory changes. The document also details how to handle out-of-stock SKUs (show “notify me” and hide from default listings when hidden by seller) and how promotional badges (e.g., “Free shipping”, “Top Seller”) are calculated and presented.

---

## 3. Shopping Cart and Checkout Process

Shoplite’s cart persists across devices for logged-in users; guests maintain a session cart via cookies for 30 days. A cart may contain items from multiple sellers; Shoplite splits the checkout into a unified payment while creating distinct seller-level orders for fulfillment. During checkout, taxes and shipping are estimated based on shipping address and seller settings; final amounts are calculated at order placement. The checkout flow includes address selection, shipping option selection (standard, expedited), payment method, promo code entry, and order review. Payment authorization occurs immediately; capture occurs at the time of order placement except where preauthorization rules apply (e.g., high-risk orders). The system supports saved cards (tokenized) and wallets. For multi-seller orders, Shoplite aggregates totals but tracks each seller’s payout and commission separately. The platform supports invoice generation and sends order confirmation emails to buyer and seller with expected shipping windows. Failed payments trigger retries and email notifications; if payment fails after retries, the order is canceled and inventory restored. The cart UI provides clear error messages when items become unavailable during checkout and supports one-click purchase for stored payment methods.

---

## 4. Payment Methods and Security

Shoplite accepts major card networks and popular digital wallets. Payment processing is handled via partnered payment gateways; card data is never stored on Shoplite servers — tokenization and PCI-compliant partners manage card details. For marketplaces, Shoplite supports split payments via the payment provider, ensuring funds are routed to sellers minus platform commission. Additional fraud mitigation includes AVS check, CVV verification, velocity checks, device fingerprinting, and machine-learning risk signals that trigger manual review for suspect transactions. Refunds are processed through the original payment method and may take 3–10 business days depending on bank processing times. For high-value or flagged transactions, Shoplite may require manual KYC review or additional documents. The Security section covers encryption (TLS 1.2+), secrets management, and recommended developer practices: use short-lived keys, rotate API keys, restrict webhook IPs, and validate payload signatures. The document also explains the dispute workflow: chargeback notifications forwarded to seller with evidence upload portals for response.

---

## 5. Order Tracking and Delivery

After a seller marks an order as shipped, Shoplite integrates with carrier partners to generate tracking numbers and provide real-time status updates. Tracking status includes: Processing, Shipped, In Transit, Out for Delivery, Delivered, and Exception. Shoplite supports auto-tracking by pushing shipping labels via partner APIs or by allowing sellers to upload tracking numbers manually. Delivery estimates are calculated using seller location, buyer location, service level, and lead time. The platform supports fulfillment options: seller fulfillment, platform-fulfilled (Shoplite Logistics), or third-party logistics (3PL) integrations. For multi-seller orders, each item gets its own shipment tracking; the buyer sees them consolidated in the order view. Delivery exceptions (missed delivery, address problem) initiate a notification sequence and request seller or buyer action. For international orders, customs, duties, and VAT handling rules are documented; Shoplite can present DDP (Delivered Duty Paid) or DAP options depending on seller preference. The platform exposes an API for tracking updates and webhooks for status changes to integrated seller systems.

---

## 6. Return and Refund Policies

Shoplite’s standardized return policy for eligible items is a 30-day return window starting from delivery date, unless the seller sets a longer window. Certain categories (perishables, intimate goods) may be non-returnable by default. Return requests require a reason code and may include photo evidence. Once a return is approved, the buyer receives a return authorization and instructions for shipping (prepaid label or buyer-paid depending on seller policy). Refunds are issued after the seller confirms item receipt and inspection; in case of seller dispute, Shoplite’s dispute resolution team intervenes. For seller-initiated refunds (e.g., wrong item), refunds are processed immediately and inventory is adjusted. Partial refunds for damaged items are supported. The document describes the timeline for refunds (typically 3–10 business days), restocking fees (optional for sellers), and cases where the buyer may receive replacement or store credit. The policy also includes guidance for fraudulent return detection and handling inbound returns to third-party warehousing.

---

## 7. Product Reviews and Ratings

Shoplite enables buyers to leave reviews with a star rating (1–5), title, body text, and optional photos. Verified purchases are flagged to help trust. Ratings aggregate at the product and seller level; seller rating is a weighted score combining product ratings, fulfillment performance, and dispute rates. To prevent abuse, Shoplite enforces policies: one review per purchase, detection of suspicious review patterns, and manual moderation for flagged content. Sellers may respond to reviews publicly. Reviews feed into search ranking, with higher-rated products boosted in relevance for certain filters. The platform supports Q&A where prospective buyers ask the seller public questions; sellers and other buyers may answer. Reviews API allows export for sellers to display on external sites. Shoplite uses review sampling to invite buyers to leave reviews via post-delivery emails and push notifications; buyers who report a problem during review submission are directed to open a support ticket instead.

---

## 8. Seller Account Setup and Management

Sellers begin with account creation, provide business details, tax IDs, and bank information for payouts. Shoplite runs automated background checks to validate identity and tax status; the manual review stage covers document veracity. Onboarding includes verifying product categories, acceptable item lists, and compliance checks for restricted goods. The seller dashboard offers step-by-step setup tasks: profile completion, store policies (shipping, returns), inventory upload templates, and pricing rules. Shoplite provides CSV and API options for bulk product listing. Sellers can opt into Shoplite Logistics or use their own shipping integrations. Payout cadence default is weekly, with optional daily payout for high-volume sellers upon credit check approval. Sellers must agree to marketplace policies, fee schedules, and dispute handling procedures. The onboarding guides include best practices for product photography, titles, and descriptions to maximize conversion.

---

## 9. Inventory Management for Sellers

Shoplite supports inventory control with stock-keeping units (SKUs), batch updates, and threshold alerts. Sellers can set `available_stock` per SKU and allow backorder or disable backorder. Inventory updates can be done via the Seller UI, CSV upload, or API webhooks. The system supports multi-warehouse inventory where sellers can allocate stock to different fulfillment centers. When orders place, inventory is reserved (not deducted) until payment capture completes to prevent overselling. Batch imports are validated and produce a preview report with errors. Inventory reporting includes low-stock alerts, turnover reports, and aging inventory suggestions. For integrated sellers, Shoplite offers real-time sync via webhooks to avoid race conditions across channels. Sellers may configure automatic restock notifications to subscribers.

---

## 10. Commission and Fee Structure

Shoplite charges a combination of listing fees (category-dependent), transaction commissions (percentage of sale), and payment processing fees. Commission tiers exist by product category and seller subscription level (Basic, Pro, Enterprise). Example: Basic sellers pay 10% commission and Pro sellers 7% with a monthly subscription fee. Additional fees may apply for promoted listings, fulfillment services, or returns handling. Payout calculations show gross sales, commission deduction, refunds, and net payable amount. Fees are computed at order settlement and visible in seller analytics. The document outlines invoicing cadence, fee disputes, and how promotional rebates are reflected in payouts. Sellers receive a detailed payout statement per payout cycle including order IDs, fees, and adjustments.

---

## 11. Customer Support Procedures

Shoplite’s customer support includes help center articles, in-app chat with bots (first-line), and human agents for escalations. Support operates 24/7 for critical incidents and business hours for standard queries. The support flow encourages self-service: searchable FAQs, guided troubleshooting, and automated flows for common tasks (track order, request return, cancel order). For unresolved issues, tickets are created with SLA rules: 24-hour response for general tickets, 48–72 hours for investigations, and 3–5 business days for appeals. Support agents have role-based dashboards with access to order history, communication logs, and seller responses. The document details escalation matrices (fraud, legal, data breach), templates for common replies, and quality metrics (first response time, resolution time). Agents must follow data privacy rules when requesting documents and only request necessary data.

---

## 12. Mobile App Features

Shoplite’s mobile app provides core marketplace features optimized for small screens: personalized home feed, push notifications for order events, in-app barcode scanner for sellers to add inventory, and one-tap checkout for saved cards. The mobile app supports offline draft carts, camera-based product photography with auto-cropping, and quick-scan QR codes for seller storefront sharing. Push notifications cover order status, promotions, and support messages. The app includes a simplified seller dashboard with order management and quick replies for buyer queries. Some heavy analytics sections are desktop-only for clarity. The document lists permissions the app uses (camera, storage, notifications) and privacy choices presented to users, plus guidance for mobile-first UI/UX patterns used in Shoplite.

---

## 13. API Documentation for Developers

Shoplite provides REST APIs for product listing, inventory updates, order retrieval, and webhooks. API authentication uses API keys created in the seller dashboard; keys may be scoped (read-only, orders-write). The API supports pagination, idempotency tokens for safe retries, and webhooks for order updates and returns. Rate limits vary by plan; Basic plan gets 60 RPM and Pro plan gets higher quotas. The document includes code samples (curl, Python requests) for common tasks: listing a product, retrieving orders, updating inventory, and responding to a webhook challenge. Webhook security includes signing payloads with a secret and replay protection via nonce and timestamp. Error codes are standardized (4xx for client errors, 5xx for server errors) with specific messages for common failure modes.

---

## 14. Security and Privacy Policies

Shoplite’s security model includes encryption-in-transit (TLS 1.2+), encryption-at-rest for sensitive fields, role-based access control, regular vulnerability scanning, and an incident response plan. Personal data processing practices follow privacy-by-design principles; Shoplite supports data subject requests (access, portability, deletion) in line with applicable laws. The document covers password storage (salted hashing), session expiration policies, and secure handling of PII. For developers, there are guidelines on storing secrets, using environment variables, and restricting access. The incident response section outlines notification timelines to affected users and regulators, evidence collection, and remediation steps.

---

## 15. Promotional Codes and Discounts

Shoplite supports promo codes (single use, multi-use), automatic discounts (cart-level), and seller-level promotions. Promo definitions include discount type (percentage, fixed amount), start/end dates, usage limits, and eligible SKUs or categories. Campaigns can be scheduled and A/B tested. The platform supports stacking rules and priority resolution when multiple promotions apply. Analytics show uplift, redemption rate, and incremental sales. For checkout, promo validation runs during cart calculation and returns clear error codes (expired, ineligible, usage limit exceeded). Sellers can allocate a budget to platform promotions and see spend vs. return in analytics.

