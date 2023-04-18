---
nav_title: API d’exportation
article_title: API d’exportation
page_order: 8
page_type: reference
description: "Cet article de référence explique pourquoi il est parfois préférable d’exporter programmatiquement les données du tableau de bord dans un fichier JSON plutôt que directement dans un fichier CSV."
platform: API

---

# API d’exportation

> Les API d’exportation de Braze vous permettent d’exporter programmatiquement des données du tableau de bord dans un fichier JSON. Consultez nos [API d’exportation][24] pour obtenir la liste des données auxquelles vous pouvez accéder, ainsi que les instructions et des d’échantillon de  code pour l’exportation.

Voici certaines des raisons qui justifient d’utiliser cette méthode plutôt qu’une exportation directe du tableau de bord vers un fichier CSV :

 - Votre fichier est très volumineux. À partir de notre tableau de bord, vous pouvez exporter un CSV de 500 000 lignes maximum. Si vous exportez des données sur un segment avec plus de 500 000 utilisateurs, vous devez utiliser notre API d’exportation, qui n’impose aucune limite sur la quantité que vous pouvez exporter.
 -  Vous souhaitez interagir avec les données par programmation.

{% alert tip %}
Pour obtenir de l’aide sur les exportations de CSV et l’API, consultez notre article [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[24]: {{site.baseurl}}/api/endpoints/export/
