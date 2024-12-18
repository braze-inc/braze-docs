---
nav_title: "Groupes d’abonnement"
article_title: Groupes d’abonnement WhatsApp
page_order: 1
description: "Cet article décrit les groupes d’abonnement WhatsApp, quels états d’abonnement sont proposés et comment les groupes d’abonnement sont définis."
page_type: reference
channel:
  - WhatsApp
 
---

# Groupes d’abonnement

> Les groupes d'abonnement WhatsApp sont créés lors de l'intégration de WhatsApp à votre application via le **portail technologique des partenaires.**

## État d’abonnement WhatsApp

Il existe deux états d’abonnement pour les utilisateurs WhatsApp : `subscribed` et `unsubscribed`.

| État | Définition |
| --- | --- |
| Abonné | L’utilisateur a explicitement confirmé qu’il souhaite recevoir des messages WhatsApp de la part d’une société spécifique. Les utilisateurs peuvent souscrire en faisant mettre à jour leur état d’abonnement par l’API d’abonnement de Braze ou en déployant une stratégie d’abonnement, conformément aux directives de WhatsApp. |
| Désabonné | Soit l’utilisateur n’a pas explicitement donné son consentement pour l’abonnement, soit son statut d’abonnement a été explicitement supprimé. <br><br> Les utilisateurs désabonnés d'un groupe d'abonnement WhatsApp ne recevront plus aucun message WhatsApp provenant de l'envoi de numéros de téléphone appartenant au groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Définir les groupes d'abonnement WhatsApp des utilisateurs

- **API REST :** Les profils utilisateurs peuvent être définis par programmation par l’[endpoint `/subscription/status/set`][4] à l'aide de l'API REST de Braze.
- **SDK Web :** Les utilisateurs peuvent être ajoutés à un groupe d'abonnement par e-mail, SMS ou WhatsApp à l'aide de la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) ou [Web][11].
- **Import d'utilisateurs**: Les utilisateurs peuvent être ajoutés à des groupes d'abonnement e-mail ou SMS via l'**importation d'utilisateurs.** Lorsque vous mettez à jour le statut du groupe d’abonnement, vous devez avoir ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Reportez-vous à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) pour plus d'informations.

### Vérifier le groupe d'abonnement WhatsApp d'un utilisateur

- **Profil utilisateur :** Les profils utilisateurs individuels sont accessibles via le tableau de bord de Braze à partir de **Audience** > **Rechercher des utilisateurs**. Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Lorsque vous êtes dans le profil d'un utilisateur, sous l'onglet **Engagement**, vous pouvez voir le groupe d'abonnement WhatsApp d'un utilisateur et son statut.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez cette page sous **Utilisateurs** > **Recherche d'utilisateurs.**
{% endalert %}

- **API REST :** Le groupe d’abonnement des profils utilisateur individuels peut être consulté par l’[endpoint Lister les groupes d’abonnement de l’utilisateur][9] ou de l’[endpoint Lister le statut des groupes d’abonnement de l’utilisateur][8] en utilisant l'API REST de Braze. 

## Processus d'opt-in et d'opt-out de WhatsApp

Actuellement, les utilisateurs peuvent s'abonner et s ['opposer à l']({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) envoi de messages WhatsApp de différentes manières, notamment par [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), par le biais d'un site web, d'un fil de discussion WhatsApp, par téléphone ou en personne. Notez que des abonnements sont nécessaires.

Les mots-clés d’abonnement ne sont pas pris en charge actuellement pour le canal WhatsApp, vous aurez donc à entretenir vous-même votre liste d’utilisateurs. WhatsApp possède une approche rétroactive vis-à-vis des abonnements et des limites de débit, ce qui fait que si vos utilisateurs commencent à vous signaler et à vous bloquer, votre limite de débit sera abaissée. 

## Mise à jour du statut d'abonnement d'un utilisateur à un canvas WhatsApp {#update-subscription-status}

Quelles que soient les méthodes d'abonnement et de désabonnement que vous utilisez, vous pouvez mettre à jour l'état de l'abonnement des profils utilisateurs à l'aide de l'une des méthodes de mise à jour suivantes :

- Créez un [webhook Braze à Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) qui met à jour le statut de l'abonnement via l'API REST, comme dans l'exemple suivant :

![][1]{: style="max-width:90%;"}

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

![][2]{: style="max-width:90%;"}

{% alert note %}
La mise à jour du statut d’abonnement d'un utilisateur peut prendre jusqu'à 60 secondes.
{% endalert %}

[1]: {% image_buster /assets/img/whatsapp/whatsapp118.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}
[4]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
Il y a [11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
