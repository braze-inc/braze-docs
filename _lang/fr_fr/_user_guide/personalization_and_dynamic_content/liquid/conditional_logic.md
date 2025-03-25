---
nav_title: Logique de messagerie conditionnelle
article_title: Logique de messagerie conditionnelle Liquid
page_order: 6
description: "Le présent article de référence couvre la manière dont les balises peuvent être utilisées dans vos campagnes."

---

# Logique de messagerie conditionnelle

> Les [tags][7] vous permettent d'inclure une logique de programmation dans vos campagnes de communication. Les balises peuvent être utilisées pour exécuter des relevés conditionnels ainsi que pour des cas d’utilisation avancés, comme l’attribution de variables ou l’itération par un bloc de code. <br><br>Cette page explique comment les tags peuvent et doivent être utilisés, par exemple comment prendre en compte les valeurs d'attributs null, nil et blank, et comment référencer des attributs personnalisés.

## Tags de mise en forme

{% raw %}
Une balise doit être enveloppée dans `{% %}`.
{% endraw %}

{% alert tip %}
Pour faciliter votre vie, Braze a inclus un formatage de couleurs qui s’activera en vert et violet si vous avez correctement formaté votre syntaxe Liquid. Le formatage vert peut aider à identifier les balises, tandis que le formatage violet met en évidence les zones qui contiennent une personnalisation.
<br><br>
Si vous rencontrez des difficultés à utiliser des messages conditionnels, essayez d’écrire la syntaxe conditionnelle avant d’insérer vos attributs personnalisés et autres éléments de Liquid.
<br><br>
Par exemple, ajoutez les éléments suivants dans le champ de message :  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Assurez-vous qu’il est en vert, puis remplacez le `X` avec le Liquid de votre choix ou le contenu connecté en utilisant le bleu `+` dans l’angle du message, et `0` avec la valeur souhaitée.
<br><br>
Ajoutez ensuite vos variations de message selon vos besoins entre les conditions `else` :
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}
{% endalert %}

## Logique conditionnelle

Vous pouvez inclure de nombreux types de [logique intelligente dans les messages][1], comme une instruction conditionnelle. Voir l'exemple suivant qui utilise des [instructions conditionnelles][8] pour internationaliser une campagne :
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Exemple étape par étape

