---
nav_title: Suivre la position
article_title: Suivre la position pour Windows Universal
platform: Windows Universal
page_order: 6
description: "Cet article de référence explique comment ajouter un suivi de la position à votre application Windows Universal."
tool: Location
hidden: true
---

# Suivre la position
{% multi_lang_include archive/windows_deprecation.md %}

1. Assurez-vous que `Package.appxmanifest` est coché dans votre fichier`location`.
2. Si vous souhaitez désactiver le suivi automatique de la position, définissez `<DisableLocationCollection>false</DisableLocationCollection>` sur `true` dans votre `AppboyConfiguration.xml`.
