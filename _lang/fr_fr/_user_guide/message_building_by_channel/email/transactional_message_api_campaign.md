---
nav_title: Campagnes d’e-mails transactionnels
article_title: Campagnes d’e-mails transactionnels
page_order: 10

description: "Le présent article de référence explique comment créer et configurer une nouvelle campagne Braze d’e-mails transactionnels."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Campagnes d’e-mails transactionnels

> Les e-mails transactionnels de Braze sont envoyés pour faciliter une transaction convenue entre l'expéditeur et le destinataire. Cet article de référence explique comment créer une campagne d'e-mails transactionnels dans le tableau de bord de Braze et générer une adresse `campaign_id` à inclure dans vos appels API pour notre [endpoint`/transactional/v1/campaigns/{campaign_id}/send`.]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)

{% alert important %}
L'e-mail transactionnel de Braze n'est disponible que dans le cadre de certaines offres de Braze. Contactez votre gestionnaire de satisfaction client Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) pour plus de détails.
{% endalert %}

Le type de campagne d'e-mail transactionnel est créé pour l'envoi d'e-mails automatisés et non promotionnels destinés à faciliter une transaction convenue entre vous et vos clients. Cela comprend des informations telles que :

- Les confirmations de commande
- La réinitialisation du mot de passe
- Les alertes de facturation
- Les alertes d’expédition

En bref, vous pouvez utiliser les e-mails transactionnels pour envoyer à un seul utilisateur des notifications critiques provenant de votre service, où la vitesse est de la plus haute importance. 

{% alert important %}
Les e-mails transactionnels diffèrent des campagnes transactionnelles, qui peuvent être utilisées pour cibler vos utilisateurs sans coûts supplémentaires. Les campagnes transactionnelles, par exemple, peuvent inclure des messages envoyés après qu’un utilisateur ajoute un élément à son panier. Pour plus d’informations, consultez les [options de ciblage de l'audience]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/).
{% endalert %}

## Étape 1 : Créer une nouvelle campagne

Pour créer une nouvelle campagne d'e-mails transactionnels, créez une campagne et sélectionnez l'**e-mail transactionnel** comme canal d'envoi de messages.

![Créez une liste déroulante de campagne avec l'option en surbrillance pour l'e-mail transactionnel.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez maintenant passer à la configuration de votre campagne d’e-mails transactionnels.

## Étape 2 : Configurer votre campagne

Le flux de création des campagnes d'e-mails de transaction est simplifié par rapport à celui d'une [campagne d'e-mails standard]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) afin de garantir que vos e-mails de transaction critiques pour l'entreprise puissent atteindre tous les utilisateurs.

Par conséquent, vous remarquerez que plusieurs paramètres que vous connaissez peut-être d’autres types de campagnes Braze ne sont pas obligatoires lors de la configuration de ce type de campagne :

- L'étape de **réception/distribution** a été simplifiée pour supprimer les options de planification. Les e-mails transactionnels seront toujours déclenchés via l'API REST de Braze à l'aide de l'ID de campagne indiqué sur la page de **réception/distribution**. D'autres paramètres, tels que les contrôles de rééligibilité et les paramètres de limite de fréquence, ont également été supprimés afin de confirmer que tous les utilisateurs sont joignables pour ces alertes transactionnelles critiques lorsque votre service déclenche une demande d'envoi.
- L'étape des **audiences ciblées** a été supprimée. Étant donné que les e-mails transactionnels enregistrent l’intégralité de votre base d’utilisateurs comme étant admissible (y compris les utilisateurs non abonnés), il n’est pas nécessaire de spécifier des filtres ou des segments. Par conséquent, si vous avez une logique à appliquer à qui doit recevoir ce message, nous vous recommandons de l’appliquer avant de déterminer si la demande d’API doit être envoyée à Braze pour déclencher le message à un utilisateur spécifique.
- L'étape des **conversions** a été supprimée. Pour le moment, les e-mails transactionnels ne prennent pas en charge le suivi des événements de conversion.

![Flux de travail de composition, réception/distribution et confirmation pour créer une campagne d'e-mails transactionnels.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Pour configurer votre campagne d'e-mails transactionnels, procédez comme suit :

1. Ajoutez un nom descriptif afin de pouvoir retrouver les résultats sur votre page **Campagnes** après avoir envoyé vos messages.
2. Composez votre e-mail ou sélectionnez un modèle.
3. Notez votre `campaign_id`. Après avoir enregistré votre campagne API, vous devez inclure les champs `campaign_id` générés dans votre demande API, comme indiqué dans l'article sur le [point de terminaison de l'e-mail transactionnel.]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)
4. Cliquez sur **Enregistrer la campagne** et vous êtes prêt à lancer votre campagne API !

{% alert note %}
Le paramètre de désabonnement à la liste en un clic pour les campagnes d'e-mails transactionnels est défini par défaut sur **Utiliser l'espace de travail par défaut**, comme pour les autres campagnes d'e-mails. Comme il s'agit d'envois de messages transactionnels, Braze n'ajoute pas la possibilité de se désabonner en un seul clic. Pour ajouter une fonction de désabonnement en un clic à ce type de campagne, [modifiez ce paramètre]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) sous **Informations sur l'envoi.**
{% endalert %}

### Balises non autorisées dans les e-mails transactionnels

Les balises Liquid `Connected Content` et `Promotion Code` ne sont pas disponibles dans les campagnes d'e-mails transactionnels.

L’utilisation de la balise `Connected Content` nécessite que Braze fasse une demande d’API sortante pendant notre processus d’envoi, ce qui peut ralentir le processus d’envoi de messages si le service externe que nous demandons subit une latence. De même, la balise `Promotion Code` nécessite que Braze effectue un traitement supplémentaire pour évaluer la disponibilité d’une promotion avant l’envoi, ce qui peut ralentir le processus d’envoi, si l’une d’elles n’est pas disponible.

Par conséquent, nous ne prenons pas en charge les balises `Connected Content` ou `Promotion Code` dans les champs de votre campagne d'e-mails transactionnels.


