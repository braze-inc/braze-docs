---
nav_title: Exporter les APIs
article_title: Exporter les APIs
page_order: 8
page_type: Référence
description: "Cet article de référence décrit pourquoi vous pourriez exporter par programmation un fichier JSON de données du tableau de bord, en exportant un CSV directement depuis le tableau de bord."
platform: API
---

# Exporter les APIs

Les API d'exportation de Braze vous permettent d'exporter par programmation un fichier JSON de données du tableau de bord. Notre [page de documentation sur les API d'exportation][24] contient une liste de données auxquelles vous pouvez accéder. ainsi que des instructions et des exemples de code pour l'exportation.

Il y a quelques raisons pour lesquelles vous préféreriez cette méthode plutôt que d'exporter un CSV directement depuis le tableau de bord :

 - Votre fichier est très volumineux. À partir de notre tableau de bord, vous pouvez exporter un CSV avec un maximum de 500.000 lignes. Si vous exportez des données sur un segment avec plus de 500 000 utilisateurs, vous devrez utiliser notre API d'exportation, qui ne limite pas le montant que vous pouvez exporter.
 -  Vous souhaitez interagir avec les données de manière programmatique.

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[24]: {{site.baseurl}}/developer_guide/rest_api/export/#export
