---
nav_title: Inclusion CSS
article_title: Inclusion CSS
page_order: 5.1
description: "Le présent article de référence décrit comment utiliser l’inclusion CSS et certaines des meilleures pratiques associées."
channel:
  - email

---

# Inclusion CSS

> L’inclusion CSS est en quelque sorte un prétraitement des e-mails qui convertit votre style en feuille de style CSS dans le corps d’un e-mail HTML. Le terme « inlining » désigne le fait que les styles sont appliqués « inline » aux éléments HTML individuels.

Pour certains clients d'e-mail, l'insertion CSS peut améliorer le rendu des e-mails et contribuer à confirmer que vos e-mails sont conformes à vos attentes. Si la majorité des feuilles de style CSS sont déjà insérées ou si vous êtes certain que votre HTML et vos feuilles de style CSS sont compatibles avec les exigences de la plupart des clients de messagerie, il n'est peut-être pas nécessaire d'activer cette fonctionnalité. Les styles incorporés dynamiquement peuvent entrer en conflit avec vos styles en ligne existants et peuvent modifier l'aperçu prévu et le rendu des e-mails.

## Utilisation de l’inclusion CSS 

Vous pouvez contrôler si l'insertion CSS est activée ou désactivée pour n'importe quel message e-mail en utilisant la bascule **Activer l'insertion CSS dans l'** onglet **Informations d'envoi de** l'éditeur HTML.

![Case à cocher pour gérer l'insertion CSS dans le compositeur HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### État d’insertion par défaut

Vous pouvez définir un état activé ou désactivé par défaut de manière globale à partir de **Paramètres** > **Préférences d'e-mail.** Recherchez le paramètre pour l'**insertion CSS**. Ce paramètre détermine la valeur par défaut souhaitée par laquelle commencent tous les nouveaux messages e-mail. Notez que la modification de ce paramètre n’affectera pas vos e-mails existants. Vous pouvez également remplacer cette valeur par défaut à tout moment au moment de composer vos e-mails.

![Option d'insertion CSS par défaut dans les nouveaux e-mails, située dans les emplacements des e-mails.]({% image_buster /assets/img_archive/css-inline1.png %})

