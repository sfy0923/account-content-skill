# Repository guidance

This repository distributes the portable GGB workflow and its independently installable IP general-topics Skill.

- Treat `skills/ggb/` and `skills/ip-general-topics/` as the distribution sources; preserve their relative references and all resources. Synchronize and compare any separate authoring source before publishing.
- Keep shared routing and invariant decisions in `SKILL.md`; put stage-specific detail in the corresponding reference.
- Preserve the seven scoring weights, the 90-point threshold, semantic deduplication, fact boundaries and genuine confirmation state unless the user explicitly changes them.
- Research-stage potential and readiness scores belong to references/research.md; they do not replace or convert into the formal seven-item score. Keep the stage and missing-data state visible.
- Keep client-specific business facts and matrix settings in project records, not in universal Skill defaults.
- Do not publish original client materials, local paths, credentials, private evaluation answers or execution logs.
- Test observable behavior. Distinguish structural validation, synthetic tests, real project acceptance, independent review and GitHub installation checks.
- For authorized feedback updates, make the relevant change, check regressions, update validation notes and version metadata as appropriate, then commit and synchronize within the user's authorization. No force push or unrelated repository edits.
- Stage explicit paths only. Before pushing, inspect changes and confirm the target repository and branch from live Git state.
- Follow `docs/maintenance.md`; never claim a scheduled automation exists unless one was actually created.
