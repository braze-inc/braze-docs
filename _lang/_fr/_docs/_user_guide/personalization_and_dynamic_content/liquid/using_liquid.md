---
nav_title: Utilisation de Liquid
article_title: Caisse d'utilisation des liquides et Vue d'ensemble
page_order: 0
description: "Liquid peut élever la personnalisation de vos messages à des hauteurs impressionnantes. Les balises liquides agissent comme des espaces réservés dans vos messages qui peuvent extraire des informations consensuelles à partir du compte de votre utilisateur et permettre la personnalisation et les pratiques de messagerie pertinentes."
---

# Cas d'utilisation des liquides et aperçu

{% raw %}

Il existe une variété d'attributs utilisateur que vous pouvez utiliser pour insérer dynamiquement des informations personnelles dans votre messagerie.

Si vous incluez le texte suivant dans votre message : `{{${first_name}}}`, le prénom de l'utilisateur (tiré du profil de l'utilisateur) sera remplacé lorsque le message sera envoyé. Si vous souhaitez utiliser la valeur d'un attribut personnalisé, vous devez ajouter l'espace de noms "custom_attribute" à la variable. Par exemple, pour utiliser un attribut personnalisé nommé "code zip", vous devez inclure `{{custom_attribute.${zip code}}}` dans votre message.

Les valeurs suivantes peuvent être substituées dans un message, selon leur disponibilité:

