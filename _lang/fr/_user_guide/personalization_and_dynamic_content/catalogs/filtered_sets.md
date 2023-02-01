---
nav_title: Ensembles filtrés
article_title: Ensembles filtrés
page_order: 2
description: "Le présent article de référence explique comment créer et utiliser des ensembles de filtres avec vos catalogues pour référencer des données dans vos campagnes Braze."
---

# Ensembles filtrés

Les ensembles de filtres sont des groupes de données qui peuvent être utilisés pour personnaliser un message pour chaque utilisateur dans votre campagne. Après avoir créé un [catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalog/), vous pouvez référencer plus finement ces données en incorporant des ensembles filtrés dans vos campagnes Braze. Prenez en compte le fait que le niveau gratuit de catalogues permet la création d’un seul ensemble filtré par catalogue. 

{% alert important %}
Les ensembles filtrés sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

Pour créer un ensemble filtré, sélectionnez votre catalogue et cliquez sur **Créer un ensemble filtré**. Sélectionnez la colonne de catalogue dans le menu déroulant **Champ de filtre**. Ensuite, sélectionnez l’opérateur et saisissez l’attribut. Continuez en ajoutant des filtres supplémentaires selon les paramétrages de filtres dont vous avez besoin.

Dans la section **Trier les types**, vous pouvez définir l’ordre de sortie des résultats. Ceci comprend une option permettant de rendre l’ordre du classement aléatoire. Saisissez ensuite le nombre maximal de résultats, jusqu’à 10, dans le **Limite de nombre** dans la section **Limite de résultats**.

Après avoir paramétré l’ensemble filtré, cliquez sur **Créer l’ensemble filtré** et cet ensemble sera affiché au-dessus des données du catalogue. Vous pouvez maintenant référencer cet ensemble filtré dans votre envoi de messages.

{% alert important %}
Les champs de chaîne de caractère comprenant plus de 1 000 caractères ne peuvent pas être filtrés.
{% endalert %}

Si vous utilisez du Liquid dans vos catalogues, tels que des attributs personnalisés ou des événements personnalisés, ceci peut entraîner le renvoi de résultats différents pour chaque utilisateur dans votre ensemble filtré.

![La section Ensembles filtrés dans un exemple de catalogue.][1]{: style="max-width:85%;"}

## Cas d’utilisation

Imaginons que vous possédiez un service de livraison de repas et désiriez envoyer un message personnalisé à vos utilisateurs ayant des préférences particulières concernant leurs repas selon la catégorie de nourriture qu’ils ont consultée le plus récemment. 

En utilisant un catalogue avec les informations de votre service de livraison de repas concernant le nom du plat, son prix, son image et sa catégorie, vous pouvez créer un ensemble filtré paramétré pour recommander trois plats sur la base de la catégorie consultée le plus récemment par un utilisateur.

![Un exemple d’un ensemble filtré pour un service de livraison de repas avec deux filtres : un qui identifie un type de produit comme étant un repas et l’autre identifiant la catégorie que l’utilisateur a visualisée le plus récemment. L’ensemble filtré est paramétré pour afficher de manière aléatoire les trois résultats renvoyés.][2]{: style="max-width:90%;"}

Pour utiliser ce catalogue et cet ensemble filtré dans une campagne, utilisez le modal **Ajouter une personnalisation** dans la section de composition de votre message lors de la création d’une campagne. Dans cet exemple, nous avons sélectionné le catalogue avec les informations de votre service de livraison de repas et l’ensemble filtré pour les recommandations de repas basées sur la catégorie visualisée le plus récemment. Ceci nous permet d’afficher le nom du plat et son prix. Pour construire plus en détail votre message, vous pouvez utiliser l’ensemble filtré pour ajouter également une image au plat recommandé en premier.

![Une carte de contenu avec l’en-tête « Vous allez ADORER ces repas très appréciés : » avec l’ensemble filtré "recommendations_be_recent_category" (la recommandation est la catégorie récente) dans la section de composition du message.][3]{: style="max-width:90%;"}

Par exemple, si vous avez un utilisateur pour lequel la catégorie visualisée le plus récemment est « Poulet ». En utilisant la personnalisation de l’ensemble et une campagne de cartes de contenu, nous pouvons envoyer des recommandations de trois plats comprenant du poulet pour cet utilisateur.

![Une carte de contenu avec l’image d’un poulet grillé au citron et une liste de trois plats recommandés comprenant du poulet sur la base de la catégorie affichée le plus récemment par l’utilisateur.][4]{: style="max-width:90%;"}

En utilisant la même personnalisation, nous pouvons également envoyer une recommandation pour trois plats à un utilisateur pour lequel la catégorie affichée le plus récemment est « Bœuf ».

![Une carte de contenu avec l’image d’un bœuf Stroganov et une liste de deux plats recommandés comprenant du bœuf sur la base de la catégorie affichée le plus récemment par l’utilisateur.][5]{: style="max-width:90%;"}


[1]: {% image_buster /assets/img_archive/catalog_filtered_sets1.png %}
[2]: {% image_buster /assets/img_archive/catalog_filtered_sets2.png %}
[3]: {% image_buster /assets/img_archive/catalog_filtered_sets3.png %}
[4]: {% image_buster /assets/img_archive/catalog_filtered_sets4.png %}
[5]: {% image_buster /assets/img_archive/catalog_filtered_sets5.png %}