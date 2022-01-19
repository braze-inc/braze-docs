---
nav_title: Événements de conversion
article_title: Événements de conversion
page_order: 5
page_type: tutoriel
description: "Cet article définit les événements de conversion, comment les utiliser et définir vos paramètres de succès au Brésil, et comment utiliser ces outils pour voir à quel point vos utilisateurs sont engagés."
tool: Campagnes
---

# Événements de conversion

> Cet article définit les événements de conversion, comment les utiliser et définir vos paramètres de succès au Brésil, et comment utiliser ces outils pour voir à quel point vos utilisateurs sont engagés. <br> <br> En utilisant des événements de conversion, vous pouvez vous assurer que vous collectez des éléments pertinents, des informations utiles que vous pourrez utiliser plus tard pour obtenir un aperçu de votre campagne.

Afin de suivre les métriques d'engagement et les détails nécessaires concernant la façon dont la messagerie conduit vos KPI, Braze vous permet de définir des événements de conversion pour chacune de vos campagnes et Canvases.

Un événement de conversion est un type de mesure de succès qui indique si un destinataire de votre messagerie effectue une action de haute valeur dans un délai défini après avoir reçu votre engagement. Avec cela, vous pouvez commencer à attribuer ces actions précieuses aux différents points d'engagement atteignant l'utilisateur.

Par exemple, si vous créez une campagne de vacances personnalisée pour les utilisateurs actifs, un événement de conversion de **Démarrer une session** dans les deux ou trois jours peut être approprié car il vous permettra de gagner un sens de l'engagement de l'utilisateur de recevoir votre message. Des événements supplémentaires comme **Effectuer un achat**, **mettre à niveau l'app**, ou n'importe lequel de vos événements personnalisés peuvent être sélectionnés comme des événements de conversion.

Pour en savoir plus sur les conversions, consultez notre [cours de mise en place de campagne](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

## Événement de conversion primaire

L'événement principal de conversion est le premier événement ajouté lors de la campagne ou de la création de Canvas . Cet événement a la plus grande incidence sur votre engagement et vos rapports. Votre événement de conversion principal est utilisé à:

- Calculez la variation du message gagnant dans [campagnes multivariées ou Canvases][4].
- Déterminez la fenêtre lorsque les revenus sont calculés pour la campagne ou Canvas.
- Ajuster les distributions de messages pour les campagnes et les toiles en utilisant [Sélection intelligente][5].

## Étape 1 : Créer une campagne avec le suivi de conversion

Accédez à la page des [Campagnes][1] dans le tableau de bord de votre entreprise et cliquez sur **Créer une Campagne**, puis sélectionnez le type de campagne que vous souhaitez créer.

Après avoir configuré les messages de votre campagne et — pour des campagnes non API — planifiées, vous aurez la possibilité d'ajouter jusqu'à quatre événements de conversion pour le suivi.

Nous vous recommandons fortement d'utiliser autant d'événements de conversion que vous jugez nécessaires car l'ajout d'un deuxième (ou troisième) événement de conversion peut enrichir considérablement vos rapports. Par exemple, disons que vous avez une campagne qui cible les utilisateurs qui sont en train de disparaître. Dans ce cas, ajouter un événement de conversion secondaire en plus de l'événement principal de conversion **Démarre la session** peut vous aider à mieux comprendre l'efficacité de votre campagne pour réintroduire vos utilisateurs dans votre application.

## Étape 2 : Ajouter des événements de conversion

Pour chaque événement de conversion que vous souhaitez suivre, sélectionnez la date limite d'événement et de conversion :

1. Sélectionnez le type général d'événement que vous souhaitez utiliser :
  - **Ouvre l'application**: Un utilisateur est compté comme ayant converti lorsqu'il ouvre une des applications que vous spécifiez (par défaut, toutes les applications du groupe d'applications).
  - **Effectue un achat**: Un utilisateur est compté comme ayant converti lors de l'achat du produit que vous spécifiez (par défaut, n'importe quel produit).
  - **Effectue un événement personnalisé**: Un utilisateur est compté comme ayant converti lorsqu'il exécute un de vos événements personnalisés existants (pas de valeur par défaut, vous devez spécifier l'événement).
  - **Application de mise à niveau**: Un utilisateur est compté comme ayant converti lorsqu'il met à niveau la version de l'application sur l'une des applications que vous spécifiez (par défaut, toutes les applications du groupe d'applications). Braze effectuera une comparaison numérique des meilleurs efforts pour déterminer si le changement de version est une mise à jour. Par exemple, un utilisateur peut convertir s'il passe de la version 1.2.3 à la 1.3. de l'application, mais Braze n'enregistrerait pas de conversion si un utilisateur passe de la 1.2.3 à la 1.2.2. Cependant, si le nom de version de l'application contient des chaînes, comme « 1.2 ». -beta2", alors Braze ne sera pas en mesure de déterminer si un changement de version est une mise à jour. Dans ce cas, Braze le comptera comme une conversion lorsque la dernière version de l'application de l'utilisateur changera.<br><br>
2. Définissez votre date limite de conversion. Il s'agit de la durée maximale qui peut passer pour envisager une conversion. Vous avez la possibilité d'autoriser jusqu'à une fenêtre de 30 jours au cours de laquelle une conversion sera comptée si l'utilisateur prend l'action spécifiée.

!\[Sélection de l'événement de conversion\]\[2\]

Une fois que vous avez sélectionné vos événements de conversion, continuez le processus de création de la campagne et commencez à envoyer votre campagne.

## Étape 3 : Voir les résultats

Accédez à la page **Détails** pour afficher les détails de chaque événement de conversion associé à la campagne que vous venez de créer. Indépendamment des événements de conversion sélectionnés, vous pouvez également voir les revenus totaux qui peuvent être attribués à cette campagne spécifique, ainsi que des variantes spécifiques, dans la fenêtre de l'événement de conversion primaire.

{% alert note %}
S'il n'y a pas d'événement de conversion sélectionné lors de la création de la campagne, la période par défaut est de trois jours.
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et de pourcentages de conversion pour votre groupe de contrôle et chaque variante.

!\[Voir les résultats\]\[3\]

## Règles de suivi de conversion

Les événements de conversion vous permettent d'attribuer l'action utilisateur à un point d'engagement. Cela dit, il y a quelques choses à noter concernant la façon dont Braze gère les conversions multiples. Consultez les scénarios suivants pour comprendre comment Braze ces conversions :

- Un utilisateur ne peut convertir qu'une seule fois à chaque événement de conversion pour une campagne ou Canvas. Par exemple, supposons qu'une campagne n'a qu'un seul événement de conversion qui est "faire n'importe quel achat". Si un utilisateur qui reçoit cette campagne fait deux achats distincts dans le délai de conversion, alors une seule conversion sera comptabilisée.
- Si un utilisateur exécute un événement de conversion dans les délais de conversion de deux campagnes séparées ou de Canvases qu'il a reçues, alors la conversion s'inscrira sur les deux.
- Un utilisateur comptera comme converti s'il a effectué l'événement de conversion spécifique dans la fenêtre, même s'il n'a pas ouvert ou cliqué sur le message.
[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %} [3]: {% image_buster /assets/img_archive/conversion_event_details.png %}

[1]: https://dashboard-01.braze.com/engagement/campaigns/ "Campaigns Page"
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing
[5]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/#intelligent-selection