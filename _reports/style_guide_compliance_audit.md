# Style Guide Compliance Audit

This audit maps repository content against the internal style and voice rules defined in `.github/copilot-instructions.md`. It focuses on language that affects clarity, inclusivity, directive tone, and durability of documentation.

## 1. Summary
- Scope: English source docs + includes; localized directories flagged where patterns appeared (not remediated yet).
- Detection Method: Regex pattern scans + spot manual validation.
- Total Raw Matches Collected (approximate, truncated at 200 per pattern):
  - Temporal/outdated phrasing: >140
  - Condescending/trivializing language (simple|simply|just|easy): 200 (cap)
  - Ableist / biased terms: 25 (majority inside style examples; few live docs)
  - "must" vs "optional" contradictions: 200 (cap)
  - Passive voice candidates: 200 (cap)
  - Future tense overuse ("will" when not future): addressed previously; residual pockets to review in release notes.

## 2. Severity Rubric
| Severity | Criteria | User Impact |
|----------|---------|-------------|
| Critical | Misleading requirement logic; could cause API misuse | High risk of integration errors |
| High | Ambiguous conditional behavior; outdated temporal language suggesting uncertainty | Slows adoption, support tickets |
| Medium | Tone/style violations (condescending, passive voice obscuring actor) | Minor clarity decrease |
| Low | Cosmetic phrasing, easily inferred meaning | Minimal impact |

## 3. Key Violation Categories & Representative Examples

### 3.1 Optional vs. Must Contradictions (Critical/High)
Pattern: Phrases combining "must" with "optional" without conditional context.
Example (API param tables): "The `broadcast` flag is optional and must be false when targeting segments." Recommended: "`broadcast` (boolean). Required only when sending to the full app audience. Omit or set to `false` when specifying users or segments."
Action: Introduce decision table template across API endpoint docs.

### 3.2 Temporal / Outdated Phrasing (High)
Pattern: currently|now|future|soon|new|latest|presently|at present|eventually.
Example: "This feature is currently in beta." Recommended: "This feature is in beta." (Add version/date if necessary: "Beta as of May 2024.")
Action: Remove vague temporal adverbs; anchor with explicit dates only when essential.

### 3.3 Condescending / Trivializing Language (Medium)
Pattern: simple|simply|just|easy.
Example: "Just add the header to authenticate." Recommended: "Add the header to authenticate."
Action: Strip trivializers from procedural steps; maintain neutral imperative.

### 3.4 Ableist / Biased Terms (Medium/High depending on context)
Matches: "blind", "struggle", "victim", brand phrase "Crazy Time" (proper noun; acceptable with context).
Example: "If the dashboard struggles under load..." Recommended: "If the dashboard experiences performance degradation under load..."
Action: Replace metaphorical ableist metaphors with precise technical descriptions; whitelist proper nouns.

### 3.5 Passive Voice Candidates (Medium)
Pattern heuristic: (was|were|is|are) + past participle.
Example: "The message was sent." Acceptable if emphasizing state; improve when instructive: "Braze sends the message." or "Send the message." Contextual review needed—do not mass replace.
Action: Rewrite action-oriented instructions to active voice; retain passive for neutral state reporting.

### 3.6 Future Tense Overuse (Medium)
Residual patterns of "will" describing current functionality.
Example: "The API will return a 200." Recommended: "The API returns 200." Action: Normalize to present tense unless genuine future events (scheduled deprecations).

## 4. Prioritized Remediation Plan
1. Decision Tables for Conditional Requirements (broadcast, segment targeting, tag creation logic). [Critical]
2. Temporal Language Normalization (remove "currently", "now", "new"). [High]
3. Ableist/Biased Language Review (replace metaphors; whitelist proper nouns). [High]
4. Trivializing Language Sweep (remove simple/simply/just/easy). [Medium]
5. Passive Voice Contextual Pass (focus on imperative steps). [Medium]
6. Future Tense Residual Cleanup (release notes, endpoint descriptions). [Medium]
7. Localization Alignment (flagged patterns forwarded to translation workflow). [Low]

## 5. Decision Table Template (to apply)
```
Parameter | Include? | Condition | Example
broadcast | Yes | Send to entire app audience | {"broadcast": true}
broadcast | No / false | Targeting users, segments, or aliases | {"broadcast": false, "segment_id": "abc"}
segment_id | Required | Targeting a segment (broadcast must be false or omitted) | {"segment_id": "abc"}
```

## 6. Replacement Guidelines
- Trivializers: "just" → (remove); "simply" → (remove); "easy" → (remove or rephrase to benefit); "simple" (as adjective) → consider neutral alternative ("basic", or rephrase).
- Ableist metaphors: "blind spot" → "gap"; "insane load" → "extreme load"; "struggles" → "experiences performance issues".
- Temporal: Remove unless date anchored. "Currently supports" → "Supports".
- Passive to Active (instructional): "Values are configured in the dashboard" → "Configure values in the dashboard.".

## 7. Tooling & Automation Suggestions
- Add pre-commit hook scanning for banned temporal + trivializing tokens.
- Maintain allowlist for proper nouns ("Crazy Time") to avoid false positives.
- Introduce lint rule categories: severity mapping to block merge for Critical/High.

## 8. Metrics & Tracking
Create CSV with columns: category,severity,file,line,excerpt,recommendation,status. Initial status = "pending"; update during remediation sprints.

## 9. Assumptions
- Some passive constructions intentionally retained for state description.
- Localized content remediation will follow source (English) cleanup; not in current sprint scope.
- Proper nouns containing flagged terms are acceptable when clearly brand/product names.

## 10. Next Steps
- Generate CSV dataset from raw matches (deduplicated, categorized).
- Apply decision tables to top 5 API docs with broadcast/segment logic.
- Implement trivializer removal batch edits.
- Draft inclusive language substitution list and circulate for SME approval.

---
Prepared as part of the content clarity and style compliance initiative.
