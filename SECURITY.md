# Security

`compact-dev` generates repository scaffolding and inspects local project structure.

- Never place credentials, private keys, `.env`, Vercel tokens, or GitHub tokens in presets.
- Generated `.env.example` files must contain names and safe examples only.
- `compact audit` flags common secret-bearing filenames and backup artifacts; it is a hygiene check, not a substitute for secret scanning.
- Deployment and provider linking are deliberately outside `compact init`.
