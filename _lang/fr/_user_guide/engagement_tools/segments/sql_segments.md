---
nav_title: "Segment Extensions SQL"
article_title: Segment Extensions SQL
alias: "/sql_segments/"
page_order: 3.2

page_type: reference
description: "Cet article décrit comment créer un Segment Extension (prolongement de segment) SQL à l’aide de requêtes Snowflake."
tool: Segments
---

# Segment Extensions SQL

Vous pouvez générer un Segment Extension à l’aide des requêtes SQL Snowflake des données [Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/). Le SQL peut vous aider à déverrouiller de nouveaux cas d’utilisation de segments parce qu’il offre la flexibilité nécessaire pour décrire les relations entre les données de manières qui ne sont pas réalisables par d’autres fonctionnalités de segmentation.

{% alert important %}
L’éditeur SQL est en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Créer des Segment Extensions à l’aide de SQL

Pour créer un Segment Extension à l’aide de SQL :

1. Aller sur **Segments** > **Segment Extensions**.
2. Cliquez sur **Create New Extension (Créer une nouvelle extension)** et sélectionnez **SQL Editor (Éditeur SQL)**.<br><br>
   ![Bouton du menu déroulant sur la page Segment Extension pour ouvrir l’éditeur SQL.][1]{: style="max-width:40%" }<br><br>
3. Ajoutez un nom pour votre Segment Extension et saisissez votre SQL. Consultez les sections suivantes pour connaître les exigences et les ressources.<br><br>
   ![Éditeur SQL montrant un exemple de Segment Extension SQL.][2]<br><br>
4. Enregistrer votre Segment Extension.

{% alert note %}
Les requêtes SQL qui prennent plus de 20 minutes à s’exécuter vont expirer.
{% endalert %}

Lorsque le traitement de l’extension s’achève, vous pouvez [créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) à l’aide de votre Segment Extension et cibler ce nouveau segment avec vos campagnes et vos Canvas.

### Requêtes SQL

Votre requête SQL doit être rédigée en utilisant la syntaxe [Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consultez le [tableau de référence]({{site.baseurl}}/sql_segments_tables/) pour obtenir une liste complète des tableaux et colonnes disponibles pour la requête.

Votre SQL doit de surcroit respecter les règles suivantes :

- Rédigez une seule instruction SQL. N’ajoutez pas de points-virgules.
- Votre SQL ne doit sélectionner qu’une seule colonne : la colonne `user_id`. Cela signifie que votre SQL doit contenir :

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

### Aperçu des résultats

Avant d’enregistrer, vous pouvez exécuter un aperçu de votre requête. Les aperçus de vos requêtes sont automatiquement limités à 100 lignes et expireront au bout de 60 secondes. L’exigence de la colonne `user_id` ne s’applique pas lors de l’exécution d’un aperçu.

## Gestion des Segment Extensions SQL

Sur la page **Segment Extensions**, les segments générés par SQL sont indiqués avec <i class="fas fa-code" alt="Segment Extension SQL"></i> à côté de leur nom.

Sélectionnez un Segment Extension SQL pour voir où l’extension est utilisée, archiver l’extension ou [actualiser l’effectif du segment](#refreshing-segment-membership) manuellement.

![Section Utilisation de l’envoi de message de l’éditeur SQL montrant l’emplacement où le segment SQL est utilisé.][3]

### Actualiser l’effectif du segment

Pour actualiser l’effectif au segment de tout Segment Extension créé à l’aide de SQL, ouvrez le Segment Extension et sélectionnez **Refresh (Actualiser)**. Actuellement, les Segment Extensions SQL ne se régénèrent pas automatiquement.

{% alert tip %}
Si vous avez créé un segment duquel vous pensez que les utilisateurs vont entrer et sortir régulièrement, actualisez manuellement le Segment Extension qu’il utilise avant de cibler ce segment dans une campagne ou un Canvas.
{% endalert %}

## Résolution des problèmes

Votre requête peut échouer pour l’une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Le SQL ne respecte pas les règles SQL
- Temporisation du traitement (après 20 minutes)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
