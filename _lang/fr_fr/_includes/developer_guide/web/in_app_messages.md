{% multi_lang_include developer_guide/prerequisites/web.md %} Cependant, aucune configuration supplémentaire n'est nécessaire.

## Types de messages

Tous les messages in-app héritent de leur prototype de [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)qui définit le comportement de base et les caractéristiques de tous les messages in-app. Les sous-classes prototypiques sont [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html), et [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

Chaque type de message in-app est personnalisable sur le contenu, les images, les icônes, les boutons d’action, l’analyse, l’affichage et la livraison.

{% tabs %}
{% tab Contextuel %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) Les messages in-app sont ainsi nommés parce que traditionnellement, sur les plateformes mobiles, ils "glissent vers le haut" ou "glissent vers le bas" depuis le haut ou le bas de l'écran. Dans le SDK Braze de Web, ces messages sont affichés comme une notification de style Growl ou Toast pour s’aligner sur le paradigme dominant du Web. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

![Un message in-app surgissant du bas d’un écran de téléphone et affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, se trouve le même le message in-app que celui affiché dans l’angle inférieur d’une page Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fenêtre modale %}

Les messages in-app de type [`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) apparaissent au centre de l'écran et sont encadrés par un panneau transparent. Utiles pour les messages plus critiques, ils peuvent être pourvus de deux actions à clic et de boutons d’analyse.

![Un message in-app modal au centre d’un écran de téléphone affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché au centre d'une page Web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Plein écran %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) Les messages in-app sont utiles pour maximiser le contenu et l'impact de votre communication avec les utilisateurs. Dans les fenêtres de navigateur étroites (par exemple, le Web mobile), les messages in-app `full` occupent toute la fenêtre du navigateur. Sur les fenêtres de navigateur plus grandes, les messages in-app `full` apparaissent de la même manière que les messages in-app `modal`. La moitié supérieure d’un message in-app `full` contient une image, et la moitié inférieure autorise jusqu’à huit lignes de texte ainsi que jusqu’à deux boutons d’action permettant l’analyse

![Un message in-app plein écran s’affiche sur l’ensemble de l’écran du téléphone et affiche : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché en grand au centre d’une page Web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personnalisé %}

Les messages in-app [`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le HTML défini par l’utilisateur est affiché dans un iframe et peut contenir du contenu enrichi, comme des images, des polices, des vidéos et des éléments interactifs, permettant un contrôle total de l’apparence et de la fonctionnalité du message. Ceux-ci prennent en charge une interface JavaScript `brazeBridge` pour appeler des méthodes du Braze Web SDK à partir de votre HTML, voir nos [meilleures pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) pour plus de détails.

{% alert important %}
Pour activer les messages in-app HTML via le SDK Web, vous **devez** fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent en effet exécuter JavaScript, d’où le besoin d’un responsable de site pour les activer.
{% endalert %}

L’exemple suivant montre un message in-app HTML paginé :

![Un message in-app en HTML avec un carrousel de contenu et des boutons interactifs.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}
