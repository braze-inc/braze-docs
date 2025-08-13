---
nav_title: Générateur de requêtes
article_title: Générateur de requêtes
page_order: 15
description: "Cet article de référence décrit comment créer des rapports à l’aide des données Braze depuis Snowflake dans le générateur de requêtes."
tool: Reports
alias: /query_builder/
---

# Générateur de requêtes

> Le générateur de rapports génère des rapports utilisant les données de Braze dans Snowflake. Le générateur de requêtes est livré avec des [modèles de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) SQL prédéfinis pour vous aider à démarrer, ou vous pouvez écrire vos propres requêtes SQL personnalisées pour obtenir encore plus d'informations.

Le générateur de requêtes permettant d'accéder directement à certaines données clients, vous ne pouvez accéder au générateur de requêtes que si vous disposez de l'[autorisation]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) « Afficher les données d’identification ».

## Exécuter des rapports dans le générateur de rapports

Pour exécuter un rapport du générateur de rapports :

1. Sélectionnez **Analyse** > **Générateur de requêtes**.
2. Sélectionnez **Créer une requête SQL**. Si vous avez besoin d'inspiration ou d'aide pour rédiger votre requête, sélectionnez **Modèle de requête** et choisissez un modèle dans la liste. Sinon, sélectionnez **SQL Editor** pour accéder directement à l'éditeur.
3. Votre rapport reçoit automatiquement un nom avec la date et l’heure actuelles. Survolez le nom et sélectionnez <i class="fas fa-pencil" alt="Edit"></i> pour donner un nom pertinent à votre requête SQL.
4. Rédigez votre requête SQL dans l'éditeur ou [demandez l'aide de l'intelligence artificielle](#ai-query-builder) à partir de l'onglet **AI Query Builder.**  Si vous écrivez votre propre code SQL, consultez la section [Écrire des requêtes SQL personnalisées](#custom-sql) pour connaître les conditions requises et les ressources.
5. Sélectionnez **Exécuter la requête**.
6. Enregistrez votre requête.
7. Pour télécharger un fichier CSV de votre rapport, sélectionnez **Exporter.**

![Générateur de requêtes affichant les résultats de la requête modélisée « Engagement de canal et chiffre d’affaires au cours des 30 derniers jours ».]({% image_buster /assets/img_archive/query_builder.png %})

Les résultats de chaque rapport peuvent être générés une fois par jour. Si vous exécutez le même rapport plus d’une fois pour un jour civil, vous verrez les mêmes résultats dans les deux rapports.

### Modèles de requêtes

Accédez aux modèles de requêtes en sélectionnant **Créer une requête SQL** > **Modèle de requête** lors de la première création d'un rapport.

Pour obtenir une liste des modèles disponibles, voir [Modèles de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/).

### Calendrier des données

Toutes les requêtes portent sur les données des 60 derniers jours.

### Fuseau horaire du générateur de requêtes

Le fuseau horaire par défaut pour interroger notre base de données Snowflake est UTC. Par conséquent, il peut y avoir quelques divergences de données entre votre page d' **engagement du canal e-mail** (qui suit le fuseau horaire de votre entreprise) et les résultats de votre générateur de requêtes.

Pour convertir le fuseau horaire dans les résultats de votre requête, ajoutez le code SQL suivant à votre requête et personnalisez-le en fonction du fuseau horaire de votre entreprise :

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

## Générer des requêtes SQL avec le générateur de requêtes basé sur l’IA

Le générateur de requêtes basé sur l’IA s'appuie sur [GPT](https://openai.com/gpt-4) d’OpenAI afin de recommander le SQL pour votre requête.

![Le générateur de requêtes SQL de l'intelligence artificielle.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

Pour générer des requêtes SQL avec le générateur de requêtes basé sur l’IA :

1. Après avoir créé un rapport dans le générateur de requêtes, sélectionnez l'onglet du **générateur de requêtes basé sur l’IA**.
2. Saisissez votre invite ou sélectionnez un exemple d'invite et sélectionnez **Générer** pour traduire votre invite en SQL.
3. Passez en revue le code SQL généré pour vous assurer qu'il est correct, puis sélectionnez **Insérer dans l'éditeur**.

### Conseils

- Familiarisez-vous avec les [tableaux de données Snowflake]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) disponibles. Si vous demandez des données qui n'existent pas dans ces tableaux, ChatGPT risque de créer un faux tableau.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) pour cette fonctionnalité. Le non-respect de ces règles entraînera une erreur.
- Vous pouvez envoyer jusqu'à 20 invites par minute avec le générateur de requêtes basé sur l’IA.

### Comment mes données sont-elles utilisées et envoyées à OpenAI ?
<!-- Contact Legal for changes. -->

Afin de générer votre requête SQL, Braze enverra vos invites à la plateforme API d'OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans le contenu que vous fournissez. Comme décrit dans les [engagements de la plateforme API d’OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Veuillez vous assurer que vous respectez les politiques d'OpenAI qui vous concernent, y compris la [politique d'utilisation](https://openai.com/policies/usage-policies). Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne tout contenu généré par l'intelligence artificielle. 

## Rédaction de requêtes SQL personnalisées {#custom-sql}

Rédigez votre requête SQL en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference). Consultez la [référence du tableau]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) pour obtenir la liste complète des tableaux et des colonnes pouvant être interrogés.

