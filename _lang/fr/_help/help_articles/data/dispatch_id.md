---
nav_title: Comportement du Dispatch ID
article_title: Comportement du Dispatch ID
page_order: 1

page_type: solution
description: "Cet article d’aide couvre le comportement du DispatchID, y compris son utilisation, ses implications et ses limitations."
---

# Comportement du Dispatch ID

Un `dispatch_id` est l’identifiant de la transmission du message, c’est un ID unique pour chaque « dispatch » envoyé par Braze. Les utilisateurs qui reçoivent un message planifié reçoivent le même `dispatch_id`, alors que les messages déclenchés par une action ou l’API recevront un `dispatch_id` unique par utilisateur.

{% alert important %}
Notez que les `dispatch_id` sont par utilisateur, par campagne pour les messages déclenchés (déclenchés par action ou par API).
{% endalert %}

Cela peut entraîner deux utilisateurs différents ayant différents `dispatch_id` pour une campagne unique si des messages ont été envoyés à deux moments différents. Ceci est souvent dû au fait que les requêtes API ont été effectuées séparément. Si les deux utilisateurs se trouvaient dans le même public de campagne dans un seul envoi, leurs `dispatch_id` seront les mêmes.

## Comportement du dispatch ID dans les campagnes

Les messages de campagne planifiés ont le même `dispatch_id`. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un `dispatch_id` unique par utilisateur. Par exemple, deux utilisateurs de votre public de campagne planifié auront le même `dispatch_id`. Cependant, deux utilisateurs dans le public d’une campagne déclenchée par API auront des `dispatch_id` différents.

Les campagnes multicanal auront le comportement décrit pour leur type de livraison.

{% alert warning %}
Un `dispatch_id` est généré de façon aléatoire pour toutes les Canvas Steps, car Braze traite les Canvas Steps comme des événements déclenchés, même lorsqu’ils sont « planifiés ». Cela peut entraîner des incohérences qui génèrent les ID. Parfois, un composant Canvas sera un `dispatch_id` unique par utilisateur par envoi, ou elle peut avoir un `dispatch_id` partagé entre les utilisateurs par envoi.
{% endalert %}

## Templater le dispatch_ID dans les messages avec Liquid

Si vous souhaitez suivre l’envoi d’un message à partir du message (dans une URL, par exemple), vous pouvez intégrer le `dispatch_id`. Vous pouvez trouver le formatage dans notre liste de tags de personnalisation pris en charge, sous [Attributs Canvas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Le comportement est exactement identique à `api_id`, c.-à-d. que lorsque `api_id` n’est pas disponible lors de la création de campagnes, il est affiché sous forme de marque substitutive et il sera prévisualisé comme `dispatch_id_for_unsent_campaign`. L’ID est généré avant l’envoi du message et sera ajouté au moment de l’envoi.

{% alert warning %}
Le templating Liquid de `dispatch_id_for_unsent_campaign` ne fonctionne pas avec les messages in-app, car les messages n’ont pas de `dispatch_id`.
{% endalert %}

## Champ Dispatch ID Currents pour l’e-mail

Pour continuer à améliorer les capacités de Currents, nous ajoutons `dispatch_id` en tant que champ aux événements e-mail Currents sur tous les types de connecteurs.

Le `dispatch_id` est l’ID unique généré pour chaque transmission (« dispatch ») envoyée depuis la plateforme Braze.

Alors que tous les clients qui reçoivent un message planifié reçoivent les mêmes `dispatch_id`, les clients qui reçoivent des messages basés sur des actions ou des API auront un `dispatch_id` unique par message. Le champ `dispatch_id` vous permet d’identifier l’instance d’une campagne récurrente qui est responsable de la conversion, ce qui vous fournit des informations supplémentaires et des informations sur les types de campagnes qui peuvent booster vos objectifs commerciaux.

Vous pouvez utiliser `dispatch_id` en tant que [tag de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), dans [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) (Événements d’engagement sur les messages), ou lorsque vous utilisez [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) ou [Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/) pour Currents.

_Dernière mise à jour le 15 juillet 2021_
