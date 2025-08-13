---
nav_title: Extensions de segments
article_title: Extensions de segments
page_order: 6
page_type: reference
description: "Cet article pratique vous explique comment configurer et utiliser une extension de segments pour améliorer vos capacités de segmentation."
tool: Segments
---

# Extensions de segments

> Les extensions de segments vous permettent de créer des segments très précis sur une longue période de l'historique d'un utilisateur. Par exemple, grâce aux extensions de segments, vous pouvez cibler les utilisateurs qui ont acheté un produit particulier au cours des seize derniers mois ou qui ont dépensé une certaine somme d'argent avec votre service. Affinez cette audience en utilisant les propriétés d'événement pour rendre le ciblage encore plus granulaire.

La segmentation de Braze vous permet de cibler les utilisateurs en fonction d'un événement personnalisé ou d'un comportement d'achat. Les extensions de segments renforcent cette capacité en vous permettant d'exploiter les données historiques enregistrées dans le profil utilisateur. Grâce aux extensions de segments, vous pouvez identifier et atteindre les utilisateurs qui ont réalisé un événement personnalisé ou un événement d'achat, quel que soit le nombre de fois au cours des deux dernières années (730 jours). 

## Pourquoi utiliser les extensions de segments ?

Les segments de Braze vous offrent de puissants outils de ciblage pour créer des groupes dynamiques d'utilisateurs. Pour la plupart des cas d'utilisation, cela suffit pour atteindre votre audience de manière efficace. Les extensions de segments sont conçues pour les cas d'utilisation avancés dans lesquels vous devez analyser des comportements remontant jusqu'à deux ans ou appliquer une logique complexe, sans compromettre la conservation des données ou les performances du système. Vous pouvez utiliser des requêtes [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) ou des données provenant de votre propre [entrepôt de données]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) pour affiner davantage votre audience.

Par exemple, la segmentation par défaut de Braze trouvera les utilisateurs qui correspondent à des critères spécifiques que vous définissez, comme l'identification d'un utilisateur qui a récemment acheté l'un de vos produits. Les extensions de segments vous permettent d'aller plus loin, par exemple en identifiant les utilisateurs qui ont acheté une couleur particulière d'un produit spécifique au moins deux fois il y a 18 à 24 mois. Les extensions de segments constituent une amélioration et non une exigence. Si vous avez besoin de filtres plus avancés ou d'une fenêtre d'observation plus longue, ils constituent un excellent outil pour vous aider tout en optimisant l'utilisation de vos données.

{% alert note %}
Par défaut, 25 extensions de segments actives sont allouées par espace de travail à un moment donné. Si vous avez besoin d’augmenter cette limite, contactez votre gestionnaire du succès des clients Braze pour discuter de votre cas d’utilisation.
{% endalert %}

## Création d'une extension de segmentation

Pour créer une extension de segment, vous allez créer un filtre pour affiner un segment de vos utilisateurs sur la base de propriétés d'événement personnalisées. Lors de la création d'une extension de segments, vous choisirez si le segment sera statique ou s'il sera actualisé dynamiquement à un intervalle donné.

### Étape 1 : Accéder aux Segment Extensions

Sélectionnez **Audience** > **Extensions de segments**.

Dans le tableau Extensions de segments, sélectionnez **Créer une nouvelle extension**, puis sélectionnez votre expérience de création d'extensions de segments :

- **Extension simple :** Créez une extension de segment axée sur un seul événement en utilisant un formulaire guidé.
Il s’agit de la meilleure option si vous ne souhaitez pas utiliser de code SQL.
- **Commencez par un modèle :** Créez un segment SQL avec un modèle personnalisable en utilisant des données Snowflake.
- **Actualisation progressive :** Écrivez un segment SQL Snowflake qui actualise automatiquement les deux derniers jours de données ou les actualise manuellement selon les besoins. Il s’agit du meilleur compromis précision/coût.
- **Actualisation complète :** Écrivez un segment SQL Snowflake qui recalcule l’intégralité de l’audience lors d’une actualisation manuelle. Il s’agit de la meilleure option lorsque vous avez besoin d’une vision complète et actualisée de votre audience.

