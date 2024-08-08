---
nav_title: Utilisation de Liquid
article_title: Scénario d’utilisation et présentation de Liquid
page_order: 0
description: "Cet article de référence fournit un aperçu des cas d’utilisation courants de Liquid et de la manière d’inclure des balises Liquid dans vos messages."
search_rank: 2
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Utilisation de Liquid

{% raw %}

> Il existe plusieurs attributs d’utilisateur à utiliser pour insérer de façon dynamique des informations personnelles dans votre messagerie.

Si vous incluez le texte suivant dans votre message : `{{${first_name}}}`, le prénom de l’utilisateur (tiré du profil de l’utilisateur) sera remplacé lorsque le message est envoyé. Si vous souhaitez utiliser la valeur d’un attribut personnalisé, vous devez ajouter le namespace "custom_attribute" à la variable. Par exemple, pour utiliser un attribut personnalisé nommé « code postal », vous ajoutez `{{custom_attribute.${zip code}}}` à votre message.

Les valeurs suivantes peuvent être remplacées par un message, selon leur disponibilité :

- [Informations de base sur l’utilisateur][1] (par ex., `first_name`, `last_name`, `email_address`)
- [Attributs personnalisés][2]
- [Propriétés de l'événement  personnalisé][11]
- [Informations sur les appareils les plus récemment utilisées][39]
- [Informations sur les appareils ciblés][40]

Vous pouvez également extraire du contenu directement depuis un serveur Web via la fonctionnalité de [Contenu connecté][9] de Braze.
{% endraw %}

{% alert important %}
Braze prend actuellement en charge Liquid jusqu’au et y compris **Liquid 5 de Shopify**.
{% endalert %}

## Utilisation de Liquid

{% raw %}

Une fois que vous connaissez [les Balise Liquid disponibles][1], utiliser Liquid peut améliorer la personnalisation de vos messages de façon impressionnante. Les balises Liquid agissent comme des indicateurs de niveau dans vos messages qui peuvent tirer des informations soumises à consentement sur le compte de votre utilisateur, et permettre la personnalisation et les pratiques de messagerie pertinentes.

Dans le bloc suivant, vous pouvez voir qu’une double utilisation d’une balise Liquid pour appeler le prénom de l’utilisateur, ainsi qu’une balise par défaut si le prénom d’un utilisateur n’est pas enregistré.

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

### Syntaxe en Liquid

Liquid suit une structure ou une syntaxe spécifique que vous devrez garder à l’esprit lorsque vous concevez une personnalisation dynamique. Voici quelques règles de base à garder à l’esprit :

1. **Utilisez des guillemets droits dans Braze :** Il y a une différence entre les guillemets courbes (**‘ ’**) et des guillemets droits (**&#39; &#39;**). Utilisez des guillemets droits (**&#39; &#39;**) dans votre Liquid dans Braze. Vous pouvez voir des guillemets courbes lorsque vous copiez-collez certains éditeurs de texte, ce qui peut entraîner des problèmes dans votre Liquid. Si vous saisissez des guillemets directement dans le tableau de bord de Braze, cela sera parfait !
2. **Les parenthèses fonctionnent en paire :** Chaque parenthèse doit être ouverte et fermée **{ }**. Assurez-vous d’utiliser des parenthèses courbes !
3. **Les instructions « IF » (Si) fonctionnent en paire :** Pour chaque `if`, vous avez besoin d’un `endif` pour indiquer que l’énoncé `if` a pris fin.

### Insertion des balises

Vous pouvez insérer des balises en saisissant deux parenthèses courbes `{{` dans n’importe quel message, ceci déclenchera une fonctionnalité d’achèvement automatique qui continuera à être mise à jour lors de votre saisie. Vous pouvez même sélectionner une variable à partir des options qui s’affichent alors que vous saisissez.

Si vous utilisez une balise personnalisée, vous pouvez copier et coller la balise dans le message que vous souhaitez.

{% endraw %}

{% alert note %}

Si vous choisissez d’utiliser Liquid dans vos e-mails, assurez-vous de :

1. l’insérer à l’aide de l’éditeur HTML, plutôt que de l’éditeur classique. L’éditeur classique peut analyser Liquid comme du texte brut.
2. Placez le code Liquid dans la balise `<body>` uniquement. Le fait de le placer en dehors de cette balise peut entraîner un rendu irrégulier lors de la livraison.

{% endalert %}

{% raw %}


### Variables préformatées

Vous pouvez insérer des variables préformatées avec des valeurs par défaut via le modal « Insérer l’attribut de personnalisation » situé en haut à droite de tout champ de texte modèle.

![Boutons Plus pour insérer des attributs de personnalisation dans les champs de texte qui prennent en charge Liquid dans Braze][44]{: style="max-width:70%;"}

Le modal insère votre valeur par défaut spécifiée dans Liquid à l’endroit où se trouvait votre curseur. Le point d’insertion est également spécifié via la zone d’aperçu, qui a le texte préalable et ultérieur. Si un bloc de texte est mis en surbrillance, le texte mis en surbrillance sera remplacé.

![Ajoutez le modal de personnalisation qui s’affiche après avoir cliqué sur Insérer la personnalisation. Le modal comporte des champs pour le type de personnalisation, l’attribut, la valeur par défaut facultative et affiche un aperçu de la syntaxe Liquid.][45]

{% endraw %}

### Attribution des variables

{% raw %}
Certaines opérations dans Liquid exigent que vous stockiez la valeur que vous souhaitez manipuler comme variable. C’est souvent le cas si votre énoncé Liquid comprend plusieurs attributs, propriétés de l’événement ou filtres.

Supposons par exemple que vous souhaitiez ajouter deux entiers de données personnalisés. Vous ne pouvez pas simplement utiliser :

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Ce Liquid ne fonctionne pas parce que vous ne pouvez pas référencer plusieurs attributs dans une ligne ; vous devez attribuer une variable à au moins une de ces valeurs avant que les fonctions mathématiques aient lieu. L’ajout de deux attributs personnalisés nécessiterait deux lignes de Liquid : l’une pour attribuer l’attribut personnalisé à une variable et l’autre pour l’ajout.

#### Exemple

Supposons que nous voulons calculer le solde actuel d’un utilisateur en ajoutant son solde de carte-cadeau et son solde de récompenses.

Tout d’abord, utilisez la balise `assign` pour remplacer l’attribut personnalisé de `current_rewards_balance` par le terme « solde ». Cela signifie que vous avez maintenant une variable intitulée `balance` que vous pouvez manipuler.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Ensuite, utilisez le filtre `plus` pour combiner le solde de la carte-cadeau de chaque utilisateur avec son solde de récompenses, indiqué par l’élément `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
Vous envoyez les mêmes variables dans chaque message ? Au lieu d’écrire la balise `assign` sans arrêt vous pouvez enregistrer cette balise comme un bloc de contenu et la placer en haut de votre message.

1. [Créer un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Donnez un nom à votre bloc de contenu (aucun espace ni caractère spécial).
3. Cliquez sur **Edit (Modifier)** au bas de la page.
4. Saisissez vos balises `assign`.

Tant que le bloc de contenu est en haut de votre message, chaque fois que la variable est insérée dans votre message comme objet, elle se rapporte à l’attribut personnalisé que vous avez choisi !
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[9]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
