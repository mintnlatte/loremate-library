# loremate-library

`loremate-library` is the shared knowledge library repository for loremate.

This repository stores public, reusable knowledge that can be browsed from the loremate web client, downloaded by directory, copied into a local `vault/public` space, indexed automatically, and used for local LLM search and chat.

## Purpose

- Manage shared public knowledge in one GitHub repository.
- Organize knowledge by project, organization, and topic.
- Let each loremate user download only the directories they need.
- Keep downloaded documents searchable through the local loremate index.

## Scope

Only content that is safe to share should be added to this repository.

Good examples:

- Public project documentation
- Technical concept notes
- Sanitized operation guides
- Learning notes and reference summaries

Do not add:

- Passwords, tokens, API keys, or credentials
- Personal or customer information
- Internal network addresses or server access details
- Confidential company documents
- Private vault documents

## Directory Structure

Initial structure:

```text
projects/
  loremate/
    README.md
    public/
      README.md

organizations/
  README.md

topics/
  README.md
```

Future example:

```text
topics/
  security/
    authentication/
      jwt-rfc-7519/
      oauth2-rfc-6749/
      tls-rfc-8446/

  programming/
    python/
      pep-8/
      pep-484/

  machine-learning/
    rag/
    transformers/

  databases/
    postgresql/
      indexes/
      mvcc/

  infrastructure/
    kubernetes/
      pods/
      services/

  security-best-practices/
    owasp-top-10/
      injection/
      broken-authentication/

  legal/
    korea/
      privacy/
```

## Authoring Rules

- Prefer `README.md` as the entry point for each directory.
- Keep one clear topic or purpose per directory.
- Use Markdown for documents.
- Prefer lowercase English names with numbers and hyphens for files and directories.
- Remove sensitive information before committing any document.

## loremate Flow

```text
GitHub loremate-library
  -> loremate Library sync
  -> select directory
  -> download to local vault/public
  -> automatic indexing
  -> local LLM search and chat
```

## Current Status

This repository is being prepared as the initial shared knowledge library for loremate.
