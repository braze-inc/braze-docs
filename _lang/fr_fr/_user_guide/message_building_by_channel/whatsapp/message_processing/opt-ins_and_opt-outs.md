---
nav_title: Abonnements et exclusions
article_title: Abonnements et désabonnements à WhatsApp
description: "Cet article de référence couvre les différentes méthodes d’abonnement et de désabonnement de WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# Abonnements et désabonnements

> La gestion des abonnements et désabonnements de WhatsApp est cruciale, étant donné que WhatsApp surveille [l’évaluation de qualité de votre numéro de téléphone](https://www.facebook.com/business/help/896873687365001) et que de faibles notes peuvent entraîner une réduction de vos limites de messages. <br><br>L'un des moyens de créer une évaluation de qualité consiste à empêcher les utilisateurs de bloquer ou de signaler votre entreprise. Pour ce faire, vous pouvez fournir des [messages de haute qualité](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (comme la valeur des messages pour vos utilisateurs), contrôler la fréquence des messages et permettre aux clients de s'abonner pour ne plus recevoir de communications à l'avenir. <br><br>Cette page explique comment mettre en place des abonnements et des exclusions, ainsi que les différences entre les modificateurs "expression régulière" et "is".

Les abonnements peuvent provenir de sources externes ou de méthodes Braze telles que les SMS ou les messages intégrés à l’application et au navigateur. Les désabonnements peuvent être traités à l’aide de mots-clés définis dans les boutons marketing de Braze et de WhatsApp. Reportez-vous aux méthodes suivantes pour obtenir des conseils sur la configuration des options d’abonnement et de désabonnement.

#### Méthodes d’abonnement
- [Externe aux méthodes d’abonnement Braze](#external-to-braze-opt-in-methods)
  - [Liste d’abonnements créée en externe](#externally-built-opt-in-list)
  - [Message sortant dans le canal WhatsApp du support client](#outbound-message-in-customer-support-whatsapp-channel)
  - [Message WhatsApp entrant](#inbound-whatsapp-message)
- [Méthodes d’abonnement alimentées par Braze](#braze-powered-opt-in-methods)

#### Méthodes de désabonnement
- [Mots clés de désabonnement généraux](#general-opt-out-keywords)
- [Sélection de désabonnement marketing](#marketing-opt-out-selection)

## Configurez les abonnements pour votre canal WhatsApp Braze 

Pour les abonnements WhatsApp, vous devez vous conformer aux [exigences de WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Vous devrez également fournir à Braze les informations suivantes  :
- Une adresse `external_id`, un [numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) et un statut d'abonnement mis à jour pour chaque utilisateur. Pour ce faire, utilisez le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) ou l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour le numéro de téléphone et le statut de l'abonnement.

{% alert note %}
Braze a amélioré l'endpoint `/users/track` pour permettre la mise à jour du statut de l'abonnement, que vous pouvez découvrir dans [Groupes d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status). Cependant, si vous avez déjà créé des protocoles d’abonnement à l’aide de [l’endpoint `/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), vous pouvez continuer à le faire à cet endroit.
{% endalert %}

### Externe aux méthodes d’abonnement Braze

Votre application ou votre site Web (enregistrement de compte, page de paiement, paramètres de compte, terminal de carte de crédit) vers Braze.

Chaque fois que vous avez déjà un consentement marketing pour les e-mails ou les SMS, incluez une section supplémentaire pour WhatsApp. Une fois qu'un utilisateur s'est abonné, il a besoin d'une adresse `external_id`, d'un [numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) et d'une mise à jour de son statut d'abonnement. Pour ce faire, en fonction de la configuration de votre installation de Braze, vous pouvez soit exploiter l'[endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/), soit utiliser le [SDK.](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Liste d’abonnements créée en externe

Si vous avez déjà utilisé WhatsApp, vous avez peut-être déjà créé une liste d’utilisateurs abonnés conformément aux exigences WhatsApp. Dans ce cas, téléchargez un fichier CSV ou utilisez l'API avec les [informations suivantes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) dans Braze.

#### Message sortant dans le canal WhatsApp du support client

Dans votre canal de support client, effectuez un suivi des problèmes résolus avec un message automatique demandant s’il souhaite s’abonner à la communication marketing. La fonctionnalité ici dépend de la disponibilité de la fonctionnalité dans votre outil d’assistance client préféré et de l’endroit où vous conservez les informations utilisateur.

1. Fournissez un [lien de message à](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) partir de votre numéro de téléphone WhatsApp Business.
2. Fournissez des [actions de réponse rapide]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies) pour lesquelles le client répond « Oui » pour indiquer son accord
3. Configurez un déclencheur de mot-clé personnalisé.
4. Pour l’une ou l’autre de ces idées, vous devrez probablement terminer le parcours avec les éléments suivants :
	- Appelez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour ou créer un utilisateur.
	- Tirez parti de l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou utilisez le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Message WhatsApp entrant 

Demandez aux clients d’envoyer un message entrant au numéro WhatsApp.

Cela peut être configuré en tant que Canvas ou campagne, selon que vous souhaitiez ou non que l’utilisateur reçoive un message de confirmation sur le nouveau canal.

1. Créez une campagne avec le déclencheur de réception/distribution par événement d'un message entrant.
2. Créez une campagne webhook. Pour connaître un exemple de webhook, voir [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status).

{% alert tip %}
Notez que vous pouvez créer une URL ou un code QR pour rejoindre un canal WhatsApp depuis le [gestionnaire WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/), sous **Numéro de téléphone** > **Liens de messages.**<br>![WhatsApp QR code composer.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Méthodes d’abonnement alimentées par Braze 

#### Message SMS

Dans Canvas, mettez en place une campagne qui demande aux clients s'ils souhaitent s'abonner à la réception de messages WhatsApp en utilisant l'une des méthodes suivantes :
- Segment client : groupe marketing abonné en dehors des États-Unis
- Configuration du mot clé personnalisé de déclenchement

Découvrez comment mettre à jour le statut d'abonnement d'un profil utilisateur en consultant la page [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

#### Message intégré à l'application ou au navigateur

Créez un message in-app ou dans une fenêtre contextuelle dans le navigateur invitant les clients à s’abonner à l’utilisation de WhatsApp.

Utilisez le [message in-app HTML](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) avec le [« pont » JavaScript]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge) pour faire l’interface avec le SDK Braze. Assurez-vous d’utiliser l’ID du groupe d’abonnement WhatsApp. 

#### Formulaire de saisie du numéro de téléphone

Utilisez le modèle de [formulaire de capture de numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) dans l'éditeur par glisser-déposer pour les messages in-app afin de collecter les numéros de téléphone des utilisateurs et de développer vos groupes d'abonnement WhatsApp.

## Configurez les désabonnements pour votre canal WhatsApp Braze 

### Mots clés de désabonnement généraux

Vous pouvez configurer une campagne ou un Canvas qui permet aux utilisateurs qui envoient des mots spécifiques de se désinscrire des communications futures. Les Canvas peuvent être particulièrement avantageux car ils vous permettent d’inclure un message de suivi qui confirme la réussite du désabonnement. 

#### Étape 1 : Créez un canvas avec le déclencheur "Message WhatsApp entrant".
 
![Étape du canvas basée sur l'action qui permet de saisir les utilisateurs qui envoient un message WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Lorsque vous sélectionnez des mots-clés déclencheurs, incluez des mots comme « Arrêter » ou « Aucun message ». Si vous choisissez cette méthode, assurez-vous que vos clients connaissent vos mots de désabonnement. Par exemple, après avoir reçu l’abonnement initial, ajoutez une réponse de suivi comme « Pour refuser ces messages, envoyez « Arrêter » à tout moment ». 

![Étape du message pour envoyer un message entrant WhatsApp dont le corps du message est "STOP" ou "PAS DE MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Étape 2 : Mettre à jour le profil de l’utilisateur

Mettez à jour le profil de l'utilisateur en utilisant l'une des méthodes décrites dans [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

### Sélection de désabonnement marketing

Dans le créateur du modèle de message WhatsApp, vous pouvez inclure l’option de « désabonnement marketing ». Chaque fois que vous le faites, assurez-vous que le modèle est utilisé dans un Canvas avec une étape ultérieure pour un changement de groupe d’abonnement. 

1. Créez un modèle de message avec la réponse rapide « désabonnement marketing ».<br>![Modèle de message avec option de pied de page "Marketing opt-out"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Section permettant de configurer un bouton de sortie marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Créez un Canvas qui utilise ce modèle de message.<br><br>
3. Suivez les étapes de l’exemple précédent, mais avec le texte de déclenchement « STOP PROMOTIONS ».<br><br>
4. Mettez à jour le statut d'abonnement de l'utilisateur en utilisant l'une des méthodes décrites dans [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

## Mettre en place des flux de travail d'abonnement et de désabonnement

Vous pouvez configurer les flux de réponse par mot-clé "START" et "STOP" pour WhatsApp à l'aide de ces deux méthodes :

- [Étape de mise à jour de l'utilisateur](#user-update-step)
- [Campagne webhook pour déclencher une deuxième campagne WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Étape de mise à jour de l'utilisateur

L'[étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) peut ajouter le numéro de téléphone de l'utilisateur au groupe d’abonnement WhatsApp lorsque l'utilisateur envoie un mot-clé au numéro de téléphone du groupe d’abonnement.

L'étape de mise à jour de l'utilisateur permet d'éviter les conditions de concurrence, car l'utilisateur ne passera pas à l'étape suivante du canvas avant que son numéro de téléphone ne soit ajouté au groupe d'abonnement. Elle comporte également moins d'étapes à configurer que les autres méthodes, c'est pourquoi Braze recommande généralement cette méthode.

1. Créez un canvas avec l'étape du canvas basée sur l'action **Envoyer un message entrant WhatsApp**. Sélectionnez **Localisation du corps du message** et entrez « DÉMARRER » pour **EST**.

{% alert important %}
Pour les messages « ARRÊTER », inversez l'étape du message confirmant le désabonnement et l'étape de mise à jour de l'utilisateur. Si vous ne le faites pas, l'utilisateur sera d'abord exclu du groupe d'abonnement, puis ne pourra pas recevoir le message de confirmation.
{% endalert %}

![Une étape d'envoi de messages WhatsApp dont le corps du message est "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Dans le canvas, créez une étape **Paramétrer la mise à jour utilisateur** et pour **Action**, sélectionnez **Éditeur JSON avancé**. <br><br>![Utilisateur Mettre à jour l'étape avec une action de "Editeur JSON avancé".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\. Remplissez l'**objet User Update** avec la charge utile JSON suivante, en remplaçant `XXXXXXXXXXX` par l'ID de votre groupe d'abonnement :

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4\. Ajoutez une étape de message WhatsApp ultérieure. <br><br>![Étape de mise à jour de l'utilisateur dans un canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considérations

La mise à jour peut s'effectuer à des vitesses variables car Braze regroupe les demandes d'[étapes de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

### Campagne webhook pour déclencher une deuxième campagne WhatsApp

Une campagne Webhook peut déclencher l'entrée dans une deuxième campagne après avoir ajouté le numéro de téléphone de l'utilisateur au groupe d'abonnement WhatsApp lorsque l'utilisateur envoie un mot-clé au numéro de téléphone du groupe d'abonnement.

{% alert important %}
Vous ne devez pas utiliser cette méthode pour les messages STOP. Le message de confirmation sera envoyé avant que l'utilisateur ne soit supprimé du groupe d'abonnement, de sorte que vous puissiez utiliser l'une des deux autres étapes.
{% endalert %}

1. Créez une campagne ou un canvas avec une étape **Envoyer un message WhatsApp entrant** basée sur un événement. Sélectionnez **Localisation du corps du message** et entrez « DÉMARRER » pour **EST**.

![Étape d'envoi de messages WhatsApp dont le corps du message est "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. Dans la campagne ou le canvas, créez une étape Message de webhook et changez le **Corps de la demande** sur **Texte brut**.

![Envoi de messages pour un webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. Saisissez l'[URL de l'endpoint]({{site.baseurl}}/api/basics/) du client dans l'**URL du webhook**, suivie du lien de l'endpoint `campaigns/trigger/send`. Par exemple, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Champ de l'URL du webhook dans la section "Composer un webhook".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Dans le texte brut, saisissez la charge utile JSON suivante et remplacez `XXXXXXXXXXX` par l'ID de votre groupe d'abonnement. Vous devrez remplacer le site `campaign_id` après avoir créé votre deuxième campagne.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5\. Créez une campagne WhatsApp (votre deuxième campagne) et définissez le déclencheur sur API. Veillez à copier cet `campaign_id` dans la charge utile JSON de votre première campagne.

#### Considérations

- Les mises à jour d'attributs à partir de la charge utile JSON du déclencheur de l'API du canvas ne sont pas encore prises en charge, de sorte que vous ne pouvez déclencher une campagne WhatsApp que pour le message de réponse WhatsApp (comme à l'étape 2).
- Un modèle WhatsApp doit être approuvé pour pouvoir l'envoyer en tant que message de réponse. En effet, pour obtenir une réponse rapide, il faut que le déclencheur de l'envoi du message soit situé dans la même campagne ou le même Canvas. Si vous utilisez une [étape de mise à jour de l'utilisateur](#user-update-step), vous pouvez envoyer un message de réponse rapide sans l'approbation de Meta.

## Comprendre la différence entre les modificateurs "expression régulière" et "is".

Dans ce tableau, `STOP` est utilisé comme exemple de déclencheur pour démontrer le fonctionnement des modificateurs.

| Modificateur | Mot déclencheur | Action |
| --- | --- | --- |
| `Is` | `STOP` | Capte toute utilisation du mot "stop" dans son intégralité, quel que soit le cas de figure. Par exemple, il attrape "stop" mais pas "arrêtez s'il vous plaît". |
| `Matches regex` | `STOP` | Capte toute utilisation de "STOP" dans ce cas. Par exemple, il attrape "stop" mais pas "PLEASE STOP". |
| `Matches regex` | `(?i)STOP(?-i)` | Capture toute utilisation de "STOP" dans tous les cas. Par exemple, cela permet d'attraper "stop", "veuillez arrêter" et "n'arrêtez jamais de m'envoyer des messages". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

