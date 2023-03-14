---
nav_title: Bibliothèque multimédia
article_title: Bibliothèque multimédia
page_order: 0
page_type: reference
description: "Cet article de référence couvre la bibliothèque multimédia. Ici, vous pouvez apprendre à gérer vos actifs dans un emplacement unique et centralisé, à générer des images à l’aide de l’IA, à accéder aux médias dans votre éditeur de messages."
tool: Médias

---

# Bibliothèque multimédia

> La bibliothèque multimédia vous permet de gérer vos ressources à un seul et même endroit. Pour accéder à cette fonctionnalité, accédez à l’onglet **Media Library (Bibliothèque multimédia)** dans la section [Templates & Media (Modèles et médias)][4] de votre tableau de bord.

Vous pouvez utiliser la **Media Library (bibliothèque multimédia)** pour :

* Télécharger plusieurs images simultanément
* Télécharger des fichiers .vcf (Virtual Contact File)
* Télécharger un dossier avec vos images (50 images max.)
* [Générer une image en utilisant l’IA](#generate-ai) et l’enregistrer dans la bibliothèque multimédia
* Rogner une image au bon format pour vos messages
* Ajouter des balises ou des équipes pour mieux organiser vos images
* Effectuer une recherche par balises ou équipes dans la grille de la bibliothèque multimédia
* Glisser et déposer des images ou dossiers à télécharger
* Supprimer des images

![Page Media Library (Bibliothèque multimédia) qui inclut une section « Upload To Library (Envoyer vers la bibliothèque) » pour glisser-déposer ou télécharger des fichiers. La bibliothèque multimédia inclut également une liste des contenus téléchargés.][1]

{% alert tip %} Si vous avez besoin d’aide avec la bibliothèque multimédia, consultez notre [FAQ sur les modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Détails de l’image

Dans la bibliothèque multimédia, vous pouvez voir le type, la taille, les dimensions et l’URL de l’image, ainsi que la date à laquelle elle a été ajoutée à la bibliothèque.

## Spécifications des images

La taille de toutes les images téléchargées dans la bibliothèque multimédia doit être inférieure à 5 Mo. Les types de fichiers pris en charge sont PNG, JPEG et GIF. Pour obtenir des recommandations sur les images en fonction du canal de communication, reportez-vous aux sections suivantes.

### Cartes de contenu

| Type de carte | Format     | Qualité de l’image       |
| --------- | ---------------- | ------------------- |
| Classique   | Format 1:1 | 60 x 60 pixels        |
| Avec légende | Format 4:3 | Largeur minimum : 600 px |
| Bannière    | Tout format | Largeur minimum : 600 px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Pour plus d’informations, consultez les [informations créatives des cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

### E-mail

| Type d’image   | Format     | Qualité de l’image       |
| ------------ | ---------------- | ------------------- |
| Image d’en-tête | Tout format | Largeur maximale : 600 px |
| Image du corps   | Tout format | Largeur maximale : 480 px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Les images de petite taille et de haute qualité se chargeront plus rapidement, il est donc recommandé d’utiliser le plus petit format possible pour obtenir le résultat souhaité.

### Messages in-app

{% tabs local %}
{% tab Full screen %}

| Disposition | Format | Qualité de l’image | Remarques |
| ----- | ----- | ----- | ----- |
| Image et texte | Format 6:5 | Haute résolution 1200 px par 1000 px<br><br>Résolution minimale 600 px par 500 px | L’image peut être rognée de tous les côtés, mais elle occupera toujours la moitié supérieure de la fenêtre. |
| Image uniquement | Format 3:5 | Haute résolution 1200 px par 2000 px<br><br>Résolution minimale 600 px par 1000 px | Sur les appareils grand format, l’image peut être rognée sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Modal %}

| Disposition | Format | Qualité de l’image | Remarques |
| ----- | ----- | ----- | ----- |
| Image et texte | Format 29:10 | Haute résolution 1450 px par 500 px<br><br>Résolution minimale 600 px par 205 px | Les images hautes seront réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
| Image uniquement | Presque n’importe quel format | Haute résolution 1200 px par 2000 px<br><br>Résolution minimale 600 px par 600 px | Le message est redimensionné pour accepter des images de la plupart des rapports d’aspect.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Slideup %}

| Disposition | Format | Qualité de l’image | Remarques |
| ----- | ----- | ----- | ----- |
| Image et texte | Format 1:1 | Haute résolution 150 px par 150 px<br><br>Résolution minimale 50 px par 50 px | Les images de différents rapports d’aspect s’insèrent dans un conteneur d’images carré, sans rognage.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% endtabs %}

