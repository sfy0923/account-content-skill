# Repository guidance

This repository distributes one portable account content workflow Skill.

- Treat `skills/account-content-workflow/` as the source of truth; preserve its relative references and all resources.
- Keep shared routing and invariant decisions in `SKILL.md`; put stage-specific detail in the corresponding reference.
- Preserve the seven scoring weights, the 90-point threshold, semantic deduplication, fact boundaries and genuine confirmation state unless the user explicitly changes them.
- Keep client-specific business facts and matrix settings in project records, not in universal Skill defaults.
- Do not publish original client materials, local paths, credentials, private evaluation answers or execution logs.
- Test observable behavior. Distinguish structural validation, synthetic tests, real project acceptance, independent review and GitHub installation checks.
- For authorized feedback updates, make the relevant change, check regressions, update validation notes and version metadata as appropriate, then commit and synchronize within the user's authorization. No force push or unrelated repository edits.
- Stage explicit paths only. Before pushing, inspect changes and confirm the target repository and branch from live Git state.
- Follow `docs/maintenance.md`; never claim a scheduled automation exists unless one was actually created.
