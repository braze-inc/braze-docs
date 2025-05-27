---
nav_title: Extensions de segments
article_title: Extensions de segments
page_order: 3.1
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

![Table avec différentes expériences de création d'extensions de segments à choisir.][20]{: style="max-width:50%"}

Si vous sélectionnez une expérience qui utilise SQL, reportez-vous à la section [Extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) pour plus d'informations.

Si vous sélectionnez l'**extension simple**, passez aux étapes suivantes.

### Étape 2 : Nommer votre Segment Extension

Nommez votre Segment Extension en décrivant le type d’utilisateur que vous souhaitez cibler. Cela vous permettra de retrouver facilement cette extension lorsque vous souhaiterez l’utiliser en tant que filtre dans votre segment.

![Segment Extension nommée « Online Shoppers Extenion - 90 Days (Extension pour acheteurs en ligne : 90 jours) » avec la case « Regenerate Extension Daily (Renouveler l’extension quotidiennement) » cochée.][2]

### Étape 3 : Choisir vos critères

Sélectionnez un critère d’achat, de message, d’engagement ou d’événement personnalisé pour le ciblage. Après avoir sélectionné les critères du type d'événement souhaité, choisissez l'article acheté, l'interaction du message ou l'événement personnalisé spécifique que vous souhaitez cibler pour votre liste d'utilisateurs. Choisissez ensuite le nombre de fois (supérieur, inférieur ou égal) que l'utilisateur doit avoir effectué l'événement, ainsi que la période de temps - pour les extensions de segments en particulier, vous pouvez remonter jusqu'aux 730 derniers jours (2 ans).

La segmentation basée sur les données d'événements de plus de 730 jours peut être effectuée à l'aide d'autres filtres disponibles dans **Segments**. Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relatives (par exemple les X derniers jours), une date de début, une date de fin ou une plage de dates exactes (de la date A à la date B).

![Critères de segmentation pour les utilisateurs qui ont effectué un événement personnalisé, "# de aaa", plus de 0 fois dans la plage de dates du 1er août 2023 au 10 août 2023.][3]

#### Segmentation des propriétés de l’événement

Pour accroître la précision du ciblage, cochez la case **Ajouter des filtres de propriété**. Cela vous permettra d’analyser les résultats en fonction des propriétés spécifiques de votre achat ou événement personnalisé. Nous prenons en charge la segmentation des propriétés de l’événement en fonction des objets de chaîne de caractères, numériques, booléens et temporels.

Pour les propriétés des chaînes de caractères, vous pouvez saisir plusieurs valeurs à la fois. Dans l'exemple ci-dessous, ce filtre recherche les utilisateurs dont le statut est égal à l'une des valeurs suivantes : or, argent ou bronze.

![Segmentation basée sur les propriétés des chaînes de caractères.][13.5]

![Segmentation basée sur les propriétés numériques.][13]

![Segmentation basée sur les propriétés booléennes.][14]

![Segmentation basée sur les objets temporels.][15]

Nous prenons également en charge la segmentation basée sur les [propriétés d'événements imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmenter en fonction de propriétés de l’événement imbriqué.][18]

Les Segment Extensions s’appuient sur le stockage à long terme des propriétés de l’événement et n’ont pas de limite de stockage de propriété horodatée. Vous pouvez regarder les propriétés de l’événement suivies sur les deux dernières années. L’utilisation de propriétés de l’événement dans des Segment Extensions n’affecte pas l’utilisation de vos points de données.

{% alert note %}
Vous n'avez pas besoin des extensions de segment pour utiliser les propriétés d'événement ou les attributs personnalisés imbriqués dans votre segment. Les extensions de segments ne font que prolonger la fenêtre historique utilisée pour créer un segment. Vous pouvez créer un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) en temps réel qui utilise les propriétés d'événements des 30 derniers jours ou des attributs personnalisés imbriqués. De même, vous pouvez [planifier le déclenchement de votre message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) en temps réel sur la base d'une propriété d'événement - aucune extension de segment n'est nécessaire.
{% endalert %}

### Étape 4 : Désigner des paramètres d'actualisation (facultatif)

Si vous n'avez pas besoin que votre extension soit actualisée à intervalles réguliers, vous pouvez l'enregistrer sans utiliser les paramètres d'actualisation, et Braze générera par défaut votre extension de segmentation en fonction de votre adhésion d'utilisateur à ce moment-là. Utilisez le comportement par défaut si vous ne souhaitez générer l'audience qu'une seule fois et la cibler ensuite avec une campagne ponctuelle.

Votre segmentation commencera toujours à être traitée après l'enregistrement initial. À chaque fois que votre segment est actualisé, Braze ré-exécute le segment et met à jour l'appartenance au segment pour refléter les utilisateurs de votre segment au moment de l'actualisation. Cela peut aider vos campagnes récurrentes à atteindre les utilisateurs les plus pertinents.

#### Mise en place d'une actualisation récurrente

Pour mettre en place une planification récurrente, sélectionnez **Actualiser les paramètres** dans le coin supérieur droit de votre extension spécifique. L'option permettant d'actualiser les paramètres est disponible pour tous les types d'extensions de segments, y compris les segments SQL, les segments CDI et les extensions de segments basées sur des formulaires simples.

{% alert important %}
Pour optimiser la gestion de vos données, les paramètres d'actualisation sont automatiquement désactivés pour les extensions de segments non utilisées. Les extensions de segments sont considérées comme inutilisées lorsqu'elles sont :

- N'est pas utilisé dans des campagnes, des canevas ou des segments actifs ou inactifs (brouillons, arrêtés, archivés) ; ou
- N’a pas été modifiée depuis plus de 7 jours

Braze informera le contact de l'entreprise et le créateur de l'extension si ce paramètre est désactivé. L’option permettant de renouveler les extensions quotidiennement peut être réactivée à tout moment.
{% endalert %}

#### Sélectionner vos paramètres d'actualisation

![Paramètres d'intervalle d'actualisation avec une fréquence d'actualisation hebdomadaire, une heure de début de 10 heures et le lundi sélectionné comme jour.][21]{: style="max-width:60%;"}

Dans le panneau **Paramètres d'actualisation**, vous pouvez sélectionner la fréquence à laquelle cette extension de segments sera actualisée : toutes les heures, tous les jours, toutes les semaines ou tous les mois. Vous devrez également sélectionner l'heure spécifique (dans le fuseau horaire de votre entreprise) à laquelle l'actualisation doit avoir lieu, par exemple :

- Si votre campagne d'e-mail est envoyée tous les lundis à 11 heures, heure de la société, et que vous voulez vous assurer que votre segment est actualisé juste avant l'envoi, vous devriez choisir une planification d'actualisation hebdomadaire à 10 heures les lundis.
- Si vous souhaitez que votre segmentation soit actualisée tous les jours, sélectionnez la fréquence d'actualisation quotidienne, puis choisissez l'heure à laquelle l'actualisation doit avoir lieu.

{% alert note %}
La possibilité de définir une planification d'actualisation horaire n'est pas disponible pour les extensions de segments basées sur des formulaires (mais vous pouvez définir des planifications quotidiennes, hebdomadaires ou mensuelles).
{% endalert %}

#### Consommation de crédits et coûts supplémentaires

Étant donné que les actualisations réexécutent la requête de votre segment, chaque actualisation pour les segments SQL consommera des crédits de segment SQL, et chaque actualisation pour les segments CDI entraînera un coût au sein de votre entrepôt de données third-party.

{% alert note %}
L'actualisation des segments peut prendre jusqu'à 60 minutes en raison du temps de traitement des données. Les segments en cours d'actualisation auront un statut "En cours" dans votre liste d'extensions de segments. Cela a plusieurs implications :

- Pour terminer le traitement de votre segment avant une heure précise, choisissez une heure d'actualisation située 60 minutes plus tôt. 
- Il ne peut y avoir qu'une seule actualisation à la fois pour une extension de segments donnée. En cas de conflit où une nouvelle actualisation est lancée alors qu'une actualisation existante a déjà commencé à être traitée, Braze annulera la nouvelle demande d'actualisation et poursuivra le traitement en cours.
{% endalert %}

#### Critères de désactivation automatique des extensions périmées

Les actualisations planifiées sont automatiquement désactivées lorsqu'une extension de segments est périmée. Une extension de segments est périmée si elle répond aux critères suivants :

- Non utilisé dans des campagnes ou des canvas actifs
- Non utilisé dans un segment d'une campagne ou d'un canvas actifs.
- Non utilisé dans un segment où le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) est activé.
- N'a pas été modifié depuis plus de sept jours
- N'a pas été ajouté à une campagne ou à Canvas (y compris les brouillons), ou à un segment depuis plus de sept jours.

Si l'actualisation planifiée est désactivée pour une extension de segments, une notification l'indique pour cette extension.

![Une notification indiquant que "Les actualisations planifiées ont été désactivées pour cette extension car elle n'est pas utilisée dans des campagnes, des canevas ou des segments actifs". L'extension de segments a été désactivée le 23 février 2025 à 0h00\. "][1]

Lorsque vous êtes prêt à utiliser une extension de segment périmée, [passez en revue les paramètres d'actualisation](#step-4-designate-refresh-settings-optional), sélectionnez la planification d'actualisation qui correspond à votre cas d'utilisation, puis enregistrez toutes les modifications.

### Étape 5 : Enregistrez votre extension de segment

Une fois que vous aurez sélectionné **Enregistrer**, le traitement de votre demande d'extension commencera. La durée nécessaire pour générer votre extension dépend du nombre d’utilisateurs que vous avez, du nombre d’événements personnalisés ou d’événements d’achat que vous collectez, et du nombre de jours que vous analysez dans l’historique.

Pendant que votre extension est en cours de traitement, vous verrez une petite animation à côté du nom de l'extension, et le mot "Processing" dans la colonne **Last Processed de** la liste des extensions. Notez que vous ne pourrez pas modifier une extension lorsqu’elle est en cours de traitement.

![Page "Segment Extensions" avec deux extensions actives.][5]

### Étape 6 : Utiliser votre extension dans un segment

Après avoir créé une extension, vous pouvez l’utiliser comme filtre lorsque vous créez un segment ou définissez une audience pour une campagne ou un Canvas. Commencez par choisir l'**extension segmentation de Braze** dans la liste des filtres de la section **Attributs de l'utilisateur**.

![La section "Filtres" avec un filtre déroulant affichant "Braze Segment Extensions".][6]

Dans la liste des filtres Braze Segment Extension, choisissez l’extension que vous souhaitez inclure ou exclure de ce segment.

![Un filtre "Braze Segment Extensions" qui inclut un segment "Online Shoppers Ext...".][7]

Pour afficher les critères de l'extension, sélectionnez **Afficher les détails de l'extension** pour afficher les détails dans une fenêtre modale/boîte de dialogue, etc.

![Détails de l'extension pour le "Online Shoppers Extension - 90 Days".][8]{: style="max-width:70%;"}

Vous pouvez maintenant [créer votre segment][11] comme vous le faites habituellement.

## Foire aux questions

### Puis-je créer une extension de segments qui utilise plusieurs événements personnalisés ?

Oui. Vous pouvez ajouter plusieurs événements ou référencer plusieurs tables Snowflake lorsque vous utilisez les [extensions de segments SQL.]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) 

Lorsque vous utilisez l'extension **simple** Segment Extensions, vous pouvez sélectionner un événement personnalisé, un événement d'achat ou une interaction de canal. Toutefois, vous pouvez combiner plusieurs extensions de segments à l'aide d'un ET ou d'un OU lors de la création du segment.

### Puis-je archiver des extensions de segments si elles existent dans une campagne active ?

Non. Avant de pouvoir archiver une extension de segment, vous devez la supprimer de tous les envois de messages actifs.

[1]: {% image_buster /assets/img/segment/segment_extension_disabled.png %}
[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension1.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[13.5]: {% image_buster /assets/img/segment/property5.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}
