---
nav_title: Extensions de segments
article_title: Extensions de segments
page_order: 3.1

page_type: tutorial
description: "Cet article pratique vous explique comment configurer et utiliser une extension de segments pour améliorer vos capacités de segmentation."
tool: Segments
---

# Extensions de segments

> La segmentation de Braze vous permet de cibler les utilisateurs en fonction d'un événement personnalisé ou d'un comportement d'achat stocké pendant toute la durée de vie de ce profil utilisateur. Les exemples comprennent le fait de trouver des utilisateurs qui ont ou n’ont pas effectué un événement personnalisé donné depuis un moment spécifique, ou bien de segmenter les utilisateurs sur la base des produits qu’ils ont déjà achetés ou combien d’argent ils ont dépensé pour votre service.

Les Segment Extensions sont des définitions d’audience vous permettant d’utiliser des propriétés de l’événement imbriqué ou créer des ensembles fenêtrés d’un événement personnalisé et des propriétés de l’événement d’achat au cours des deux dernières années (730 jours). Par exemple, la segmentation de Braze vous permet de trouver les utilisateurs qui ont acheté un produit spécifique au cours de leur vie. Avec Segment Extensions, vous pouvez affiner cette audience pour des utilisateurs qui ont acheté une couleur donnée d’un produit donné au moins deux fois au cours des 2 dernières années. Lorsque vous créez une extension de segment, vous pouvez également spécifier si l’audience est statique ou régénérée toutes les 24 heures.

L’utilisation des propriétés de l’événement imbriqué pour la [livraison par événement][19] n’a pas besoin d’extensions de segment, étant donné que le traitement des événements s’effectue en temps réel. De même, les Attributs personnalisés imbriqués n’ont pas besoin d’utiliser les Segment Extensions.

{% alert important %}
Par défaut, 25 extensions de segments actives sont allouées par espace de travail à un moment donné. Si vous avez besoin d’augmenter cette limite, contactez votre gestionnaire du succès des clients Braze pour discuter de votre cas d’utilisation.
{% endalert %}

## Étape 1 : Accéder aux Segment Extensions

Sélectionnez **Audience** > **Extensions de segments**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez cette page sous **Engagement** > **Segments** > **Extensions de segments**.
{% endalert %}

Dans le tableau Extensions de segments, cliquez sur **Créer une nouvelle extension**, puis sélectionnez votre expérience de création d'extensions de segments :

- **Extension simple :** Créez une extension de segment axée sur un seul événement en utilisant un formulaire guidé.
Il s’agit de la meilleure option si vous ne souhaitez pas utiliser de code SQL.
- **Commencez par un modèle :** Créez un segment SQL avec un modèle personnalisable en utilisant des données Snowflake.
- **Actualisation progressive :** Écrivez un segment SQL Snowflake qui actualise automatiquement les deux derniers jours de données ou les actualise manuellement selon les besoins. Il s’agit du meilleur compromis précision/coût.
- **Actualisation complète :** Écrivez un segment SQL Snowflake qui recalcule l’intégralité de l’audience lors d’une actualisation manuelle. Il s’agit de la meilleure option lorsque vous avez besoin d’une vision complète et actualisée de votre audience.

![][20]{: style="max-width:50%"}

Si vous sélectionnez une expérience qui utilise SQL, reportez-vous à la section [Extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) pour plus d'informations.

Si vous sélectionnez l'**extension simple**, passez aux étapes suivantes.

## Étape 2 : Nommer votre Segment Extension

Nommez votre Segment Extension en décrivant le type d’utilisateur que vous souhaitez cibler. Cela vous permettra de retrouver facilement cette extension lorsque vous souhaiterez l’utiliser en tant que filtre dans votre segment.

![Segment Extension nommée « Online Shoppers Extenion - 90 Days (Extension pour acheteurs en ligne : 90 jours) » avec la case « Regenerate Extension Daily (Renouveler l’extension quotidiennement) » cochée.][2]

## Étape 3 : Choisir vos critères

