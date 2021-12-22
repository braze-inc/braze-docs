---
nav_title: Extensions de segment
article_title: Extensions de segment
page_order: 3.1
page_type: tutoriel
description: "Cet article vous guidera à travers comment utiliser une extension de segment avec les segments de Braze."
tool: Segments
---

# Extensions de segment

> Cet article vous guidera à travers comment utiliser une extension de segment pour améliorer vos capacités de segmentation

Une extension de segment étend nos capacités de segmentation existantes en vous permettant de cibler des listes d'utilisateurs plus précises en fonction de leur événement personnalisé et de leur comportement d'achat au cours des 365 derniers jours. Vous pouvez créer un maximum de 10 extensions de segment par groupe d'applications. Une fois ces listes d'extensions générées, elles peuvent ensuite être incluses ou exclues comme un [filtre][10] dans vos segments. Lors de la création d'une extension de segment, vous pouvez également spécifier que la liste sera régénérée une fois toutes les 24 heures.

## Étape 1 : Accédez aux extensions de segment

À partir du côté gauche du tableau de bord sous Engagement, développez la section Segments, et cliquez sur **Extension de segment**. À partir de la table des extensions de segments, cliquez sur **+ Créer une nouvelle extension**.

## Étape 2 : Nommez votre extension de segment

Nommez votre Extension de Segment en décrivant le type d'utilisateurs pour lequel vous souhaitez filtrer. Cela permettra de s'assurer que cette extension peut être facilement et précisément découverte lors de son application comme filtre dans votre segment.

!\[Nom de l'extension de segment\]\[2\]

## Étape 3 : Choisissez vos critères

Sélectionnez parmi les critères d'achat ou d'événement personnalisé pour le ciblage. Une fois que vous avez sélectionné les critères de type d'événement souhaités, choisissez celui qui a acheté un article ou un événement personnalisé spécifique que vous souhaitez cibler pour votre liste d'utilisateurs. Puis choisissez combien de fois (plus de, moins que, ou égal à) l'utilisateur aurait besoin d'avoir terminé l'événement, et combien de jours pour regarder en arrière, jusqu'à 365 jours.

!\[Critères d'extension du segment\]\[3\]

### Segmentation des propriétés de l'événement

Pour augmenter la précision de ciblage, cochez la case **Ajouter des filtres de propriétés**. Cela vous permettra de percer en fonction des propriétés spécifiques de votre achat ou de votre événement personnalisé. Nous prenons en charge la segmentation des propriétés d'événement basée sur des objets de chaîne, numérique, booléen et horaire. Nous supportons également la segmentation basée sur les propriétés [d'événements imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/nested_object_support/).

!\[Propriété de l'événement\]\[12\]

!\[Arrow\]\[16\]{: style="border:0;"}

!\[Propriété de l'événement\]\[13\]

!\[Propriété de l'événement\]\[14\]

!\[Propriété de l'événement\]\[15\]

Les extensions de segment s'appuient sur le stockage à long terme des propriétés d'événement et ne disposent pas de la limite de stockage personnalisée de 30 jours. Cela signifie que vous pouvez regarder en arrière les propriétés de l'événement suivies au cours de l'année écoulée, et le suivi n'attend pas que l'extension ait été configurée d'abord.

{% alert note %} L'utilisation des propriétés d'événement dans les extensions de segment n'affecte pas l'utilisation du point de données.  {% endalert %}

### Régénération de l'extension

Vous pouvez spécifier si vous voulez que cette extension représente un seul instantané dans le temps, ou si vous voulez que cette extension se régénère quotidiennement. Votre extension commencera toujours le traitement après la sauvegarde initiale. Si vous souhaitez que l'extension soit régénérée quotidiennement, cochez la case **Régénérer l'extension Quotidienne** et la régénération commencera à être traitée vers minuit chaque jour dans le fuseau horaire de votre entreprise.

{% alert important %}
À partir du 1er février 2022, le paramètre de régénération des extensions quotidiennes sera automatiquement désactivé pour les extensions de segment non utilisées. Braze définit les extensions inutilisées comme celles qui répondent aux critères suivants :

- Non utilisé dans aucune campagne active, Canvases ou segments actifs
- Non utilisé dans aucune campagne inactive (brouillon, arrêté, archivé), Canvases ou segments
- N'a pas été modifié depuis plus de 7 jours

Braze informera le contact de la société et le créateur de l'extension lorsque ce paramètre est désactivé. L'option de régénérer les extensions quotidiennement peut être activée à tout moment.
{% endalert %}

## Étape 4 : Enregistrez votre extension de segment

Une fois que vous cliquez sur **Enregistrer**, votre extension commencera à être traitée. La durée de génération de votre extension dépend du nombre d'utilisateurs que vous avez, combien d'événements personnalisés ou d'acheter des événements que vous capturez, et combien de jours vous regardez dans l'histoire.

Pendant le traitement de votre extension, vous verrez une petite animation à côté du nom de l'extension, et le mot "Traitement" dans la colonne **Dernier traité** de la liste des extensions. Notez que vous ne serez pas en mesure de modifier une extension pendant son traitement.

!\[Traitement de l'extension du segment\]\[5\]

## Étape 5 : Utilisez votre extension dans un segment

Une fois que vous avez créé une extension, vous pouvez l'utiliser comme un filtre lors de la création d'un segment ou de la définition d'un public pour une campagne ou Canvas. Commencez par choisir **Braze Segment Extension** dans la liste de filtres sous la section **Attributs Utilisateurs**.

!\[Extension de segment comme filtre de segment\]\[6\]

Dans la liste des filtres d'extension de segment de Braze, choisissez l'extension que vous souhaitez inclure ou exclure dans ce segment.

!\[Extension de segment comme filtre de segment\]\[7\]

Pour afficher les critères d'extension, cliquez sur **Voir les détails de l'extension** pour afficher les détails dans une fenêtre contextuelle.

!\[Module de détails d'extension de Segment \]\[8\]{: style="max-width:70%;"}

Maintenant, vous pouvez continuer comme d'habitude avec [la création de votre segment][11].
[2]: {% image_buster /assets/img/segment/segment_extension2.png %} [3]: {% image_buster /assets/img/segment/segment_extension3.png %} [5]: {% image_buster /assets/img/segment/segment_extension5. ng %} [6]: {% image_buster /assets/img/segment/segment_extension7.png %} [7]: {% image_buster /assets/img/segment/segment_extension6. ng %} [8]: {% image_buster /assets/img/segment/segment_extension8.png %} [12]: {% image_buster /assets/img/segment/property1.png %} [13]: {% image_buster /assets/img/segment/property2. ng %} [14]: {% image_buster /assets/img/segment/property3.png %} [15]: {% image_buster /assets/img/segment/property4. ng %} [16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}

[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
