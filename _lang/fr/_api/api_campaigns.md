---
nav_title: Campagnes API
article_title: Campagnes API
page_order: 5
description: "Cet article de référence explique comment générer un campaign_id à inclure dans vos appels d’API et comment configurer cette campagne."
page_type: reference
tool: Campaigns

---
# Campagnes API

> Cet article de référence explique comment générer un `campaign_id` à inclure dans vos appels d’API et comment configurer cette campagne.

Les campagnes API sont généralement utilisées pour l’envoi de messages transactionnels. Lorsque vous créez des campagnes API (et non des [campagnes déclenchées par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)), le tableau de bord de Braze n’est utilisé que pour générer un `campaign_id` qui vous permet de suivre les données analytiques pour composer les rapports de campagne. Vous pouvez également générer un ID de variation de message qui est différent pour chaque variante de votre campagne. 

Vous enverrez alors cette information à votre équipe de développement pour l’utiliser dans la requête API, avec les éléments suivants :
- Copie de campagne
- Appartenance à une audience
- Actifs

Après le début de la campagne, vous pouvez voir les résultats dans le tableau de bord. Les campagnes API utilisent les [API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) de Braze qui disposent des mêmes options détaillées de reporting et de reciblage que les campagnes créées entièrement à l’aide du tableau de bord.

{% alert warning %}
Tous les utilisateurs sont éligibles pour les campagnes API, même ceux de votre groupe de contrôle global, étant donné que les campagnes API sont généralement transactionnelles.
{% endalert %}

## Créer une nouvelle campagne

Accédez à la page **Campaigns (Campagnes)** sur votre compte Braze et cliquez sur **Create Campaign (Créer une campagne)**, puis sélectionnez **API Campaigns (Campagnes API)**. Vous pouvez maintenant passer à la configuration de votre campagne API.

{% alert note %}
Une [campagne déclenchée par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) est différente d’une campagne API.
{% endalert %}

## Configurer votre campagne

Pour configurer votre campagne, procédez comme suit :

1. Ajoutez un titre descriptif pour pouvoir trouver les résultats sur notre page Campagnes après avoir envoyé vos messages.
2. Cliquez sur **Add Message (Ajouter un message)** et ajoutez les types de messages qui seront inclus dans votre campagne API. Ceci vous permettra de générer un `campaign_id` et un ID de variation de message qui changera pour chaque canal que vous ajoutez. 
3. Vous pouvez éventuellement ajouter un événement de conversion pour suivre les conversions de l’utilisateur sur une action spécifique ou un objectif de campagne.
4. Cliquez sur **Save Campaign (Enregistrer la campagne)** et vous êtes prêt à commencer votre campagne API !

## Appels API

Après l’enregistrement de votre campagne API, intégrez ce qui suit dans votre requête API : 
- Les champs `campaign_id` générés avec votre requête API sont renseignés dans les [Endpoints de messages envoyés][2].
- Un [objet de message]({{site.baseurl}}/api/objects_filters/#messaging-objects) pour chaque plateforme comprise dans la campagne. Dans l’objet de message, renseignez l’ID de variation de message. Ceci précisera que des statistiques doivent être recueillies et affichées pour cette variante. Les objets de message suivants sont pris en charge : Android, Cartes de contenu, e-mail, iOS, Kindle, SMS/MMS, notification push Web et webhook.

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints

