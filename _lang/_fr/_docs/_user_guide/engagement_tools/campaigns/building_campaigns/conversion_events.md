---
nav_title: Événements de conversion
article_title: Événements de conversion
page_order: 5
page_type: tutoriel
description: "Cet article pratique va au-delà de ce que sont les événements de conversion, comment les utiliser et définir vos paramètres de succès au Brésil, et comment utiliser ces outils pour voir à quel point vos utilisateurs sont engagés"
tool: Campagnes
---

# Événements de conversion

> Cet article pratique va au-delà de ce que sont les événements de conversion, comment les utiliser et définir vos paramètres de succès au Brésil, ainsi que la façon d'utiliser ces outils pour voir à quel point vos utilisateurs sont engagés. <br> <br> En utilisant des événements de conversion, vous pouvez vous assurer que vous collectez des éléments pertinents, des informations utiles que vous pourrez utiliser plus tard pour obtenir un aperçu de votre campagne.

Afin de suivre les métriques d'engagement et les détails nécessaires concernant la façon dont la messagerie conduit vos KPI, Braze vous permet de définir des événements de conversion pour chacune de vos campagnes et Canvases.

Un événement de conversion est un type de mesure de succès qui indique si un destinataire de votre messagerie effectue une action de haute valeur dans un délai défini après avoir reçu votre engagement. Avec cela, vous pouvez commencer à attribuer ces actions précieuses aux différents points d'engagement atteignant l'utilisateur. Par exemple, si vous créez une campagne de vacances personnalisée pour les utilisateurs actifs, un événement de conversion de "Démarre la session" dans les 2 ou 3 jours peut être approprié, car cela vous permettra alors de comprendre le rythme auquel votre engagement a aidé les utilisateurs à revenir après avoir reçu votre message.

Pour en savoir plus sur les conversions, consultez notre [cours de mise en place de campagne](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

Avec "Faire un achat", des événements comme "Démarrer une session", "Mettre à niveau l'application", ou n'importe lequel de vos événements personnalisés peuvent être sélectionnés comme des événements de conversion. Vous trouverez ci-dessous plus de détails sur la fonctionnalité, ainsi que les étapes nécessaires à leur mise en œuvre.

## Événement de conversion primaire

L'événement de conversion primaire est le premier événement ajouté lors de la création de la campagne ou de la toile et c'est celui qui a le plus d'influence sur votre engagement et vos rapports. Il est utilisé à:

- Calculez la variation des messages gagnants dans les campagnes multivariées ou les Canvases.
- Déterminez la fenêtre dans laquelle les revenus sont calculés pour la campagne ou Canvas.
- Ajuster les distributions de messages pour les campagnes et les toiles en utilisant la sélection intelligente.

## Étape 1 : Créer une campagne avec le suivi de conversion

Accédez à la page des [Campagnes][1] dans le tableau de bord de votre entreprise et cliquez sur **Créer une Campagne**, puis sélectionnez le type de campagne que vous souhaitez créer.

Après avoir configuré les messages de votre campagne et — pour des campagnes non API — planifiées, vous aurez la possibilité d'ajouter jusqu'à quatre événements de conversion pour le suivi. Nous vous recommandons fortement d'en utiliser autant que vous le jugez nécessaire, comme l'ajout d'une deuxième (ou troisième) événement de conversion peut considérablement enrichir vos rapports. Par exemple, si vous aviez une campagne ou Canvas ciblant les utilisateurs en train de disparaître, bien qu'un événement de conversion de "Démarrage de la session" centré sur la rétention soit utile dans les 3 jours, peut-être que vous voulez aussi ajouter un événement de conversion secondaire de la réalisation d'un autre événement personnalisé de grande valeur. De cette façon, vous pouvez replonger dans le tableau de bord et comprendre non seulement dans quelle mesure votre campagne ou Canvas repousse les utilisateurs dans votre application, mais aussi à quel point ces sessions sont actives et impliquées.

## Étape 2 : Ajouter des événements de conversion

Pour chaque événement de conversion que vous souhaitez suivre, sélectionnez la date limite d'événement et de conversion :

1. Sélectionnez le type général d'événement que vous souhaitez utiliser.<br>!\[Sélection d'événement de conversion\]\[2\]<br><br>
  - __Ouvre l'application__: Un utilisateur est compté comme ayant converti lorsqu'il ouvre une des applications que vous spécifiez (par défaut, toutes les applications du groupe d'applications).
  - __Effectue un achat__: Un utilisateur est compté comme ayant converti lors de l'achat du produit que vous spécifiez (par défaut, n'importe quel produit).
  - __Effectue un événement personnalisé__: Un utilisateur est compté comme ayant converti lorsqu'il exécute un de vos événements personnalisés existants (pas de valeur par défaut, vous devez spécifier l'événement).
  - __Application de mise à niveau__: Un utilisateur est compté comme ayant converti lorsqu'il met à niveau la version de l'application sur l'une des applications que vous spécifiez (par défaut, toutes les applications du groupe d'applications). Braze effectuera une comparaison numérique des meilleurs efforts pour déterminer si le changement de version était, en fait, une mise à niveau. Par exemple, un utilisateur peut convertir s'il passe de la version 1.2.3 à la 1.3. de l'application, tandis que Braze n'enregistrera pas de conversion si un utilisateur passe de 1.2.3 à 1.2.2. Cependant, si les noms de version de l'application contiennent des chaînes, comme « 1.2 ». -beta2", alors Braze ne sera pas en mesure de déterminer si un changement de version était, en fait, une mise à niveau. Dans ce cas, Braze le comptera comme une conversion lorsque la version la plus récente de l'application de l'utilisateur changera.<br><br>