- [Informations utilisateur de base][1] (par exemple `prénom`, `nom de famille`, `email_address`)
- [Attributs personnalisés][2]
- [Propriétés personnalisées de l'événement][11]
- [Informations sur l'appareil le plus récemment utilisé][39]
- [Informations sur le périphérique cible][40]

Vous pouvez également extraire du contenu directement depuis un serveur web via la fonctionnalité [Contenu connecté][9] de Braze.
{% endraw %}

{% alert important %}
Braze prend actuellement en charge Liquid jusqu'à __Liquid 3 de Shopify__. Nous ne supportons pas actuellement Liquid 4 et au-delà.
{% endalert %}

## Utilisation de Liquid

{% raw %}

Une fois que vous connaissez les [balises Liquid disponibles][1], l'utilisation de Liquid peut élever la personnalisation de vos messages à des hauteurs impressionnantes. Les balises liquides agissent comme des espaces réservés dans vos messages qui peuvent extraire des informations consensuelles à partir du compte de votre utilisateur et permettre la personnalisation et les pratiques de messagerie pertinentes.

Dans le bloc ci-dessous, vous pouvez voir qu'une double utilisation d'un tag Liquid pour appeler le prénom de l'utilisateur ainsi qu'une balise par défaut dans le cas où un utilisateur ne serait pas enregistré.

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

### Syntaxe des liquides

Liquid suit une structure spécifique, ou syntaxe, que vous devrez garder à l'esprit lorsque vous créez une personnalisation dynamique. Voici quelques règles de base à garder à l'esprit :

1. **Utilisez des guillemets droits en Brésil :** Il y a une différence entre les guillemets bouclés (**'''****et les guillemets droits(** '**). Utilisez des guillemets droits (**''**) dans votre liquide au Brésil. Vous pouvez voir des guillemets bouclés lorsque vous copiez et collez à partir de certains éditeurs de texte, ce qui peut causer des problèmes dans votre Liquid. Si vous saisissez des guillemets dans le tableau de bord de Braze, vous allez très bien!</li>
2 **Des crochets viennent en couples :** Chaque crochet doit à la fois ouvrir et fermer **{ }** Assurez-vous d'utiliser des accolades !
3 **Si les déclarations viennent en paires :** Pour chaque `si`, vous avez besoin d'un `endif` pour indiquer l'instruction `si` est terminée.</ol>

### Insertion de balises

Vous pouvez insérer des balises en tapant `{{` dans n'importe quel message, qui déclenchera une fonction de complétion automatique qui continuera à se mettre à jour pendant que vous tapez. Vous pouvez même sélectionner une variable parmi les options qui apparaissent lorsque vous tapez.

Si vous utilisez un tag personnalisé, vous pouvez copier et coller le tag dans le message que vous voulez.

{% endraw %}

{% alert note %}

Si vous choisissez d'utiliser Liquid dans vos messages électroniques, assurez-vous de :

1. Insérez-le en utilisant l'éditeur HTML par opposition à l'éditeur classique. L'Éditeur Classique peut analyser le Liquide en texte clair.
2. Placez uniquement le code Liquid dans la balise `<body>`. Le placer en dehors de cette balise peut causer un rendu incohérent lors de la livraison.

{% endalert %}

{% raw %}


### Pre-formatted variables

Vous pouvez insérer des variables pré-formatées avec des valeurs par défaut dans la modale "Insérer un attribut de personnalisation" située en haut à droite de n'importe quel champ de texte modèle.

!\[Modal buttons\]\[44\]{: style="max-width:70%;"}

Le modal insérera Liquid avec la valeur par défaut spécifiée au point où se trouvait votre curseur. Le point d'insertion est également spécifié via la zone de prévisualisation, qui a le texte avant et après. Si un bloc de texte est mis en surbrillance, le texte surligné sera remplacé.

!\[Modal\]\[45\]

{% endraw %}

### Attribution de variables

{% raw %}
Certaines opérations dans Liquid nécessitent de stocker la valeur que vous voulez manipuler en tant que variable. C'est souvent le cas si votre requête Liquid inclut plusieurs attributs, propriétés d'événement ou filtres.

Par exemple, disons que vous voulez ajouter deux entiers de données personnalisées ensemble. Vous ne pouvez pas simplement utiliser :

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}} 
```

Ce Liquid ne fonctionne pas car vous ne pouvez pas référencer plusieurs attributs sur une seule ligne; vous devrez assigner une variable à au moins une de ces valeurs avant que les fonctions mathématiques ne se déroulent. Ajouter deux attributs personnalisés nécessiterait deux lignes de Liquid : l'une pour assigner l'attribut personnalisé à une variable, et l'autre pour effectuer l'ajout.

#### Exemple

Par exemple, calculons le solde actuel d'un utilisateur en ajoutant son solde de carte-cadeau et son solde de récompense :

Premièrement, utilisez la balise `assigner` pour sous-situer l'attribut personnalisé de `current_rewards_balance` avec le terme "balance". Cela signifie que vous avez maintenant une variable nommée `balance`, que vous pouvez manipuler.

```liquid
{% balance assignée = {{custom_attribute.${current_rewards_balance}}} %}
```

Ensuite, nous utilisons le filtre `plus` qui combine le solde de la carte-cadeau de chaque utilisateur avec son solde de remises, signifié par `{{balance}}`.

```liquid
{% balance assignée = {{custom_attribute.${current_rewards_balance}}} %}
Vous avez ${{custom_attribute.${giftcard_balance} | plus : {{balance}}}} à dépenser ! 
```
{% endraw %}

{% alert tip %}
Vous vous trouvez à assigner les mêmes variables dans chaque message ? Au lieu d'écrire encore et encore la balise `assigner` vous pouvez enregistrer ce tag en tant que bloc de contenu et le placer en haut de votre message à la place.

1. [Créer un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Donnez un nom à votre Bloc de Contenu (sans espaces ni caractères spéciaux).
3. Cliquez sur **Modifier** au bas de la page.
4. Tapez vos tags `assigner`.

Tant que le bloc de contenu est en haut de votre message, chaque fois que la variable est insérée dans votre message en tant qu'objet, elle fera référence à l'attribut personnalisé que vous avez choisi !
{% endalert %}
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %} [45]: {% image_buster /assets/img_archive/insert_var_shot.png %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[9]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
