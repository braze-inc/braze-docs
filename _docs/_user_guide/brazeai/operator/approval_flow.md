---
nav_title: Approval Flow
article_title: BrazeAI Operator<sup>TM</sup> approval flow
page_order: 2
description: "Learn how the approval flow works when BrazeAI Operator<sup>TM</sup> proposes changes in the dashboard."
---

# BrazeAI Operator<sup>TM</sup> approval flow

> Learn how the approval flow works when BrazeAI Operator<sup>TM</sup> proposes changes in the dashboard.

## How approval cards work

When Operator proposes changes in the dashboard (such as filling in form fields, updating settings, or generating images), it presents each change as an approval card for review.

1. **Operator summarizes the plan:** Operator explains what it plans to do before showing approval cards.
2. **Individual approval cards appear:** Each proposed change is presented as a separate card that shows what Operator wants to change or do in the dashboard. For changes to existing values, both the previous value and the proposed value for comparison
3. **Review and approve:** Review each card and either approve or decline it.
4. **Action executes:** Approved actions are executed in Braze. Declined actions are not applied.

{% alert note %}
If an action fails after approval, Operator will notify with details about the failure.
{% endalert %}

## Modifying a plan

To change something Operator proposed, describe the modification in the chat using natural language. Operator will refresh the approval list with updated items. Previously approved and executed items remain unchanged.

{% alert note %}
Approved actions can't be undone through Operator. Describe the new change to Operator or make changes manually in the dashboard.
{% endalert %}

## Auto-approve all actions

The **Auto-approve all actions** toggle is located in the Operator chat panel.

- **On:** Operator's suggested actions execute immediately without requiring manual approval. Some actions still require explicit approval for safety, such as generating images or making modifications to workspace-level settings.
- **Off (default):** All proposed actions follow the approval flow described above.

{% alert important %}
Auto-approve resets when you refresh the page, open a new tab, or log out and back in. Moving between pages in the dashboard does not reset it. Auto-approve can be turned off at any time.
{% endalert %}

When auto-approve is enabled, a confirmation modal appears to verify your choice.

> Add image for auto-approve toggle and confirmation modal.
