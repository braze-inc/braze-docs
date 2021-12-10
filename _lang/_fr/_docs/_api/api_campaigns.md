---
nav_title: Campagnes API
article_title: Campagnes API
page_order: 5
description: "Cet article de référence couvre la façon de générer un campaign_id à inclure dans vos appels API et comment configurer cette campagne."
page_type: Référence
alias: /api/api_campaigns/
tool: Campagnes
---

# Campagnes API

> Cet article de référence couvre comment générer un `campaign_id` à inclure dans vos appels API et comment configurer cette campagne.

{% alert note %}
Les campagnes envoyées via la <a href="{{site.baseurl}}/api/endpoints/messaging/"> Messaging API</a> peuvent avoir les mêmes options détaillées de rapport et de redistribution que les campagnes créées sur le tableau de bord.
{% endalert %}

## Créer une nouvelle campagne

Accédez à la page des **Campagnes** de votre compte Braze et cliquez sur __Créer une Campagne__, puis sélectionnez __Campagnes API__. Maintenant, vous pouvez passer à la configuration de votre campagne API.

{% alert note %}
Une campagne [déclenchée par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) est différente d'une campagne API.
{% endalert %}

## Configurer votre campagne

Pour configurer votre campagne, effectuez les étapes suivantes :

1. Ajoutez un titre descriptif pour que vous puissiez trouver les résultats sur la page de nos campagnes après avoir envoyé vos messages.
2. Cliquez sur **Ajouter un message** et ajoutez les types de messages qui seront inclus dans votre campagne API. Cela va créer un `ID de variation de message`qui servira de votre `campaign_id`. <br><br> Après avoir enregistré votre campagne API, vous devez inclure les champs `campaign_id` générés avec votre requête API où noté dans le [Envoyer des messages points de terminaison][2].<br><br>
3. Optionnellement, vous pouvez ajouter un événement de conversion pour suivre les conversions d'utilisateurs sur une action ou un objectif de campagne.
4. Cliquez sur **Enregistrer la campagne** et vous êtes configuré pour démarrer votre campagne API !

!\[Créer des campagnes API\]\[4\]
[4]: {% image_buster /assets/img/createapicampaigns.gif %} "API Campaign Creation"

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints
