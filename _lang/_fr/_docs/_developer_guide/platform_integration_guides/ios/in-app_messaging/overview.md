---
nav_title: Aperçu
article_title: Aperçu des messages dans l'application pour iOS
platform: iOS
page_order: 0
description: "Cet article couvre la messagerie iOS dans l'application, quand au mieux l'utiliser, en plus de plusieurs cas d'utilisation exceptionnels."
channel:
  - messages intégrés à l'application
---

# Messages dans l'application

Les [Messages In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à obtenir du contenu à votre utilisateur sans interrompre sa journée avec une notification push. Des messages personnalisés et personnalisés dans l'application améliorent l'expérience utilisateur et aident votre public à tirer le meilleur parti de votre application. Avec une variété de mises en page et d'outils de personnalisation à choisir, les messages intégrés attirent plus que jamais vos utilisateurs.

Pour voir des exemples de messages dans l'application, consultez notre [Études de cas][31].

## Types de messages dans l'application

Braze propose actuellement les types de messages par défaut suivants dans l'application:

- `Glissement vers le haut`
- `Modal`
- `Plein`
- `HTML plein`

Chaque type de message intégré est hautement personnalisable entre le contenu, les images, les icônes, les actions de clic, les analytiques, l'affichage et la livraison.

Tous les messages dans l'application sont des sous-classes du `ABKInAppMessage`, qui définit le comportement de base et les traits pour tous les messages dans l'application. Les structures de classe de messages dans l'application comme suit:

!\[Modèles ABKInAppMessage\]\[29\]

{% alert important %}
Par défaut, les messages dans l'application sont activés après avoir terminé l'intégration standard du SDK, y compris la prise en charge du GIF. <br><br> __Notez que l'intégration de `SDWebImage` est nécessaire si vous prévoyez d'utiliser notre interface utilisateur Braze pour afficher des images__ dans les messages In-App iOS, Flux d'actualités ou Cartes de contenu.
{% endalert %}

### Comportements attendus par type de message

Voici ce à quoi il semble que vos utilisateurs ouvrent un de nos types de messages dans l'application.

{% tabs %}
  {% tab Slideup %}

  [`Glisser vers le haut`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) Les messages dans l'application sont nommés parce qu'ils "glissent vers le haut" ou "glisser" vers le bas depuis le haut ou le bas de l'écran.  Elles couvrent une petite partie de l'écran et offrent une capacité de messagerie efficace et non intrusive.

  <br>

  ![Comportement de glissement]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

  <br>

{% endtab %}
{% tab Modal %}

[`Les messages modaux`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) dans l'application apparaissent au centre de l'écran et sont encadrés par un panneau translucide. Utile pour des messages plus critiques, ils peuvent être équipés de deux boutons permettant de cliquer sur l'action et l'analyse.

 <br>

  ![Comportement modal]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

 <br>

{% endtab %}
{% tab Full Screen %}

[`Complète`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) les messages intégrés à l'application sont utiles pour maximiser le contenu et l'impact de votre communication utilisateur.  La moitié supérieure d'un message de `plein` dans l'application contient une image et la moitié inférieure affiche du texte ainsi que jusqu'à deux boutons activés par les clics d'action et d'analyse.

<br>

![Comportement plein écran]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Custom HTML %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) les messages dans l'application sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu du message HTML complet dans l'application défini par l'utilisateur est affiché dans un `WKWebView`et peut éventuellement contenir un autre contenu riche, comme les images et les polices, permettant un contrôle total de l'apparence et de la fonctionnalité du message. <br><br>Les messages dans l'application iOS prennent en charge une interface JavaScript `appboyBridge` pour appeler des méthodes sur le Braze Web SDK à partir de l'intérieur de votre HTML, voir <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/best_practices//">Meilleures pratiques</a> pour plus de détails.

L'exemple suivant montre un message HTML complet dans l'application paginé :

![HTML5 IAM Example]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

> Le contenu du message complet intégré à l'application est affiché dans un WKWebView et peut éventuellement contenir d'autres contenus riches, comme les images et les polices, permettant un contrôle total de l'apparence et de la fonctionnalité du message. **Veuillez noter que nous ne prenons actuellement pas en charge l'affichage de messages personnalisés dans l'application HTML dans un iFrame sur les plateformes iOS et Android.**

> **Démarrage dans iOS SDK version 3.19. , les méthodes JavaScript suivantes ne sont pas opérées dans les messages HTML dans l'application: `alerte`, `confirmez`, `invite`.**

{% endtab %}
{% endtabs %}
[29]: {% image_buster /assets/img_archive/ABKInAppMessage-models.png %}

[31]: https://www.braze.com/customers
