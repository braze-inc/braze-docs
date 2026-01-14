---
nav_title: Modifier un attribut personnalisé ou un type d’événement
article_title: Modifier un attribut personnalisé ou un type d’événement
page_order: 1

page_type: solution
description: "Cet article d’aide vous explique comment modifier le type de données d’un attribut personnalisé ou d’un événement personnalisé, ainsi que les implications si vous le faites."
---

# Modifier un attribut personnalisé ou un type d’événement

Pour modifier le type de données d'un attribut ou d'un événement personnalisé, à partir du tableau de bord de Braze, naviguez vers **Paramètres des données** et sélectionnez **Attributs personnalisés** ou **Événements personnalisés**.

![L'onglet Attributs personnalisés permet de modifier l'attribut ou le type de données]({% image_buster /assets/img/change_custom_attribute.png %})

Si vous devez modifier le type de données d'un attribut ou d'un événement personnalisé (par exemple, remplacer `time` par `string`), tenez compte des éléments suivants :

- Les filtres correspondants dans les segments, campagnes, Canvas ou autres emplacements utilisant l’attribut ou l’événement modifié ne seront pas automatiquement mis à jour. Avant de pouvoir modifier les attributs, vous devez arrêter toutes les campagnes ou les campagnes utilisant les attributs dans les segments ou les filtres, et supprimer les attributs des filtres qui les référencent.
- Les données utilisateur ne seront pas mises à jour rétroactivement. Si l’attribut modifié était sur un profil utilisateur avant le changement de type de données, cette valeur sera toujours l’ancien type de données. Cela peut faire sortir des utilisateurs des segments qui contiennent l’attribut modifié. Le filtre recherche activement le nouveau type de données, mais si un profil a toujours le type de données précédent, cet utilisateur sera désormais exclu du segment. Ces utilisateurs doivent être mis à jour pour revenir dans les segments appropriés. Vous pouvez le faire avec l'[endpoint`users/track`.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- Les nouvelles données ne seront pas acceptées si elles ne correspondent pas au nouveau type de données. Par exemple, un appel API à l’endpoint `users/track` qui contient le type de données précédent pour un attribut modifié ne sera pas accepté. Vous devez appeler le nouveau type de données.

{% alert important %}
La possibilité d'empêcher la détection automatique de mettre à jour le type de données de l'attribut personnalisé est actuellement en accès anticipé. Contactez votre gestionnaire de satisfaction client si vous souhaitez participer à cet accès anticipé.
{% endalert %}

_Dernière mise à jour le 8 février 2024_

