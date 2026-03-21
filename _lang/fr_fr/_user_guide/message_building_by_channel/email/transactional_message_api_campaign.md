---
nav_title: Campagnes d'e-mails transactionnels
article_title: Campagnes d'e-mails transactionnels
page_order: 10

description: "Le présent article de référence explique comment créer et configurer une nouvelle campagne Braze d'e-mails transactionnels."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Campagnes d'e-mails transactionnels

> Les e-mails transactionnels de Braze sont envoyés pour faciliter une transaction convenue entre un expéditeur et le destinataire. Cet article de référence explique comment créer une campagne d'e-mails transactionnels dans le tableau de bord de Braze et générer un `campaign_id` à inclure dans vos appels API pour notre [endpoint `/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
L'e-mail transactionnel de Braze n'est disponible que dans le cadre de certaines offres Braze. Contactez votre Customer Success Manager Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) pour plus de détails.
{% endalert %}

Le type de campagne d'e-mail transactionnel est spécialement conçu pour l'envoi d'e-mails automatisés et non promotionnels destinés à faciliter une transaction convenue entre vous et vos clients. Cela inclut des informations telles que :

- Les confirmations de commande
- Les réinitialisations de mot de passe
- Les alertes de facturation
- Les alertes d'expédition

En bref, vous pouvez utiliser les e-mails transactionnels pour envoyer à un seul utilisateur des notifications critiques provenant de votre service, lorsque la rapidité est primordiale. 

{% alert important %}
Les e-mails transactionnels diffèrent des campagnes transactionnelles, qui peuvent être utilisées pour cibler vos utilisateurs sans coûts supplémentaires. Les campagnes transactionnelles peuvent par exemple inclure des messages envoyés après qu'un utilisateur a ajouté un article à son panier. Pour plus d'informations, consultez les [options de ciblage de l'audience]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/).
{% endalert %}

{% alert note %}
Les envois d'e-mails transactionnels via l'API prennent en charge l'archivage des messages. Si l'archivage des messages est activé pour les e-mails dans votre espace de travail, Braze enregistre une copie rendue de chaque e-mail transactionnel envoyé. Pour en savoir plus, consultez la section [Archivage des messages]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving/).
{% endalert %}

## Étape 1 : Créer une nouvelle campagne

Pour créer une nouvelle campagne d'e-mails transactionnels, créez une campagne et sélectionnez **E-mail transactionnel** comme canal de communication.

![Liste déroulante de création de campagne avec l'option e-mail transactionnel en surbrillance.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez maintenant passer à la configuration de votre campagne d'e-mails transactionnels.

## Étape 2 : Configurer votre campagne

Le flux de création des campagnes d'e-mails transactionnels est simplifié par rapport à celui d'une [campagne d'e-mails standard]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) afin de garantir que vos e-mails transactionnels critiques puissent atteindre tous les utilisateurs.

Vous remarquerez donc que plusieurs paramètres que vous connaissez peut-être d'autres types de campagnes Braze ne sont pas requis pour ce type de campagne :

- L'étape de **réception/distribution** a été simplifiée : les options de planification ont été retirées. Les e-mails transactionnels sont toujours déclenchés via l'API REST de Braze à l'aide de l'ID de campagne indiqué sur la page de **réception/distribution**. D'autres paramètres, tels que les contrôles de rééligibilité et les paramètres de limite de fréquence, ont également été supprimés afin de garantir que tous les utilisateurs sont joignables pour ces alertes transactionnelles critiques lorsque votre service déclenche une demande d'envoi.
- L'étape des **audiences ciblées** a été supprimée. Étant donné que les e-mails transactionnels considèrent l'intégralité de votre base d'utilisateurs comme éligible (y compris les utilisateurs désabonnés), il n'est pas nécessaire de spécifier des filtres ou des segments. Par conséquent, si vous souhaitez appliquer une logique pour déterminer qui doit recevoir ce message, nous vous recommandons de le faire avant de décider si la requête API doit être envoyée à Braze pour déclencher le message à un utilisateur spécifique.
- L'étape des **conversions** a été supprimée. Pour le moment, les e-mails transactionnels ne prennent pas en charge le suivi des événements de conversion.

![Flux Rédiger, Réception/distribution et Confirmer pour créer une campagne d'e-mails transactionnels.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Pour configurer votre campagne d'e-mails transactionnels, procédez comme suit :

1. Ajoutez un nom descriptif afin de pouvoir retrouver les résultats sur votre page **Campagnes** après l'envoi de vos messages.
2. Rédigez votre e-mail ou sélectionnez un modèle.
3. Notez votre `campaign_id`. Après avoir enregistré votre campagne API, vous devez inclure les champs `campaign_id` générés dans votre requête API, comme indiqué dans l'article sur l'[endpoint de l'e-mail transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Cliquez sur **Enregistrer la campagne** et vous êtes prêt à lancer votre campagne API !

{% alert note %}
Le paramètre de désabonnement en un clic pour les campagnes d'e-mails transactionnels est défini par défaut sur **Utiliser la valeur par défaut de l'espace de travail**, comme pour les autres campagnes d'e-mails. Comme il s'agit d'envoi de messages transactionnels, Braze n'ajoute pas le désabonnement en un clic. Pour ajouter un désabonnement en un clic à ce type de campagne, [modifiez ce paramètre]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) sous **Informations sur l'envoi**.
{% endalert %}

### Étiquettes non autorisées dans les e-mails transactionnels

Les étiquettes Liquid `Connected Content` et `Promotion Code` ne sont pas disponibles dans les campagnes d'e-mails transactionnels.

L'utilisation de l'étiquette `Connected Content` nécessite que Braze effectue une requête API sortante pendant le processus d'envoi, ce qui peut ralentir l'envoi du message si le service externe sollicité subit une latence. De même, l'étiquette `Promotion Code` nécessite un traitement supplémentaire de la part de Braze pour évaluer la disponibilité d'un code de promotion avant l'envoi, ce qui peut ralentir le processus si aucun code n'est disponible.

Par conséquent, les étiquettes `Connected Content` et `Promotion Code` ne sont pas prises en charge dans les champs de votre campagne d'e-mails transactionnels.