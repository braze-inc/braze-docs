---
nav_title: "Logique conditionnelle d'envoi des messages"
article_title: "Logique conditionnelle de l'envoi de messages liquides"
page_order: 6
description: "Cet article de référence explique comment les tags peuvent et doivent être utilisés dans vos campagnes."

---

# Logique conditionnelle d'envoi des messages

> Les [étiquettes](https://docs.shopify.com/themes/liquid-documentation/tags) vous permettent d'inclure une logique de programmation dans vos campagnes d'envoi de messages. Les tags peuvent être utilisés pour l'exécution d'instructions conditionnelles ainsi que pour des cas d'utilisation avancés, comme l'affectation de variables ou l'itération dans un bloc de code. <br><br>Cette page explique comment les tags peuvent et doivent être utilisés, par exemple comment prendre en compte les valeurs d'attributs null, nil et blank, et comment référencer des attributs personnalisés.

## Tags de mise en forme

{% raw %}
Une étiquette doit être enveloppée dans `{% %}`.
{% endraw %}

Pour vous faciliter un peu la vie, Braze a inclus un formatage en couleur qui s'activera en vert et en violet si vous avez correctement formaté votre syntaxe Liquid. La mise en forme verte peut aider à identifier les tags, tandis que la mise en forme violette met en évidence les zones qui contiennent de la personnalisation.

Si vous avez des difficultés à utiliser l'envoi conditionnel de messages, essayez de rédiger la syntaxe conditionnelle avant d'insérer vos attributs personnalisés et d'autres éléments Liquid.

Par exemple, ajoutez d'abord ce qui suit dans le champ du message :  
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Assurez-vous qu'il apparaît en vert, puis remplacez le `X` par le contenu liquide ou connecté de votre choix en utilisant le `+` bleu dans le coin du champ de message, et le `0` par la valeur que vous souhaitez.
<br><br>
Ensuite, ajoutez les variations de votre message au fur et à mesure que vous en avez besoin entre les conditionnels de `else`:
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

Vous avez la possibilité d'inclure une déclaration `{% else %}` dans votre logique conditionnelle. Si aucune des conditions que vous avez définies n'est remplie, l'instruction `{% else %}` spécifie le message qui doit être envoyé. Dans cet exemple, nous choisissons par défaut l'anglais si la langue de l'utilisateur n'est ni l'anglais, ni l'espagnol, ni le chinois.

#### `endif`

L'étiquette `{% endif %}` indique que vous avez terminé votre logique conditionnelle. Vous devez inclure l'étiquette `{% endif %}` dans tout message comportant une logique conditionnelle. Si vous n'incluez pas d'étiquette `{% endif %}` dans votre logique conditionnelle, vous obtiendrez une erreur car Braze ne pourra pas analyser votre message.

### Tutoriel : Fournir un contenu basé sur l'emplacement/localisation

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

{% details Full Liquid code %}

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

## Prise en compte des valeurs d'attributs null, nil et blank

La logique conditionnelle est un moyen utile de prendre en compte les valeurs d'attributs qui ne sont pas définies dans les profils utilisateurs.

### Valeurs d'attributs nulles et nuls

Une valeur nulle se produit lorsque la valeur d'un attribut personnalisé n'a pas été définie. Par exemple, un utilisateur qui n'a pas encore défini son prénom n'aura pas de prénom enregistré dans Braze.

Dans certaines circonstances, vous souhaiterez peut-être envoyer un message complètement différent aux utilisateurs qui ont un prénom et à ceux qui n'en ont pas.

L'étiquette suivante vous permet de spécifier un message pour les utilisateurs dont l'attribut "prénom" est nul :

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %} 

Un exemple de message dans le tableau de bord de Braze, utilisant un attribut null 'first name'.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Notez qu'une valeur d'attribut null n'est pas strictement associée à un type de valeur (par exemple, une chaîne "null" est la même chose qu'un tableau "null"). Dans l'exemple ci-dessus, la valeur d'attribut null fait référence à un prénom non défini, qui serait une chaîne.

{% endraw %}

### Valeurs d'attributs vides

Une valeur vide apparaît lorsque l'attribut d'un profil utilisateur n'est pas défini, est défini avec une chaîne de caractères (` `) ou est défini comme `false`. Les valeurs vides doivent être vérifiées avant les autres variables afin d'éviter une erreur de traitement du liquide.

L'étiquette suivante vous permet de spécifier un message pour les utilisateurs dont l'attribut "prénom" est vide.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %} 

## Référencement d'attributs personnalisés

Après avoir [créé des attrib]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)uts personnalisés, vous pouvez y faire référence dans vos envois de messages liquides.

Lorsque vous utilisez la logique conditionnelle, vous devez connaître le type de données de l'attribut personnalisé afin de vous assurer que vous utilisez la bonne syntaxe. Dans la page **Attributs personnalisés** du tableau de bord, recherchez le type de données associé à votre attribut personnalisé, puis référez-vous aux exemples suivants listés pour chaque type de données.

\![Sélection d'un type de données pour un attribut personnalisé. L'exemple fourni montre un attribut Favorite_Category avec une chaîne de caractères comme type de données.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Les chaînes de caractères et les tableaux doivent être entourés d'apostrophes droites, tandis que les booléens et les entiers n'ont jamais d'apostrophes.
{% endalert %}

#### Booléen

Les [booléens]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans) sont des valeurs binaires et peuvent avoir pour valeur `true` ou `false`, par exemple `registration_complete: true`. Les valeurs booléennes ne sont pas entourées d'apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Nombre

Les [nombres]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers) sont des valeurs numériques, qui peuvent être des entiers ou des flottants. Par exemple, un utilisateur peut avoir `shoe_size: 10` ou `levels_completed: 287`. Les valeurs numériques ne sont pas entourées d'apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Vous pouvez également utiliser d'autres [opérateurs de base](https://shopify.dev/docs/themes/liquid/reference/basics/operators) tels que moins que (<) ou plus grand que (>) pour les nombres entiers :

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### Chaîne de caractères

Une [chaîne de caractères]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings) est composée de caractères alphanumériques et stocke une donnée concernant votre utilisateur. Par exemple, vous pouvez avoir `favorite_color: red` ou `phone_number: 3025981329`. Les valeurs chaînes de caractères doivent être entourées d'apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Pour les chaînes de caractères, vous pouvez utiliser à la fois "==" et "contains" dans votre liquide.

#### Réseau

Un [tableau]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays) est une liste d'informations sur votre utilisateur. Par exemple, un utilisateur peut avoir `last_viewed_shows: stranger things, planet earth, westworld`. Les valeurs du tableau doivent être entourées d'apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Pour les tableaux, vous devez utiliser "contains" et ne pouvez pas utiliser "==". 

#### L'heure

L'heure à laquelle un événement s'est produit. Les valeurs [temporelles]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) doivent être assorties d'un [filtre mathématique]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters) pour être utilisées dans la logique conditionnelle.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