Pour plus d’informations, consultez les [informations créatives sur les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Notification push

{% tabs local %}
{% tab iOS %}

| Format | Qualité de l’image | Remarques |
| ---- | ---- | ---- |
| Format 2:1 (recommandé) | 1 038 x 1 038 pixels maximum | À compter du mois de janvier 2020, les notifications push enrichies pour iOS peuvent gérer des images de 1 038 par 1 038 pixels tant que leur taille est inférieure à 10 Mo, mais nous recommandons d’utiliser des fichiers aussi petits que possible. En pratique, l’envoi de fichiers volumineux peut entraîner une surcharge inutile du réseau et rendre les échecs de téléchargement plus courants.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### Ressources supplémentaires

- [Spécifications des images et du texte des notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Notifications enrichies pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)

{% endtab %}
{% tab Android %}

Les notifications enrichies pour Android ne prennent pas en charge les GIF.

| Type d’image | Format | Qualité de l’image |
| ---- | ----- | ---- |
| Icône de notification push | Format 1:1 | S.O. |
| Notification étendue | Format 2:1 | Petite : 512 px par 256 px<br>Moyenne : 1024 px par 512 px<br>Grande : 2048 px par 1024 px |
| Image incorporée | Format 3:2 | S.O. |

##### Ressources supplémentaires

- [Spécifications des images et du texte des notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Notifications enrichies pour Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)
- [Notifications push d’images incorporées pour Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/)

{% endtab %}
{% endtabs %}

## Accès à la bibliothèque multimédia à partir d’un éditeur de messages

La bibliothèque multimédia est un emplacement centralisé qui regroupe pour les ressources de votre tableau de bord, étant donné que toutes les images sont téléchargées directement dans la bibliothèque. Ceci vous permet de réutilisez des images dans des messages différents.

![Deux moyens habituels d’accéder à la bibliothèque multimédia selon l’éditeur de message. Un montre l’éditeur Drag & Drop e-mail avec le titre « Images et GIF » et un bouton « Ajouter depuis la bibliothèque multimédia ». L’autre présente les éditeurs standards comme les notifications push et les messages in-app, avec le titre « Média » et un bouton pour « Ajouter une image ».][1.5]{: style="border:none"}

## Générer une image en utilisant l’IA {#generate-ai}

Vous pouvez générer des images pour votre bibliothèque multimédia en utilisant [DALL E 2](https://openai.com/dall-e-2/), un système IA d’OpenAI qui peut créer des images et des représentations artistiques réalistes à partir d’une description en langage naturel. Chaque requête génère quatre variations de votre demande et votre entreprise peut générer des images 10 fois par jour. Ce total s’applique à tous les utilisateurs de votre entreprise.

1. À partir de la bibliothèque multimédia, cliquez sur <i class="fas fa-wand-magic-sparkles"></i> **AI Image Generator (Générateur d’image par IA)**.
2. Saisissez une description de l’image que vous désirez générer, jusqu’à 300 caractères. Plus la description est détaillée, meilleur sera le résultat.
3. Cliquez sur **Generate Images (Générer des images)**. Il faudra environ une minute pour que vos images soient générées.
4. Cliquez <i class="fas fa-download" title="Ajouter une image à la bibliothèque multimédia"></i> sur les images que vous aimez pour les ajouter à votre bibliothèque multimédia.

![Modal du générateur d’images par IA dans la bibliothèque multimédia.][6]{: style="max-width:75%"}

[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1.5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}