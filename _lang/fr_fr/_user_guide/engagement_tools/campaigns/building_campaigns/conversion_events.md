---
nav_title: Événements de conversion
article_title: Événements de conversion
page_order: 5
page_type: tutorial
description: "Le présent article définit les événements de conversion, comment les utiliser et définir vos indicateurs de réussite au sein de Braze et comment utiliser ces outils pour voir le niveau d’engagement de vos utilisateurs."
tool: Campaigns

---
# Événements de conversion

> En utilisant des événements de conversion, vous pouvez vous assurer de collecter des informations pertinentes et utiles que vous pouvez utiliser ultérieurement pour obtenir des informations sur votre campagne. 

Pour suivre les indicateurs d'engagement et les détails nécessaires concernant la façon dont l'envoi de messages stimule vos indicateurs clés de performance, Braze vous permet de définir des événements de conversion pour chacune de vos campagnes et Canevas.

Un événement de conversion est un type de métrique de réussite qui suit si un destinataire de vos messages effectue une action de grande valeur dans un délai défini après avoir reçu votre interaction. Vous pouvez ainsi commencer à attribuer ces actions précieuses aux différents points d’engagement qui touchent à l’utilisateur. 

Par exemple, si vous créez une campagne de vacances personnalisée pour les utilisateurs actifs, un événement de conversion de **Démarrer une session** dans les deux ou trois jours peut être approprié car il vous permettra de recueillir un sentiment d'engagement de l'utilisateur à partir de la réception de votre message. Des événements supplémentaires tels que l'**achat**, la **mise à niveau de l'application** ou tout autre événement personnalisé peuvent être sélectionnés en tant qu'événements de conversion.

Pour en savoir plus sur les conversions, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes !

## Événement de conversion primaire

L’événement de conversion principal est le premier événement ajouté lors de la création de la campagne ou du Canvas. Cet événement est le plus important concernant votre engagement et votre signalement. Votre événement de conversion principal est utilisé pour :

- Calculez la variation du message gagnant dans [les campagnes multivariées][4] ou Canvases.
- Déterminez la fenêtre pour laquelle le revenu est calculé pour la campagne ou le canvas.
- Ajustez les distributions des messages pour les campagnes et les canvas en utilisant la [sélection intelligente][5].

{% alert note %}
Si les messages sont annulés à l'aide de l'étiquette Liquid `abort`, seuls les utilisateurs qui passent par les variantes sont potentiellement annulés. Cela signifie que les messages adressés aux utilisateurs qui passent par le groupe de contrôle ne seront pas interrompus, ce qui peut conduire à des pourcentages de conversion faussés entre les variantes et les groupes de contrôle. En guise de solution de contournement, utilisez la [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) pour cibler vos utilisateurs à l'entrée de la campagne et du canvas.
{% endalert %}

## Étape 1 : Créer une campagne avec suivi de conversion

[Créez une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) pour le canal de messages que vous souhaitez. Après avoir configuré les messages et la planification de votre campagne, vous aurez la possibilité d’ajouter jusqu’à quatre événements de conversion pour le suivi.

