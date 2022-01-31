---
nav_title: Comportement de l'ID d'expédition
article_title: Comportement de l'ID d'expédition
page_order: 1
page_type: Solution
description: "Cet article couvre le comportement de l'ID d'expédition, y compris son utilisation, ses implications et ses limites."
---

# Comportement de l'ID d'envoi

Un `dispatch_id` est l'ID du message dispatch-a unique ID pour chaque "transmission" envoyée depuis Braze. Les utilisateurs qui envoient un message programmé obtiennent le même `dispatch_id`, alors que les messages déclenchés par une action ou une API recevront un `dispatch_id unique` par utilisateur.

{% alert important %}
Notez que `dispatch_ids` sont par utilisateur, par campagne pour les messages déclenchés (basés sur l'action ou déclenchés par API).
{% endalert %}

Cela peut faire que deux utilisateurs différents aient des `dispatch_ids différents` pour une seule campagne si les messages ont été envoyés à deux reprises différentes. Ceci est souvent dû au fait que les requêtes API ont été faites séparément. Si les deux utilisateurs étaient dans le même public de campagne en un seul envoi, leurs identifiants d'expédition seraient les mêmes.

## Comportement de l'ID d'envoi dans les campagnes

Les messages de campagne programmés obtiennent le même `dispatch_id`. Les messages de campagne basés sur l'action ou sur l'API recevront un `dispatch_id unique` par utilisateur.

Les campagnes multi-canaux auront le même comportement que celui décrit ci-dessus.

Par exemple, si Becky et Tom sont tous deux inclus dans votre public de campagne planifiée, alors ils auront le même `dispatch_id`.

S'ils sont inclus dans l'audience d'une campagne déclenchée par l'API, ils auront différents `dispatch_ids`.

{% alert warning %}
Les identifiants d'expédition sont générés aléatoirement pour toutes les étapes de Canvas parce que Braze traite les Étapes Canvas comme des événements déclenchés, même lorsqu'ils sont « planifiés ». Cela peut entraîner des incohérences générant les ids. Parfois, une étape de Canvas aura des `dispatch_ids uniques` par utilisateur par envoi, ou il peut avoir partagé `dispatch_ids` entre les utilisateurs par envoi.
{% endalert %}

## Modèle d'ID d'envoi dans les messages avec Liquid

Si vous voulez suivre l'envoi d'un message depuis l'intérieur du message (dans une URL, par exemple), vous pouvez modéliser dans le `dispatch_id`. Vous pouvez trouver le formatage pour cela dans notre liste de balises de personnalisation supportées, sous [Attributs de canvas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Cela se comporte comme `api_id`, car l'api_id `api_id` n'est pas disponible lors de la création de la campagne, elle est tempérée en tant que placeholder et sera prévisualisée comme `dispatch_id_for_unsent_campaign`. L'identifiant est généré avant l'envoi du message, et sera inclus dans l'heure d'envoi.

{% alert warning %}
Les modèles liquides de `dispatch_id_for_unsent_campaign` ne fonctionnent pas avec les messages dans l'application, car les messages dans l'application n'ont pas de `dispatch_id`.
{% endalert %}

## Champ Devises d'envoi pour l'e-mail

Dans le but de continuer à améliorer nos capacités de courants, nous ajoutons `dispatch_id` en tant que champ aux événements Courriel courants pour tous les types de connecteurs.

Le `dispatch_id` est l'id unique généré pour chaque transmission – ou expédition – envoyée depuis la plateforme Braze.

Alors que tous les clients qui reçoivent un message planifié reçoivent le même `dispatch_id`, les clients qui reçoivent des messages basés sur l'action ou sur l'API recevront un `dispatch_id unique` par message. Le champ `dispatch_id` vous permet d'identifier quelle instance d'une campagne récurrente est responsable de la conversion, ainsi vous disposez de plus d'informations et de plus amples informations sur les types de campagnes qui vous aident à pousser l'aiguille sur vos objectifs commerciaux.

Vous pouvez utiliser `dispatch_id` comme une [étiquette de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), dans [Événements d'engagement de message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/), ou lorsque vous utilisez [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events), ou [Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/) pour Courants.

_Dernière mise à jour le 15 juillet 2021_