Sélectionnez un critère d’achat, de message, d’engagement ou d’événement personnalisé pour le ciblage. Après avoir sélectionné les critères du type d'événement souhaité, choisissez l'article acheté, l'interaction du message ou l'événement personnalisé spécifique que vous souhaitez cibler pour votre liste d'utilisateurs. Choisissez ensuite le nombre de fois (supérieur, inférieur ou égal) que l'utilisateur doit avoir effectué l'événement, ainsi que la période de temps - pour les extensions de segments en particulier, vous pouvez remonter jusqu'aux 730 derniers jours (2 ans).

La segmentation basée sur les données d'événements de plus de 730 jours peut être effectuée à l'aide d'autres filtres disponibles dans **Segments**. Lorsque vous choisissez votre période, vous pouvez spécifier une plage de dates relatives (par exemple les X derniers jours), une date de début, une date de fin ou une plage de dates exactes (de la date A à la date B).

![][3]

### Segmentation des propriétés de l’événement

Pour accroître la précision du ciblage, cochez la case **Ajouter des filtres de propriété**. Cela vous permettra d’analyser les résultats en fonction des propriétés spécifiques de votre achat ou événement personnalisé. Nous prenons en charge la segmentation des propriétés de l’événement en fonction des objets de chaîne de caractères, numériques, booléens et temporels.

Pour les propriétés des chaînes de caractères, vous pouvez saisir plusieurs valeurs à la fois. Dans l'exemple ci-dessous, ce filtre recherche les utilisateurs dont le statut est égal à l'une des valeurs suivantes : or, argent ou bronze.

![Segmentation basée sur les propriétés des chaînes de caractères.][13.5]

![Segmentation basée sur les propriétés numériques.][13]

![Segmentation basée sur les propriétés booléennes.][14]

![Segmentation basée sur les objets temporels.][15]

