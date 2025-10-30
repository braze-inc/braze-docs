---
nav_title: Les bases de la campagne
article_title: Les bases de la campagne
page_order: 1
page_type: reference
description: "Cet article de référence présente les bases des campagnes, en abordant différentes questions que vous devriez vous poser lorsque vous implantez vos premières campagnes."
tool: Campaigns

---

# L'essentiel des campagnes

> Cet article de référence présente les bases des campagnes, en abordant différentes questions que vous devriez vous poser lorsque vous implantez vos premières campagnes.

## Comprendre la structure de la campagne

Avant d'aborder les moindres détails de l'implémentation des campagnes, identifions les éléments clés permettant de comprendre le fonctionnement des campagnes sur les différents canaux d'envoi de messages.

Les campagnes sont une étape de message unique pour se connecter à vos utilisateurs sur les canaux, ou plus communément appelés canaux d'envoi de messages. Ces canaux d'envoi de messages comprennent les cartes de contenu, les e-mails, les messages in-app, le push, les SMS et MMS, et les webhooks. En comprenant où résident vos personnalisés, vous pouvez exploiter les canaux d'envoi de messages appropriés pour communiquer.

## Créer le parcours client

Les campagnes pouvant être créées de manière unique en fonction du canal d'envoi des messages, vous pouvez utiliser ces cinq W de la visualisation pour vous aider à identifier et à conceptualiser vos stratégies et vos objectifs en matière d'engagement client.

### Le "quoi" : Donnez un nom à votre campagne

> Qu'essayez-vous d'aider l'utilisateur à faire ou à comprendre ?

Ne sous-estimez jamais le pouvoir du nom. Braze est créé pour la collaboration, c'est donc le moment idéal pour vous familiariser avec la manière dont vous communiquerez vos objectifs à votre équipe. Pour en savoir plus sur les parcours clients, consultez notre cours d'apprentissage Braze sur [le mappage des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles)!

### Le "quand" : Créer des conditions de départ

> Quand le client sera-t-il confronté à cette campagne ? 

Les utilisateurs peuvent entrer dans votre campagne de trois façons : à une date et une heure définies (planifiées), lorsqu'ils effectuent une action spécifique (basées sur l'action) ou lorsqu'ils font quelque chose qui déclenche un appel API (déclenchées par l'API). 

La réception/distribution planifiée consiste à ajuster vos campagnes pour qu'elles soient envoyées à une heure précise et, éventuellement, selon une cadence déterminée. Les campagnes basées sur l'action répondent à des comportements spécifiques des clients au fur et à mesure qu'ils se produisent en temps réel. Il peut s'agir d'effectuer un achat ou d'interagir avec une autre campagne. Des campagnes déclenchées par l'API peuvent être mises en place pour déterminer les actions clés des clients sur votre plateforme qui, une fois réalisées, déclencheront un appel API vers Braze et enverront vos campagnes.

### Le "qui" : Sélectionnez une audience

> Qui cherchez-vous à atteindre ? 

Vous pouvez utiliser des [segments]({{site.baseurl}}/user_guide/engagement_tools/segments) prédéfinis pour cibler les utilisateurs en fonction de leurs caractéristiques démographiques, comportementales ou techniques et de leurs actions. Ajoutez d'autres filtres lorsque vous créez votre campagne afin d'adapter davantage votre segmentation. Seuls les utilisateurs qui correspondent à ces critères d'audience cible peuvent accéder au voyage. Consultez ce tableau pour un résumé rapide des types de filtres disponibles.

| Filtre | Description |
|---|---|
| Données personnalisées | Segmentez les utilisateurs en fonction des événements et des attributs que vous définissez. Peut utiliser des fonctionnalités spécifiques à votre produit. |
| Activité de l'utilisateur | Segmentez les clients en fonction de leurs actions et de leurs achats. |
| Reciblage | Segmentez les clients qui ont été envoyés, reçus ou qui ont interagi avec des campagnes précédentes. |
| Activité de marketeur | Segmentez les clients en fonction de comportements universels comme le dernier engagement ou les campagnes reçues. |
| Attributs de l'utilisateur | Segmenter les clients en fonction de leurs attributs et caractéristiques constants. |
| Attribution d'installation | Segmentez les clients en fonction de leur première source, du groupe d'annonces, de la campagne ou de l'annonce. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Le "pourquoi" : Identifier les événements de conversion

> Pourquoi créez-vous cette campagne ? 

Il est toujours important d'avoir un objectif défini en tête, et les campagnes vous aident à comprendre vos performances par rapport à des indicateurs clés de performance tels que l'engagement des sessions, les achats et les événements personnalisés. En sélectionnant au moins un [événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), vous aurez la possibilité de comprendre les performances de votre campagne.

### Le "où" : Trouver mon audience

> Où puis-je atteindre au mieux mon audience ?

C'est ici que nous déterminons quels canaux de communication sont les plus judicieux pour votre parcours utilisateur. Idéalement, vous souhaitez atteindre vos utilisateurs là où ils sont le plus actifs.

### Le "comment" : Créer l'expérience

> Comment créer ma campagne après avoir identifié les cinq "W" ?

Envisagez d'implémenter des variantes et des tests A/B à mesure que vous vous familiarisez avec la création de campagnes. Notez que les campagnes prennent en charge jusqu'à huit variantes avec un groupe de contrôle. Utilisez les analyses/analytiques de votre campagne pour faire des choix éclairés au fur et à mesure que vous créez votre campagne, en ajustant tout ce qui va de votre audience segmentée au contenu de votre envoi messages.

