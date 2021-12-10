---
nav_title: Événements personnalisés de suivi
article_title: Suivi des événements personnalisés pour Windows Universal
platform: Univers Windows
page_order: 2
description: "Cet article de référence couvre la façon de suivre les événements personnalisés sur la plate-forme Windows Universelle."
---

# Suivi des événements personnalisés

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les habitudes d'utilisation de votre application et pour segmenter vos utilisateurs par leurs actions sur le tableau de bord.

Tous les événements sont enregistrés en utilisant le `EventLogger`, qui est une propriété exposée dans IAppboy. Pour obtenir une référence à la `EventLogger`, appelez `Appboy.SharedInstance.EventLogger`. Vous pouvez utiliser les méthodes suivantes pour suivre les actions importantes de l'utilisateur et les événements personnalisés :

```csharp
bool LogCustomEvent(chaîne VOTRE_EVENT_NAME)
```

Vous devriez également consulter nos notes sur [les conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

