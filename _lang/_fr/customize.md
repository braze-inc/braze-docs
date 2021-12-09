---
nav_title: Customize
article_title: Customize
page_order: 2
layout: featured
guide_top_header: "Customize Your Content Cards"
guide_top_text: "Customizing Content Cards and the feed they'll sit in cannot be done during the campaign creation process - you must work with your engineers and developers to build and customize your cards. It's easy and completely customizable this way!"
description: "Customizing Content Cards and the feed they'll sit in must be done with your engineers and developers. This article will cover where this information can be found in the Braze docs."
guide_featured_title: "Customize Content Cards for..."
guide_featured_list:
  - 
    name: Android
    link: /docs/developer_guide/platform_integration_guides/android/content_cards/customization/
    fa_icon: fab fa-android
  - 
    name: iOS
    link: /docs/developer_guide/platform_integration_guides/ios/content_cards/customization/
    fa_icon: fab fa-apple
  - 
    name: Web
    link: /docs/developer_guide/platform_integration_guides/web/content_cards/customization/
    fa_icon: fas fa-globe
channel:
  - content cards
---

<br>

## Change "empty feed" language

You can change the language that appears automatically in empty Content Card feeds by [redefining the localizable content card strings](https://github.com/Appboy/appboy-ios-sdk/blob/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources/en.lproj/AppboyContentCardsLocalizable.strings) in your app’s localizable strings file:
```
"Appboy.content-cards.no-card.text" = "No Cards!!!!";
"Appboy.content-cards.done-button.title" = "Done";
"Appboy.content-cards.no-card.text" = "We have no updates.\nPlease check again later.";
"Appboy.content-cards.no-connection.title" = "Connection Error";
"Appboy.content-cards.no-connection.message" = "Cannot establish network connection.\nPlease try again later.";
```
{% alert note %}
If you want to update it for different languages, find the corresponding language in [the Resources folder structure](https://github.com/Appboy/appboy-ios-sdk/tree/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources) with the same string `Appboy.content-cards.no-card.text`.
{% endalert %}

<br>
