---
nav_title: Utilisation des recommandations
article_title: "Utiliser les recommandations d'articles dans vos messages"
description: "Cet article explique comment utiliser les recommandations d'articles dans votre message."
page_order: 1.2
---

# Utiliser les recommandations d'articles dans vos messages

> Une fois votre recommandation formée, vous pouvez utiliser Liquid pour récupérer et afficher les éléments recommandés dans vos messages en travaillant directement avec l'objet Liquid `product_recommendation`.

{% alert tip %}
Pour une présentation étape par étape, consultez notre cours d'apprentissage Braze : [Créer des expériences personnalisées grâce à l'intelligence artificielle](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## Conditions préalables

Avant de pouvoir utiliser des recommandations dans vos messages, vous devrez [créer et former un moteur de recommandation]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/). La formation peut durer entre 10 minutes et 36 heures. Vous recevrez un e-mail lorsque la formation sera terminée ou si une erreur s'est produite.

## Utiliser des recommandations dans vos messages

### Étape 1 : Ajouter le code Liquid

Une fois la formation de votre recommandation terminée, vous pouvez personnaliser vos messages avec Liquid pour y insérer les produits les plus populaires de ce catalogue.

{% tabs local %}
{% tab code préformaté %}
![Modale "Ajouter une personnalisation" avec la recommandation d'articles comme type de personnalisation.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Vous pouvez générer du liquide à partir de la section **Ajouter une personnalisation** dans votre compositeur de messages :

1. Dans tous les compositeurs de messages qui prennent en charge la personnalisation, sélectionnez <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Ajouter une personnalisation"></i> pour ouvrir la fenêtre de personnalisation.
2. Pour le **type de personnalisation**, sélectionnez **Recommandation produit**.
3. Pour **Nom de la recommandation de l'élément**, sélectionnez la recommandation que vous venez de créer.
4. Pour **Nombre de produits prédits**, indiquez le nombre de meilleurs produits que vous souhaitez insérer. Par exemple, vous pouvez afficher les trois produits les plus achetés.
5. Pour les **informations à afficher**, sélectionnez les champs du catalogue à inclure pour chaque article. Les valeurs de ces champs pour chaque article seront tirées du catalogue associé à cette recommandation.
6. Sélectionnez l'icône **Copier** et collez le liquide à l'endroit voulu dans votre message.
{% endtab %}

{% tab code personnalisé %}
Vous pouvez écrire un code Liquid personnalisé en faisant référence à l'objet `product_recommendation` d'un catalogue. Il contient toutes les données de recommandation de produits générées dynamiquement pour ce catalogue, structurées sous la forme d'un tableau d'objets, où chaque objet représente un article recommandé.

|Spécifications|Détails|
|-------------|-------|
|**Structure**|Chaque élément est accessible sous la forme `items[index]`, où l'index commence à 0 (pour le premier élément) et s'incrémente pour les éléments suivants.|
|**Champs du catalogue**|Chaque élément du tableau contient des paires clé-valeur correspondant à des champs (colonnes) du catalogue. Par exemple, les champs de catalogue courants pour les recommandations de produits sont les suivants :<br>- `name` ou `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Utilisez l'étiquette `assign` pour récupérer les données de `product_recommendation` et les affecter à une variable.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

Remplacez les éléments suivants :

|Marque substitutive|Description|
|-----------|-----------|
|`recommendation_name`|Le nom de la recommandation d'intelligence artificielle que vous avez créée dans Braze.|
|`items`|Variable contenant le tableau des éléments recommandés.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Ensuite, faites référence à des éléments spécifiques et à leurs champs en utilisant l'indexation de tableau et la notation par points :

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

Pour inclure plusieurs éléments, faites référence à chaque élément individuellement par son index. `.name` et `.price` tirent le champ correspondant du catalogue. 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

Les recommandations de l'intelligence artificielle renvoient plusieurs produits sous la forme d'un tableau, où `items[0]` est le premier article, `items[1]` le deuxième, et ainsi de suite. Si une recommandation ne renvoie qu'un seul élément, toute tentative de référence à `items[1]` aboutira à un champ vide.
{% endtab %}
{% endtabs %}

### Étape 2 : Référencez une image (facultatif)

Si le catalogue que vous recommandez comporte des liens vers des images, vous pouvez y faire référence dans votre message. 

{% tabs %}
{% tab Glisser-déposer%}
Dans l'éditeur par glisser-déposer de l'e-mail, ajoutez un bloc d'image à votre e-mail, puis sélectionnez le bloc d'image pour ouvrir les **propriétés de l'image.**

![Panneau des propriétés de l'image dans l'éditeur par glisser-déposer]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

Basculez sur **Image with Liquid**, puis ajoutez ce qui suit au champ **Dynamic URL :** 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].image_url_field }}
```
{% endraw %}

Remplacez les éléments suivants :

|Marque substitutive|Description|
|-----------|-----------|
|`recommendation_name`|Le nom de votre recommandation.|
|`image_url_field`|Le nom du champ de votre catalogue qui contient les URL des images.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Pour inclure une image substitutive dans vos e-mails de prévisualisation et de test, sélectionnez **Choisir une** image, puis choisissez une image dans votre bibliothèque multimédia ou saisissez l'URL d'une image sur votre site d'hébergement.
{% endtab %}

{% tab HTML %}
Pour les références d'images HTML, définissez l'attribut image `src` sur le champ URL de l'image dans le catalogue. Vous pouvez utiliser un autre champ, tel que le nom ou la description d'un produit, comme texte alt.

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

Remplacez les éléments suivants :

|Marque substitutive|Description|
|-----------|-----------|
|`recommendation_name`|Le nom de votre recommandation.|
|`image_url_field`|Le nom du champ de votre catalogue qui contient les URL des images.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}
