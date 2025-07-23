---
nav_title: "Utilisation des recommandations d'éléments"
article_title: "Utiliser les recommandations d'articles dans vos messages"
description: "Cet article explique comment utiliser les recommandations d'articles dans votre message."
page_order: 20
---

# Utiliser les recommandations d'articles dans vos messages

> Une fois votre recommandation formée, vous pouvez utiliser Liquid pour rechercher et afficher les éléments recommandés dans vos messages. La clé ici est de travailler directement avec l'objet `product_recommendation` Liquid. Cet article traite de l'objet `product_recommendation` Liquid et comprend un tutoriel pour vous aider à mettre ces connaissances en pratique.

{% alert tip %}
Cet article décrit en détail la syntaxe de l'objet Liquid. Toutefois, vous pouvez [insérer des variables préformatées]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) avec des valeurs par défaut via la fenêtre modale/boîte de dialogue **Ajouter une personnalisation** située en haut à droite de n'importe quel champ de texte modélisé.
{% endalert %}

Pour obtenir des conseils supplémentaires sur l'utilisation des recommandations d'articles d'intelligence artificielle dans Braze, consultez notre [cours d'][1]apprentissage Braze [sur l'élaboration d'expériences personnalisées avec l'intelligence artificielle.][1] Ce cours couvre les cas d'utilisation du secteur, les instructions étape par étape et un cas d'utilisation supplémentaire pour la création d'un message in-app avec des recommandations basées sur l'intelligence artificielle.

## Anatomie de l'objet de la recommandation

L'objet `product_recommendation` représente l'ensemble des éléments conseillés par le modèle. Il fournit des données directement à partir du catalogue associé, structurées sous la forme d'un tableau d'objets, où chaque objet représente un article conseillé.

- **Structure :** Chaque élément est accessible sous la forme `items[index]`, où l'index commence à 0 (pour le premier élément) et s'incrémente pour les éléments suivants.
- **Champs du catalogue :** Chaque élément du tableau contient des paires clé-valeur correspondant à des champs (colonnes) du catalogue. Par exemple, les champs de catalogue courants pour les recommandations de produits sont les suivants :
   - `name` ou `title`
   - `price`
   - `image_url`

## Balises Liquid

L'objet `product_recommendation` contient des recommandations de produits générées dynamiquement. Pour y accéder dans Liquid, vous devez d'abord affecter les données à une variable avant de les utiliser dans votre message.

### Attribution des données de recommandation

Commencez toujours par l'étiquette assign pour récupérer les données de `product_recommendation` et les stocker dans une variable.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
```

{% endraw %}

- `RECOMMENDATION_NAME` : Remplacez ce nom par celui de la recommandation d'intelligence artificielle que vous avez créée dans Braze.
- `items` : Variable contenant le tableau des éléments recommandés.

### Accéder à des éléments individuels

Une fois les données de recommandation affectées, vous pouvez faire référence à des éléments spécifiques et à leurs champs à l'aide de l'indexation de tableau et de la notation par points :

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
```

{% endraw %}

Pour inclure plusieurs éléments, faites référence à chaque élément individuellement par son index. `.name` et `.price` tirent le champ correspondant du catalogue. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```

{% endraw %}

Les recommandations de l'intelligence artificielle renvoient plusieurs produits sous la forme d'un tableau, où `items[0]` est le premier article, `items[1]` le deuxième, et ainsi de suite. Si une recommandation ne renvoie qu'un seul élément, toute tentative de référence à `items[1]` aboutira à un champ vide.

## Ajout d'images

Si le catalogue utilisé par votre recommandation comporte des liens vers des images, vous pouvez faire référence à ces images dans votre message. 

{% tabs %}

{% tab Glisser-déposer%}
Dans les compositeurs avec des champs d'image, ajoutez le Liquid suivant au champ correspondant dans le compositeur :

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

Pour l'éditeur par glisser-déposer de l'e-mail :

1. Ajoutez un bloc d'images à votre e-mail.
2. Sélectionnez le bloc d'image (et non le bouton **Parcourir** ) pour ouvrir le panneau des **propriétés de l'image.** 
3. Allumez l'**image avec du liquide**. 
4. Collez l'extrait de code liquide dans le champ **URL dynamique**.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

![Panneau des propriétés de l'image dans l'éditeur par glisser-déposer]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:60%"}

{:start="5"}

5. Pour inclure une image substitutive dans vos e-mails de prévisualisation et de test, appuyez sur **Choisir une image** pour ajouter une image substitutive à partir de la bibliothèque multimédia, ou saisissez une URL où votre image est hébergée.

{% endtab %}

{% tab HTML %}

Pour les références d'images HTML, définissez l'attribut image `src` sur le champ URL de l'image dans le catalogue. Vous pouvez utiliser un autre champ, tel que le nom ou la description d'un produit, comme texte alt.

{% raw %}

```html
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
<img src="{{ items[0].IMAGE_URL_FIELD }}" alt="{{ items[0].name }}">
```

{% endraw %}

{% endtab %}

{% endtabs %}

-  Remplacez `MY_RECOMMENDATION_NAME` par le nom de votre recommandation
- Remplacez `IMAGE_URL_FIELD` par le nom du champ de votre catalogue qui contient les URL des images.


## Tutoriel : Créer un e-mail d'abandon de panier

Dans ce tutoriel, vous apprendrez à créer un e-mail dynamique qui recommande des produits aux utilisateurs en fonction de leurs préférences ou de leur comportement en utilisant les recommandations d'articles de l'intelligence artificielle de Braze. 

Supposons que vous soyez marketeur chez "Flash & Thread", un détaillant de vêtements en ligne. Vous souhaitez réengager les clients qui ont laissé des articles dans leur panier et leur proposer des produits supplémentaires. Votre objectif est de créer un e-mail qui affiche les articles abandonnés et des recommandations personnalisées.

### Étape 1 : Préparez votre catalogue

Votre recommandation tirera des articles d'un catalogue. Suivez les étapes de la création d'un catalogue. Assurez-vous que votre catalogue comprend ces champs :

| Champ | Type de données | Description |
| --- | --- | --- |
| id | Chaîne de caractères | Un identifiant unique pour chaque article de votre catalogue |
| nom | Chaîne de caractères | Le nom du produit, par exemple "Pull en tricot rayé". |
| prix | Nombre | Le prix du produit, par exemple "49,99". |
| image_url | Chaîne de caractères | Une URL pointant vers l'image du produit. Doit être sécurisé par HTTPS. Si vos images sont hébergées dans la bibliothèque multimédia, survolez une ressource pour copier son URL. |
| category | Chaîne de caractères | La catégorie du produit, comme "Pulls" ou "Accessoires". |
| color | Chaîne de caractères | Une couleur descriptive pour le produit, comme "Marine/Gris". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


#### Exemple de catalogue

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table class="tg">
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>prix</th>
    <th>image_url</th>
    <th>category</th>
    <th>color</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>Pull tricoté à rayures</td>
    <td>49.99</td>
    <td>https://{{media_library}}/images/67a41294f5eac400685ce908/original.png?1738805908</td>
    <td>Pulls</td>
    <td>bleu marine/gris</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>Chaussures personnalisées pour Yacht Club</td>
    <td>79.99</td>
    <td>https://{{media_library}}/images/67a4136fe5a7660068bbe046/original.png?1738806127</td>
    <td>Chaussures</td>
    <td>bleu marine</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>Retour aux chaussures de travail</td>
    <td>89.99</td>
    <td>https://{{media_library}}/images/67a41370f542c1006798c26e/original.png?1738806128</td>
    <td>Chaussures</td>
    <td>Pink/Gold</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>Chapeau de fin d’été</td>
    <td>29.99</td>
    <td>https://{{media_library}}/images/67a4136fbf6f620068511b67/original.png?1738806127</td>
    <td>Accessoires</td>
    <td>Blanc Floral</td>
  </tr>
</table>


### Étape 2 : Mettre en place votre recommandation

1. Dans votre catalogue, sélectionnez **Créer une recommandation**.
2. Suivez la procédure décrite dans la section [Création d'une recommandation d'élément d'intelligence artificielle]][3]. 
3. Pour le type de recommandation, sélectionnez **Intelligence artificielle personnalisée.**
4. Utilisez le catalogue que vous venez de créer pour former la recommandation. Cela peut prendre un certain temps - vous recevrez un e-mail lorsque la formation sera terminée.

### Étape 3 : Créer un e-mail

Lorsque la recommandation a terminé sa formation, vous pouvez l'utiliser dans vos messages.

1. Créez un e-mail avec l'éditeur par glisser-déposer.
2. Dans le corps du message, ajoutez un bloc d'image à l'endroit où vous souhaitez extraire une recommandation du catalogue. 
3. Sélectionnez le bloc d'image et activez l'option **Image avec liquide** dans le panneau des **propriétés de l'image**. 
4. Collez cet extrait de code liquide dans le champ URL dynamique.


{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].image_url }}
```

{% endraw %}

{: start="5"}

5. Sous l'image, ajoutez un bloc de paragraphes. C'est ici que vous ajouterez le nom du produit et tout détail complémentaire. 
6. Collez l'extrait de code liquide suivant dans le bloc. Le nom, la catégorie, la couleur et le prix de la première recommandation sont extraits du catalogue et ajoutés sur des lignes distinctes. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].name }}
{{ items[0].category }}
{{ items[0].color }}
${{ items[0].price }}
```

{% endraw %}

{: start="7"}

7. Pour les deux extraits de code, remplacez `abandoned_cart` par le nom de votre recommandation dans Braze.
8. Vérifiez que les noms des champs de l'article (`{{ items[0].field_name }}`) correspondent aux noms des colonnes de votre catalogue.
9. Incrémentez le tableau d'une unité à chaque fois que vous répétez le bloc afin d'extraire du catalogue l'élément recommandé suivant. Par exemple, le tableau commence par `{{ items[0].name }}`, de sorte que l'élément suivant serait `{{ items[1].name }}`.

### Étape 4 : Prévisualisez votre message

Pour voir à quoi ressemble votre message pour un utilisateur réel :

1. Allez dans l'onglet **Prévisualisation et test de** votre éditeur.
2. Sélectionnez **Utilisateur aléatoire** dans la liste déroulante.
3. Sélectionnez **Obtenir un utilisateur aléatoire** pour récupérer un utilisateur de votre audience et prévisualiser l'affichage de l'e-mail avec ses données.

L'aperçu rendra entièrement Liquid, y compris les recommandations de l'intelligence artificielle, tant que l'utilisateur sélectionné possède les attributs requis ou les données d'événement liées à la recommandation.

Si la recommandation n'apparaît pas dans l'aperçu, vérifiez les points suivants :

- L'utilisateur a interagi avec des produits ou des événements pertinents qui ont formé le modèle de recommandation.
- La recommandation elle-même a été entraînée avec succès
- Le code Liquid fait référence à la recommandation et aux champs corrects.



[1]: https://learning.braze.com/ai-item-recommendations-use-case/1996254
[2]: {% image_buster /assets/img/image_with_liquid.png %}
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations#creating-an-ai-item-recommendation