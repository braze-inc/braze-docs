---
nav_title: Filtres
article_title: Filtres Liquid
page_order: 3
description: "Cette page de référence répertorie les filtres qui peuvent être utilisés pour reformater du contenu statique ou dynamique."

---

# Filtres

> Le présent article de référence présente un aperçu des filtres dans Liquid et couvre les filtres pris en charge par Braze. Vous recherchez des idées sur la façon d’utiliser ces filtres ? Découvrez notre [Bibliothèque de scénarios d’utilisation de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

{% raw %}

Les filtres vous permettent de modifier la sortie des nombres, des chaînes de caractères, des variables et des objets dans Liquid. Vous pouvez utiliser des filtres pour reformater le texte statique ou dynamique, par exemple, modifier une chaîne de caractères de minuscules en majuscules ou effectuer des opérations mathématiques, comme des additions ou des divisions.

Il faut associer ces filtres à une balise de sortie `{{ }}` et les indiquer par un caractère pipe `|`.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

Dans cet exemple, `Grosse vente` est une chaîne de caractère et `upcase` est le filtre appliqué.

Vous pouvez utiliser plusieurs filtres sur une sortie. Ils sont appliqués de gauche à droite.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Braze ne prend pas en charge tous les filtres Liquid de Shopify. Cette page a pour objectif définir les filtres Liquid que Braze a testés, néanmoins, cette liste peut ne pas être exhaustive. Toujours tester votre Liquid avant d’envoyer des messages. 
<br><br>Si vous avez des questions sur un filtre non répertorié ici, contactez le service d’assistance ou le gestionnaire du succès des clients.
{% endalert %}

## Filtres de tableau

Les filtres de tableau servent à modifier leur sortie.

| Filtre         | Définition                                                                                                         | Pris en charge |
| :------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [joindre][1.1]    | Joint les éléments d’un tableau avec le caractère transmis en tant de paramètre. Il en résulte une chaîne de caractères unique.          | ✅  Oui   |
| [premier][1.2]   | Renvoie le premier élément d’un tableau. Dans un tableau d’attribut personnalisé, c’est la valeur ajoutée la plus ancienne.         | ✅  Oui   |
| [dernier][1.3]    | Renvoie le dernier élément d’un tableau. Dans un tableau d’attribut personnalisé, c’est la valeur ajoutée la plus récente.                 | ✅  Oui   |
| [compact][1.4]  | Enlève tous les éléments `nil` d’un tableau.                                                                              | ✅  Oui    |
| [concat][1.5]  | Combine un tableau avec un autre tableau.                                                                              | ✅  Oui    |
| [index][1.6]   | Renvoie l’élément à l’emplacement d’index spécifié dans un tableau. Le premier élément d’un tableau est référencé avec `[0]`. | ✅  Oui   |
| [carte][1.7]     | Accepte l’attribut d’un élément de tableau comme paramètre et crée un tableau à partir de la valeur de chaque élément du tableau.        | ✅  Oui   |
| [inverser][1.8] | Inverse l’ordre des éléments dans un tableau.                                                                       | ✅  Oui   |
| [Taille][1.9]    | Renvoie la taille d’une chaîne de caractères (nombre de caractères) ou un tableau (nombre d’éléments).                      | ✅  Oui   |
| [trier][1.10]    | Trie les éléments d’un tableau par un attribut donné d’un élément dans le tableau.                                    | ✅  Oui   |
| [sort_natural][1.11]    | Trie les éléments d’un tableau selon un ordre alphabétique sensible à la casse.                                    | ✅  Oui   |
| [uniq][1.12]   | Supprime les instances en doublon d’éléments dans un tableau.                                                           | ✅  Oui   |
| [where][1.13]   | Filtre un tableau pour n’afficher que les objets ayant une valeur de propriété spécifique.                                                           | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtres de couleur

Les [filtres de couleur][2.1] ne sont pas pris en charge par Braze.

## Filtres de polices

Les [Filtres de police][3.1] ne sont pas pris en charge par Braze.

## Filtres mathématiques

Les filtres mathématiques vous permettent d’effectuer des opérations mathématiques. Rappelez-vous : si vous utilisez plusieurs filtres sur une sortie, ils sont appliqués de gauche à droite.

| Filtre            | Définition                                                                                                                     | Pris en charge |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [abs][4.1]        | Renvoie la valeur absolue d’un nombre.                                                                                        | ✅  Oui   |
| [at_most][4.2]    | Limite un nombre à une valeur maximale.                                                                                            | ✅  Oui    |
| [at_least][4.3]   | Limite un nombre à une valeur minimale.                                                                                            | ✅  Oui   |
| [Plafond][4.4]       | Arrondit une sortie au nombre entier le plus proche.                                                                                    | ✅  Oui   |
| [divided_by][4.5] | Divise une sortie par un nombre. La sortie est arrondie au nombre entier le plus proche. Pour évitez l’arrondi, suivez le conseil suivant. | ✅  Oui   |
| [Palier][4.6]      | Arrondit une sortie au nombre entier inférieur le plus proche.                                                                                  | ✅  Oui   |
| [moins][4.7]      | Soustrait un nombre à partir d’une sortie.                                                                                             | ✅  Oui   |
| [plus][4.8]       | Ajoute un numéro à une sortie.                                                                                                    | ✅  Oui   |
| [Arrondi][4.9]      | Arrondit la sortie au nombre entier le plus proche ou au nombre spécifié de décimales.                                                      | ✅  Oui   |
| [Fois][4.10]     | Multiplie une sortie par un nombre.                                                                                              | ✅  Oui   |
| [modulo][4.11]    | Divise une sortie par un nombre et renvoie le reliquat.                                                                       | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Lorsque vous divisez les nombres entiers par des entiers dans Liquid, si la réponse est un float (nombre avec une décimale), Liquid arrondira automatiquement au nombre entier le plus proche. Cependant, la division des nombres entiers par des floats fournit toujours un float. Cela signifie que vous pouvez transformer vos nombres entiers en float (1,0, 2,0, 3,0) pour obtenir un float.
{% raw %}
<br><br>For example,`{{15 | divided_by: 2}}` will output `7`, whereas  `{{15 | divided_by: 2.0}}` will output `7.5`.
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

Par exemple, supposons que nous voulons calculer le solde actuel d’un utilisateur en ajoutant son solde de carte-cadeau et son solde de récompenses. Tout d’abord, utilisez la balise `assign` pour remplacer l’attribut personnalisé de `current_rewards_balance` par le terme « solde ». Cela signifie que vous avez maintenant une variable intitulée `balance` que vous pouvez manipuler.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Ensuite, utilisez le filtre `plus` pour combiner le solde de la carte-cadeau de chaque utilisateur avec son solde de récompenses, indiqué par l’objet `{{balance}}`. 
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres monétaires

Si vous mettez à jour un utilisateur sur son achat, un solde de compte ou tout ce qui concerne une somme d’argent, vous devez utiliser des filtres monétaires. Les filtres monétaires permettent de garantir que vos décimales sont à l’endroit approprié et qu’aucun élément de votre mise à jour n’est perdu (comme ce problème `0` à la fin).

| Filtre                              | Définition                                                                                                             | Pris en charge |
| :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :-------- |
| [argent][5.1]                        | Formate les nombres pour s’assurer que les décimales sont à l’endroit approprié et que les zéros ne sont pas supprimés de la fin des nombres. | ✅  Oui   |
| [money_with_currency][5.2]          | Formate les nombre avec le symbole de devise. | ⛔  Non   |
| [money_without_trailing_zeros][5.3] | Formate les nombres pour exclure le séparateur de décimale (soit `.`, soit `,`) et des zéros de fin. S’il n’y a pas de zéro de fin, ce filtre se comporte comme le filtre `money`. | ✅  Oui   |
| [money_without_currency][5.4]       | Formate les nombre sans le symbole de devise.                                                       | ⛔  Non    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Comparaison du filtre monétaire Shopify avec celui de Braze.

{% alert warning %}
Le comportement du filtre Shopify `money` est différent du filtre de Braze. Consultez les exemples suivants pour obtenir une description précise du comportement attendu.
{% endalert %}

{% raw %}
Si vous mettiez en place un attribut personnalisé (comme `account_balance`), vous devez toujours utiliser le filtre `money` pour vous assurer que vos décimales sont au bon endroit et que les zéros ne sont pas retirés de la fin de tous les numéros :

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| AVEC LE FILTRE MONÉTAIRE                       | SANS LE FILTRE MONÉTAIRE                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Avec filtre monétaire][1]                     | ![Sans filtre monétaire][2]                  |
| Où `account_balance` est une saisie à `17.8`. | Où `account_balance` est une saisie à `17.8`. |
{: .reset-td-br-1 .reset-td-br-2}

