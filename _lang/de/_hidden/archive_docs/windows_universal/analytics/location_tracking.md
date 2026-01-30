---
nav_title: Standort-Tracking
article_title: Standort-Tracking für Windows Universal
platform: Windows Universal
page_order: 6
description: "Dieser referenzierte Artikel beschreibt, wie Sie Ihrer Windows Universal App Standort-Tracking hinzufügen."
tool: Location
hidden: true
---

# Standort-Tracking
{% multi_lang_include archive/windows_deprecation.md %}

1. Vergewissern Sie sich, dass in Ihrer Datei `Package.appxmanifest` die Option `location` aktiviert ist.
2. Wenn Sie das automatische Standort-Tracking deaktivieren möchten, setzen Sie `<DisableLocationCollection>false</DisableLocationCollection>` auf `true` in Ihrem `AppboyConfiguration.xml`.
