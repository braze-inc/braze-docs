---
nav_title: Étape de mise à jour de l'utilisateur
article_title: Étape de mise à jour de l'utilisateur
permalink: "/fr/user_update/"
hidden: vrai
page_type: Référence
description: "Cet article de référence traite de l'étape de mise à jour de l'utilisateur et de la façon de les utiliser dans vos Canvases."
tool: Toile
---

# Étape de mise à jour de l'utilisateur

!\[Étape de mise à jour de l'utilisateur Canvas\]\[1\]{: style="float:right;max-width:45%;margin-left:15px;"}

L'étape de mise à jour de l'utilisateur de Canvas vous permet de mettre à jour les attributs, les événements de l'utilisateur et achète dans un compositeur JSON, donc il n'est pas nécessaire d'inclure des informations sensibles comme les clés d'API.

Avec l'étape de mise à jour de l'utilisateur, les mises à jour ne comptent pas pour vos utilisateurs ou ne suivent pas la limite de taux par minute. Au lieu de cela, les mises à jour sont par lots et Braze peut les traiter plus efficacement qu'un webhook brésilien.

Les utilisateurs ne passeront aux étapes de Canvas en aval qu'une fois que les mises à jour de l'utilisateur auront été complétées. Si votre messagerie en aval repose sur les mises à jour de l'utilisateur que vous effectuez, vous pouvez vous assurer que ces mises à jour sont terminées avant la date d'envoi des messages.

{% alert important %}
Les mises à jour des utilisateurs de Canvas sont actuellement en accès anticipé. Braze va commencer à déprécier les webhooks Braze-to-Braze une fois que cette fonctionnalité est généralement disponible. Veuillez communiquer avec votre gestionnaire de comptes Braze si vous êtes intéressé à participer aux mises à jour anticipées des utilisateurs de Canvas .
{% endalert %}

## Créer une étape de mise à jour utilisateur

Pour créer une étape de mise à jour de l'utilisateur, ajoutez une étape à votre Canvas. Utilisez le menu déroulant en haut de la nouvelle étape pour sélectionner `Étape de mise à jour utilisateur`. Ensuite, ajoutez un attribut, un événement ou achetez un objet JSON au compositeur JSON.

!\[JSON Composer\]\[2\]

{% alert note %}
N'incluez aucune des informations suivantes dans le compositeur JSON :
* ID d'utilisateur externe
* Clé API
* URL du cluster Braze
* Champs liés aux importations de jetons push
{% endalert %}

À titre d'exemple, les utilisateurs qui reçoivent l'étape de mise à jour de l'utilisateur ci-dessous auront l'attribut membre VIP défini à `true`.

!\[Exemple dans JSON Composer\]\[3\]

### Fonctionnalités de personnalisation

L'étape de mise à jour de l'utilisateur prend également en charge les fonctionnalités de personnalisation suivantes :

* [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
* [Blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* Liquid logique (y compris [Abandon des messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)
* Mises à jour d'attributs ou d'événements multiples par objet

{% alert note %}
Les propriétés d'entrée et d'événement ne sont pas supportées pour l'étape de mise à jour de l'utilisateur.
{% endalert %}
[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} [2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} [3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
