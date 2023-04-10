---
nav_title: Abonnements et désabonnements
article_title: Abonnements et désabonnements WhatsApp
description: "Cet article de référence couvre les différentes méthodes d’abonnement et de désabonnement de WhatsApp."
page_type: partner
search_tag: Partenaire
page_order: 5

---

# Abonnements et désabonnements

## Aperçu

La gestion des abonnements et désabonnements de WhatsApp est cruciale, étant donné que WhatsApp surveille l’[évaluation de qualité de votre numéro de téléphone](https://www.facebook.com/business/help/896873687365001) et que de faibles notes peuvent entraîner une réduction de vos limites de messages. Une façon de garantir une évaluation de haute qualité est d’empêcher les utilisateurs de bloquer ou de signaler votre entreprise. Cela peut être fait en fournissant des [communications de haute qualité](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (c.-à-d., de la valeur pour vos utilisateurs), en contrôlant la fréquence des messages et en permettant aux clients de refuser de recevoir des communications futures. 

Les abonnements peuvent provenir de sources externes ou de méthodes Braze telles que les SMS ou les messages dans l’application et le navigateur. Les désabonnements peuvent être traités à l’aide de mots-clés définis dans les boutons marketing de Braze et de WhatsApp. Reportez-vous aux méthodes suivantes pour obtenir des conseils sur la configuration des options d’abonnement et de désabonnement. 

#### Méthodes d’abonnement
- [Externe aux méthodes d’abonnement Braze ](#external-to-braze-opt-in-methods)
  - [Liste d’abonnements créée en externe](#externally-built-opt-in-list)
  - [Message sortant dans le canal WhatsApp du support client](#outbound-message-in-customer-support-whatsapp-channel)
  - [Message WhatsApp entrant](#inbound-whatsapp-message)
- [Méthodes d’abonnement alimentées par Braze](#braze-powered-opt-in-methods)

#### Méthodes de désabonnement
- [Mots clés de désabonnement généraux](#general-opt-out-keywords)
- [Sélection de désabonnement marketing](#marketing-opt-out-selection)

## Configurez les abonnements pour votre canal WhatsApp Braze 

Pour les abonnements WhatsApp, vous devez vous conformer aux [exigences de WhatsApp](https://business.facebook.com/business/help/718961699259789#). Vous devrez également fournir à Braze les informations suivantes  :
- Un `external_id`, un numéro de téléphone et un statut d’abonnement mis à jour pour chaque utilisateur. Pour ce faire, utilisez le [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) ou l’endpoint [`/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) pour mettre à jour le numéro de téléphone et le statut de l’abonnement. 

{% alert note %}
Veuillez noter que Braze a récemment apporté une amélioration à l’endpoint `/users/track` qui permet de mettre à jour les statuts d’abonnement. Cependant, si vous avez déjà créé des protocoles d’abonnement à l’aide du [`/subscription/status/set endpoint`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), vous pouvez continuer à le faire à cet endroit.
{% endalert %}

### Externe aux méthodes d’abonnement Braze 

Votre application ou votre site Web (enregistrement de compte, page de paiement, paramètres de compte, terminal de carte de crédit) vers Braze.

Chaque fois que vous avez déjà un consentement marketing pour les e-mails ou les SMS, incluez une section supplémentaire pour WhatsApp. Une fois qu’un utilisateur s’est abonné, il a besoin d’un `external_id`, d’un numéro de téléphone et d’un statut d’abonnement mis à jour. Pour ce faire, en fonction de la configuration de votre installation de Braze, exploitez l’endpoint [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou utilisez le [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287).

#### Liste d’abonnements créée en externe

Si vous avez déjà utilisé WhatsApp, vous avez peut-être déjà créé une liste d’utilisateurs abonnés conformément aux exigences WhatsApp. Dans ce cas, chargez un fichier CSV ou utilisez l’API avec les [informations suivantes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) dans Braze.

#### Message sortant dans le canal WhatsApp du support client

Dans votre canal de support client, effectuez un suivi des problèmes résolus avec un message automatique demandant s’il souhaite s’abonner à la communication marketing. La fonctionnalité ici dépend de la disponibilité de la fonctionnalité dans votre outil d’assistance client préféré et de l’endroit où vous conservez les informations utilisateur.

1. Fournissez un [lien de message] à partir de votre numéro de téléphone WhatsApp Business.
2. Fournissez des [actions de réponse rapide]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/quick_replies/) pour lesquelles le client répond « Oui » pour indiquer son accord
3. Configurez un déclencheur de mot-clé personnalisé.
4. Pour l’une ou l’autre de ces idées, vous devrez probablement terminer le parcours avec les éléments suivants :
	- Appelez l’endpoint [/users/track](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) pour mettre à jour ou créer un utilisateur 
	- Tirez parti de l’endpoint [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou utilisez le [SDK](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) 

#### Message WhatsApp entrant 

Demandez aux clients d’envoyer un message entrant au numéro WhatsApp.

Cela peut être configuré en tant que Canvas ou campagne, selon que vous souhaitiez ou non que l’utilisateur reçoive un message de confirmation sur le nouveau canal.

1. Créez une campagne webhook<br>**Exemple de méthode [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) :**<br>![][2]<br><br>![][3]<br><br>
2. Créez une campagne avec le déclencheur de livraison par événement d’un message entrant<br>![][1]

{% alert tip %}
Notez que vous pouvez créer une URL ou un code QR pour joindre un canal WhatsApp à partir du [gestionnaire WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/) dans **Numéro de téléphone** > **Liens de message**.<br>![]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Méthodes d’abonnement alimentées par Braze 

#### Message SMS

Dans Canvas, configurez une campagne qui demande aux clients s’ils souhaitent s’abonner pour recevoir des messages WhatsApp. Par exemple :
- Segment client : groupe marketing abonné en dehors des États-Unis
- Configuration du mot clé personnalisé de déclenchement
- Méthode de mise à jour :
	- [Webhook Braze à Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) qui met à jour le statut de l’abonnement via l’API Rest
	- Mettez à jour le profil utilisateur via l’éditeur JSON avancé avec le modèle suivant : 

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

#### Message dans l'application et dans le navigateur

Créez un message in-app ou dans une fenêtre contextuelle dans le navigateur invitant les clients à s’abonner à l’utilisation de WhatsApp.

Utilisez le [message HTML in-app](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) avec le [« pont » JavaScript]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages/#javascript-bridge) pour l’interface avec Braze SDK. Assurez-vous d’utiliser l’ID du groupe d’abonnement WhatsApp. 

## Configurez les désabonnements pour votre canal WhatsApp Braze 

### Mots clés de désabonnement généraux

Vous pouvez configurer une campagne ou un Canvas qui permet aux utilisateurs qui envoient des mots spécifiques de se désinscrire des communications futures. Les Canvas peuvent être particulièrement avantageux car ils vous permettent d’inclure un message de suivi qui confirme la réussite du désabonnement. 

#### Étape 1 : Créez un Canvas avec le déclencheur « Message WhatsApp entrant »"
 
![][6]{: style="max-width:85%;"}

Lorsque vous sélectionnez des mots-clés déclencheurs, incluez des mots comme « Arrêter » ou « Aucun message ». Si vous choisissez cette méthode, assurez-vous que vos clients connaissent vos mots de désabonnement. Par exemple, après avoir reçu l’abonnement initial, ajoutez une réponse de suivi comme « Pour refuser ces messages, envoyez « Arrêter » à tout moment ». 

![][7]

#### Étape 2 : Mettre à jour le profil de l’utilisateur

Mettez à jour le profil de l’utilisateur en utilisant l’éditeur JSON avancé ou en créant un [webhook Braze à Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know). 

1. À l’aide de l’éditeur JSON avancé de l’action Canvas « Mettre à jour le profil utilisateur », utilisez le modèle suivant :

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

2. Créer un [webhook Braze à Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know) qui met à jour le statut d’abonnement de l’utilisateur sur « Désabonné ». Un exemple similaire peut être trouvé ci-dessous :<br><br>![][8]<br><br>![][9]<br><br>Vous pouvez éventuellement inclure un message de suivi qui indique à l’utilisateur qu’il a été désabonné du canal. Assurez-vous que cela se produit avant l’étape de désabonnement, car vous ne pourrez plus envoyer de message à l’utilisateur. 

### Sélection de désabonnement marketing

Dans le créateur du modèle de message WhatsApp, vous pouvez inclure l’option de « désabonnement marketing ». Chaque fois que vous le faites, assurez-vous que le modèle est utilisé dans un Canvas avec une étape ultérieure pour un changement de groupe d’abonnement. 

1. Créez un modèle de message avec la réponse rapide « désabonnement marketing ».<br>![][11]<br><br>![][12]<br><br>
2. Créez un Canvas qui utilise ce modèle de message.<br><br>
3. Suivez les étapes de l’exemple précédent, mais avec le texte de déclenchement « STOP PROMOTIONS ».<br><br>
4. Mettre à jour le statut d’abonnement de l’utilisateur.
  - Créez un [webhook Braze à Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks#things-to-know) qui met à jour le statut d’abonnement de l’utilisateur sur « Désabonné »"
  - Utilisez l’éditeur JSON avancé de Canvas « Mettre à jour le profil utilisateur » avec le modèle suivant :

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
Notez que Braze prévoit de traiter automatiquement ces désabonnements marketing au cours de l’année prochaine, mais nécessite un processus manuel pour les configurer. 
 
[1]: {% image_buster /assets/img/whatsapp/whatsapp111.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp112.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp113.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp114.png %} 
[5]: {% image_buster /assets/img/whatsapp/whatsapp115.png %} 
[6]: {% image_buster /assets/img/whatsapp/whatsapp116.png %} 
[7]: {% image_buster /assets/img/whatsapp/whatsapp117.png %} 
[8]: {% image_buster /assets/img/whatsapp/whatsapp118.png %} 
[9]: {% image_buster /assets/img/whatsapp/whatsapp119.png %} 
[10]: {% image_buster /assets/img/whatsapp/whatsapp120.png %} 
[11]: {% image_buster /assets/img/whatsapp/whatsapp121.png %} 
[12]: {% image_buster /assets/img/whatsapp/whatsapp122.png %} 
