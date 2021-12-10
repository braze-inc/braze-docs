---
nav_title: Analyses
article_title: Analytiques pour Xamarin
platform:
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "Cet article couvre les analytiques iOS, Android et FireOS pour la plate-forme Xamarin."
---

# Analyse Xamarin

## Paramétrage des identifiants d'utilisateur

{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(contexte).ChangeUser("VOTRE_USER_ID");
```

Consultez [les instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) pour une discussion approfondie sur le moment et la façon de définir et de modifier un ID d'utilisateur.

{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance().ChangeUser("YOUR_USER_ID");
```

Consultez [les instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) pour une discussion approfondie sur le moment et la façon de définir et de modifier un ID d'utilisateur.
{% endtab %}
{% endtabs %}

## Suivi des événements personnalisés
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(contexte).LogCustomEvent("VOTRE_EVENT_NAME");
```

Consultez [les instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) pour une discussion approfondie sur le suivi des meilleures pratiques et interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogCustomEvent ("VOTRE_EVENT_NAME");
```

**Exemple d'implémentation** - `logCustomEvent` est utilisé dans l'application `AppboySampleViewController.cs` dans l'application [exemple TestApp.XamariniOS](https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS).

Consultez [les instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) pour une discussion approfondie sur le suivi des meilleures pratiques et interfaces.
{% endtab %}
{% endtabs %}

## Achats de journalisation
{% tabs %}
{% tab Android %}
```csharp
format@@0 Braze.getInstance(context).LogPurchase("YOUR_PURCHASE_NAME", 100);
```

Consultez [les instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases=) pour une discussion approfondie sur le suivi des revenus des meilleures pratiques et des interfaces.
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogPurchase ("myProduct", "USD", new NSDecimalNumber("10"));
```

**Exemple d'implémentation** - Vous pouvez voir les propriétés de l'utilisateur être définies dans l'échantillon de l'application `EventsAndPurchasesButtonHandler` méthode dans `AppboySampleViewController.cs`.

Consultez [les instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) pour une discussion approfondie sur le suivi des revenus des meilleures pratiques et des interfaces.
{% endtab %}
{% endtabs %}

## Paramétrage des attributs personnalisés
{% tabs %}
{% tab %}
```csharp
Braze.getInstance(contexte).CurrentUser.SetFirstName("Prénom");
```

Consultez [les instructions d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) pour une discussion approfondie sur le suivi des meilleures pratiques et interfaces.
{% endtab %}
{% tab iOS %}

```csharp
// C#
Appboy.SharedInstance ().User.FirstName = "VOTRE_NOM";
```

**Exemple d'implémentation** - Vous pouvez voir les propriétés de l'utilisateur être définies dans la méthode `UserPropertyButtonHandler` de l'application exemple dans `AppboySampleViewController.cs`.

Consultez [les instructions d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) pour une discussion approfondie sur le suivi des meilleures pratiques et interfaces.
{% endtab %}
{% endtabs %}

## Suivi de localisation

- Android: Voir [les instructions d'intégration Android][2] pour plus d'informations sur la façon de prendre en charge le suivi de l'emplacement.
- iOS: Voir [Xamarin Walkthrough - Utilisation de l'emplacement d'arrière-plan][11] et [les instructions d'intégration iOS][12] pour plus d'informations sur la façon de prendre en charge le suivi de l'emplacement.

## Suivi des données sociales (Android uniquement)

Vous pouvez voir la liaison Xamarin accéder à ces interfaces dans le `HomeFragment.cs` de notre exemple d'application.  L'exemple de code enregistre un partage social et remplit l'utilisateur de Braze avec les données des réseaux sociaux.

```csharp
// Enregistrer les données de Facebook
FacebookUser = new FacebookUser("708379", "Test", "User", "test@braze.com", "Test", "Test", "Testtown", "Gender.Male, new Java.Lang.Integer(100), new String[]{"Cats", "Dogs"}, "06/17/1987");
Braze.getInstance(context).CurrentUser. etFacebookData(facebookUser);

// Record Twitter Data
TwitterUser twitterUser = new TwitterUser(6253282, "Test", "User", "User", "Tester", new Java.Lang.Integer(100), new Java.Lang.Integer(100), new Java.Lang.Integer(100), "https://si0.twimg.com/profile_images/2685532587/fa47382ad67a0135acc62d4c6b49dbdc_bigger.jpeg");
Braze.getInstance(context).CurrentUser.SetTwitterData(twitterUser);
```
Consultez [les instructions d'intégration Android][6] pour une discussion approfondie sur les meilleures pratiques et les interfaces des données sociales.

[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/social_data_tracking/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/#location-tracking
[11]: http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/locations_and_geofences/