---
nav_title: Utilisation du liquide
article_title: "Cas d'utilisation des liquides et aperçu"
page_order: 0
description: "Cet article de référence donne un aperçu des cas d'utilisation courants de Liquid et explique comment inclure les étiquettes Liquid dans vos messages."
search_rank: 2
---

# ![cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"} Utilisation de liquides

> Cet article montre comment vous pouvez utiliser une variété d'attributs d'utilisateur pour insérer dynamiquement des informations personnelles dans votre envoi de messages.

Liquid est un langage de template open-source développé par Shopify et écrit en Ruby. Vous pouvez l'utiliser dans Braze pour intégrer les données du profil utilisateur dans vos messages et personnaliser ces données. Par exemple, vous pouvez utiliser les étiquettes Liquid pour créer des messages conditionnels, comme l'envoi d'offres différentes en fonction de la date anniversaire de l'abonnement d'un utilisateur. En outre, les filtres peuvent manipuler les données, par exemple en formatant la date d'inscription d'un utilisateur à partir d'un horodatage dans un format plus lisible, tel que "15 janvier 2022". Pour plus de détails sur la syntaxe Liquid et ses possibilités, reportez-vous à la section [Tags de personnalisation pris en charge.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

## Comment cela fonctionne-t-il ?

Les étiquettes Liquid agissent comme des marqueurs substitutifs dans vos messages qui peuvent tirer des informations consenties du compte de votre utilisateur et permettre la personnalisation et des pratiques de messagerie pertinentes.

Dans le bloc suivant, vous pouvez voir qu'il y a une double utilisation d'une étiquette Liquid pour appeler le prénom de l'utilisateur, ainsi qu'une étiquette par défaut dans l'événement où un utilisateur n'aurait pas son prénom enregistré.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Pour un utilisateur nommé Janet Doe, le message apparaîtra comme suit :

```
Hi Janet, thanks for using the App!
```

Ou bien...

```
Hi Valued User, thanks for using the App!
```

## Valeurs prises en charge à remplacer

Les valeurs suivantes peuvent être substituées dans un message, en fonction de leur disponibilité :

- [Informations de base sur l'utilisateur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) (par exemple, `first_name`, `last_name`, `email_address`)
- [Attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)
    - [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#liquid-templating)
- [Propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- [Informations sur l'appareil le plus récemment utilisé]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information)
- [Informations sur l'appareil cible]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information)

Vous pouvez également extraire du contenu directement d'un serveur web grâce au [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) de Braze.

{% alert important %}
Braze prend actuellement en charge Liquid jusqu'à et y compris Liquid 5 de Shopify.
{% endalert %}

## Utilisation du liquide

Grâce aux [étiquettes Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), vous pouvez rehausser la qualité de vos messages en les enrichissant d'une touche de personnalisation. 

### Syntaxe liquide

Liquid suit une structure spécifique, ou syntaxe, que vous devez garder à l'esprit lorsque vous créez une personnalisation dynamique. Voici quelques règles de base à garder à l'esprit :

1. **Utilisez des guillemets droits dans Braze :** Il existe une différence entre les guillemets frisés ('**')** et les guillemets droits ('**').** Utilisez des guillemets droits ('**')** dans votre liquide dans Braze. Vous pouvez voir des guillemets frisés lorsque vous copiez et collez à partir de certains éditeurs de texte, ce qui peut causer des problèmes dans votre Liquid. Si vous saisissez les devis directement dans le tableau de bord de Braze, tout ira bien !
2. **Les supports sont livrés par paires :** Chaque parenthèse doit à la fois ouvrir et fermer **{ }.** Veillez à utiliser des parenthèses curieuses !
3. **Les déclarations sont présentées par paires :** Pour chaque `if`, vous avez besoin d'un `endif` pour indiquer que la déclaration `if` est terminée.

#### Attributs par défaut et attributs personnalisés

{% raw %}

Si vous incluez le texte suivant dans votre message : `{{${first_name}}}` le prénom de l'utilisateur (tiré du profil de l'utilisateur) sera substitué lors de l'envoi du message. Vous pouvez utiliser le même format avec d'autres attributs par défaut de l'utilisateur.

Si vous souhaitez utiliser la valeur d'un attribut personnalisé, vous devez ajouter l'espace de noms "custom_attribute" à la variable. Par exemple, pour utiliser un attribut personnalisé nommé "zip code", vous devez inclure `{{custom_attribute.${zip code}}}` dans votre message.

### Insérer des étiquettes

Vous pouvez insérer des tags en tapant deux crochets ouverts `{{` dans n'importe quel message, ce qui déclenchera une fonctionnalité d'autocomplétion qui continuera à se mettre à jour au fur et à mesure que vous tapez. Vous pouvez même sélectionner une variable à partir des options qui apparaissent au fur et à mesure que vous tapez.

Si vous utilisez un tag personnalisé, vous pouvez copier et coller l'étiquette dans le message de votre choix.

#### Exceptions pour les doubles crochets

Si vous utilisez une étiquette à l'intérieur d'une autre étiquette Liquid, comme `{% assign %}` ou `{% if %}`, vous pouvez utiliser des doubles crochets ou ne pas utiliser de crochets. Ce n'est que lorsque l'étiquette est isolée qu'elle doit être placée entre doubles crochets. Pour plus de simplicité, vous pouvez toujours utiliser des doubles crochets. 

Les étiquettes suivantes sont toutes correctes :

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

Si vous utilisez Liquid dans vos messages e-mail, veillez à le faire :

1. Insérez-le en utilisant l'éditeur HTML plutôt que l'éditeur classique. L'éditeur classique peut analyser le liquide comme du texte en clair. Par exemple, le Liquid analyserait comme {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} au lieu de templer le prénom de l'utilisateur.
2. Placez le code Liquid uniquement à l'intérieur de l'étiquette `<body>`. Si vous le placez en dehors de cette étiquette, vous risquez d'obtenir un rendu incohérent lors de la réception/distribution.

{% endalert %}

### Insérer des variables préformatées

Vous pouvez insérer des variables préformatées avec des valeurs par défaut dans la fenêtre modale/boîte de dialogue **Ajouter une personnalisation** située à proximité de n'importe quel champ de texte modèle.

\![La fenêtre modale/boîte de dialogue de personnalisation qui apparaît après avoir sélectionné insérer une personnalisation. La fenêtre modale comporte des champs pour le type de personnalisation, l'attribut, la valeur par défaut facultative, et affiche un aperçu de la syntaxe du liquide.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

La fenêtre modale insère Liquid avec la valeur par défaut que vous avez spécifiée à l'endroit où se trouvait votre curseur. Le point d'insertion est également spécifié par la boîte de prévisualisation, qui contient le texte avant et après. Si un bloc de texte est surligné, le texte surligné sera remplacé.

Un GIF de la modale Ajouter une personnalisation qui montre l'utilisateur insérant "compagnon de route" comme valeur par défaut, et la modale remplaçant le texte en surbrillance "nom" dans le compositeur par l'extrait de code Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

### Attribution de variables

{% raw %}
Certaines opérations dans Liquid exigent que vous stockiez la valeur que vous souhaitez manipuler sous la forme d'une variable. C'est souvent le cas si votre déclaration Liquid comprend plusieurs attributs, propriétés d'événement ou filtres.

Par exemple, supposons que vous souhaitiez additionner deux entiers de données personnalisées. 

#### Exemple de liquide incorrect

Vous ne pouvez pas utiliser :

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Ce Liquid ne fonctionne pas parce que vous ne pouvez pas référencer plusieurs attributs en une seule ligne ; vous devez affecter une variable à au moins l'une de ces valeurs avant que les fonctions mathématiques n'interviennent. L'ajout de deux attributs personnalisés nécessiterait deux lignes de Liquid : une pour affecter l'attribut personnalisé à une variable et une pour effectuer l'ajout.

#### Exemple de liquide correct

Vous pouvez utiliser :

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutoriel : Utiliser des variables pour calculer un solde

Calculons le solde actuel d'un utilisateur en additionnant le solde de sa carte cadeau et le solde de ses récompenses :

Tout d'abord, utilisez l'étiquette `assign` pour remplacer l'attribut personnalisé de `current_rewards_balance` par le terme "balance". Cela signifie que vous avez maintenant une variable nommée `balance`, que vous pouvez manipuler.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Ensuite, nous utiliserons le filtre `plus` pour combiner le solde de la carte cadeau de chaque utilisateur avec son solde de récompenses, signifié par `{{balance}}`.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
Vous vous retrouvez à assigner les mêmes variables dans chaque message ? Au lieu d'écrire la balise `assign` à plusieurs reprises, vous pouvez enregistrer cette balise en tant que bloc de contenu et la placer en haut de votre message.

1. [Créez un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Donnez un nom à votre bloc de contenu (sans espaces ni caractères spéciaux).
3. Sélectionnez **Modifier** en bas de la page.
4. Saisissez vos étiquettes `assign`.

Tant que le bloc de contenu se trouve en haut de votre message, chaque fois que la variable est insérée dans votre message en tant qu'objet, elle fera référence à l'attribut personnalisé que vous avez choisi !
{% endalert %}

