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

> Vous pouvez générer une extension de segmentation à l'aide de requêtes SQL de données [Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/). Le SQL peut vous aider à déverrouiller de nouveaux cas d’utilisation de segments parce qu’il offre la flexibilité nécessaire pour décrire les relations entre les données de manières qui ne sont pas réalisables par d’autres fonctionnalités de segmentation.

À l'instar des extensions de segments standard, vous pouvez interroger les événements des deux dernières années (730 jours) dans votre extension de segment SQL.

## Types d'extensions de segments SQL

Vous avez le choix entre deux types d'éditeurs SQL lors de la création de votre extension de segment SQL : l'éditeur SQL et l'éditeur SQL incrémentiel.

- **Création d'extensions avec l'éditeur SQL (actualisation complète) :** À chaque fois que votre segment est actualisé, Braze interroge toutes les données disponibles pour mettre à jour votre segment, ce qui utilise plus de crédits que les actualisations incrémentielles. Les extensions à actualisation complète peuvent régénérer automatiquement l’adhésion tous les jours, mais ne peuvent pas être actualisées à l'aide de l'actualisation incrémentielle.
- **Création d'extensions avec l'éditeur SQL incrémental (actualisation incrémentale) :** L'actualisation incrémentale ne calcule que les données des deux derniers jours, ce qui est plus économique et consomme moins de crédits à chaque fois. Lorsque vous créez un segment SQL à actualisation incrémentielle, vous pouvez le configurer pour qu'il régénère automatiquement l'adhésion tous les jours. <br><br>Le principal avantage des extensions avec actualisation incrémentielle est que vous pouvez configurer votre segmentation pour qu'elle actualise automatiquement l'adhésion tous les jours. Dans le cas des segments créés avec notre éditeur SQL habituel, l’adhésion ne peut être actualisée que manuellement. Cela permet de réduire le coût d'une actualisation quotidienne des données pour les extensions de segments SQL.

{% alert tip %}
Vous pouvez effectuer une actualisation complète manuelle sur tous les segments SQL créés dans l'un ou l'autre des éditeurs SQL.
{% endalert %}

## Création d'extensions de segments SQL

{% tabs local %}
{% tab Actualisation complète %}

Pour créer une extension de segments SQL entièrement actualisée :