Le filtre `money` de Braze diffère de Shopify en ce qu’il n’applique pas automatiquement les points décimaux selon un réglage prédéfini. Prenons par exemple le scénario suivant : `rewards_redeemed` contient une valeur de `145` :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Selon le filtre [monétaire][5.1] de Shopify, il devrait avoir une sortie de `$1.45`, mais avec Braze, il aura une sortie de `$145.00`. En tant que solution de contournement, nous pouvons utiliser le filtre `divided_by` pour manipuler le nombre en une décimale, avant d’appliquer le filtre monétaire :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
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
Les guillemets droits sont différents des guillemets courbes dans Liquid. Soyez prudent lorsque vous copiez et collez Liquid depuis un éditeur de texte dans Braze, car les guillemets courbes provoquent des erreurs dans Liquid.. Si vous rédigez avec Liquid directement dans Braze, les guillemets droits seront appliqués automatiquement.
{% endalert %}

| Filtre                                           | Description                     | Pris en charge |
| :----------------------------------------------- | ------------------------------- | --------- |
| [ajouter][6.1]                                    | Ajoute des caractères à une chaîne de caractères. | ✅  Oui   |
| [camelcase][6.2]                                 | Transforme une chaîne de caractères en CamelCase. | ⛔  Non    |
| [capitaliser][6.3]                                | Capitalise le premier mot dans une chaîne de caractères.   | ✅  Oui   |
| [minuscules][6.4]                                  | Convertit une chaîne de caractères en minuscules. | ✅  Oui   |
| [escape][6.5]                                    | Échappe une chaîne de caractères.  | ✅  Oui   |
| [handle/handleize][6.6]                          | Formate une chaîne de caractère en handle.     | ⛔  Non    |
| [md5][6.7]                                       | Convertit une chaîne de caractères en hash MD5. Consulter le [Codage des filtres][3] pour en savoir plus. | ✅  Oui   |
| [sha1][6.8]                                      | Convertit une chaîne de caractères en hash SHA-1. Consulter le [Codage des filtres][3] pour en savoir plus. | ✅  Oui   |
| hmac_sha1_hex<br>(auparavant [hmac_sha_1][6.10]) | Convertit une chaîne de caractères en hash SHA-1 en utilisant un code d’authentification de message hash (HMAC). Transmet la clé secrète pour le message en tant que paramètre au filtre. Consulter le [Codage des filtres][3] pour en savoir plus. | ✅  Oui   |
| [hmac_sha256][6.11]                              | Convertit une chaîne de caractères en hash SHA-256 en utilisant un code d’authentification de message hash (HMAC). Transmet la clé secrète pour le message en tant que paramètre au filtre.| ✅  Oui   |
| [newline_to_br][6.12]                            | Insère une balise `<br>` de saut de ligne devant chaque saut de ligne dans une chaîne de caractères. | ✅  Oui   |
| [pluralize][6.13]                                | Génère la version au singulier ou au pluriel d’une chaîne de caractères anglaise en fonction de la valeur d’un nombre. | ⛔  Non    |
| [prepend][6.14]                                  | Ajoute des caractères au début d’une chaîne de caractères.  | ✅  Oui   |
| [supprimer][6.15]                                   | Supprime toutes les occurrences d’une sous-chaîne d’une chaîne de caractères. | ✅  Oui   |
| [remove_first][6.16]                             | Supprime uniquement la première occurrence d’une sous-chaîne d’une chaîne de caractères. | ✅  Oui   |
| [remplacer][6.17]                                  | Remplace toutes les occurrences d’une chaîne de caractères par une sous-chaîne.  | ✅  Oui   |
| [replace_first][6.18]                            | Remplace la première occurrence d’une chaîne de caractères par une sous-chaîne.  | ✅  Oui   |
| [slice][6.19]                                    | Le filtre de coupe restitue une sous-chaîne, à partir de l’index spécifié. | ✅  Oui   |
| [split][6.20]                                    | Le filtre de division prend une sous-chaîne comme paramètre. La sous-chaîne est utilisée comme séparateur pour diviser une chaîne de caractères en tableau.   | ✅  Oui   |
| [strip][6.21]                                    | Découpe les tabulations, les espaces et les nouvelles lignes (tous les espaces blancs) à gauche et à droite d’une chaîne de caractères. | ✅  Oui   |
| [lstrip][6.22]                                   | Découpe les tabulations, les espaces et les nouvelles lignes (tous les espaces blancs) à gauche d’une chaîne de caractères. | ⛔  Non    |
| [rstrip][6.23]                                   | Découpe les tabulations, les espaces et les nouvelles lignes (tous les espaces blancs) à droite d’une chaîne de caractères. | ⛔  Non    |
| [strip_html][6.24]                               | Permet de découper toutes les balises HTML d’une chaîne de caractères. | ✅  Oui   |
| [strip_newlines][6.25]                           | Supprime les sauts de ligne/nouvelles lignes d’une chaîne de caractères. | ✅  Oui   |
| [truncate][6.26]                                 | Tronque une chaîne de caractères en nombre de caractères transmis comme premier paramètre. Une ellipse (…) est ajoutée à la chaîne de caractères tronquée et est incluse dans le nombre de caractères. | ✅  Oui   |
| [truncatewords][6.27]                            | Tronque une chaîne de caractères en nombre de caractères transmis comme premier paramètre. Une ellipse (…) est ajoutée à la chaîne de caractères tronquée. | ✅  Oui   |
| [upcase][6.28]                                   | Convertit une chaîne de caractères en majuscules. | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtres supplémentaires

