---
nav_title: Réglage des valeurs par défaut
article_title: Réglage des valeurs liquides par défaut
page_order: 5
description: "Définir les valeurs par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages."
---

# Réglage des valeurs par défaut

{% raw %}

Définir les valeurs par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages. Les valeurs par défaut peuvent être ajoutées en spécifiant un [Filtre liquide][3] (utiliser `|` pour distinguer le filtre en ligne, comme indiqué ci-dessous) avec le nom "default."

```
| par défaut : 'Insérer votre valeur par défaut désirée ici'
```

Si une valeur par défaut n'est pas fournie et que le champ est manquant ou non défini sur l'utilisateur, le champ sera vide dans le message.

L'exemple ci-dessous montre la syntaxe correcte pour ajouter une valeur par défaut. Dans ce cas, les mots "Utilisateur Valeur" remplaceront l'attribut `{{ ${first_name} }}` si le champ `prénom` d'un utilisateur est vide ou indisponible.

```liquid
Bonjour {{ ${first_name} | par défaut: 'Utilisateur valué' }}, merci d'utiliser l'application !
```

Pour un utilisateur nommé Janet Doe, le message apparaît à l'utilisateur comme :

```
Bonjour Janet, merci d'utiliser l'application !
```

Ou...

```
Utilisateur Hi Valued, merci d'utiliser l'application!
```

{% endraw %}
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}

[3]: http://docs.shopify.com/themes/liquid-documentation/filters