2. Définir un "délai de conversion". Vous avez la possibilité d'autoriser jusqu'à une fenêtre de 30 jours au cours de laquelle une conversion sera comptée si l'utilisateur prend l'action spécifiée.

Une fois que vous avez sélectionné vos événements de conversion, continuez le processus de création de la campagne et commencez à envoyer votre campagne.

## Étape 3 : Voir les résultats

Accédez à la page **Détails** pour afficher les détails de chaque événement de conversion associé à la campagne que vous venez de créer. Indépendamment des événements de conversion sélectionnés, vous pouvez également voir les revenus totaux qui peuvent être attribués à cette campagne spécifique — ainsi que des variantes spécifiques — pendant la fenêtre de l'événement de conversion primaire.

{% alert note %}
Si aucun événement de conversion n'a été sélectionné lors de la création de la campagne, la période par défaut est de 3 jours.
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et de pourcentages de conversion pour votre groupe de contrôle et chaque variante.

!\[Voir les résultats\]\[3\]

## Règles de suivi de conversion

Les événements de conversion vous permettent d'attribuer l'action utilisateur à un point d'engagement. Cela dit, il y a quelques choses à noter concernant la façon dont Braze gère les conversions quand il y a plusieurs en jeu. Veuillez trouver les scénarios décrits ci-dessous.

- Un utilisateur ne peut convertir qu'une seule fois à chaque événement de conversion pour une campagne ou Canvas. Par exemple, supposons qu'une campagne n'a qu'un seul événement de conversion qui est "faire n'importe quel achat". Si un utilisateur qui reçoit cette campagne fait 2 achats distincts dans le délai de conversion, une seule conversion sera comptabilisée.
- Si un utilisateur exécute un événement de conversion dans les délais de conversion de deux campagnes séparées ou de Canvases qu'il a reçues, la conversion s'inscrira sur les deux.
- Un utilisateur comptera comme converti s'il a effectué l'événement de conversion spécifique dans la fenêtre même s'il n'a pas ouvert/cliqué sur le message
[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %} [3]: {% image_buster /assets/img_archive/conversion_event_details.png %}

[1]: https://dashboard-01.braze.com/engagement/campaigns/ "Campaigns Page"
