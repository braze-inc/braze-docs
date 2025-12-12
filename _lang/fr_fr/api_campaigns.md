---
nav_title: Campagnes API
article_title: Campagnes API
page_order: 5
description: "Cet article de référence explique comment générer un identifiant de campagne à inclure dans vos appels API et comment configurer cette campagne."
page_type: reference
tool: Campaigns

---
# Campagnes API

> Cet article de référence explique comment générer un `campaign_id` à inclure dans vos appels d’API et comment configurer cette campagne.

Les campagnes API sont généralement utilisées pour l’envoi de messages transactionnels. Lors de la création de campagnes API (et non de [campagnes déclenchées par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)), le tableau de bord de Braze n'est utilisé que pour générer un `campaign_id`, qui vous permet de suivre l'analyse/analytique pour les rapports de campagne. Vous pouvez également générer un ID de variation de message qui est différent pour chaque variante de votre campagne. 

Vous enverrez alors cette information à votre équipe de développement pour l’utiliser dans la requête API, avec les éléments suivants :
- Copie de campagne
- Appartenance à une audience
- Ressources

Après le début de la campagne, vous pouvez voir les résultats dans le tableau de bord. Les campagnes API utilisent les [API d'envoi de messages de]({{site.baseurl}}/api/endpoints/messaging/) Braze, qui disposent des mêmes options de reporting détaillé et de reciblage que les campagnes créées entièrement via le tableau de bord.

{% alert warning %}
Tous les utilisateurs sont éligibles pour les campagnes API, même ceux de votre groupe de contrôle global, étant donné que les campagnes API sont généralement transactionnelles. Un en-tête de [liste de désabonnement en un clic]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe) n'est pas ajouté à ces envois. Si vous souhaitez ajouter un en-tête de liste de désabonnement en un seul clic à toutes les campagnes API, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Créer une nouvelle campagne

Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**, puis sélectionnez **Campagnes API.** Vous pouvez maintenant passer à la configuration de votre campagne API.

Une [campagne déclenchée par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) est différente d'une campagne API.

## Configurer votre campagne

Pour configurer votre campagne, procédez comme suit :

1. Ajoutez un titre descriptif pour pouvoir trouver les résultats sur notre page Campagnes après avoir envoyé vos messages.
2. Cliquez sur **Ajouter un message** et ajoutez les types d'envoi de messages qui seront inclus dans votre campagne API. Ceci vous permettra de générer un `campaign_id` et un ID de variation de message qui changera pour chaque canal que vous ajoutez. 
3. Vous pouvez éventuellement ajouter un événement de conversion pour suivre les conversions de l’utilisateur sur une action spécifique ou un objectif de campagne.
4. Cliquez sur **Enregistrer la campagne** et vous êtes prêt à commencer votre campagne API !

## Appels API

Après l’enregistrement de votre campagne API, intégrez ce qui suit dans votre requête API : 
- Les champs `campaign_id` générés avec votre demande d'API sont indiqués dans les [points de terminaison d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints)
- Un [objet message]({{site.baseurl}}/api/objects_filters/#messaging-objects) pour chaque plate-forme incluse dans la campagne. Dans l’objet de message, renseignez l’ID de variation de message. Cela permet de spécifier que les statistiques doivent être collectées et affichées sous cette variante. Les objets de message suivants sont pris en charge : Android, Cartes de contenu, e-mail, iOS, Kindle, SMS/MMS, notification push Web et webhook.


