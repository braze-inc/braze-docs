---
nav_title: Segments CDI
article_title: Segments CDI
page_order: 0
page_type: reference
tool: 
- Segments
description: "Cet article pratique vous explique comment configurer le ciblage de localisation pour segmenter des utilisateurs en fonction de leur emplacement."

---

# segments CDI

> Avec Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI), vous pouvez configurer une connexion directe depuis votre entrepôt de données ou votre système de stockage de fichiers vers Braze pour synchroniser les données utilisateur ou de catalogue pertinentes de manière récurrente.

{% alert warning %}
Cette fonctionnalité interroge directement votre entrepôt de données, vous devrez donc supporter tous les coûts associés à l'exécution de ces requêtes dans votre entrepôt de données. Les segments CDI ne consommeront pas de [crédits de segment SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage), ne comptent pas dans votre limite d'extension de segment et ne consomment pas de points de données.
{% endalert %}

## Conditions préalables

Pour utiliser les données de votre entrepôt de données pour la segmentation dans votre espace de travail Braze, vous devrez créer une [source connectée]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/), puis créer un segment CDI dans vos [Extensions de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Les segments CDI vous permettent d'écrire des requêtes SQL qui interrogent directement votre propre entrepôt de données en utilisant les données mises à disposition via vos connexions CDI, et de créer un groupe d'utilisateurs pouvant être ciblés au sein de Braze.

## Création d'un segment CDI

### Étape 1 : Configurez votre source

Avant de créer votre premier segment CDI, configurez une nouvelle source connectée avec votre entrepôt de données en suivant les étapes dans [Sources connectées]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/).

### Étape 2 : Créer un segment

Tout d'abord, créez une nouvelle [Extension de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), puis sélectionnez **Actualisation complète**.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Pour votre source de données, choisissez **Tables de données CDI**.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Dans le cadre de votre configuration CDI, vous pouvez choisir parmi différentes connexions à utiliser dans les segments CDI. Chaque connexion dispose d'un ensemble spécifique de tables de données. Votre équipe de développement peut configurer vos connexions et vos tables de données lors de la configuration de CDI.

Pour voir les tables de données disponibles, sélectionnez **Référence**. Lorsque vous êtes prêt, sélectionnez une connexion.

![]({% image_buster /assets/img/segment/connection_schema.png %}){: style="max-width:100%;"}

Ensuite, écrivez le SQL pour votre segment en utilisant [la syntaxe SQL de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql).

Gardez à l'esprit que tous les segments CDI doivent utiliser `external_user_id` comme colonne sélectionnée, et votre `external_user_id` doit correspondre à celui défini dans Braze pour les utilisateurs. Si les résultats de votre requête incluent des utilisateurs qui n'existent pas dans Braze, ces utilisateurs seront ignorés. Braze ne créera pas de nouveaux utilisateurs en fonction des résultats de votre segment CDI.

{% alert tip %}
Pour savoir comment prévisualiser votre segment, gérer votre segment et exécuter des actualisations automatiques des adhésions, consultez [Extensions de segment SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/).
{% endalert %}

Enfin, vous pouvez [utiliser cette extension de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) dans un segment Braze pour envoyer une campagne ou un Canvas à ce public.

## Considérations

- Une extension de segment peut référencer des données provenant d'une seule connexion, pas de plusieurs.    
- Une extension de segment peut utiliser l'un des éléments suivants comme source de données : Données CDI ou données Braze Snowflake (Currents). Vous ne pouvez pas mélanger les sources de données dans une extension de segment, mais vous pouvez créer plusieurs extensions de segment à référencer ensemble dans un segment.

## Résolution des problèmes

- Votre requête peut expirer lorsqu'elle atteint votre temps d'exécution maximum, lequel est configuré pour chaque synchronisation de connexion sur la page **Cloud Data Ingestion**. La durée maximale autorisée est de 60 minutes.
- Assurez-vous que votre SQL est écrit en utilisant une syntaxe appropriée pour votre entrepôt de données. 
