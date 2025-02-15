---
nav_title: Générateur de requêtes
article_title: Générateur de requêtes
page_order: 15
page_type: reference
description: "Cet article de référence décrit comment créer des rapports à l’aide des données Braze depuis Snowflake dans le générateur de requêtes."
tool: Reports
---

# Générateur de requêtes

> Le générateur de rapports génère des rapports utilisant les données de Braze dans Snowflake. Le générateur de requêtes est livré avec des [modèles de requêtes]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/query_templates/) SQL prédéfinis pour vous aider à démarrer, ou vous pouvez écrire vos propres requêtes SQL personnalisées pour obtenir encore plus d'informations.

Le générateur de requêtes permettant d'accéder directement à certaines données clients, vous ne pouvez accéder au générateur de requêtes que si vous disposez de l'[autorisation]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/) « Afficher les données d’identification ».

## Exécuter des rapports dans le générateur de rapports

Pour exécuter un rapport du générateur de rapports :

1. Sélectionnez **Analyse** > **Générateur de requêtes**.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), vous trouverez le **générateur de requêtes** sous **Données**.
{% endalert %}

{:start="2"}
2\. Sélectionnez **Créer une requête SQL**. Si vous avez besoin d'inspiration ou d'aide pour rédiger votre requête, sélectionnez **Modèle de requête** et choisissez un modèle dans la liste. Sinon, sélectionnez **SQL Editor** pour accéder directement à l'éditeur.
3\. Votre rapport reçoit automatiquement un nom avec la date et l’heure actuelles. Survolez le nom et sélectionnez <i class="fas fa-pencil" alt="Edit"></i> pour donner un nom pertinent à votre requête SQL.
4\. Rédigez votre requête SQL dans l'éditeur ou [demandez l'aide de l'intelligence artificielle](#ai-query-builder) à partir de l'onglet **AI Query Builder.** Si vous écrivez votre propre code SQL, consultez la section [Écrire des requêtes SQL personnalisées](#custom-sql) pour connaître les conditions requises et les ressources.
5\. Sélectionnez **Exécuter la requête**.
6\. Enregistrez votre requête.
7\. Pour télécharger un fichier CSV de votre rapport, sélectionnez **Exporter.**

![Générateur de requêtes affichant les résultats de la requête modélisée « Engagement de canal et chiffre d’affaires au cours des 30 derniers jours ».]({% image_buster /assets/img_archive/query_builder.png %})

Les résultats de chaque rapport peuvent être générés une fois par jour. Si vous exécutez le même rapport plus d’une fois pour un jour civil, vous verrez les mêmes résultats dans les deux rapports.

### Modèles de requêtes

Accédez aux modèles de requêtes en sélectionnant **Créer une requête SQL** > **Modèle de requête** lors de la première création d'un rapport.

Pour obtenir une liste des modèles disponibles, voir [Modèles de requêtes]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/query_templates/).

### Calendrier des données

Toutes les requêtes portent sur les données des 60 derniers jours. 

## Générer des requêtes SQL avec le générateur de requêtes basé sur l’IA

Le générateur de requêtes basé sur l’IA s'appuie sur [GPT](https://openai.com/gpt-4) d’OpenAI afin de recommander le SQL pour votre requête.

![][2]{: style="max-width:60%;" }

Pour générer des requêtes SQL avec le générateur de requêtes basé sur l’IA :

1. Après avoir créé un rapport dans le générateur de requêtes, sélectionnez l'onglet du **générateur de requêtes basé sur l’IA**.
2. Saisissez votre invite ou sélectionnez un exemple d'invite et sélectionnez **Générer** pour traduire votre invite en SQL.
3. Passez en revue le code SQL généré pour vous assurer qu'il est correct, puis sélectionnez **Insérer dans l'éditeur**.

### Conseils

