---
nav_title: Paramétrage des valeurs par défaut
article_title: Paramétrage des valeurs par défaut de Liquid
page_order: 5
description: "Cet article de référence explique comment définir les valeurs de secours par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages."

---

# Paramétrage des valeurs par défaut

{% raw %}

Définissez les valeurs de secours par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages. Les valeurs par défaut peuvent être ajoutées en spécifiant un [Filtre Liquid][3] (utilisez `|` pour distinguer le filtre en ligne, comme illustré), avec le nom « par défaut »."

```
| default: 'Insert Your Desired Default Here'
```

Si une valeur par défaut n’est pas fournie et que le champ est manquant ou non défini sur l’utilisateur, le champ sera vide dans le message.

L’exemple suivant montre la syntaxe correcte pour ajouter une valeur par défaut. Dans ce cas, les mots « Cher utilisateur » remplacent l’attribut `{{ ${first_name} }}` si un utilisateur `first_name` est vide ou indisponible.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Pour un utilisateur nommé Janet Doe, le message s’affiche comme suit :

```
Hi Janet, thanks for using the App!
```

OU

```
Hi Valued User, thanks for using the App!
```

{% endraw %}

[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
