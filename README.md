# loremate-library

`loremate-library` is the shared knowledge library repository for [loremate](https://github.com/mintnlatte/loremate).

This repository stores public, reusable knowledge that can be browsed from the loremate web client, downloaded by directory, copied into a local `vault/public` space, indexed automatically, and used for local LLM search and chat.

## Purpose

- Manage shared public knowledge in one GitHub repository.
- Organize knowledge by source and topic.
- Let each loremate user download only the directories they need.
- Keep downloaded documents searchable through the local loremate index.

## Scope

Only content that is safe to share should be added to this repository.

Good examples:

- Public technical specifications (RFC, PEP, W3C)
- Open-source product documentation excerpts
- Sanitized operation guides
- Learning notes and reference summaries

Do not add:

- Passwords, tokens, API keys, or credentials
- Personal or customer information
- Internal network addresses or server access details
- Confidential company documents
- Private vault documents

## Directory Structure

Each top-level directory is a **category**, with **subcategories** grouping related documents. Each document lives in its own folder containing `README.md` (human-facing summary), `metadata.yaml` (structured metadata), and one or more body files.

```text
loremate-library/
├── standards/
│   ├── rfc/                        # IETF RFCs
│   │   ├── rfc-7519-jwt/
│   │   ├── rfc-6749-oauth2/
│   │   ├── rfc-8446-tls13/
│   │   ├── rfc-9110-http-semantics/
│   │   └── rfc-7231-http11-semantics/
│   └── pep/                        # Python Enhancement Proposals
│       ├── pep-0008-style-guide/
│       ├── pep-0484-type-hints/
│       ├── pep-0517-build-system/
│       ├── pep-0518-pyproject/
│       └── pep-0621-project-metadata/
│
├── manuals/
│   ├── kubernetes/                 # Kubernetes concept pages
│   │   ├── pods/
│   │   ├── service/
│   │   ├── deployment/
│   │   ├── configmap/
│   │   ├── secret/
│   │   └── persistent-volumes/
│   └── docker-compose/             # Compose Specification
│       ├── compose-spec/
│       ├── services/
│       ├── networks/
│       └── volumes/
│
├── security/
│   └── owasp/                      # OWASP Top 10 (2021)
│       ├── A01-broken-access-control/
│       ├── A02-cryptographic-failures/
│       ├── A03-injection/
│       ├── A04-insecure-design/
│       ├── A05-security-misconfiguration/
│       └── A07-identification-authentication-failures/
│
├── papers/
│   └── arxiv/                      # arXiv abstracts + metadata
│       ├── transformer/
│       ├── rag/
│       ├── bert/
│       ├── lost-in-the-middle/
│       ├── self-rag/
│       └── rag-survey/
│
└── korean/
    └── wiki/                       # Korean Wikipedia articles (raw wikitext)
        ├── rag/
        ├── transformer/
        └── pipa/
```

### Per-folder layout

Every category, subcategory, and document folder contains:

```text
<folder>/
├── README.md          # Human-facing summary (free-form markdown). Indexed for RAG.
├── metadata.yaml      # Structured metadata. Excluded from RAG index.
└── <body>.md          # Document body. Multiple body files allowed.
```

See [docs/metadata-schema.md](https://github.com/mintnlatte/loremate/blob/main/docs/metadata-schema.md) in the loremate repo for the full `metadata.yaml` schema.

## Authoring Rules

- Each document gets its own folder with `README.md` + `metadata.yaml` + body file(s).
- Use lowercase English slugs with numbers and hyphens for folder names (`rfc-7519-jwt`, not `RFC 7519`).
- `title` is the only required `metadata.yaml` field; `source`, `license`, `tags`, `language` are strongly recommended.
- Remove sensitive information before committing any document.

## Licenses

Each document retains its original license. The `license` field of `metadata.yaml` records it.

| Source | License |
|---|---|
| RFC (IETF) | IETF Trust |
| PEP (python.org) | Public Domain |
| Kubernetes documentation | CC BY 4.0 |
| Docker Compose Spec | Apache-2.0 |
| OWASP Top 10 | CC BY-SA 4.0 |
| arXiv abstracts | arXiv non-exclusive |
| Korean Wikipedia | CC BY-SA 4.0 |

## Seeding

The contents of this repository can be regenerated from public sources with [`scripts/seed_private_vault.sh`](https://github.com/mintnlatte/loremate/blob/main/scripts/seed_private_vault.sh) in the loremate repo.

## loremate Flow

```text
GitHub loremate-library
  -> loremate "Sync Library" (mirror clone/pull)
  -> select category in tree
  -> "Download" to local vault/public
  -> automatic indexing (vector + FTS)
  -> local LLM search and chat
```

Add to `data/loremate/config.yaml`:

```yaml
library:
  repo_url: git@github.com:mintnlatte/loremate-library.git
  branch: main
```

Then click **Sync Library** in the sidebar.
