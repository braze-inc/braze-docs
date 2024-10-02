---
nav_title: Aperçu
article_title: Aperçu du message In-App pour iOS
platform: iOS
page_order: 0
description: "Cet article de référence couvre les types d’envois de messages in-app dans l’application iOS, les comportements attendus et plusieurs cas d’utilisation."
channel:
  - messages In-App
search_rank: 4
---

{% multi_lang_include deprecations/objective-c.md %}

# Messages in-app

Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à obtenir du contenu à votre utilisateur sans interrompre votre journée avec une notification push. Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Grâce à un choix de mises en page et d’outils de personnalisation, les messages In-App supposent un engagement inédit de vos utilisateurs.

Pour voir des exemples de messages in-app, consultez nos [études de cas][31].

## Types de messages in-app

Braze propose actuellement les types de messages in-app par défaut suivants : 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

Chaque type de message in-app est hautement personnalisable en termes de contenu, d’images, d’icônes, d’actions de clic, d’analyse, d’affichage et de diffusion.

Tous les messages in-app sont des sous-classes de `ABKInAppMessage`, qui définit le comportement et les caractéristiques de base pour tous les messages in-app. Les structures de classe de message in-app sont les suivantes :

![Un graphique montrant que la classe ABKinAppMessage est la classe racine des ABKinAppMessageSlideup, ABKInAppMessageImmersive et ABKinAppMessageHTML. L’ABKinAppMessage inclut des propriétés personnalisables comme le message, les extras, la durée, l’action de clic, l’URI, l’action de rejet, l’orientation des icônes et l’alignement du texte. L’ABKinAppMessagEslideup comprend des propriétés personnalisables comme le chevron et l’ancre coulissante. L’immersionABKinAppMessageImmersif inclut des propriétés personnalisables comme l’en-tête, le bouton de fermeture, le cadre et les boutons de message in-app. ABKinAppMessageHTML vous permet de consigner manuellement les clics du bouton de message in-app HTML.][29]

{% alert important %}
Par défaut, les messages in-app sont activés après avoir terminé l’intégration SDK standard, y compris la prise en charge GIF. 
<br><br>
Notez que l’intégration de `SDWebImage` est requise si vous prévoyez d’utiliser notre interface utilisateur Braze pour afficher des images dans les messages in-app iOS ou les cartes de contenu.
{% endalert %}

### Comportements attendus par types de messages

Voilà à quoi ressemble l’ouverture de nos types de messages in-app par défaut pour vos utilisateurs.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) Les messages in-app sont ainsi nommés, car ils « surgissent » du haut ou du bas de l’écran. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

![Un message in-app surgissant du bas d’un écran de téléphone et affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, se trouve le même le message in-app que celui affiché dans l’angle inférieur d’une page Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) Les messages in-app apparaissent au centre de l’écran et sont encadrés par un panneau transparent. Utiles pour les messages plus critiques, ils peuvent être pourvus de deux actions à clic et de boutons d’analyse.

![Un message in-app modal au centre d’un écran de téléphone affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché au centre d’une page Web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}

Les messages in-app [`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) sont utiles pour maximiser le contenu et l’impact de votre communication utilisateur. La moitié supérieure d’un `full` message in-app contient une image, et la moitié inférieure affiche le texte et deux boutons d’action permettant l’analyse.

![Un message in-app plein écran s’affiche sur l’ensemble de l’écran du téléphone et affiche : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le message in-app est affiché en grand au centre d’une page Web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Custom HTML %}

Les messages in-app [`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu des messages in-app entièrement en HTML défini par l’utilisateur est affiché dans un `WKWebView` et peut éventuellement contenir d’autres contenus enrichis, tels que des images et des polices, permettant un contrôle total de l’apparence et de la fonctionnalité du message. <br><br>Les messages in-app IOS prennent en charge une interface JavaScript `appboyBridge` pour appeler des méthodes SDK Braze pour le Web depuis votre HTML. Consultez nos [meilleures pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) pour plus de détails.

L’exemple suivant montre la mise en page d’un message in-app HTML complet :

![Un message in-app HTML avec un ensemble de contenus et des boutons interactifs.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Le contenu complet du message in-app est affiché dans un `WKWebView` et peut éventuellement contenir d’autres contenus enrichis, comme des images et des polices, permettant un contrôle total de l’apparence et des fonctionnalités du message. Notez que nous ne prenons actuellement pas en charge l’affichage de messages in-app HTML personnalisés dans un iFrame sur les plateformes iOS et Android.

{% alert note %}
À partir de la version 3.19.0 de SDK iOS, les méthodes JavaScript suivantes ne sont pas opérationnelles dans les messages in-app HTML : `alert`, `confirm`, `prompt`.
{% endalert %}

{% endtab %}
{% endtabs %}

[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}
[30]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[31]: https://www.braze.com/customers
