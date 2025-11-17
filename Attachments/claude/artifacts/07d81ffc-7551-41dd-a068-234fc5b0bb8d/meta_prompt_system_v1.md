---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: meta_prompt_system
version_uuid: 391aa644-4108-4ec6-89a5-a32034ff7caa
version_number: 1
command: create
conversation_id: 07d81ffc-7551-41dd-a068-234fc5b0bb8d
create_time: 2025-07-31T07:00:14.000Z
format: markdown
aliases: [Meta-Prompt System for Firebase Application Design, meta_prompt_system_v1]
---

# Meta-Prompt System for Firebase Application Design (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Crafting a New Prompt|Crafting a New Prompt]]

## Content

# Meta-Prompt System for Firebase Application Design

## Layer 1: Master Prompt Generator
**Purpose**: Creates specialized prompt generators for different Firebase application contexts

### Master Prompt Template:
```
You are a Firebase Application Design Prompt Architect. Your task is to create a specialized prompt generator for [SPECIFIC_FIREBASE_CONTEXT]. 

Generate a prompt that will create prompts for building Firebase applications in the domain of [APPLICATION_TYPE].

Your generated prompt should:
1. Define the specific Firebase services most relevant to [APPLICATION_TYPE]
2. Establish architectural patterns common to [APPLICATION_TYPE] applications
3. Include security considerations specific to [APPLICATION_TYPE]
4. Address scalability requirements for [APPLICATION_TYPE]
5. Incorporate best practices for [APPLICATION_TYPE] user experiences

The prompt you generate should create detailed, actionable prompts that developers can use to build robust Firebase applications.

Context Variables:
- SPECIFIC_FIREBASE_CONTEXT: [e.g., "Real-time collaboration apps", "E-commerce platforms", "Social media apps"]
- APPLICATION_TYPE: [e.g., "collaborative productivity tools", "marketplace applications", "social networking platforms"]
- TARGET_SCALE: [e.g., "startup MVP", "enterprise-grade", "global scale"]
- PRIMARY_USERS: [e.g., "business teams", "consumers", "developers"]
```

## Layer 2: Specialized Prompt Generators
**Purpose**: Creates domain-specific prompt generators based on Layer 1 output

### Example Output from Layer 1 (E-commerce Focus):
```
You are a Firebase E-commerce Application Prompt Generator. Create detailed prompts for building Firebase-powered e-commerce applications.

Your generated prompts should address:

FIREBASE SERVICES INTEGRATION:
- Firestore for product catalogs and inventory
- Authentication for user accounts and admin panels
- Cloud Functions for payment processing and order management
- Cloud Storage for product images and assets
- Firebase Hosting for web storefronts
- Cloud Messaging for order notifications

ARCHITECTURAL PATTERNS:
- Microservices architecture using Cloud Functions
- Real-time inventory management with Firestore listeners
- Secure payment flows with Stripe/PayPal integration
- Multi-tenant architecture for marketplace scenarios

SECURITY FRAMEWORKS:
- Role-based access control (customers, vendors, admins)
- PCI compliance considerations for payment data
- Input validation and sanitization for product data
- Rate limiting for API endpoints

Generate a prompt for: [SPECIFIC_ECOMMERCE_SCENARIO]
```

## Layer 3: Application-Specific Prompt Generators
**Purpose**: Creates targeted prompts for specific Firebase application scenarios

### Example Output from Layer 2 (Multi-vendor Marketplace):
```
You are designing a Firebase-powered multi-vendor marketplace application. Create a comprehensive development prompt that addresses:

CORE FUNCTIONALITY:
- Vendor onboarding and verification system using Firebase Auth custom claims
- Product catalog management with Firestore subcollections per vendor
- Order processing workflow with Cloud Functions triggers
- Payment splitting between platform and vendors using Stripe Connect
- Real-time inventory synchronization across vendor dashboards

TECHNICAL ARCHITECTURE:
- Design Firestore data model for vendors, products, orders, and reviews
- Implement Cloud Functions for order lifecycle management
- Set up Firebase Security Rules for multi-tenant data access
- Configure Cloud Storage with organized vendor asset management
- Integrate Firebase Analytics for vendor performance tracking

SECURITY & COMPLIANCE:
- Implement vendor identity verification workflows
- Set up automated content moderation for product listings
- Design secure payment processing with PCI compliance
- Establish data privacy controls for vendor and customer information
- Create audit trails for financial transactions

SCALABILITY CONSIDERATIONS:
- Design for horizontal scaling with Firestore subcollections
- Implement caching strategies for frequently accessed product data
- Set up monitoring and alerting for high-traffic scenarios
- Plan for international expansion with multi-region deployment

USER EXPERIENCE:
- Vendor dashboard with real-time sales analytics
- Customer interface with advanced search and filtering
- Mobile-responsive design with Progressive Web App features
- Push notifications for order updates and promotional campaigns

Generate specific implementation guidance for: [MARKETPLACE_FEATURE]
```

## Layer 4: Feature-Specific Implementation Prompts
**Purpose**: Creates detailed implementation prompts for specific features

### Example Output from Layer 3 (Real-time Inventory System):
```
Build a real-time inventory management system for a Firebase multi-vendor marketplace:

DATABASE DESIGN:
Create Firestore collections:
- `/vendors/{vendorId}/products/{productId}` with inventory tracking
- `/inventory-logs/{logId}` for audit trail
- `/low-stock-alerts/{alertId}` for automated notifications

Implement the following Firestore structure:
```javascript
// Product document structure
{
  name: "Product Name",
  price: 29.99,
  inventory: {
    available: 150,
    reserved: 25,
    total: 175,
    lowStockThreshold: 10,
    lastUpdated: timestamp
  },
  vendor: {
    id: "vendor123",
    name: "Vendor Name"
  }
}
```

CLOUD