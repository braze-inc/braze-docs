---
nav_title: Bibliothèque multimédia
article_title: Bibliothèque multimédia
page_order: 0
page_type: reference
description: "Cet article de référence couvre la bibliothèque multimédia. Ici, vous pouvez apprendre à gérer vos ressources dans un emplacement unique et centralisé, générer des images à l'aide de l'intelligence artificielle et accéder aux médias dans votre éditeur de messages."
tool: Media

---

# Bibliothèque multimédia

> La bibliothèque multimédia vous permet de gérer vos ressources de façon centralisée. 

## Bibliothèque multimédia ou réseau de diffusion de contenu

L'utilisation de la bibliothèque multimédia au lieu d'un réseau de diffusion de contenu (CDN) permet d'améliorer la mise en cache et les performances des messages in-app. Toutes les ressources de la bibliothèque multimédia présentes dans un message in-app seront pré-mises en cache pour un affichage plus rapide et seront disponibles hors ligne. De plus, la bibliothèque multimédia est intégrée aux compositeurs de Braze, ce qui permet aux marketeurs de sélectionner ou d'étiqueter des images au lieu de copier-coller les URL des images.

## Accès à la bibliothèque multimédia

Dans la bibliothèque multimédia, vous pouvez voir le type de ressource, la taille, les dimensions, l'URL, la date d'ajout à la bibliothèque et d'autres informations. Pour accéder à votre bibliothèque multimédia Braze, allez dans **Modèles** > **Bibliothèque multimédia**. Vous pouvez alors :

* Charger plusieurs images simultanément
* Charger des fichiers Virtual Contact File (.vcf)
* Charger des fichiers vidéo à utiliser dans les messages WhatsApp
* Charger un dossier contenant vos images (jusqu'à 50 images)
* [Générer une image à l'aide de l'intelligence artificielle](#generate-ai) et la stocker dans la bibliothèque multimédia
* Rogner une image existante au bon rapport hauteur/largeur pour vos messages
* Ajouter des étiquettes ou des équipes pour mieux organiser vos images
* Rechercher par étiquettes ou par équipes dans la grille de la bibliothèque multimédia
* Glisser-déposer des images ou dossiers à charger
* Supprimer des images

![Page de la bibliothèque multimédia qui inclut une section « Upload To Library » pour glisser-déposer ou charger des fichiers. La bibliothèque multimédia contient également une liste des contenus chargés.]({% image_buster /assets/img_archive/media_library_main.png %})

Par la suite, lorsque vous rédigez un message dans Braze, vous pouvez importer vos images depuis la bibliothèque multimédia.

![Deux moyens habituels d'accéder à la bibliothèque multimédia selon l'éditeur de message. L'un montre l'éditeur Drag & Drop e-mail avec le titre « Images et GIF » et un bouton « Ajouter depuis la bibliothèque multimédia ». L'autre affiche les éditeurs standard, tels que les notifications push et les messages in-app, avec le titre « Médias » et un bouton « Ajouter une image ».]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Pour plus d'informations sur la bibliothèque multimédia, consultez la [FAQ sur les modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Spécifications des images

Toutes les images chargées dans la bibliothèque multimédia doivent être inférieures à 5&nbsp;Mo. Les types de fichiers pris en charge sont PNG, JPEG, GIF, SVG et WebP. Pour obtenir des recommandations sur les images en fonction du canal de communication, reportez-vous aux sections suivantes.

{% alert important %}
Les GIF aux formats très allongés (par exemple, 3000 x 2 pixels) ou comportant 300 images ou plus peuvent échouer au chargement, même si la taille totale du fichier est réduite.
{% endalert %}

### Cartes de contenu

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### Messages in-app

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Pour plus d'informations, reportez-vous à la rubrique [Détails créatifs des messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Notifications push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

#### Longueurs de message recommandées

Pour de meilleurs résultats, consultez les recommandations de longueur de message suivantes lors de la rédaction de vos notifications push. Des variations sont possibles en fonction de la présence d'une image, de l'état de la notification (iOS), des paramètres d'affichage de l'appareil de l'utilisateur et de la taille de l'appareil.

| Type de message | Longueur recommandée (texte seul) | Longueur recommandée (rich) |
| --- | --- | --- |
| Écran de verrouillage iOS | 160 caractères | 130 caractères |
| Centre de notifications iOS | 160 caractères | 130 caractères |
| Bannière d'alerte iOS | 80 caractères | 65 caractères |
| Écran de verrouillage Android | 49 caractères | N/A |
| Tiroir de notifications Android | 597 caractères | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Pour plus d'informations sur le nombre de caractères iOS, consultez les [recommandations de nombre de caractères iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

#### Notifications push web

{% tabs %}
{% tab Images %}

| Navigateur | Taille d'icône recommandée |
| --- | --- |
| Chrome | 192 x 192 px ou plus |
| Firefox | 192 x 192 px ou plus |
| Safari | 192 x 192 px ou plus (configurable par campagne avec Safari 16 sur macOS 13+) |
| Opera | 192 x 192 px ou plus |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| Navigateur | Plateforme | Taille de la grande image |
| --- | --- | --- |
| Chrome | Android | Rapport hauteur/largeur 2:1 |
| Firefox | Android | N/A |
| Chrome | Windows | Rapport hauteur/largeur 2:1 |
| Edge | Windows | Rapport hauteur/largeur 2:1 |
| Firefox | Windows | N/A |
| Opera | Windows | Rapport hauteur/largeur 2:1 |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Texte %}

| Navigateur | Plateforme | Longueur maximale du titre | Longueur maximale du corps |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### Exemples de notifications push

{% tabs %}
{% tab iOS %}

![Notification push iOS avec le texte : « Hi! This is an iOS Push with an image » accompagné d'un emoji. Une petite image est affichée à côté du texte.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notification push iOS en mode étendu avec le même texte que le message précédent et une image agrandie au-dessus du texte.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Notification push Android avec une grande image sous le texte du message.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Les notifications avec grande image s'affichent de manière optimale avec une image d'au moins 600 x 300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}

### Vidéo

Les vidéos chargées dans la bibliothèque multimédia ne peuvent être utilisées que dans les messages WhatsApp. Pour plus d'informations, consultez [Créer un message WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Générer des images avec BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Avant d'utiliser cette fonctionnalité, consultez la [manière dont vos données sont utilisées et envoyées à OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}