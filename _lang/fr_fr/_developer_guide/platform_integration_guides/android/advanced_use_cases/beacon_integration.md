---
nav_title: Intégration de balise
article_title: Intégration de balise pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Cet article de référence explique comment enregistrer des événements personnalisés à l’aide des balises Gimbal pour Android ou FireOS."

---

# Intégration de balise

> Cet article vous expliquera comment intégrer des types spécifiques de balises avec Braze pour permettre la segmentation et la messagerie.

## Balises Gimbal

Une fois que vous avez configuré et intégré vos balises Gimbal dans votre application, vous pouvez enregistrer des événements personnalisés pour des choses comme une visite qui commence ou se termine, ou une balise vue. Vous pouvez également enregistrer des propriétés pour ces événements, comme le nom du lieu ou le temps de pause.

Pour enregistrer un événement personnalisé lorsqu’un utilisateur entre dans un lieu, incluez ce code dans la méthode `onVisitStart` :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

Le `requestImmediateDataFlush` vérifie que votre événement sera enregistré même si l'application est en arrière-plan, et le même processus peut être implémenté pour quitter un emplacement. Notez que l’activité et le contexte dans lesquels vous travaillez peuvent changer la manière exacte dont vous intégrez les lignes `logCustomEvent` et `requestImmediateDataFlush`. Notez également que ce code crée et incrémente un événement personnalisé unique pour chaque nouveau lieu que l’utilisateur saisit. Ainsi, si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement personnalisé générique « Lieu saisi » et d’inclure le nom du lieu comme propriété d’événement.
