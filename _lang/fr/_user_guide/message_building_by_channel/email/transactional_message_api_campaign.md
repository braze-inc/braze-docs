---
nav_title: E-mails transactionnels
article_title: Campagnes d’e-mails transactionnels
page_order: 7

description: "Le présent article de référence explique comment créer et configurer une nouvelle campagne Braze d’e-mails transactionnels."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Campagnes d’e-mails transactionnels

> Les e-mails transactionnels sont envoyés pour faciliter une transaction convenue entre un expéditeur et le destinataire. Le présent article de référence explique comment créer une campagne d’e-mails transactionnels dans le tableau de bord de Braze et générer un `campaign_id` à inclure dans votre appel d’API pour notre [endpoint d’API d’e-mail transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
L’e-mail transactionnel n’est disponible que dans certains forfaits Braze. Contactez votre gestionnaire du succès des clients de Braze ou ouvrez un [ticket d’assistance]({{site.baseurl}}/braze_support/) pour plus de détails.
{% endalert %}

Le type de campagne d’e-mails transactionnels de Braze est conçu spécialement pour l’envoi de courriels automatisés et non promotionnels afin de faciliter une transaction convenue entre vous et vos clients. Cela comprend des informations telles que :

- Les confirmations de commande
- La réinitialisation du mot de passe
- Les alertes de facturation
- Les alertes d’expédition

En bref, vous pouvez utiliser les e-mails transactionnels pour envoyer des notifications critiques provenant de votre service à un seul utilisateur où la vitesse est de la plus haute importance. 

{% alert important %}
Les e-mails transactionnels diffèrent des campagnes transactionnelles, qui peuvent être utilisées pour cibler vos utilisateurs sans frais supplémentaires. Les campagnes transactionnelles, par exemple, peuvent inclure des messages envoyés après qu’un utilisateur ajoute un élément à son panier. Consultez les [options de ciblage du public]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) pour plus d’informations. 
{% endalert %}

## Créer une nouvelle campagne

Pour créer une nouvelle campagne d’e-mails transactionnels, accédez à la page **Campagne**, cliquez sur **Créer une campagne**, et sélectionnez **E-mail transactionnel** dans la liste déroulante.

![Créer une liste déroulante de campagne avec l’option mise en surbrillance pour l’e-mail transactionnel.][1]{: style="float:right;max-width:30%;margin-left:15px;"}

Vous pouvez maintenant passer à la configuration de votre campagne d’e-mails transactionnels.

## Configurer votre campagne

Le flux de création de campagnes pour les campagnes d’e-mails transactionnels est plus simple que celui d’une [campagne standard par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/) afin de garantir que votre e-mail transactionnel stratégique touche tous les utilisateurs.

Par conséquent, vous remarquerez que plusieurs paramètres que vous connaissez peut-être d’autres types de campagnes Braze ne sont pas obligatoires lors de la configuration de ce type de campagne :

- L’étape de **livraison** a été simplifiée pour supprimer les options de planification. Les e-mails transactionnels seront toujours déclenchés via l’API REST de Braze en utilisant l’ID de campagne affiché sur la page **Livraison**. D’autres paramètres, comme des contrôles de réadmissibilité et des paramètres de limite de fréquence, ont également été supprimés pour s’assurer que tous les utilisateurs sont accessibles pour ces alertes transactionnelles critiques lorsque votre service déclenche une demande d’envoi.
- L’étape de **ciblage des utilisateurs** a été supprimée. Étant donné que les e-mails transactionnels enregistrent l’intégralité de votre base d’utilisateurs comme étant admissible (y compris les utilisateurs non abonnés), il n’est pas nécessaire de spécifier des filtres ou des segments. Par conséquent, si vous avez une logique à appliquer à qui doit recevoir ce message, nous vous recommandons de l’appliquer avant de déterminer si la demande d’API doit être envoyée à Braze pour déclencher le message à un utilisateur spécifique.
- L’étape des **conversions** a été supprimé. Les e-mails transactionnels ne prennent pas en charge le suivi des événements de conversion pour le moment.

![Composer, livrer et confirmer le flux de travail pour créer une campagne d'e-mails transactionnels.][2]

Pour configurer votre campagne d'e-mails transactionnels, suivez les étapes générales suivantes :

1. Ajoutez un nom descriptif pour pouvoir trouver les résultats sur vos **Campaigns** après avoir envoyé vos messages.
2. Composez votre e-mail ou sélectionnez un modèle.
3. Notez votre `campaign_id`. Après avoir enregistré votre campagne API, vous devez inclure les champs `campaign_id` générés avec votre demande d’API, lorsque cela est indiqué dans l’article [endpoint d’e-mail transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Cliquez sur **Enregistrer la campagne** et vous êtes prêt à commencer votre campagne API !

### Balises non autorisées dans les e-mails transactionnels

Les balises Liquid `Connected Content` et `Promotion Code` ne sont pas disponibles dans les campagnes d'e-mails transactionnels.

L’utilisation de la balise `Connected Content` nécessite que Braze fasse une demande d’API sortante pendant notre processus d’envoi, ce qui peut ralentir le processus d’envoi de messages si le service externe que nous demandons subit une latence. De même, la balise `Promotion Code` nécessite que Braze effectue un traitement supplémentaire pour évaluer la disponibilité d’une promotion avant l’envoi, ce qui peut ralentir le processus d’envoi, si l’une d’elles n’est pas disponible.

Par conséquent, nous ne prenons pas en charge les balises `Connected Content` ou `Promotion Code` dans les champs de votre campagne d'e-mails transactionnels.


[1]: {% image_buster /assets/img/transactional_email_campaign.png %} 
[2]: {% image_buster /assets/img/transactional_campaign_compose.png %}
