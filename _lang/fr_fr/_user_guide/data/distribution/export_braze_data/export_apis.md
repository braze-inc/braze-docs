---
nav_title: "API d'exportation"
article_title: "API d'exportation"
page_order: 8
page_type: reference
description: "Cet article de référence explique pourquoi vous pouvez exporter par programme un fichier JSON de données de tableau de bord, plutôt que d'exporter un fichier CSV directement à partir du tableau de bord."
platform: API

---

# API d'exportation

> Cette page couvre les API d'exportation de Braze, qui vous permettent d'exporter par programme un fichier JSON de données de tableau de bord. Reportez-vous à [Export endpoints]({{site.baseurl}}/api/endpoints/export/) pour obtenir une liste des données auxquelles vous pouvez accéder, ainsi que des instructions et un exemple de code pour l'exportation.

## Quand utiliser les API d'exportation au lieu des téléchargements CVS ?

Il y a quelques raisons pour lesquelles vous préférerez cette méthode à l'exportation d'un CSV directement à partir du tableau de bord :

 - Votre fichier est très volumineux. Depuis notre tableau de bord, vous pouvez exporter un fichier CSV contenant au maximum 500 000 lignes. Si vous exportez des données sur un segment comptant plus de 500 000 utilisateurs, vous devrez utiliser notre API d'exportation, qui n'impose aucune limite à la quantité de données que vous pouvez exporter.
 -  Vous souhaitez interagir avec les données de manière programmatique.

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, reportez-vous à la [résolution des problèmes d'exportation.]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)
{% endalert %}

