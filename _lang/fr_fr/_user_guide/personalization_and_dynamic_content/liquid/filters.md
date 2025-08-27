---
nav_title: Filtres
article_title: Filtres Liquid
page_order: 3
description: "Cette page de référence répertorie les filtres qui peuvent être utilisés pour reformater du contenu statique ou dynamique."

---

# Filtres

> Cet article de référence donne un aperçu des filtres dans Liquid et présente les filtres pris en charge par Braze. Vous recherchez des idées sur la façon d’utiliser ces filtres ? Découvrez notre [bibliothèque de scénarios d'utilisation de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Les filtres vous permettent de modifier la sortie des nombres, des chaînes de caractères, des variables et des objets dans Liquid. Vous pouvez utiliser des filtres pour reformater le texte statique ou dynamique, par exemple, modifier une chaîne de caractères de minuscules en majuscules ou effectuer des opérations mathématiques, comme des additions ou des divisions.

{% alert important %}
Braze ne prend pas en charge tous les filtres Liquid de Shopify. Cette page a pour objectif définir les filtres Liquid que Braze a testés, néanmoins, cette liste peut ne pas être exhaustive. Toujours tester votre Liquid avant d’envoyer des messages. <br><br>Si vous avez des questions sur un filtre qui n'est pas répertorié ici, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Syntaxe du filtre

{% raw %}

Les filtres doivent être placés dans une balise de sortie `{{ }}` et sont indiqués par un caractère pipe `|`.

{% endraw %}

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

Dans cet exemple, `Big Sale` est une chaîne de caractère, et `upcase` est le filtre appliqué.

### Syntaxe pour les filtres multiples

Vous pouvez utiliser plusieurs filtres sur une sortie. Ils sont appliqués de gauche à droite.

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres de tableau

Les filtres de tableau servent à modifier leur sortie.

| Filtre               | Définition                                                                                                         | Pris en charge |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join](https://shopify.dev/api/liquid/filters/array-filters#join)          | Joint les éléments d’un tableau avec le caractère transmis en tant de paramètre. Il en résulte une chaîne de caractères unique.          | ✅  Oui   |
| [first](https://shopify.dev/api/liquid/filters/array-filters#first)         | Renvoie le premier élément d’un tableau. Dans un tableau d’attribut personnalisé, c’est la valeur ajoutée la plus ancienne.                | ✅  Oui   |
| [last](https://shopify.dev/api/liquid/filters/array-filters#last)          | Renvoie le dernier élément d’un tableau. Dans un tableau d’attribut personnalisé, c’est la valeur ajoutée la plus récente.          | ✅  Oui   |
| [compact](https://shopify.dev/api/liquid/filters#compact)       | Enlève tous les éléments `nil` d’un tableau.                                                                             | ✅  Oui   |
| [concat](https://shopify.dev/api/liquid/filters/array-filters#concat)        | Combine un tableau avec un autre tableau.                                                                              | ✅  Oui   |
| [index](https://shopify.dev/api/liquid/filters/array-filters#index)         | Renvoie l’élément à l’emplacement d’index spécifié dans un tableau. Le premier élément d’un tableau est référencé avec `[0]`. | ✅  Oui   |
| [map](https://shopify.dev/api/liquid/filters/array-filters#map)           | Accepte l’attribut d’un élément de tableau comme paramètre et crée un tableau à partir de la valeur de chaque élément du tableau.        | ✅  Oui   |
| [reverse](https://shopify.dev/api/liquid/filters/array-filters#reverse)       | Inverse l’ordre des éléments dans un tableau.                                                                       | ✅  Oui   |
| [size](https://shopify.dev/api/liquid/filters/array-filters#size)          | Renvoie la taille d’une chaîne de caractères (nombre de caractères) ou un tableau (nombre d’éléments).                      | ✅  Oui   |
| [sort](https://shopify.dev/api/liquid/filters/array-filters#sort)         | Trie les éléments d’un tableau par un attribut donné d’un élément dans le tableau.                                    | ✅  Oui   |
| [trier_naturellement](https://shopify.dev/api/liquid/filters#sort_natural) | Trie les éléments d’un tableau selon un ordre alphabétique sensible à la casse.                                                | ✅  Oui   |
| [uniq](https://shopify.dev/api/liquid/filters/array-filters#uniq)         | Supprime les instances en doublon d’éléments dans un tableau.                                                           | ✅  Oui   |
| [where](https://shopify.dev/api/liquid/filters#where)        | Filtre un tableau pour n’afficher que les objets ayant une valeur de propriété spécifique.                                             | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtres de couleur

[Les filtres de couleur](https://shopify.dev/api/liquid/filters/color-filters) ne sont pas pris en charge dans Braze.

## Filtres de polices

[Les filtres de police](https://shopify.dev/api/liquid/filters/font-filters) ne sont pas pris en charge dans Braze.

## Filtres mathématiques

Les filtres mathématiques vous permettent d’effectuer des opérations mathématiques. Si vous utilisez plusieurs filtres sur une même sortie, ils seront appliqués de gauche à droite.

| Filtre  | Définition      | Pris en charge |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/math-filters#abs)        | Renvoie la valeur absolue d’un nombre.     | ✅  Oui   |
| [at_most](https://shopify.dev/api/liquid/filters/math-filters#at_most)    | Limite un nombre à une valeur maximale.   | ✅  Oui   |
| [at_least](https://shopify.dev/api/liquid/filters/math-filters#at_least)   | Limite un nombre à une valeur minimale.   | ✅  Oui   |
| [ceil](https://shopify.dev/api/liquid/filters/math-filters#ceil)       | Arrondit une sortie au nombre entier le plus proche.  | ✅  Oui   |
| [divisé par](https://shopify.dev/api/liquid/filters/math-filters#divided_by) | Divise une sortie par un nombre. La sortie est arrondie au nombre entier le plus proche. Pour évitez l’arrondi, suivez le conseil suivant. | ✅  Oui   |
| [floor](https://shopify.dev/api/liquid/filters/math-filters#floor)      | Arrondit une sortie au nombre entier inférieur le plus proche.        | ✅  Oui   |
| [minus](https://shopify.dev/api/liquid/filters/math-filters#minus)      | Soustrait un nombre à partir d’une sortie.          | ✅  Oui   |
| [plus](https://shopify.dev/api/liquid/filters/math-filters#plus)       | Ajoute un numéro à une sortie.     | ✅  Oui   |
| [round](https://shopify.dev/api/liquid/filters/math-filters#round)      | Arrondit la sortie au nombre entier le plus proche ou au nombre spécifié de décimales.  | ✅  Oui   |
| [times](https://shopify.dev/api/liquid/filters/math-filters#times)     | Multiplie une sortie par un nombre.       | ✅  Oui   |
| [modulo](https://shopify.dev/api/liquid/filters/math-filters#modulo)    | Divise une sortie par un nombre et renvoie le reliquat.   | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Lorsque vous divisez les nombres entiers par des entiers dans Liquid, si la réponse est un float (nombre avec une décimale), Liquid arrondira automatiquement au nombre entier le plus proche. Cependant, la division des nombres entiers par des floats fournit toujours un float. Cela signifie que vous pouvez transformer vos nombres entiers en float (1,0, 2,0, 3,0) pour obtenir un float.
{% raw %}
<br><br>Par exemple, `{{15 | divided_by: 2}}` génère `7`, tandis que `{{15 | divided_by: 2.0}}` génère `7.5`.
{% endraw %}
{% endalert %}

### Opérations mathématiques avec attributs personnalisés

N’oubliez pas que vous ne pouvez pas effectuer d’opérations mathématiques entre deux attributs personnalisés.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Cet exemple ne fonctionnerait pas parce que vous ne pouvez pas référencer plusieurs attributs personnalisés dans une ligne de Liquid. Au lieu de cela, vous devez attribuer une variable à au moins une de ces valeurs avant de réaliser les fonctions mathématiques. L’ajout de deux attributs personnalisés nécessite deux lignes de Liquid :

1. Une pour affecter l’attribut personnalisé à une variable,
2. L’autre pour effectuer l’addition.

#### Cas d’utilisation : Calculer le solde actuel

Supposons que nous voulions calculer le solde actuel d'un utilisateur en additionnant le solde de sa carte cadeau et le solde de ses récompenses.

1. Utilisez l'étiquette `assign` pour remplacer l'attribut personnalisé de `current_rewards_balance` par le terme "balance". Cela signifie que vous avez maintenant une variable intitulée `balance` que vous pouvez manipuler.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2\. Utilisez le filtre `plus` pour combiner le solde de la carte cadeau de chaque utilisateur avec son solde de récompenses, indiqué par l'objet `{{balance}}`.
{% endraw %}
{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres monétaires

Si vous mettez à jour un utilisateur sur son achat, un solde de compte ou tout ce qui concerne une somme d’argent, vous devez utiliser des filtres monétaires. Les filtres monétaires permettent de garantir que vos décimales sont à l’endroit approprié et qu’aucun élément de votre mise à jour n’est perdu (comme ce problème `0` à la fin).

| Filtre         | Définition          | Pris en charge |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money-filters#money)      | Formate les nombres pour s’assurer que les décimales sont à l’endroit approprié et que les zéros ne sont pas supprimés de la fin des nombres.   | ✅  Oui   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money-filters#money_with_currency)    | Formate les nombre avec le symbole de devise.     | ⛔  Non    |
| [argent_sans_monnaie](https://shopify.dev/api/liquid/filters/money-filters#money_without_currency)     | Formate les nombre sans le symbole de devise.      | ⛔  Non    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Pour formater correctement un nombre avec le filtre `money`, supprimez toutes les virgules du nombre et ajoutez le filtre `plus: 0` avant le filtre `money`. Par exemple, voir le Liquid suivant :<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Comparaison du filtre monétaire Shopify avec celui de Braze.

{% alert warning %}
Le comportement du filtre Shopify `money` diffère de la façon dont il est utilisé dans Braze. Consultez les exemples suivants pour obtenir une description précise du comportement attendu.
{% endalert %}

{% raw %}
Si vous saisissez un attribut personnalisé (comme `account_balance`), vous devez toujours utiliser le filtre `money` pour placer les décimales au bon endroit et éviter que des zéros ne tombent à la fin des nombres :

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| AVEC LE FILTRE MONÉTAIRE                       | SANS LE FILTRE MONÉTAIRE                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Avec filtre à argent]({% image_buster /assets/img/with_money_filter.png %})                     | ![Filtre sans argent]({% image_buster /assets/img/without_money_filter.png %})                  |
| Où `account_balance` est une saisie à `17.8`. | Où `account_balance` est une saisie à `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Le filtre `money` de Braze diffère de celui de Shopify car il n'applique pas automatiquement les décimales en fonction d'un paramètre prédéfini. Prenons par exemple le scénario suivant : `rewards_redeemed` contient une valeur de `145` :

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Selon le filtre [money](https://shopify.dev/api/liquid/filters/money-filters#money) de Shopify, cela devrait générer `$1.45`, cependant dans Braze, cela va générer `$145.00`. En tant que solution de contournement, nous pouvons utiliser le filtre `divided_by` pour manipuler le nombre en une décimale, avant d’appliquer le filtre monétaire :

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres de chaîne de caractère

Les filtres de chaîne de caractère sont utilisés pour manipuler les sorties et les variables des chaînes de caractères. Les chaînes de caractères sont une combinaison de caractères alphanumériques et doivent être entourées de guillemets droits.

{% alert note %}
Les guillemets droits sont différents des guillemets courbes dans Liquid. Soyez prudent lorsque vous copiez et collez Liquid depuis un éditeur de texte dans Braze, car les guillemets courbes provoquent des erreurs dans Liquid.. Si vous écrivez votre liquide directement dans Braze, les guillemets droits seront appliqués automatiquement.
{% endalert %}

| Filtre          | Description     | Pris en charge |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/string-filters#append)     | Ajoute des caractères à une chaîne de caractères.           | ✅  Oui   |
| [camelcase](https://shopify.dev/api/liquid/filters/string-filters#camelcase)     | Transforme une chaîne de caractères en CamelCase.             | ⛔  Non    |
| [capitaliser](https://shopify.dev/api/liquid/filters/string-filters#capitalize)     | Met en majuscule le premier mot d'une chaîne et met en minuscule les caractères restants.         | ✅  Oui   |
| [downcase](https://shopify.dev/api/liquid/filters/string-filters#downcase)      | Convertit une chaîne de caractères en minuscules.         | ✅  Oui   |
| [escape](https://shopify.dev/api/liquid/filters/string-filters#escape)    | Échappe une chaîne de caractères.             | ✅  Oui   |
| [handle/handleize](https://shopify.dev/api/liquid/filters/string-filters#handle-handleize)        | Formate une chaîne de caractère en handle.        | ⛔  Non    |
| [md5](https://shopify.dev/api/liquid/filters/string-filters#md5)    | Convertit une chaîne de caractères en hash MD5. Pour plus d'informations, reportez-vous à la section [Filtres d'encodage]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).   | ✅  Oui   |
| [sha1](https://shopify.dev/api/liquid/filters/string-filters#sha1)    | Convertit une chaîne de caractères en hash SHA-1. Pour plus d'informations, reportez-vous à la section [Filtres d'encodage]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).  | ✅  Oui   |
| hmac_sha1_hex<br>(précédemment [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Convertit une chaîne de caractères en hash SHA-1 en utilisant un code d’authentification de message hash (HMAC). Transmet la clé secrète pour le message en tant que paramètre au filtre. Pour plus d'informations, reportez-vous à la section [Filtres d'encodage]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters). | ✅  Oui   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256)    | Convertit une chaîne de caractères en hash SHA-256 en utilisant un code d’authentification de message hash (HMAC). Transmet la clé secrète pour le message en tant que paramètre au filtre.       | ✅  Oui   |
| hmac_sha512 | Convertit une chaîne en un hachage SHA-512 en utilisant un code d'authentification de message de hachage (HMAC). Transmet la clé secrète pour le message en tant que paramètre au filtre. | ✅  Oui  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/string-filters#newline_to_br)     | Insère une balise HTML de saut de ligne `<br>` devant chaque saut de ligne dans une chaîne.        | ✅  Oui   |
| [pluralize](https://shopify.dev/api/liquid/filters/string-filters#pluralize)   | Génère la version au singulier ou au pluriel d’une chaîne de caractères anglaise en fonction de la valeur d’un nombre.      | ⛔  Non    |
| [prepend](https://shopify.dev/api/liquid/filters/string-filters#prepend)     | Ajoute des caractères au début d’une chaîne de caractères.      | ✅  Oui   |
| [supprimer](https://shopify.dev/api/liquid/filters/string-filters#remove)      | Supprime toutes les occurrences d’une sous-chaîne d’une chaîne de caractères.       | ✅  Oui   |
| [remove_first](https://shopify.dev/api/liquid/filters/string-filters#remove_first)    | Supprime uniquement la première occurrence d’une sous-chaîne d’une chaîne de caractères.      | ✅  Oui   |
| [replace](https://shopify.dev/api/liquid/filters/string-filters#replace)        | Remplace toutes les occurrences d’une chaîne de caractères par une sous-chaîne.   | ✅  Oui   |
| [replace_first](https://shopify.dev/api/liquid/filters/string-filters#replace_first)        | Remplace la première occurrence d’une chaîne de caractères par une sous-chaîne.      | ✅  Oui   |
| [slice](https://shopify.dev/api/liquid/filters/string-filters#slice)       | Le filtre de coupe restitue une sous-chaîne, à partir de l’index spécifié.       | ✅  Oui   |
| [split](https://shopify.dev/api/liquid/filters/string-filters#split)  | Le filtre de division prend une sous-chaîne comme paramètre. La sous-chaîne est utilisée comme séparateur pour diviser une chaîne de caractères en tableau.            | ✅  Oui   |
| [strip](https://shopify.dev/api/liquid/filters/string-filters#strip)   | Découpe les tabulations, les espaces et les nouvelles lignes (tous les espaces blancs) à gauche et à droite d’une chaîne de caractères.                                                                                                    | ✅  Oui   |
| [lstrip](https://shopify.dev/api/liquid/filters/string-filters#lstrip)     | Découpe les tabulations, les espaces et les nouvelles lignes (tous les espaces blancs) à gauche d’une chaîne de caractères.    | ⛔  Non    |
| [rstrip](https://shopify.dev/api/liquid/filters/string-filters#rstrip)             | Découpe les tabulations, les espaces et les nouvelles lignes (tous les espaces blancs) à droite d’une chaîne de caractères.          | ⛔  Non    |
| [strip_html](https://shopify.dev/api/liquid/filters/string-filters#strip_html)         | Permet de découper toutes les balises HTML d’une chaîne de caractères.        | ✅  Oui   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/string-filters#strip_newlines)  | Supprime les sauts de ligne/nouvelles lignes d’une chaîne de caractères.        | ✅  Oui   |
| [truncate](https://shopify.dev/api/liquid/filters/string-filters#truncate)    | Tronque une chaîne de caractères en nombre de caractères transmis comme premier paramètre. Une ellipse (…) est ajoutée à la chaîne de caractères tronquée et est incluse dans le nombre de caractères.    | ✅  Oui   |
| [truncatewords](https://shopify.dev/api/liquid/filters/string-filters#truncatewords)   | Tronque une chaîne de caractères en nombre de caractères transmis comme premier paramètre. Une ellipse (…) est ajoutée à la chaîne de caractères tronquée.    | ✅  Oui   |
| [upcase](https://shopify.dev/api/liquid/filters/string-filters#upcase)   | Convertit une chaîne de caractères en majuscules.      | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtres supplémentaires

Les filtres généraux suivants ont de nombreuses fonctions, y compris le formatage ou la conversion de contenu.

| Filtre                | Description                                                                                                                      | Pris en charge |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/additional-filters#date)           | Convertit un horodatage en un autre format de date. Reportez-vous au [Filtre de date](#date-filter) pour plus d'informations.         | ✅  Oui   |
| [default](https://shopify.dev/api/liquid/filters/additional-filters#default)        | Définit une valeur par défaut pour toute variable sans valeur attribuée. Peut être utilisé avec des chaînes de caractères, des tableaux et des hachages.      | ✅  Oui   |
| [format_address](https://shopify.dev/api/liquid/filters/additional-filters#format_address) | Formate une adresse pour imprimer les éléments de l’adresse dans l’ordre selon leur emplacement.        | ⛔  Non    |
| [highlight](https://shopify.dev/api/liquid/filters/additional-filters#highlight)      | Entoure les mots à l’intérieur des résultats de recherche d’une balise HTML `<strong>` avec la classe surlignée si elle correspond aux termes de recherche transmis. | ⛔  Non    |
| `time_zone`             | Reportez-vous à la section [Filtre de fuseau horaire](#time-zone-filter).     | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez trouver plus de filtres pris en charge, tels que les filtres d'encodage et d'URL, sur notre page [Filtres Avancés]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Filtre date {#date-filter}

Le filtre `date` peut servir à convertir un horodatage en un format de date différent. Vous pouvez transmettre des paramètres au filtre `date` pour reformater l’horodatage. Pour obtenir des exemples de ces paramètres, consultez [strfti.me](http://www.strfti.me/).

Par exemple, supposons que la valeur de `date_attribute` est l'horodatage `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

En plus des options de formatage `strftime`, Braze prend également en charge la conversion d’un horodatage en temps Unix avec le filtre de date `%s`. Par exemple, pour obtenir `date_attribute` en temps Unix :

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Filtre fuseau horaire {#time-zone-filter}

{% raw %}
En plus des filtres que vous trouverez dans la documentation de Shopify, Braze prend également en charge le filtre `time_zone`.

Le filtre `time_zone` prend une heure, un fuseau horaire et un format de date et restitue l’heure dans ce fuseau horaire dans le format de date spécifié. Par exemple, supposons que la valeur de `{{custom_attribute.$date_attribute}}}` est `2021-08-04 9:00:00 UTC` :
{% endraw %}

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Vous pouvez également utiliser la variable réservée `now` pour accéder à la date et à l’heure actuelles pour les manipuler.

{% tabs local %}
{% tab Entrée %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab Sortie %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}









