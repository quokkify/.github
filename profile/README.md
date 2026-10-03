# Quokkify

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-light.svg" />
    <img src="https://raw.githubusercontent.com/quokkify/.github/main/assets/branding/quokkify-banner-light.svg" alt="Quokkify — Build once. Automate forever." width="100%" />
  </picture>
</p>

<p align="center">
  Reusable engineering tools, delivery automation, and practical applications. Adopt the building blocks you need—or explore how they work in real projects.
</p>

---

## Repository map

Browse by purpose: project foundations, CI/CD actions, engineering libraries, agent resources, or applications. Each repository links to its documentation and release history.

### Foundation and shared delivery

| Repository | Version | Purpose |
|---|---|---|
| [`project-toolkit`](https://github.com/quokkify/project-toolkit) | [![Version](https://img.shields.io/github/v/release/quokkify/project-toolkit?label=version&style=flat-square&sort=date)](https://github.com/quokkify/project-toolkit/releases) | Reusable project scaffolding, workflows, composite actions, and Copier templates. |
| [`renovate-presets`](https://github.com/quokkify/renovate-presets) | [![Version](https://img.shields.io/github/v/release/quokkify/renovate-presets?label=version&style=flat-square&sort=date)](https://github.com/quokkify/renovate-presets/releases) | Shared Renovate configuration for consistent dependency updates. |

### CI/CD actions

| Repository | Version | Purpose |
|---|---|---|
| [`compose-health-check-action`](https://github.com/quokkify/compose-health-check-action) | [![Version](https://img.shields.io/github/v/release/quokkify/compose-health-check-action?label=version&style=flat-square&sort=date)](https://github.com/quokkify/compose-health-check-action/releases) | Runs Docker Compose with health checks and actionable diagnostics. |
| [`gh-pages-subdir-action`](https://github.com/quokkify/gh-pages-subdir-action) | [![Version](https://img.shields.io/github/v/release/quokkify/gh-pages-subdir-action?label=version&style=flat-square&sort=date)](https://github.com/quokkify/gh-pages-subdir-action/releases) | Publishes generated sites and reports into isolated GitHub Pages subdirectories. |
| [`allure-report-action`](https://github.com/quokkify/allure-report-action) | [![Version](https://img.shields.io/github/v/release/quokkify/allure-report-action?label=version&style=flat-square&sort=date)](https://github.com/quokkify/allure-report-action/releases) | Builds Allure reports and pull-request test summaries, with optional Pages publishing. |

### Engineering libraries

| Repository | Version | Purpose |
|---|---|---|
| [`q4j`](https://github.com/quokkify/q4j) | [![Version](https://img.shields.io/github/v/release/quokkify/q4j?label=version&style=flat-square&sort=date)](https://github.com/quokkify/q4j/releases) | Modular Java libraries and integrations for test automation and quality engineering. |

### Agent resources

| Repository | Version | Purpose |
|---|---|---|
| [`skills`](https://github.com/quokkify/skills) | [![Version](https://img.shields.io/github/v/release/quokkify/skills?label=version&style=flat-square&sort=date)](https://github.com/quokkify/skills/releases) | Portable skills, adapters, and safety-focused execution patterns for AI agents. |

### Applications and experiments

Projects that apply these engineering practices to automotive services, marketplace operations, and game trading.

| Repository | Version | Purpose |
|---|---|---|
| [`car-service-platform`](https://github.com/quokkify/car-service-platform) | [![Version](https://img.shields.io/github/v/release/quokkify/car-service-platform?label=version&style=flat-square&sort=date)](https://github.com/quokkify/car-service-platform/releases) | CRM and operations workspace for automotive service businesses. |
| [`marketdesk`](https://github.com/quokkify/marketdesk) | [![Backend version](https://img.shields.io/github/v/release/quokkify/marketdesk?filter=backend-v%2A&label=backend&style=flat-square&sort=date)](https://github.com/quokkify/marketdesk/releases?q=backend-v)<br>[![Frontend version](https://img.shields.io/github/v/release/quokkify/marketdesk?filter=frontend-v%2A&label=frontend&style=flat-square&sort=date)](https://github.com/quokkify/marketdesk/releases?q=frontend-v)<br>[![Assets version](https://img.shields.io/github/v/release/quokkify/marketdesk?filter=assets-v%2A&label=assets&style=flat-square&sort=date)](https://github.com/quokkify/marketdesk/releases?q=assets-v) | Marketplace workspace for managing products and listings across Polish marketplaces. |
| [`path-of-exile-starter`](https://github.com/quokkify/path-of-exile-starter) | [![Version](https://img.shields.io/github/v/release/quokkify/path-of-exile-starter?label=version&style=flat-square&sort=date)](https://github.com/quokkify/path-of-exile-starter/releases) | Telegram bot and supporting services for Path of Exile trading and market data. |

## How to use this collection

- **Start or standardize a project:** explore `project-toolkit` for scaffolding and shared delivery patterns.
- **Improve an existing pipeline:** choose individual actions, dependency presets, or libraries without adopting the whole collection.
- **Work with AI agents:** explore `skills` for portable workflows and execution patterns.
- **Explore practical applications:** visit the application repositories for setup instructions, demos, and project-specific capabilities.

These are complementary entry points, not a mandatory dependency chain.

## Versions and project status

Version badges link to release history and update automatically from published GitHub releases. They indicate the latest non-prerelease release, not production readiness or a shared maturity level across projects.

For setup, supported runtimes, current capabilities, known gaps, and roadmap, read the corresponding repository's README and status documentation. Evaluate readiness there before adopting a project.

## Principles

- **Reusable over repeated** — common engineering work belongs in versioned building blocks.
- **Composable over monolithic** — adopt only the automation a project needs.
- **Predictable over clever** — prefer explicit versions, reviewable updates, and stable contracts.
- **Diagnostics by default** — failures should explain what broke and where to look.
- **Honest maturity** — unfinished projects should say so clearly.

## Contributing

Found a bug, have an idea, or want to contribute? Open an issue or pull request in the relevant repository and follow its contribution guidance.

---

**Build once. Automate forever.**
