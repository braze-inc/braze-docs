
{% tab android %}
Braze propose plusieurs types de messages in-app par défaut, chacun pouvant être personnalisé avec des messages, des images, des icônes [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2), des actions cliquables, des analyses, des palettes de couleurs, et bien plus encore.

Leur comportement et leurs caractéristiques de base sont définis par [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html)l'interface, dans une sous-classe appelée [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).`IInAppMessage`Elle comprend également une sous-interface, [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html), qui vous permet d'ajouter [des boutons](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) de fermeture, d'action par clic et d'analyse/analytique à votre application.

{% alert important %}
Veuillez noter que les messages in-app contenant des boutons incluront le`clickAction`message dans la charge utile finale si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) Les messages in-app sont ainsi nommés parce qu'ils "glissent vers le haut" ou "glissent vers le bas" depuis le haut ou le bas de l'écran. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

L'objet de message in-app `slideup` étend [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).

![Un message in-app surgissant du bas d’un écran de téléphone et affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app s'affiche dans le coin inférieur droit d'une page Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
Les messages in-app de type [`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) apparaissent au centre de l'écran et sont encadrés par un panneau transparent. Ils sont utiles pour les messages plus critiques et peuvent être équipés d'un bouton d’action et d'un bouton activé par analyse.

Ce type de message est une sous-classe de [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html), une classe abstraite qui implémente `IInAppMessageImmersive`, vous permettant d'ajouter des fonctionnalités personnalisées à vos messages in-app générés localement.

![Un message in-app modal au centre d’un écran de téléphone affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché au centre d'une page Web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) Les messages in-app sont utiles pour maximiser le contenu et l'impact de votre communication avec les utilisateurs. La moitié supérieure d’un `full` message in-app contient une image, et la moitié inférieure affiche le texte et deux boutons d’action permettant l’analyse.

Ce type de message étend [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html), vous offrant la possibilité d'ajouter des fonctionnalités personnalisées à vos messages in-app générés localement.

![Un message in-app plein écran s’affiche sur l’ensemble de l’écran du téléphone et affiche : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le message in-app est affiché en grand au centre d’une page Web.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
Les messages in-app [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu du message in-app en HTML défini par l’utilisateur est affiché dans un `WebView` et peut éventuellement contenir d’autres contenus enrichis, tels que des images et des polices, permettant un contrôle total de l’apparence et de la fonctionnalité du message.

Ce type de message implémente [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html), qui est une sous-classe de [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html).

{% alert note %}
Sur Android, les liens configurés avec`target="_blank"`  dans les messages in-app personnalisés s'ouvrent dans le navigateur web par défaut de l'appareil.
{% endalert %}

Les messages in-app pour l'application Android prennent en charge une interface `brazeBridge`JavaScript permettant d'appeler des méthodes sur le SDK Android Braze à partir de votre code HTML. Veuillez consulter notre page <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">sur le pont JavaScript</a> pour plus de détails.

![Message in-app HTML avec un carrousel de contenu et des boutons interactifs.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Actuellement, nous ne prenons pas en charge l’affichage de messages in-app HTML personnalisés dans un iFrame sur les plateformes iOS et Android.
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Vous pouvez également définir des affichages personnalisés pour les messages in-app de votre application. Pour obtenir des instructions détaillées, veuillez consulter [la section Configuration des fabriques personnalisées]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories).
{% endalert %}
{% endtab %}