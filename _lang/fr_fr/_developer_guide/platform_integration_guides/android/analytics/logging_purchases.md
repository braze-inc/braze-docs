---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Cet article de référence montre comment suivre les achats et les revenus dans l’application et attribuer des propriétés d’achat dans votre application Android ou FireOS."

---
 
# Enregistrer les achats

> Enregistrez les achats dans l’application afin que vous puissiez suivre vos revenus au fil du temps et entre leurs différentes sources, tout en segmentant vos utilisateurs selon leur valeur à vie. Cet article de référence montre comment suivre les achats et les revenus dans l’application et attribuer des propriétés d’achat dans votre application Android ou FireOS.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant la mise en œuvre, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans notre [aperçu analytique]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

## Suivi des achats et des revenus

Pour utiliser cette fonctionnalité, appelez [`logPurchase()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html) après un achat réussi dans votre application. Si l’identifiant du produit est vide, l’achat ne sera pas enregistré sur Braze.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous transmettez une valeur de `10 USD` et une quantité de `3`, trois achats de 10 dollars pour un total de 30 dollars seront enregistrés sur le profil utilisateur. Les quantités doivent être inférieures ou égales à 100. Les valeurs des achats peuvent être négatives.
{% endalert %}

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées sur les achats en passant soit un [tableau de propriétés d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) soit un objet [Propriétés Braze](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html) avec vos informations d'achat.

#### Formatage de l’objet Braze Properties

Les propriétés sont définies comme des paires clé-valeur. Les clés sont des objets de type `String` et les valeurs peuvent être des objets de type `String`, `int`, `float`, `boolean` ou [`Date`](http://developer.android.com/reference/java/util/Date.html).

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

Pour plus d’informations, reportez-vous à notre [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html).

### Journaliser les achats au niveau de la commande
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### API REST

Vous pouvez également utiliser notre API REST pour enregistrer les achats. Reportez-vous à la [Documentation de l'API utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

