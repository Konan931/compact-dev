# Decision log

## 2026-09-17 — Separate generator from generated repository

`compact init` now operates on a user-selected target and composes declarative presets. The installed package path is no longer treated as the project root.

## 2026-09-17 — Provider presets are preparation, not deployment

The Vercel preset may create safe repository configuration and documentation, but linking, secret synchronization, preview creation, and production deployment remain explicit user actions.
