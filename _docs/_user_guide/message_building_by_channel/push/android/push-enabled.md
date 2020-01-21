---
nav_title: "Push-Enabled Users"
page_order: 1
page_type: reference
description: "This reference article goes over what it means to be Push-Enabled."

platform: Android
channel:
  - Push
tool:
  - Docs
  - Dashboard
  - Campaigns
---

# What makes an Android user "Push-Enabled"?


When users uninstall or turn off push notifications in their settings, Braze will update the user’s push enabled status. We will assign the user a “Push registered for no apps” value, letting our clients know that push will not be delivered to that user. If a user re-installs or changes their push settings back, Braze will update the profile accordingly. 