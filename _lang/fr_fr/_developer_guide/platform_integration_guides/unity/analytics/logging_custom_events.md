---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "Cet article de référence explique comment journaliser les événements personnalisés sur la plateforme Unity."

---

# Suivre les événements personnalisés

> Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord.

Avant de procéder à la mise en œuvre, n'oubliez pas de consulter les exemples d'options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques.][4] Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze prend également en charge l’ajout de métadonnées aux événements personnalisés en transmettant un `Dictionary` de propriétés d’événement :

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## API REST

Vous pouvez également utiliser notre API REST pour enregistrer les événements. Reportez-vous à la documentation de l'[API des utilisateurs][5] pour plus de détails.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
