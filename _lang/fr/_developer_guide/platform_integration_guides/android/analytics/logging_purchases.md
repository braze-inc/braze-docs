---
nav_title: Enregistrer les achats
article_title: Enregistrer les achats pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Cet article de référence montre comment suivre les achats et les revenus dans l’application et attribuer des propriétés d’achat dans votre application Android ou FireOS."

---
 
# Enregistrer les achats pour Android et FireOS

Enregistrez les achats dans l’application afin que vous puissiez suivre vos revenus au fil du temps et entre leurs différentes sources, tout en segmentant vos utilisateurs selon leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant l’implémentation, assurez-vous d’étudier des exemples d’options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d’achat dans notre [aperçu d’analytique][3].

## Suivi des achats et des revenus

Pour utiliser cette fonction, appelez [`logPurchase()`][6] après un achat réussi dans votre application. Si l’identifiant du produit est vide, l’achat ne sera pas enregistré sur Braze.

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

Vous pouvez ajouter des métadonnées sur les achats en transmettant un [tableau de propriétés de l'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) ou un [objet Propriétés Braze][4] avec vos informations d'achat.

#### Formatage de l’objet Braze Properties

Les propriétés sont définies comme des paires clé-valeur. Les clés sont des objets `String` et les valeurs peuvent être des objets `String`, `int`, `float`, `boolean`, ou [`Date`][5].

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

Consultez notre [KDoc][6] pour plus d’informations.

### Journaliser les achats au niveau de la commande
Si vous souhaitez journaliser les achats au niveau de la commande au lieu du niveau de produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Consultez notre [spécification d’objet d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) pour en savoir plus. 

### Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### API REST

Vous pouvez également utiliser notre API REST pour enregistrer les achats. Reportez-vous à la [Documentation de l’API utilisateur][1] pour plus de détails.

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html
[5]: http://developer.android.com/reference/java/util/Date.html
[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-purchase.html
