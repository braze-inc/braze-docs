---
nav_title: Campagnes transactionnelles
article_title: Campagnes transactionnelles
page_order: 5
description: "Cet article de référence couvre la façon de créer et de configurer une nouvelle campagne d'email transactionnelle Braze."
page_type: Référence
alias: "/api/api_campaigns/transactional_campaigns"
tool: Campagnes
---

# Campagnes d'email transactionnelles

Les courriels transactionnels sont ceux qui sont envoyés pour faciliter une transaction convenue entre un expéditeur et le destinataire. Le type de campagne transactionnelle d'email de Braze est conçu pour envoyer des messages électroniques automatisés et non promotionnels comme les confirmations de commande, les réinitialisations de mot de passe, des alertes de facturation, ou d'autres notifications critiques pour les entreprises provenant de votre service pour un seul utilisateur où la vitesse est de la plus haute importance.

{% alert important %}
Le courrier électronique transactionnel n'est disponible que dans le cadre de certains paquets Braze. Pour plus de détails, veuillez contacter votre Responsable du service client de Braze.
{% endalert %}

Cet article de référence couvre la façon de créer une campagne transationelle dans le tableau de bord de Braze et de générer un `campaign_id` pour inclure dans votre API des appels pour notre [point de terminaison d'API d'Email Transactionnel]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).


## Créer une nouvelle campagne
Accédez à la page des **Campagnes** de votre compte Braze et cliquez sur __Créer une Campagne__, puis sélectionnez __Email transactionnel__ sous la section __Transactionnelle__.

!\[Select Transactional Email Campaign\]\[1\]{: style="float:right;max-width:25%;margin-left:15px;"}

Maintenant, vous pouvez passer à la configuration de votre campagne transactionnelle.

## Configurer votre campagne

Lors du lancement d'une campagne transactionnelle, Braze a simplifié le flux de création de campagnes afin de vous assurer que vos courriels transactionnels critiques peuvent atteindre tous les utilisateurs. Résultat: vous remarquerez quelques paramètres avec lesquels vous pouvez être familier avec d'autres types de campagne Braze ne sont pas requis lors de la configuration de ce type de campagne :

- La page de livraison a été simplifiée pour supprimer les options de planification. Les courriels transactionnels seront toujours déclenchés par l'API REST de Braze en utilisant l'ID de campagne affiché sur la page de livraison. Des paramètres supplémentaires que vous pouvez utiliser pour trouver sur cette page, tels que les contrôles de rééligibilité et les paramètres de plafonnement de fréquence, ont également été supprimés afin de s'assurer que tous les utilisateurs sont accessibles pour ces alertes transactionnelles critiques lorsque votre service déclenche une demande d'envoi.<br><br>
- En tant que courriels transactionnels inscrivent toute votre base d'utilisateurs comme éligible, y compris les utilisateurs désabonnés, il n'y a pas besoin de spécifier des filtres ou des segments avec la page **Utilisateurs cibles**. Par conséquent, si vous avez une logique à appliquer à qui doit recevoir ce message, nous vous recommandons d'appliquer cette logique avant de déterminer si vous devez faire une requête API à Braze pour déclencher le message à un utilisateur spécifique.<br><br>
- Les courriels transactionnels ne prennent pas en charge le suivi des événements de conversion pour le moment.

!\[Flux de création de campagne transactionnelle\]\[2\]

1. Ajoutez un titre descriptif pour que vous puissiez trouver les résultats sur la page de nos campagnes après avoir envoyé vos messages.
2. Écrivez votre courriel ou sélectionnez à partir d'un modèle.
3. Prenez note de votre `campaign_id`. Après avoir enregistré votre campagne API, vous devez inclure les champs générés `campaign_id` avec votre requête API où il est noté dans la spécification [Transactional Email Endpoint Endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)
4. Cliquez sur __Enregistrer la campagne__ et vous êtes configuré pour démarrer votre campagne API !

### Tags interdits dans les courriels transactionnels

Veuillez noter que les balises `Contenus connectés` et `Code promotionnel` Liquide ne sont actuellement pas disponibles dans les campagnes d'email transactionnelles.

L'utilisation de la balise `Contenu connecté` nécessite que Braze fasse une demande d'API sortante pendant notre processus d'envoi, qui peut ralentir le processus d'envoi du message si le service externe que nous demandons est en latence.  De même, la balise `Promotion Code` nécessite que Braze effectue un traitement supplémentaire pour évaluer la disponibilité d'une promotion avant l'envoi, qui peut ralentir le processus d'envoi s'il n'est pas disponible.

Résultat: nous ne prenons pas en charge l'inclusion des balises `Contenus connectés` ou `Code promotionnel` dans aucun domaine de votre campagne transactionnelle d'e-mail.
[1]: {% image_buster /assets/img/transactional_email_campaign.png %} [2]: {% image_buster /assets/img/transactional_campaign_compose.png %}
