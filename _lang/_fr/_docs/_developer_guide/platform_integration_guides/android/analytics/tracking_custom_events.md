---
nav_title: Événements personnalisés de suivi
article_title: Suivi des événements personnalisés pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 2
description: "Cet article de référence couvre comment ajouter et suivre des événements personnalisés pour votre application Android."
---

# Suivi des événements personnalisés pour Android/FireOS

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les habitudes d'utilisation de votre application et pour segmenter vos utilisateurs par leurs actions sur le tableau de bord.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. les attributs personnalisés vs les événements d'achat dans notre [Aperçu analytique][], ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Ajout d'un événement personnalisé

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```

{% endtab %}
{% endtabs %}

Consultez le [Javadoc][2] pour plus d'informations.

### Ajout de propriétés

Vous pouvez ajouter des métadonnées sur les événements personnalisés en passant un objet [Propriétés de Braze][4] avec votre événement personnalisé.

Les propriétés sont définies comme des paires clé-valeur.  Les clés sont des objets `String` et les valeurs peuvent être `String`, `int`, `float`, `booléen`, ou [`Date`][3] objets.

{% tabs %}
{% tab JAVA %}

```java
BrazeProperties eventProperties = new BrazeProperties();
eventProperties.addProperty("key", "value");
Braze.getInstance(YOUR_ACTIVITY.this).logCustomEvent(YOUR_EVENT_NAME, eventProperties);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val eventProperties = BrazeProperties()
eventProperties.addProperty("key", "value")
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME, eventProperties)
```

{% endtab %}
{% endtabs %}

### Clés réservées

Les clés suivantes sont __RESERVES__ et __NE PEUT PAS__ être utilisées comme propriétés d'événement personnalisées:

- `Heure`
- `nom_événement`

Consultez le [Javadoc][6] pour plus d'informations.

[Aperçu analytique]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#logCustomEvent(java.lang.String)
[3]: http://developer.android.com/reference/java/util/Date.html
[4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/outgoing/BrazeProperties.html
[6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#logCustomEvent(java.lang.String,%20com.appboy.models.outgoing.AppboyProperties)
