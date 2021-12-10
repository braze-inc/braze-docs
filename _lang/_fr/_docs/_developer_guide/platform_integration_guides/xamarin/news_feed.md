---
nav_title: Flux d'actualité
article_title: Flux d'actualité pour Xamarin
platform:
  - Xamarin
  - iOS
  - Android
page_order: 3
description: "Cet article couvre l'intégration des flux RSS pour iOS, Android et FireOS pour la plate-forme Xamarin."
channel: fil d'actualité
---

# Flux d'actualité

## Android

Consultez [les instructions d'intégration Android][1] pour plus d'informations sur la façon d'intégrer le flux d'actualités dans votre application Xamarin Android.  De plus, vous pouvez regarder les exemples d'implémentation de l'application [][2].

## iOS

Consultez [les instructions d'intégration iOS][11] pour plus d'informations sur la façon d'intégrer le flux d'actualités dans votre application Xamarin iOS.  De plus, vous pouvez regarder les exemples d'implémentation \[exemple d'application\]\[12\].

Parmi toutes les options d'implémentation, le plus rapide à implémenter est le Modal, qui peut être ajouté en faisant ce qui suit dans votre contrôleur de vue:

```csharp
// C#
ABKFeedViewControllerModalContext m = new ABKFeedViewControllerModalContext ();
this.PresentViewController (m, true, null);
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed
[2]: https://github.com/Appboy/appboy-xamarin-bindings
[2]: https://github.com/Appboy/appboy-xamarin-bindings
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
