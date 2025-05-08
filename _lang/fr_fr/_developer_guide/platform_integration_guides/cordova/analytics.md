---
nav_title: Analyse
article_title: Intégration de l’analyse
page_order: 3
---

# Intégration de l’analyse

> Découvrez comment intégrer l'analyse pour le SDK Braze Cordova.

{% multi_lang_include cordova/prerequisites.md %}

## Journalisation des événements personnalisés

Pour enregistrer des événements personnalisés, utilisez la méthode `logCustomEvent()`. Pour des instructions plus approfondies, consultez les guides [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) pour l'enregistrement des événements personnalisés.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logCustomEvent("CUSTOM_EVENT_WITH_PROPERTIES", properties);
```

## Enregistrer les achats

Pour enregistrer les achats, utilisez la méthode `logPurchase()`. Pour des instructions plus détaillées, consultez les guides [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) pour l'enregistrement des achats.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% alert tip %}
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions).
{% endalert %}

## Définition des attributs personnalisés

Pour définir des attributs personnalisés, utilisez la méthode `setCustomUserAttribute()`. Pour des instructions plus approfondies, consultez les guides [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) définissant les attributs personnalisés.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```

## Définir des ID utilisateur

Pour définir les ID des utilisateurs, utilisez la méthode `changeUser()`. Pour des instructions plus approfondies, consultez les guides [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) pour la définition des ID utilisateur.

```javascript
BrazePlugin.changeUser("USER_ID");
```
