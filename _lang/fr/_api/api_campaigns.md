---
nav_title: Campagnes API
article_title: Campagnes API
page_order: 5
description: "Cet article de référence explique comment générer une id_campagne à inclure dans vos appels d’API et comment configurer cette campagne."
page_type: reference
tool: Campaigns

---
# Campagnes API

> Cet article de référence explique comment générer une `campaign_id` à inclure dans vos appels d’API et comment configurer cette campagne.

{% alert note %}
Les campagnes envoyées à l’aide de l’API de messagerie <a href="{{site.baseurl}}/api/endpoints/messaging/"></a> peuvent avoir les mêmes options détaillées de reporting et de reciblage que les campagnes créées sur le tableau de bord.
{% endalert %}

## Créer une nouvelle campagne

Accédez à la page **Campaigns (Campagnes)** sur votre compte Braze d’entreprise et cliquez sur **Create Campaign (Créer une campagne)**, puis sélectionnez **API Campaigns (Campagnes API)**. Vous pouvez maintenant passer à la configuration de votre campagne API.

{% alert note %}
Une [campagne déclenchée par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) est différente d’une campagne API.
{% endalert %}

## Configurer votre campagne

Pour configurer votre campagne, procédez comme suit :

1. Ajoutez un titre descriptif pour pouvoir trouver les résultats sur notre page Campagnes après avoir envoyé vos messages.
2. Cliquez sur **Add Message (Ajouter un message)** et ajoutez les types de messages qui seront inclus dans votre campagne API. Cela créera un `Message Variation ID` qui servira de `campaign_id`. <br>
<br>
 Après avoir enregistré votre campagne API, vous devez inclure les champs `campaign_id` générés avec votre demande d’API, lorsque cela est indiqué dans l’article [Send Messages Endpoints (Endpoints d’envoi de messages)][2].<br>
<br>

3. Vous pouvez éventuellement ajouter un événement de conversion pour suivre les conversions de l’utilisateur sur une action spécifique ou un objectif de campagne.
4. Cliquez sur **Save Campaign (Enregistrer la campagne)** et vous êtes prêt à commencer votre campagne API !


[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints

