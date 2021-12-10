---
nav_title: Aperçu
article_title: Aperçu des messages dans l'application pour le Web
platform: Web
channel: messages intégrés à l'application
page_order: 0
page_type: Référence
description: "Cet article de référence fournit une vue d'ensemble des messages dans l'application, y compris les meilleures pratiques et les cas d'utilisation."
---

# Messages dans l'application

Les [Messages In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à obtenir du contenu à votre utilisateur sans interrompre sa journée avec une notification push. Des messages personnalisés et personnalisés dans l'application améliorent l'expérience utilisateur et aident votre public à tirer le meilleur parti de votre application. Avec une variété de mises en page et d'outils de personnalisation à choisir, les messages intégrés attirent plus que jamais vos utilisateurs.

Pour voir des exemples de messages dans l'application, consultez notre [Études de cas][53].

## Types de messages dans l'application

Braze propose actuellement les types de messages par défaut suivants dans l'application:

- [`Glissement vers le haut`][13]
- [`Modal`][17]
- [`Plein`][41]
- [`HTML`][42]

Chaque type de message intégré est personnalisable selon le contenu, les images, les icônes, les actions de clic, les analytiques, l'affichage et la livraison.

Tous les messages dans l'application héritent de leur prototype de [`appboy.InAppMessage`][2], qui définit le comportement de base et les traits pour tous les messages dans l'application. Les sous-classes protypiques sont [appboy.SlideUpMessage][3], [appboy.ModalMessage][6], [appboy.FullScreenMessage][7], et [appboy.HtmlMessage][12].

## Comportements attendus par type de message

Voici ce à quoi il semble que vos utilisateurs ouvrent un de nos types de messages dans l'application.

{% tabs %}
  {% tab Slideup %}

  [`Glisser vers le haut`](https://js.appboycdn.com/web-sdk/latest/doc/ab.SlideUpMessage.html) les messages dans l'application sont nommés car traditionnellement sur les plates-formes mobiles, ils "glisser" vers le haut ou le bas de l'écran. Dans le Braze Web SDK, ces messages sont affichés comme plus d'une notification de style Growl ou Toast, pour s'aligner avec le paradigme dominant du Web. Elles couvrent une petite partie de l'écran et offrent une capacité de messagerie efficace et non intrusive.

  <br>

  ![Comportement de glissement]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Modal %}

[`Les messages modaux`](https://js.appboycdn.com/web-sdk/latest/doc/ab.ModalMessage.html) dans l'application apparaissent au centre de l'écran et sont encadrés par un panneau translucide. Utile pour des messages plus critiques, ils peuvent être équipés de deux boutons permettant de cliquer sur l'action et l'analyse.

  <br>

  ![Comportement modal]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Full Screen %}

[`Complète`](https://js.appboycdn.com/web-sdk/latest/doc/ab.FullScreenMessage.html) les messages intégrés à l'application sont utiles pour maximiser le contenu et l'impact de votre communication utilisateur. Sur les fenêtres de navigateur étroites (par exemple le Web mobile), `les messages complets` dans l'application prennent toute la fenêtre du navigateur. Sur de plus grandes fenêtres de navigateur, `les messages complets` dans l'application apparaissent de la même façon que les messages `modaux` dans l'application. La moitié supérieure d'un message `complet` dans l'application contient une image et la moitié inférieure permet jusqu'à huit lignes de texte ainsi que jusqu'à deux boutons activés par les clics et les analytiques

<br>

![Comportement plein écran]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Custom HTML %}

[`Les messages HTML`](https://js.appboycdn.com/web-sdk/latest/doc/ab.HtmlMessage.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le code HTML défini par l'utilisateur est affiché dans un iframe et peut contenir un contenu riche, comme les images, les polices, vidéo et éléments interactifs, permettant un contrôle total de l'apparence et de la fonctionnalité du message. Ceux-ci prennent en charge une interface JavaScript `appboyBridge` pour appeler des méthodes sur le Braze Web SDK à partir de votre HTML, voir [les meilleures pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) pour plus de détails.

{% alert important %}

Pour activer les messages HTML dans l'application, votre intégration SDK __doit__ fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, . `appboy.initialize('VOTRE API_COUR', {allowUserSuppliedJavascript: true})`. Ceci est pour des raisons de sécurité - les messages HTML dans l'application peuvent exécuter JavaScript donc nous avons besoin d'un responsable du site pour les activer. <br> <br> au Brésil, le SDK web traite le modèle de type de message de type "Formulaire de capture de courriel" comme un message HTML dans l'application. donc la même option `allowUserSuppliedJavascript` doit être définie.

{% endalert %}

L'exemple suivant montre un message HTML paginé dans l'application:

![HTML5 IAM Example]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/ab.SlideUpMessage.html
[6]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ModalMessage.html
[7]: https://js.appboycdn.com/web-sdk/latest/doc/ab.FullScreenMessage.html
[12]: https://js.appboycdn.com/web-sdk/latest/doc/ab.HtmlMessage.html
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[42]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#html-in-app-messages
[53]: https://www.braze.com/customers