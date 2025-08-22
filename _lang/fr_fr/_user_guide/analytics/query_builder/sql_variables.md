---
nav_title: Variables SQL
article_title: Variables SQL du générateur de requêtes
page_order: 2
page_type: reference
description: "Apprenez à utiliser les variables dans le générateur de requêtes, afin de pouvoir réutiliser vos requêtes et d'éviter de coder en dur des données dans votre code."
tool: Reports
---

# Variables SQL du générateur de requêtes

> Apprenez à utiliser les variables SQL dans le générateur de requêtes, afin de pouvoir réutiliser vos requêtes et d'éviter de coder en dur des données dans votre code.

## Pourquoi utiliser des variables SQL ?

Les avantages de l'utilisation des variables SQL sont les suivants

- Enregistrez-vous en créant une variable de campagne à sélectionner dans une liste lors de la création de votre rapport, au lieu de coller les ID de campagne.
- Échangez des valeurs en ajoutant des variables qui vous permettent de réutiliser le rapport pour des cas d'utilisation légèrement différents à l'avenir (par exemple, un événement personnalisé différent).
- Réduisez les erreurs de l'utilisateur lorsqu'il modifie votre SQL en réduisant la quantité d'édition nécessaire pour chaque rapport. Les collaborateurs qui sont plus à l'aise avec SQL peuvent créer des rapports que les collègues moins techniques peuvent ensuite utiliser.

## Utilisation de variables

### Étape 1 : Ajouter une variable

Pour ajouter une variable à votre requête, utilisez la syntaxe suivante :

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Remplacez les éléments suivants :

