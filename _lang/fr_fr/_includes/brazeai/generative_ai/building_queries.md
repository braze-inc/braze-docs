> Apprenez à utiliser le générateur de rapports, afin de pouvoir générer des rapports à partir des données de Braze dans Snowflake. Le générateur de requêtes est livré avec des [modèles de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL prédéfinis pour vous aider à démarrer, ou vous pouvez écrire vos propres requêtes SQL personnalisées pour obtenir encore plus d'informations.

## Conditions préalables

Vous aurez besoin des [ autorisations "Voir les informations confidentielles"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) pour utiliser le générateur de requêtes, car il permet d'accéder directement à certaines données des clients.

## Utilisation du générateur de requêtes

### Étape 1 : Créer une requête SQL

Pour créer une nouvelle requête, accédez à **Analyse/analytique** > **Générateur de requêtes**, puis sélectionnez **Créer une requête SQL**.

![Les options "Modèle de requête" et "Éditeur SQL" se trouvent dans le menu déroulant "Créer une requête SQL".]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Si vous avez besoin d'inspiration ou d'aide pour rédiger votre requête, choisissez **Modèle de requête** et sélectionnez un [modèle préétabli]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/). Pour commencer avec une requête vierge, sélectionnez **Éditeur SQL.**

Votre rapport reçoit automatiquement un nom avec la date et l’heure actuelles. Survolez le nom et sélectionnez <i class="fas fa-pencil" alt="Edit"></i> pour donner un nom pertinent à votre requête SQL.

![Un exemple de rapport intitulé "Channel engagement for May 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Étape 2 : Créez votre requête

Lors de la construction de votre requête, vous pouvez choisir de vous faire aider par l'intelligence artificielle ou de la créer vous-même.

{% tabs local %}
{% tab Utiliser BrazeAI %}
Le générateur de requêtes basé sur l’IA s'appuie sur [GPT](https://openai.com/gpt-4) d’OpenAI afin de recommander le SQL pour votre requête. Pour générer des requêtes SQL avec le générateur de requêtes basé sur l’IA :

1. Après avoir créé un rapport dans le générateur de requêtes, sélectionnez l'onglet du **générateur de requêtes basé sur l’IA**.
2. Saisissez votre invite ou sélectionnez un exemple d'invite et sélectionnez **Générer** pour traduire votre invite en SQL.
3. Passez en revue le code SQL généré pour vous assurer qu'il est correct, puis sélectionnez **Insérer dans l'éditeur**.

![Le générateur de requêtes SQL de l'intelligence artificielle.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Conseils

- Familiarisez-vous avec les [tableaux de données Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Si vous demandez des données qui n'existent pas dans ces tableaux, ChatGPT risque de créer un faux tableau.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) pour cette fonctionnalité. Le non-respect de ces règles entraînera une erreur.
- Vous pouvez envoyer jusqu'à 20 invites par minute avec le générateur de requêtes basé sur l’IA.

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Par moi-même %}
Rédigez votre requête SQL en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference). Consultez la [référence du tableau]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) pour obtenir la liste complète des tableaux et des colonnes pouvant être interrogés.

Pour afficher les détails d'une table dans le générateur de requêtes :

1. Dans la page **Générateur de requête**, ouvrez le panneau **Référence** et sélectionnez **Tables de données** disponibles pour afficher les tables de données disponibles et leurs noms.
3. Sélectionnez <i class="fas fa-chevron-down" alt=""></i> **Voir les détails** pour afficher la description du tableau et des informations sur les colonnes du tableau, telles que les types de données.
4. Pour insérer le nom de la table dans votre SQL, sélectionnez <i class="fas fa-copy" title="Copier le nom de la table dans l&apos;éditeur SQL"></i>.

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

Si vous effectuez une recherche sur `CANVAS_ID`, `CANVAS_VARIATION_API_ID` ou `CAMPAIGN_ID`, les colonnes de noms qui leur sont associées seront automatiquement incluses dans le tableau des résultats. Il n'est pas nécessaire de les inclure dans la requête `SELECT` elle-même.