Nous prenons également en charge la segmentation basée sur les [propriétés d'événements imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/).

![Segmenter en fonction de propriétés de l’événement imbriqué.][18]

Les Segment Extensions s’appuient sur le stockage à long terme des propriétés de l’événement et n’ont pas de limite de stockage de propriété horodatée. Vous pouvez regarder les propriétés de l’événement suivies sur les deux dernières années.

{% alert note %}
L’utilisation de propriétés de l’événement dans des Segment Extensions n’affecte pas l’utilisation de vos points de données.
{% endalert %}

## Étape 4 : Désigner des paramètres d'actualisation (facultatif)

Si vous n'avez pas besoin que votre extension soit actualisée à intervalles réguliers, vous pouvez l'enregistrer sans utiliser les paramètres d'actualisation, et Braze générera par défaut votre extension de segmentation en fonction de votre adhésion d'utilisateur à ce moment-là. Utilisez le comportement par défaut si vous ne souhaitez générer l'audience qu'une seule fois et la cibler ensuite avec une campagne ponctuelle.

Votre segmentation commencera toujours à être traitée après l'enregistrement initial. À chaque fois que votre segment est actualisé, Braze ré-exécute le segment et met à jour l'appartenance au segment pour refléter les utilisateurs de votre segment au moment de l'actualisation. Cela peut aider vos campagnes récurrentes à atteindre les utilisateurs les plus pertinents.

### Mise en place d'une actualisation récurrente

Pour mettre en place une planification récurrente, sélectionnez **Actualiser les paramètres** dans le coin supérieur droit de votre extension spécifique. L'option permettant d'actualiser les paramètres est disponible pour tous les types d'extensions de segments, y compris les segments SQL, les segments CDI et les extensions de segments basées sur des formulaires simples.

{% alert important %}
Les paramètres d'actualisation sont automatiquement désactivés pour les extensions de segments non utilisées. Braze définit une extension non utilisée comme une extension répondant aux critères suivants :

- Utilisée dans aucune campagne, ni aucun canvas ou segment actif
- Utilisée dans aucune campagne, ni aucun canvas ou segment inactif, à l’état d’ébauche, abandonné(e) ou archivé(e)
- N’a pas été modifiée depuis plus de 7 jours

Si ce paramètre est désactivé, Braze informera son contact au sein de l’entreprise ainsi que la personne ayant créé l’extension. L’option permettant de renouveler les extensions quotidiennement peut être réactivée à tout moment.
{% endalert %}

#### Sélectionner vos paramètres d'actualisation

![Paramètres d'intervalle d'actualisation avec une fréquence d'actualisation hebdomadaire, une heure de début de 10 heures et le lundi sélectionné comme jour.][21]{: style="max-width:60%;"}

Dans le panneau **Paramètres d'actualisation**, vous pouvez sélectionner la fréquence à laquelle cette extension de segments sera actualisée : toutes les heures, tous les jours, toutes les semaines ou tous les mois. Vous devrez également sélectionner l'heure spécifique (dans le fuseau horaire de votre entreprise) à laquelle l'actualisation doit avoir lieu, par exemple :

- Si votre campagne d'e-mail est envoyée tous les lundis à 11 heures, heure de la société, et que vous voulez vous assurer que votre segment est actualisé juste avant l'envoi, vous devriez choisir une planification d'actualisation hebdomadaire à 10 heures les lundis.
- Si vous souhaitez que votre segmentation soit actualisée tous les jours, sélectionnez la fréquence d'actualisation quotidienne, puis choisissez l'heure à laquelle l'actualisation doit avoir lieu.

{% alert note %}
La possibilité de définir une planification d'actualisation horaire n'est pas disponible pour les extensions de segments basées sur des formulaires (mais vous pouvez définir des planifications quotidiennes, hebdomadaires ou mensuelles).
{% endalert %}

### Consommation de crédits et coûts supplémentaires

Étant donné que les actualisations réexécutent la requête de votre segment, chaque actualisation pour les segments SQL consommera des crédits de segment SQL, et chaque actualisation pour les segments CDI entraînera un coût au sein de votre entrepôt de données third-party.

{% alert note %}
L'actualisation des segments peut prendre jusqu'à 60 minutes en raison du temps de traitement des données. Les segments en cours d'actualisation auront un statut "En cours" dans votre liste d'extensions de segments. Cela a plusieurs implications :

- Pour terminer le traitement de votre segment avant une heure précise, choisissez une heure d'actualisation située 60 minutes plus tôt. 
- Il ne peut y avoir qu'une seule actualisation à la fois pour une extension de segments donnée. En cas de conflit où une nouvelle actualisation est lancée alors qu'une actualisation existante a déjà commencé à être traitée, Braze annulera la nouvelle demande d'actualisation et poursuivra le traitement en cours.
{% endalert %}

## Étape 5 : Enregistrez votre extension de segment

Une fois que vous aurez cliqué sur **Enregistrer**, le traitement de votre demande d'extension commencera. La durée nécessaire pour générer votre extension dépend du nombre d’utilisateurs que vous avez, du nombre d’événements personnalisés ou d’événements d’achat que vous collectez, et du nombre de jours que vous analysez dans l’historique.

Pendant que votre extension est en cours de traitement, vous verrez une petite animation à côté du nom de l'extension, et le mot "Processing" dans la colonne **Last Processed de** la liste des extensions. Notez que vous ne pourrez pas modifier une extension lorsqu’elle est en cours de traitement.

![][5]

## Étape 6 : Utiliser votre extension dans un segment

Après avoir créé une extension, vous pouvez l’utiliser comme filtre lorsque vous créez un segment ou définissez une audience pour une campagne ou un Canvas. Commencez par choisir l'**extension segmentation de Braze** dans la liste des filtres de la section **Attributs de l'utilisateur**.

![][6]

Dans la liste des filtres Braze Segment Extension, choisissez l’extension que vous souhaitez inclure ou exclure de ce segment.

![][7]

Pour afficher les critères de l'extension, cliquez sur **Afficher les détails de l'extension** pour afficher les détails dans une fenêtre modale.

![][8]{: style="max-width:70%;"}

Vous pouvez maintenant [créer votre segment][11] comme vous le faites habituellement.

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
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}
