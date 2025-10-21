---
nav_title: Workspace Messaging Rate Limits
article_title: Workspace Messaging Rate Limits
page_order: 1
page_type: reference
description: "This article describes how to configure workspace messaging rate limits to control the rate at which messages are sent from your workspace."
hidden: true
---

# Workspace Messaging Rate Limits

Workspace messaging rate limits allow you to control the rate at which messages are sent from your entire workspace. This helps you manage your messaging volume across all campaigns and Canvases within the workspace.

## How it works

Workspace messaging rate limits apply to all outbound messaging from your workspace, including campaigns and Canvases. When you set a workspace rate limit, Braze will throttle message delivery to ensure the combined messaging volume from all sources doesn't exceed your specified limit.

## Setting your workspace messaging rate limit

To configure your workspace messaging rate limit:

1. In the Braze dashboard, go to **Settings** > **Global Rate Limits**.
2. Set your desired messaging rate limit.
3. Save your settings.

{% alert note %}
Workspace messaging rate limits affect all messaging channels and campaigns within your workspace. Make sure to consider your overall messaging strategy when setting these limits.
{% endalert %}

## Important considerations

- Rate limits apply to the entire workspace, not individual campaigns
- This setting affects all messaging channels (push, email, SMS, etc.)
- Changes to rate limits may take a few minutes to take effect
- Consider your peak messaging times when setting limits