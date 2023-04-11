---
nav_title: Mise à jour utilisateur 
article_title: Mise à jour utilisateur 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Cet article de référence aborde le composant de mises à jour de l’utilisateur et la façon de l’utiliser dans votre Canvas."
tool: Canvas
---

# Mise à jour utilisateur 

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

Le composant User Update (Mise à jour de l’utilisateur) vous permet de mettre à jour les attributs, événements et achats d’un utilisateur dans un éditeur JSON. Il n’est donc pas nécessaire d’inclure des informations sensibles, par exemple des clés API.

Avec Mise à jour utilisateur, les mises à jour ne comptent pas pour vos utilisateurs ou ne suivent pas la limitation du débit par minute. Au lieu de cela, les mises à jour sont regroupées pour que Braze puisse les traiter plus efficacement qu’un webhook Braze-à-Braze. Notez que ce composant consomme [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

Les utilisateurs ne passeront à l’étape Canvas suivante qu’une fois les mises à jour pertinentes de l’utilisateur effectuées. Si votre message suivant repose sur les mises à jour de l’utilisateur que vous effectuez, vous pouvez vous assurer que ces mises à jour ont été effectuées avant que les messages ne soient envoyés.

## Créer une mise à jour utilisateur

Glissez-déplacez le composant depuis la barre latérale ou cliquez le bouton plus <i class="fas fa-plus-circle"></i> en bas d’une variante ou d’une étape et sélectionnez **User Update (Mise à jour de l’utilisateur)**. 

Il existe trois options qui vous permettent de mettre à jour les informations existantes, d’ajouter de nouvelles ou de supprimer des informations de profil utilisateur. Toutes les étapes de mise à jour de l’utilisateur dans un groupe d’apps peuvent mettre à jour jusqu’à 200 000 profils utilisateur par minute.

{% alert tip %}
Vous pouvez également tester les modifications apportées à ce composant en recherchant un utilisateur et en lui appliquant la modification. Cela mettra à jour l’utilisateur.
{% endalert %}

### Mettre à jour l’attribut personnalisé

Pour ajouter ou mettre à jour un attribut personnalisé, sélectionnez un nom d’attribut dans votre liste d’attributs et entrez la valeur clé.

![][4]{: style="max-width:90%;"}

### Supprimer un attribut personnalisé

Pour supprimer un attribut personnalisé, sélectionnez un nom d’attribut à l’aide de la liste déroulante. Vous pouvez passer au compositeur JSON avancé pour modifier davantage. 

![][5]{: style="max-width:90%;"}

### Compositeur JSON avancé

Ajoutez un attribut, un événement ou un objet JSON d'achat d’un maximum de 65 536 caractères à l’éditeur JSON. Un utilisateur [abonnement mondial]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) et [groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) peut également être défini.

![][2]{: style="max-width:90%;"}

En utilisant le compositeur avancé, vous pouvez également prévisualiser et tester le fait que le profil utilisateur est mis à jour avec les modifications apportées grâce à l’onglet **Preview and test (Aperçu et test)**. Vous pouvez sélectionner un utilisateur aléatoire ou rechercher un utilisateur spécifique. Ensuite, après avoir envoyé un test à un utilisateur, affichez le profil utilisateur en utilisant le lien généré.

![][6]{: style="max-width:90%;"}

#### Limitations

Vous n’avez pas besoin d’inclure de données sensibles telles que votre clé API lorsque vous utilisez le compositeur JSON, car elles sont automatiquement fournies par la plateforme. Ainsi, les champs suivants ne sont pas nécessaires et ne doivent pas être utilisés dans le compositeur JSON :
* ID utilisateur externe
* Clé API
* URL du cluster Braze
* Champs liés aux importations de jetons de notification push
{% raw %}
#### Consigner un événement personnalisé

À l’aide du composeur JSON, vous pouvez également enregistrer des événements personnalisés. Notez que cela nécessite un horodatage au format ISO, il est donc nécessaire d’attribuer une heure et une date avec du Liquid au début. Prenons cet exemple qui enregistre un événement avec une heure.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
	"events": [{
		"name": "logged_user_event",
		"time": "timestamp" }]
}
```

Cet exemple suivant relie un événement à une application spécifique à l’aide d’un événement personnalisé avec des propriétés facultatives et l’`app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
	"events": [{
		"app_id": "b93361df-d496-432f-8d34-fb41cf7b2e25",
		"name": "rented_movie",
		"time": "timestamp",
		"properties": {
			"release": { "studio": "FilmStudio", "year": "2022" },
			"cast": [{ "name": "Actor1" }, { "name": "Actor2" }]
		}
	}]
}
```

#### Mettre à jour les groupes d’abonnement SMS 

Vous pouvez également mettre à jour les groupes d'abonnement à l'aide de l'étape de mise à jour utilisateur. L'exemple suivant montre une mise à jour des groupes d'abonnement. Vous pouvez effectuer une ou plusieurs mises à jour de groupe d'abonnement.

```
{
"attributes": [{
	"subscription_groups" : [
	{ "subscription_group_id": "bcc803d1-45df-4548-8f02-c4e9e87a1f8f", "subscription_state": "subscribed" },
	{ "subscription_group_id": "subscription_group_identifier_2", "subscription_state": "subscribed" },
	{ "subscription_group_id": "subscription_group_identifier_3", "subscription_state": "subscribed" }]
	}
	]
}
```
{% endraw %}
## Cas d’utilisation

### Définir la propriété d’entrée Canvas comme attribut

Vous pouvez utiliser l’étape de mise à jour de l’utilisateur pour faire persister un `canvas_entry_property`.  Imaginons que vous ayez un événement qui se déclenche lorsqu’un article est ajouté à un panier. Vous pouvez stocker l’ID de l’article le plus récemment ajouté au panier et l’utiliser pour une campagne de remarketing. Utilisez la fonctionnalité de personnalisation pour récupérer une propriété d’entrée Canvas et la stocker dans un attribut.

![][8]{: style="max-width:90%;"}

#### Personnalisation

Pour stocker la propriété de l’événement déclencheur d’un Canvas comme un attribut, utilisez le modal de personnalisation pour extraire et stocker la propriété d’entrée de Canvas. La mise à jour de l’utilisateur prend également en charge les fonctionnalités de personnalisation suivantes : 
* [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propriétés d’entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)
* Logique Liquid (y compris l’[annulation de messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Plusieurs mises à jour d’attribut ou d’événement par objet

### Augmenter les nombres

Ce composant peut également être utilisé pour suivre le nombre de fois qu’un utilisateur a effectué un événement en nombres d’incréments et de décrémentations. Par exemple, vous pouvez suivre le nombre de cours qu’un utilisateur a suivis au cours d’une semaine. À l’aide de ce composant, le nombre de cours peut être réinitialisé au début de la semaine avant de recommencer le suivi. 

![][7]{: style="max-width:90%;"}

### Ajouter aux tableaux

Vous pouvez ajouter ou supprimer des éléments d’un tableau et supprimer un élément. Par exemple, vous pouvez utiliser cette étape pour ajouter ou supprimer des éléments d’une liste de souhaits.

![][9]{: style="max-width:90%;"}

[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} 
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} 
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
[4]: {% image_buster /assets/img_archive/canvas_user_update_update.png %} 
[5]: {% image_buster /assets/img_archive/canvas_user_update_remove.png %} 
[6]: {% image_buster /assets/img_archive/canvas_user_update_test_preview.png %} 
[7]: {% image_buster /assets/img_archive/canvas_user_update_increment.png %} 
[8]: {% image_buster /assets/img_archive/canvas_user_update_cep.png %} 
[9]: {% image_buster /assets/img_archive/canvas_user_update_wishlist.png %} 