| Nom de l'ID | Colonne des noms associés |
| --- | --- |
| `CANVAS_ID` | Nom du canvas |
| `CANVAS_VARIATION_API_ID` | Nom de la variante du canvas |
| `CAMPAIGN_ID` | Nom de campagne |
{: .reset-td-br-1 .reset-td-br-2 }

Cette requête permet de récupérer les trois ID et leurs colonnes de noms associées avec un maximum de 100 lignes :

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

#### Résolution des problèmes

Votre requête peut échouer pour l’une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Temporisation du traitement (après 6 minutes)
    - Les rapports qui prennent plus de 6 minutes à s’exécuter vont expirer.
    - Si un rapport expire, essayez de limiter la plage de temps pour laquelle vous requêtez les données ou requêtez un ensemble de données plus spécifique.
{% endtab %}
{% endtabs %}

### Étape 3 : Générer votre rapport

Lorsque vous avez fini de créer votre requête, sélectionnez **Exécuter la requête**. S'il n'y a pas d'erreur ou de [dépassement de délai](#report-timeouts), un fichier CSV sera généré à partir de la requête.

Pour télécharger le rapport CSV, sélectionnez **Exporter**.

![Générateur de requêtes affichant les résultats de la requête modélisée « Engagement de canal et chiffre d’affaires au cours des 30 derniers jours ».]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Chaque rapport ne peut générer des résultats qu'une seule fois par jour. Si vous exécutez le même rapport plusieurs fois au cours d'une même journée calendaire, vous obtiendrez les mêmes résultats dans chaque rapport.
{% endalert %}

## Signaler les dépassements de délai

Les rapports qui s'exécutent en plus de six minutes sont interrompus. S'il s'agit de la première requête que vous exécutez depuis un certain temps, son traitement peut prendre plus de temps et il y a donc plus de chances qu'elle s'interrompe. Si cela se produit, essayez d’exécuter le rapport à nouveau.

Si, après plusieurs tentatives, votre rapport n'aboutit toujours pas, [contactez le service d'assistance.]({{site.baseurl}}/help/support#braze-support)

## Données et résultats

Toutes les requêtes portent sur les données des 60 derniers jours. Lorsque vous exportez vos résultats, ils ne contiennent pas plus de 1 000 lignes. Pour les rapports qui nécessitent de plus grandes quantités de données, vous pouvez utiliser des outils tels que [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) ou l'[endpoint API d'exportation.]({{site.baseurl}}/api/endpoints/export)

## Crédits Snowflake

Chaque entreprise dispose de 5 crédits Snowflake par mois, partagés entre tous les espaces de travail. Une petite partie d'un crédit Snowflake est utilisée chaque fois que vous exécutez une requête ou que vous prévisualisez une table.

{% alert note %}
Les crédits Snowflake ne sont pas partagés entre les fonctionnalités. Par exemple, les crédits des extensions de segments SQL et du générateur de requêtes sont indépendants les uns des autres.
{% endalert %}

L'utilisation des crédits est corrélée à la durée d'exécution de votre requête SQL. Plus la durée d'exécution est longue, plus la part d'un crédit Snowflake que coûtera une requête sera élevée. La durée d'exécution peut varier en fonction de la complexité et de la taille de vos requêtes au fil du temps. Plus vous exécutez des requêtes complexes et fréquentes, plus votre allocation de ressources est importante et plus votre temps d'exécution est court.

Les crédits ne sont pas utilisés lorsque vous rédigez, modifiez ou enregistrez des rapports dans l'éditeur SQL de Braze. Vos crédits seront rétablis à 5 le premier de chaque mois à 12 heures UTC. Vous pouvez suivre l'utilisation de votre crédit mensuel en haut de la page du générateur de requêtes.

![Générateur de requêtes indiquant le montant des crédits utilisés pendant le mois en cours.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Lorsque vous atteignez le plafond de crédit, vous ne pouvez plus exécuter de requêtes, mais vous pouvez créer, modifier et enregistrer des rapports SQL. Si vous souhaitez acheter plus de crédits pour le gestionnaire de requêtes (Query Builder), veuillez contacter votre gestionnaire de compte.
