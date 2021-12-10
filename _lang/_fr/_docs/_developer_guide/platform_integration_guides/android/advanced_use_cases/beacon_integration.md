---
nav_title: Intégration de balises
article_title: Intégration de balises pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 2
description: "Cet article explique comment enregistrer des événements personnalisés en utilisant les balises Gimbal pour Android."
---

# Intégration des balises

Ici, nous allons parcourir comment intégrer des types spécifiques de balises avec Braze pour permettre la segmentation et la messagerie.

## Balises de Nacelle

Une fois que vos balises Gimbal sont configurées et intégrées dans votre application, vous pouvez enregistrer des événements personnalisés pour des choses comme une visite commençant ou se terminant, ou une balise en cours de vue. Vous pouvez également enregistrer des propriétés pour ces événements, comme le nom du lieu ou le temps de maintenance.

Pour enregistrer un événement personnalisé lorsqu'un utilisateur entre un lieu, saisissez ce code dans la méthode `onVisitStart`:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entré" + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entré" + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

La `requestImmediateDataFlush` garantit que votre événement sera enregistré même si l'application est en arrière-plan, et le même processus peut être implémenté pour quitter un emplacement. Veuillez noter que l'activité et le contexte dans lesquels vous travaillez peuvent changer exactement la façon dont vous intégrez les lignes `logCustomEvent` et `requestImmediateDataFlush`. Notez également que ce qui précède créera et incrémentera un événement personnalisé unique pour chaque nouvel endroit que l'utilisateur entrera. En tant que tel, si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement personnalisé générique « Place Entrée » et d'inclure le nom du lieu comme propriété d'événement.
