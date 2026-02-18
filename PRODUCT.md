# Funila — Commercial Intelligence System

**Turn ad traffic into qualified WhatsApp leads.**

---

## 1. The Core Problem
Most businesses investing in paid traffic face a "Black Hole" when directing leads to WhatsApp.
- **The Waste Cycle:** Money goes out, clicks come in, but sales teams waste hours qualifying curious leads manually.
- **Data Loss:** Once a lead clicks "Message", attribution is lost. You don't know which campaign generated the sale.
- **Blind Spots:** No financial profile, no intent score, no tracking of drop-offs.

**The Result:** High CAC, low conversion efficiency, and frustrated sales teams acting as SDRs.

## 2. The Solution: Intelligent Funneling
Funila sits between your ad and your WhatsApp, adding a layer of intelligence that filters, tracks, and qualifies every single click.

### The 4 Layers of Intelligence

1.  **Link Tracker (The Ghost Layer)**
    *   Replaces direct WhatsApp links.
    *   Tracks device, location, OS, and Campaign UTMs instantly (<300ms redirect).
    *   Invisible to the user, invaluable to the business.

2.  **Smart Squeeze Page (Progressive Profiling)**
    *   A high-conversion landing page that captures data in micro-steps.
    *   **Step 1:** Identity (Name, Phone).
    *   **Step 2:** Professional Profile (Job type, Tenure).
    *   **Step 3:** Financial Health (Income estimate, Financing history).
    *   *Result:* Natural filtration of unqualified leads.

3.  **Automatic Scoring Engine**
    *   Calculates an internal lead score (0-100) based on profile data.
    *   **Serasa Integration (Pro):** Real-time credit score check via API for high-ticket sales (Real Estate, Vehicles).
    *   **Status Assignment:** 🔥 Hot, 🟡 Warm, ❄️ Cold.

4.  **Contextual Hand-off**
    *   The lead arrives on WhatsApp with a pre-filled message containing their full profile.
    *   *Example:* "Hello! I'm Ana, employed for 4 years, income ~4k. Saw your ad about the downtown apartment."
    *   The salesperson starts closing, not qualifying.

## 3. Target Verticals
*   **Real Estate:** Filter leads by financing potential before the first "Hello".
*   **Agencies:** Prove ROI to clients by delivering qualified leads, not just clicks.
*   **High-Ticket Services:** Solar, Insurance, and Automotive sectors where qualification matters.

## 4. Technical Architecture
Built for speed, privacy, and scale.

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | Vanilla JS / PWA | Ultra-lightweight squeeze pages (GitHub Pages). |
| **Backend** | Python FastAPI | High-performance API for scoring and tracking (Render). |
| **Database** | PostgreSQL (Supabase) | Relational data integrity for leads and events. |
| **Auth** | JWT / Supabase Auth | Secure tenant isolation. |
| **Privacy** | AES-256 Encryption | LGPD/GDPR compliant storage of sensitive data (CPF). |

## 5. Ecosystem & Vision
Funila is part of the **RDP Studio** ecosystem, designed to bridge the gap between marketing investment and sales reality.

*   **Focus:** Actionable data over vanity metrics.
*   **Philosophy:** "Cognitive Capture" — Intuitive flows that feel natural to the user but powerful for the business.
*   **Design System:** Dark-mode first, high-contrast, accessibility-focused interface.

---

**© 2026 RDP Studio. All rights reserved.**