![Tableau proposant différentes expériences de création d'extensions de segments.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Si vous sélectionnez une expérience qui utilise SQL, reportez-vous à la section [Extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) pour plus d'informations.

Si vous sélectionnez l'**extension simple**, passez aux étapes suivantes.

### Étape 2 : Nommer votre Segment Extension

Nommez votre Segment Extension en décrivant le type d’utilisateur que vous souhaitez cibler. Cela vous permettra de retrouver facilement cette extension lorsque vous souhaiterez l’utiliser en tant que filtre dans votre segment.

![Extension de segments nommée "Online Shoppers Extension - 90 Days".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Étape 3 : Choisir vos critères

Sélectionnez un critère d’achat, de message, d’engagement ou d’événement personnalisé pour le ciblage. Après avoir sélectionné les critères du type d'événement souhaité, choisissez l'article acheté, l'interaction du message ou l'événement personnalisé spécifique que vous souhaitez cibler pour votre liste d'utilisateurs. Choisissez ensuite le nombre de fois (supérieur, inférieur ou égal) que l'utilisateur doit avoir effectué l'événement, ainsi que la période de temps - pour les extensions de segments en particulier, vous pouvez remonter jusqu'aux 730 derniers jours (2 ans).

La segmentation basée sur les données d'événements de plus de 730 jours peut être effectuée à l'aide d'autres filtres disponibles dans **Segments**. Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relatives pour sélectionner les X derniers jours, une date de début, une date de fin ou une plage de dates exactes (de la date A à la date B).

![Critères de segmentation pour les utilisateurs qui ont effectué un événement personnalisé plus de 2 fois entre le 1er mars 2025 et le 31 mars 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Segmentation des propriétés de l’événement

Pour accroître la précision du ciblage, cochez la case **Ajouter des filtres de propriété**. Cela vous permettra d’analyser les résultats en fonction des propriétés spécifiques de votre achat ou événement personnalisé. Nous prenons en charge la segmentation des propriétés de l’événement en fonction des objets de chaîne de caractères, numériques, booléens et temporels.

Pour les propriétés des chaînes de caractères, vous pouvez saisir plusieurs valeurs à la fois. Dans l'exemple ci-dessous, ce filtre recherche les utilisateurs dont le statut est égal à l'une des valeurs suivantes : or, argent ou bronze.

![Segmentation basée sur les propriétés des chaînes de caractères.]({% image_buster /assets/img/segment/property5.png %})

![Segmentation basée sur des propriétés numériques.]({% image_buster /assets/img/segment/property2.png %})

![Segmentation basée sur des propriétés booléennes.]({% image_buster /assets/img/segment/property3.png %})

![Segmentation basée sur des objets temporels.]({% image_buster /assets/img/segment/property4.png %})

Nous prenons également en charge la segmentation basée sur les [propriétés d'événements imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmentation basée sur les propriétés d'événements imbriqués.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Les Segment Extensions s’appuient sur le stockage à long terme des propriétés de l’événement et n’ont pas de limite de stockage de propriété horodatée. Vous pouvez regarder les propriétés de l’événement suivies sur les deux dernières années. L’utilisation de propriétés de l’événement dans des Segment Extensions n’affecte pas l’utilisation de vos points de données.

{% alert note %}
Vous n'avez pas besoin des extensions de segment pour utiliser les propriétés d'événement ou les attributs personnalisés imbriqués dans votre segment. Les extensions de segments ne font que prolonger la fenêtre historique utilisée pour créer un segment. Vous pouvez créer un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) en temps réel qui utilise les propriétés d'événements des 30 derniers jours ou des attributs personnalisés imbriqués. De même, vous pouvez [planifier le déclenchement de votre message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) en temps réel sur la base d'une propriété d'événement - aucune extension de segment n'est nécessaire.
{% endalert %}

### Étape 4 : Désigner des paramètres d'actualisation (facultatif)

{% multi_lang_include segments.md section='Actualiser les paramètres' %}

### Étape 5 : Enregistrez votre extension de segment

Après avoir sélectionné **Enregistrer**, le traitement de votre demande d'extension commencera. La durée nécessaire pour générer votre extension dépend du nombre d’utilisateurs que vous avez, du nombre d’événements personnalisés ou d’événements d’achat que vous collectez, et du nombre de jours que vous analysez dans l’historique.

Pendant que votre extension est en cours de traitement, vous verrez une petite animation à côté du nom de l'extension, et le mot "Processing" dans la colonne **Last Processed de** la liste des extensions. Notez que vous ne pourrez pas modifier une extension lorsqu’elle est en cours de traitement.

![Page "Segment Extensions" avec deux extensions actives.]({% image_buster /assets/img/segment/segment_extension5.png %})

Lors du traitement d'une extension de segments, Braze continuera d'utiliser l'historique des versions du segment d'avant le début du traitement à des fins de segmentation de l'audience. Le traitement a lieu à chaque fois qu'un enregistrement ou une actualisation se produit, et implique l'interrogation et l'actualisation des profils utilisateurs - en d'autres termes, la composition de votre segmentation n'est pas mise à jour instantanément. Cela signifie que si l'action d'un utilisateur n'est pas effectuée avant le début de l'actualisation, nous ne pouvons pas garantir que l'utilisateur sera inclus dans l'extension de segments une fois l'actualisation terminée. Inversement, les utilisateurs qui figuraient dans l'extension de segment avant l'actualisation et qui ne répondent plus aux critères continueront à correspondre à votre segmentation jusqu'à ce que le processus d'actualisation soit terminé et que les mises à jour soient appliquées.

### Étape 6 : Utiliser votre extension dans un segment

Après avoir créé une extension, vous pouvez l'utiliser comme filtre lors de la création d'un segment ou de la définition d'une audience pour une campagne ou un Canvas. Commencez par choisir l'**extension segmentation de Braze** dans la liste des filtres de la section **Attributs de l'utilisateur**.

![Section "Filtres" avec un filtre déroulant affichant "Braze Segment Extensions".]({% image_buster /assets/img/segment/segment_extension7.png %})

Dans la liste des filtres Braze Segment Extension, choisissez l’extension que vous souhaitez inclure ou exclure de ce segment.

![Un filtre "Braze Segment Extensions" qui inclut un segment "1 clic d'e-mail dans les 56 derniers jours".]({% image_buster /assets/img/segment/segment_extension6.png %})

Pour consulter les critères d'extension, sélectionnez **Afficher les détails de l'extension** pour afficher les détails dans une nouvelle fenêtre.

![Extension pour "1 clic d'e-mail dans les 56 derniers jours".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Vous pouvez maintenant procéder comme d'habitude à la [création de votre segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Foire aux questions

### Puis-je créer une extension de segments qui utilise plusieurs événements personnalisés ?

Oui. Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake lorsque vous utilisez les [extensions de segments SQL.]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) 

Lorsque vous utilisez l'extension **simple** Segment Extensions, vous pouvez sélectionner un événement personnalisé, un événement d'achat ou une interaction de canal. Toutefois, vous pouvez combiner plusieurs extensions de segments à l'aide d'un ET ou d'un OU lors de la création du segment.

### Puis-je archiver des extensions de segments si elles existent dans une campagne active ?

Non. Avant de pouvoir archiver une extension de segment, vous devez la supprimer de tous les envois de messages actifs.

### Puis-je utiliser des tableaux dans les extensions de segments ?

Oui. Pour utiliser des tableaux, ajoutez des crochets (`[]`) au nom de votre propriété. Si votre propriété est `location_code`, vous devez saisir `location_code[]`. 

Braze utilise `[]` pour parcourir les tableaux et vérifier si un élément du tableau parcouru correspond à la propriété de l'événement. Par exemple, vous pouvez créer une segmentation des utilisateurs qui correspondent à au moins une valeur d'une propriété d'un tableau.

### Comment Braze calcule-t-il la période de temps pour une période relative de "derniers \__ jours" ?

Lorsque les extensions de segments calculent la période relative ("les X derniers jours"), l'heure de début est fixée à minuit UTC. Par exemple, pour une extension de segment qui s'actualise le 2024-09-16 21:00 UTC et spécifie 10 jours, l'heure de début est fixée au 2024-09-06 00:00 UTC, et non au 2024-09-06 21:00 UTC. 

Toutefois, vous pouvez spécifier les fuseaux horaires en utilisant des segments SQL pour identifier les utilisateurs qui ont effectué l'événement personnalisé il y a 10 jours en se basant sur minuit à l'heure de la société, ou les utilisateurs qui ont effectué l'événement il y a 10 jours en se basant sur l'heure actuelle.

