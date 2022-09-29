---
nav_title: Bibliothèque multimédia
article_title: Bibliothèque multimédia
page_order: 0
page_type: reference
description: "Cet article de référence explique comment utiliser la bibliothèque multimédia pour gérer vos ressources dans un seul emplacement centralisé."
tool: Media

---

# Bibliothèque multimédia

> La bibliothèque multimédia vous permet de gérer vos ressources à un seul et même endroit. Pour accéder à cette fonction, accédez à l’onglet **Media Library (Bibliothèque multimédia)** dans la section [Templates & Media (Modèles et médias)][4] de votre tableau de bord.

Vous pouvez utiliser la **bibliothèque multimédia** pour :

* Télécharger plusieurs images simultanément
* Télécharger des fichiers .vcf (Virtual Contact File)
* Télécharger un dossier avec vos images (50 images max.)
* Rogner une image au bon format pour vos messages
* Ajouter des balises ou des équipes pour mieux organiser vos images
* Effectuer une recherche par balises ou équipes dans la nouvelle grille de la bibliothèque multimédia
* Glisser et déposer des images ou dossiers à télécharger
* Supprimer des images

![Page Media Library (Bibliothèque multimédia) qui inclut une section « Upload To Library (Envoyer vers la bibliothèque) » pour glisser-déposer ou télécharger des fichiers. La bibliothèque multimédia inclut également une liste des contenus téléchargés.][1]

## Statistiques disponibles

Dans la bibliothèque multimédia, vous pouvez voir les dimensions, l’URL et le type de l’image, ainsi que la date à laquelle elle a été ajoutée à la bibliothèque.

## Accès à la bibliothèque multimédia à partir d’un éditeur de messages

La bibliothèque multimédia est un emplacement centralisé qui regroupe pour les ressources de votre tableau de bord, étant donné que toutes les images sont téléchargées directement dans la bibliothèque. Cette fonctionnalité pratique vous permet de réutiliser des images dans différents messages.

## Gestion du contenu

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) et [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) vos modèles ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la section [Templates & Media (Modèles et médias)]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert tip %} Si vous avez besoin d’aide avec la bibliothèque multimédia, consultez notre [FAQ sur les modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

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

### Messages dans l’application

{% tabs local %}
{% tab Full screen %}

| Disposition | Format | Qualité de l’image | Remarques |
| ----- | ----- | ----- | ----- |
| Image et texte | Format 6:5 | Haute résolution : 1 200 x 1 000 pixels<br><br>Résolution minimum : 600 x 500 pixels | L’image peut être rognée de tous les côtés, mais elle occupera toujours la moitié supérieure de la fenêtre. |
| Image uniquement | Format 3:5 | Haute résolution : 1 200 x 2 000 pixels<br><br>Résolution minimum : 600 x 1 000 pixels | Sur les appareils grand format, l’image peut être rognée sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Modal %}

| Disposition | Format | Qualité de l’image | Remarques |
| ----- | ----- | ----- | ----- |
| Image et texte | Format 29:10 | Haute résolution : 1 450 x 500 pixels<br><br>Résolution minimum : 600 x 205 pixels | Les images hautes seront réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
| Image uniquement | Presque n’importe quel format | Haute résolution : 1 200 x 2 000 pixels<br><br>Résolution minimum : 600 x 600 pixels | Le message sera redimensionné pour s’adapter à la plupart des formats d’image.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% tab Slideup %}

| Disposition | Format | Qualité de l’image | Remarques |
| ----- | ----- | ----- | ----- |
| Image et texte | Format 1:1 | Haute résolution : 150 x 150 pixels<br><br>Résolution minimum : 50 x 50 pixels | Les images de différents formats seront insérées dans un conteneur d’images carré, sans rognage.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% endtab %}
{% endtabs %}

Pour plus d’informations, consultez les [informations créatives sur les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Notification push

{% tabs local %}
{% tab iOS %}

| Format | Qualité de l’image | Remarques |
| ---- | ---- | ---- |
| Format 2:1 (recommandé) | 1 038 x 1 038 pixels maximum | À compter du mois de janvier 2020, les notifications push enrichies pour iOS peuvent gérer des images de 1 038 par 1 038 pixels tant que leur taille est inférieure à 10 Mo, mais nous recommandons d’utiliser des fichiers aussi petits que possible. En pratique, l’envoi de fichiers volumineux peut entraîner une surcharge inutile du réseau et rendre les échecs de téléchargement plus courants.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### Ressources supplémentaires

- [Spécifications des images et du texte des notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Notifications enrichies pour iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/)

{% endtab %}
{% tab Android %}

Les notifications enrichies pour Android ne prennent pas en charge les GIF.

| Type d’image | Format | Qualité de l’image |
| ---- | ----- | ---- |
| Icône de notification push | Format 1:1 | S/O |
| Notification étendue | Format 2:1 | Small: 512 x 256 pixels<br>Moyenne : 1 024 x 512 pixels<br>Grande : 2 048 x 1 024 pixels |
| Image incorporée | Format 3:2 | S/O |

##### Ressources supplémentaires

- [Spécifications des images et du texte des notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Notifications enrichies pour Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/)
- [Notifications push d’images incorporées pour Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/)

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
