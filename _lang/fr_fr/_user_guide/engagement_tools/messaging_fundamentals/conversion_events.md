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

> Un événement de conversion est un type d'indicateur de réussite qui permet de savoir si un destinataire de votre message effectue une action à forte valeur ajoutée dans un laps de temps défini après avoir reçu votre envoi. Utilisez ces événements pour vous assurer que vous recueillez des informations pertinentes et utiles que vous pourrez utiliser ultérieurement pour obtenir des informations pour votre campagne ou votre Canvas.

## Comment cela fonctionne-t-il ?

Disons que vous créez une campagne de vacances personnalisée pour les utilisateurs actifs, un événement de conversion de **Démarrer une session** dans les deux ou trois jours peut être approprié car il vous permettra de recueillir un sentiment d'engagement de l'utilisateur à partir de la réception de votre message. Des événements supplémentaires tels que l'**achat**, la **mise à niveau de l'application** ou tout autre événement personnalisé peuvent être sélectionnés en tant qu'événements de conversion.

{% alert tip %}
Pour en savoir plus sur les conversions, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes.
{% endalert %}

### Règles de suivi des conversions

Les événements de conversion vous permettent d'attribuer l'action de l'utilisateur à un point d'engagement. Cela dit, il y a quelques points à noter concernant la façon dont Braze gère les conversions multiples. Consultez les scénarios suivants pour comprendre comment Braze suit ces conversions :

- Les conversions se font par utilisateur et non par appareil. Cela signifie qu'un utilisateur ne peut se convertir qu'une seule fois, même si un message est envoyé à plusieurs appareils. Autre exemple, supposons qu'une campagne ne comporte qu'un seul événement de conversion, à savoir "Effectue un achat". Si un utilisateur qui reçoit cette campagne effectue deux achats distincts dans le délai de conversion, une seule conversion sera comptabilisée.
- Si un utilisateur effectue un événement de conversion dans les délais de conversion de deux campagnes ou Canvas distinctes qu'il a reçues, alors la conversion s'enregistrera sur les deux.
- Un utilisateur sera considéré comme converti s'il a effectué l'événement de conversion spécifique dans la fenêtre, même s'il n'a pas ouvert ou cliqué sur le message.
- Pour les Canvas, le suivi des conversions fonctionne sur la base du délai de conversion final qui commence lorsqu'un utilisateur entre dans le Canvas, et non sur la base de l'heure de diffusion des messages individuels. Cela signifie que les conversions peuvent être comptabilisées même pendant les périodes de retard entre les messages dans Canvas.

### Événement de conversion principal

L'événement de conversion principal est le premier événement ajouté lors de la création de la campagne ou du Canvas. C'est l'événement qui a le plus d'incidence sur votre engagement et vos rapports d'engagement. Votre événement de conversion principal sert à :

- Calculez la variation du message gagnant dans les campagnes [multivariées]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) ou les canevas.
- Déterminez la fenêtre dans laquelle le chiffre d'affaires est calculé pour la campagne ou le Canvas.
- Ajustez la distribution des messages pour les campagnes et les toiles à l'aide de la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% alert note %}
Si les messages sont interrompus à l'aide de l'étiquette Liquid `abort`, seuls les utilisateurs qui passent par les variantes sont potentiellement interrompus. Cela signifie que les messages adressés aux utilisateurs qui passent par le groupe de contrôle ne seront pas interrompus, ce qui peut conduire à des pourcentages de conversion faussés entre les variantes et les groupes de contrôle. En guise de solution de contournement, utilisez la [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) pour cibler vos utilisateurs à l'entrée de la campagne et du canvas.
{% endalert %}

## Création d'une campagne avec suivi des conversions

### Étape 1 : Implémentez votre campagne

[Créez une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) pour le canal de messages que vous souhaitez. Après avoir configuré les messages et la planification de votre campagne, vous aurez la possibilité d'ajouter jusqu'à quatre événements de conversion pour le suivi.

Nous vous recommandons d'utiliser autant d'événements de conversion que vous le jugez nécessaire, car l'ajout d'un deuxième (ou d'un troisième) événement de conversion peut considérablement enrichir votre rapport. Par exemple, supposons que vous ayez une campagne qui cible les utilisateurs en déperdition. Dans ce cas, l'ajout d'un événement de conversion secondaire et de l'événement de conversion principal **Starts Session** peut vous permettre de mieux comprendre l'efficacité de votre campagne pour ce qui est de ramener vos utilisateurs dans votre application. 

### Étape 2 : Ajouter les événements de conversion

Tout d'abord, sélectionnez le type général d'événement que vous souhaitez utiliser :

| Type d'événement de conversion         | Description                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Début de la session**      | Un utilisateur est considéré comme converti lorsqu'il ouvre l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail).                                                                                                                                                                                                         |
| **Effectue un achat**      | Un utilisateur est considéré comme converti lorsqu'il achète le produit que vous indiquez (par défaut, n'importe quel produit).                                                                                                                                                                                                                                 |
| **Exécution d'un événement personnalisé** | Un utilisateur est considéré comme converti lorsqu'il effectue l'un de vos événements personnalisés existants (pas de valeur par défaut, vous devez spécifier l'événement).                                                                                                                                                                                                        |
| **Mise à jour de l'application**         | Un utilisateur est considéré comme converti lorsqu'il met à jour la version de l'application dans l'une des applications que vous spécifiez (par défaut, toutes les applications de l'espace de travail). Braze effectue une comparaison numérique dans les règles de l'art pour déterminer si le changement était une mise à niveau. Les versions non numériques sont comptabilisées comme des conversions si la version change.              |
| **Ouvre l'e-mail**         | Un utilisateur est considéré comme converti lorsqu'il ouvre l'e-mail (uniquement pour les campagnes d'e-mailing).                                                                                                                                                                                                                                                 |
| **Clics e-mail**        | Un utilisateur est considéré comme converti lorsqu'il clique sur un lien dans l'e-mail (uniquement pour les campagnes d'e-mailing).                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Fixez votre délai de conversion. Il s'agit du délai maximum qui peut s'écouler pour envisager une conversion. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle la conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Le type d'événement de conversion "Effectue un achat" sert d'exemple pour enregistrer les conversions des utilisateurs qui effectuent un achat, quel qu'il soit. Le délai de conversion est de 12 heures.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Après avoir sélectionné vos événements de conversion, poursuivez le processus de création de la campagne et commencez à envoyer votre campagne.

### Étape 3 : Consultez vos résultats

Accédez à la page **Détails** pour afficher les détails de chaque événement de conversion associé à la campagne que vous venez de créer. Quels que soient les événements de conversion sélectionnés, vous pouvez également voir le chiffre d'affaires total qui peut être attribué à cette campagne spécifique, ainsi qu'à des variantes spécifiques, pendant la fenêtre de l'événement de conversion principal.

{% alert note %}
Si aucun événement de conversion n'a été sélectionné lors de la création de la campagne, le délai est fixé par défaut à trois jours.
{% endalert %}

En outre, pour les messages multivariés, vous pouvez voir le nombre de conversions et les pourcentages de conversion pour votre groupe de contrôle et chaque variante.

Quatre événements de conversion qui suivent les conversions en fonction du moment où un achat a été effectué dans les trois heures, où un achat a été effectué dans les deux heures, où une session a été lancée dans les 30 minutes et où une session a été lancée dans les 25 minutes.]({% image_buster /assets/img_archive/conversion_event_details.png %})


