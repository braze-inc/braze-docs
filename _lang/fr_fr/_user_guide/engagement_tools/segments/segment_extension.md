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

La segmentation de Braze vous permet de cibler les utilisateurs en fonction d'un événement personnalisé ou d'un comportement d'achat. Les extensions de segments renforcent cette capacité en vous permettant de puiser dans les données historiques enregistrées dans le profil utilisateur. Grâce aux extensions de segments, vous pouvez identifier et atteindre les utilisateurs qui ont réalisé un événement personnalisé ou un événement d'achat, quel que soit le nombre de fois au cours des deux dernières années (730 jours). 

## Pourquoi utiliser les extensions de segments ?

Les segments de Braze vous offrent de puissants outils de ciblage pour créer des groupes dynamiques d'utilisateurs. Pour la plupart des cas d'utilisation, cela suffit pour atteindre votre audience de manière efficace. Les extensions de segments sont conçues pour les cas d'utilisation avancés dans lesquels vous devez analyser des comportements remontant jusqu'à deux ans ou appliquer une logique complexe, sans compromettre la conservation des données ou les performances du système. Vous pouvez utiliser des requêtes [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) (SQL Segment Extensions) ou des données provenant de votre propre [entrepôt de données]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) pour affiner davantage votre audience.

Par exemple, la segmentation par défaut de Braze trouvera les utilisateurs qui correspondent à des critères spécifiques que vous définissez, comme l'identification d'un utilisateur qui a récemment acheté l'un de vos produits. Les extensions de segments vous permettent d'aller plus loin, par exemple en identifiant les utilisateurs qui ont acheté une couleur particulière d'un produit spécifique au moins deux fois il y a 18 à 24 mois. Les extensions de segments constituent une amélioration et non une exigence. Si vous avez besoin de filtres plus avancés ou d'une fenêtre d'observation plus longue, ils constituent un excellent outil pour vous aider tout en optimisant l'utilisation de vos données.

{% alert note %}
Par défaut, 25 extensions de segments actives sont attribuées par espace de travail à un moment donné. Si vous avez besoin d'augmenter cette limite, contactez votre gestionnaire satisfaction client Braze pour discuter de votre cas d'utilisation.
{% endalert %}

## Création d'une extension de segmentation

Pour créer une extension de segment, vous allez créer un filtre pour affiner un segment de vos utilisateurs sur la base de propriétés d'événement personnalisées. Lors de la création d'une extension de segments, vous choisirez si le segment sera statique ou s'il sera actualisé dynamiquement à un intervalle donné.

### Étape 1 : Naviguer vers les extensions de segments

Allez dans **Audience** > **Extensions de** segments.

Dans le tableau Extensions de segments, sélectionnez **Créer une nouvelle extension**, puis sélectionnez votre expérience de création d'extensions de segments :

- **Extension simple :** Créez une extension de segmentation axée sur un seul événement en utilisant un formulaire guidé.
Le mieux pour les cas où vous ne voulez pas utiliser SQL.
- **Commencez par un modèle :** Créez un segment SQL avec un modèle personnalisable en utilisant les données de Snowflake.
- **Actualiser de manière incrémentielle :** Écrivez un segment SQL Snowflake qui actualise automatiquement les données des deux derniers jours ou qui les actualise manuellement si nécessaire. Le meilleur moyen d'équilibrer la précision et le rapport coût-efficacité.
- **Actualiser complètement :** Ecrivez un segment SQL avec les données de Snowflake ou toute autre [source connectée à CDI]({{site.baseurl}}/cdi_segment_extensions/) qui actualise l'ensemble de l'audience lors d'une réactualisation manuelle. C'est la solution idéale lorsque vous avez besoin d'une vue complète et actualisée de votre audience.

!Table avec différentes expériences de création d'extensions de segments à choisir.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Si vous sélectionnez une expérience qui utilise SQL, reportez-vous à la section [Extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) pour plus d'informations. Si vous sélectionnez **Extension simple**, passez à l'étape 2.

#### Utilisation du crédit SQL

Les types d'extensions de segments suivants consomment des crédits SQL :

- SQL Segment Extensions (actualisation incrémentielle et complète)
- Segments du catalogue
- Segments du CDI 
    - Les crédits sont consommés dans votre propre entrepôt de données

