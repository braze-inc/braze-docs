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

Pour obtenir les meilleurs résultats, respectez les consignes suivantes concernant la taille de l'image et la longueur du message lors de la rédaction de vos messages push. Il peut y avoir des écarts en fonction de la présence d'une image, de l'état de la notification (iOS) et du réglage de l'affichage de l'appareil de l'utilisateur, ainsi que de la taille de l'appareil. En cas de doute, faites en sorte que votre texte soit court et agréable à lire.

## iOS et Android push

{% tabs local %}
{% tab Images %}

**Type d'image** | **Taille d'image recommandée** | **Taille maximale de l'image** | **Types de fichiers**
--- | --- | --- | ---
(iOS) 2:1 *Recommandé* | 500 KB | 5 MB | PNG, JPEG, GIF
(Android) Icône Push | 500 KB | 5 MB | PNG, JPEG
(Android) Notification élargie | 500 KB | 5 MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Text %}

| Type de message | Longueur recommandée des messages (texte uniquement) | Longueur d'envoi des messages recommandée (Rich)
--- | ---
(iOS) Écran de verrouillage | 160 caractères | 130 caractères
(iOS) Centre de notification | 160 caractères | 130 caractères
(iOS) Bannière d'alerte | 80 caractères | 65 caractères
Écran de verrouillage (Android) | 49 caractères | N/A
(Android) Tiroir de notification | 597 caractères | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Vous vous demandez combien de caractères vous pouvez utiliser dans une notification push iOS sans qu'elle soit tronquée ? Consultez nos [directives sur le nombre de caractères pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Payload Size %}

**Plateforme** | **Taille**
--- | ---
avant iOS 8 | 0.256 KB
post iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image Example %}
{% subtabs %}
{% subtab iOS %}

\![Notification push iOS avec le texte suivant : "Bonjour ! Il s'agit d'un iOS Push avec une image" avec un emoji. Une petite image figure à côté du texte.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
\![Notification push iOS sur un hard push avec le même texte que le message précédent avec une image développée précédant le texte.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

!notification push Android avec une grande image sous le texte du message.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Les notifications de grandes images s'affichent mieux lorsqu'elles utilisent une image d'au moins 600x300 pixels.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Text Example %}
{% subtabs %}
{% subtab iOS %}

\![Notification push iOS avec le texte suivant : "Bonjour ! Il s'agit d'un "push" d'iOS.]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
!notification push Android affichée sur l'écran d'accueil.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Poussée sur le web

{% tabs local %}
{% tab Images %}

| **Navigateur** | **Taille d'icône recommandée**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (les icônes sont configurables par campagne avec Safari 16 sur macOS 13+).
Opéra | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **Navigateur** | **Plateforme** | **Grande taille d'image**
| --- | --- | ---
Chrome | Android | Rapport hauteur/largeur 2:1
Firefox | Android | N/A
Chrome | Fenêtres | Rapport hauteur/largeur 2:1
Bord | Fenêtres | Rapport hauteur/largeur 2:1
Firefox | Fenêtres | N/A
Firefox | Fenêtres | Rapport hauteur/largeur 2:1
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opéra | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Text %}

| **Navigateur** | **Plateforme** | **Longueur maximale du titre**  | **Longueur maximale du corps du message**
| --- | --- | --- | ---
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Fenêtres | 50 | 120
Bord | Fenêtres | 50 | 120
Firefox | Fenêtres | 54 | 200
Opéra | Fenêtres | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opéra | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


