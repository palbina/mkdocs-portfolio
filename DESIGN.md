# Design System: Neon Volt (SRE Edition)
**Project:** Cloud Native Engineer Portfolio - High Impact Edition

## 1. Visual Theme & Atmosphere
The **"Neon Volt"** theme is a radical departure from traditional documentation aesthetics. It is a **High-Contrast, Retro-Futuristic Industrial** design inspired by high-end SRE dashboards and mission-critical terminal interfaces. 

*   **Mood:** Aggressive, precise, authoritative, and high-energy.
*   **Philosophy:** "Visibility through intensity."
*   **Textures:** Deep obsidian backgrounds with subtle grid overlays and radial energy gradients.

## 2. Color Palette & Roles

### Dark Mode (Deep Obsidian - Default)
*   **Electric Lime (#CCFF00):** The "Volt" color. Used for all critical interactions, metrics, and primary accents. It represents system health and high performance.
*   **Deep Obsidian (#050505):** The base background layer, providing maximum contrast for the neon elements.
*   **Surface Onyx (#0A0A0A):** Used for structural elements like headers and stat containers.
*   **Volt Glow (rgba(204, 255, 0, 0.4)):** Unified resplandor effect for all interactive elements and icons.
*   **Titanium White (#FFFFFF):** Used for main headings to ensure they cut through the visual intensity.

## 3. Typography Rules
*   **Headings (Inter Black):** Massive font sizes (up to **5rem**) with tight line-height (**0.9**) and negative letter-spacing (**-0.05em**) for a brutalist, industrial look.
*   **Data Metrics (JetBrains Mono):** Used for all numerical data, technical callouts, and timeline dates. It reinforces the engineering "source of truth" feel.
*   **Labels:** All-caps with wide tracking (**0.2em**) for a "military-grade" tagging aesthetic.

## 4. Component Stylings
*   **Buttons:**
    *   **Primary:** Sharp edges (**2px radius**). Solid Lime background. Hover state transitions to White with an intensified glow.
    *   **Secondary:** Ghost style with subtle background and white text.
*   **Icons (Unicode Unified):**
    *   **Style:** Industrial Unicode Emojis (⚙️, 🛠️, 📡, 🔐, 🛡️, 💾, 🤖).
    *   **Effect:** Master Glow Utility applying `drop-shadow` in Electric Lime. Unified scale from **2rem** (compact) to **4.5rem** (hero).
*   **Project Cards:**
    *   **Architecture:** Deep black containers with glowing borders on hover. Organised in a **3-column grid** for symmetrical balance.
    *   **Impact Badges:** Left-bordered callouts with a **Volt-tinted background**.
*   **Timeline:** A vertical industrial marker system for documenting trajectory and achievements.
*   **Tech Showcase:** "Command Center" modules with lateral status bars and `[ SYSTEM_OK ]` indicators.

## 5. Layout Principles
*   **Brutal Spacing:** Large top paddings (**6rem**) to create a dramatic entrance.
*   **Grid Consistency:** Fixed 3-column layout for desktop, responsive scaling for mobile.
*   **Report Style Case Studies:** Projects structured as technical dossiers with metadata grids and industrial data tables.
