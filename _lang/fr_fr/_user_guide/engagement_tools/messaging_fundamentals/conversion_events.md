---
nav_title: Événements de conversion
article_title: Événements de conversion
page_order: 4
page_type: reference
description: "Cet article de référence définit les événements de conversion, comment les utiliser pour définir vos indicateurs de réussite dans Braze, et comment utiliser ces événements pour connaître l'engagement de vos utilisateurs."
tool:
    - Campaigns
    - Canvas
---

# Événements de conversion

> Un événement de conversion est un type d'indicateur de réussite qui permet de savoir si un destinataire de votre message effectue une action à forte valeur ajoutée dans un laps de temps déterminé après avoir reçu votre envoi. Utilisez ces événements pour vous assurer que vous recueillez des informations pertinentes et utiles que vous pourrez ensuite utiliser pour obtenir des informations pour votre campagne ou votre Canvas.

## Fonctionnement

Disons que vous créez une campagne de vacances personnalisée pour les utilisateurs actifs, un événement de conversion de **Démarrer une session** dans les deux ou trois jours peut être approprié car il vous permettra de recueillir un sentiment d'engagement de l'utilisateur à partir de la réception de votre message. Des événements supplémentaires tels que l'**achat**, la **mise à niveau de l'application** ou tout autre événement personnalisé peuvent être sélectionnés en tant qu'événements de conversion.

{% alert tip %}
Pour en savoir plus sur les conversions, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes.
{% endalert %}

### Règles de suivi de conversion

Les événements de conversion vous permettent d’attribuer une action utilisateur à un point d’engagement. Cela dit, il y a quelques éléments à prendre en compte concernant la manière dont Braze gère les conversions multiples. Découvrez les scénarios suivants pour comprendre comment Braze suit ces conversions :

- Les conversions se font par utilisateur et non par appareil. Cela signifie qu'un utilisateur ne peut se convertir qu'une seule fois, même si un message est envoyé sur plusieurs appareils. Autre exemple, supposons qu'une campagne ne comporte qu'un seul événement de conversion, à savoir "Effectue un achat". Si un utilisateur qui reçoit cette campagne effectue deux achats distincts avant la date limite de conversion, une seule conversion sera comptée.
- Si un utilisateur effectue un événement de conversion dans les délais de conversion de deux campagnes ou Canvas distincts qu’il a reçus, la conversion s’enregistrera pour les deux.
- Un utilisateur comptera comme s’étant converti s’il a effectué l’événement de conversion spécifique durant la période, même s’il n’a pas ouvert ou cliqué sur le message.

### Événement de conversion primaire

L’événement de conversion principal est le premier événement ajouté lors de la création de la campagne ou du Canvas. Cet événement est le plus important concernant votre engagement et votre signalement. Votre événement de conversion principal est utilisé pour :

- Calculez la variation du message gagnant dans les campagnes [multivariées]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) ou les canevas.
- Déterminez la fenêtre pour laquelle le revenu est calculé pour la campagne ou le canvas.
- Ajustez la distribution des messages pour les campagnes et les toiles à l'aide de la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% alert note %}
Si les messages sont annulés à l'aide de l'étiquette Liquid `abort`, seuls les utilisateurs qui passent par les variantes sont potentiellement annulés. Cela signifie que les messages adressés aux utilisateurs qui passent par le groupe de contrôle ne seront pas interrompus, ce qui peut conduire à des pourcentages de conversion faussés entre les variantes et les groupes de contrôle. En guise de solution de contournement, utilisez la [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) pour cibler vos utilisateurs à l'entrée de la campagne et du canvas.
{% endalert %}

## Création d'une campagne avec suivi des conversions

### Étape 1 : Implémentez votre campagne

[Créez une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) pour le canal de messages que vous souhaitez. Après avoir configuré les messages et la planification de votre campagne, vous aurez la possibilité d’ajouter jusqu’à quatre événements de conversion pour le suivi.

Nous vous recommandons d'utiliser autant d'événements de conversion que vous le jugez nécessaire, car l'ajout d'un deuxième (ou d'un troisième) événement de conversion peut considérablement enrichir votre rapport. Supposons par exemple que vous ayez une campagne qui cible les utilisateurs absents. Dans ce cas, l'ajout d'un événement de conversion secondaire et de l'événement de conversion principal **Starts Session** peut vous permettre de mieux comprendre l'efficacité de votre campagne pour ce qui est de ramener vos utilisateurs dans votre application. 

### Étape 2 : Ajouter les événements de conversion

Tout d'abord, sélectionnez le type général d'événement que vous souhaitez utiliser :

| Type d'événement de conversion         | Description                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lancer la session**      | Un utilisateur est considéré comme converti lorsqu'il ouvre l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail).                                                                                                                                                                                                         |
| **Effectuer un achat**      | Un utilisateur est compté comme ayant été converti lorsqu’il achète le produit que vous avez spécifié (par défaut, n’importe quel produit).                                                                                                                                                                                                                                 |
| **Effectuer un événement personnalisé** | Un utilisateur est compté comme ayant été converti lorsqu’il exécute l’un de vos événements personnalisés existants (aucun par défaut, vous devez spécifier l’événement).                                                                                                                                                                                                        |
| **Mettre à niveau l’application**         | Un utilisateur est considéré comme converti lorsqu'il met à jour la version de l'application dans l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). Braze effectue une comparaison numérique dans les règles de l'art pour déterminer si le changement était une mise à niveau. Les versions non numériques sont comptabilisées comme des conversions si la version change.              |
| **Ouvre l’e-mail**         | Un utilisateur est considéré comme converti lorsqu'il ouvre l'e-mail (uniquement pour les campagnes d'e-mailing).                                                                                                                                                                                                                                                 |
| **Clique sur l’e-mail**        | Un utilisateur est considéré comme converti lorsqu'il clique sur un lien dans l'e-mail (uniquement pour les campagnes d'e-mailing).                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Définissez votre date limite de conversion. Il s’agit du temps maximum qui peut s’écouler pour envisager une conversion. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle la conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

![Le type d’événement de conversion « Effectue un achat » utilisé comme exemple pour enregistrer les conversions des utilisateurs qui effectuent un achat. Le délai de conversion est de 12 heures.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Après avoir sélectionné vos événements de conversion, poursuivez le processus de création de la campagne et commencez à envoyer votre campagne.

### Étape 3 : Consultez vos résultats

Accédez à la page **Détails** pour afficher les détails de chaque événement de conversion associé à la campagne que vous venez de créer. Quels que soient vos événements de conversion sélectionnés, vous pouvez également voir le revenu total qui peut être attribué à cette campagne spécifique, ainsi qu’à ses variantes spécifiques, durant la période de l’événement de conversion principal.

{% alert note %}
Si aucun événement de conversion n'a été sélectionné lors de la création de la campagne, le délai est fixé par défaut à trois jours.
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et le pourcentage de conversion pour votre groupe de contrôle ainsi que chaque variante.

![Quatre événements de conversion qui permettent de suivre les conversions en fonction du moment où un achat a été effectué dans les trois heures, où un achat a été effectué dans les deux heures, où une session a commencé dans les 30 minutes et où une session a commencé dans les 25 minutes.]({% image_buster /assets/img_archive/conversion_event_details.png %})