### Étape 2 : Nommez votre extension de segmentation

Nommez votre extension de segments en décrivant le type d'utilisateurs que vous souhaitez filtrer. Cela permettra de découvrir facilement et précisément cette extension lorsque vous l'appliquerez comme filtre dans votre segmentation.

!Extension de segmentation nommée "Extension pour les acheteurs en ligne - 90 jours".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Étape 3 : Choisissez vos critères

Sélectionnez des critères d'achat, d'engagement message ou d'événement personnalisé pour le ciblage. Après avoir sélectionné les critères du type d'événement souhaité, choisissez l'article acheté, l'interaction du message ou l'événement personnalisé spécifique que vous souhaitez cibler pour votre liste d'utilisateurs. Choisissez ensuite le nombre de fois (supérieur, inférieur ou égal) que l'utilisateur doit avoir effectué l'événement, ainsi que la période de temps - pour les extensions de segments en particulier, vous pouvez remonter jusqu'aux 730 derniers jours (2 ans).

La segmentation basée sur les données d'événements de plus de 730 jours peut être effectuée à l'aide d'autres filtres situés dans **Segments**. Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relatives pour sélectionner les X derniers jours, une date de début, une date de fin ou une plage de dates exactes (de la date A à la date B).

Critères de segmentation pour les utilisateurs qui ont effectué un événement personnalisé plus de 2 fois entre le 1er et le 31 mars 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### Segmentation des propriétés d'événement

Pour accroître la précision du ciblage, cochez la case **Ajouter des filtres de propriété**. Cela vous permettra d'effectuer des recherches en fonction des propriétés spécifiques de votre achat ou de votre événement personnalisé. Nous prenons en charge la segmentation des propriétés d'événement sur la base de chaînes de caractères, d'objets numériques, booléens et temporels.

Pour les propriétés de type chaîne de caractères, vous pouvez saisir plusieurs valeurs à la fois. Dans l'exemple ci-dessous, ce filtre recherche les utilisateurs dont le statut est égal à l'une des valeurs suivantes : or, argent ou bronze.

\![Segmentation basée sur les propriétés des chaînes de caractères.]({% image_buster /assets/img/segment/property5.png %})

!Segmentation basée sur les propriétés numériques.]({% image_buster /assets/img/segment/property2.png %})

!Segmentation basée sur des propriétés booléennes.]({% image_buster /assets/img/segment/property3.png %})

!Segmentation basée sur des objets de type datetime.]({% image_buster /assets/img/segment/property4.png %})

Nous prenons également en charge la segmentation basée sur les [propriétés d'événements imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

!Segmentation basée sur les propriétés d'événements imbriqués.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Les extensions de segments reposent sur le stockage à long terme des propriétés d'événement et n'ont pas de limite de stockage des propriétés horodatées. Vous pouvez consulter les propriétés d'événement suivies au cours des deux dernières années. L'utilisation des propriétés d'événement dans les extensions de segments n'a pas d'incidence sur l'utilisation des points de données.

{% alert note %}
Vous n'avez pas besoin des extensions de segment pour utiliser les propriétés d'événement ou les attributs personnalisés imbriqués dans votre segment. Les extensions de segments ne font que prolonger la fenêtre historique utilisée pour créer un segment par défaut. Vous pouvez créer un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) par défaut en temps réel qui utilise les propriétés des événements des 30 derniers jours ou des attributs personnalisés imbriqués. De même, vous pouvez [planifier le]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) déclenchement de [votre message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) en temps réel sur la base d'une propriété d'événement - aucune extension de segment n'est nécessaire.
{% endalert %}

### Étape 4 : Désigner des paramètres d'actualisation (facultatif)

{% multi_lang_include segments.md section='Refresh settings' %}

### Étape 5 : Enregistrez votre extension de segmentation

Après avoir sélectionné **Enregistrer**, le traitement de votre extension de segments commencera. Le temps nécessaire pour générer votre extension de segmentation dépend du nombre d'utilisateurs, du nombre d'événements personnalisés ou d'événements d'achat que vous capturez et du nombre de jours de l'historique.

Pendant que votre extension de segment est en cours de traitement, vous verrez une petite animation à côté du nom de l'extension de segment, et le mot "Processing" dans la colonne **Last Processed (Dernier traitement) de** la liste des extensions de segment. Notez que vous ne pourrez pas modifier une extension de segments pendant qu'elle est en cours de traitement.

