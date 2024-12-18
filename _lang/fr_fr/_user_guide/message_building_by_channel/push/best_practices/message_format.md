---
nav_title: Formats des messages
article_title: "Formats d'envoi de messages et d'images en mode push"
page_order: 5
page_type: reference
description: "Cet article décrit les formats de message et d'image pour les notifications push."
channel: push

---

# Formats d'envoi de messages et d'images en mode push

> Cet article de référence décrit les formats de message et d'image pour les notifications push.

Pour de meilleurs résultats, reportez-vous aux directives de taille et de longueur de message suivantes lors de l’élaboration de vos messages de notification push. Il peut y avoir une variation en fonction de la présence d’une image, de l’état de la notification (iOS) et du réglage d’affichage de l’appareil de l’utilisateur, ainsi que de sa taille. En cas de doute, gardez votre texte bref et agréable.

## iOS et Android push

{% tabs local %}
{% tab Images %}

**Type d'image** | **Taille d’image recommandée** | **Taille maximale de l'image** | **Types de fichiers**
--- | --- | --- | ---
(iOS) 2:1 *Recommandé* | 500 KB | 5 MB | PNG, JPEG, GIF
Icône de notification push (Android) | 500 KB | 5 MB | PNG, JPEG
Notification étendue (Android) | 500 KB | 5 MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Texte %}

| Type de message | Longueur recommandée du message (texte uniquement) | Longueur recommandée du message (riche)
--- | ---
Écran de verrouillage (iOS) | 160 caractères | 130 caractères
Centre de notification (iOS) | 160 caractères | 130 caractères
Alerte en bannière (iOS) | 80 caractères | 65 caractères
Écran de verrouillage (Android) | 49 caractères | S.O.
Barre de notification (Android) | 597 caractères | S.O.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Vous vous demandez combien de caractères vous pouvez utiliser dans une notification push iOS sans qu’elle soit tronquée ? Consultez nos [directives sur le nombre de caractères pour iOS.]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

{% endtab %}
{% tab Taille de la charge utile %}

**Plateforme** | **Taille**
--- | ---
Pré-iOS 8 | 0,256 Ko
Post-iOS 8 | 2 Ko
Android (FCM) | 4 Ko
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Exemple d'image %}
{% subtabs %}
{% subtab iOS %}

![Notification push iOS avec un texte qui dit : «∘Bonjour ! Ceci est une notification push iOS avec une image » avec un émoji. Une petite image figure à côté du texte.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notification push iOS sur une notification push dure avec le même texte que le message précédent avec une image développée précédant le texte.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Notification push Android avec une grande image sous le texte du message.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Les notifications avec de grandes images s’affichent mieux lorsque vous utilisez une image d’au moins 600 x 300 pixels.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Exemple de texte %}
{% subtabs %}
{% subtab iOS %}

![Notification push iOS avec un texte qui dit : «∘Bonjour ! Ceci est une notification push iOS. »]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Notification push Android affichée sur l'écran d'accueil.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Push Web

{% tabs local %}
{% tab Images %}

| **Navigateur** | **Taille d'icône recommandée**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (les icônes sont configurables par campagne avec Safari 16 sur macOS 13+)
Opera | 192 x 192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **Navigateur** | **Plateforme** | **Grande taille d'image**
| --- | --- | ---
Chrome | Android | Format 2:1
Firefox | Android | S.O.
Chrome | Windows | Format 2:1
Edge | Windows | Format 2:1
Firefox | Windows | S.O.
Firefox | Windows | Format 2:1
Safari | macOS | S.O.
Chrome | macOS | S.O.
Firefox | macOS | S.O.
Opera | macOS | S.O.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Texte %}

| **Navigateur** | **Plateforme** | **Longueur maximale du titre**  | **Longueur maximale du corps du message**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


