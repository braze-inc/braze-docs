---
nav_title: Analytique
article_title: Analytique de Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "Cet article couvre l’analytique iOS, Android et FireOS pour la plateforme Xamarin."

---
 
# Analytique Xamarin

## Définir des ID utilisateur

{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).ChangeUser("YOUR_USER_ID");
```

Consultez les [instructions d’intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) pour une explication approfondie sur le moment auquel définir et modifier un ID utilisateur et comment le faire.

{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance().ChangeUser("YOUR_USER_ID");
```

Consultez les [instructions d’intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) pour une explication approfondie sur le moment auquel définir et modifier un ID utilisateur et comment le faire.
{% endtab %}
{% endtabs %}

## Suivre les événements personnalisés
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogCustomEvent("YOUR_EVENT_NAME");
```

Consultez les [instructions d’intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) pour une explication approfondie des bonnes pratiques de suivi des événements et des interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogCustomEvent ("YOUR_EVENT_NAME");
```

**Exemple d’implémentation** : `logCustomEvent` est utilisé `AppboySampleViewController.cs` au sein de l’exemple d’application [TestApp.XamariniOS](https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS).

Consultez les [instructions d’intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) pour une explication approfondie des bonnes pratiques de suivi des événements et des interfaces.
{% endtab %}
{% endtabs %}

## Enregistrer les achats
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogPurchase("product_id", 100);
```

Consultez les [instructions d’intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases=) pour une explication approfondie des bonnes pratiques de suivi des revenus et des interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogPurchase ("product_id", "USD", new NSDecimalNumber("10"));
```

**Exemple d’implémentation** : Vous pouvez voir les propriétés utilisateur définies dans la méthode `EventsAndPurchasesButtonHandler` de l’exemple d’application dans `AppboySampleViewController.cs`.

Consultez les [instructions d’intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) pour une explication approfondie des bonnes pratiques de suivi des revenus et des interfaces.
{% endtab %}
{% endtabs %}

### Journaliser les achats au niveau de la commande
Si vous souhaitez journaliser les achats au niveau de la commande au lieu du niveau de produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Consultez notre [spécification d’objet d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) pour en savoir plus. 

## Définition des attributs personnalisés
{% tabs %}
{% tab %}
```csharp
Braze.getInstance(context).CurrentUser.SetFirstName("FirstName");
```

Consultez les [instructions d’intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) pour une explication approfondie des bonnes pratiques de suivi des attributs et des interfaces.
{% endtab %}
{% tab iOS %}

```csharp
// C#
Appboy.SharedInstance ().User.FirstName = "YOUR_NAME";
```

**Exemple d’implémentation** : Vous pouvez voir les propriétés utilisateur définies dans la méthode `UserPropertyButtonHandler` de l’exemple d’application dans `AppboySampleViewController.cs`.

Consultez les [instructions d’intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) pour une explication approfondie des bonnes pratiques de suivi des attributs et des interfaces.
{% endtab %}
{% endtabs %}

## Suivi de localisation

- Android : Consultez les [instructions d’intégration Android][2] pour plus d’informations sur la manière de prendre en charge le suivi des localisations.
- iOS : Consultez le [guide d’utilisation de l’emplacement en arrière-plan][11] de Xamarin et les [instructions d’intégration iOS][12] pour plus d’informations sur la manière de prendre en charge le suivi des localisations.
```

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/#location-tracking
[11]: http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/locations_and_geofences/
