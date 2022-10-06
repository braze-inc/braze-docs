---
nav_title: Inlining CSS
article_title: Inlining CSS
page_order: 5
description: "L’inlining CSS peut améliorer la façon dont les e-mails sont rendus. Le présent article de référence décrit comment utiliser l’inlining CSS et certaines des meilleures pratiques associées."
channel:
  - E-mail

---

# Inlining CSS

L’inlining CSS est une forme de prétraitement de l’e-mail qui met votre style CSS dans le corps d’un e-mail HTML. Le terme « inlining » désigne le fait que les styles sont appliqués « inline » aux éléments HTML individuels.

Pour certains clients par e-mail, l’inlining CSS peut améliorer le rendu des e-mails et garantir que vos e-mails ont l’aspect que vous souhaitez.

## Utilisation du inlining CSS 

Vous pouvez contrôler si l’inlining CSS est activé ou désactivé pour tout e-mail via une case à cocher sur l’onglet **Sending Info (Informations d’envoià** du compositeur HTML, et sur l’onglet **Avancé** de l’éditeur Drag & Drop.

| Compositeur HTML | Éditeur Drag & Drop|
| --- | --- |
| ![Case à cocher pour gérer l’inlining CSS dans le compositeur HTML.][2]{: style="max-width:80%;"} | ![Basculer pour gérer l’inlining CSS dans l’éditeur Drag & Drop.][3]{: style="max-width:80%;"} |

De plus, vous pouvez définir un statut par défaut global (Activé/Désactivé) dans **Manage Settings (Gérer les paramètres)** > **Email Settings (Paramètres des E-mails)** > **Inline CSS**. Ce paramètre garantit que tous les nouveaux e-mails commencent par la valeur par défaut souhaitée. Notez que la modification de ce paramètre n’affectera pas vos e-mails existants. Vous pouvez également remplacer cette valeur par défaut à tout moment au moment de composer vos e-mails.

![Option par défaut « Inlining CSS pour les nouveaux e-mails » dans les paramètres de messagerie.][1]

[1]:{% image_buster /assets/img_archive/css-inline1.png %}
[2]:{% image_buster /assets/img_archive/css-inline2.png %}
[3]:{% image_buster /assets/img_archive/css-inline3.png %}
