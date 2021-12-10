---
nav_title: Changement de l'attribut personnalisé ou du type de données de l'événement
article_title: Changement de l'attribut personnalisé ou du type de données de l'événement
page_order: 0
page_type: Solution
description: "Cet article vous guide dans la façon de modifier le type de données d'un attribut personnalisé ou d'un événement personnalisé, et les implications de ce changement."
---

# Changement d'attribut personnalisé ou de type de données d'événement

Pour modifier le type de données d'un attribut ou d'un événement personnalisé, depuis le tableau de bord Braze, accédez à __Gérer les paramètres__ et sélectionnez l'onglet __Attributs personnalisés__ ou __Événements personnalisés__.

!\[Change Data Type of Custom Attirbutes\]\[1\]

Si vous devez modifier le type de données d'un attribut personnalisé ou d'un événement (par exemple, d'une date `` à une chaîne ``)...

- Les filtres pertinents dans les segments, les campagnes, les toiles ou autres lieux en utilisant l'attribut ou l'événement modifié ne sont pas automatiquement mis à jour. Avant de pouvoir modifier les attributs, vous devez supprimer le filtre ou les déclencheurs qui les référencent.
- Les données utilisateur __ne seront pas mises à jour rétroactivement__. Si l'attribut modifié était sur un profil avant le changement de type de données, alors cette valeur sera toujours l'ancien type de données. Cela peut faire tomber les utilisateurs des segments qui contiennent l'attribut changé. Le filtre va rechercher activement le nouveau type de données, mais si un profil a toujours le type de données précédent, cet utilisateur sera maintenant exclu du Segment. Ces utilisateurs doivent être mis à jour pour revenir aux segments appropriés. Vous pouvez le faire via Braze [`utilisateur/piste` endpoint]({{site.baseurl}}/api/endpoints/user_data/#custom-attribute-data-types).
- Les nouvelles données entrantes ne seront pas acceptées si ce n'est pas le nouveau type de données. Par exemple, un appel API au point de terminaison `utilisateur/piste` qui contient le type de données précédent pour un attribut modifié ne sera pas accepté. Vous devez appeler le nouveau type de données.

_Dernière mise à jour le 5 mai 2021_
[1]: {% image_buster /assets/img/change_custom_attribute.png %}