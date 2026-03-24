---
nav_title: Événements de conversion
article_title: Événements de conversion
page_order: 3
page_type: reference
description: "Cet article de référence définit les événements de conversion, comment les utiliser pour définir vos indicateurs de réussite dans Braze, et comment utiliser ces événements pour connaître l'engagement de vos utilisateurs."
tool:
    - Campaigns
    - Canvas
---

# Événements de conversion

> Un événement de conversion est un type d'indicateur de réussite qui permet de savoir si un destinataire de votre message effectue une action à forte valeur ajoutée dans un laps de temps déterminé après avoir reçu votre envoi. Utilisez ces événements pour vous assurer que vous recueillez des informations pertinentes et utiles que vous pourrez ensuite utiliser pour obtenir des informations pour votre campagne ou votre Canvas.

## Fonctionnement

Pour une campagne personnalisée ayant un ciblage sur les utilisateurs actifs pendant les fêtes, un événement de conversion consistant à **démarrer une session** dans les deux ou trois jours peut être approprié, car il vous permet d'évaluer l'engagement des utilisateurs après la réception de votre message. Vous pouvez également sélectionner des événements supplémentaires tels que **« Passer une commande** », « **Mettre à niveau l'application** » ou tout autre événement personnalisé comme événements de conversion.

{% alert tip %}
Pour en savoir plus sur les conversions, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes.
{% endalert %}

### Règles de suivi de conversion

Les événements de conversion attribuent les actions des utilisateurs à un point d'engagement. Veuillez noter les points suivants concernant la manière dont Braze gère les conversions multiples :

- **Campagnes à canal unique** : Les conversions se font par utilisateur et non par appareil. Au sein d'un même canal, un utilisateur ne convertit qu'une seule fois par événement de conversion, même si un message est envoyé à plusieurs appareils. Par exemple, si une campagne ne comporte qu'un seul événement de conversion défini sur « Effectuer un achat » et qu'un utilisateur effectue deux achats distincts avant la date limite de conversion, Braze ne comptabilise qu'une seule conversion.
- **Campagnes multicanales** : Dans le cadre des campagnes multicanales, chaque canal dispose de ses propres opportunités de conversion. Un utilisateur peut effectuer une conversion par canal après avoir reçu un message sur ce canal. Cela signifie que si un utilisateur reçoit des messages sur plusieurs canaux (par exemple, à la fois par e-mail et par notification push) et effectue l'action de conversion, Braze comptabilise une conversion pour chaque canal, ce qui peut entraîner des taux de conversion supérieurs à 100 %.
- Si un utilisateur effectue un événement de conversion dans les délais de conversion de deux campagnes ou canevas distincts qu'il a reçus, la conversion est enregistrée dans les deux.
- Un utilisateur est considéré comme converti s'il a effectué l'événement de conversion spécifique dans la fenêtre, même s'il n'a pas ouvert ou cliqué sur le message.
- Pour les canevas, le suivi des conversions fonctionne en fonction de la date limite de conversion finale qui commence lorsque l'utilisateur accède au canevas, et non en fonction du moment où chaque message est envoyé. Braze comptabilise les conversions même pendant les périodes de retard entre les messages dans Canvas.

### Événement de conversion primaire

L'événement de conversion principal est le premier événement que vous ajoutez lors de la création d'une campagne ou d'un canvas. Cet événement est le plus important concernant votre engagement et votre signalement. Braze utilise votre événement de conversion principal pour :

- Calculez la variation du message gagnant dans les campagnes [multivariées]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) ou les canevas.
- Déterminez la fenêtre pour laquelle le revenu est calculé pour la campagne ou le canvas.
- Ajustez la distribution des messages pour les campagnes et les toiles à l'aide de la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