Dans cet exemple, nous utilisons des balises avec des énoncés « if », « elsif » et « else » pour fournir du contenu internationalisé.

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
```
Si la langue de l'utilisateur est l'anglais, la première condition est remplie et l'utilisateur recevra un message en anglais.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

Vous pouvez spécifier autant d'instructions conditionnelles que vous le souhaitez. Les conditions suivantes seront vérifiées si les conditions précédentes ne sont pas remplies. Dans cet exemple, si l'appareil de l'utilisateur n'est pas réglé sur l'anglais, ce code vérifiera si l'appareil de l'utilisateur est réglé sur l'espagnol ou le chinois. Si l'appareil de l'utilisateur remplit l'une de ces conditions, l'utilisateur recevra un message dans la langue concernée.

```liquid
{% else %}
This is a message from Braze! This is going to go to anyone who didn't match the other specified languages!
```

Vous avez la possibilité d’inclure une instruction `{% else %}` dans votre logique conditionnelle. Si aucune des conditions que vous spécifiez n’est remplie, l’instruction `{% else %}` détermine le message à envoyer. Dans ce cas, nous choisissons par défaut l'anglais si la langue de l'utilisateur n'est ni l'anglais, ni l'espagnol, ni le chinois.

```liquid
{% endif %}
```

L'étiquette `{% endif %}` indique que vous avez terminé votre logique conditionnelle. Vous devez inclure l'étiquette `{% endif %}` dans tout message comportant une logique conditionnelle. Si vous n'incluez pas d'étiquette `{% endif %}` dans votre logique conditionnelle, vous obtiendrez une erreur car Braze ne pourra pas analyser votre message.

{% endraw %}

## Prise en compte des valeurs d'attribut nulles, nil et vides

La logique conditionnelle est un moyen utile de tenir compte des valeurs d'attributs qui ne sont pas définies dans les profils des utilisateurs.

### Valeurs d'attribut nulles et nil

Une valeur nulle se produit lorsque la valeur d'un attribut personnalisé n'a pas été définie. Par exemple, un utilisateur qui n'a pas encore défini son prénom n'aura pas de prénom enregistré dans Braze.

Dans certaines circonstances, vous souhaiterez peut-être envoyer un message complètement différent aux utilisateurs qui ont un prénom et à ceux qui n'en ont pas.

La balise suivante vous permet de spécifier un message pour les utilisateurs ayant un attribut  « prénom »  nul.

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

![Un exemple de message dans le tableau de bord de Braze, utilisant un attribut null 'first name'.][36]{: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Notez qu'une valeur d'attribut nulle n'est pas strictement associée à un type de valeur (par exemple, une chaîne "nulle" est la même qu'un tableau "nul"), donc dans l'exemple ci-dessus, la valeur d'attribut nulle fait référence à un prénom non défini, qui serait une chaîne.

{% endraw %}

### Valeurs d'attributs vides

Une valeur vide se produit lorsque l'attribut sur un profil utilisateur n'est pas défini, est défini avec une chaîne d'espaces (` `) ou est défini comme `false`. Les valeurs vides doivent être vérifiées avant les autres variables pour éviter une erreur de traitement Liquid.

Le tag suivant vous permet de spécifier un message pour les utilisateurs qui ont un attribut "prénom" vide.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## Référencer des attributs personnalisés

Après avoir [créé des attributs personnalisés][2], vous pouvez faire référence à ces attributs personnalisés dans votre messagerie Liquid.

Lorsque vous utilisez une logique conditionnelle, vous devez connaître le type de données de l’attribut personnalisé pour vous assurer que vous utilisez la syntaxe correcte. À partir de la page **Attributs personnalisés** dans le tableau de bord, recherchez le type de données associé à votre attribut personnalisé, puis consultez les exemples suivants répertoriés pour chaque type de données.

![Sélection d’un type de données pour un attribut personnalisé. L'exemple fourni montre un attribut de type Favorite_Category avec des données de type chaîne de caractères.][20]{: style="max-width:80%;"}

{% alert tip %}
Les chaînes de caractères et les baies nécessitent des apostrophes droites autour de eux, tandis que les booléens et les entiers n’auront jamais d’apostrophes.
{% endalert %}

#### Valeur booléenne

Les [booléens][9] sont des valeurs binaires et peuvent être définis sur `true` ou `false`, comme `registration_complete: true`. Les valeurs booléennes ne sont pas entourées d’apostrophes..

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Nombre

Les [nombres][10] sont des valeurs numériques, qui peuvent être des entiers ou des floats. Par exemple, un utilisateur peut `shoe_size: 10` ou `levels_completed: 287`. Les chiffres ne sont pas entourés d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Vous pouvez également utiliser d'autres [opérateurs de base](https://shopify.dev/docs/themes/liquid/reference/basics/operators), tels que inférieur à (<) ou supérieur à (>) pour les nombres entiers :

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### Chaîne de caractères

Une [chaîne de caractères][11] est composée de caractères alphanumériques et stocke un élément de données concernant votre utilisateur. Par exemple, vous pourriez avoir `favorite_color: red` ou `phone_number: 3025981329`. Les valeurs de chaîne de caractères doivent être entourées d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Pour les chaînes de caractères, vous pouvez utiliser « == » ou « contient » dans votre Liquid.

#### Tableau

Un [tableau][12] est une liste d'informations sur votre utilisateur. Par exemple, un utilisateur peut avoir `last_viewed_shows: stranger things, planet earth, westworld`. Les valeurs de baie doivent être entourées d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Pour les baies, vous devez utiliser « contains » et ne pas utiliser « == ». 

#### Date

Un horodatage du moment où un événement a eu lieu. [Temps][13] les valeurs doivent avoir un [filtre mathématique][5] sur elles pour être utilisées dans la logique conditionnelle.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


[36]:{% image_buster /assets/img/value_null.png %}
Il y a [1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
Il y a [7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags « Tags de flux de contrôle »
[9]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time
[20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}
