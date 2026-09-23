# Quokkify

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-light.svg" />
    <img src="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-light.svg" alt="Quokkify — Build once. Automate forever." width="100%" />
  </picture>
</p>

<p align="center">
  Reusable delivery foundations, engineering tools, agent resources, and practical applications for more consistent software projects.
</p>

---

## Start here: project-toolkit

[`project-toolkit`](https://github.com/quokkify/project-toolkit) [![Release](https://img.shields.io/github/v/release/quokkify/project-toolkit)](https://github.com/quokkify/project-toolkit/releases) is the starting point for Quokkify's shared engineering approach. It contains reusable workflows, composite actions, and Copier templates for Python, Node.js, Java, Docker, and polyglot repositories.

It is a foundation and a point of orientation—not a claim that every repository depends on every part of it.

## Repository map

Quokkify repositories are grouped by role. This is a navigation map, not a ranking of product readiness or importance.

### Foundation and shared delivery

- [`project-toolkit`](https://github.com/quokkify/project-toolkit) [![Release](https://img.shields.io/github/v/release/quokkify/project-toolkit)](https://github.com/quokkify/project-toolkit/releases) — reusable project scaffolding, workflows, actions, and templates.
- [`renovate-presets`](https://github.com/quokkify/renovate-presets) [![Release](https://img.shields.io/github/v/release/quokkify/renovate-presets)](https://github.com/quokkify/renovate-presets/releases) — shared Renovate configuration for consistent dependency updates.

### CI/CD actions

- [`compose-health-check-action`](https://github.com/quokkify/compose-health-check-action) [![Release](https://img.shields.io/github/v/release/quokkify/compose-health-check-action)](https://github.com/quokkify/compose-health-check-action/releases) — runs Docker Compose with health checks and actionable diagnostics.
- [`gh-pages-subdir-action`](https://github.com/quokkify/gh-pages-subdir-action) [![Release](https://img.shields.io/github/v/release/quokkify/gh-pages-subdir-action)](https://github.com/quokkify/gh-pages-subdir-action/releases) — publishes generated sites and reports into isolated GitHub Pages subdirectories.
- [`allure-report-action`](https://github.com/quokkify/allure-report-action) [![Release](https://img.shields.io/github/v/release/quokkify/allure-report-action)](https://github.com/quokkify/allure-report-action/releases) — builds Allure reports and pull-request test summaries, with optional Pages publishing.

### Engineering libraries

- [`q4j`](https://github.com/quokkify/q4j) [![Release](https://img.shields.io/github/v/release/quokkify/q4j)](https://github.com/quokkify/q4j/releases) — modular Java libraries and integrations for test automation and quality engineering.

### Agent resources

- [`skills`](https://github.com/quokkify/skills) [![Release](https://img.shields.io/github/v/release/quokkify/skills)](https://github.com/quokkify/skills/releases) — portable skills, adapters, and safety-focused execution patterns for AI agents.

### Applications and experiments

These repositories demonstrate applications of the same engineering mindset. They are listed for discoverability, not as production-ready product endorsements.

- [`car-service-platform`](https://github.com/quokkify/car-service-platform) [![Release](https://img.shields.io/github/v/release/quokkify/car-service-platform)](https://github.com/quokkify/car-service-platform/releases) — CRM and operations workspace for automotive service businesses.
- [`marketdesk`](https://github.com/quokkify/marketdesk) [![Release](https://img.shields.io/github/v/release/quokkify/marketdesk)](https://github.com/quokkify/marketdesk/releases) — internal marketplace workspace for managing products and listings across Polish marketplaces.
- [`path-of-exile-starter`](https://github.com/quokkify/path-of-exile-starter) [![Release](https://img.shields.io/github/v/release/quokkify/path-of-exile-starter)](https://github.com/quokkify/path-of-exile-starter/releases) — Telegram bot and supporting services for Path of Exile trading and market data.

## How the repositories relate

- **Project foundations** provide repeatable scaffolding and delivery patterns.
- **Presets, actions, and libraries** are independently usable building blocks for CI/CD, maintenance, reporting, and quality engineering.
- **Agent resources** describe portable workflows and execution patterns for compatible AI agents.
- **Applications and experiments** apply selected practices to real workflows; they do not imply a single mandatory dependency chain.

The repositories can be used independently. Together, they form a toolkit for creating, maintaining, testing, and applying software projects.

## Reading project status correctly

The profile is intentionally a stable navigation page, not a live project-status registry.

For each repository, treat its own README and status files as the source of truth for:

- maturity and implementation state;
- production readiness and known gaps;
- supported runtimes, integrations, and deployment constraints;
- releases, roadmap, and current capabilities.

Unless a repository explicitly says otherwise, production readiness should not be assumed.

## Principles

- **Reusable over repeated** — common engineering work belongs in versioned building blocks.
- **Composable over monolithic** — adopt only the automation a project needs.
- **Predictable over clever** — prefer explicit versions, reviewable updates, and stable contracts.
- **Diagnostics by default** — failures should explain what broke and where to look.
- **Honest maturity** — unfinished projects should say so clearly.

## Contributing

Ideas, issues, and contributions are welcome. If you find repetitive engineering work that could become a reusable tool—or see a way to improve an existing project—open an issue in the relevant repository.

Project-specific screenshots, demos, setup instructions, and detailed status belong in the corresponding project repository, where their context can be kept current.

---

**Build once. Automate forever.**
