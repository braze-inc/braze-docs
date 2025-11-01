---
nav_title: "Groupes d'abonnement"
article_title: "Groupes d'abonnement WhatsApp"
page_order: 1
description: "Cet article présente les groupes d'abonnement WhatsApp, les états d'abonnement proposés et la définition des groupes d'abonnement."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp
 
---

# Groupes d'abonnement

> Les groupes d'abonnement WhatsApp sont créés lors de l'intégration de WhatsApp à votre application via le **portail technologique des partenaires.**

## États de l'abonnement à WhatsApp

Il existe deux types d'abonnement pour les utilisateurs de WhatsApp : `subscribed` et `unsubscribed`.

| État | Définition |
| --- | --- |
| Abonné | L'utilisateur a explicitement confirmé qu'il souhaitait recevoir des messages WhatsApp d'une entreprise spécifique. Les utilisateurs peuvent être abonnés en voyant l'état de leur abonnement mis à jour via l'API d'abonnement de Braze ou en déployant une stratégie d'opt-in, conformément aux directives de WhatsApp. |
| Désabonné | L'utilisateur n'a pas explicitement donné son accord pour l'abonnement ou son statut d'abonné a été explicitement supprimé. <br><br> Les utilisateurs désabonnés d'un groupe d'abonnement WhatsApp ne recevront plus aucun message WhatsApp provenant de l'envoi de numéros de téléphone appartenant au groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Définir les groupes d'abonnement WhatsApp des utilisateurs

- **API REST :** Les profils utilisateurs peuvent être définis de manière programmatique par l'[endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) à l'aide de l'API REST de Braze.
- **SDK Web :** Les utilisateurs peuvent être ajoutés à un groupe d'abonnement par e-mail, SMS ou WhatsApp à l'aide de la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web.](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)
- **Import d'utilisateurs**: Les utilisateurs peuvent être ajoutés à des groupes d'abonnement e-mail ou SMS via l'**importation d'utilisateurs.** Lors de la mise à jour du statut du groupe d'abonnement, vous devez avoir ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Reportez-vous à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) pour plus d'informations.

### Vérifier le groupe d'abonnement WhatsApp d'un utilisateur

- **Profil utilisateur :** Les profils utilisateurs individuels sont accessibles via le tableau de bord de Braze à partir de **Audience** > Recherche d'utilisateurs. Vous pouvez y rechercher des profils utilisateurs par e-mail, numéro de téléphone ou ID externe. Lorsque vous êtes dans le profil d'un utilisateur, sous l'onglet **Engagement**, vous pouvez voir le groupe d'abonnement WhatsApp d'un utilisateur et son statut.

- **API REST :** Les profils d'utilisateurs individuels et les groupes d'abonnement peuvent être consultés à l'aide de l' [endpoint List user's subscription groups]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou [List user's subscription group status en]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) utilisant l'API REST de Braze. 

## Processus d'opt-in et d'opt-out de WhatsApp

Actuellement, les utilisateurs peuvent s'abonner et s ['opposer à l']({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) envoi de messages WhatsApp de différentes manières, notamment par [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), par le biais d'un site web, d'un fil de discussion WhatsApp, par téléphone ou en personne. Notez que des abonnements sont nécessaires.

Les mots-clés avec abonnement ne sont actuellement pas pris en charge pour le canal WhatsApp, il vous appartiendra donc de tenir à jour une liste d'utilisateurs. WhatsApp a une approche rétrospective des abonnements et des limites de débit : si les utilisateurs commencent à vous signaler ou à vous bloquer, votre limite de débit sera abaissée. 

## Mise à jour de l'état de l'abonnement d'un utilisateur à un WhatsApp Canvas {#update-subscription-status}

Quelles que soient les méthodes d'abonnement et de désabonnement que vous utilisez, vous pouvez mettre à jour l'état de l'abonnement des profils utilisateurs à l'aide de l'une des méthodes de mise à jour suivantes :

- Créez un [webhook Braze à Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) qui met à jour le statut de l'abonnement via l'API REST, comme dans l'exemple suivant :

\![Webhook composer avec un message en utilisant la méthode POST.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Pour éviter les conditions de concurrence, tout envoi de messages de suivi après le webhook doit être contenu dans un second Canvas qui est déclenché par les résultats du premier Canvas (par exemple, un utilisateur est entré dans une variation du Canvas et fait partie d'un groupe d'abonnement WhatsApp).

- Utilisez l'éditeur JSON avancé pour mettre à jour le profil utilisateur avec le modèle suivant : 

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

! l'étape de mise à jour de l'utilisateur avec une étape d'éditeur JSON avancé.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
La mise à jour de l'abonnement d'un utilisateur peut prendre jusqu'à 60 secondes.
{% endalert %}