!page "Extensions de segments" avec deux extensions actives.]({% image_buster /assets/img/segment/segment_extension5.png %})

Lors du traitement d'une extension de segments, Braze continue d'utiliser l'historique des versions du segment par défaut d'avant le début du traitement à des fins de segmentation de l'audience. Le traitement a lieu à chaque fois qu'un enregistrement ou une actualisation se produit et implique l'interrogation et la mise à jour des profils utilisateurs - en d'autres termes, la composition de votre segment par défaut n'est pas mise à jour instantanément. Cela signifie que si l'action d'un utilisateur n'est pas effectuée avant le début de l'actualisation, nous ne pouvons pas garantir que l'utilisateur sera inclus dans l'extension de segments une fois l'actualisation terminée. Inversement, les utilisateurs qui faisaient partie de l'extension de segment avant l'actualisation et qui ne répondent plus aux critères continueront à correspondre à votre segmentation de sourds jusqu'à ce que le processus d'actualisation soit terminé et que les mises à jour soient appliquées.

### Étape 6 : Utilisez votre extension dans un segment

Après avoir créé une extension de segment, vous pouvez l'utiliser comme filtre lors de la création d'un segment ou de la définition d'une audience pour une campagne ou un Canvas. Commencez par choisir l'**extension segmentation de Braze** dans la liste des filtres de la section **Attributs de l'utilisateur**.

!section "Filtres" avec un filtre déroulant affichant "Extensions de segments Braze".]({% image_buster /assets/img/segment/segment_extension7.png %})

Dans la liste de filtres Extension de segment de Braze, choisissez l'extension de segment que vous souhaitez inclure ou exclure dans ce segment.

Un filtre "Braze Segment Extensions" qui inclut un segment "1 click e-mail dans les 56 derniers jours".]({% image_buster /assets/img/segment/segment_extension6.png %})

Pour consulter les critères de segmentation, sélectionnez **Afficher les détails de l'extension** pour afficher les détails dans une nouvelle fenêtre.

!Extension pour "1 clic d'e-mail dans les 56 derniers jours".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Vous pouvez maintenant procéder comme d'habitude à la [création de votre segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Questions fréquemment posées

### Puis-je créer une extension de segments qui utilise plusieurs événements personnalisés ?

Oui. Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake lorsque vous utilisez les [extensions de segments SQL.]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) 

Lorsque vous utilisez les extensions **simples** de segments, vous pouvez sélectionner un événement personnalisé, un événement d'achat ou une interaction de canal. Toutefois, vous pouvez combiner plusieurs extensions de segments à l'aide d'un ET ou d'un OU lors de la création du segment par défaut.

### Puis-je archiver des extensions de segments si elles existent dans une campagne active ?

Non. Avant de pouvoir archiver une extension de segment, vous devez la supprimer de tous les envois de messages actifs.

### Puis-je utiliser des tableaux dans les extensions de segments ?

Oui. Pour utiliser des tableaux, ajoutez des crochets (`[]`) au nom de votre propriété. Si votre propriété est `location_code`, vous devez saisir `location_code[]`. 

Braze utilise `[]` pour parcourir les tableaux et vérifier si un élément du tableau parcouru correspond à la propriété de l'événement. Par exemple, vous pouvez créer une extension de segments pour les utilisateurs qui correspondent à au moins une valeur d'une propriété d'un tableau.

### Comment Braze calcule-t-il la période pour une période relative de "derniers __ jours" ?

Lorsque les extensions de segments calculent la période relative ("les X derniers jours"), l'heure de début est fixée à minuit UTC. Par exemple, pour une extension de segment qui s'actualise le 2024-09-16 21:00 UTC et spécifie 10 jours, l'heure de début est fixée au 2024-09-06 00:00 UTC, et non au 2024-09-06 21:00 UTC. 

Toutefois, vous pouvez spécifier les fuseaux horaires en utilisant des segments SQL pour identifier les utilisateurs qui ont effectué l'événement personnalisé il y a 10 jours en se basant sur minuit à l'heure de la société, ou les utilisateurs qui ont effectué l'événement il y a 10 jours en se basant sur l'heure actuelle.

