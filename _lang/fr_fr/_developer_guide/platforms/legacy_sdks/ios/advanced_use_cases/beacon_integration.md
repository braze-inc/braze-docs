---
nav_title: Intégration de balise
article_title: Intégration de balise pour iOS
platform: iOS
page_order: 4
description: "Cet article traite de la journalisation des événements personnalisés à l'aide des balises Infillion pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration de balise

Ici, nous allons découvrir la manière d’intégrer des types spécifiques de balises avec Braze pour permettre la segmentation et la messagerie.

## Balises Infillion

Une fois vos balises Infillion configurées et intégrées à votre application, vous pouvez enregistrer des événements personnalisés tels que le début ou la fin d'une visite ou l'observation d'une balise. Vous pouvez également enregistrer des propriétés pour ces événements, comme le nom du lieu ou le temps de pause.

Pour enregistrer un événement personnalisé lorsqu’un utilisateur accède à un endroit, saisissez ce code dans la méthode `didBeginVisit` :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

Le `flushDataAndProcessRequestQueue` garantit que votre événement est enregistré, même si l’application est en arrière-plan et que le même processus peut être implémenté pour quitter un emplacement. Notez que cela créera et incrémentera un événement personnalisé unique pour chaque nouvel endroit que l’utilisateur visitera. Si vous prévoyez de créer plus de 50 endroits, nous vous recommandons de créer un événement personnalisé générique « Place Entered » (Lieu accédé) et d’inclure le nom du lieu comme propriété d’événement.
