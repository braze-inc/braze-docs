---
nav_title: Segment Extensions
article_title: Segment Extensions
page_order: 3.1

page_type: tutorial
description: "Cet article pratique vous explique comment utiliser une Segment Extension avec des segments Braze."
tool: Segments
---

# Segment Extensions

> Cet article vous explique comment utiliser une Segment Extension pour améliorer vos capacités de segmentation.

Les Segment Extensions élargissent nos capacités de segmentation en vous permettant de cibler des listes plus précises d’utilisateurs en fonction de leur événement personnalisé et de leur comportement d’achat au cours des 365 derniers jours. Vous pouvez créer un maximum de 10 Segment Extensions par groupe d’apps. Une fois ces listes d’extension générées, elles peuvent être incluses ou exclues de vos segments sous forme de [filtres][10]. Lorsque vous créez une Segment Extension, vous pouvez également choisir que la liste soit renouvelée une fois toutes les 24 heures.

## Étape 1 : Accéder aux Segment Extensions

Dans **Engagements**, développez la liste **Segments** et cliquez sur **Segment Extension**. Dans le tableau Segment Extension, cliquez sur <i class="fas fa-plus"></i> **Create New Extension (Créer une nouvelle extension)**.

## Étape 2 : Nommer votre Segment Extension

Nommez votre Segment Extension en décrivant le type d’utilisateur que vous souhaitez cibler. Cela vous permettra de retrouver facilement cette extension lorsque vous souhaiterez l’utiliser en tant que filtre dans votre segment.

![Segment Extension nommée « Online Shoppers Extenion - 90 Days (Extension pour acheteurs en ligne : 90 jours) » avec la case « Regenerate Extension Daily (Renouveler quotidiennement l’extension) » cochée.][2]

## Étape 3 : Choisir vos critères

Sélectionnez un critère d’achat ou d’événement personnalisé pour le ciblage. Après avoir sélectionné vos critères de type d’événement, choisissez l’article acheté ou l’événement personnalisé que vous souhaitez cibler pour votre liste d’utilisateurs. Choisissez ensuite le nombre de fois (supérieur à, inférieur à ou égal à) que l’utilisateur devra avoir effectué l’événement, et le nombre de jours que vous souhaitez analyser (365 jours maximum).

![Segment ][3]

### Segmentation des propriétés d’événement

Pour augmenter la précision du ciblage, cochez la case **Add Property Filters (Ajouter des filtres de propriété)**. Cela vous permettra d’analyser les résultats en fonction des propriétés spécifiques de votre achat ou événement personnalisé. Nous prenons en charge la segmentation des propriétés d’événement en fonction des objets de chaîne de caractères, numériques, booléens et temporels. 

![Segmentation basée sur les propriétés numériques.][13]

![Segmentation basée sur les propriétés booléennes.][14]

![Segmentation basée sur les objets temporels.][15]

Nous prenons également en charge la segmentation basée sur les [Propriétés d’événement imbriqué]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#nested-objects).

Les Segment Extensions s’appuient sur le stockage à long terme des propriétés d’événement et ne sont pas soumises à la limite de stockage des propriétés d’événement personnalisé de 30 jours. Cela signifie que vous pouvez analyser les propriétés d’événement suivies au cours de l’année, et que le suivi ne doit pas attendre que l’extension ait été configurée en premier.

{% alert note %} 
L’utilisation de propriétés d’événement dans des Segment Extensions n’affecte pas l’utilisation de vos points de données.
{% endalert %}

### Régénération de l’extension

Vous pouvez indiquer si vous souhaitez que cette extension représente une instantanée à un moment T, ou si vous souhaitez que cette extension soit renouvelée quotidiennement. Votre extension sera toujours traitée après la sauvegarde initiale. Si vous souhaitez que l’extension soit renouvelée quotidiennement, cochez la case **Regenerate Extension Daily (Renouveler quotidiennement l’extension)** et l’extension sera régénérée chaque jour à partir de minuit selon le fuseau horaire de votre entreprise.

{% alert important %}
À compter du 1er février 2022, le paramètre permettant de renouveler les extensions quotidiennement sera automatiquement désactivé pour les Segment Extensions non utilisées. Braze définit les extensions non utilisées comme celles qui répondent aux critères suivants :

- Utilisée dans aucune campagne, ni aucun Canvas ou segment actif
- Utilisée dans aucune campagne, ni aucun Canvas ou segment actif (qu’il soit une ébauche, abandonné ou archivé)
- N’a pas été modifiée depuis plus de 7 jours

Braze informera la personne de contact de la société et le créateur de l’extension lorsque ce paramètre est désactivé. L’option permettant de renouveler les extensions quotidiennement peut être réactivée à tout moment.
{% endalert %}

## Étape 4 : Enregistrer votre Segment Extension

Le traitement de votre extension commencera une fois que vous aurez cliqué sur **Save (Enregistrer)**. La durée nécessaire pour générer votre extension dépend du nombre d’utilisateurs que vous avez, du nombre d’événements personnalisés ou d’événements d’achat que vous collectez, et du nombre de jours que vous analysez dans l’historique.

Pendant le traitement de votre extension, vous verrez une petite animation à côté du nom de l’extension et le mot « Processing (Traitement) » s’afficher dans la colonne **Last Processed (Dernier traitement)** de la liste des extensions. Notez que vous ne pourrez pas modifier une extension lorsqu’elle est en cours de traitement.

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
