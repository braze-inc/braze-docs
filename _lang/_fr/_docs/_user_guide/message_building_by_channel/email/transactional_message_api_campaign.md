---
nav_title: Campagnes transactionnelles
article_title: Campagnes d'email transactionnelles
page_order: 7
description: "Cet article de référence traite de la façon de créer et de configurer une nouvelle campagne d'email transactionnel de Braze."
page_type: Référence
tool:
  - Campagnes
channel: Email
alias: "/api/api_campaigns/transactional_campaigns"
---

# Campagnes d'email transactionnelles

> Cet article de référence couvre la façon de créer une campagne d'email transactionnelle dans le tableau de bord de Braze et de générer un `campaign_id` pour inclure dans votre API des appels pour notre [point de terminaison d'API d'email transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
Le courrier électronique transactionnel n'est disponible que dans le cadre de certains paquets Braze. Veuillez contacter votre gestionnaire de service client Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) pour plus de détails.
{% endalert %}

Les courriels transactionnels sont votre solution unique pour envoyer des messages électroniques automatisés et non promotionnels afin de faciliter une transaction convenue entre vous et vos clients. Cela inclut des informations telles que:

- Confirmation de commande
- Réinitialisation du mot de passe
- Alertes de facturation
- Alertes d'expédition

En bref, utilisez les courriels transactionnels pour envoyer des notifications critiques pour les entreprises provenant de votre service pour un seul utilisateur où la vitesse est de la plus haute importance.

{% alert note %}
Les e-mails transactionnels diffèrent des campagnes transactionnelles qui peuvent être utilisées pour cibler vos utilisateurs sans frais supplémentaires. Consultez [options de ciblage du public]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) pour plus d'informations.
{% endalert %}

## Créer une nouvelle campagne

Pour créer une nouvelle campagne d'e-mail de transaction, accédez à la page **Campagnes** et cliquez sur **Créer une campagne**, puis sélectionnez **Email transactionnel** dans le menu déroulant.

!\[Select Transactional Email Campaign\]\[1\]{: style="float:right;max-width:30%;margin-left:15px;"}

Maintenant, vous pouvez passer à la configuration de votre campagne Transactional Email campaign.

## Configurer votre campagne

Le flux de création de campagne pour les campagnes d'emails de transaction est simplifié par rapport à celui d'une [campagne d'e-mail standard]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/) pour s'assurer que votre e-mail de transaction critique en entreprise peut atteindre tous les utilisateurs.

Résultat: vous remarquerez quelques paramètres avec lesquels vous pouvez être familier avec d'autres types de campagne Braze ne sont pas requis lors de la configuration de ce type de campagne :

- L'étape **Delivery** a été simplifiée pour supprimer les options de planification. Les e-mails transactionnels seront toujours déclenchés par l'API REST de Braze en utilisant l'ID de la campagne affiché sur la page **Delivery**. Des paramètres supplémentaires que vous pouvez utiliser pour trouver sur cette page, tels que les contrôles de rééligibilité et les paramètres de plafonnement de fréquence, ont également été supprimés pour s'assurer que tous les utilisateurs sont joignables pour ces alertes transactionnelles critiques lorsque votre service déclenche une demande d'envoi.
- L'étape **Utilisateurs cibles** a été supprimée. Étant donné que les E-mails transactionnels inscrivent toute votre base d'utilisateurs comme éligibles (y compris les utilisateurs désabonnés), il n'est pas nécessaire de spécifier des filtres ou des segments. Par conséquent, si vous avez une logique à appliquer à qui doit recevoir ce message, nous vous recommandons d'appliquer cette logique avant de déterminer si vous devez faire une requête API à Braze pour déclencher le message à un utilisateur spécifique.
- L'étape **Conversions** a été supprimée. Les courriels transactionnels ne prennent pas en charge le suivi des événements de conversion pour le moment.

!\[Flux de création de campagne transactionnelle\]\[2\]

Pour configurer votre campagne d'email transactionnel, suivez ces étapes générales :

1. Ajoutez un nom descriptif pour que vous puissiez trouver les résultats sur votre page **Campagnes** après avoir envoyé vos messages.
2. Écrivez votre courriel ou sélectionnez à partir d'un modèle.
3. Prenez note de votre `campaign_id`. Après avoir enregistré votre campagne API, vous devez inclure les champs générés `campaign_id` avec votre requête API où il est noté dans l'article [Transactional Email Endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Cliquez sur **Enregistrer la campagne** et vous êtes configuré pour démarrer votre campagne API !

### Tags interdits dans les courriels transactionnels

Les balises `Contenus connectés` et `Code promotionnel` Liquid ne sont actuellement pas disponibles dans les campagnes transactionnelles d'E-mail.

L'utilisation de la balise `Contenu connecté` nécessite que Braze fasse une demande d'API sortante pendant notre processus d'envoi, qui peut ralentir le processus d'envoi du message si le service externe que nous demandons est en latence. De même, la balise `Promotion Code` nécessite que Braze effectue un traitement supplémentaire pour évaluer la disponibilité d'une promotion avant l'envoi, qui peut ralentir le processus d'envoi s'il n'est pas disponible.

Résultat: nous ne prenons pas en charge l'inclusion des balises `Contenus connectés` ou `Code promotionnel` dans aucun domaine de votre campagne Transactionnelle d'E-mail.
[1]: {% image_buster /assets/img/transactional_email_campaign.png %} [2]: {% image_buster /assets/img/transactional_campaign_compose.png %}