1. Sélectionnez **Audience** > **Extensions de segments**.
2. Cliquez sur **Créer une nouvelle extension** et sélectionnez **Actualiser complètement**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Ajoutez un nom pour votre Segment Extension et saisissez votre SQL. Pour connaître les exigences et les ressources, reportez-vous à la section [Écriture de code SQL](#writing-sql).<br><br>
   ![Éditeur SQL montrant un exemple d'extension de segmentation SQL.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Enregistrer votre Segment Extension.

{% endtab %}
{% tab Actualisation incrémentielle %}

L'éditeur SQL d'actualisation incrémentale permet à l'utilisateur d'effectuer des requêtes agrégées par date pour un événement situé dans un laps de temps donné. Pour créer une extension de segment SQL à actualisation incrémentielle :

1. Sélectionnez **Audience** > **Extensions de segments**.
{% alert note %}

Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), vous trouverez cette page sous **Engagement** > **Segments** > **Extensions de segments**.
{% endalert %}

{:start="2"}
2\. Cliquez sur **Créer une nouvelle extension** et sélectionnez **Actualisation incrémentielle**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3\. Ajoutez un nom pour votre Segment Extension et saisissez votre SQL. Pour connaître les exigences et les ressources, reportez-vous à la section [Écriture de code SQL](#writing-sql).<br><br>
   ![Éditeur SQL montrant un exemple d'extension de segments SQL à actualisation incrémentielle.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4\. Si vous le souhaitez, sélectionnez **Regénérer l'extension quotidiennement**.<br><br>
   ![Case à cocher pour regénérer l'extension quotidiennement.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Lorsque cette option est sélectionnée, Braze met automatiquement à jour la segmentation chaque jour. Cela signifie que chaque jour à minuit dans le fuseau horaire de votre entreprise (avec un retard potentiel d'une heure), Braze vérifiera s'il y a de nouveaux utilisateurs dans votre segmentation et les ajoutera automatiquement à votre segmentation. Si une extension de segment n'a pas été utilisée depuis 7 jours, Braze interrompt automatiquement la regénération quotidienne. Une extension de segments inutilisée est une extension qui ne fait pas partie d'une campagne ou d'un Canvas (la campagne ou le Canvas n'a pas besoin d'être actif pour que l'extension soit considérée comme "utilisée").<br><br>
5\. Enregistrer votre Segment Extension.

{% endtab %}

{% tab Générateur de SQL pour l'intelligence artificielle %}

{% alert note %}
Le générateur SQL basé sur l’IA est actuellement disponible en tant que fonctionnalité bêta. Si vous souhaitez participer à cet essai bêta, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

Le générateur SQL basé sur l’IA s'appuie sur [GPT](https://openai.com/gpt-4) d’OpenAI pour recommander du code SQL pour votre segment SQL.

![Générateur SQL basé sur l’IA, avec l'invite « Utilisateurs ayant reçu une notification au cours du mois passé »]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Pour utiliser le générateur SQL basé sur l’IA, procédez comme suit :

1. Cliquez sur **Lancer le générateur SQL de l'intelligence artificielle** après avoir créé un [segment SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) à l'aide d'une actualisation complète ou incrémentielle.
2. Saisissez votre invite et cliquez sur **Générer** pour traduire votre invite en code SQL.
3. Passez en revue le code SQL généré pour vous assurer qu'il est correct, puis enregistrez votre segment.

### Exemples d'invites
- Utilisateurs ayant reçu un e-mail au cours du dernier mois
- Utilisateurs ayant effectué moins de cinq achats au cours de l'année écoulée

### Conseils
- Familiarisez-vous avec les [tableaux de données Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Si vous demandez des données qui n'existent pas dans ces tableaux, ChatGPT risque de créer un faux tableau.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) pour cette fonctionnalité. Le non-respect de ces règles entraînera une erreur. Par exemple, votre code SQL doit sélectionner la colonne `user_id`. Il peut être utile de commencer votre invite par « Utilisateurs qui ».
- Vous pouvez envoyer jusqu'à 20 invites par minute avec le générateur SQL basé sur l’IA.

### Comment mes données sont-elles utilisées et envoyées à OpenAI ?

Afin de générer votre requête SQL, Braze enverra vos invites à la plateforme API d'OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans le contenu que vous fournissez. Comme décrit dans les [engagements de la plateforme API d’OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Veuillez vous assurer que vous respectez les politiques d'OpenAI qui vous concernent, y compris la [politique d'utilisation](https://openai.com/policies/usage-policies). Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne tout contenu généré par l'intelligence artificielle.
{% endtab %}
{% endtabs %}

{% alert note %}
Les requêtes SQL qui prennent plus de 20 minutes à s’exécuter vont expirer.
{% endalert %}

Lorsque le traitement de l'extension est terminé, vous pouvez [créer un segment][4] à l'aide de votre extension de segment et cibler ce nouveau segment avec vos campagnes et vos Canvases.

## Requêtes SQL

Votre requête SQL doit être écrite en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference.html). Consultez la [référence du tableau]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) pour obtenir la liste complète des tableaux et des colonnes pouvant être interrogés.

{% alert important %}
Notez que les tables disponibles pour l'interrogation ne contiennent que des données sur les événements. Si vous souhaitez interroger les attributs de l'utilisateur, vous devez combiner votre segment SQL avec les filtres d'attributs personnalisés du [segmenteur classique]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
{% endalert %} 

{% tabs %}
{% tab Éditeur SQL %}

Votre SQL doit de surcroit respecter les règles suivantes :

- Rédigez une seule instruction SQL. N’ajoutez pas de points-virgules.
- Votre SQL ne doit sélectionner qu’une seule colonne : la colonne `user_id`. Cela signifie que votre SQL doit contenir :

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Il n'est pas possible d'interroger les utilisateurs n'ayant participé à aucun événement, ce qui signifie que toute interrogation portant sur des utilisateurs ayant participé à un événement moins de X fois devra suivre cette solution de contournement :
   1. Ecrivez une requête pour sélectionner les utilisateurs qui ont l'événement PLUS de X fois.
   2. Lorsque vous faites référence à votre extension de segment dans votre segment, sélectionnez `doesn't include` pour inverser le résultat.

{% endtab %}
{% tab Éditeur SQL incrémental %}

Toutes les requêtes d'actualisation incrémentale se composent de deux parties : une requête et les détails du schéma.

1. Dans l'éditeur, écrivez une requête qui sélectionne les `user_id` dans la table de votre choix.
2. Ajoutez des détails sur le schéma en sélectionnant un **opérateur**, un **nombre de fois** et une **période de temps** dans les champs situés au-dessus de l'éditeur. La requête vérifiera si la somme de la colonne agrégée remplit une certaine condition spécifiée par les marqueurs substitutifs {% raw %}`{{operator}}` et `{{number of times}}`{% endraw %}. Le fonctionnement est similaire à celui du processus de création des extensions de segments classiques.<br><br>
   - **Opérateur :** Indiquez si l'événement s'est produit plus de fois, moins de fois ou autant de fois qu’un nombre d'occurrences donné.<br>
   ![Champ opérateur avec "Plus de" sélectionné.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Nombre de fois :** Combien de fois souhaitez-vous évaluer l'événement par rapport à l'opérateur.<br>
   ![Nombre de fois où "5" a été saisi.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Période :** Nombre de jours, de 1 à 730, pendant lesquels vous souhaitez vérifier les instances de l'événement. Cette période se réfère aux jours passés par rapport au jour actuel. L'exemple suivant présente une requête pour les utilisateurs qui ont effectué l'événement plus de 5 fois au cours des 365 derniers jours.<br>
   ![Champ de la période de temps avec "365" saisi.]({% image_buster /assets/img_archive/sql_segments_period.png %})

Dans l'exemple suivant, le segment obtenu contiendra les utilisateurs qui ont effectué l'événement `favorited` plus de 3 fois au cours des 30 derniers jours, après une date spécifiée.

![Éditeur SQL montrant un exemple d'extension de segments SQL à actualisation incrémentielle.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![Aperçu SQL d'une extension de segment SQL à actualisation incrémentielle.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

### Règles supplémentaires

Votre requête d'actualisation incrémentielle doit en outre respecter les règles suivantes :

- Rédigez une seule instruction SQL. N’ajoutez pas de points-virgules.
- Votre segment SQL à actualisation incrémentielle ne pourrait se référer qu'à un seul événement. Vos listes déroulantes pour la date et le nombre font référence à l'événement que vous avez choisi.
- Votre code SQL doit comporter les colonnes suivantes : `user_id`, `$start_date` et une fonction d'agrégation (telle que `COUNT`). Tout SQL enregistré sans ces trois champs entraînera une erreur.

{% alert tip %}
Les segments à actualisation incrémentielle prennent en compte les événements tardifs, c'est-à-dire les événements survenus il y a plus de 2 jours (par exemple, les événements SDK qui n'étaient pas envoyés au moment où ils ont été capturés).
{% endalert %}

{% endtab %}
{% endtabs %}

## Aperçu des résultats

Avant d’enregistrer, vous pouvez exécuter un aperçu de votre requête. Les aperçus de vos requêtes sont automatiquement limités à 100 lignes et expireront au bout de 60 secondes. L’exigence de la colonne `user_id` ne s’applique pas lors de l’exécution d’un aperçu.

Pour les extensions de segments SQL incrémentielles, l'aperçu n'inclura pas les critères supplémentaires de votre opérateur, le nombre de fois et les champs de la période.

## Gestion des Segment Extensions SQL

Sur la page **Extensions de segments**, les segments générés à l'aide de SQL sont signalés par <i class="fas fa-code" alt="SQL Segment Extension"></i> à côté de leur nom.

Sélectionnez une extension de segment SQL pour voir où l'extension est utilisée, archiver l'extension ou [actualiser manuellement l’appartenance à un segment](#refreshing-segment-membership).

![Section Utilisation des messages de l'éditeur SQL montrant où le segment de message est utilisé.][3]

### Actualiser l’effectif du segment

Pour actualiser la composition des segments d'une extension de segment créée à l'aide de SQL, ouvrez l'extension de segment et sélectionnez **Actualiser**. Seule l'actualisation incrémentielle des extensions de segments SQL peut se régénérer automatiquement (si elle est sélectionnée).

{% alert tip %}
Si vous avez créé un segment duquel vous pensez que les utilisateurs vont entrer et sortir régulièrement, actualisez manuellement le Segment Extension qu’il utilise avant de cibler ce segment dans une campagne ou un Canvas.
{% endalert %}

## Contrôle de l'utilisation de vos segments SQL

Chaque espace de travail Braze dispose de 5 crédits Snowflake par mois. Si vous avez besoin de plus de crédits, contactez votre gestionnaire de compte. Les crédits sont utilisés chaque fois que vous actualisez, ou enregistrez et actualisez, l'adhésion à un segment SQL. Les crédits ne sont pas utilisés lorsque vous exécutez des aperçus dans un segment SQL ou lorsque vous enregistrez ou actualisez une extension de segment classique.

{% alert note %}
Les crédits Snowflake ne sont pas partagés entre les fonctionnalités. Par exemple, les crédits des extensions de segments SQL et du générateur de requêtes sont indépendants les uns des autres.
{% endalert %}

L'utilisation des crédits est corrélée à la durée d'exécution de votre requête SQL. Plus la durée d'exécution est longue, plus une requête coûtera de crédits. La durée d'exécution peut varier en fonction de la complexité et de la taille de vos requêtes au fil du temps. Plus vous exécutez des requêtes complexes et fréquentes, plus votre allocation de ressources est importante et plus votre temps d'exécution est court.

Pour économiser des crédits, affichez un aperçu de votre requête pour vous assurer qu'elle est correcte avant d'enregistrer l'extension de segment SQL.

Vos crédits seront rétablis à 5 le premier de chaque mois à 12 heures UTC. Vous pouvez suivre l'utilisation de votre crédit tout au long du mois dans le panneau d'utilisation des crédits. Dans la page **Extensions de segments**, cliquez sur <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage.**

![Panneau Utilisation des crédits SQL dans la page Extensions de segments SQL][5]{: style="max-width:60%"}

Lorsque vos crédits atteignent zéro, il se produit ce qui suit :

- Toutes les extensions de segments SQL configurées pour s'actualiser automatiquement cessent de s'actualiser, ce qui a un impact sur l'appartenance à ces segments et sur toutes les campagnes ou les canevas qui ciblent ces segments.
- Vous ne pouvez enregistrer les nouvelles extensions de segments SQL en tant que brouillons que jusqu'à la fin du mois.

Tous les utilisateurs de l'entreprise qui ont créé un segment SQL et les administrateurs de votre entreprise recevront un e-mail de notification lorsque vous aurez utilisé 50 %, 80 % et 100 % de vos crédits. Après la réinitialisation de vos crédits au début du mois suivant, vous pouvez créer d'autres segments SQL, et les actualisations automatiques reprendront.

Si vous souhaitez acheter plus de crédits de segments SQL ou des extensions de segments supplémentaires, veuillez contacter votre gestionnaire de compte.

## Résolution des problèmes

Votre requête peut échouer pour l’une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- SQL ne respecte pas les [règles SQL](#writing-sql)
- Temporisation du traitement (après 20 minutes)

[1]: {% image_buster /assets/img_archive/sql_segments_create.png %}
[2]: {% image_buster /assets/img_archive/sql_segments_editor.png %}
[3]: {% image_buster /assets/img_archive/sql_segments_usage.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment
[5]: {% image_buster /assets/img_archive/sql_segments_credits.png %}
[6]: {% image_buster /assets/img/ai_sql_generator.png %}
