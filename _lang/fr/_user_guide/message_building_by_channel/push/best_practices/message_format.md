---
nav_title: Format de message
article_title: Format de message de notification push
page_order: 5
page_type: reference
description: "Le présent article décrit les formats de message et d’image pour les notifications push iOS et Android."
channel: push

---

# Format de message

> Le présent article de référence décrit les formats de message et d’image pour les notifications push iOS et Android.

## iOS

{% tabs local %}
{% tab General %}

- **Longueur du message :**
  - Écran de verrouillage iOS : 110 caractères
  - Centre de notification iOS : 110 caractères
  - Alerte en bannière iOS : 62 caractères
  - Alerte contextuelle iOS : 235 caractères
- **Taille de charge utile :**
  - iOS : 2 Ko
- **Nombre de lignes :**
  - Écran de verrouillage iOS : 4 lignes
  - Centre de notification iOS : 4 lignes
  - Alerte en bannière iOS : 2 lignes
  - Alerte contextuelle iOS : 8 lignes
- **IU personnalisable :** Non
- **Possibilité de lien profond :** Oui

{% endtab %}
{% tab Image Sizes %}

|    Format   | Taille d’image recommandée | Taille d’image maximale |   Types de fichiers  |
|:-----------------:|:----------------------:|:------------------:|:-------------:|
| 2:1 (recommandé) |          500 Ko         |         5 Mo        | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Text Example %}

![Notification push iOS avec un texte qui dit : «∘Bonjour ! Ceci est une notification push iOS ».]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endtab %}
{% tab Image Example %}

![Notification push iOS avec un texte qui dit : «∘Bonjour ! Ceci est une notification push iOS avec une image » avec un émoji. Il y a une petite image à côté du texte.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notification push iOS sur une notification push dure avec le même texte que le message précédent avec une image étendue précédant le texte.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

## Android

{% tabs local %}
{% tab General %}

- **Longueur du message :**
  - Écran de verrouillage : 1 ligne (49 caractères maximum estimés)
  - Zone de notification : 1 ligne, jusqu’à 8 lignes lorsqu’elles sont étendues (estimation de 597 caractères maximum)
- **Taille de charge utile :**
  - FCM : 4 Ko
- **IU personnalisable :** Oui
- **Possibilité de lien profond :** Oui

{% endtab %}
{% tab Image Sizes %}

#### Icône de notification push

|         Format         | Taille d’image recommandée |                         Taille d’image maximale                         | Types de fichiers |
|:----------------------------:|:----------------------:|:------------------------------------------------------------------:|:----------:|
| 1:1 (400 x 400 pixels minimum) |          500 Ko         | S.O. cependant, un équilibre doit être trouvé entre la qualité et la taille |  PNG, JPG  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

#### Image de notification étendue

|         Format         | Taille d’image recommandée |                         Taille d’image maximale                         | Types de fichiers |
|:----------------------------:|:----------------------:|:------------------------------------------------------------------:|:----------:|
| 2:1 (600 x 300 pixels minimum) |          500 Ko         | S.O. cependant, un équilibre doit être trouvé entre la qualité et la taille |  PNG, JPG  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
Les images plus petites et de haute qualité se chargeront plus rapidement, il est donc recommandé d’utiliser le plus petit actif possible pour obtenir l’affichage souhaité.
{% endalert %}

{% endtab %}
{% tab Text Example %}

![Notification push Android affichée sur l’écran d’accueil.]({% image_buster /assets/img_archive/Push_Android_2.png %})

{% endtab %}
{% tab Image Example %}

![Notification push Android avec une grande image sous le texte du message.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Les notifications avec de grandes images s’affichent mieux lorsque vous utilisez une image d’au moins 600 x 300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}


