# Quokkify

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-light.svg" />
    <img src="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-light.svg" alt="Quokkify — Build once. Automate forever." width="100%" />
  </picture>
</p>

<p align="center">
  Reusable workflows, actions, presets, agent skills, testing utilities, and practical applications for consistent engineering across projects.
</p>

<p align="center">
  <a href="https://github.com/quokkify"><img src="https://img.shields.io/badge/GitHub-quokkify-181717?logo=github" alt="GitHub organization" /></a>
</p>

---

## What we do

- Turn repeated setup and maintenance into reusable automation
- Build composable CI/CD workflows and GitHub Actions
- Standardize dependency updates, releases, and project scaffolding
- Share portable agent workflows with explicit safety and recovery boundaries
- Make Docker Compose validation reliable and easy to diagnose
- Create practical testing utilities for real delivery pipelines
- Build focused products that apply this automation to real workflows

## Our focus

We build small, dependable tools and useful applications that remove repetitive work from software delivery and everyday operations. The goal is straightforward: consistent project setup, predictable CI, safer dependency maintenance, and clear diagnostics when something fails.

## Projects & applications

Maturity labels describe the current engineering state, not a production SLA. Each project keeps its detailed status and known gaps in its own repository.

| Repository | Maturity | What it is |
| :-- | :-- | :-- |
| [car-service-platform](https://github.com/quokkify/car-service-platform) | **Beta · active development** | CRM and operations workspace for automotive service businesses: repairs, vehicles, parts, purchasing, documents, dashboards, and customer updates. Django/DRF + React/Vite + PostgreSQL. |
| [marketdesk](https://github.com/quokkify/marketdesk) | **Prototype · active development** | Hermes-connected internal marketplace workspace for managing products and listings across Polish marketplaces. The platform is unfinished and remains an internal work in progress. |
| [path-of-exile-starter](https://github.com/quokkify/path-of-exile-starter) | **Active development** | Telegram bot and supporting services that help Path of Exile players get started with trading and market data. |

## Project automation

| Repository | Version | Description |
| :-- | :-- | :-- |
| [project-toolkit](https://github.com/quokkify/project-toolkit) | [![Release](https://img.shields.io/github/v/release/quokkify/project-toolkit)](https://github.com/quokkify/project-toolkit/releases) | Reusable workflows, composite actions, and Copier templates for Python, Node.js, Java, Docker, and polyglot repositories. |
| [renovate-presets](https://github.com/quokkify/renovate-presets) | [![Release](https://img.shields.io/github/v/release/quokkify/renovate-presets)](https://github.com/quokkify/renovate-presets/releases) | Shared Renovate presets for consistent, reviewable dependency updates across projects. |

## Agent engineering

| Repository | Version | Description |
| :-- | :-- | :-- |
| [skills](https://github.com/quokkify/skills) | [![Release](https://img.shields.io/github/v/release/quokkify/skills)](https://github.com/quokkify/skills/releases) | Portable skills, adapters, and safety-focused execution patterns for Hermes, Claude Code, Codex, and compatible agents. |

## CI/CD tooling

| Repository | Version | Description |
| :-- | :-- | :-- |
| [compose-health-check-action](https://github.com/quokkify/compose-health-check-action) | [![Release](https://img.shields.io/github/v/release/quokkify/compose-health-check-action)](https://github.com/quokkify/compose-health-check-action/releases) | Runs Docker Compose with health checks, platform detection, and actionable failure diagnostics. |
| [gh-pages-subdir-action](https://github.com/quokkify/gh-pages-subdir-action) | [![Release](https://img.shields.io/github/v/release/quokkify/gh-pages-subdir-action)](https://github.com/quokkify/gh-pages-subdir-action/releases) | Publishes generated sites and test reports into isolated GitHub Pages subdirectories while preserving sibling deployments. |
| [allure-report-action](https://github.com/quokkify/allure-report-action) | [![Release](https://img.shields.io/github/v/release/quokkify/allure-report-action)](https://github.com/quokkify/allure-report-action/releases) | Builds Allure reports, badges, and idempotent pull-request test summaries, with optional pyramid artifacts and Pages publishing. |

## Quality engineering

| Repository | Version | Description |
| :-- | :-- | :-- |
| [q4j](https://github.com/quokkify/q4j) | [![Release](https://img.shields.io/github/v/release/quokkify/q4j)](https://github.com/quokkify/q4j/releases) | Modular Java libraries and integrations for test automation and quality engineering. |

---

## How the pieces fit together

```text
project-toolkit
Scaffolding • CI workflows
        ↓
renovate-presets
Dependency maintenance
        ↓
compose-health-check-action + allure-report-action + q4j
Service, report, and test verification
        ↓
car-service-platform + marketdesk + path-of-exile-starter
Applications built and maintained with the same delivery foundations
```

Each repository can be used independently. Together they form a practical automation layer for creating, maintaining, and validating software projects—and for applying those foundations to real products.

## Principles

- **Reusable over repeated** — common engineering work belongs in versioned building blocks
- **Composable over monolithic** — adopt only the automation a project needs
- **Predictable over clever** — explicit versions, reviewable updates, and stable contracts
- **Diagnostics by default** — failures should explain what broke and where to look
- **Automation with control** — routine work runs automatically; important changes stay visible
- **Honest maturity** — unfinished projects should say so clearly

---

## Philosophy

**Build once. Automate forever.**

Good automation should save time without hiding how a project works. We favor tools that are easy to adopt, safe to update, and useful across different stacks.

## Contributing

Ideas, issues, and contributions are welcome. If you find repetitive engineering work that could become a reusable tool—or see a way to improve an existing project—open an issue in the relevant repository.

## Migrated projects

These repositories are maintained under the Quokkify organization. Their former `ylazakovich/*` URLs redirect to the organization repositories. Project-specific showcase assets are versioned here so project READMEs can use stable raw URLs.

| Repository | Status | Showcase |
| :-- | :-- | :-- |
| [car-service-platform](https://github.com/quokkify/car-service-platform) | Beta · active development · production readiness not certified | [Dashboard](https://raw.githubusercontent.com/quokkify/.github/main/assets/projects/car-service-platform/dashboard.png) |
| [marketdesk](https://github.com/quokkify/marketdesk) | Prototype · active development · not ready for production | [Products](https://raw.githubusercontent.com/quokkify/.github/main/assets/projects/marketdesk/products.png) |
| [path-of-exile-starter](https://github.com/quokkify/path-of-exile-starter) | Active development · production readiness not certified | [Preview](https://raw.githubusercontent.com/quokkify/.github/main/assets/projects/path-of-exile-starter/preview.gif) |

Project repositories retain runtime-required local assets; only documentation/showcase copies are hosted here. See each project README for its asset inventory and Copier update command.