| Marque substitutive      | Description                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | Le type de variable prédéfinie que vous souhaitez utiliser, par exemple `campaign` ou `catalog_fields`. Pour obtenir la liste complète, consultez la section [Types de variables pris en charge.](#variable-types) |
| `custom_label` | L'étiquette utilisée pour identifier la variable dans l'onglet **Variables** de votre générateur de requêtes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Dans l'exemple suivant, le nombre total d'utilisateurs entre le premier et le dernier jour d'un mois est interrogé pour une campagne. Une valeur sera attribuée à chaque variable à l'étape suivante.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Étape 2 : Attribuer une valeur

Par défaut, l'onglet **Variables** n'est pas affiché dans le générateur de requêtes. Il n'apparaît qu'après avoir ajouté votre première variable à la requête. Vous pourrez alors lui attribuer une valeur. Les valeurs spécifiques que vous pouvez choisir dépendent du [type de](#variable-types) cette variable.

Dans l'exemple suivant, la campagne "Lancement de la fonctionnalité d'été" est attribuée comme valeur, ainsi que le premier et le dernier jour du mois de juin 2025.

![L'onglet "Variable" du générateur de requêtes illustre l'exemple donné.]({% image_buster /assets/img/query_builder_example.png %})

## Types de variables générales {#variable-types}

### Nombre

`number` peut être utilisée en combinaison avec d'autres variables autres que des chaînes de caractères. Accepte tout nombre positif ou négatif, y compris les nombres décimaux, tels que `5.5`.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Chaîne de caractères

Pour modifier les valeurs des chaînes de caractères répétitives entre les exécutions/un rapports. Utilisez cette variable pour éviter de coder en dur une valeur plusieurs fois dans votre code SQL.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Liste {#list}

Pour faire une sélection dans une liste d'options.

{% tabs local %}
{% tab choisissez-en un %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab choisir plusieurs %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Bouton radio

Pour afficher les options sous forme de boutons radio au lieu d'une liste déroulante dans l'onglet **Variables.**  Il ne peut pas être utilisé seul, mais doit être associé à une [liste](#list).

{% tabs %}
{% tab utilisation %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Exemple de bouton radio rendu en Braze.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Multi-sélection

Indique si la liste déroulante de sélection permet une sélection unique ou multiple. Il ne peut pas être utilisé seul, mais doit être associé à une [liste](#list).

{% tabs %}
{% tab utilisation %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Exemple de liste multi-sélection rendue en Braze.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Options 

Pour fournir la liste des options sélectionnables sous la forme d'une étiquette et d'une valeur. L'étiquette est ce qui est affiché et la valeur est ce par quoi la variable est remplacée lorsque l'option est sélectionnée. Il ne peut pas être utilisé seul, mais doit être associé à une [liste](#list).

{% tabs %}
{% tab utilisation %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Types de variables spécifiques au Braze

### Plage de dates

Pour afficher un calendrier dans lequel vous pouvez sélectionner des dates. Remplacez `start_date` et `end_date` par un horodatage Unix en secondes pour une date spécifiée en UTC, tel que `1696517353`. En option, vous pouvez définir uniquement une `start_date` ou une `end_date` pour n'afficher qu'une seule date dans le calendrier. Si les libellés de vos `start_date` et `end_date` ne correspondent pas, ils seront traités comme deux dates distinctes et non comme une fourchette de dates.

{% tabs %}
{% tab utilisation %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Vous pouvez choisir l'une des options suivantes pour la plage de dates. Si les deux `start_date` et `end_date` sont utilisés et partagent la même étiquette, toutes les options seront affichées. Sinon, si une seule option est utilisée, seule l'option spécifiée sera affichée.

| Option | Description | Valeurs requises |
| --- | --- | --- |
| Relative | Spécifie les X derniers jours | Nécessite `start_date` |
| Date de début | Spécifie une date de début | Nécessite `start_date` |
| Date de fin | Spécifie une date de fin | Nécessite `end_date` |
| Plage de dates | Spécifie une date de début et une date de fin | Requiert à la fois `start_date` et `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Votre liquid sera utilisé pour afficher un calendrier dans la plage de dates donnée :

![Exemple de calendrier réalisé en Braze.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campagnes

{% tabs local %}
{% tab une campagne %}
Pour la sélection d'une campagne. Si vous partagez la même étiquette avec un Canvas, un bouton radio apparaîtra dans l'onglet **Variables**, permettant de sélectionner soit le Canvas, soit la campagne.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campagnes multiples %}
Pour les campagnes à sélection multiple. Si vous partagez la même étiquette avec un Canvas, un bouton radio apparaîtra dans l'onglet **Variables** pour sélectionner soit le Canvas, soit la campagne.

- **Valeur de remplacement :** ID BSON des campagnes

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variante de campagne %}
Pour sélectionner les variantes de campagne qui appartiennent à la campagne sélectionnée. Elle doit être utilisée en conjonction avec une campagne ou une variable de campagne.

- **Valeur de remplacement :** ID d’API des variantes de campagne, chaînes de caractères délimitées par des virgules, par exemple `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Toutes les variables de campagne et de Canvas doivent utiliser les mêmes identifiants afin de synchroniser les états au sein d'un même groupe.
{% endalert %}

### Canvas

{% tabs local %}
{% tab une toile %}
Pour la sélection d'une toile. Si vous partagez le même label avec une campagne, un bouton radio apparaîtra dans l'onglet **Variables**, permettant de sélectionner soit Canvas, soit campagne.

- **Valeur de remplacement :** ID BSON du canvas

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab plusieurs toiles %}
Pour sélectionner plusieurs toiles. Si vous partagez le même label avec une campagne, un bouton radio apparaîtra dans l'onglet **Variables** pour sélectionner soit Canvas, soit campagne.

- **Valeur de remplacement :** ID BSON des canvas

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab variante du canvas %}
Pour sélectionner les variantes du canvas qui appartiennent à un canevas choisi. Ceci doit être utilisé avec un canvas ou une variante de canvas. Définissez un ou plusieurs ID API de variantes de Canvas, sous la forme d'une chaîne de caractères séparés par des virgules, comme dans `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab une étape du canvas %}
Pour sélectionner une étape du canvas qui appartient à un canvas choisi. Il doit être utilisé avec une variable Canvas.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab plusieurs étapes du canvas %}
Pour sélectionner les étapes du canvas qui appartiennent aux canvas choisis. Ceci doit être utilisé avec un canvas ou une variante de canvas.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Toutes les variables de campagne et de Canvas doivent utiliser les mêmes identifiants afin de synchroniser les états au sein d'un même groupe.
{% endalert %}

### Produits

`products` permet de sélectionner un ou plusieurs produits dans le tableau de bord de Braze.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab exemple %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Événements personnalisés

Sélectionnez un ou plusieurs événements personnalisés ou propriétés d'événement personnalisé dans une liste.

{% tabs local %}
{% tab événement %}
`custom_events` permet de sélectionner un ou plusieurs événements personnalisés dans le tableau de bord de Braze.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab example %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name = '{{custom_events.${Purchased Game}}}';
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab propriétés %}
`custom_event_properties` est utilisée pour sélectionner une ou plusieurs propriétés de l'événement personnalisé en cours de sélection.  Nécessite un ensemble de variables `custom_events`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Espace de travail

`workspace` permet de sélectionner un seul espace de travail dans le tableau de bord de Braze.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Catalogues

Sélectionnez un ou plusieurs catologs ou champs de catologs dans une liste.

{% tabs local %}
{% tab catologues %}
`catalogs` permet de sélectionner un ou plusieurs catologues dans le tableau de bord de Braze.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab champs catologiques %}
`catalog_fields` est utilisé pour définir un ou plusieurs champs du catalogue actuellement sélectionné. Nécessite un ensemble de variables `catalogs`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segments

Pour sélectionner les segments pour lesquels le [suivi des analyses]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) est activé. Indiquez l'ID de l'analyse/analytique du segment, qui correspond aux ID stockés dans la colonne `user_segment_membership_ids` dans les tables où cette colonne est disponible.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Balises

Pour la sélection des tags pour les campagnes et les toiles. Définissez les campagnes et les toiles avec des ID BSON séparés par des virgules et associés aux tags sélectionnés.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Métadonnées des variables

Des métadonnées peuvent être attachées à une variable afin de modifier son comportement en ajoutant les métadonnées à l'aide du caractère pipe ( | ) qui suit l'étiquette de la variable. L'ordre des métadonnées n'a pas d'importance et vous pouvez en ajouter autant que vous le souhaitez. En outre, tous les types de métadonnées peuvent être utilisés pour n'importe quelle variable, à l'exception des métadonnées spéciales qui sont spécifiques à certaines variables (cela sera indiqué dans ces cas). L'utilisation de toutes les métadonnées est facultative et permet de modifier le comportement des variables par défaut.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Valeur booléenne

Pour savoir si la valeur d'une variable est remplie. Ceci est utile pour les variables optionnelles lorsque vous souhaitez court-circuiter une condition si la valeur de la variable n'est pas remplie. Peut prendre la valeur `true` ou `false` en fonction de la valeur de l'autre variable.

{% tabs %}
{% tab utilisation %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` et `name` font référence à la variable référencée. Par exemple, pour court-circuiter la variable facultative suivante : {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Visible

Pour savoir si les variables sont visibles. Toutes les variables sont visibles par défaut dans l'onglet **Variables**, où vous pouvez saisir des valeurs.

Il existe plusieurs variables spéciales dont la valeur dépend d'une autre variable, par exemple si une autre variable a une valeur. Ces variables spéciales sont marquées comme non visibles et n'apparaissent donc pas dans l'onglet **Variables.** 

{% tabs %}
{% tab utilisation %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Requis

Pour savoir si les variables sont requises par défaut. Une valeur vide pour une variable entraîne généralement une requête incorrecte.

{% tabs %}
{% tab utilisation %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Commander

Pour sélectionner la position de la variable dans l'onglet **Variables.** 

{% tabs %}
{% tab utilisation %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Inclure les devis

{% tabs local %}
{% tab guillemets simples %}
Pour entourer les valeurs d'une variable de guillemets simples.

{% subtabs %}
{% subtab usage %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab guillemets doubles %}
Pour entourer les valeurs d'une variable avec des guillemets doubles.

{% subtabs %}
{% subtab usage %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Marque substitutive

Pour spécifier le texte marque substitutive affiché dans le champ de saisie de la variable.

{% tabs %}
{% tab utilisation %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Description

Pour spécifier le texte de description affiché sous le champ de saisie de la variable.

{% tabs %}
{% tab utilisation %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Valeur par défaut

Pour spécifier la valeur par défaut de la variable lorsqu'aucune valeur n'est spécifiée.

{% tabs %}
{% tab utilisation %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Masquer l'étiquette

Pour masquer l'étiquette de la variable.

{% tabs %}
{% tab utilisation %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}
