---
nav_title: Tracking Push Unsubscribes
article_title: Tracking Push Unsubscribes
page_type: solution
description: "This help article provides some tips to track push unsubscribes."
channel: push
---

# Tracking push unsubscribes

Push unsubscribes are dependent on when there's an update to a user's push status from, for example, Apple or Google. This means push unsubscribes are not included as a metric in push campaign analytics.

As a workaround, we recommend creating a custom event for push unsubscribes based on whether a user's push enabled status is `true` or `false` in order to track this metric.