Nous vous recommandons vivement d'utiliser autant d'événements de conversion que vous le jugez nécessaire, car l'ajout d'un deuxième (ou d'un troisième) événement de conversion peut considérablement enrichir votre rapport. Supposons par exemple que vous ayez une campagne qui cible les utilisateurs absents. Dans ce cas, l'ajout d'un événement de conversion secondaire et de l'événement de conversion principal **Starts Session** peut vous permettre de mieux comprendre l'efficacité de votre campagne pour ce qui est de ramener vos utilisateurs dans votre application. 

## Étape 2 : Ajouter des événements de conversion

Pour chaque événement de conversion dont vous souhaitez assurer le suivi, sélectionnez l'événement et la date limite de conversion.

1. Sélectionnez le type général d’événement que vous souhaitez utiliser :
  - **Lance la session** : Un utilisateur est considéré comme converti lorsqu'il ouvre l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail).
  - **Effectue un achat** : Un utilisateur est compté comme ayant été converti lorsqu’il achète le produit que vous avez spécifié (par défaut, n’importe quel produit).
  - **Effectue un événement personnalisé**: Un utilisateur est compté comme ayant été converti lorsqu’il exécute l’un de vos événements personnalisés existants (aucun par défaut, vous devez spécifier l’événement).
  - **Met à niveau l'application** : Un utilisateur est considéré comme converti lorsqu'il met à jour la version de l'application dans l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). Braze effectuera une comparaison numérique au mieux pour déterminer si le changement de version était une mise à niveau. Par exemple, un utilisateur sera converti s’il a mis à niveau de la version 1.2.3 à la version 1.3.0 de l’application, mais Braze n’enregistrera pas une conversion si un utilisateur rétrograde de 1.2.3 à 1.2.2. Cependant, si le nom de la version de l’application contient des chaînes de caractères, comme « 1.2.3-beta2 », alors Braze ne pourra pas déterminer si le changement de version était une mise à niveau. Dans cette situation, Braze la comptera comme une conversion lorsque la version d’application la plus récente de l’utilisateur est modifiée.
  - **Ouvre l’e-mail** : Un utilisateur est considéré comme converti lorsqu'il ouvre l'e-mail (uniquement pour les campagnes d'e-mailing).
  - **Clique sur l’e-mail** : Un utilisateur est considéré comme converti lorsqu'il clique sur un lien dans l'e-mail (uniquement pour les campagnes d'e-mailing).<br><br>
2. Définissez votre date limite de conversion. Il s’agit du temps maximum qui peut s’écouler pour envisager une conversion. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle la conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.  

![Le type d’événement de conversion « Effectue un achat » utilisé comme exemple pour enregistrer les conversions des utilisateurs qui effectuent un achat. Il a une date limite de conversion de 12 heures.][2]

Une fois que vous avez sélectionné vos événements de conversion, continuez le processus de création de campagne et commencez à l’envoyer.

## Étape 3 : Afficher les résultats

Accédez à la page **Détails** pour afficher les détails de chaque événement de conversion associé à la campagne que vous venez de créer. Quels que soient vos événements de conversion sélectionnés, vous pouvez également voir le revenu total qui peut être attribué à cette campagne spécifique, ainsi qu’à ses variantes spécifiques, durant la période de l’événement de conversion principal.

{% alert note %}
Si aucun événement de conversion n'a été sélectionné lors de la création de la campagne, le délai est fixé par défaut à trois jours.
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et le pourcentage de conversion pour votre groupe de contrôle ainsi que chaque variante.

![][3]

## Règles de suivi de conversion

Les événements de conversion vous permettent d’attribuer une action utilisateur à un point d’engagement. Cela dit, il y a quelques éléments à prendre en compte concernant la manière dont Braze gère les conversions multiples. Découvrez les scénarios suivants pour comprendre comment Braze suit ces conversions :

- Les conversions se font par utilisateur et non par appareil. Cela signifie qu'un utilisateur ne peut se convertir qu'une seule fois, même si un message est envoyé sur plusieurs appareils. Autre exemple, supposons qu'une campagne ne comporte qu'un seul événement de conversion, à savoir "Effectue un achat". Si un utilisateur qui reçoit cette campagne effectue deux achats distincts avant la date limite de conversion, une seule conversion sera comptée.
- Si un utilisateur effectue un événement de conversion dans les délais de conversion de deux campagnes ou Canvas distincts qu’il a reçus, la conversion s’enregistrera pour les deux.
- Un utilisateur comptera comme s’étant converti s’il a effectué l’événement de conversion spécifique durant la période, même s’il n’a pas ouvert ou cliqué sur le message.

[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[3]: {% image_buster /assets/img_archive/conversion_event_details.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing
[5]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
