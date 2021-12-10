---
nav_title: Logique de la messagerie conditionnelle
article_title: Logique de Messagerie Liquide Conditionnelle
page_order: 6
description: "Les balises vous permettent d'inclure la logique de programmation dans vos campagnes de messagerie. Cet article de référence couvre comment les tags peuvent et doivent être utilisés dans vos campagnes."
---

# La logique de messagerie conditionnelle (tags)

[Les balises][7] vous permettent d'inclure la logique de programmation dans vos campagnes de messagerie.

{% raw %}
Un tag doit être enveloppé dans `{% %}`.
{% endraw %}

Les balises peuvent être utilisées pour exécuter des instructions conditionnelles ainsi que pour des cas d'utilisation avancés, comme l'assignation de variables ou l'itération à travers un bloc de code.

{% alert tip %}
Pour vous faciliter un peu la vie, Braze a inclus le formatage de couleur qui s'activera en vert et violet si vous formatez correctement votre syntaxe Liquid. <br><br> Si vous avez du mal à utiliser la messagerie conditionnelle, essayez d'écrire la syntaxe conditionnelle avant d'insérer vos attributs personnalisés et d'autres éléments Liquid. <br><br> Par exemple, ajoutez d'abord ce qui suit dans le champ de message :
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Veillez à ce que les points forts soient en vert, puis remplacez le `X` avec le Liquid ou le Contenu Connecté de votre choix en utilisant le bleu `+` dans le coin du champ message, et le `0` avec la valeur désirée. <br><br> Ensuite, ajoutez les variations de votre message comme vous en avez besoin entre les conditions `else`:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Merci d'avoir acheté ! Voici encore 10% de réduction !
{% else %}
Achetez maintenant ! 5% de réduction vous convaincraient-ils?
{% endif %}
```
{% endraw %}
{% endalert %}

## Logique conditionnelle

Vous pouvez inclure de nombreux types de [logique intelligente dans les messages][1] — un exemple est une instruction conditionnelle. Voir l'exemple suivant qui utilise [conditions][8] pour internationaliser une campagne :
{% raw %}

```liquid
{% if ${language} == 'fr' %}
Ceci est un message en anglais du Brésil !
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
<unk> <unk> <unk> <unk> <unk> <unk> <unk> Braze<unk> 中文<unk> <unk> い
{% else %}
Ceci est un message du Brésil ! Cela va aller à tous ceux qui ne correspondent pas aux autres langues spécifiées !
{% endif %}
```

### Exemple étape par étape

Dans cet exemple, nous utilisons des balises avec des instructions "si", "elsif" et "else" pour fournir du contenu internationalisé.

```liquid
{% if ${language} == 'fr' %}
Ceci est un message en anglais du Brésil !
```
Si la langue du client est l'anglais, la première condition est remplie et le client recevra un message en anglais.

```liquid
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
```

Vous pouvez spécifier autant d'instructions conditionnelles que vous le souhaitez- les conditions suivantes seront vérifiées si les conditions précédentes ne sont pas remplies. Dans cet exemple, si l'appareil d'un client n'est pas configuré en anglais, ce code vérifiera si l'appareil du client est réglé sur l'espagnol ou le chinois. Si l'appareil du client remplit l'une de ces conditions, le client recevra un message dans la langue concernée.

```liquid
{% else %}
Ceci est un message du Brésil ! Cela va aller à tous ceux qui ne correspondent pas aux autres langues spécifiées !
```

Vous avez la possibilité d'inclure une instruction `{% else %}` dans votre logique conditionnelle. Si aucune des conditions que vous avez définies n'est remplie, l'instruction `{% else %}`  spécifie le message qui doit être envoyé. Dans ce cas, nous utilisons par défaut l'anglais si la langue d'un client n'est pas l'anglais, l'espagnol ou le chinois.

```liquid
{% endif %}
```

La balise `{% endif %}`  indique que vous avez terminé votre logique conditionnelle. Vous devez inclure le tag `{% endif %}`  dans n'importe quel message avec une logique conditionnelle. Si vous n'incluez pas une balise `{% endif %}`  dans votre logique conditionnelle, vous obtiendrez une erreur car Braze ne pourra pas analyser votre message.

{% endraw %}

## Comptabilisation des valeurs d'attribut NULL

La logique conditionnelle est un moyen utile de tenir compte des valeurs d'attributs nuls. Une valeur NULL se produit lorsque la valeur d'un attribut personnalisé n'a pas été définie. Par exemple, un utilisateur qui n'a pas encore défini son prénom n'aura pas de prénom dans la base de données de Brase.

Dans certaines circonstances, vous pouvez envoyer un message complètement différent aux utilisateurs qui ont un prénom défini et aux utilisateurs qui n'ont pas de prénom.

Le tag suivant vous permet de spécifier un message pour les utilisateurs avec un attribut null "prénome" :

{% raw %}
```liquid
{% if ${first_name} == vide %}
....
{% endif %}

