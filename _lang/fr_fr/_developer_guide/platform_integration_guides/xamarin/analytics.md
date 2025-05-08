---
nav_title: Analyse
article_title: Analyses pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "Cet article couvre l’analyse iOS, Android et FireOS pour la plateforme Xamarin."

---
 
# Analyses Xamarin

> Découvrez comment générer et examiner des analyses pour la plateforme Xamarin.

## Suivi d’une session

Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à une meilleure connaissance de vos utilisateurs. Sur la base de la sémantique de session suivante, notre SDK génère des points de données « démarrage de la session » et « fin de la session » qui comptent pour la longueur de session et le nombre de sessions visibles dans le tableau de bord de Braze.

Pour définir un ID utilisateur ou démarrer une session, utilisez la méthode `ChangeUser`, qui utilise un paramètre d’ID utilisateur.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).ChangeUser("user_id");
```

Consultez les [instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) pour une discussion approfondie sur quand et comment définir et modifier un ID utilisateur.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.ChangeUser("user_id");
```

Consultez les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) pour une discussion approfondie sur quand et comment définir et modifier un ID utilisateur.

{% endtab %}
{% endtabs %}

## Journalisation des événements personnalisés

Vous pouvez enregistrer des événements personnalisés dans Braze à l'aide de `LogCustomEvent` pour en savoir plus sur les habitudes d'utilisation de votre appli et pour segmenter vos utilisateurs en fonction de leurs actions dans le tableau de bord.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogCustomEvent("event_name");
```

Consultez les [instructions relatives à l'intégration d'Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des événements.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogCustomEvent("event_name");
```

Consultez les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des événements.

{% endtab %}
{% endtabs %}

## Enregistrer les achats

Enregistrez les achats in-app à l'aide de `LogPurchase` pour suivre vos chiffres d'affaires dans le temps et selon les sources de revenus, ainsi que pour segmenter vos utilisateurs en fonction de leur valeur vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

Consultez les [instructions relatives à l'intégration d'Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des chiffres d'affaires.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

Consultez les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) pour une discussion approfondie sur les meilleures pratiques et les interfaces de suivi des chiffres d'affaires.

{% endtab %}
{% endtabs %}

### Journaliser les achats au niveau de la commande

Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Clés réservées

Les clés suivantes sont réservées et **ne peuvent pas** être utilisées comme propriétés d'achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Enregistrer des attributs personnalisés

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

### Attributs par défaut de l’utilisateur

Pour assigner automatiquement des attributs d’utilisateur collectés par Braze, vous pouvez utiliser des méthodes d’initiateurs fournies avec le SDK. Par exemple, vous pouvez définir le prénom de l'utilisateur :

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

Les attributs suivants sont pris en charge :

- Prénom
- Nom
- Genre
- Date de naissance
- Ville d’origine
- Pays
- Numéro de téléphone
- E-mail

### Attributs utilisateur personnalisés

Outre nos méthodes prédéfinies d'attribut utilisateur, Braze propose également des attributs personnalisés utilisant `SetCustomUserAttribute` pour suivre les données de vos applications.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

Consultez les [instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) pour une discussion approfondie sur les meilleures pratiques et les interfaces de suivi des attributs.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

Consultez les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) pour une discussion approfondie sur les meilleures pratiques et interfaces de suivi des attributs.

{% endtab %}
{% endtabs %}

## Suivi de localisation

Pour un exemple de journalisation et de suivi des analyses, reportez-vous à nos exemples d'applications [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/MainActivity.cs) et [iOS MAUI.](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/MainPage.xaml.cs) 

{% tabs %}
{% tab android %}
Pour plus d'informations, consultez les [instructions relatives à l'intégration d'Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/).
{% endtab %}

{% tab ios %}
Pour prendre en charge le suivi local, consultez [iOS : Utilisation de l'emplacement/localisation en arrière-plan](http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/) et les [instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/).
{% endtab %}
{% endtabs %}

