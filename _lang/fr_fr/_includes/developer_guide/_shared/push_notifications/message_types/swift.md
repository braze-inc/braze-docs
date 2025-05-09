{% tab swift %}
Chaque type de message in-app est hautement personnalisable en termes de contenu, d’images, d’icônes, d’actions de clic, d’analyse, d’affichage et de diffusion. Il s'agit de types énumérés de `Braze.InAppMessage`, qui définit le comportement et les caractéristiques de base de tous les messages in-app. Pour obtenir la liste complète des propriétés et de l'utilisation des messages in-app, consultez la [classe`InAppMessage` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Voici les types de messages in-app disponibles dans Braze et ce à quoi ils ressembleront pour les utilisateurs finaux.

{% subtabs %}
{% subtab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) Les messages in-app portent ce nom parce qu'ils "glissent vers le haut" ou "glissent vers le bas" depuis le haut ou le bas de l'écran. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

![Un message in-app contextuel en bas et en haut de l'écran d'un téléphone.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

Les messages in-app de type [`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) apparaissent au centre de l'écran et sont encadrés par un panneau transparent. Utiles pour les communications plus critiques, ils peuvent être équipés d'un maximum de deux boutons dotés d'une fonction d'analyse.

![Un message in-app modal au centre de l'écran d'un téléphone.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

Les messages in-app de type [`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) apparaissent au centre de l'écran et sont encadrés par un panneau transparent. Ces messages sont similaires au type `Modal`, mais sans en-tête ni texte de message. Utiles pour les communications plus critiques, ils peuvent être équipés d'un maximum de deux boutons dotés d'une fonction d'analyse.

![Un message in-app dans une image modale au centre de l'écran d'un téléphone.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) Les messages in-app sont utiles pour maximiser le contenu et l'impact de votre communication avec les utilisateurs. La moitié supérieure d'un message in-app `Full` contient une image, et la moitié inférieure affiche du texte et jusqu'à deux boutons permettant l'analyse.

![Un message in-app en plein écran qui s'affiche sur tout l'écran du téléphone.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

[Les messages in-app `Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) sont similaires aux messages in-app `Full`, sauf qu'ils ne comportent pas d'en-tête ni de texte de message. Ce type de message est utile pour maximiser le contenu et l'impact de votre communication avec les utilisateurs. Un message in-app `Full Image` contient une image qui s'étend sur tout l'écran, avec la possibilité d'afficher jusqu'à deux boutons compatibles avec l'analyse.

![Un message in-app en image plein écran qui s'affiche sur tout l'écran d’un téléphone.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

Les messages in-app [`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu des messages in-app entièrement en HTML défini par l’utilisateur est affiché dans un `WKWebView` et peut éventuellement contenir d’autres contenus enrichis, tels que des images et des polices, permettant un contrôle total de l’apparence et de la fonctionnalité du message. <br><br>Les messages in-app IOS prennent en charge une interface JavaScript `brazeBridge` pour appeler des méthodes sur le SDK Braze pour le Web depuis votre HTML. Pour plus d’informations, consultez nos [meilleures pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

L’exemple suivant montre la mise en page d’un message in-app HTML complet :

![Un message in-app en HTML avec un carrousel de contenu et des boutons interactifs.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Notez que nous ne prenons actuellement pas en charge l’affichage de messages in-app HTML personnalisés dans un iFrame sur les plateformes iOS et Android.

{% endsubtab %}
{% subtab Control %}

[Les messages in-app `Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) ne contiennent pas de composant d'interface utilisateur et sont utilisés principalement à des fins d'analyse. Ce type est utilisé pour vérifier la réception d'un message in-app envoyé à un groupe de contrôle.

Pour plus de détails sur la sélection intelligente et les groupes de contrôle, reportez-vous à la section [Sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
