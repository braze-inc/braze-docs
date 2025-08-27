---
nav_title: Logique de messagerie conditionnelle
article_title: Logique de messagerie conditionnelle Liquid
page_order: 6
description: "Le présent article de référence couvre la manière dont les balises peuvent être utilisées dans vos campagnes."

---

# Logique de messagerie conditionnelle

> Les [étiquettes](https://docs.shopify.com/themes/liquid-documentation/tags) vous permettent d'inclure une logique de programmation dans vos campagnes d'envoi de messages. Les balises peuvent être utilisées pour exécuter des relevés conditionnels ainsi que pour des cas d’utilisation avancés, comme l’attribution de variables ou l’itération par un bloc de code. <br><br>Cette page explique comment les tags peuvent et doivent être utilisés, par exemple comment prendre en compte les valeurs d'attributs null, nil et blank, et comment référencer des attributs personnalisés.

## Tags de mise en forme

{% raw %}
Une balise doit être enveloppée dans `{% %}`.
{% endraw %}

Pour faciliter votre vie, Braze a inclus un formatage de couleurs qui s’activera en vert et violet si vous avez correctement formaté votre syntaxe Liquid. Le formatage vert peut aider à identifier les balises, tandis que le formatage violet met en évidence les zones qui contiennent une personnalisation.

Si vous rencontrez des difficultés à utiliser des messages conditionnels, essayez d’écrire la syntaxe conditionnelle avant d’insérer vos attributs personnalisés et autres éléments de Liquid.

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

## Logique conditionnelle

Vous pouvez inclure de nombreux types de [logique intelligente dans les messages](http://docs.shopify.com/themes/liquid-documentation/basics), comme une instruction conditionnelle. L'exemple suivant utilise des [conditionnels](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags) pour internationaliser une campagne :
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

### Tags conditionnels

#### `if` et `elsif`

La logique conditionnelle commence par l'étiquette `if`, qui énonce la première condition à vérifier. Les conditions suivantes utilisent l'étiquette `elsif` et seront vérifiées si les conditions précédentes ne sont pas remplies. Dans cet exemple, si l'appareil de l'utilisateur n'est pas réglé sur l'anglais, ce code vérifiera si l'appareil de l'utilisateur est réglé sur l'espagnol et, en cas d'échec, il vérifiera si l'appareil est réglé sur l'anglais. Si l'appareil de l'utilisateur remplit l'une de ces conditions, l'utilisateur recevra un message dans la langue concernée.

#### `else`

Vous avez la possibilité d’inclure une instruction `{% else %}` dans votre logique conditionnelle. Si aucune des conditions que vous avez définies n'est remplie, l'instruction `{% else %}` spécifie le message qui doit être envoyé. Dans cet exemple, nous choisissons par défaut l'anglais si la langue de l'utilisateur n'est ni l'anglais, ni l'espagnol, ni le chinois.

#### `endif`

L'étiquette `{% endif %}` indique que vous avez terminé votre logique conditionnelle. Vous devez inclure l'étiquette `{% endif %}` dans tout message comportant une logique conditionnelle. Si vous n'incluez pas d'étiquette `{% endif %}` dans votre logique conditionnelle, vous obtiendrez une erreur car Braze ne pourra pas analyser votre message.

### Tutoriel : Fournir un contenu basé sur l'emplacement/localisation

À la fin de ce tutoriel, vous serez en mesure d'utiliser des tags avec des instructions "if", "elsif" et "else" pour diffuser du contenu en fonction de l'emplacement/localisation de l'utilisateur.

1. Commencez par une étiquette `if` pour établir quel message doit être envoyé lorsque la ville de l'utilisateur est New York. Si la ville de l'utilisateur est New York, cette première condition est remplie et l'utilisateur recevra un message spécifiant son identité new-yorkaise.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at your local Sandwich Emperor. 
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2\. Ensuite, utilisez l'étiquette `elseif` pour déterminer quel message doit être envoyé si la ville de l'utilisateur est Los Angeles.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3\. Utilisons une autre étiquette `elseif` pour déterminer quel message doit être envoyé si la ville de l'utilisateur est Chicago.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
```

{: start="4"}
4\. Utilisons maintenant l'étiquette `{% else %}` pour spécifier quel message doit être envoyé si la ville de l'utilisateur n'est ni San Francisco, ni New York, ni Chicago.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5\. Enfin, nous utiliserons l'étiquette `{% endif %}` pour indiquer que notre logique conditionnelle est terminée.

```liquid
{% endif %}
```

{% endraw %}

{% details Code complet du liquide %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal! 
  Get 20% off your next sandwich at our New York location. 
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich! 
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you! 
  Swing by our restaurant and get 20% off your favorite sandwich. 
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal! 
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

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

![Un exemple de message dans le tableau de bord de Braze, utilisant un attribut "prénom" nul.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

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

Après avoir [créé des attrib]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)uts personnalisés, vous pouvez y faire référence dans vos envois de messages liquides.

Lorsque vous utilisez une logique conditionnelle, vous devez connaître le type de données de l’attribut personnalisé pour vous assurer que vous utilisez la syntaxe correcte. À partir de la page **Attributs personnalisés** dans le tableau de bord, recherchez le type de données associé à votre attribut personnalisé, puis consultez les exemples suivants répertoriés pour chaque type de données.

![Sélection d’un type de données pour un attribut personnalisé. L'exemple fourni montre un attribut Favorite_Category avec une chaîne de caractères comme type de données.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Les chaînes de caractères et les baies nécessitent des apostrophes droites autour de eux, tandis que les booléens et les entiers n’auront jamais d’apostrophes.
{% endalert %}

#### Valeur booléenne

Les [booléens]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans) sont des valeurs binaires et peuvent avoir pour valeur `true` ou `false`, par exemple `registration_complete: true`. Les valeurs booléennes ne sont pas entourées d’apostrophes..

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Nombre

Les [nombres]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers) sont des valeurs numériques, qui peuvent être des entiers ou des flottants. Par exemple, un utilisateur peut `shoe_size: 10` ou `levels_completed: 287`. Les chiffres ne sont pas entourés d’apostrophes.

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

Une [chaîne de caractères]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings) est composée de caractères alphanumériques et stocke une donnée concernant votre utilisateur. Par exemple, vous pourriez avoir `favorite_color: red` ou `phone_number: 3025981329`. Les valeurs de chaîne de caractères doivent être entourées d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Pour les chaînes de caractères, vous pouvez utiliser « == » ou « contient » dans votre Liquid.

#### Tableau

Un [tableau]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays) est une liste d'informations sur votre utilisateur. Par exemple, un utilisateur peut avoir `last_viewed_shows: stranger things, planet earth, westworld`. Les valeurs de baie doivent être entourées d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Pour les baies, vous devez utiliser « contains » et ne pas utiliser « == ». 

#### Date

Horodatage du moment où un événement a eu lieu. Les valeurs [temporelles]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) doivent être assorties d'un [filtre mathématique]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters) pour être utilisées dans la logique conditionnelle.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


