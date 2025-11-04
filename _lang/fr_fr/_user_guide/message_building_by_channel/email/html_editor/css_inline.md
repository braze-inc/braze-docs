---
nav_title: Insertion CSS
article_title: Insertion CSS
page_order: 5.1
description: "Cet article de référence explique comment activer l'insertion CSS et présente quelques bonnes pratiques."
channel:
  - email

---

# Insertion CSS

> L'insertion CSS est une forme de prétraitement des e-mails qui déplace les styles d'une feuille de style CSS dans le corps d'un e-mail HTML. Le terme "inlining" fait référence au fait que les styles sont appliqués "inline" à des éléments HTML individuels.

Pour certains clients d'e-mail, l'insertion CSS peut améliorer le rendu des e-mails et contribuer à confirmer que vos e-mails sont conformes à vos attentes. Si la majorité des feuilles de style CSS sont déjà insérées ou si vous êtes certain que votre HTML et vos feuilles de style CSS sont compatibles avec les exigences de la plupart des clients de messagerie, il n'est peut-être pas nécessaire d'activer cette fonctionnalité. Les styles incorporés dynamiquement peuvent entrer en conflit avec vos styles en ligne existants et peuvent modifier l'aperçu prévu et le rendu des e-mails.

## Utilisation de l'insertion CSS

Vous pouvez contrôler si l'insertion CSS est activée ou désactivée pour n'importe quel message e-mail en utilisant la bascule **Activer l'insertion CSS dans l'** onglet **Informations d'envoi de** l'éditeur HTML.

\![Case à cocher pour gérer l'insertion CSS dans le compositeur HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### État de l'inlining par défaut

Vous pouvez définir un état activé ou désactivé par défaut de manière globale à partir de **Paramètres** > **Préférences d'e-mail.** Emplacement/localisation du paramètre pour l'**insertion CSS.** Ce paramètre détermine la valeur par défaut souhaitée par laquelle commencent tous les nouveaux messages e-mail. Notez que la modification de ce paramètre n'affectera aucun de vos messages e-mail existants. Vous pouvez également modifier cette valeur par défaut à tout moment lors de la rédaction des messages e-mail.

!Option Inline CSS sur les nouveaux e-mails par défaut située dans les emplacements de l'e-mail.]({% image_buster /assets/img_archive/css-inline1.png %})

