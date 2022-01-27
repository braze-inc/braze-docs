---
nav_title: Achats de journalisation
article_title: Achats de journalisation pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 4
description: "Cet article de référence montre comment suivre les achats et les revenus dans l'application et attribuer des propriétés d'achat dans votre application Android."
---

# Enregistrement des achats pour Android/FireOS

Enregistrez vos achats dans l'application afin de pouvoir suivre vos revenus au fil du temps et à travers les sources de revenus. ainsi que segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous rapportez dans une devise autre que le dollar seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été déclarés.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre [Aperçu analytique][3].

## Suivi des achats et des revenus

Pour utiliser cette fonctionnalité, ajoutez cette méthode d'appel après un achat réussi dans votre application :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal prix,
   int quantité
);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantité: Int
)
```

{% endtab %}
{% endtabs %}

__Si l'identifiant du produit est vide, l'achat ne sera pas enregistré sur Brésil.__ Voir le [KDoc][6] pour plus d'informations.

{% alert tip %}
  Si vous passez une valeur de `10 USD`, et une quantité de `3` alors qui se connectera au profil de l'utilisateur comme 3 achats de 10 dollars pour un total de 30 dollars. La quantité doit être inférieure ou égale à 100. Les valeurs d'achat peuvent être négatives.
{% endalert %}

### Ajout de propriétés

Vous pouvez ajouter des métadonnées sur les achats en passant un objet [Propriétés de Braze][4] avec vos informations d'achat.

Les propriétés sont définies comme des paires clé-valeur.  Les clés sont des objets `String` et les valeurs peuvent être `String`, `int`, `float`, `booléen`, ou [`Date`][5] objets.

{% tabs %}
{% tab JAVA %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endtab %}
{% endtabs %}

Consultez le [KDoc][6] pour plus d'informations.

### Clés réservées

Les clés suivantes sont __RÉSERVÉES__ et __NE PEUT PAS__ être utilisées comme propriétés d'achat:

- `Heure`
- `identifiant_produit`
- `Quantité`
- `nom_événement`
- `prix`
- `Devise`

### API REST

Vous pouvez également utiliser notre API REST pour enregistrer vos achats. Reportez-vous à la [documentation de l'API utilisateur][1] pour plus de détails.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[4]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html
[5]: http://developer.android.com/reference/java/util/Date.html
[6]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/log-purchase.html
