---
nav_title: Reviewing Actions
article_title: Reviewing BrazeAI Operator<sup>TM</sup> actions
page_order: 2
description: "Learn how to review and approve actions when BrazeAI Operator<sup>TM</sup> proposes changes in the dashboard."
---

# Reviewing BrazeAI Operator<sup>TM</sup> actions

> Learn how to review and approve actions when BrazeAI Operator<sup>TM</sup> proposes changes in the dashboard.

## How action cards work

When Operator proposes changes in the dashboard (such as filling in form fields, updating settings, or generating images), it presents each change as an action card for review.

1. **Operator summarizes the plan:** Operator explains what it plans to do before showing action cards.
2. **Individual action cards appear:** Each proposed change is presented as a separate card that shows what Operator wants to change or do in the dashboard. For changes to existing values, both the previous value and the proposed value are shown side by side for comparison.
3. **Review and approve:** Review each card and either approve or decline it.
4. **Action executes:** Approved actions are executed in Braze. Declined actions are not applied.

{% alert note %}
If an action fails after approval, Operator will notify with details about the failure.
{% endalert %}

![Operator presenting suggested action cards for review.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; float:right; margin-left:15px;"}

## Modifying a plan

To change something Operator proposed, describe the modification in the chat using natural language. Operator will refresh the action list with updated items. Previously approved and executed items remain unchanged.

{% alert note %}
Approved actions can't be undone through Operator. Describe the new change to Operator or make changes manually in the dashboard.
{% endalert %}

## Auto-approve all actions

The **Auto-approve all actions** toggle is located in the Operator chat panel.

- **On:** Operator's suggested actions execute immediately without requiring manual approval. Some actions still require explicit approval for safety, such as generating images or making modifications to workspace-level settings.
- **Off (default):** All proposed actions follow the review process described above.

{% alert important %}
Auto-approve resets when you refresh the page, open a new tab, or log out and back in. Moving between pages in the dashboard does not reset it. Auto-approve can be turned off at any time.
{% endalert %}

When auto-approve is enabled, a confirmation modal appears to verify your choice.

![The auto-approve toggle and confirmation modal in the Operator chat panel.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:40%;"}