Pour afficher les détails d'une table dans le générateur de requêtes :

1. Dans la page **Générateur de requête**, ouvrez le panneau **Référence** et sélectionnez **Tables de données** disponibles pour afficher les tables de données disponibles et leurs noms.
3. Sélectionnez <i class="fas fa-chevron-down" alt=""></i> **Voir les détails** pour afficher la description du tableau et des informations sur les colonnes du tableau, telles que les types de données.
4. Pour insérer le nom de la table dans votre SQL, sélectionnez <i class="fas fa-copy" title="Copier le nom de la table dans l&apos;éditeur SQL"></i>.

Pour utiliser des requêtes pré-écrites fournies par Braze, sélectionnez **Modèle de requête** lors de la première création d'un rapport dans le générateur de requêtes.

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

### Remplir automatiquement le nom de la variante de la campagne

Si vous souhaitez que le nom de la variante de la campagne se remplisse automatiquement, incluez le nom de la colonne `MESSAGE_VARIATION_API_ID` dans votre requête, comme dans cet exemple :

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Résolution des problèmes

Votre requête peut échouer pour l’une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Temporisation du traitement (après 6 minutes)
    - Les rapports qui prennent plus de 6 minutes à s’exécuter vont expirer.
    - Si un rapport expire, essayez de limiter la plage de temps pour laquelle vous requêtez les données ou requêtez un ensemble de données plus spécifique.

## Utilisation de variables

Utilisez des variables pour utiliser des types de variables prédéfinis dans SQL afin de référencer des valeurs sans devoir copier manuellement la valeur. Par exemple, au lieu de copier manuellement l'ID d'une campagne dans l'éditeur SQL, vous pouvez utiliser {% raw %}`{{campaign.${My campaign}}}`{% endraw %} pour sélectionner directement une campagne dans une liste déroulante de l'onglet **Variables.** 

Une fois la variable créée, elle apparaît dans l'onglet **Variables** de votre rapport Query Builder. Les avantages de l'utilisation des variables SQL sont les suivants

- Enregistrez-vous en créant une variable de campagne à sélectionner dans une liste lors de la création de votre rapport, au lieu de coller les ID de campagne.
- Échangez des valeurs en ajoutant des variables qui vous permettent de réutiliser le rapport pour des cas d'utilisation légèrement différents à l'avenir (par exemple, un événement personnalisé différent).
- Réduisez les erreurs de l'utilisateur lorsqu'il modifie votre SQL en réduisant la quantité d'édition nécessaire pour chaque rapport. Les collaborateurs qui sont plus à l'aise avec SQL peuvent créer des rapports que les collègues moins techniques peuvent ensuite utiliser.

### Recommandations

Les variables doivent respecter la syntaxe Liquid suivante : {% raw %}`{{ type.${name}}}`{% endraw %}, où `type` doit être l'un des types acceptés et `name` peut être le nom de votre choix. Les étiquettes de ces variables correspondent par défaut au nom de la variable.

