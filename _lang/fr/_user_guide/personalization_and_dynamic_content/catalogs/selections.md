---
nav_title: Sélections
article_title: Sélections
page_order: 2
description: "Le présent article de référence explique comment créer et utiliser des sélections avec vos catalogues pour référencer des données dans vos campagnes Braze."
---

# Sélections

> Les sélections sont des groupes de données qui peuvent être utilisés pour personnaliser un message pour chaque utilisateur dans votre campagne. Après avoir créé un [catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalog/), vous pouvez référencer plus finement ces données en incorporant des sélections dans vos campagnes Braze. Prenez en compte le fait que le niveau gratuit de catalogues permet la création d’une seule sélection par catalogue. 

{% alert important %}
Les sélections sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

Pour créer une sélection, sélectionnez votre catalogue et cliquez sur **Create Selection (Créer une sélection)**. Sélectionnez la colonne de catalogue dans le menu déroulant **Champ de filtre**. Ensuite, sélectionnez l’opérateur et saisissez l’attribut. Continuez en ajoutant des filtres supplémentaires selon les paramétrages de filtres dont vous avez besoin.

Dans la section **Trier les types**, vous pouvez définir l’ordre de sortie des résultats. Ceci comprend une option permettant de rendre l’ordre du classement aléatoire. Saisissez ensuite le nombre maximal de résultats, jusqu’à 10, dans le **Limite de nombre** dans la section **Limite de résultats**.

Après avoir configuré la sélection, cliquez sur **Create Selection (Créer une sélection)** et la sélection s’affichera au-dessus des données du catalogue. Vous pouvez maintenant référencer cette sélection dans votre envoi de messages.

{% alert important %}
Les champs de chaîne de caractère comprenant plus de 1 000 caractères ne peuvent pas être filtrés.
{% endalert %}

Si vous utilisez du Liquid dans vos catalogues, tels que des attributs personnalisés ou des événements personnalisés, ceci peut entraîner le renvoi de résultats différents pour chaque utilisateur dans votre sélection.

![La section Sélections dans un exemple de catalogue.][1]

## Cas d’utilisation

Imaginons que vous possédiez un service de livraison de repas et désiriez envoyer un message personnalisé à vos utilisateurs ayant des préférences particulières concernant leurs repas selon la catégorie de nourriture qu’ils ont consultée le plus récemment. 

En utilisant un catalogue avec les informations de votre service de livraison de repas concernant le nom du plat, son prix, son image et sa catégorie, vous pouvez créer une sélection paramétrée pour recommander trois plats sur la base de la catégorie consultée le plus récemment par un utilisateur.

![Un exemple d’une sélection pour un service de livraison de repas avec deux filtres : un qui identifie un type de produit comme étant un repas et l’autre identifiant la catégorie que l’utilisateur a visualisée le plus récemment. La sélection est paramétrée pour afficher de manière aléatoire les trois résultats renvoyés.][2]{: style="max-width:90%;"}

Pour utiliser ce catalogue et cette sélection dans une campagne, utilisez le modal **Ajouter une personnalisation** dans la section de composition de votre message lors de la création d’une campagne. Dans cet exemple, nous avons sélectionné le catalogue avec les informations de votre service de livraison de repas et la sélection pour les recommandations de repas basées sur la catégorie visualisée le plus récemment. Ceci nous permet d’afficher le nom du plat et son prix. Pour construire plus en détail notre message, vous pouvez utiliser la sélection pour ajouter également une image au plat recommandé en premier.

![Une carte de contenu avec l’en-tête « Vous allez ADORER ces repas très appréciés : » avec la sélection « recommendations_be_recent_category » dans la section de composition du message.][3]{: style="max-width:90%;"}

Par exemple, si vous avez un utilisateur pour lequel la catégorie visualisée le plus récemment est « Poulet ». En utilisant la personnalisation de l’ensemble et une campagne de cartes de contenu, nous pouvons envoyer des recommandations de trois plats comprenant du poulet pour cet utilisateur.

![Une carte de contenu avec l’image d’un poulet grillé au citron et une liste de trois plats recommandés comprenant du poulet sur la base de la catégorie affichée le plus récemment par l’utilisateur.][4]{: style="max-width:90%;"}

En utilisant la même personnalisation, nous pouvons également envoyer une recommandation pour trois plats à un utilisateur pour lequel la catégorie affichée le plus récemment est « Bœuf ».

![Une carte de contenu avec l’image d’un bœuf Stroganov et une liste de deux plats recommandés comprenant du bœuf sur la base de la catégorie affichée le plus récemment par l’utilisateur.][5]{: style="max-width:90%;"}


[1]: {% image_buster /assets/img_archive/catalog_selections1.png %}
[2]: {% image_buster /assets/img_archive/catalog_selections2.png %}
[3]: {% image_buster /assets/img_archive/catalog_selections3.png %}
[4]: {% image_buster /assets/img_archive/catalog_selections4.png %}
[5]: {% image_buster /assets/img_archive/catalog_selections5.png %}