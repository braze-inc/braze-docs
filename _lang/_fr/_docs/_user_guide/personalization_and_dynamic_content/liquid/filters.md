---
nav_title: Filtres
article_title: Filtres Liquide
page_order: 3
description: "Les filtres peuvent être utilisés pour reformater le contenu statique ou dynamique. Cet article de référence couvre les filtres Liquid supportés par Braze."
---

# Filtres

> Cet article de référence fournit une vue d'ensemble des filtres dans le liquide et couvre les filtres qui sont supportés par le bras. Vous cherchez des idées sur la façon dont vous pouvez utiliser ces filtres ? Consultez notre [bibliothèque de cas d'utilisation de liquides]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

{% raw %}

Les filtres sont comment vous pouvez modifier la sortie des nombres, des chaînes, des variables et des objets dans Liquid. Vous pouvez utiliser des filtres pour reformater du texte statique ou dynamique, comme changer une chaîne de caractères de minuscule en majuscule ou pour effectuer des opérations mathématiques, comme l'ajout ou la division.

Les filtres doivent être placés dans une balise de sortie `{{ }}` et sont notés par un caractère de pipe `|`.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcas}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
GRANDE VENTE
```
{% endraw %}
{% endtab %}
{% endtabs %}

Dans l'exemple ci-dessus, `Big Sale` est une chaîne, et `upcase` est le filtre en cours d'application.

Vous pouvez utiliser plusieurs filtres sur une seule sortie. Ils sont appliqués de gauche à droite.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: “BIG” }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Vente
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Braze ne supporte pas tous les filtres Liquid de Shopify. Cette page tente de décrire les filtres Liquid que Braze a testés, mais il se peut que ce ne soit pas une liste complète. Testez toujours votre Liquid avant d'envoyer des messages. <br><br>Si vous avez des questions à propos d'un filtre qui n'est pas listé ici, veuillez contacter le Support ou contacter votre Responsable Customer Success Manager.
{% endalert %}

## Filtres de tableau

Les filtres de tableaux sont utilisés pour modifier la sortie des tableaux.

| Filtre           | Définition                                                                                                                      | Supporté |
|:---------------- |:------------------------------------------------------------------------------------------------------------------------------- |:-------- |
| [rejoindre][1.1] | Rejoint les éléments d'un tableau avec le caractère passé comme paramètre. Le résultat est une seule chaîne.                    | ✅ Oui    |
| [premier][1.2]   | Retourne le premier élément d'un tableau. Dans un tableau d'attributs personnalisés, c'est la dernière valeur ajoutée.          | ✅ Oui    |
| [dernier][1.3]   | Retourne le dernier élément d'un tableau. Dans un tableau d'attributs personnalisés, c'est la valeur ajoutée la plus ancienne.  | ✅ Oui    |
| [concat][1.4]    | Combine un tableau avec un autre tableau.                                                                                       | ⛔ Non    |
| [index][1.5]     | Renvoie l'élément à l'emplacement de l'index spécifié dans un tableau. Le premier élément d'un tableau est référencé par `[0]`. | ✅ Oui    |
| [carte][1.6]     | Accepte l'attribut d'un tableau en tant que paramètre et crée un tableau à partir de la valeur de chaque élément du tableau.    | ✅ Oui    |
| [inversé][1.7]   | Inverse l'ordre des éléments d'un tableau.                                                                                      | ✅ Oui    |
| [taille][1.8]    | Retourne la taille d'une chaîne de caractères (le nombre de caractères) ou d'un tableau (le nombre d'éléments).                 | ✅ Oui    |
| [trier][1.9]     | Trie les éléments d'un tableau par un attribut donné d'un élément dans le tableau.                                              | ✅ Oui    |
| [uniq][1.10]     | Supprime toutes les instances dupliquées d'éléments dans un tableau.                                                            | ✅ Oui    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtres de couleur

[Les filtres de couleur][2.1] ne sont pas pris en charge en Brésil.

## Filtres de police

[Les filtres de police][3.1] ne sont pas pris en charge en Brésil.

## Filtres mathématiques

Les filtres mathématiques vous permettent d'effectuer des opérations mathématiques. N'oubliez pas : si vous utilisez plusieurs filtres sur une sortie, ils sont appliqués de gauche à droite.

| Filtre            | Définition                                                                                                                                            | Supporté |
|:----------------- |:----------------------------------------------------------------------------------------------------------------------------------------------------- |:-------- |
| [abs][4.1]        | Renvoie la valeur absolue d'un nombre.                                                                                                                | ✅ Oui    |
| [à _maximum][4.2] | Limite un nombre à une valeur maximale.                                                                                                               | ⛔ Non    |
| [au moins][4.3]   | Limite un nombre à une valeur minimale.                                                                                                               | ⛔ Non    |
| [télé][4.4]       | Arrondie une sortie à un entier le plus proche.                                                                                                       | ✅ Oui    |
| [divisé par][4.5] | Divise une sortie par un nombre. La sortie est arrondie à l'entier le plus proche. Consultez les conseils ci-dessous pour éviter les arrondissements. | ✅ Oui    |
| [plancher][4.6]   | Arrondie une sortie vers l'entier le plus proche.                                                                                                     | ✅ Oui    |
| [minus][4.7]      | Soustrait un nombre d'une sortie.                                                                                                                     | ✅ Oui    |
| [plus][4.8]       | Ajoute un nombre à une sortie.                                                                                                                        | ✅ Oui    |
| [manche][4.9]     | Arrondit la sortie à l'entier le plus proche ou au nombre spécifié de décimales.                                                                      | ✅ Oui    |
| [fois][4.10]      | Multiplie une sortie par un nombre.                                                                                                                   | ✅ Oui    |
| [modulo][4.11]    | Divise une sortie par un nombre et retourne le reste.                                                                                                 | ✅ Oui    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Lorsque vous divisez des entiers (nombres entiers) par des entiers dans Liquid, si la réponse est un float (nombre avec un décimal), Liquid s'arrondit automatiquement à un entier le plus proche. Cependant, diviser les nombres entiers par des nombres décimaux vous donnera toujours un nombre décimal . Cela signifie que vous pouvez transformer vos entiers en un nombre décimal (1.0, 2.0, 3.0) pour retourner un nombre décimal.
{% raw %}
<br><br>Par exemple,`{{15 | divided_by: 2}}` affichera `7`, tandis que  `{{15 | divided_by: 2.0}}` affichera `7.5`.
{% endraw %}
{% endalert %}

### Opérations mathématiques avec attributs personnalisés

Gardez à l'esprit que vous ne pouvez pas effectuer d'opérations mathématiques entre deux attributs personnalisés.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Cet exemple ne fonctionnerait pas parce que vous ne pouvez pas référencer plusieurs attributs personnalisés dans une ligne de Liquid. À la place, vous devrez assigner une variable à au moins une de ces valeurs avant que les fonctions mathématiques ne se déroulent. Ajouter deux attributs personnalisés ensemble nécessiterait deux lignes de Liquid :

1. Un pour assigner l'attribut personnalisé à une variable,
2. Un pour effectuer l'ajout.

Par exemple, disons que nous voulons calculer le solde actuel d'un utilisateur en ajoutant son solde de carte-cadeau et son solde de récompense. Premièrement, utilisez la balise `assigner` pour remplacer l'attribut personnalisé de `current_rewards_balance` par le terme « balance ». Cela signifie que vous avez maintenant une variable nommée `balance`, que vous pouvez manipuler.

```liquid
{% balance assignée = {{custom_attribute.${current_rewards_balance}}} %}
```

Ensuite, utilisez le filtre `plus` pour combiner le solde de la carte-cadeau de chaque utilisateur avec son solde de récompense, signifié par l'objet `{{balance}}`.
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% balance assignée = {{custom_attribute.${current_rewards_balance}}} %}
Vous avez ${{custom_attribute.${giftcard_balance} | plus : {{balance}}}} à dépenser !
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Vous avez 35 $ pour dépenser!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtres d'argent

Si vous mettez à jour un utilisateur à son achat, un solde de compte ou quoi que ce soit en ce qui concerne l'argent, vous devriez utiliser des filtres d'argent. Les filtres d'argent s'assurent que vos décimales sont au bon endroit et qu'aucune partie de votre mise à jour n'est perdue (comme ce pesant `0` à la fin).

| Filtre                                          | Définition                                                                                                                                                                           | Supporté |
|:----------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:-------- |
| [argent][5.1]                                   | Formats les nombres pour s'assurer que les décimales sont à la bonne place, et les zéros ne sont pas supprimés de la fin des nombres.                                                | ✅ Oui    |
| [argent_avec_monnaie][5.2]                    | Formate les nombres avec le symbole de devise.                                                                                                                                       | ✅ Oui    |
| [format@@0 money_without_trailing_zeros][5.3] | Forme les nombres pour exclure le séparateur décimal (soit `.` ou `,`) et les zéros suivants. S'il n'y a pas de zéros suivants, alors ce filtre se comporte comme le filtre `money`. | ✅ Oui    |
| [argent_sans_monnaie][5.4]                    | Formate les nombres sans le symbole de devise.                                                                                                                                       | ⛔ Non    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Filtre argent Shopify vs filtre argent Braze

{% alert warning %}
Le comportement du filtre Shopify `money` diffère de la façon dont il est utilisé en Brésil. Reportez-vous aux exemples ci-dessous pour une description précise du comportement attendu.
{% endalert %}

{% raw %}
Dans le cas où vous saisissez un attribut personnalisé (comme `account_balance`), vous devriez toujours utiliser le filtre `money` pour vous assurer que vos décimales sont au bon endroit, et les zéros ne sont pas abandonnés à la fin des nombres, comme montré ci-dessous:

```liquid
${{custom_attribute.${account_balance} | argent}}
```
{% endraw %}

| AVEC LE FILTRE D'ARGENT                  | SANS LE FILTRE D'ARGENT                  |
|:---------------------------------------- |:---------------------------------------- |
| !\[Filtre avec argent \]\[1\]            | !\[Sans filtre d'argent\]\[2\]           |
| Où `account_balance` est entré à `17,8`. | Où `account_balance` est entré à `17,8`. |
{: .reset-td-br-1 .reset-td-br-2}

Le filtre `money` dans Braze diffère de Shopify dans la mesure où il n'applique pas automatiquement les points décimaux selon un paramètre prédéfini. Par exemple, prenez le scénario suivant où `rewards_redeemed` contient une valeur de `145`:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | argent }}
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

Selon le filtre [argent][5.1] de Shopify, cela devrait avoir une sortie de `$1. 5`, cependant en Brésil, cela aura une sortie de `$145,00`. Comme solution de contournement, nous pouvons utiliser le filtre `divisé par` pour manipuler le nombre en décimal, avant d'appliquer le filtre de l'argent :

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | argent }}
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

## Filtres de chaîne de caractères

Les filtres de chaînes de caractères sont utilisés pour manipuler les sorties et les variables des chaînes. Les chaînes de caractères sont une combinaison de caractères alphanumériques et doivent être entourées de guillemets droits.

{% alert note %}
Les guillemets droits sont différents des guillemets bouclés de Liquid. Faites attention lorsque vous copiez et collez Liquid d'un éditeur de texte dans Braze, car les guillemets bouclés provoqueront des erreurs avec votre Liquid. Si vous écrivez votre Liquid directement dans Braze, les guillemets droits seront appliqués automatiquement.
{% endalert %}

| Filtre                                                       | Libellé                                                                                                                                                                                                                                       | Supporté |
|:------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [ajouter][6.1]                                               | Ajoute des caractères à une chaîne.                                                                                                                                                                                                           | ✅ Oui    |
| [camélia][6.2]                                               | Convertit une chaîne en CamelCase.                                                                                                                                                                                                            | ⛔ Non    |
| [majuscule][6.3]                                             | Majuscule le premier mot dans une chaîne.                                                                                                                                                                                                     | ✅ Oui    |
| [downcase][6.4]                                              | Convertit une chaîne en minuscules.                                                                                                                                                                                                           | ✅ Oui    |
| [échapper][6.5]                                              | Échappe une chaîne.                                                                                                                                                                                                                           | ✅ Oui    |
| [poignée / poignée][6.6]                                     | Formate une chaîne de caractères en un gestionnaire.                                                                                                                                                                                          | ⛔ Non    |
| [md5][6.7]                                                   | Convertit une chaîne en un hash MD5. Reportez-vous à [Filtres d'encodage][3] pour en savoir plus.                                                                                                                                             | ✅ Oui    |
| [sha1][6.8]                                                  | Convertit une chaîne en un hachage SHA-1. Reportez-vous à [Filtres d'encodage][3] pour en savoir plus.                                                                                                                                        | ✅ Oui    |
| hmac_sha1_hex<br>(précédemment [hmac_sha_1][6.10]) | Convertit une chaîne en un hachage SHA-1 en utilisant un code d'authentification de hachage de message (HMAC). Passer la clé secrète du message en tant que paramètre au filtre. Reportez-vous à [Filtres d'encodage][3] pour en savoir plus. | ✅ Oui    |
| [hmac_sha256][6.11]                                          | Convertit une chaîne de caractères en un hachage SHA-256 en utilisant un code d'authentification de hachage de message (HMAC). Passer la clé secrète du message en tant que paramètre au filtre.                                              | ✅ Oui    |
| [newline_to_br][6.12]                                      | Insère une balise HTML `<br>` saut de ligne devant chaque saut de ligne dans une chaîne.                                                                                                                                                | ✅ Oui    |
| [pluraliser][6.13]                                           | Affiche la version singulière ou plurielle d'une chaîne de caractères anglaise basée sur la valeur d'un nombre.                                                                                                                               | ⛔ Non    |
| [préfixe][6.14]                                              | Ajoute des caractères à une chaîne.                                                                                                                                                                                                           | ✅ Oui    |
| [Enlever][6.15]                                              | Supprime toutes les occurrences d'une sous-chaîne d'une chaîne.                                                                                                                                                                               | ✅ Oui    |
| [Retirer d'abord][6.16]                                      | Supprime seulement la première occurrence d'une sous-chaîne d'une chaîne.                                                                                                                                                                     | ✅ Oui    |
| [Remplacer][6.17]                                            | Remplace toutes les occurrences d'une chaîne par une sous-chaîne.                                                                                                                                                                             | ✅ Oui    |
| [Remplacer d'abord][6.18]                                    | Remplace la première occurrence d'une chaîne par une sous-chaîne.                                                                                                                                                                             | ✅ Oui    |
| [tranche][6.19]                                              | Le filtre "slice" renvoie une sous-chaîne à partir de l'index spécifié.                                                                                                                                                                       | ✅ Oui    |
| [séparer][6.20]                                              | Le filtre de séparation prend une sous-chaîne comme paramètre. La sous-chaîne est utilisée comme délimiteur pour diviser une chaîne en un tableau.                                                                                            | ✅ Oui    |
| [bande][6.21]                                                | Enlève les tabulations, les espaces et les nouvelles lignes (tous les blancs) du côté gauche et droit d'une chaîne.                                                                                                                           | ✅ Oui    |
| [lstrip][6.22]                                               | Enlève les tabulations, les espaces et les nouvelles lignes (tous les blancs) à partir du côté gauche d'une chaîne de caractères.                                                                                                             | ⛔ Non    |
| [ruban][6.23]                                                | Enlève les tabulations, les espaces et les nouvelles lignes (tous les blancs) du côté droit d'une chaîne.                                                                                                                                     | ⛔ Non    |
| [format@@0 strip_html][6.24]                                 | Enlève toutes les balises HTML d'une chaîne.                                                                                                                                                                                                  | ✅ Oui    |
| [strip_newlines][6.25]                                       | Supprime les sauts de ligne/saut de ligne d'une chaîne.                                                                                                                                                                                       | ✅ Oui    |
| [tronquer][6.26]                                             | Tronque une chaîne vers le bas au nombre de caractères passés comme premier paramètre. Une ellipse (...) est ajoutée à la chaîne tronquée et est incluse dans le nombre de caractères.                                                        | ✅ Oui    |
| [mots tronqués][6.27]                                        | Tronque une chaîne de caractères au nombre de mots passés comme premier paramètre. Une ellipse (...) est ajoutée à la chaîne tronquée.                                                                                                        | ✅ Oui    |
| [upcase][6.28]                                               | Convertit une chaîne en majuscules.                                                                                                                                                                                                           | ✅ Oui    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Filtres supplémentaires

Les filtres généraux suivants servent à de nombreuses fins, y compris la mise en forme ou la conversion de contenu.

| Filtre                     | Libellé                                                                                                                                                                            | Supporté |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-------- |
| [date][7.1]                | Convertit un horodatage en un autre format de date. Reportez-vous au [filtre de date](#date-filter) ci-dessous pour en savoir plus.                                                | ✅ Oui    |
| [par défaut][7.2]          | Définit une valeur par défaut pour toute variable sans valeur assignée. Peut être utilisé avec des chaînes, des tableaux et des haches.                                            | ✅ Oui    |
| [Format de l'adresse][7.3] | Formate une adresse pour imprimer les éléments de l'adresse dans l'ordre selon leur locale.                                                                                        | ⛔ Non    |
| [en surbrillance][7.4]     | Inclus les mots dans les résultats de recherche avec une balise HTML `<strong>` </code> avec la surbrillance de la classe si elle correspond aux termes de recherche soumis. | ⛔ Non    |
| fuseau horaire             | Reportez-vous à [Filtre de fuseau horaire](#time-zone-filter) ci-dessous pour en savoir plus.                                                                                      | ✅ Oui    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous pouvez trouver des filtres plus supportés, tels que l'encodage et les filtres d'URL, sur notre page [Filtres Avancés]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Filtre de date {#date-filter}

Le filtre `date` peut être utilisé pour convertir un horodatage dans un format de date différent. Vous pouvez passer dans les paramètres au filtre `date` pour reformater l'horodatage. Pour des exemples de ces paramètres, reportez-vous à [strfti.me](http://www.strfti.me/).

Par exemple, disons que la valeur de `date_attribute` est l'horodatage `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b','d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 Juin
```
{% endraw %}
{% endtab %}
{% endtabs %}

En plus des options de formatage `strftime` , Braze prend également en charge la conversion d'un horodatage en heure Unix avec le filtre de date `%s`. Par exemple, pour obtenir l'attribut `date_attribute` en temps Unix :

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

### Filtre de fuseau horaire {#time-zone-filter}

{% raw %}
En plus des filtres que vous trouverez dans la documentation de Shopify, Braze prend également en charge le filtre `time_zon`.

Le filtre `time_zone` prend un instant, une fuseau horaire, et un format de date et renvoie l'heure dans ce fuseau horaire dans le format de date spécifié. Par exemple, disons que la valeur de `{{custom_attribute.$date_attribute}}}` est `2021-08-04 9:00:00 UTC`:
{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'Amérique/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Mer 4 août 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Vous pouvez également utiliser la variable réservée `maintenant` pour accéder à la date et à l'heure courante pour la manipulation.

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
[1]: {% image_buster /assets/img/with_money_filter.png %} [2]: {% image_buster /assets/img/without_money_filter.png %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#uniq

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
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters
