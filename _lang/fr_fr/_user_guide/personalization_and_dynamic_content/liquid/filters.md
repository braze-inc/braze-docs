---
nav_title: Filtres
article_title: Filtres à liquides
page_order: 3
description: "Cette page de référence répertorie les filtres qui peuvent être utilisés pour reformater du contenu statique ou dynamique."

---

# Filtres

> Cet article de référence donne un aperçu des filtres dans Liquid et présente les filtres pris en charge par Braze. Vous cherchez des idées pour utiliser ces filtres ? Consultez notre [bibliothèque de cas d'utilisation de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Les filtres vous permettent de modifier la sortie des nombres, des chaînes de caractères, des variables et des objets dans Liquid. Vous pouvez utiliser des filtres pour reformater du texte statique ou dynamique, par exemple pour faire passer une chaîne de caractères de minuscules à majuscules ou pour effectuer des opérations mathématiques, telles que l'addition ou la division.

{% alert important %}
Braze ne prend pas en charge tous les filtres liquides de Shopify. Cette page tente de présenter les filtres à liquides testés par Braze, mais la liste n'est pas exhaustive. Testez toujours votre Liquid avant d'envoyer des messages. <br><br>Si vous avez des questions sur un filtre qui n'est pas répertorié ici, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Syntaxe du filtre

{% raw %}

Les filtres doivent être placés à l'intérieur d'une étiquette de sortie `{{ }}` et sont signalés par un caractère pipe `|`.

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

Dans cet exemple, `Big Sale` est une chaîne de caractères et `upcase` est le filtre appliqué.

### Syntaxe pour les filtres multiples

Vous pouvez utiliser plusieurs filtres sur une même sortie. Ils sont appliqués de gauche à droite.

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

## Filtres de réseau

Les filtres de tableaux sont utilisés pour modifier la sortie des tableaux.

| Filtre               | Définition                                                                                                         | Soutenu |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [rejoindre](https://shopify.dev/docs/api/liquid/filters/join)          | Joint les éléments d'un tableau avec le caractère passé en paramètre. Le résultat est une chaîne de caractères unique.          | ✅ Oui   |
| [premier](https://shopify.dev/docs/api/liquid/filters/first)         | Renvoie le premier élément d'un tableau. Dans un tableau d'attributs personnalisés, il s'agit de la valeur ajoutée la plus ancienne.                | ✅ Oui   |
| [dernier](https://shopify.dev/docs/api/liquid/filters/last)          | Renvoie le dernier élément d'un tableau. Dans un tableau d'attributs personnalisés, il s'agit de la dernière valeur ajoutée.          | ✅ Oui   |
| [compact](https://shopify.dev/api/liquid/filters/compact)       | Supprime tous les éléments `nil` d'un tableau.                                                                             | ✅ Oui   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Combine un tableau avec un autre tableau.                                                                              | ✅ Oui   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Renvoie l'élément situé à l'emplacement/localisation spécifié dans un tableau. Le premier élément d'un tableau est référencé par `[0]`. | ⛔ Non   |
| [mappage](https://shopify.dev/api/liquid/filters/map)           | Accepte l'attribut d'un élément de tableau comme paramètre et crée un tableau à partir de la valeur de chaque élément de tableau.        | ✅ Oui   |
| [inverser](https://shopify.dev/api/liquid/filters/reverse)       | Inverse l'ordre des éléments d'un tableau.                                                                       | ✅ Oui   |
| [taille](https://shopify.dev/api/liquid/filters/size)          | Renvoie la taille d'une chaîne de caractères (le nombre de caractères) ou d'un tableau (le nombre d'éléments).                      | ✅ Oui   |
| [trier](https://shopify.dev/api/liquid/filters/sort)         | Trie les éléments d'un tableau en fonction d'un attribut donné d'un élément du tableau.                                    | ✅ Oui   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Trie les éléments d'un tableau par ordre alphabétique insensible à la casse.                                                | ✅ Oui   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Supprime les instances dupliquées des éléments d'un tableau.                                                           | ✅ Oui   |
| [où](https://shopify.dev/api/liquid/where)        | Filtre un tableau pour n'inclure que les éléments ayant une valeur de propriété spécifique.                                             | ✅ Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtres de couleur

Les [filtres de couleur](https://shopify.dev/api/liquid/filters/color-filters) ne sont pas pris en charge par Braze.

## Filtres de polices

Les [filtres de police](https://shopify.dev/api/liquid/filters/font-filters) ne sont pas pris en charge par Braze.

## Filtres mathématiques

Les filtres mathématiques vous permettent d'effectuer des opérations mathématiques. Si vous utilisez plusieurs filtres sur une même sortie, ils seront appliqués de gauche à droite.

| Filtre  | Définition      | Soutenu |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Renvoie la valeur absolue d'un nombre.     | ✅ Oui   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Limite un nombre à une valeur maximale.   | ✅ Oui   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Limite un nombre à une valeur minimale.   | ✅ Oui   |
| [plafond](https://shopify.dev/api/liquid/filters/ceil)       | Arrondit une sortie à l'entier le plus proche.  | ✅ Oui   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Divise une sortie par un nombre. Le résultat est arrondi à l'entier inférieur le plus proche. Consultez l'astuce suivante pour éviter les arrondis. | ✅ Oui   |
| [plancher](https://shopify.dev/api/liquid/filters/floor)      | Arrondit une sortie à l'entier le plus proche.        | ✅ Oui   |
| [moins](https://shopify.dev/api/liquid/filters/minus)      | Soustrait un nombre d'une sortie.          | ✅ Oui   |
| [plus](https://shopify.dev/api/liquid/filters/plus)       | Ajoute un nombre à une sortie.     | ✅ Oui   |
| [ronde](https://shopify.dev/api/liquid/filters/round)      | Arrondit la sortie à l'entier le plus proche ou au nombre de décimales spécifié.  | ✅ Oui   |
| [fois](https://shopify.dev/api/liquid/filters/times)     | Multiplie une sortie par un nombre.       | ✅ Oui   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Divise une sortie par un nombre et renvoie le reste.   | ✅ Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Lorsque vous divisez des entiers (nombres entiers) par des entiers dans Liquid, si la réponse est un float (nombre avec une décimale), Liquid arrondira automatiquement à l'entier inférieur le plus proche. Cependant, la division d'entiers par des flottants vous donnera toujours un float. Cela signifie que vous pouvez transformer vos entiers en float (1.0, 2.0, 3.0) pour renvoyer un float.
{% raw %}
<br><br>Par exemple,`{{15 | divided_by: 2}}` produira `7`, tandis que `{{15 | divided_by: 2.0}}` produira `7.5`.
{% endraw %}
{% endalert %}

### Opérations mathématiques avec des attributs personnalisés

Gardez à l'esprit que vous ne pouvez pas effectuer d'opérations mathématiques entre deux attributs personnalisés.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Cet exemple ne fonctionnerait pas car vous ne pouvez pas faire référence à plusieurs attributs personnalisés dans une seule ligne de Liquid. Au lieu de cela, vous devez assigner une variable à au moins une de ces valeurs avant que les fonctions mathématiques ne soient exécutées. L'ajout de deux attributs personnalisés nécessiterait deux lignes de Liquid :

1. Un pour affecter l'attribut personnalisé à une variable,
2. Un pour effectuer l'addition.

#### Cas d'utilisation : Calculer le solde actuel

Supposons que nous voulions calculer le solde actuel d'un utilisateur en additionnant le solde de sa carte cadeau et le solde de ses récompenses.

1. Utilisez l'étiquette `assign` pour remplacer l'attribut personnalisé de `current_rewards_balance` par le terme "balance". Cela signifie que vous avez maintenant une variable nommée `balance`, que vous pouvez manipuler.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2\. Utilisez le filtre `plus` pour combiner le solde de la carte cadeau de chaque utilisateur avec son solde de récompenses, indiqué par l'objet `{{balance}}`.
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

## Filtres à argent

Si vous informez un utilisateur de ses achats, du solde de son compte ou de toute autre information concernant l'argent, vous devez utiliser des filtres d'argent. Les filtres monétaires garantissent que vos décimales sont à la bonne place et qu'aucun élément de votre mise à jour n'est perdu (comme ce pesant `0` à la fin).

| Filtre         | Définition          | Soutenu |
| :--------------- | :--------------- | :-------- |
| [argent](https://shopify.dev/api/liquid/filters/money)      | Formate les nombres pour s'assurer que les décimales sont à la bonne place et que les zéros ne sont pas supprimés à la fin des nombres.   | ✅ Oui   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formate les nombres avec le symbole de la devise.     | ⛔ Non    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formate les nombres sans le symbole de la devise.      | ⛔ Non    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Pour formater correctement un numéro avec le filtre `money`, supprimez toutes les virgules du numéro et ajoutez le filtre `plus: 0` avant le filtre `money`. Par exemple, voir le Liquid suivant :<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Filtre à argent de Shopify contre filtre à argent de Braze

{% alert warning %}
Le comportement du filtre Shopify `money` diffère de la façon dont il est utilisé dans Braze. Reportez-vous aux exemples suivants pour avoir une idée précise du comportement attendu.
{% endalert %}

{% raw %}
Si vous saisissez un attribut personnalisé (comme `account_balance`), vous devez toujours utiliser le filtre `money` pour placer les décimales au bon endroit et éviter que des zéros ne tombent à la fin des nombres :

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| AVEC LE FILTRE À ARGENT                       | SANS LE FILTRE DE L'ARGENT                    |
| :------------------------------------------ | :------------------------------------------ |
| \![Avec filtre à argent]({% image_buster /assets/img/with_money_filter.png %})                     | \![Sans filtre à argent]({% image_buster /assets/img/without_money_filter.png %})                  |
| Où `account_balance` est l'entrée à `17.8`. | Où `account_balance` est l'entrée à `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Le filtre `money` de Braze diffère de celui de Shopify car il n'applique pas automatiquement les décimales en fonction d'un paramètre prédéfini. Par exemple, prenez le scénario suivant dans lequel `rewards_redeemed` contient une valeur de `145`:

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

Selon le filtre [monétaire](https://shopify.dev/api/liquid/filters/money) de Shopify, cela devrait avoir une sortie de `$1.45`, cependant dans Braze, cela aura une sortie de `$145.00`. Pour contourner le problème, nous pouvons utiliser le filtre `divided_by` pour transformer le nombre en décimale, avant d'appliquer le filtre money :

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

## Chaîne de caractères

Les filtres de chaînes sont utilisés pour manipuler les sorties et les variables des chaînes de caractères. Les chaînes de caractères sont une combinaison de caractères alphanumériques et doivent être placées entre guillemets droits.

{% alert note %}
Les guillemets droits sont différents des guillemets frisés dans Liquid. Faites attention lorsque vous copiez et collez du liquide d'un éditeur de texte dans Braze, car les guillemets frisés provoqueront des erreurs avec votre liquide. Si vous écrivez votre liquide directement dans Braze, les guillemets droits seront appliqués automatiquement.
{% endalert %}

| Filtre          | Description     | Soutenu |
| :--------------- | ------------- | --------- |
| [ajouter](https://shopify.dev/api/liquid/filters/append)     | Ajoute des caractères à une chaîne de caractères.           | ✅ Oui   |
| [caméliser](https://shopify.dev/docs/api/liquid/filters/camelize)     | Convertit une chaîne de caractères en CamelCase.             | ⛔ Non    |
| [capitaliser](https://shopify.dev/api/liquid/filters/capitalize)     | Met en majuscule le premier mot d'une chaîne de caractères et met en minuscule les autres caractères.         | ✅ Oui   |
| [cas descendant](https://shopify.dev/api/liquid/filters/downcase)      | Convertit une chaîne de caractères en minuscules.         | ✅ Oui   |
| [s'échapper](https://shopify.dev/api/liquid/filters/escape)    | Échappe une chaîne de caractères.             | ✅ Oui   |
| [manipuler](https://shopify.dev/api/liquid/filters/handleize)        | Formate une chaîne de caractères en une poignée.        | ⛔ Non    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Convertit une chaîne de caractères en un hachage MD5. Pour plus d'informations, reportez-vous à la section [Filtres d'encodage]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).   | ✅ Oui   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Convertit une chaîne de caractères en un hachage SHA-1. Pour plus d'informations, reportez-vous à la section [Filtres d'encodage]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).  | ✅ Oui   |
| hmac_sha1_hex<br>(précédemment [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Convertit une chaîne de caractères en un hachage SHA-1 à l'aide d'un code d'authentification de message de hachage (HMAC). Transmettez la clé secrète du message en tant que paramètre au filtre. Pour plus d'informations, reportez-vous à la section [Filtres d'encodage]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters). | ✅ Oui   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Convertit une chaîne de caractères en un hachage SHA-256 à l'aide d'un code d'authentification de message de hachage (HMAC). Transmettez la clé secrète du message en tant que paramètre au filtre.       | ✅ Oui   |
| hmac_sha512 | Convertit une chaîne de caractères en un hachage SHA-512 à l'aide d'un code d'authentification de message de hachage (HMAC). Transmettez la clé secrète du message en tant que paramètre au filtre. | ✅ Oui  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Insère une étiquette HTML `<br>` devant chaque saut de ligne d'une chaîne de caractères.        | ✅ Oui   |
| [pluraliser](https://shopify.dev/api/liquid/filters/pluralize)   | Produit la version singulière ou plurielle d'une chaîne de caractères en anglais en fonction de la valeur d'un nombre.      | ⛔ Non    |
| [précéder](https://shopify.dev/api/liquid/filters/prepend)     | Ajoute des caractères à une chaîne de caractères.      | ✅ Oui   |
| [supprimer](https://shopify.dev/api/liquid/filters/remove)      | Supprime toutes les occurrences d'une sous-chaîne d'une chaîne de caractères.       | ✅ Oui   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Supprime uniquement la première occurrence d'une sous-chaîne d'une chaîne de caractères.      | ✅ Oui   |
| [remplacer](https://shopify.dev/api/liquid/filters/replace)        | Remplace toutes les occurrences d'une chaîne de caractères par une sous-chaîne.   | ✅ Oui   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Remplace la première occurrence d'une chaîne de caractères par une sous-chaîne.      | ✅ Oui   |
| [tranche](https://shopify.dev/api/liquid/filters/slice)       | Le filtre de tranche renvoie une sous-chaîne commençant à l'index spécifié.       | ✅ Oui   |
| [diviser](https://shopify.dev/api/liquid/filters/split)  | Le filtre de fractionnement prend en paramètre une sous-chaîne. Le sous-chaîne est utilisé comme délimiteur pour diviser une chaîne de caractères en un tableau.            | ✅ Oui   |
| [bande](https://shopify.dev/api/liquid/filters/strip)   | Supprime les onglets, les espaces et les nouvelles lignes (tous les espaces blancs) des côtés gauche et droit d'une chaîne de caractères.                                                                                                    | ✅ Oui   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Supprime les onglets, les espaces et les nouvelles lignes (tous les espaces blancs) de la partie gauche d'une chaîne de caractères.    | ⛔ Non    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Supprime les onglets, les espaces et les nouvelles lignes (tous les espaces blancs) de la partie droite d'une chaîne de caractères.          | ⛔ Non    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Supprime toutes les étiquettes HTML d'une chaîne de caractères.        | ✅ Oui   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Supprime les sauts de ligne et les nouvelles lignes d'une chaîne de caractères.        | ✅ Oui   |
| [tronquer](https://shopify.dev/api/liquid/filters/truncate)    | Tronque une chaîne de caractères jusqu'au nombre de caractères transmis en tant que premier paramètre. Un point de suspension (...) est ajouté à la chaîne de caractères tronquée et est inclus dans le nombre de caractères.    | ✅ Oui   |
| [mots tronconiques](https://shopify.dev/api/liquid/filters/truncatewords)   | Tronque une chaîne de caractères jusqu'au nombre de mots transmis en premier paramètre. Un point de suspension (...) est ajouté à la chaîne de caractères tronquée.    | ✅ Oui   |
| [cas de remontée](https://shopify.dev/api/liquid/filters/upcase)   | Convertit une chaîne de caractères en majuscules.      | ✅ Oui   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtres supplémentaires

Les filtres généraux suivants ont de nombreuses fonctions, y compris le formatage ou la conversion de contenu.

| Filtre                | Description                                                                                                                      | Soutenu |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date)           | Convertit un horodatage en un autre format de date. Pour plus d'informations, reportez-vous à la section [Filtre de date](#date-filter).         | ✅ Oui   |
| [par défaut](https://shopify.dev/api/liquid/filters/default)        | Définit une valeur par défaut pour toute variable sans valeur assignée. Peut être utilisé avec des chaînes, des tableaux et des hachages.      | ✅ Oui   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formate une adresse pour imprimer les éléments de l'adresse dans l'ordre de leur localisation.        | ⛔ Non    |
| [mettre en évidence](https://shopify.dev/api/liquid/filters/highlight)      | Enveloppe les tags à l'intérieur des résultats de recherche avec une étiquette HTML `<strong>` avec la classe highlight s'ils correspondent aux termes de recherche soumis. | ⛔ Non    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous trouverez d'autres filtres pris en charge, tels que les filtres d'encodage et d'URL, sur notre page [Filtres avancés]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Filtre de date {#date-filter}

Le filtre `date` peut être utilisé pour convertir un horodatage dans un format de date différent. Vous pouvez passer des paramètres au filtre `date` pour reformater l'horodatage. Pour des exemples de ces paramètres, reportez-vous à [strfti.me](http://www.strfti.me/).

Par exemple, disons que la valeur de `date_attribute` est l'horodatage `2021-06-03 17:13:41 UTC`.

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

Outre les options de formatage de `strftime`, Braze prend également en charge la conversion d'un horodatage en heure Unix à l'aide du filtre de date `%s`. Par exemple, pour obtenir le site `date_attribute` en temps Unix :

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