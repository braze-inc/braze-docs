
{% tab android %}
Braze propose plusieurs types de messages in-app par défaut, chacun personnalisable avec des messages, des images, des icônes [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2), des actions de clic, des analyses, des schémas de couleurs, et plus encore.

Leur comportement de base et leurs caractéristiques sont définis par l'interface [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) dans une sous-classe appelée [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html). `IInAppMessage` comprend également une sous-interface, [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)qui vous permet d'ajouter des [boutons de](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) fermeture, de clic-action et d'analyse/analytique à votre application.

{% alert important %}
N'oubliez pas que les messages in-app contenant des boutons incluront le message `clickAction` dans la charge utile finale si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) Les messages in-app sont ainsi nommés parce qu'ils "glissent vers le haut" ou "glissent vers le bas" depuis le haut ou le bas de l'écran. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

L'objet de message in-app `slideup` étend [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).

![Un message in-app surgissant du bas d’un écran de téléphone et affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché dans l’angle inférieur droit d'une page web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
Les messages in-app de type [`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) apparaissent au centre de l'écran et sont encadrés par un panneau transparent. Ils sont utiles pour les messages plus critiques et peuvent être équipés d'un bouton d’action et d'un bouton activé par analyse.

Ce type de message est une sous-classe de [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)une classe abstraite qui implémente `IInAppMessageImmersive`, ce qui vous permet d'ajouter des fonctionnalités personnalisées à vos messages in-app générés localement.

![Un message in-app modal au centre d’un écran de téléphone affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché au centre d'une page Web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) Les messages in-app sont utiles pour maximiser le contenu et l'impact de votre communication avec les utilisateurs. La moitié supérieure d’un `full` message in-app contient une image, et la moitié inférieure affiche le texte et deux boutons d’action permettant l’analyse.

Ce type de message s'étend à [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)vous permettant d'ajouter des fonctionnalités personnalisées à vos messages in-app générés localement.

![Un message in-app plein écran s’affiche sur l’ensemble de l’écran du téléphone et affiche : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché en grand au centre d'une page web.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
Les messages in-app [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu du message in-app en HTML défini par l’utilisateur est affiché dans un `WebView` et peut éventuellement contenir d’autres contenus enrichis, tels que des images et des polices, permettant un contrôle total de l’apparence et de la fonctionnalité du message.

Ce type de message met en œuvre la norme [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html)qui est une sous-classe de [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html).

Les messages in-app Android prennent en charge une interface JavaScript `brazeBridge` pour appeler des méthodes du SDK Android de Braze à partir de votre HTML, voir notre page <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">pont JavaScript</a> pour plus de détails.

![Un message in-app en HTML avec un carrousel de contenu et des boutons interactifs.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Actuellement, nous ne prenons pas en charge l’affichage de messages in-app HTML personnalisés dans un iFrame sur les plateformes iOS et Android.
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Vous pouvez également définir des envois de messages in-app personnalisés pour votre application. Pour en savoir plus, consultez la rubrique [Création d'usines personnalisées]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories).
{% endalert %}
{% endtab %}