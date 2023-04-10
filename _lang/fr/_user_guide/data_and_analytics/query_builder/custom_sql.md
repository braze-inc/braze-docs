---
nav_title: SQL personnalisé dans le générateur de requêtes
article_title: SQL personnalisé dans le générateur de requêtes
page_order: 1
page_type: reference
description: "Cet article de référence décrit comment utiliser du SQL personnalisé pour débloquer de nouveaux insights dans le générateur de requêtes."
tool: Reports
---

# SQL personnalisé dans le générateur de requêtes

Avec le générateur de requêtes, vous pouvez générer des rapports en utilisant les données Braze dans Snowflake qui utilise maintenant du SQL personnalisé pour débloquer de nouveaux insights.

{% alert important %}
L’éditeur SQL est en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Créer des rapports SQL personnalisés

Pour exécuter un rapport :

1. Rendez-vous sur **Query Builder (Générateur de requêtes)**, sous **Data (Données)**.
2. Cliquez sur **+ Create New SQL Report (+ Créer un nouveau rapport SQL)**.
3. Votre rapport reçoit automatiquement un nom avec la date et l’heure actuelles. Survolez le nom et cliquez <i class="fas fa-pencil" alt="Modifier"></i> pour donner un nom significatif à votre requête SQL.
4. Écrivez votre requête SQL dans l’éditeur. Consultez [Écriture SQL](#writing-sql) pour voir les exigences et des ressources.
5. Cliquez sur **Run Query (Exécuter la requête)**.
6. Enregistrez votre requête.
7. Pour télécharger votre rapport au format CSV, cliquez sur **Export (Exporter)**.

## Données et résultats

Les résultats et les exportations de résultats sont des tableaux qui peuvent contenir jusqu’à 500 lignes. Pour les rapports qui nécessitent de plus grandes quantités de données, utilisez un autre outil tel que [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) ou les [API d’exportation]({{site.baseurl}}/api/endpoints/export) de Braze.

## Requêtes SQL

Votre requête SQL doit être rédigée en utilisant la syntaxe [Snowflake](https://docs.snowflake.com/en/sql-reference). Consultez le [tableau de référence]({{site.baseurl}}/sql_segments_tables/) pour obtenir une liste complète des tableaux et colonnes disponibles pour la requête.

Pour afficher les détails du tableau dans le générateur de requêtes :

1. Dans la page **Query Builder (Générateur de requêtes)**, sélectionnez l'onglet **Available Data Tables (Tables de données disponibles)** pour afficher les tables de données disponibles et leurs noms.
3. Cliquez sur <i class="fas fa-chevron-down" alt=""></i> **See Details (Voir les détails)** pour afficher la description du tableau et les informations sur les colonnes du tableau, telles que les types de données.
4. Pour insérer le nom de la table dans votre SQL, cliquez sur <i class="fas fa-copy" title="Copier le nom de la table dans l'éditeur SQL"></i>.

Pour afficher les requêtes pré-écrites fournies par Braze :

1. Sélectionnez l’onglet **Query Templates (Modèles de requête)**.
2. Sélectionnez le rapport que vous souhaitez exécuter.
3. Cliquez sur **Run Query (Exécuter la requête)** pour afficher les résultats.

Restreindre votre requête à une période spécifique vous aidera à générer des résultats plus rapidement. Voici un exemple de requête qui obtient le nombre d’achats et le chiffre d’affaires généré pour la dernière heure.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Cette requête récupère le nombre d’envois d’e-mails au cours du dernier mois :

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

## Résolution des problèmes

Votre requête peut échouer pour l’une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Temporisation du traitement (après 6 minutes)
    - Les rapports qui prennent plus de 6 minutes à s’exécuter vont expirer.
    - Si un rapport expire, essayez de limiter la plage de temps pour laquelle vous requêtez les données ou requêtez un ensemble de données plus spécifique.