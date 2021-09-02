---
nav_title: Location Tracking
article_title: Location Tracking for Windows Universal
platform: Windows Universal
page_order: 6
description: "This reference article covers how add location tracking to your Windows Universal app."
tool: Location

---

# Location Tracking

1. Ensure that within your `Package.appxmanifest` file the following option is checked:
  - Location
2. If you want to turn off automatic location tracking, set `<DisableLocationCollection>false</DisableLocationCollection>` to true in your `AppboyConfiguration.xml`
