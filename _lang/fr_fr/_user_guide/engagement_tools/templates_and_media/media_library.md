---
nav_title: Bibliothèque multimédia
article_title: Bibliothèque multimédia
page_order: 0
page_type: reference
description: "Cet article de référence couvre la bibliothèque multimédia. Ici, vous pouvez apprendre à gérer vos actifs dans un emplacement unique et centralisé, à générer des images à l’aide de l’IA, à accéder aux médias dans votre éditeur de messages."
tool: Media

---

# Bibliothèque multimédia

> La bibliothèque multimédia vous permet de gérer vos ressources de façon centralisée. 

## Bibliothèque multimédia vs. RÉSEAU DE DIFFUSION DE CONTENU

L'utilisation de la bibliothèque multimédia au lieu d'un réseau de diffusion/distribution de contenu (CDN) permet d'améliorer la mise en cache et les performances des messages in-app. Toutes les ressources de la bibliothèque multimédia trouvées dans un message in-app seront mises en cache pour un affichage plus rapide et seront disponibles pour un affichage hors ligne. En outre, la bibliothèque multimédia est intégrée aux compositeurs de Braze, ce qui permet aux marketeurs de sélectionner ou d'étiqueter des images au lieu de copier et de coller les URL des images.

## Accès à la bibliothèque multimédia

Dans la bibliothèque multimédia, vous pouvez voir le type de ressource, la taille, les dimensions, l'URL, la date à laquelle elle a été ajoutée à la bibliothèque et d'autres informations. Pour accéder à votre bibliothèque multimédia Braze, allez dans CECI > Modèles **.** Ici, vous pouvez :

* Télécharger plusieurs images simultanément
* Télécharger des fichiers .vcf (Virtual Contact File)
* Téléchargez des fichiers vidéo à utiliser dans les messages WhatsApp
* Téléchargez un dossier avec vos images (maximum 50 images)
* [Générer une image à l'aide de l'intelligence artificielle](#generate-ai) et la stocker dans la bibliothèque multimédia.
* Rogner une image au bon format pour vos messages
* Ajouter des balises ou des équipes pour mieux organiser vos images
* Recherche par tags ou par équipes dans la grille de la bibliothèque multimédia
* Glisser et déposer des images ou dossiers à télécharger
* Supprimer des images

![Page Media Library (Bibliothèque multimédia) qui inclut une section « Upload To Library (Envoyer vers la bibliothèque) » pour glisser-déposer ou télécharger des fichiers. Vous trouverez également une liste des contenus téléchargés dans la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_main.png %})

Plus tard, lorsque vous rédigez un message dans Braze, vous pouvez extraire vos images de la bibliothèque multimédia.

![Deux moyens habituels d’accéder à la bibliothèque multimédia selon l’éditeur de message. Un montre l’éditeur Drag & Drop e-mail avec le titre « Images et GIF » et un bouton « Ajouter depuis la bibliothèque multimédia ». L'autre montre les éditeurs standard, tels que les messages in-app et push, avec le titre "Media" et un bouton pour "Ajouter une image".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Si vous avez besoin d’aide avec la bibliothèque multimédia, consultez notre [FAQ sur les modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Spécifications des images

Toutes les images chargées dans la bibliothèque multimédia doivent être inférieures à 5 Mo. Les types de fichiers pris en charge sont PNG, JPEG, GIF et SVG. Pour obtenir des recommandations sur les images en fonction du canal de communication, reportez-vous aux sections suivantes.

### Cartes de contenu

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-mail

{% multi_lang_include image_specs.md variable_name="e-mail"  %}

### in-app Messages

{% multi_lang_include image_specs.md variable_name="messages in-app"  %}

Pour plus d'informations, reportez-vous à la rubrique [Informations créatives sur les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Notification push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
Pour des ressources supplémentaires, voir les [spécifications de l'image et du texte de Push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Vidéo

Les vidéos téléchargées dans la bibliothèque multimédia ne peuvent pour l'instant être utilisées que dans les messages WhatsApp. Pour plus d'informations, reportez-vous à la section [Création d'un message Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
L'ajout de vidéos aux messages WhatsApp est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Générer des images avec <sup>BrazeAITM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Avant d'utiliser cette fonctionnalité, examinez la [manière dont vos données sont utilisées et envoyées à OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
