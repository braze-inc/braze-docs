---
nav_title: Abonnements et exclusions
article_title: Abonnements et désabonnements à WhatsApp
description: "Cet article de référence traite des différentes méthodes d'abonnement et de désabonnement à WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# L'abonnement et l'exclusion

> La gestion des inscriptions et des abonnements à WhatsApp est cruciale, car WhatsApp surveille l'[évaluation de la qualité de](https://www.facebook.com/business/help/896873687365001) votre [numéro de téléphone](https://www.facebook.com/business/help/896873687365001), et une faible évaluation peut entraîner une réduction de vos limites de messages. <br><br>L'un des moyens de créer une évaluation de qualité consiste à empêcher les utilisateurs de bloquer ou de signaler votre entreprise. Pour ce faire, vous pouvez fournir des [messages de haute qualité](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (comme la valeur des messages pour vos utilisateurs), contrôler la fréquence des messages et permettre aux clients de s'abonner pour ne plus recevoir de communications à l'avenir. <br><br>Cette page explique comment mettre en place des abonnements et des exclusions, ainsi que les différences entre les modificateurs "expression régulière" et "is".

Les opt-ins peuvent provenir de sources externes ou de méthodes Braze, comme les SMS ou les messages in-app et in-browser. Les exclusions peuvent être traitées à l'aide de mots-clés définis dans Braze et de boutons de marketing WhatsApp. Référez-vous aux méthodes suivantes pour obtenir des conseils sur la mise en place d'un système d'abonnement et de désabonnement.

#### Méthodes d'abonnement
- [Méthodes d'abonnement externes à Braze](#external-to-braze-opt-in-methods)
  - [Liste d'abonnés créée en externe](#externally-built-opt-in-list)
  - [Message sortant dans le canal de communication WhatsApp de l'assistance à la clientèle.](#outbound-message-in-customer-support-whatsapp-channel)
  - [Envoi de messages par WhatsApp](#inbound-whatsapp-message)
- [Méthodes d'abonnement à la puissance de Braze](#braze-powered-opt-in-methods)

#### Méthodes d'abonnement
- [Mots clés généraux pour l'abonnement](#general-opt-out-keywords)
- [Sélection de l'option de refus du marketeur (opt-out)](#marketing-opt-out-selection)

## Mettre en place des abonnements pour votre canal WhatsApp de Braze

Pour les abonnements WhatsApp, vous devez vous conformer aux [exigences de WhatsApp.](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) Vous devrez également fournir à Braze les informations suivantes :
- Une adresse `external_id`, un [numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) et un statut d'abonnement mis à jour pour chaque utilisateur. Pour ce faire, vous pouvez utiliser le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) ou l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour le numéro de téléphone et l'état de l'abonnement.

{% alert note %}
Braze a publié une amélioration de l'endpoint `/users/track` qui permet de mettre à jour le statut de l'abonnement que vous pouvez découvrir dans [Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status). Toutefois, si vous avez déjà créé des protocoles d'abonnement en utilisant l'[endpoint`/v2/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/), vous pouvez continuer à le faire à cet endroit.
{% endalert %}

### Méthodes d'abonnement externes à Braze

Votre app ou site web (enregistrement du compte, page de paiement, paramètres du compte, terminal de carte de crédit) à Braze.

Si vous disposez déjà d'un consentement marketing pour l'e-mail ou l'envoi de SMS, ajoutez une section supplémentaire pour WhatsApp. Une fois qu'un utilisateur s'est abonné, il a besoin d'une adresse `external_id`, d'un [numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) et d'une mise à jour de son statut d'abonnement. Pour ce faire, en fonction de la configuration de votre installation de Braze, vous pouvez soit exploiter l'[endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/), soit utiliser le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Liste d'abonnés créée en externe

Si vous avez déjà utilisé WhatsApp, vous avez peut-être déjà créé une liste d'utilisateurs avec des abonnements conformes aux exigences de WhatsApp. Dans ce cas, téléchargez un fichier CSV ou utilisez l'API avec les [informations suivantes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) dans Braze.

#### Message sortant dans le canal de communication WhatsApp de l'assistance à la clientèle.

Dans votre canal d'assistance à la clientèle, assurez le suivi des problèmes résolus à l'aide d'un message automatique demandant aux clients s'ils souhaitent s'abonner à des envois de messages marketing. La fonctionnalité dépend ici de la disponibilité des fonctionnalités dans l'outil d'assistance à la clientèle que vous avez choisi et de l'endroit où vous conservez les informations sur les utilisateurs.

1. Fournissez un [lien de message à](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) partir de votre numéro de téléphone WhatsApp Business.
2. Fournir des [actions de réponse rapide]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies) lorsque le client répond "Oui" pour indiquer qu'il est abonné.
3. Mettez en place un déclencheur de mots-clés personnalisé.
4. Pour l'une ou l'autre de ces idées, vous devrez probablement terminer le chemin par ce qui suit :
	- Appelez l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour ou créer un utilisateur.
	- Tirez parti de l'[endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) ou utilisez le [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Envoi de messages par WhatsApp 

Demandez aux clients d'envoyer un message entrant au numéro WhatsApp.

Cette opération peut être implémentée en tant que Canvas ou campagne, selon que vous souhaitez ou non que l'utilisateur reçoive un message de confirmation sur le nouveau canal.

1. Créez une campagne avec le déclencheur de réception/distribution par événement d'un message entrant.
2. Créez une campagne webhook. Pour un exemple de webhook, voir [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status).

{% alert tip %}
Notez que vous pouvez créer une URL ou un code QR pour rejoindre un canal WhatsApp depuis le [gestionnaire WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/), sous **Numéro de téléphone** > **Liens de messages.**<br>!Composez le code QR de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Méthodes d'abonnement à la puissance de Braze 

#### Message SMS

Dans Canvas, mettez en place une campagne qui demande aux clients s'ils souhaitent s'abonner à la réception de messages WhatsApp en utilisant l'une des méthodes suivantes :
- Segmentation de la clientèle : groupe de marketeurs abonnés en dehors des États-Unis
- Configuration personnalisée des déclencheurs de mots-clés

Découvrez comment mettre à jour le statut du [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status) d'un profil utilisateur en consultant la page [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

#### Message in-app ou in-browser

Créez un message in-app ou un pop-up dans le navigateur invitant les clients à s'abonner à l'utilisation de WhatsApp.

Utilisez un [message in-app HTML](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) avec un ["pont" JavaScript]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge) pour interfacer avec le SDK de Braze. Veillez à utiliser l'ID du groupe d'abonnement WhatsApp. 

#### Formulaire de saisie du numéro de téléphone

Utilisez le modèle de [formulaire de capture de numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) dans l'éditeur par glisser-déposer pour les messages in-app afin de collecter les numéros de téléphone des utilisateurs et de développer vos groupes d'abonnement WhatsApp.

## Configurer les abonnements pour votre canal WhatsApp de Braze

### Mots clés généraux pour l'abonnement

Vous pouvez mettre en place une campagne ou un canvas qui permet aux utilisateurs qui envoient des messages avec des mots particuliers de se désabonner des futurs messages. Les canevas peuvent être particulièrement utiles car ils vous permettent d'inclure un message de suivi qui confirme la réussite de l'abonnement. 

#### Étape 1 : Créez un canvas avec le déclencheur "Message WhatsApp entrant".
 
!étape du canvas basée sur l'action qui permet de saisir les utilisateurs qui envoient un message entrant WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Lors de la sélection des mots-clés déclencheurs, incluez des mots tels que "Stop" ou "Pas de message". Si vous optez pour cette méthode, veillez à ce que vos clients connaissent vos modalités d'abonnement. Par exemple, après avoir reçu l'abonnement initial, incluez une réponse de suivi telle que "Pour ne plus recevoir ces messages, envoyez le message "Stop" à tout moment." 

\![Étape du message pour envoyer un message entrant WhatsApp dont le corps du message est "STOP" ou "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Étape 2 : Mise à jour du profil utilisateur

Mettez à jour le profil de l'utilisateur en utilisant l'une des méthodes décrites dans [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

### Sélection de l'option de refus du marketeur (opt-out)

Dans le créateur de modèles de messages WhatsApp, vous pouvez inclure l'option "opt-out marketing". Chaque fois que vous incluez ceci, assurez-vous que le modèle est utilisé dans un canvas avec une étape du canvas pour un changement de groupe d'abonnement. 

1. Créez un modèle de message avec la réponse rapide "opt-out marketing".<br>\![Modèle de message avec une option de pied de page "Marketing opt-out".]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>\![Section permettant de configurer un bouton de marketing oopt-out.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Créez un canvas qui utilise ce modèle de message.<br><br>
3. Suivez les étapes de l'exemple précédent mais avec le texte du déclencheur "ARRÊTEZ LES PROMOTIONS".<br><br>
4. Mettez à jour le statut du groupe [d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status) de l'utilisateur en utilisant l'une des méthodes décrites dans [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status).

## Mettre en place des flux de travail d'abonnement et de désabonnement

Vous pouvez configurer les flux de réponse par mot-clé "START" et "STOP" pour WhatsApp à l'aide de ces deux méthodes :

- [Étape de mise à jour de l'utilisateur](#user-update-step)
- [Campagne webhook pour déclencher une deuxième campagne WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Étape de mise à jour de l'utilisateur

L' [étape de mise à jour de l']({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) utilisateur peut ajouter le numéro de téléphone de l'utilisateur au subscription groups WhatsApp lorsque l'utilisateur envoie un mot-clé au numéro de téléphone du subscription groups.

L'étape de mise à jour de l'utilisateur permet d'éviter les conditions de concurrence, car l'utilisateur ne passera pas à l'étape suivante du canvas avant que son numéro de téléphone ne soit ajouté au groupe d'abonnement. Elle comporte également moins d'étapes à mettre en place que les autres méthodes, c'est pourquoi Braze recommande généralement cette méthode.

1. Créez un canvas avec l'étape du canvas basée sur l'action **Envoyer un message entrant WhatsApp**. Sélectionnez **Où le corps du message** et entrez "START" pour **Is.**

{% alert important %}
Pour les envois "STOP", inversez l'étape du message confirmant l'abonnement et l'étape de la mise à jour de l'utilisateur. Si vous ne le faites pas, l'utilisateur sera d'abord exclu du groupe d'abonnement, puis ne pourra pas recevoir le message de confirmation.
{% endalert %}

\![Une étape du message WhatsApp dont le corps du message est "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Dans le canvas, créez une étape **Set Up User Update** et pour **Action** sélectionnez **Advanced JSON Editor.** <br><br>\![Étape de mise à jour de l'utilisateur avec une action de "Editeur JSON avancé".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
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
4\. Ajoutez une étape ultérieure au message WhatsApp. <br><br>!Étape de mise à jour de l'utilisateur dans un canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considérations

La mise à jour peut s'effectuer à des vitesses variables car Braze regroupe les demandes d'[étapes de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/).

### Campagne webhook pour déclencher une deuxième campagne WhatsApp

Une campagne Webhook peut déclencher l'entrée dans une deuxième campagne après avoir ajouté le numéro de téléphone de l'utilisateur au groupe d'abonnement WhatsApp lorsque l'utilisateur envoie un mot-clé au numéro de téléphone du groupe d'abonnement.

{% alert important %}
Vous ne devez pas utiliser cette méthode pour les messages STOP. Le message de confirmation sera envoyé avant que l'utilisateur ne soit supprimé du groupe d'abonnement, de sorte que vous puissiez utiliser l'une des deux autres étapes.
{% endalert %}

1. Créez une campagne ou un canvas avec une étape du canvas basée sur l'action **Envoyez un message WhatsApp Inbound**. Sélectionnez **Où le corps du message** et entrez "START" pour **Is.**

\![Étape du message WhatsApp dont le corps du message est "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. Dans la campagne ou le canvas, créez une étape Webhook Message, et changez le **Request Body** en **Raw Text**.

\![Message étape pour un webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. Saisissez l' [URL de]({{site.baseurl}}/api/basics/) l' [endpoint du]({{site.baseurl}}/api/basics/) personnalisé dans l' **URL du webhook**, suivi du lien de l'endpoint `campaigns/trigger/send`. Par exemple, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

! [champ Webhook URL dans la section "Compose Webhook".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Dans le texte brut, entrez la charge utile JSON suivante et remplacez `XXXXXXXXXXX` par votre ID de groupe d'abonnement. Vous devrez remplacer le site `campaign_id` après avoir créé votre deuxième campagne.

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
5\. Créez une campagne WhatsApp (votre deuxième campagne) et définissez le déclencheur sur API. Veillez à copier cette adresse `campaign_id` dans la charge utile JSON de votre première campagne.

#### Considérations

- Les mises à jour d'attributs à partir de la charge utile JSON du déclencheur de l'API Canvas ne sont pas encore prises en charge, de sorte que vous ne pouvez déclencher une campagne WhatsApp que pour le message de réponse WhatsApp (comme à l'étape 2).
- Un modèle WhatsApp doit être approuvé pour pouvoir l'envoyer en tant que message de réponse. En effet, pour obtenir une réponse rapide, il faut que le déclencheur de l'envoi du message soit situé dans la même campagne ou le même Canvas. Si vous utilisez une [étape de mise à jour de l'utilisateur](#user-update-step), vous pouvez envoyer un message de réponse rapide sans l'approbation de Meta.

## Comprendre la différence entre les modificateurs "expression régulière" et "is".

Dans ce tableau, `STOP` est utilisé comme exemple de déclencheur pour démontrer le fonctionnement des modificateurs.

| Modificateur | Mot déclencheur | Action |
| --- | --- | --- |
| `Is` | `STOP` | Capte toute utilisation du mot "stop" dans son intégralité, quel que soit le cas de figure. Par exemple, il attrape "stop" mais pas "arrêtez s'il vous plaît". |
| `Matches regex` | `STOP` | Il attrape toute utilisation de "STOP" dans ce cas précis. Par exemple, il attrape "STOP" et "VEUILLEZ ARRÊTER", mais pas "stop". |
| `Matches regex` | `(?i)STOP(?-i)` | Capture toute utilisation de "STOP" dans tous les cas. Par exemple, cela permet d'attraper "stop", "veuillez arrêter" et "n'arrêtez jamais de m'envoyer des messages". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