- Familiarisez-vous avec les [tableaux de données Snowflake]({{site.baseurl}}/sql_segments_tables/) disponibles. Si vous demandez des données qui n'existent pas dans ces tableaux, ChatGPT risque de créer un faux tableau.
- Familiarisez-vous avec les [règles d'écriture SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) pour cette fonctionnalité. Le non-respect de ces règles entraînera une erreur.
- Vous pouvez envoyer jusqu'à 20 invites par minute avec le générateur de requêtes basé sur l’IA.

### Comment mes données sont-elles utilisées et envoyées à OpenAI ?
<!-- Contact Legal for changes. -->

Afin de générer votre requête SQL, Braze enverra vos invites à la plateforme API d'OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans le contenu que vous fournissez. Comme décrit dans les [engagements de la plateforme API d’OpenAI](https://openai.com/policies/api-data-usage-policies), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer leurs modèles et seront supprimées après 30 jours. Veuillez vous assurer que vous respectez les politiques d'OpenAI qui vous concernent, y compris la [politique d'utilisation](https://openai.com/policies/usage-policies). Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne tout contenu généré par l'intelligence artificielle. 

## Rédaction de requêtes SQL personnalisées {#custom-sql}

Rédigez votre requête SQL en utilisant la [syntaxe Snowflake](https://docs.snowflake.com/en/sql-reference). Consultez la [référence du tableau]({{site.baseurl}}/sql_segments_tables/) pour obtenir la liste complète des tableaux et des colonnes pouvant être interrogés.

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

### Résolution des problèmes

Votre requête peut échouer pour l’une des raisons suivantes :

- Erreurs de syntaxe dans votre requête SQL
- Temporisation du traitement (après 6 minutes)
    - Les rapports qui prennent plus de 6 minutes à s’exécuter vont expirer.
    - Si un rapport expire, essayez de limiter la plage de temps pour laquelle vous requêtez les données ou requêtez un ensemble de données plus spécifique.

## Utilisation de variables

Utilisez des variables pour utiliser des types de variables prédéfinis dans SQL afin de référencer des valeurs sans devoir copier manuellement la valeur. Par exemple, au lieu de copier manuellement l'ID d'une campagne dans l'éditeur SQL, vous pouvez utiliser {% raw %}`{{campaign.${My campaign}}}`{% endraw %} pour sélectionner directement une campagne dans une liste déroulante de l'onglet **Variables.** 

![][3]

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

![][4]{: style="max-width:50%;"}

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

![][5]{: style="max-width:50%;"}

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

##### Étape de canvas

Pour sélectionner une étape du canvas qui appartient à un canvas choisi. Il doit être utilisé avec une variable Canvas.

- **Valeur de remplacement :** ID API de l'étape du canvas
- **Exemple d'utilisation :** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Étapes de Canvas

Pour sélectionner les étapes du canvas qui appartiennent aux canvas choisis. Ceci doit être utilisé avec un canvas ou une variante de canvas.

- **Valeur de remplacement :** ID des étapes du canvas dans l'API
- **Exemple d'utilisation :** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}

#### Produits

Pour sélectionner une liste de noms de produits.

- **Valeur de remplacement :** Les noms de produits sont entourés de guillemets simples et séparés par des virgules, par exemple `product1, product2`
- **Exemple d'utilisation :** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

#### Événements personnalisés

Pour sélectionner une liste d'événements personnalisés.

- **Valeur de remplacement :** Les noms des propriétés d'événements personnalisés sont séparés par des virgules, par exemple `event1, event2`
- **Exemple d'utilisation :** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

#### Propriétés de l'événement  personnalisé

Pour sélectionner une liste de propriétés d'événements personnalisés. Elle doit être utilisée avec la variable des événements personnalisés.

- **Valeur de remplacement :** Les noms des propriétés d'événements personnalisés sont séparés par des virgules, par exemple `property1, property2`
- **Exemple d'utilisation :** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

#### Espace de travail

Pour sélectionner un espace de travail.

- **Valeur de remplacement :** ID BSON de l’espace de travail
- **Exemple d'utilisation :** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

#### Catalogues

Pour la sélection des catalogues.

- **Valeur de remplacement :** Catalogue BSON IDs
- **Exemple d'utilisation :** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

#### Champs du catalogue

Pour la sélection des champs du catalogue. Elle doit être utilisée avec la variable catalogs.

- **Valeur de remplacement :** Noms des champs du catalogue
- **Exemple d'utilisation :** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

#### Options {#options}

Pour faire une sélection dans une liste d'options.

- **Valeur de remplacement :** La valeur des options sélectionnées
- **Exemple d'utilisation :**
    - Pour sélectionner une liste déroulante : {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - `is_multi_select` permet de spécifier si l'utilisateur final peut sélectionner plus d'une option
    - Pour le bouton radio : {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

#### Segments

Pour sélectionner les segments pour lesquels le [suivi des analyses]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/) est activé.

- **Valeur de remplacement :** L'ID de l'analyse du segment, qui correspond aux ID stockés dans la colonne `user_segment_membership_ids` dans les tables où cette colonne est disponible.
- **Exemple d'utilisation :** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

#### Chaîne de caractères

Pour modifier les valeurs des chaînes de caractères répétitives entre les exécutions/un rapports. Utilisez cette variable pour éviter de coder en dur une valeur plusieurs fois dans votre code SQL.

- **Valeur de remplacement :** La chaîne de caractères telle quelle sans les guillemets qui l'entourent
- **Exemple d'utilisation :** {% raw %}`{{string.${some name}}}`{% endraw %}

#### Balises

Pour la sélection des tags pour les campagnes et les toiles.

- **Valeur de remplacement :** Campagnes et toiles avec des ID BSON séparés par des virgules et associés aux tags sélectionnés.
- **Exemple d'utilisation :** {% raw %}`{{tags.${some tags}}}`{% endraw %}

### Métadonnées des variables

Des métadonnées peuvent être attachées à une variable afin de modifier son comportement en ajoutant les métadonnées à l'aide du caractère pipe ( | ) après le nom de la variable. L'ordre des métadonnées n'a pas d'importance et vous pouvez en ajouter autant que vous le souhaitez. En outre, tous les types de métadonnées peuvent être utilisés pour n'importe quelle variable, à l'exception des métadonnées spéciales qui sont spécifiques à certaines variables (cela sera indiqué dans ces cas). L'utilisation de toutes les métadonnées est facultative et permet de modifier le comportement des variables par défaut.

**Exemple d'utilisation :** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

#### Visible

Pour savoir si les variables sont visibles. Toutes les variables sont visibles par défaut dans l'onglet **Variables**, où vous pouvez saisir des valeurs.

Il existe plusieurs variables spéciales dont la valeur dépend d'une autre variable, par exemple si une autre variable a une valeur. Ces variables spéciales sont marquées comme non visibles et n'apparaissent donc pas dans l'onglet **Variables.** 

**Exemple d'utilisation :** `visible: ‘false’`

#### Requis

Pour savoir si les variables sont requises par défaut. Une valeur vide pour une variable entraîne généralement une requête incorrecte.

**Exemple d'utilisation :** `required: ‘false’`

#### Commander

Pour sélectionner la position de la variable dans l'onglet **Variables.** 

**Exemple d'utilisation :** `order: ‘1’`

#### Inclure des guillemets simples

Pour entourer les valeurs d'une variable de guillemets simples.

**Exemple d'utilisation :** `include_quotes: ‘true’`

#### Inclure des guillemets doubles

Pour entourer les valeurs d'une variable avec des guillemets doubles.

**Exemple d'utilisation :** `include_double_quotes: ‘true’`

#### Multi-sélection

Indique si la liste déroulante de sélection permet une sélection unique ou multiple. Pour l'instant, vous ne pouvez inclure ces métadonnées que si vous utilisez la variable [Options.](#options) 

**Exemple d'utilisation :** `is_multi_select: ‘true’`

![][7]{: style="max-width:50%;"}

#### Bouton radio

Pour afficher les options sous forme de boutons radio au lieu d'une liste déroulante dans l'onglet **Variables.**  Vous ne pouvez inclure ces métadonnées que si vous utilisez la variable [Options.](#options)

**Exemple d'utilisation :** `is_radio_button: ‘true’`

![][6]{: style="max-width:50%;"}

#### Options 

Pour fournir la liste des options sélectionnables sous la forme d'une étiquette et d'une valeur. L'étiquette est ce qui est affiché et la valeur est ce par quoi la variable est remplacée lorsque l'option est sélectionnée. Vous ne pouvez inclure ces métadonnées que si vous utilisez la variable [Options.](#options) 

**Exemple d'utilisation :** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

#### Marque substitutive

Pour spécifier le texte marque substitutive affiché dans le champ de saisie de la variable.

**Exemple d'utilisation :** `placeholder: ‘enter some value’`

#### Description

Permet de spécifier le texte de description affiché sous le champ de saisie de la variable.

**Exemple d'utilisation :** `description: ‘some description’`

#### Valeur par défaut

Pour spécifier la valeur par défaut de la variable lorsqu'aucune valeur n'est spécifiée.

**Exemple d'utilisation :** `default_value: ‘5’`

#### Masquer l'étiquette

Pour masquer l'étiquette du nom de la variable. Le nom de la variable est utilisé comme étiquette par défaut.

**Exemple d'utilisation :** `hide_label: ‘true’`

### Variables spéciales

Les variables suivantes peuvent être utilisées avec d'autres variables :

#### Présence ou absence de la valeur d'une autre variable

Pour savoir si la valeur d'une variable est remplie. Ceci est utile pour les variables optionnelles lorsque vous souhaitez court-circuiter une condition si la valeur de la variable n'est pas remplie.

- **Valeur de remplacement :** `true` ou `false` en fonction de la valeur de l'autre variable
- **Exemple d'utilisation :** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` et `name` font référence à la variable référencée. Par exemple, pour court-circuiter la variable facultative {% raw %}`{{campaigns.${messaging}}`, vous pouvez utiliser ce qui suit :
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}

## Temporisation du rapport

Les rapports qui s'exécutent en plus de six minutes sont interrompus. S'il s'agit de la première requête que vous exécutez depuis un certain temps, son traitement peut prendre plus de temps et il y a donc plus de chances qu'elle s'interrompe. Si cela se produit, essayez d’exécuter le rapport à nouveau.

Si un rapport n'aboutit pas ou génère des erreurs même après une nouvelle tentative, contactez le [service d'assistance]({{site.baseurl}}/help/support#braze-support).

## Données et résultats

Les résultats et les exportations de résultats sont des tableaux qui peuvent contenir jusqu'à 1 000 lignes. Pour les rapports qui nécessitent de plus grandes quantités de données, utilisez un autre outil tel que [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) ou les [API d'exportation de]({{site.baseurl}}/api/endpoints/export) Braze.

## Contrôle de l'utilisation du générateur de requêtes

Chaque espace de travail Braze dispose de 5 crédits Snowflake par mois. Une petite partie d'un crédit Snowflake est utilisée chaque fois que vous exécutez une requête ou que vous prévisualisez une table.

{% alert note %}
Les crédits Snowflake ne sont pas partagés entre les fonctionnalités. Par exemple, les crédits des extensions de segments SQL et du générateur de requêtes sont indépendants les uns des autres.
{% endalert %}

L'utilisation des crédits est corrélée à la durée d'exécution de votre requête SQL. Plus la durée d'exécution est longue, plus la part d'un crédit Snowflake que coûtera une requête sera élevée. La durée d'exécution peut varier en fonction de la complexité et de la taille de vos requêtes au fil du temps. Plus vous exécutez des requêtes complexes et fréquentes, plus votre allocation de ressources est importante et plus votre temps d'exécution est court.

Les crédits ne sont pas utilisés lorsque vous rédigez, modifiez ou enregistrez des rapports dans l'éditeur SQL de Braze. Vos crédits seront rétablis à 5 le premier de chaque mois à 12 heures UTC. Vous pouvez suivre l'utilisation de votre crédit mensuel en haut de la page du générateur de requêtes.

![Générateur de requêtes indiquant le montant des crédits utilisés pendant le mois en cours.][1]{: style="max-width:60%;"}

Lorsque vous atteignez le plafond de crédit, vous ne pouvez plus exécuter de requêtes, mais vous pouvez créer, modifier et enregistrer des rapports SQL. Si vous souhaitez acheter plus de crédits pour le gestionnaire de requêtes (Query Builder), veuillez contacter votre gestionnaire de compte.

[1]: {% image_buster /assets/img_archive/query_builder_credits.png %}
[2]: {% image_buster /assets/img_archive/query_builder_ai_tab.png %}
[3]: {% image_buster /assets/img_archive/sql_variables_panel.png %}
[4]: {% image_buster /assets/img_archive/query_builder_time_range.png %}
[5]: {% image_buster /assets/img_archive/sql_variables_canvases.png %}
[6]: {% image_buster /assets/img_archive/sql_variables_campaigns.png %}
[7]: {% image_buster /assets/img_archive/sql_variables_productname.png %}
