---
nav_title: Format du message
article_title: Format du message push
page_order: 5
page_type: Référence
description: "Cet article décrit les formats de messages et d'images pour les notifications push iOS, Android et Windows."
channel: Pousser
---

# Format du message

> Cet article de référence décrit les formats de messages et d'images pour les notifications push iOS, Android et Windows.

## iOS

{% tabs local %}
{% tab General %}

- **Longueur du message :**
  - Écran de verrouillage iOS : 110 caractères
  - Centre de notification iOS : 110 caractères
  - Alerte de bannière iOS : 62 caractères
  - Alerte Pop Up iOS : 235 caractères
- **Taille de la charge utile :**
  - iOS: 2Ko
- **Nombre de lignes:**
  - Écran de verrouillage iOS : 4 Lignes
  - Centre de notification iOS : 4 Lignes
  - Alerte de bannière iOS : 2 lignes
  - Alerte Pop Up iOS : 8 Lignes
- **Interface utilisateur personnalisable :** Non
- **Possibilité de lien profond :** Oui

{% endtab %}
{% tab Image Sizes %}

|  Ratio d'aspect  | Taille de l'image recommandée | Taille maximale de l'image | Types de fichiers |
|:----------------:|:-----------------------------:|:--------------------------:|:-----------------:|
| 2:1 (recommandé) |             500Ko             |            5 Mo            |   PNG, JPG, GIF   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Text Example %}

![Petite notification Push iOS]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endtab %}
{% tab Image Example %}

![Push riche iOS]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS Rich Push On Hard Push]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

## Android

{% tabs local %}
{% tab General %}

- **Longueur du message :**
  - Écran de verrouillage : 1 ligne (estimée à 49 caractères max)
  - Panneau de notification : 1 ligne, jusqu'à 8 lignes en cas d'extension (estimée à 597 caractères max)
- **Taille de la charge utile :**
  - FCM: 4KB
- **IU personnalisable :** Oui
- **Possibilité de lien profond :** Oui

{% endtab %}
{% tab Image Sizes %}

#### Icône Push

|        Ratio d'aspect        | Taille de l'image recommandée |                         Taille maximale de l'image                          | Types de fichiers |
|:----------------------------:|:-----------------------------:|:---------------------------------------------------------------------------:|:-----------------:|
| 1:1 (400x400 pixels minimum) |             500Ko             | N/A - cependant un équilibre doit être trouvé entre la qualité et la taille |     PNG, JPG      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

#### Image de notification étendue

|        Ratio d'aspect        | Taille de l'image recommandée |                         Taille maximale de l'image                          | Types de fichiers |
|:----------------------------:|:-----------------------------:|:---------------------------------------------------------------------------:|:-----------------:|
| 2:1 (600x300 pixels minimum) |             500Ko             | N/A - cependant un équilibre doit être trouvé entre la qualité et la taille |     PNG, JPG      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
Des images plus petites et de haute qualité se chargeront plus rapidement. Il est donc recommandé d'utiliser le plus petit actif possible pour atteindre la sortie souhaitée.
{% endalert %}

{% endtab %}
{% tab Text Example %}

![Push Android]({% image_buster /assets/img_archive/Push_Android_2.png %})

{% endtab %}
{% tab Image Example %}

![Grande image Android]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Les notifications d'images de grande taille s'affichent mieux lorsque vous utilisez une image d'au moins 600x300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}

## Univers Windows

{% tabs local %}
{% tab General %}

- **Longueur du message :** Dépend de l'appareil
- **Taille de la charge utile :** 3 kilo-octets
- **Nombre de lignes :** 1-3 lignes
- **Interface utilisateur personnalisable :** Non
- **Possibilité de lien profond :** Non

{% endtab %}
{% tab Text Example %}

![Universelle de la fenêtre Push]({% image_buster /assets/img_archive/Push_Window8_Toast.png %})

{% endtab %}
{% endtabs %}

## Windows Phone 8

{% tabs local %}
{% tab General %}

- **Longueur du message :** Varies. Si seul le titre est défini, environ 40 caractères peuvent être affichés. Si seul le contenu est défini, environ 47 caractères peuvent être affichés. Si le titre et le contenu sont définis, alors environ 41 caractères peuvent être affichés.
- **Taille de la charge utile :** 5 kilo-octets
- **Nombre de lignes :** 1
- **Interface utilisateur personnalisable :** Non
- **Possibilité de lien profond :** Non

{% endtab %}
{% tab Text Example %}

![Pousser Window8]({% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %})

{% endtab %}
{% endtabs %}
[27]: {% image_buster /assets/img_archive/android_push_img2.png %} [42]: {% image_buster /assets/img_archive/iOS_push_notification_small. ng %} [43]: {% image_buster /assets/img_archive/Push_Android_2.png %} [46]:{% image_buster /assets/img_archive/Push_Window8_Toast. ng %} [47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %} [54]: {% image_buster /assets/img_archive/braze_richpush1.png %} [55]: {% image_buster /assets/img_archive/braze_richpush2.png %}
