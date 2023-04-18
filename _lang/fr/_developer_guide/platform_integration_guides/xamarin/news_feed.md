---
nav_title: Fil d’actualité
article_title: Fil d’actualité pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 3
description: "Cet article couvre l’intégration de fils d’actualité sur iOS, Android et FireOS pour la plate-forme Xamarin."
channel: fil d’actualité 
---

# Intégration du fil d’actualité

> Cet article explique comment configurer un fil d’actualité iOS, Android et FireOS pour la plateforme Xamarin.

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

## Android

Consultez les [instructions d’intégration Android][1] pour une savoir comment intégrer le fil d’actualité dans votre application Xamarin sur Android.  En outre, vous pouvez consulter [l’exemple d’application][2] pour des échantillons d’implémentation.

## iOS 

Consultez les [instructions d’intégration iOS][11] pour savoir comment intégrer le fil d’actualité dans votre application Xamarin sur iOS.  En outre, vous pouvez consulter [l’exemple d’application][12] pour des échantillons d’implémentation.

Parmi toutes les options d’implémentation, le plus rapide à mettre en œuvre est le Modal, qui peut être ajouté en procédant comme suit dans votre ViewController :

```csharp
// C#
ABKFeedViewControllerModalContext m = new ABKFeedViewControllerModalContext ();
this.PresentViewController (m, true, null);
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed
[2]: https://github.com/braze-inc/braze-xamarin-sdk
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[12]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples
