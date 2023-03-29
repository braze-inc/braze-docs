---
nav_title: Mise à jour utilisateur 
article_title: Mise à jour utilisateur 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Cet article de référence aborde les étapes de mises à jour utilisateur et la façon de les utiliser dans votre Canvas."
tool: Canvas
---

# Mise à jour utilisateur 

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

Le composant de mise à jour de l’utilisateur vous permet de mettre à jour les attributs, événements et achats d’un utilisateur dans un éditeur JSON. Il n’est donc pas nécessaire d’inclure des informations sensibles, par exemple des clés API.

Avec Mise à jour utilisateur, les mises à jour ne comptent pas pour vos utilisateurs ou ne suivent pas la limite de taux par minute. Au lieu de cela, les mises à jour sont regroupées pour que Braze puisse les traiter plus efficacement qu’un webhook Braze-à-Braze. Notez que ce composant consomme [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

Les utilisateurs ne passeront à des étapes Canvas en aval qu’une fois les mises à jour pertinentes de l’utilisateur effectuées. Si votre message en aval repose sur les mises à jour de l’utilisateur que vous effectuez, vous pouvez vous assurer que ces mises à jour ont été effectuées avant que les messages ne soient envoyés.

## Créer une mise à jour utilisateur

Glissez-déplacez le composant depuis la barre latérale ou cliquez le bouton plus <i class="fas fa-plus-circle"></i> en bas d’une étape et sélectionnez **User Update (Chemins d’expérience)**. 

Il existe trois options qui vous permettent de mettre à jour les informations existantes, d’ajouter de nouvelles ou de supprimer des informations de profil utilisateur. Toutes les étapes de mise à jour de l’utilisateur dans un groupe d’apps peuvent mettre à jour jusqu’à 200 000 profils utilisateur par minute.

### Mettre à jour l’attribut personnalisé

Pour ajouter ou mettre à jour un attribut personnalisé, sélectionnez un nom d’attribut dans votre liste d’attributs et entrez la valeur clé.

![][4]{: style="max-width:90%;"}

### Supprimer un attribut personnalisé

Pour supprimer un attribut personnalisé, sélectionnez un nom d’attribut à l’aide de la liste déroulante. Vous pouvez passer au compositeur JSON avancé pour modifier davantage. 

![][5]{: style="max-width:90%;"}

### Compositeur JSON avancé

Ajoutez un attribut, un événement ou un objet JSON d’achat d’un maximum de 65 536 caractères à l’éditeur JSON. Un utilisateur [abonnement mondial]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) et [groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) peut également être défini.

![][2]{: style="max-width:90%;"}

En utilisant le compositeur avancé, vous pouvez également prévisualiser et tester le fait que le profil utilisateur est mis à jour avec les modifications apportées grâce à l’onglet **Preview and test (Aperçu et test)**. Vous pouvez sélectionner un utilisateur aléatoire ou rechercher un utilisateur spécifique. Ensuite, après avoir envoyé un test à un utilisateur, affichez le profil utilisateur en utilisant le lien généré.

![][6]{: style="max-width:90%;"}

#### Limitations

Vous n’avez pas besoin d’inclure de données sensibles telles que votre clé API lorsque vous utilisez le compositeur JSON, car elles sont automatiquement fournies par la plateforme. Ainsi, les champs suivants ne sont pas nécessaires et ne doivent pas être utilisés dans le compositeur JSON :
* ID utilisateur externe
* Clé API
* URL du cluster Braze
* Champs liés aux importations de jetons de notification push

## Cas d’utilisation

Par exemple, si nous voulons que le groupe d’utilisateurs soit promu aux membres de fidélité, sélectionnez **Loyalty Member (Membre de fidélité)** comme nom d’attribut, et sélectionnez `True` comme valeur de clé correspondante. Ainsi, les utilisateurs qui entrent dans cette étape de mise à jour de l’utilisateur verront leur attribut Membre VIP mis à jour vers `True`.

![][3]{: style="max-width:90%;"}

## Fonctionnalités de personnalisation

Pour stocker la propriété de l’événement déclencheur d’un Canvas comme un attribut, utilisez le modal de personnalisation pour extraire et stocker la propriété d’entrée de Canvas. Ce composant prend également en charge les fonctionnalités de personnalisation suivantes : 
* [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Propriétés d’entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)
* Logique Liquid (y compris l’[annulation de messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Plusieurs mises à jour d’attribut ou d’événement par objet


[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} 
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} 
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
[4]: {% image_buster /assets/img_archive/canvas_user_update_update.png %} 
[5]: {% image_buster /assets/img_archive/canvas_user_update_remove.png %} 
[6]: {% image_buster /assets/img_archive/canvas_user_update_test_preview.png %} 