Par défaut, toutes les variables sont obligatoires (et votre rapport ne s'exécutera pas si les valeurs des variables ne sont pas sélectionnées), à l'exception de la plage de dates, qui prend par défaut les 30 derniers jours lorsque la valeur n'est pas fournie.

### Types de variables

Les types de variables suivants sont acceptés :

- [Nombre](#number)
- [Plage de dates](#date-range)
- [Messagerie](#messaging)
- [Produits](#products)
- [Événements personnalisés](#custom-events)
- [Propriétés d'événements personnalisés](#custom-event-properties)
- [Espace de travail](#workspace)
- [Catalogues](#catalogs)
- [Champs du catalogue](#catalog-fields)
- [Options](#options)
- [Segments](#segments)
- [Chaîne de caractères](#string)
- [Balises](#tags)

#### Nombre

- **Valeur de remplacement :** La valeur fournie, telle que `5.5`
- **Exemple d'utilisation :** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Plage de dates

Si vous utilisez à la fois `start_date` et `end_date`, ils doivent avoir le même nom pour que vous puissiez les utiliser comme plage de dates.

##### Exemples de valeurs

Le type de plage de dates peut être relatif, date de début, date de fin ou plage de dates.

Les quatre types sont affichés si `start_date` et `end_date` sont utilisés avec le même nom. Si vous n'en utilisez qu'un seul, seuls les types pertinents seront affichés.

| Type de plage de dates | Description | Valeurs requises |
| --- | --- | --- |
| Relative | Spécifie les X derniers jours | Nécessite `start_date` |
| Date de début | Spécifie une date de début | Nécessite `start_date` |
| Date de fin | Spécifie une date de fin | Nécessite `end_date` |
| Plage de dates | Spécifie une date de début et une date de fin | Requiert à la fois `start_date` et `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Valeur de remplacement :** Remplace `start_date` et `end_date` par un horodatage Unix en secondes pour une date spécifiée en UTC, par exemple `1696517353`.
- **Exemple d'utilisation :** Pour toutes les variables relatives, date de début, date de fin et plage de dates :
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Vous pouvez utiliser `start_date` ou `end_date` si vous ne souhaitez pas de plage de dates.

#### Messagerie

Toutes les variables d'envoi de messages doivent partager le même identifiant lorsque vous souhaitez lier leur état dans un seul groupe.

##### Canvas

Pour la sélection d'une toile. Si vous partagez le même nom avec une campagne, un bouton radio apparaîtra dans l'onglet **Variables**, permettant de sélectionner soit Canvas, soit la campagne.

- **Valeur de remplacement :** ID BSON du canvas
- **Exemple d'utilisation :** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Canvas

Pour sélectionner plusieurs toiles. Si vous partagez le même nom avec une campagne, un bouton radio apparaîtra dans l'onglet **Variables** pour sélectionner soit Canvas, soit la campagne.

- **Valeur de remplacement :** ID BSON des canvas
- **Exemple d'utilisation :** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campagne arrêtée

Pour la sélection d'une campagne. Si vous partagez le même nom avec un Canvas, un bouton radio apparaîtra dans l'onglet **Variables**, permettant de sélectionner soit le Canvas, soit la campagne.

- **Valeur de remplacement :** Campagne ID BSON
- **Exemple d'utilisation :** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### Campagnes

Pour les campagnes à sélection multiple. Si vous partagez le même nom avec un Canvas, un bouton radio apparaîtra dans l'onglet **Variables** pour sélectionner soit le Canvas, soit la campagne.

- **Valeur de remplacement :** ID BSON des campagnes
- **Exemple d'utilisation :** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de campagne

Pour sélectionner les variantes de campagne qui appartiennent à la campagne sélectionnée. Elle doit être utilisée en conjonction avec une campagne ou une variable de campagne.

- **Valeur de remplacement :** ID d’API des variantes de campagne, chaînes de caractères délimitées par des virgules, par exemple `api-id1, api-id2`.
- **Exemple d'utilisation :** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes de Canvas

Pour sélectionner les variantes du canvas qui appartiennent à un canevas choisi. Ceci doit être utilisé avec un canvas ou une variante de canvas.

- **Valeur de remplacement :** ID d’API de variantes de canvas, chaînes de caractères délimitées par des virgules comme dans `api-id1, api-id2`.
- **Exemple d'utilisation :** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Étape du canvas

Pour sélectionner une étape du canvas qui appartient à un canvas choisi. Il doit être utilisé avec une variable Canvas.

- **Valeur de remplacement :** ID API de l'étape du canvas
- **Exemple d'utilisation :** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Étapes du canvas

Pour sélectionner les étapes du canvas qui appartiennent aux canvas choisis. Ceci doit être utilisé avec un canvas ou une variante de canvas.

- **Valeur de remplacement :** ID des étapes du canvas dans l'API
- **Exemple d'utilisation :** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}
