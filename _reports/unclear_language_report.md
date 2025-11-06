# Unclear / Ambiguous Language Audit

Generated: 2025-11-05
Branch: ae-localization-optimization
Scope: Sampled `_docs/_user_guide/**`, `_docs/_partners/**`, permissions include.
Focus Categories:
1. Modal uncertainty (may, might, could, can, should, typically, often, sometimes)
2. Vague quantifiers (some, several, a number of, various)
3. Conditional ambiguity (optional vs must juxtaposition, unclear requirement boundaries)
4. Redundancy / repetition (duplicate sentences or duplicated guidance in same section)
5. Mixed scope definitions (permissions: permission sets vs roles vs teams) – clarity gaps
6. Risk/impact statements lacking actionable guidance
7. Potential contradiction (feature required + described as optional, or cached duration guarantees vs disclaimers)

---
## 1. Modal Uncertainty
These lines use modals without clarifying conditions, outcomes, or decision criteria.
| File | Line | Excerpt | Issue | Recommendation |
| --- | --- | --- | --- | --- |
| whatsapp/meta_resources.md | 74 | "This may result in lower delivery rates..." | May without mitigation guidance | Add: "To monitor impact, review X metric daily and adjust Y." |
| key_value_pairs.md | 140 | "...may be used for whatever purpose you choose." | Open-ended; no guardrails | Provide allowed vs discouraged examples (performance/privacy). |
| connected_content/caching_responses.md | 44 | Multiple repeated may statements about eviction | Suggestion vs actual behavior unclear | Replace with description of policy + deterministic cache invalidation triggers. |
| connected_content/making_an_api_call.md | 68 | "Braze systems may make the same Connected Content API call..." | Unclear frequency; no guidance to mitigate | Provide max duplicate call rate and recommendation (idempotent design). |
| facebook_audience_sync.md | 120 | "typically fewer than 1,000 users" | Typical threshold unverified | Specify exact threshold if contractual, else state range or link reference. |
| judo.md | 19 | "may incorporate content..." | Diffuse scope | Enumerate concrete supported components list. |
| caching_responses.md | 76 | "might be used across multiple users" | Data mixing risk not addressed | Add privacy guidance re user-specific secrets, avoid PII in cached responses. |

(Additional matches exist; prioritized top impact.)

## 2. Vague Quantifiers
| File | Line | Excerpt | Issue | Recommendation |
| --- | --- | --- | --- | --- |
| campaigns_canvases.md | 19 | "four main types" then table also includes API variations | Verify completeness | Confirm only four canonical types; if more, relabel "primary types". |
| workspaces.md | 58 | "several games" | Non-specific | Replace with example count or remove word. |
| sessionm.md | 112 | "several different internal levers" | Vague mechanism | Name levers or link to taxonomy. |
| cloudinary.md | 165 | "Further customization" | Too general | Provide 2–3 concrete parameter examples. |
| amazon_personalize.md | 38 | "Some common use cases" | Could mislead if list incomplete | Add note "Examples include..." or link to full catalog. |

## 3. Conditional Ambiguity / Optional vs Required
| File | Line | Excerpt | Issue | Recommendation |
| in-app_messages/traditional/create.md | 326 | "start date ... must" / "end date optional" | Clear but could add use-case guidance | Explain when to omit end date; add lifecycle scenarios. |
| content_blocks_templates/post_update_content_block.md | 38–55 | Numerous "optional" + strict length constraints | Optional yet constraints suggest validation | Clarify that constraints apply if field present; add error behavior. |
| schedule_messages/post_schedule_triggered_campaigns.md | 68 | broadcast optional yet "must" set true in some cases | Potential confusion for first-time integrators | Add explicit decision table (broadcast vs recipients). |
| link_shortening.md | 85–86 | user_click_tracking_enabled depends on link_shortening_enabled | Hidden coupling | Add parameter dependency diagram / table. |

## 4. Redundancy / Repetition
| File | Line(s) | Excerpt | Issue | Recommendation |
| caching_responses.md | 44 (repeated 4x) | Same paragraph repeated | Noise / risk of divergence | Deduplicate single authoritative paragraph. |
| facebook_audience_sync.md | 167 (duplicate) | Repeats bullet about reaching limit | Remove duplicate instance. |
| judo.md | 19 + 31 + 33 | Repetitive "may" phrasing | Streamline; consolidate experience categories list. |
| making_an_api_call.md | 68 (repeated 3x) | Duplicate call behavior paragraph | Keep one; reference idempotency guidelines. |

