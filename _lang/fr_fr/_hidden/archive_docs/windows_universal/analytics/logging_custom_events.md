---
nav_title: Suivre les événements personnalisés
article_title: Suivre les événements personnalisés pour Windows Universal
platform: Windows Universal
page_order: 2
description: "Cet article de référence explique comment suivre les événements personnalisés sur la plateforme Universal Windows."
hidden: true
---

# Suivre les événements personnalisés
{% multi_lang_include archive/windows_deprecation.md %}

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les modèles d’utilisation de votre application et segmenter vos utilisateurs en fonction de leurs actions sur le tableau de bord. Nous vous recommandons également de vous familiariser avec les [conventions de dénomination de nos événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

Tous les événements sont enregistrés en utilisant le `EventLogger`, qui est une propriété exposée dans IAppboy. Pour obtenir une référence au `EventLogger`, appelez `Appboy.SharedInstance.EventLogger`. Vous pouvez utiliser les méthodes suivantes pour suivre les actions importantes des utilisateurs et les événements personnalisés :

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
