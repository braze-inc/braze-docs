---
nav_title: Événements personnalisés de suivi
article_title: Suivi des événements personnalisés pour l'unité
platform:
  - Unité
  - iOS
  - Android
page_order: 1
description: "Cet article de référence décrit comment enregistrer les événements personnalisés sur la plate-forme Unity."
---

# Journalisation des événements personnalisés

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les habitudes d'utilisation de votre application et pour segmenter vos utilisateurs par leurs actions sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][4]. Vous devriez également consulter nos notes sur [les conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```csharp
AppboyBinding.LogCustomEvent("nom de l'événement");
```

Braze prend également en charge l'ajout de métadonnées sur les événements personnalisés en passant un `dictionnaire` de propriétés d'événement:

```csharp
AppboyBinding.LogCustomEvent("nom de l'événement", properties(Dictionary<string, object>));
```

## API REST

Vous pouvez également utiliser notre API REST pour enregistrer des événements. Reportez-vous à la documentation [de l'API utilisateur][5] pour plus de détails.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