## 5. Mixed Scope Definitions (Permissions)
`_includes/permissions.md` lists "Scope of access" values: "Company wide", "Specific workspaces", "Specific dashboard".
Issues:
- "Company wide" vs "Specific dashboard" ambiguous—dashboard is already company-level. Suggest "Workspace-level segment access" or "Audience filtering layer" for Teams.
- Roles description mixes role concept with named example; could confuse "workspace-access controls" vs "permissions".
Recommendations:
1. Standardize scope labels: "Organization-wide", "Workspace-specific", "Audience-restricted (cross-workspace)".
2. Add summary sentence clarifying layering: Permission set (capabilities) + Role (capabilities + workspace scope) + Team (audience scope overlay).
3. Provide visual matrix (Feature x Axis: Permissions, Workspace Access, Audience Filtering).

## 6. Risk/Impact Statements Lacking Actionable Guidance
| File | Line | Excerpt | Gap | Recommendation |
| connected_content/making_an_api_call.md | 66 | "confirm your usage won't violate any rate-limiting" | No method to confirm | Add steps: monitor 429 count, preflight HEAD, implement exponential backoff limit N. |
| cloudinary.md | 106 | "results in recipients only receiving assets that are contextually relevant" | Missing validation/testing steps | Provide preview test instructions and fallback behavior if transformation fails. |
| google_audience_sync.md | 85 | Liability note about consent | No remediation path | Include logic snippet for filtering consent attributes and audit frequency. |
| link_shortening.md | 86 | Tracking dependency | No failure mode description | Add: "If dependency unmet, API returns 400 with code X". |

## 7. Potential Contradictions
| File | Line | Excerpt | Concern | Recommendation |
| caching_responses.md | 44 | Cache duration suggestion vs eviction unpredictability | Could mislead SLA assumptions | Provide explicit statement: "Cache is opportunistic; do not rely for consistency; design idempotent fetch." |
| facebook_audience_sync.md | 120 | "typically fewer than 1,000" threshold vs error conditions | Implicit policy vs absence of official doc | Cite official Facebook doc or replace with "below ad network minimum audience size". |
| permissions.md | Table | Teams scope "Specific dashboard" vs roles/permission sets layering | Mis-scope terms | Revise terminology (see Section 5). |

## 8. Prioritization (Severity Ranking)
1. Contradictions impacting configuration (broadcast parameter logic; caching behavior). 
2. Risk statements without mitigation (rate limiting, consent liability). 
3. Permissions scope ambiguity (access control misapplication risk). 
4. Redundancies (noise, maintenance overhead). 
5. Modal uncertainty diminishing instructional clarity. 
6. Vague quantifiers (low severity unless tied to compliance/thresholds). 

## 9. Recommended Remediation Playbook
| Category | Fix Pattern |
| --- | --- |
| Modal uncertainty | Replace modal with deterministic behavior OR add conditional clause + action ("If X, do Y"). |
| Vague quantifier | Replace with range, exact number, or remove non-informative quantifier. |
| Optional vs must | Introduce decision table clarifying mutually exclusive parameters. |
| Repetition | Consolidate; ensure single source of truth. |
| Permissions scope | Introduce layered model diagram + consistent vocabulary. |
| Risk statements | Append "Monitoring" + "Fallback" subsections. |
| Cache vagueness | Add explicit non-SLA disclaimer + design principle. |

## 10. Next Steps
1. Implement priority fixes (Sections 3,5,7) in a dedicated PR.
2. Add lint rule (regex) for overuse of modals without following action clause.
3. Create style guideline addendum: "Uncertainty & Risk Communication".
4. Add permissions matrix asset (`_includes/permissions_matrix.html`).
5. Run second-pass scan for "may" preceded by subject where deterministic behavior known.

---
## 11. Appendix: Detection Heuristics
Patterns flagged: `\b(may|might|could|should|typically|often|sometimes|some|several|various|a number of|as needed|as necessary)\b` plus `must.*optional|optional.*must`.
False positives intentionally included where context could benefit from clarification.

## 12. Limitations
- Automated pattern scan; deeper logical contradictions (e.g., between separate pages) not exhaustively analyzed.
- Threshold references (e.g., audience size) require SME validation for authoritative figures.

---
## 13. Summary
Total sample ambiguous matches reviewed (subset): ~150 across user guide and partner docs. Prioritized ~40 for immediate clarification. Focus on reducing uncertainty, clarifying configuration decisions, and improving permission model comprehension.

---
Generated by automated audit pass. Ready for editorial refinement.
