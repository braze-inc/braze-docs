---
nav_title: Extensions de segments CDI
article_title: CDI Extensions de segments
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool: 
- Segments
description: "Cet article pratique vous explique comment configurer le ciblage par emplacement, ce qui vous permet de segmenter les utilisateurs en fonction de leur emplacement/localisation."

---

# CDI Extensions de segments

> Avec Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI), vous pouvez établir une connexion directe entre votre entrepôt de données ou votre système de stockage de fichiers et Braze pour synchroniser de manière récurrente les données pertinentes relatives aux utilisateurs ou aux catalogues.

{% alert warning %}
Les CDI Segment Extensions interrogent directement votre entrepôt de données. Vous devrez donc supporter tous les coûts liés à l'exécution de ces requêtes dans votre entrepôt de données. Les extensions de segments CDI ne consomment pas de [crédits de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), ne comptent pas dans votre limite d'extensions de segments et n'enregistrent pas de points de données.
{% endalert %}

## Conditions préalables

Pour utiliser les données de votre entrepôt de données à des fins de segmentation dans votre espace de travail Braze, vous devez créer une [source connectée]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/), puis un segment CDI dans vos [extensions de segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) Les CDI Segment Extensions vous permettent d'écrire un langage SQL qui interroge directement votre propre entrepôt de données en utilisant les données mises à disposition par vos connexions CDI, et de créer un groupe d'utilisateurs qui peut être ciblé dans Braze.

## Création d'un segment CDI

### Étape 1 : Configurez votre source

Avant de créer votre première extension de segments CDI, configurez une nouvelle source connectée avec votre entrepôt de données en suivant les étapes indiquées dans [Sources connectées]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/).

### Étape 2 : Créer une segmentation

Tout d'abord, créez une nouvelle [extension de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), puis sélectionnez l'option **Actualisation complète**.

\![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Pour votre source de données, sélectionnez **Tables de données CDI**.

\![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Dans le cadre de votre configuration CDI, vous pouvez sélectionner différentes connexions à utiliser dans les extensions de segments CDI. Chaque connexion dispose d'un ensemble spécifique de tables de données. Votre équipe de développement peut configurer vos connexions et vos tables de données lors de la configuration de CDI.

Pour afficher les tables de données disponibles, y compris leur schéma et toute description disponible, sélectionnez **Référence.** Lorsque vous êtes prêt, sélectionnez une connexion.

\![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

Ensuite, écrivez le code SQL pour votre segmentation en utilisant [la syntaxe SQL de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

N'oubliez pas que toutes les extensions de segments CDI doivent utiliser `external_user_id` comme colonne sélectionnée et que votre `external_user_id` doit correspondre à celui défini dans Braze pour les utilisateurs. Si les résultats de votre requête incluent des utilisateurs qui n'existent pas dans Braze, ces utilisateurs seront ignorés. Braze ne créera pas de nouveaux utilisateurs sur la base des résultats de votre extension de segmentation CDI.

{% alert tip %}
Pour savoir comment vous pouvez prévisualiser vos extensions de segments, gérer vos extensions de segments et actualiser automatiquement les adhésions, voir [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Enfin, vous pouvez [utiliser cette extension de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) au sein d'un segment Braze pour envoyer une campagne ou un Canvas à cette audience.

## Considérations

- Une extension de segments ne peut faire référence qu'à des données provenant d'une seule connexion, et non de plusieurs.    
- Une extension de segments peut utiliser l'un des éléments suivants comme source de données : Données CDI ou données Braze Snowflake (Currents). Vous ne pouvez pas mélanger les sources de données au sein d'une extension de segment, mais vous pouvez créer plusieurs extensions de segments à référencer ensemble au sein d'un segment.

## Résolution des problèmes

- Votre requête risque d'expirer lorsqu'elle atteint votre durée d'exécution maximale, qui est définie pour chaque synchronisation de connexion sur la page **Cloud Data Ingestion**. La durée maximale autorisée est de 60 minutes.
- Assurez-vous que votre langage SQL est écrit en utilisant la syntaxe appropriée pour votre entrepôt de données. 