Le nombre d'événements de conversion principaux correspond au nombre d'événements de conversion qui se sont produits. Pour les campagnes multicanales, Braze comptabilise les conversions par canal (comme décrit dans [les règles de suivi des conversions](#conversion-tracking-rules)), ce qui signifie que le nombre de conversions peut dépasser le nombre d'utilisateurs uniques et entraîner des taux de conversion supérieurs à 100 %. Braze calcule le taux d'événement de conversion principal en divisant ce nombre par le nombre de destinataires uniques. Braze considère qu'un utilisateur est un destinataire lorsque le message est envoyé ou affiché, selon le canal utilisé. Par exemple, dans le cas d'une notification push ou d'un e-mail, un utilisateur devient destinataire une fois que Braze a envoyé le message. Pour les messages in-app ou les cartes de contenu, l'utilisateur doit consulter le message pour être considéré comme destinataire.

{% alert note %}
Si vous interrompez l'envoi de messages à l'aide de l'étiquette`abort` Liquid, Braze interrompt l'envoi de messages uniquement pour les utilisateurs qui passent par des variantes. Les messages destinés aux utilisateurs du groupe de contrôle ne sont pas interrompus, ce qui peut entraîner des pourcentages de conversion biaisés entre les variantes et les groupes de contrôle. En guise de solution de contournement, utilisez la [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) pour cibler vos utilisateurs à l'entrée de la campagne et du canvas.
{% endalert %}

## Création d'une campagne avec suivi des conversions

### Étape 1 : Implémentez votre campagne

[Créez une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) pour le canal de messages que vous souhaitez. Après avoir configuré les messages et la planification de votre campagne, vous pouvez ajouter jusqu'à quatre événements de conversion à suivre.

Veuillez utiliser autant d'événements de conversion que nécessaire. L'ajout d'un deuxième ou d'un troisième événement de conversion enrichit considérablement vos rapports. Par exemple, pour une campagne de ciblage des utilisateurs inactifs, l'ajout d'un événement de conversion secondaire en plus de l'événement de conversion principal **« Démarrage de session** » vous aide à évaluer l'efficacité de votre campagne pour ramener les utilisateurs vers votre application. 

### Étape 2 : Ajouter les événements de conversion

Tout d'abord, sélectionnez le type général d'événement que vous souhaitez utiliser :

| Type d'événement de conversion   | Description                |
|-------------------------|----------------------------|
| **Lancer la session**      | Un utilisateur est considéré comme converti lorsqu'il ouvre l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail).|
| **Effectuer un achat**      | Un utilisateur est considéré comme converti lorsqu'il enregistre un [événement d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/). Ceci permet de suivre tout achat par défaut, ou vous pouvez spécifier un produit particulier.|
| **Commandes passées**        | Un utilisateur est considéré comme converti lorsqu'il déclenche l'[événement recommandé « Commande passée » dans le domaine du commerce électronique]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events?tab=ecommerce.order_placed#ecommerce-recommended-events). Ceci permet de suivre toute commande par défaut, ou vous pouvez filtrer par produit spécifique.<br><br>L'événement « Commander des lieux » est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé. |
| **Effectuer un événement personnalisé**| Un utilisateur est compté comme ayant été converti lorsqu’il exécute l’un de vos événements personnalisés existants (aucun par défaut, vous devez spécifier l’événement).|
| **Mettre à niveau l’application**         | Un utilisateur est considéré comme converti lorsqu'il met à jour la version de l'application dans l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). Braze effectue une comparaison numérique dans les règles de l'art pour déterminer si le changement était une mise à niveau. Les versions non numériques sont comptabilisées comme des conversions si la version change.|
| **Ouvre l’e-mail**         | Un utilisateur est considéré comme converti lorsqu'il ouvre l'e-mail (uniquement pour les campagnes d'e-mailing).|
| **Clique sur l’e-mail**        | Un utilisateur est considéré comme converti lorsqu'il clique sur un lien dans l'e-mail (uniquement pour les campagnes d'e-mailing).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
**Les propriétés imbriquées ne sont pas prises en charge dans les événements de conversion**. Il n'est pas possible d'utiliser des propriétés imbriquées dans les événements de conversion. Par exemple, si`product_code`  ou`product_name`  sont des propriétés imbriquées dans un`products`tableau  (tel que `products[].product_code`), il n'est pas possible de les utiliser pour vérifier si un achat de produit spécifique a été effectué lors d'un événement de conversion.
{% endalert %}

Définissez votre date limite de conversion. Il s'agit du délai maximal pouvant s'écouler avant que Braze ne considère une conversion. Vous pouvez définir une période maximale de 30 jours pendant laquelle Braze comptabilise la conversion si l'utilisateur effectue l'action spécifiée.

![Le type d’événement de conversion « Effectue un achat » utilisé comme exemple pour enregistrer les conversions des utilisateurs qui effectuent un achat. Il a une date limite de conversion de 12 heures.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Après avoir sélectionné vos événements de conversion, poursuivez le processus de création de la campagne et commencez à envoyer votre campagne.

### Étape 3 : Consultez vos résultats

Veuillez vous rendre sur la page **Détails** pour consulter les informations relatives à chaque événement de conversion associé à la campagne que vous avez créée. Quels que soient les événements de conversion que vous avez sélectionnés, vous pouvez également consulter le chiffre d'affaires total attribué à cette campagne spécifique, ainsi qu'à des variantes spécifiques, pendant la période de l'événement de conversion principal.

{% alert note %}
Si vous ne sélectionnez aucun événement de conversion lors de la création de la campagne, la durée par défaut est de trois jours.
{% endalert %}

De plus, pour les messages multivariés, vous pouvez voir le nombre de conversions et le pourcentage de conversion pour votre groupe de contrôle ainsi que chaque variante.

![Quatre événements de conversion qui suivent les conversions en fonction du moment où un achat a été effectué dans les trois heures, d'un achat effectué dans les deux heures, d'une session commencée dans les 30 minutes et d'une session commencée dans les 25 minutes.]({% image_buster /assets/img_archive/conversion_event_details.png %})