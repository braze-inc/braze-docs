---
nav_title: Étape de mise à jour de l’utilisateur
article_title: Étape de mise à jour de l’utilisateur
permalink: "/user_update/"
hidden: true
page_type: reference
description: "Cet article de référence aborde les étapes de mises à jour utilisateur et la façon de les utiliser dans votre Canvas."
tool: Canvas
---

# Étape de mise à jour de l’utilisateur

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

L’étape de mise à jour de l’utilisateur Canvas vous permet de mettre à jour les attributs, événements et achats d’un utilisateur dans un éditeur JSON. Il n’est donc pas nécessaire d’inclure des informations sensibles, par exemple des clés API.

Avec l’étape de mise à jour de l’utilisateur, les mises à jour ne comptent pas dans les limites de débit par minute ou des utilisateurs. Au lieu de cela, les mises à jour sont regroupées pour que Braze puisse les traiter plus efficacement qu’un webhook Braze-à-Braze.

Les utilisateurs ne passeront à des étapes Canvas en aval qu’une fois les mises à jour pertinentes de l’utilisateur effectuées. Si votre message en aval repose sur les mises à jour de l’utilisateur que vous effectuez, vous pouvez vous assurer que ces mises à jour ont été effectuées avant que les messages ne soient envoyés.

{% alert important %}
L’étape de mise à jour de l’utilisateur Canvas est actuellement en accès anticipé. Braze commencera à rendre obsolètes les webhooks Braze à Braze une fois cette fonctionnalité disponible. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé des mises à jour utilisateur de Canvas.
{% endalert %}

## Créer une étape de mise à jour utilisateur

Pour créer une étape de mise à jour de l’utilisateur, ajoutez une étape à votre Canvas. Utilisez le menu déroulant en haut de la nouvelle étape pour sélectionner `User Update Step`. Ensuite, ajoutez un attribut, un événement ou un objet JSON d'achat à l’éditeur JSON.

![][2] 

{% alert note %}
N’incluez pas les informations suivantes dans l’éditeur JSON :
* ID utilisateur externe
* Clé API
* URL du cluster Braze
* Champs liés aux importations de jetons de notification push
{% endalert %}

Par exemple, les utilisateurs qui reçoivent l’étape suivante de mise à jour utilisateur auront l’attribut Membre VIP défini sur `true`.

![][3]

### Fonctionnalités de personnalisation

L’étape de mise à jour de l’utilisateur prend également en charge les fonctions de personnalisation suivantes : 
* [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propriétés d’entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) et [propriétés de l’événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)
* Logique Liquid (dont [Annulation de messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Plusieurs mises à jour d’attribut ou d’événement par objet


[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} 
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} 
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
