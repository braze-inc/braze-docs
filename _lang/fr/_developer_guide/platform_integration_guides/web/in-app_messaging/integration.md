---
nav_title: Intégration
article_title: Intégration de message in-app pour le Web
platform: Web
channel: messages In-App
page_order: 0
page_type: reference
description: "Cet article comprend des ressources sur les types de message in-app et le comportement des messages pour votre application Web."
search_rank: 2
---

# Intégration de message in-app

> Cet article explique comment configurer des messages in-app pour l’application Web.

Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à proposer du contenu à vos utilisateurs sans interrompre leur journée avec une notification push. Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Avec plusieurs mises en page et outils de personnalisation, les messages in-app impliquent plus que jamais vos utilisateurs.

Pour voir des exemples de messages in-app, consultez nos [études de cas][53].

## Types de messages in-app

Braze propose actuellement les types de messages in-app par défaut suivants : 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

Chaque type de message in-app est personnalisable sur le contenu, les images, les icônes, les boutons d’action, l’analytique, l’affichage et la livraison.

Tous les messages in-app intégrés héritent leur prototype de [`InAppMessage`][2] qui définit le comportement et les traits de base pour tous les messages in-app. Les sous-classes de prototypes sont [`SlideUpMessage`][3], [`ModalMessage`][6], [`FullScreenMessage`][7] et [`HtmlMessage`][12].

## Comportements attendus par type de message

Voilà à quoi ressemble l’ouverture de nos types de messages in-app par défaut pour vos utilisateurs.

{% tabs %}
{% tab Slideup %}

Les messages in-app [`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) sont ainsi nommés car, traditionnellement, sur les plateformes mobiles, ils « glissent vers le haut » ou « glissent vers le bas » depuis le haut ou le bas de l’écran. Dans le SDK Braze de Web, ces messages sont affichés comme une notification de style Growl ou Toast pour s’aligner sur le paradigme dominant du Web. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

![Un message in-app surgissant du bas d’un écran de téléphone et affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, se trouve le même le message in-app que celui affiché dans l’angle inférieur d’une page Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) Les messages in-app apparaissent au centre de l’écran et sont encadrés par un panneau transparent. Utiles pour les messages plus critiques, ils peuvent être pourvus de deux actions à clic et de boutons d’analyse.

![Un message in-app modal au centre d’un écran de téléphone affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché au centre d’une page Web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}

Les messages in-app [`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) sont utiles pour maximiser le contenu et l’impact de votre communication utilisateur. Sur les fenêtres de navigateur étroites (par ex., le Web mobile), `full` les messages in-app prennent la totalité de la fenêtre du navigateur. Sur les fenêtres de navigateur plus grandes, les messages in-app `full` apparaissent de la même manière que les messages in-app `modal`. La moitié supérieure d’un message in-app `full` contient une image, et la moitié inférieure autorise jusqu’à huit lignes de texte ainsi que jusqu’à deux boutons d’action permettant l’analytique

![Un message in-app plein écran s’affiche sur l’ensemble de l’écran du téléphone et affiche : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le message in-app est affiché en grand au centre d’une page Web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Custom HTML %}

Les messages in-app [`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le HTML défini par l’utilisateur est affiché dans un iframe et peut contenir du contenu enrichi, comme des images, des polices, des vidéos et des éléments interactifs, permettant un contrôle total de l’apparence et de la fonctionnalité du message. Ils prennent en charge une interface JavaScript `appboyBridge` pour appeler des méthodes SDK Braze pour le Web depuis votre HTML. Consultez nos [meilleures pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) pour plus de détails.

{% alert important %}

Pour activer les messages in-app HTML via le SDK pour le Web, vous **devez** fournir l’option d’initialisation `allowUserSuppliedJavascript` à Braze, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages In-App HTML peuvent en effet exécuter JavaScript, d’où le besoin d’un responsable de site pour les activer.

{% endalert %}

L’exemple suivant montre un message in-app HTML paginé :

![Un message in-app HTML avec un carrousel de contenus et des boutons interactifs.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## Intégration

Par défaut, les messages in-app sont automatiquement affichés dans le cadre des [instructions d’intégration][1] que nous recommandons. Une personnalisation supplémentaire peut être effectuée en suivant les étapes de ce guide.

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html
[6]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html
[7]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html
[12]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[42]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#html-in-app-messages
[53]: https://www.braze.com/customers
