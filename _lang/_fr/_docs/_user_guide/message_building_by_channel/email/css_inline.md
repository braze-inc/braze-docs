---
nav_title: CSS Inlining
article_title: CSS Inlining
page_order: 5
description: "L'inlining CSS peut améliorer le rendu des courriels. Cet article de référence traite de la façon d'activer la mise en page CSS et certaines bonnes pratiques."
channel:
  - Email
---

# CSS inlining

L'inlining CSS est une forme de prétraitement d'email qui déplace les styles dans une feuille de style CSS dans le corps d'un e-mail HTML. Le terme « inlining » désigne le fait que les styles sont appliqués « inline » à chaque élément HTML.

Pour certains clients de messagerie, la mise en page CSS peut améliorer la façon dont les courriels sont affichés et aider à assurer que vos courriels ressemblent à ce que vous attendez.

## Utilisation de l'inline CSS

Vous pouvez contrôler si l'inlining CSS est activé ou désactivé pour tout message de courriel via une case à cocher dans l'onglet **Sending Info** du Compositeur HTML, et l'onglet **Avancé** de l'Éditeur Glisser & Déposer.

| Compositeur HTML                                                        | Editeur Glisser & Déposer                                                    |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| !\[Gérer CSS inlining in HTML composer\]\[2\]{: style="max-width:80%;"} | !\[Gérer CSS inlining in Drag & Drop Editor\]\[3\]{: style="max-width:80%;"} |

De plus, vous pouvez définir un état par défaut sur ou éteint globalement à partir de **Gérer les paramètres** > **Paramètres de messagerie** > **CSS en ligne**. Ce paramètre garantit que tous les nouveaux courriels commencent par la valeur par défaut souhaitée. Notez que le changement de ce paramètre n'affectera aucun de vos courriels existants. Vous pouvez également remplacer cette valeur par défaut à tout moment lors de la rédaction de messages électroniques.

!\[CSS Inlining\]\[1\]
[1]:{% image_buster /assets/img_archive/css-inline1.png %} [2]:{% image_buster /assets/img_archive/css-inline2.png %} [3]:{% image_buster /assets/img_archive/css-inline3.png %}
