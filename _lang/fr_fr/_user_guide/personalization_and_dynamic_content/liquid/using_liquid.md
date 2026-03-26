---
nav_title: Utilisation de Liquid
article_title: Scénario d’utilisation et présentation de Liquid
page_order: 0
description: "Cet article de référence donne un aperçu des cas d'utilisation courants de Liquid et explique comment inclure les étiquettes Liquid dans vos messages."
search_rank: 2
---

# [![Cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"} Utilisation de Liquid

> Cet article explique comment utiliser divers attributs utilisateur pour insérer de manière dynamique des informations personnelles dans vos envois de messages.

Liquid est un langage de modélisation open-source développé par Shopify et écrit en Ruby. Vous pouvez l'utiliser dans Braze pour extraire les données du profil utilisateur dans vos messages et personnaliser ces données. Par exemple, vous pouvez utiliser des étiquettes Liquid pour créer des messages conditionnels, tels que l'envoi d'offres différentes en fonction de la date anniversaire de l'abonnement d'un utilisateur. De plus, les filtres peuvent manipuler les données, par exemple en convertissant la date d'inscription d'un utilisateur d'un horodatage en un format plus lisible, tel que « 15 janvier 2022 ». Pour plus de détails sur la syntaxe Liquid et ses possibilités, reportez-vous à la section [Tags de personnalisation pris en charge.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

## Fonctionnement

Les balises Liquid agissent comme des indicateurs de niveau dans vos messages qui peuvent tirer des informations soumises à consentement sur le compte de votre utilisateur, et permettre la personnalisation et les pratiques de messagerie pertinentes.

Dans le bloc suivant, vous pouvez voir qu’une double utilisation d’une balise Liquid pour appeler le prénom de l’utilisateur, ainsi qu’une balise par défaut si le prénom d’un utilisateur n’est pas enregistré.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Pour un utilisateur nommé Janet Doe, le message s’affiche comme suit :

```
Hi Janet, thanks for using the App!
```

OU

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
Les commentaires HTML (`<!-- -->`) sont supprimés avant toute lecture de Liquid, de sorte que les étiquettes Liquid contenues dans les commentaires HTML **ne** s'affichent **pas** dans votre message. Pour un rendu correct, veuillez vous assurer que toutes les étiquettes Liquid que vous souhaitez utiliser se trouvent en dehors des commentaires HTML.
{% endalert %}

## Valeurs acceptées pour la substitution

Les valeurs suivantes peuvent être remplacées par un message, selon leur disponibilité :

- [Informations de base sur l'utilisateur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) (par exemple, `first_name`, `last_name`, `email_address`)
- [Attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)
    - [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#liquid-templating)
- [Propriétés de l'événement  personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- [Informations sur les appareils les plus récemment utilisées]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information)
- [Informations sur l'appareil cible]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information)

Vous pouvez également extraire du contenu directement d'un serveur web grâce au [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) de Braze.

{% alert important %}
Braze prend actuellement en charge Liquid jusqu'à la version Liquid 5 de Shopify.
{% endalert %}

## Utilisation de Liquid

Grâce aux [étiquettes Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), vous pouvez rehausser la qualité de vos messages en les enrichissant d'une touche de personnalisation. 

### Syntaxe en Liquid

Liquid suit une structure ou une syntaxe spécifique que vous devrez garder à l’esprit lorsque vous concevez une personnalisation dynamique. Voici quelques règles de base à garder à l’esprit :

1. **Utilisez des guillemets droits dans Braze :** Il existe une différence entre les guillemets frisés ('**')** et les guillemets droits ('**').** Utilisez des guillemets droits ('**')** dans votre liquide dans Braze. Vous pouvez voir des guillemets courbes lorsque vous copiez-collez certains éditeurs de texte, ce qui peut entraîner des problèmes dans votre Liquid. Si vous saisissez des guillemets directement dans le tableau de bord de Braze, cela sera parfait !
2. **Les parenthèses fonctionnent par deux :** Une parenthèse ouverte doit être suivie d’une parenthèse fermée **{ }**. Assurez-vous d’utiliser des parenthèses courbes !
3. **Les déclarations sont présentées par paires :** Pour chaque `if`, vous avez besoin d’un `endif` pour indiquer que l’énoncé `if` a pris fin.
4. **Les noms de variables doivent utiliser des caractères ASCII :** Les noms de variables liquides (créés avec`assign`  ou `capture`) ne prennent en charge que les lettres ASCII, les chiffres et les traits de soulignement. Les noms d'attributs de personnalisation Braze (à l'intérieur de`custom_attribute.${...}`  ou `event_properties.${...}`) peuvent inclure des caractères non ASCII.

#### Où utiliser les opérateurs et les filtres

Les opérateurs (tels que `==`, `!=`, `>`, `and`, `or`) et les filtres (tels que `| size`, `| plus`) ne peuvent être utilisés que dans des contextes Liquid spécifiques.

| Contexte | Opérateurs | Filtres |
|-----------|-----------|---------|
| `assign` | Non pris en charge | Pris en charge |
| `if`, `elsif`, `unless` | Pris en charge | Non pris en charge |
| `case`, `when` | Non pris en charge | Non pris en charge |
| `for` | Non pris en charge | Non pris en charge |
| Accès au tableau (`[ ]`) | Non pris en charge | Non pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsque vous avez besoin d'une valeur filtrée dans un contexte qui ne prend pas en charge les filtres, veuillez d'abord assigner le résultat à une variable.

{% raw %}

##### Utiliser un résultat de filtre dans une condition

Il n'est pas possible d'utiliser un filtre directement dans une instruction conditionnelle. Ceci est incorrect :

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

Veuillez plutôt assigner le résultat du filtre à une variable :

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### Utiliser un résultat de filtre dans une boucle « for »

Il n'est pas possible d'appliquer un filtre à l'itérable dans une`for`boucle. Ceci est incorrect :

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

Veuillez plutôt attribuer la valeur filtrée à une variable :

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### Utiliser un résultat de filtre pour accéder à un tableau

Il n'est pas possible d'utiliser un filtre entre crochets. Ceci est incorrect :

```liquid
{{ my_array[my_var | minus: 1] }}
```

Veuillez plutôt attribuer d'abord la valeur filtrée :

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### Enregistrer le résultat d'une comparaison dans une variable

Il n'est pas possible d'utiliser un opérateur dans une`assign`instruction. Ceci est incorrect :

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

Veuillez plutôt utiliser une condition pour définir la variable :

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### Attributs par défaut et attributs personnalisés

{% raw %}

Si vous incluez le texte suivant dans votre message : `{{${first_name}}}`, le prénom de l’utilisateur (tiré du profil de l’utilisateur) sera remplacé lorsque le message est envoyé. Vous pouvez utiliser le même format avec d'autres attributs utilisateurs par défaut.

Si vous souhaitez utiliser la valeur d'un attribut personnalisé, il est nécessaire d'ajouter l'espace de noms"custom_attribute"à la variable. Par exemple, pour utiliser un attribut personnalisé nommé « code postal », vous ajoutez `{{custom_attribute.${zip code}}}` à votre message.

### Insertion des balises

Vous pouvez insérer des balises en saisissant deux parenthèses courbes `{{` dans n’importe quel message, ceci déclenchera une fonctionnalité d’achèvement automatique qui continuera à être mise à jour lors de votre saisie. Vous pouvez même sélectionner une variable à partir des options qui s’affichent alors que vous saisissez.

Si vous utilisez une balise personnalisée, vous pouvez copier et coller la balise dans le message que vous souhaitez.

#### Exceptions pour les doubles crochets

Si vous utilisez une étiquette à l'intérieur d'une autre étiquette Liquid, telle que`{% assign %}`ou `{% if %}`, vous pouvez utiliser soit des doubles crochets, soit aucun crochet. Ce n'est que lorsque l'étiquette est seule qu'elle doit être placée entre deux crochets. Pour simplifier, vous pouvez toujours utiliser des doubles crochets. 

Les tags suivants sont tous corrects :

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

Si vous utilisez Liquid dans vos messages d'e-mail, veuillez vous assurer de :

1. l’insérer à l’aide de l’éditeur HTML, plutôt que de l’éditeur classique. L'éditeur classique peut analyser le Liquid comme du texte brut. Par exemple, le Liquid serait analysé comme suit {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %}: au lieu d'utiliser un modèle dans le prénom de l'utilisateur.
2. Placez le code Liquid dans la balise `<body>` uniquement. Le fait de le placer en dehors de cette balise peut entraîner un rendu irrégulier lors de la livraison.

{% endalert %}

### Insertion de variables préformatées

Vous pouvez insérer des variables préformatées avec des valeurs par défaut dans la fenêtre modale/boîte de dialogue **Ajouter une personnalisation** située à proximité de n'importe quel champ de texte modèle.

![La fenêtre modale Ajouter une personnalisation qui apparaît après avoir sélectionné Insérer une personnalisation. La fenêtre modale comporte des champs pour le type de personnalisation, l'attribut, la valeur par défaut facultative et affiche un aperçu de la syntaxe Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

La fenêtre modale insère Liquid avec la valeur par défaut que vous avez spécifiée à l'endroit où se trouvait votre curseur. Le point d'insertion est également indiqué par la zone d'aperçu, qui contient le texte avant et après. Si un bloc de texte est mis en surbrillance, le texte mis en surbrillance sera remplacé.

![GIF de la fenêtre modale « Ajouter une personnalisation » montrant l'utilisateur saisissant « compagnon de voyage » comme valeur par défaut, et la fenêtre modale remplaçant le texte surligné « nom » dans l'éditeur par l'extrait de code Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

### Attribution des variables

{% raw %}
Certaines opérations dans Liquid exigent que vous stockiez la valeur que vous souhaitez manipuler comme variable. C’est souvent le cas si votre énoncé Liquid comprend plusieurs attributs, propriétés de l’événement ou filtres.

Supposons par exemple que vous souhaitiez ajouter deux entiers de données personnalisés. 

#### Exemple incorrect de liquid

Vous ne pouvez pas utiliser :

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Ce liquid ne fonctionne pas car il n'est pas possible de référencer plusieurs attributs dans une seule ligne ; il est nécessaire d'attribuer une variable à au moins une de ces valeurs avant que les fonctions mathématiques ne puissent être exécutées. L’ajout de deux attributs personnalisés nécessiterait deux lignes de Liquid : l’une pour attribuer l’attribut personnalisé à une variable et l’autre pour l’ajout.

#### Exemple correct de liquid

Vous pouvez utiliser :

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutoriel : Utiliser des variables pour calculer un solde

Calculons le solde actuel d'un utilisateur en additionnant le solde de sa carte cadeau et le solde de ses récompenses :

Tout d’abord, utilisez la balise `assign` pour remplacer l’attribut personnalisé de `current_rewards_balance` par le terme « solde ». Cela signifie que vous avez maintenant une variable intitulée `balance` que vous pouvez manipuler.

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
Vous envoyez les mêmes variables dans chaque message ? Au lieu d’écrire la balise `assign` sans arrêt vous pouvez enregistrer cette balise comme un bloc de contenu et la placer en haut de votre message.

1. [Créez un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Donnez un nom à votre bloc de contenu (aucun espace ni caractère spécial).
3. Sélectionnez **Modifier** en bas de la page.
4. Veuillez saisir vos`assign`tags.

Tant que le bloc de contenu est en haut de votre message, chaque fois que la variable est insérée dans votre message comme objet, elle se rapporte à l’attribut personnalisé que vous avez choisi !
{% endalert %}