Les filtres généraux suivants servent de nombreux objectifs, notamment le formatage ou la conversion de contenus.

| Filtre         | Description                                                                         | Pris en charge |
| -------------- | ----------------------------------------------------------------------------------- | :-------- |
| [date][7.1]           | Convertit un horodatage en un autre format de date. Consulter [Filtre de date](#date-filter) pour en savoir plus. | ✅  Oui   |
| [default][7.2]        | Définit une valeur par défaut pour toute variable sans valeur attribuée. Peut être utilisé avec des chaînes de caractères, des tableaux et des hachages. | ✅  Oui   |
| [format_address][7.3] | Formate une adresse pour imprimer les éléments de l’adresse dans l’ordre selon leur emplacement. | ⛔  Non    |
| [highlight][7.4]      | Entoure les mots à l’intérieur des résultats de recherche d’une balise HTML `<strong>` avec la classe surlignée si elle correspond aux termes de recherche transmis. | ⛔  Non    |
| time_zone      | Consulter [Filtre fuseau horaire](#time-zone-filter) pour en savoir plus. | ✅  Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Un nombre plus important de filtres pris en charge, tels que les filtres d’encodage et d’URL, figurent sur notre page [Filtres avancés]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) .

### Filtre date {#date-filter}

Le filtre `date` peut servir à convertir un horodatage en un format de date différent. Vous pouvez transmettre des paramètres au filtre `date` pour reformater l’horodatage. Pour des exemples de ces paramètres, consultez [strfti.me](http://www.strfti.me/).

Par exemple, supposons que la valeur de `date_attribute` est l’horodatage `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

En plus des options de formatage `strftime`, Braze prend également en charge la conversion d’un horodatage en temps Unix avec le filtre de date `%s`. Par exemple, pour obtenir `date_attribute` en temps Unix :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
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
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Vous pouvez également utiliser la variable réservée `now` pour accéder à la date et à l’heure actuelles pour les manipuler.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters#compact
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.11]: https://shopify.dev/api/liquid/filters#sort_natural
[1.12]: https://shopify.dev/api/liquid/filters/array-filters#uniq
[1.13]: https://shopify.dev/api/liquid/filters#where

[2.1]: https://shopify.dev/api/liquid/filters/color-filters
[3.1]: https://shopify.dev/api/liquid/filters/font-filters

[4.1]: https://shopify.dev/api/liquid/filters/math-filters#abs
[4.2]: https://shopify.dev/api/liquid/filters/math-filters#at_most
[4.3]: https://shopify.dev/api/liquid/filters/math-filters#at_least
[4.4]: https://shopify.dev/api/liquid/filters/math-filters#ceil
[4.5]: https://shopify.dev/api/liquid/filters/math-filters#divided_by
[4.6]: https://shopify.dev/api/liquid/filters/math-filters#floor
[4.7]: https://shopify.dev/api/liquid/filters/math-filters#minus
[4.8]: https://shopify.dev/api/liquid/filters/math-filters#plus
[4.9]: https://shopify.dev/api/liquid/filters/math-filters#round
[4.10]: https://shopify.dev/api/liquid/filters/math-filters#times
[4.11]: https://shopify.dev/api/liquid/filters/math-filters#modulo

[5.1]: https://shopify.dev/api/liquid/filters/money-filters#money
[5.2]: https://shopify.dev/api/liquid/filters/money-filters#money_with_currency
[5.3]: https://shopify.dev/api/liquid/filters/money-filters#money_without_trailing_zeros
[5.4]: https://shopify.dev/api/liquid/filters/money-filters#money_without_currency

[6.1]: https://shopify.dev/api/liquid/filters/string-filters#append
[6.2]: https://shopify.dev/api/liquid/filters/string-filters#camelcase
[6.3]: https://shopify.dev/api/liquid/filters/string-filters#capitalize
[6.4]: https://shopify.dev/api/liquid/filters/string-filters#downcase
[6.5]: https://shopify.dev/api/liquid/filters/string-filters#escape
[6.6]: https://shopify.dev/api/liquid/filters/string-filters#handle-handleize
[6.7]: https://shopify.dev/api/liquid/filters/string-filters#md5
[6.8]: https://shopify.dev/api/liquid/filters/string-filters#sha1
[6.10]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1
[6.11]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256
[6.12]: https://shopify.dev/api/liquid/filters/string-filters#newline_to_br
[6.13]: https://shopify.dev/api/liquid/filters/string-filters#pluralize
[6.14]: https://shopify.dev/api/liquid/filters/string-filters#prepend
[6.15]: https://shopify.dev/api/liquid/filters/string-filters#remove
[6.16]: https://shopify.dev/api/liquid/filters/string-filters#remove_first
[6.17]: https://shopify.dev/api/liquid/filters/string-filters#replace
[6.18]: https://shopify.dev/api/liquid/filters/string-filters#replace_first
[6.19]: https://shopify.dev/api/liquid/filters/string-filters#slice
[6.20]: https://shopify.dev/api/liquid/filters/string-filters#split
[6.21]: https://shopify.dev/api/liquid/filters/string-filters#strip
[6.22]: https://shopify.dev/api/liquid/filters/string-filters#lstrip
[6.23]: https://shopify.dev/api/liquid/filters/string-filters#rstrip
[6.24]: https://shopify.dev/api/liquid/filters/string-filters#strip_html
[6.25]: https://shopify.dev/api/liquid/filters/string-filters#strip_newlines
[6.26]: https://shopify.dev/api/liquid/filters/string-filters#truncate
[6.27]: https://shopify.dev/api/liquid/filters/string-filters#truncatewords
[6.28]: https://shopify.dev/api/liquid/filters/string-filters#upcase

[7.1]: https://shopify.dev/api/liquid/filters/additional-filters#date
[7.2]: https://shopify.dev/api/liquid/filters/additional-filters#default
[7.3]: https://shopify.dev/api/liquid/filters/additional-filters#format_address
[7.4]: https://shopify.dev/api/liquid/filters/additional-filters#highlight


[1]: {% image_buster /assets/img/with_money_filter.png %}
[2]: {% image_buster /assets/img/without_money_filter.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters
