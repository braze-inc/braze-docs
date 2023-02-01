---
nav_title: Logique de messagerie conditionnelle
article_title: Logique de messagerie conditionnelle Liquid
page_order: 6
description: "Les balises vous permettent d’inclure la logique de programmation dans vos campagnes de messagerie. Le présent article de référence couvre la manière dont les balises peuvent être utilisées dans vos campagnes."

---

# Logique de messagerie conditionnelle (balises)

Les [balises][7] vous permettent d’inclure la logique de programmation dans vos campagnes de communication.

{% raw %}
Une balise doit être enveloppée dans `{% %}`.. 
{% endraw %}

Les balises peuvent être utilisées pour exécuter des relevés conditionnels ainsi que pour des cas d’utilisation avancés, comme l’attribution de variables ou l’itération par un bloc de code.

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

Assurez-vous qu’il est en vert, puis remplacez le `X`  avec le Liquid de votre choix ou le contenu connecté en utilisant le`+` bleu dans le coin champ du message, et  `0`  comme valeur souhaitée.
<br><br>
Ajoutez ensuite vos variations de message selon vos besoins entre les conditions « else » :
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Merci d’avoir acheté ! Voici encore 10 % de réduction ! 
{% else %}
Achetez maintenant ! Seriez-vous convaincu par 5 % de réduction ? 
{% endif %}
```
{% endraw %}
{% endalert %}

## Logique conditionnelle

Vous pouvez inclure de nombreux types de [logique intelligente dans les messages][1] — un exemple pouvant être un énoncé conditionnel. Voir l’exemple suivant qui utilise les [conditionnels][8] pour internationaliser une campagne :
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
Ceci est un message de Braze ! Il sera envoyé à tous ceux qui ne correspondent pas aux autres  langues spécifiées !
{% endif %}
```

### Exemple étape par étape

Dans cet exemple, nous utilisons des balises avec des instructions "if", "elsif" and "else"  pour fournir du contenu internationalisé.

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
```
Si la langue du client est l'Anglais, la première condition est remplie et le client recevra un message en Anglais.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

Vous pouvez spécifier autant de relevés conditionnels que vous le souhaitez, les conditions suivantes seront vérifiées si les conditions précédentes ne sont pas remplies. Dans cet exemple, si le périphérique d’un client n’est pas défini sur Anglais, ce code vérifiera si le périphérique du client est configuré en espagnol ou en chinois. Si le dispositif du client répond à l’une de ces conditions, le client recevra un message dans la langue correspondante.

```liquid
{% else %}
Ceci est un message de Braze ! Il sera envoyé à tous ceux qui ne correspondent pas aux autres  langues spécifiées !
```

Vous avez la possibilité d’inclure une instruction `{% else %}` dans votre logique conditionnelle. Si aucune des conditions que vous spécifiez n’est remplie, l’instruction `{% else %}`  détermine le message à envoyer. Dans ce cas, nous utilisons par défaut l'Anglais si la langue d'un client n'est pas l'Anglais, l'Espagnol ou le Chinois.

```liquid
{% endif %}
```

La balise `{% endif %}`   indique que vous avez terminé votre logique conditionnelle. Vous devez inclure
la balise `{% endif %}` dans tout message avec une logique conditionnelle. Si vous ne mettez pas de balise {% endif %}`  dans votre logique conditionnelle, vous aurez une erreur car Braze ne pourra pas parser votre message.

{% endraw %}

## Comptabilisation des valeurs d’attributs nulles

La logique conditionnelle est un moyen utile de tenir compte des valeurs d’attribut nulles. Une valeur nulle se produit lorsque la valeur d’un attribut personnalisé n’a pas été définie. Par exemple, un utilisateur qui n’a pas encore défini son prénom n’aura pas de prénom dans la base de données de Braze.

Dans certains cas, vous pouvez envoyer un message complètement différent aux utilisateurs qui ont un premier nom de nom et des utilisateurs qui n’ont pas de prénom configuré.

La balise suivante vous permet de spécifier un message pour les utilisateurs ayant un attribut  « prénom »  nul.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}

```
{% endraw %}

![][36]

{% raw %}
```liquid
{% if ${first_name} == blank %}
Ce sont nos soldes ! Dépêchez-vous : 10 % de réduction sur tous nos articles aujourd’hui seulement !
{% else %}
Bonjour, {{${first_name | default: '  '}}, ce sont nos soldes ! Dépêchez-vous : 10 % de réduction sur tous nos articles aujourd’hui seulement !
{% endif %}
```
{% endraw %}

## Référencer des attributs personnalisés

Après avoir créé des [attributs personnalisés][2] depuis **Manage Settings** > **Attributs personnalisés**, vous pouvez référencer ces attributs personnalisés dans votre envoi de messages Liquid. 

Lorsque vous utilisez une logique conditionnelle, vous devez connaître le type de données de l’attribut personnalisé pour vous assurer que vous utilisez la syntaxe correcte. Dans **Attributs personnalisés** dans le tableau de bord, recherchez le type de données associé à votre attribut personnalisé, puis reportez-vous aux exemples suivants pour chaque type de données.

![Sélection d’un type de données pour un attribut personnalisé. L’exemple présente un attribut de type Catégorie_préférée avec un type de données de chaîne de caractères.][20]{: style="max-width:80%;"}

{% alert tip %}
Les chaînes de caractères et les baies nécessitent des apostrophes droites autour de eux, tandis que les booléens et les entiers n’auront jamais d’apostrophes.
{% endalert %}

#### Booléen

Les [Booléens][9] sont des valeurs binaires et peuvent être définis sur `true` ou `false`, comme `registration_complete: true`. Les valeurs booléennes ne sont pas entourées d’apostrophes..

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### Nombre

Les [Nombres][10] sont des valeurs numériques, qui peuvent être des entiers ou des flottants. Par exemple, un utilisateur peut `shoe_size: 10` ou `levels_completed: 287`. Les chiffres ne sont pas entourés d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Vous pouvez également utiliser [opérateurs de base](https://shopify.dev/docs/themes/liquid/reference/basics/operators) comme inférieur à (<) or greater than (>) pour les entiers :

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### Chaîne de caractères

Une [Chaîne de caractères][11] est composée de caractères alphanumériques et stocke un élément de données sur votre utilisateur. Par exemple, vous pourriez avoir `favorite_color: red` ou `phone_number: 3025981329`. Les valeurs de chaîne de caractères doivent être entourées d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Pour les chaînes de caractères, vous pouvez utiliser « == » ou « contient » dans votre Liquid.

#### Baie

Un [Tableau][12] est une liste d’informations sur votre utilisateur. Par exemple, un utilisateur peut avoir `last_viewed_shows: stranger things, planet earth, westworld`. Les valeurs de baie doivent être entourées d’apostrophes.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Pour les baies, vous devez utiliser « contains » et ne pas utiliser « == ». 

#### Heure

Horodatage du moment où un événement a eu lieu. Les valeurs [Heure][13] doivent disposer d’un [filtre mathématique][5] pour être utilisées dans la logique conditionnelle.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}


[36]:{% image_buster /assets/img/value_null.png %}
[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Balises de flux de contrôle"
[9]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time
[20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}
