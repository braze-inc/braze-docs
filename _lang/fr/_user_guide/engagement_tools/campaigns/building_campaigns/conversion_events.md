---
nav_title: Événements de conversion
article_title: Événements de conversion
page_order: 5
page_type: tutorial
description: "Le présent article définit les événements de conversion, comment les utiliser et définir vos métriques de réussite au sein de Braze et comment utiliser ces outils pour voir le niveau d’engagement de vos utilisateurs."
tool: Campaigns

---
# Événements de conversion

> Le présent article définit les événements de conversion, comment les utiliser et définir vos métriques de réussite au sein de Braze et comment utiliser ces outils pour voir le niveau d’engagement de vos utilisateurs.
> <br>
> <br>
> En utilisant des événements de conversion, vous pouvez vous assurer de collecter des informations pertinentes et utiles que vous pouvez utiliser ultérieurement pour obtenir des informations sur votre campagne. 

Afin de suivre les métriques d’engagement et les détails nécessaires sur la manière dont la messagerie pilote vos indicateurs clés de performance, Braze vous permet de définir des événements de conversion pour chacune de vos campagnes et de vos Canvas.

Un événement de conversion est un type de métrique de réussite qui suit si un destinataire de vos messages effectue une action de grande valeur dans un délai défini après avoir reçu votre interaction. Vous pouvez ainsi commencer à attribuer ces actions précieuses aux différents points d’engagement qui touchent à l’utilisateur. 

Par exemple, si vous créez une campagne de vacances personnalisée pour les utilisateurs actifs, un événement de conversion de type **Démarrer la session** dans un délai de deux ou trois jours peut être approprié car il vous permettra d’obtenir une idée de l’engagement de l’utilisateur à recevoir votre message. Des événements supplémentaires comme **Réaliser un achat**, **Mettre à niveau l’application** ou l’un de vos événements personnalisés peuvent être sélectionnés comme événements de conversion.

Pour en savoir plus sur les conversions, consultez notre [Cours d’apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration de campagne !

## Événement de conversion primaire

L’événement de conversion primaire est le premier événement ajouté lors de la création de la campagne ou du Canvas. Cet événement est le plus important concernant votre engagement et votre signalement. Votre événement de conversion primaire est utilisé pour :

- Calculer la variation de message gagnante dans les campagnes et les Canvas [multivariés][4].
- Déterminer la fenêtre pour laquelle le revenu est calculé pour la campagne ou le Canvas.
- Ajuster les distributions des messages pour les campagnes et les Canvas en utilisant la [Sélection intelligente][5].

## Étape 1 : Créer une campagne avec suivi de conversion

Naviguez jusqu’à la page **Campaigns** dans le tableau de bord de votre société et cliquez sur **Créer la campagne**, puis sélectionnez le type de campagne que vous souhaitez créer.

Après avoir configuré les messages et la planification de votre campagne, vous aurez la possibilité d’ajouter jusqu’à quatre événements de conversion pour le suivi. 

Nous vous recommandons vivement d’utiliser autant d’événements de conversion que vous estimez nécessaires puisque l’ajout d’un deuxième événement de conversion (ou d’un troisième) peut enrichir considérablement votre rapport. Supposons par exemple que vous ayez une campagne qui cible les utilisateurs absents. Dans ce cas, ajouter un événement de conversion secondaire en plus du primaire qui est **Démarrer la session** peut vous permettre de mieux comprendre l’efficacité de votre campagne pour inciter vos utilisateurs à retourner vers votre application. 

## Étape 2 : Ajouter des événements de conversion

Pour chaque événement de conversion que vous souhaitez suivre, sélectionnez l’échéance de l’événement et de la conversion.

1. Sélectionnez le type général d’événement que vous souhaitez utiliser :
  - **Ouvre l’application** : Un utilisateur est compté comme ayant été converti lorsqu’il ouvre une des applications que vous avez spécifiées (par défaut toutes les applications du groupe d’apps).
  - **Effectue un achat** : Un utilisateur est compté comme ayant été converti lorsqu’il achète le produit que vous avez spécifié (par défaut, n’importe quel produit).
  - **Effectue un événement personnalisé** : Un utilisateur est compté comme ayant été converti lorsqu’il exécute l’un de vos événements personnalisés existants (aucun par défaut, vous devez spécifier l’événement).
  - **Met à niveau l’application** : Un utilisateur est compté comme ayant été converti lorsqu’il met à jour la version d’une des applications que vous avez spécifiées (par défaut toutes les applications du groupe d’apps). Braze effectuera une comparaison numérique au mieux pour déterminer si le changement de version était une mise à niveau. Par exemple, un utilisateur sera converti s’il a mis à niveau de la version 1.2.3 à la version 1.3.0 de l’application, mais Braze n’enregistrera pas une conversion si un utilisateur rétrograde de 1.2.3 à 1.2.2. Cependant, si le nom de la version de l’application contient des chaînes de caractères, comme « 1.2.3-beta2 », alors Braze ne pourra pas déterminer si le changement de version était une mise à niveau. Dans cette situation, Braze la comptera comme une conversion lorsque la version d’application la plus récente de l’utilisateur est modifiée.<br><br>
2. Définissez votre date limite de conversion. Il s’agit du temps maximum qui peut s’écouler pour envisager une conversion. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.  

![Le type d’événement de conversion « Effectue un achat » utilisé comme exemple pour enregistrer les conversions des utilisateurs qui effectuent un achat. Il a une date limite de conversion de 12 heures.][2]

Une fois que vous avez sélectionné vos événements de conversion, continuez le processus de création de campagne et commencez à l’envoyer.

## Étape 3 : Afficher les résultats

Naviguez jusqu’à la page **Détails** pour afficher les détails de chaque événement de conversion associé à la campagne que vous venez de créer. Quels que soient vos événements de conversion sélectionnés, vous pouvez également voir le revenu total qui peut être attribué à cette campagne spécifique, ainsi qu’à ses variantes spécifiques, durant la période de l’événement de conversion primaire.

{% alert note %}
S’il n’y a pas d’événement de conversion sélectionné lors de la création de la campagne, la période par défaut est de trois jours. 
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et le pourcentage de conversion pour votre groupe de contrôle ainsi que chaque variante.

![][3]

## Règles de suivi de conversion

Les événements de conversion vous permettent d’attribuer une action utilisateur à un point d’engagement. Cela dit, il y a quelques éléments à prendre en compte concernant la manière dont Braze gère les conversions multiples. Découvrez les scénarios suivants pour comprendre comment Braze suit ces conversions :

- Un utilisateur peut se convertir une fois seulement pour chaque événement de conversion d’une campagne ou d’un Canvas. Par exemple, supposons qu’une campagne ne comporte qu’un seul événement de conversion qui est « Effectue n’importe quel achat ». Si un utilisateur qui reçoit cette campagne effectue deux achats distincts avant la date limite de conversion, une seule conversion sera comptée.
- Si un utilisateur effectue un événement de conversion dans les délais de conversion de deux campagnes ou Canvas distincts qu’il a reçus, la conversion s’enregistrera pour les deux.
- Un utilisateur comptera comme s’étant converti s’il a effectué l’événement de conversion spécifique durant la période, même s’il n’a pas ouvert ou cliqué sur le message.

[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[3]: {% image_buster /assets/img_archive/conversion_event_details.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing
[5]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/#intelligent-selection