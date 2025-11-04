---
nav_title: Comportement du Dispatch ID
article_title: Comportement du Dispatch ID
page_order: 0

page_type: solution
description: "Cet article d'aide couvre le comportement de l'ID de répartition, y compris son utilisation, ses implications et ses limites."
---

# Comportement du Dispatch ID

Un `dispatch_id` est l’identifiant de la transmission du message, c’est un ID unique pour chaque « dispatch » envoyé par Braze. Les utilisateurs qui reçoivent un message planifié reçoivent le même `dispatch_id`. En règle générale, les messages basés sur une action ou déclenchés par une API recevront une adresse `dispatch_id` unique par utilisateur, mais les messages envoyés à proximité d'un autre peuvent partager la même adresse `dispatch_id` entre plusieurs utilisateurs.

Ainsi, deux utilisateurs différents peuvent avoir des ID d'envoi différents pour une même campagne si les messages ont été envoyés à deux moments différents. Ceci est souvent dû au fait que les requêtes API ont été effectuées séparément. Si les deux utilisateurs faisaient partie de la même audience de campagne lors d'un envoi unique, leurs ID d'envoi seraient les mêmes.

## Comportement du dispatch ID dans les campagnes

Les messages de campagne planifiés ont le même `dispatch_id`. Les messages de campagne basés sur des actions ou déclenchés par l'API peuvent obtenir un `dispatch_id` unique par utilisateur, ou le `dispatch_id` peut être le même pour plusieurs utilisateurs lorsqu'il est envoyé à proximité immédiate ou dans le cadre du même appel API, comme décrit ci-dessus. Par exemple, deux utilisateurs faisant partie de l'audience de votre campagne planifiée auront la même adresse `dispatch_id` chaque fois que la campagne est planifiée. Toutefois, deux utilisateurs faisant partie de l'audience d'une campagne déclenchée par une API peuvent avoir des ID d'envoi différents s'ils ont été envoyés lors d'appels API distincts et s'ils ne se trouvent pas à proximité l'un de l'autre.

Les campagnes multicanal auront le comportement décrit pour leur type de livraison.

{% alert warning %}
Une adresse `dispatch_id` est générée de manière aléatoire pour toutes les étapes du canvas, car Braze considère les étapes du canvas comme des événements déclenchés, même lorsqu'elles sont "planifiées". Cela peut entraîner des incohérences qui génèrent les ID. Il arrive qu'un composant Canvas ait un `dispatch_id` unique par utilisateur et par envoi, ou qu'il ait des ID de répartition partagés entre les utilisateurs et par envoi.
{% endalert %}

## Templater le dispatch_ID dans les messages avec Liquid

Si vous souhaitez suivre l’envoi d’un message à partir du message (dans une URL, par exemple), vous pouvez intégrer le `dispatch_id`. Vous trouverez le formatage correspondant sous Attributs du canevas dans notre liste des [tags de personnalisation pris en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Le comportement est exactement identique à `api_id`, c.-à-d. que lorsque `api_id` n’est pas disponible lors de la création de campagnes, il est affiché sous forme de marque substitutive et il sera prévisualisé comme `dispatch_id_for_unsent_campaign`. L’ID est généré avant l’envoi du message et sera ajouté au moment de l’envoi.

{% alert warning %}
Le modèle liquide de `dispatch_id_for_unsent_campaign` ne fonctionne pas avec les messages in-app puisque les messages in-app n'ont pas de `dispatch_id`.
{% endalert %}

## Champ Dispatch ID Currents pour l’e-mail

Dans le but de continuer à améliorer nos capacités Currents, `dispatch_id` est également un champ dans les événements d'e-mail Currents pour tous les types de connecteurs. Le `dispatch_id` est l’ID unique généré pour chaque transmission (« dispatch ») envoyée depuis la plateforme Braze.

Alors que tous les clients qui reçoivent un message planifié reçoivent les mêmes `dispatch_id`, les clients qui reçoivent des messages basés sur des actions ou des API auront un `dispatch_id` unique par message. Le champ `dispatch_id` vous permet d’identifier l’instance d’une campagne récurrente qui est responsable de la conversion, ce qui vous fournit des informations supplémentaires et des informations sur les types de campagnes qui peuvent booster vos objectifs commerciaux.

Vous pouvez utiliser `dispatch_id` comme [étiquette de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), dans les [événements d'engagement aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) ou lorsque vous utilisez [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) ou [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) pour Currents.

_Dernière mise à jour le 15 juillet 2021_