```
{% endraw %}

!\[NullValues\]\[36\]

## Référencement des attributs personnalisés

Après avoir créé [attributs personnalisés][2] à partir de **Gérer les paramètres** > **Attributs personnalisés**, vous pouvez référencer ces attributs personnalisés dans votre message Liquid.

Lorsque vous utilisez une logique conditionnelle, vous devrez connaître le type de données de l'attribut personnalisé pour vous assurer que vous utilisez la bonne syntaxe. À partir de la page [Attributs personnalisés][4] dans le tableau de bord, rechercher le type de données associé à votre attribut personnalisé, puis référencer les exemples listés ci-dessous pour chaque type de données.

!\[Type de données d'attribut personnalisé\]\[20\]{: style="max-width:80%;"}

{% alert tip %}
Les chaînes de caractères et les tableaux requièrent des apostrophes droits autour d'eux, tandis que les booléens et les entiers n'auront jamais d'apostrophes.
{% endalert %}

#### Boolean

[Les booléens][9] sont des valeurs binaires, et peuvent être réglés à `true` ou `false`, comme `registration_complete : true`. Les valeurs booléennes n'ont pas d'apostrophes autour d'elles.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == vrai %}
```

{% endraw %}

#### Numéros

[Nombres][10] sont des valeurs numériques, qui peuvent être des entiers ou des nombres flottants. Par exemple, un utilisateur peut avoir `shoe_size: 10` ou `levels_completed: 287`. Les valeurs de nombre n'ont pas d'apostrophes autour d'elles.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Vous pouvez également utiliser d'autres [opérateurs de base](https://shopify.dev/docs/themes/liquid/reference/basics/operators) comme inférieurs à (<) ou supérieurs à (>) pour des entiers :

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### Chaîne de caractères

Une chaîne [][11] est composée de caractères alphanumériques et stocke une partie de données sur votre utilisateur. Par exemple, vous pouvez avoir `favite_color: rouge` ou `phone_number: 3025981329`. Les valeurs de chaîne de caractères doivent avoir des apostrophes autour d'eux.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Pour les cordes, vous pouvez utiliser à la fois "==" ou "contains" dans votre liquide.

#### Tableau

Un tableau [][12] est une liste d'informations sur votre utilisateur. Par exemple, un utilisateur peut avoir `last_viewed_shows : choses inconnues, planète terre, monde occidental`. Les valeurs des tableaux doivent avoir des apostrophes autour d'eux.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contient 'homeland' %}
```

{% endraw %}

Pour les tableaux, vous devez utiliser "contains" et ne pouvez pas utiliser "==".

#### Date et heure

Un timbre de l'heure de la tenue d'un événement. [Instant][13] les valeurs doivent avoir un [filtre mathématique][5] sur elles pour être utilisées en logique conditionnelle.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %} 
```

{% endraw %}
[36]:{% image_buster /assets/img/value_null.png %} [20]: {% image_buster /assets/img_archive/custom_attribute_data_type.png %}

[1]: http://docs.shopify.com/themes/liquid-documentation/basics
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[4]: https://dashboard-01.braze.com/app_settings/app_settings/custom_attributes/ "Custom Attributes"
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#math-filters
[7]: https://docs.shopify.com/themes/liquid-documentation/tags
[8]: http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags "Control Flow Tags"
[9]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#booleans
[10]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#numbers
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#strings
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[12]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#arrays
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time
