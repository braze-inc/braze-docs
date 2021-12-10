---
nav_title: Aperçu
article_title: Aperçu des messages dans l'application pour Android/FireOS
page_order: 0
platform:
  - Android
  - Pare-feu
description: "Cet article couvre la messagerie Android dans l'application, quand au mieux l'utiliser, en plus de plusieurs cas d'utilisation."
channel:
  - messages intégrés à l'application
---

# Messages dans l'application

Les [Messages In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à obtenir du contenu à votre utilisateur sans interrompre sa journée avec une notification push. Des messages personnalisés et personnalisés dans l'application améliorent l'expérience utilisateur et aident votre public à tirer le meilleur parti de votre application. Avec une variété de mises en page et d'outils de personnalisation à choisir, les messages intégrés attirent plus que jamais vos utilisateurs.

Pour voir des exemples de messages dans l'application, consultez notre [Études de cas][83].

## Types de messages dans l'application

Braze propose plusieurs types de messages par défaut dans l'application, chacun personnalisable avec des messages, des images, des icônes [Font Awesome][15] , des actions de clic, des analytiques, un style modifiable et des schémas de couleurs. Les types actuellement disponibles sont :

- `Glissement vers le haut`
- `Modal`
- `Plein`
- `HTML plein`

Il est également possible de [définir votre propre vue de message personnalisée dans l'application][12].

Tous les messages intégrés implémentent l'interface [`IInAppMessage`][3] , qui définit le comportement de base et les traits pour tous les messages de l'application. [`InAppMessageBase`][27] est une classe abstraite qui implémente `IInAppMessage` et fournit l'implémentation de message dans l'application fondamentale. Toutes les classes de messages in-app sont des sous-classes de `InAppMessageBase`.

En outre, il y a une sous-interface de `IInAppMessage` appelée [`IInAppMessageImmersive`][8], qui ajoute l'action de clic et les outils d'analyse ont activé [boutons][50], ainsi que le texte d'en-tête et un bouton fermer. [`InAppMessageImmersiveBase`][28] est une classe abstraite qui implémente `IInAppMessageImmersive` et fournit la fondation `immersive` d'implémentation de message dans l'application. `Les messages modaux` et `pleins` dans l'application sont des sous-classes de `InAppMessageImmersiveBase`.

Les messages HTML complets dans l'application sont [`InAppMessageHtmlFull`][51] instances, qui implémentent [`IInAppMessageHtml`][52], une autre sous-classe de `IInAppMessage`.

### Comportements attendus par type de message

Voici ce à quoi ressemblera chaque type de message dans l'application pour vos utilisateurs.

{% tabs %}
  {% tab Slideup %}
  [`Glisser vers le haut`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/InAppMessageSlideup.html) Les messages dans l'application sont nommés parce qu'ils "glissent vers le haut" ou "glisser" vers le bas depuis le haut ou le bas de l'écran.  Elles couvrent une petite partie de l'écran et offrent une capacité de messagerie efficace et non intrusive.

  <br>

  ![Comportement de glissement]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Modal %}
[`Les messages modaux`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/InAppMessageModal.html) dans l'application apparaissent au centre de l'écran et sont encadrés par un panneau translucide. Utile pour des messages plus critiques, ils peuvent être équipés de deux boutons permettant de cliquer sur l'action et l'analyse.

  <br>

  ![Comportement modal]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

  <br>


{% endtab %}
{% tab Full Screen %}
[`Complète`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/InAppMessageFull) les messages intégrés à l'application sont utiles pour maximiser le contenu et l'impact de votre communication utilisateur.  La moitié supérieure d'un message de `plein` dans l'application contient une image et la moitié inférieure affiche du texte ainsi que jusqu'à deux boutons activés par les clics d'action et d'analyse.

![Exemple complet]({% image_buster /assets/img_archive/In-App_Full.png %})


{% endtab %}
{% tab Custom HTML %}
[`Les messages HTML plein`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/InAppMessageHtmlFull.html) dans l'application sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu du message HTML Full in-app défini par l'utilisateur est affiché dans un {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} et peut éventuellement contenir d'autres contenus riches. comme les images et les polices, permettant un contrôle total de l'apparence et de la fonctionnalité du message. <br><br>Les messages dans l'application Android prennent en charge une interface JavaScript `brazeBridge` pour appeler des méthodes sur le Braze Web SDK à partir de l'intérieur de votre HTML, voir <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/best_practices/">Meilleures pratiques</a> pour plus de détails.

<br>

![Comportement plein écran]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

Le contenu du message complet intégré à l'application est affiché dans un `WKWebView` et peut éventuellement contenir d'autres contenus riches, comme les images et les polices, permettant un contrôle total de l'apparence et de la fonctionnalité du message.

{% alert important %}
Veuillez noter que nous ne prenons actuellement pas en charge l'affichage de messages personnalisés dans l'application HTML dans un iFrame sur les plateformes iOS et Android.
{% endalert %}

{% endtab %}
{% endtabs %}

#### En profondeur: définir des types de messages personnalisés dans l'application

Braze `slideup` de l'objet message dans l'application étend [`InAppMessageBase`][27]. Les messages de type `plein` et `modal` de Braze étendent [`InAppMessageImmersiveBase`][28]. L'extension d'une de ces classes vous donne la possibilité d'ajouter des fonctionnalités personnalisées à vos messages locaux dans l'application.

[3]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/IInAppMessage.html
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/IInAppMessageImmersive.html
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-a-custom-view-factory
[15]: http://fortawesome.github.io/Font-Awesome/
[27]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/InAppMessageBase.html
[28]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/InAppMessageImmersiveBase.html
[50]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/MessageButton.html
[51]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/InAppMessageHtmlFull.html
[52]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/models/inappmessage/IInAppMessageHtml.html
[83]: https://www.braze.com/customers
