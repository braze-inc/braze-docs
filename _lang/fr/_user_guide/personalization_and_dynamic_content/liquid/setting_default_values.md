---
nav_title: Paramétrage des valeurs par défaut
article_title: Paramétrage des valeurs par défaut de Liquid
page_order: 5
description: "Définissez les valeurs de secours par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages."

---

# Paramétrage des valeurs par défaut

{% raw %}

Définissez les valeurs de secours par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages. Des valeurs par défaut peuvent être ajoutées en spécifiant un [Liquid Filter][3] (utilsez `|` pour différencier le filtre, comme ci-dessous) avec le nom "default."

```
| default: 'Insérez ici votre valeur par défaut souhaitée.'
```

Si une valeur par défaut n’est pas fournie et que le champ est manquant ou non défini sur l’utilisateur, le champ sera vide dans le message.

L’exemple suivant montre la syntaxe correcte pour ajouter une valeur par défaut. Dans ce cas, les mots « Cher utilisateur » remplacent l’attribut `{{ ${first_name} }}`   si le champ « first_name » (Prénom) d’un utilisateur  est vide ou indisponible.

```liquid
Bonjour {{ ${first_name} | default: 'cher utilisateur' }}, merci d’utiliser notre appli !
```

Pour un utilisateur nommé Janet Doe, le message s’affiche comme suit :

```
Bonjour Janet, merci d’utiliser notre appli !
```

Ou...

```
Bonjour cher utilisateur, merci d’utiliser notre appli !
```

{% endraw %}

[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
