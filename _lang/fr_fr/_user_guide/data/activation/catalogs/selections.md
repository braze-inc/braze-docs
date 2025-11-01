---
nav_title: Sélections
article_title: Sélections
page_order: 5
description: "Cet article de référence explique comment créer et utiliser des sélections avec vos catalogues pour référencer des données dans vos campagnes Braze."
---

# Sélections

> Les sélections sont des groupes de données qui peuvent être utilisés pour personnaliser un message pour chaque utilisateur de votre campagne. Lorsque vous utilisez une sélection, vous configurez essentiellement des filtres personnalisés basés sur des colonnes spécifiques de votre catalogue. Il peut s'agir de filtres pour la marque, la taille, l'emplacement/localisation, la date d'ajout, etc. Il vous permet de contrôler ce que vous montrez aux utilisateurs en définissant des critères auxquels les éléments doivent d'abord répondre.<br><br>Cette page explique comment créer et utiliser des sélections dans vos catalogues.

Après avoir créé un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/), vous pouvez référencer davantage les données de votre catalogue en incorporant des sélections dans vos campagnes ou recommandations Braze.

\![La section Sélections dans un exemple de catalogue.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Ce qu'il faut savoir

- Vous pouvez créer jusqu'à 30 sélections par catalogue.
- Vous pouvez ajouter jusqu'à 10 filtres par sélection.
- Les sélections sont idéales pour affiner les recommandations à partir des données du catalogue Braze. Si vous êtes en quête d'inspiration, consultez les [recommandations de l'article About]({{site.baseurl}}/user_guide/brazeai/recommendations/) pour des exemples de cas d'utilisation.

## Création d'une sélection

Pour créer une sélection, procédez comme suit.

1. Allez dans **Catalogues** et sélectionnez votre catalogue dans la liste.
2. Sélectionnez l'onglet **Sélection** et cliquez sur **Créer une sélection**.
3. Donnez à votre sélection un nom et une description facultative.
4. Dans le champ **Filtre**, sélectionnez la colonne du catalogue sur laquelle vous voulez filtrer. Les chaînes de caractères de plus de 1 000 caractères ne peuvent pas être sélectionnées pour les filtres.
5. Terminez la définition de vos critères de filtrage en sélectionnant l'opérateur approprié (par exemple, "égal" ou "n'est pas égal") et l'attribut.
6. Dans la section **Type de tri**, déterminez comment les résultats sont triés. Par défaut, les résultats sont renvoyés sans ordre particulier. Pour spécifier le tri par champ spécifique, désactivez l'option **Randomiser l'ordre de tri** et spécifiez le **champ de tri** et l'**ordre de tri** (croissant ou décroissant).
7. Dans la section **Limite des résultats**, saisissez les résultats (jusqu'à 50).
8. Sélectionnez **Créer une sélection**.

### Test et prévisualisation

Après avoir créé une sélection, vous pouvez utiliser la section **Prévisualisation pour l'utilisateur** pour voir ce qu'une sélection donnerait pour un utilisateur aléatoire ou un utilisateur spécifique. Pour les sélections qui utilisent la personnalisation, vous ne pouvez voir l'aperçu qu'après avoir sélectionné un utilisateur.

### Liquide dans les résultats de la sélection

L'utilisation de tout liquide dans les catalogues, comme les attributs personnalisés et les événements personnalisés, peut donner lieu à des résultats différents pour chaque utilisateur de votre sélection. 

{% alert note %}
Le contenu connecté liquid n'est pas pris en charge dans ces paramètres de filtrage.
{% endalert %}

\![Paramètres de filtrage pour la sélection du catalogue lorsque l'attribut est défini sur un attribut personnalisé Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Utilisation de sélections dans l'envoi de messages

Après avoir créé votre sélection, personnalisez vos messages avec Liquid pour insérer les éléments filtrés de ce catalogue. Vous pouvez demander à Braze de générer le liquide pour vous à partir de la fenêtre de personnalisation qui se trouve dans les compositeurs de messages :

1. Dans tous les compositeurs de messages qui prennent en charge la personnalisation, sélectionnez <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Ajouter une personnalisation"></i> pour ouvrir la fenêtre de personnalisation.
2. Pour le **type de personnalisation**, sélectionnez **Articles de catalogue.**
3. Sélectionnez le nom de votre catalogue.
4. Pour la **méthode de sélection des éléments**, sélectionnez **Utiliser une sélection.**
4. Sélectionnez votre choix dans la liste.
5. Pour les **informations à afficher**, sélectionnez les champs du catalogue à inclure pour chaque article.
6. Sélectionnez l'icône **Copier** et collez le liquide à l'endroit voulu dans votre message.

\![La fenêtre modale/boîte de dialogue de personnalisation avec les sélections suivantes : " Articles du catalogue " pour " Type de personnalisation ", " Jeux " pour " Nom du catalogue ", " Sélections " pour " Type de sélection ", "game_selection" pour " Sélection ", et " titre " et "description_en" pour " Informations à afficher ".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Cas d'utilisation

Imaginons que vous possédiez un service de réception/distribution de repas et que vous souhaitiez envoyer un message personnalisé à vos utilisateurs qui ont des préférences de repas spécifiques, en fonction de la catégorie d'aliments qu'ils ont consultée le plus récemment. 

En utilisant un catalogue avec les informations de votre service de réception/distribution pour le nom du repas, le prix, l'image et la catégorie du repas, vous pouvez créer une sélection pour recommander trois repas en fonction de la catégorie la plus récemment consultée par un utilisateur.

Exemple de sélection pour un service de réception/distribution de repas avec deux filtres : un qui identifie un type de produit comme étant un repas, et un qui identifie la catégorie comme étant la plus récemment consultée. La sélection est définie de manière à rendre aléatoire l'ordre dans lequel les trois résultats sont renvoyés.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Pour utiliser ce catalogue et cette sélection dans une campagne, utilisez la fenêtre modale/boîte de dialogue **Ajouter une personnalisation** dans la section de composition des messages de la création d'une campagne. Dans cet exemple, nous avons sélectionné le catalogue avec les informations de votre service de réception/distribution, et la sélection pour les recommandations de repas basées sur la catégorie la plus récemment consultée. Cela nous permet d'afficher le nom et le prix du repas. Pour créer davantage votre message, vous pouvez utiliser la sélection pour ajouter également une image du premier repas recommandé.

Une carte de contenu avec l'en-tête "Vous allez ADORER ces repas très bien notés" avec la sélection "recommendations_be_recent_category" dans la section de composition du message.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Par exemple, supposons que vous ayez un utilisateur dont la catégorie la plus récemment consultée est "Poulet". En utilisant la personnalisation définie et une campagne de cartes de contenu, vous pouvez envoyer trois recommandations de repas incluant du poulet à cet utilisateur.

Une carte de contenu avec une image de poulet au citron grillé et une liste de trois recommandations de repas incluant du poulet, basées sur la catégorie la plus récemment consultée par l'utilisateur.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

En utilisant la même personnalisation, vous pouvez également envoyer trois recommandations de repas à un utilisateur dont la catégorie la plus récemment consultée est "Bœuf".

Une carte de contenu avec une image de bœuf stroganoff et une liste de deux recommandations de repas incluant du bœuf, basées sur la dernière catégorie consultée par l'utilisateur.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}


