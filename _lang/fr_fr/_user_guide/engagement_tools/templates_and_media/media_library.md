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

Vous trouverez la **bibliothèque multimédia** sous la rubrique **Modèles**.

Vous pouvez utiliser la **bibliothèque multimédia** pour :

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

![Page Media Library (Bibliothèque multimédia) qui inclut une section « Upload To Library (Envoyer vers la bibliothèque) » pour glisser-déposer ou télécharger des fichiers. La bibliothèque multimédia contient également une liste des contenus chargés.][1]

{% alert tip %} Si vous avez besoin d’aide avec la bibliothèque multimédia, consultez notre [FAQ sur les modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Détails de l’image

Dans la bibliothèque multimédia, vous pouvez voir le type de ressource, la taille, les dimensions, l'URL, la date à laquelle elle a été ajoutée à la bibliothèque et d'autres informations. 

### Utiliser la bibliothèque multimédia plutôt qu'un réseau de diffusion de contenu

L'utilisation de la bibliothèque multimédia permet d'améliorer la mise en cache et les performances des messages in-app. Toutes les ressources de la bibliothèque multimédia trouvées dans un message in-app seront mises en cache pour un affichage plus rapide et seront disponibles pour un affichage hors ligne. En outre, la bibliothèque multimédia est intégrée aux compositeurs de Braze, ce qui permet aux marketeurs de sélectionner ou d'étiqueter des images au lieu de copier et de coller les URL des images.

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

##### Ressources supplémentaires

- [Spécifications de l'image et du texte en mode push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)

### Vidéo

Les vidéos téléchargées dans la bibliothèque multimédia ne peuvent pour l'instant être utilisées que dans les messages WhatsApp. Pour plus d'informations, reportez-vous à la section [Création d'un message Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
L'ajout de vidéos aux messages WhatsApp est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Accès à la bibliothèque multimédia à partir d’un éditeur de messages

La bibliothèque multimédia est un emplacement centralisé qui regroupe pour les ressources de votre tableau de bord, étant donné que toutes les images sont chargées directement dans la bibliothèque. Cela vous permet de réutiliser les images dans différents messages.

![Deux moyens habituels d’accéder à la bibliothèque multimédia selon l’éditeur de message. Un montre l’éditeur Drag & Drop e-mail avec le titre « Images et GIF » et un bouton « Ajouter depuis la bibliothèque multimédia ». L’autre présente les éditeurs standard, comme les notifications push et les messages in-app, avec le titre « Média » et un bouton pour « Ajouter une image ».][1.5]{: style="border:none"}

## Générer une image en utilisant l’IA {#generate-ai}

Vous pouvez générer des images pour votre bibliothèque multimédia à l'aide de [DALL-E 3](https://openai.com/index/dall-e-3/), un système d'intelligence artificielle d'OpenAI, un fournisseur tiers de Braze. Ce système peut créer des images réalistes et des œuvres d'art à partir d'une description en langage naturel. Chaque requête génère quatre variations de votre demande et votre entreprise peut générer des images 10 fois par jour. Ce total s’applique à tous les utilisateurs de votre entreprise.

1. Dans la bibliothèque multimédia, sélectionnez <i class="fas fa-wand-magic-sparkles"></i> **Générateur d’images basé sur l’IA**.
2. Saisissez une description de l’image que vous désirez générer, jusqu’à 300 caractères. Plus la description est détaillée, meilleur sera le résultat. Cette fonctionnalité ne prend en charge que la saisie de texte - le téléchargement d'une image comme référence n'est pas possible.
3. Sélectionnez **Générer des images.** Il faudra environ une minute pour que vos images soient générées.
4. Sélectionnez <i class="fas fa-download" title="Ajouter une image à la bibliothèque multimédia"></i> sur les images que vous souhaitez ajouter à votre bibliothèque multimédia.

![Fenêtre modale du générateur d’images par IA dans la bibliothèque multimédia.][6]{: style="max-width:75%"}

Entre vous et Braze, toutes les images générées à l'aide de DALL-E 3 sont votre propriété intellectuelle. Braze ne fera valoir aucune revendication de propriété intellectuelle sur ces images et ne donne aucune garantie de quelque nature que ce soit concernant tout contenu ou image généré par l’IA.

Pour générer des images, Braze enverra votre requête à la plateforme API d'OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans les données que vous fournissez. Comme décrit dans les [engagements de la plateforme API d’OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Veuillez vous assurer que vous respectez les politiques d'OpenAI qui vous concernent, lesquelles peuvent inclure sa [politique d'utilisation](https://openai.com/policies/usage-policies) et sa [politique en matière de partage et de publication](https://openai.com/policies/sharing-publication-policy). Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne tout contenu généré par l'IA. 


[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1.5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
Il y a [5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}
