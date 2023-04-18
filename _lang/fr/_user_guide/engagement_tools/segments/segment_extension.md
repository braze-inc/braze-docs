---
nav_title: Segment Extensions
article_title: Segment Extensions
page_order: 3.1

page_type: tutorial
description: "Cet article de mode d'emploi vous explique comment configurer et utiliser un Segment Extension pour améliorer vos capacités de segmentation."
tool: Segments
---

# Segment Extensions

> La segmentation Braze vous permet de cibler des utilisateurs selon les événements personnalisés ou le comportement d’achat enregistré pour la durée de vie de ce profil utilisateur. Les exemples comprennent le fait de trouver des utilisateurs qui ont ou n’ont pas effectué un événement personnalisé donné depuis un moment spécifique, ou bien de segmenter les utilisateurs sur la base des produits qu’ils ont déjà achetés ou combien d’argent ils ont dépensé pour votre service.

Les Segment Extensions sont des définitions d’audience vous permettant d’utiliser des propriétés de l’événement imbriqué ou créer des ensembles fenêtrés d’un événement personnalisé et des propriétés de l’événement d’achat au cours des deux dernières années (730 jours). À titre d’exemple, la segmentation de Braze vous permet de trouver des utilisateurs qui ont acheté un produit au cours de leur durée de vie. Avec Segment Extensions, vous pouvez affiner cette audience pour des utilisateurs qui ont acheté une couleur donnée d’un produit donné au moins deux fois au cours des 2 dernières années. Lorsque vous créez une extension de segment, vous pouvez également spécifier si l’audience est statique ou régénérée toutes les 24 heures.

L’utilisation des propriétés de l’événement imbriqué pour la [Livraison par événement][19] n’a pas besoin de Segment Extensions, car le traitement des événements se fait en temps réel. De même, les Attributs personnalisés imbriqués n’ont pas besoin d’utiliser les Segment Extensions.

{% alert important %}
Par défaut, 25 Segment Extensions actifs sont alloués par groupe d’apps à un moment donné. Si vous avez besoin d’augmenter cette limite, contactez votre gestionnaire du succès des clients Braze pour discuter de votre cas d’utilisation.
{% endalert %}

## Étape 1 : Accéder aux Segment Extensions

Dans **Engagements**, développez la liste **Segments** et cliquez sur **Segment Extension**. Dans le tableau Segment Extension, cliquez sur <i class="fas fa-plus"></i> **Create New Extension (Créer une nouvelle extension)**.

## Étape 2 : Nommer votre Segment Extension

Nommez votre Segment Extension en décrivant le type d’utilisateur que vous souhaitez cibler. Cela vous permettra de retrouver facilement cette extension lorsque vous souhaiterez l’utiliser en tant que filtre dans votre segment.

![Segment Extension nommée « Online Shoppers Extenion - 90 Days (Extension pour acheteurs en ligne : 90 jours) » avec la case « Regenerate Extension Daily (Renouveler l’extension quotidiennement) » cochée.][2]

## Étape 3 : Choisir vos critères

Sélectionnez un critère d’achat, de message, d’engagement ou d’événement personnalisé pour le ciblage. Après avoir sélectionné vos critères de type d’événement, choisissez l’article acheté, l’interaction avec un message ou l’événement personnalisé que vous souhaitez cibler pour votre liste d’utilisateurs. Choisissez ensuite le nombre de fois (supérieur à, inférieur à ou égal à) que l’utilisateur devra avoir effectué l’événement, et le nombre de jours que vous souhaitez analyser (730 jours / 2 ans maximum). La segmentation basée sur les données des événements antérieurs à 730 jours peut se faire en utilisant d’autres filtres présents dans **Segments**.

![][3]

### Segmentation des propriétés de l’événement

Pour augmenter la précision du ciblage, cochez la case **Add Property Filters (Ajouter des filtres de propriété)**. Cela vous permettra d’analyser les résultats en fonction des propriétés spécifiques de votre achat ou événement personnalisé. Nous prenons en charge la segmentation des propriétés de l’événement en fonction des objets de chaîne de caractères, numériques, booléens et temporels.

![Segmentation basée sur les propriétés numériques.][13]

![Segmentation basée sur les propriétés booléennes.][14]

![Segmentation basée sur les objets temporels.][15]

Nous prenons également en charge la segmentation basée sur les [Propriétés de l’événement imbriqué]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#nested-objects).

![Segmenter en fonction de propriétés de l’événement imbriqué.][18]

Les Segment Extensions s’appuient sur le stockage à long terme des propriétés de l’événement et n’ont pas de limite de stockage de propriété horodatée. Vous pouvez regarder les propriétés de l’événement suivies sur les deux dernières années.

{% alert note %}
L’utilisation de propriétés de l’événement dans des Segment Extensions n’affecte pas l’utilisation de vos points de données.
{% endalert %}

### Régénération de l’extension

Vous pouvez indiquer si vous souhaitez que cette extension représente un instantané à un moment T, ou si vous souhaitez que cette extension soit renouvelée quotidiennement. Votre extension sera toujours traitée après la sauvegarde initiale. Si vous souhaitez que l’extension soit renouvelée quotidiennement, cochez la case **Regenerate Extension Daily (Renouveler quotidiennement l’extension)** et l’extension sera régénérée chaque jour à partir de minuit selon le fuseau horaire de votre entreprise.

{% alert important %}
Le paramètre permettant de renouveler les extensions quotidiennement est automatiquement désactivé pour les Segment Extensions non utilisées. Braze définit les extensions non utilisées comme celles qui répondent aux critères suivants :

- Utilisée dans aucune campagne, ni aucun Canvas ou segment actif
- Utilisée dans aucune campagne, ni aucun Canvas ou segment actif (qu’il soit une ébauche, abandonné ou archivé)
- N’a pas été modifiée depuis plus de 7 jours

Braze informera la personne de contact de la société et le créateur de l’extension lorsque ce paramètre est désactivé. L’option permettant de renouveler les extensions quotidiennement peut être réactivée à tout moment.
{% endalert %}

## Étape 4 : Enregistrer votre Segment Extension

Le traitement de votre extension commencera une fois que vous aurez cliqué sur **Save (Enregistrer)**. La durée nécessaire pour générer votre extension dépend du nombre d’utilisateurs que vous avez, du nombre d’événements personnalisés ou d’événements d’achat que vous collectez, et du nombre de jours que vous analysez dans l’historique.

Pendant le traitement de votre extension, vous verrez une petite animation à côté du nom de l’extension et le mot « Processing (Traitement) » s’afficher dans la colonne **Dernier traitement** de la liste des extensions. Notez que vous ne pourrez pas modifier une extension lorsqu’elle est en cours de traitement.

![][5]

## Étape 5 : Utiliser votre extension dans un segment

Après avoir créé une extension, vous pouvez l’utiliser comme filtre lorsque vous créez un segment ou définissez une audience pour une campagne ou un Canvas. Commencez par choisir **Braze Segment Extension** dans la liste des filtres dans la section **User Attributes (Attributs utilisateur)**.

![][6]

Dans la liste des filtres Braze Segment Extension, choisissez l’extension que vous souhaitez inclure ou exclure de ce segment.

![][7]

Pour afficher les critères d’extension, cliquez sur **View Extension Details (Afficher les détails de l’extension)** pour consulter ces informations dans une fenêtre modale.

![][8]{: style="max-width:70%;"}

Vous pouvez maintenant [créer votre segment][11] comme vous le faites habituellement.

[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension3.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
