# Quokkify

<p align="center">
  <strong>Automation that makes software delivery repeatable</strong><br/>
  Reusable workflows, actions, presets, and testing utilities for consistent engineering across projects.
</p>

<p align="center">
  <a href="https://github.com/quokkify"><img src="https://img.shields.io/badge/GitHub-quokkify-181717?logo=github" alt="GitHub organization" /></a>
</p>

---

### What we do

- Turn repeated setup and maintenance into reusable automation
- Build composable CI/CD workflows and GitHub Actions
- Standardize dependency updates, releases, and project scaffolding
- Make Docker Compose validation reliable and easy to diagnose
- Create practical testing utilities for real delivery pipelines

### Our focus

We build small, dependable tools that remove repetitive work from software delivery. The goal is straightforward: consistent project setup, predictable CI, safer dependency maintenance, and clear diagnostics when something fails.

---

### Project automation

| Repository | Version | Description |
| :-- | :-- | :-- |
| [project-toolkit](https://github.com/quokkify/project-toolkit) | [![Release](https://img.shields.io/github/v/release/quokkify/project-toolkit)](https://github.com/quokkify/project-toolkit/releases) | Reusable workflows, composite actions, and Copier templates for Python, Node.js, Java, Docker, and polyglot repositories. |
| [renovate-presets](https://github.com/quokkify/renovate-presets) | [![Release](https://img.shields.io/github/v/release/quokkify/renovate-presets)](https://github.com/quokkify/renovate-presets/releases) | Shared Renovate presets for consistent, reviewable dependency updates across projects. |

### CI/CD tooling

| Repository | Version | Description |
| :-- | :-- | :-- |
| [compose-health-check-action](https://github.com/quokkify/compose-health-check-action) | [![Release](https://img.shields.io/github/v/release/quokkify/compose-health-check-action)](https://github.com/quokkify/compose-health-check-action/releases) | Runs Docker Compose with health checks, platform detection, and actionable failure diagnostics. |

### Quality engineering

| Repository | Version | Description |
| :-- | :-- | :-- |
| [autokit](https://github.com/quokkify/autokit) | [![Release](https://img.shields.io/github/v/release/quokkify/autokit)](https://github.com/quokkify/autokit/releases) | Modular Java utilities and integrations for building maintainable test automation. |

---

### How the pieces fit together

```text
Scaffold projects  →  Run consistent CI  →  Keep dependencies current  →  Verify services and tests
 project-toolkit        project-toolkit         renovate-presets             compose-health-check-action
                                                                                + autokit
```

Each repository can be used independently. Together they form a practical automation layer for creating, maintaining, and validating software projects without copying the same setup from repository to repository.

### Principles

- **Reusable over repeated** — common engineering work belongs in versioned building blocks
- **Composable over monolithic** — adopt only the automation a project needs
- **Predictable over clever** — explicit versions, reviewable updates, and stable contracts
- **Diagnostics by default** — failures should explain what broke and where to look
- **Automation with control** — routine work runs automatically; important changes stay visible

---

### Philosophy

**Build once. Automate forever.**

Good automation should save time without hiding how a project works. We favor tools that are easy to adopt, safe to update, and useful across different stacks.

### Contributing

Ideas, issues, and contributions are welcome. If you find repetitive engineering work that could become a reusable tool—or see a way to improve an existing project—open an issue in the relevant repository.
