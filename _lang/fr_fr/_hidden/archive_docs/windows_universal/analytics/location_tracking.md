---
nav_title: Suivi de localisation
article_title: Suivre la localisation pour Windows Universal
platform: Windows Universal
page_order: 6
description: "Cet article de référence explique comment ajouter une fonction de suivi de la localisation à votre application Windows Universal."
tool: Location
hidden: true
---

# Suivi de localisation
{% multi_lang_include archive/windows_deprecation.md %}

1. Assurez-vous que `Package.appxmanifest` est coché dans votre fichier`location`.
2. Si vous souhaitez désactiver le suivi automatique de la localisation, définissez `<DisableLocationCollection>false</DisableLocationCollection>` sur `true` dans votre `AppboyConfiguration.xml`.
