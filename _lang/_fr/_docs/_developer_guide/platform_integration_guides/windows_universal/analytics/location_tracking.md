---
nav_title: Suivi de la localisation
article_title: Suivi de localisation pour Windows Universal
platform: Univers Windows
page_order: 6
description: "Cet article de référence décrit comment ajouter le suivi de la localisation à votre application Windows Universelle."
tool: Localisation
---

# Suivi de localisation

1. Assurez-vous que dans votre fichier `Package.appxmanifest` , l'option suivante est cochée :
  - Localisation
2. Si vous voulez désactiver le suivi automatique de localisation, définissez `<DisableLocationCollection>false</DisableLocationCollection>` à true dans votre `AppboyConfiguration.xml`
