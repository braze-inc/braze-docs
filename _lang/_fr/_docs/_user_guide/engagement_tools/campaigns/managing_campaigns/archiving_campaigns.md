---
nav_title: Archivage des campagnes
article_title: Archivage des campagnes
page_order: 1
page_type: Référence
description: "Cet article de référence décrit comment archiver une campagne préexistante, les effets de l'archivage d'une campagne, et comment reprendre cette campagne si nécessaire."
tool:
  - Campagnes
---

# Archivage des campagnes

> Cet article de référence décrit comment archiver une campagne préexistante, les effets de l'archivage d'une campagne, et comment reprendre cette campagne si nécessaire.

Si vous souhaitez empêcher une campagne de l'envoyer ou de l'effacer de votre tableau de bord, vous pouvez l'archiver. Allez à la page **Campagnes** , cliquez sur l’icône d’équipement à côté du nom de la campagne et cliquez sur **Archive**.

!\[Archiving\]\[1\]

Archiver une campagne accomplira ce qui suit :

- Aucun autre message de cette campagne ne sera envoyé. Dans le cas de messages intégrés à l'application, aucun autre message dans l'application ne sera affiché aux utilisateurs.
- Les indicateurs de la campagne seront supprimés de :
    - Le graphique des statistiques détaillées sur la page **Aperçu**
    - Le graphique des statistiques détaillées sur la page **Revenus**
    - Le graphique des événements personnalisés au fil du temps

Il y a aussi des actions de masse que vous pouvez utiliser, comme la désactivation et l'archivage de plusieurs campagnes en cochant les cases à côté des campagnes et en cliquant sur le bouton correspondant.

!\[Archives sélectionnées\]\[3\]

Pour afficher les messages archivés de la page **Campagnes** , sélectionnez le dossier **Archivé**.

!\[Include Archived\]\[2\]

## Désarchivage des campagnes

En cliquant sur une campagne archivée vous permettra de voir ses résultats passés, vous ne pourrez pas modifier la campagne. Vous devrez désarchiver la campagne pour la modifier. Pour désarchiver une campagne, vous devez sélectionner la campagne dans le dossier **Archivé** et cliquer sur **Désarchiver la sélection**.

!\[Désarchiver la campagne\]\[4\]

La désarchivage d'une campagne ne la rend pas vivante. Cela déplacera simplement votre campagne vers le dossier de campagne **Active** où vous pourrez faire des modifications et examiner comment la campagne est configurée. À ce stade, votre campagne sera interrompue et n'enverra aucun message.

Si vous souhaitez reprendre la campagne et commencer à envoyer des messages, cliquez sur l'icône d'engrenage à côté de la campagne et sélectionnez **Reprendre**.

!\[Campagne de reprise \]\[5\]

{% alert warning %}
Lorsque vous archivez un Segment, toutes les campagnes qui l'utilisent seront __également archivées__.
{% endalert %}
[1]: {% image_buster /assets/img_archive/Archiving.png %} [2]: {% image_buster /assets/img_archive/Include_archived.png %} [3]: {% image_buster /assets/img_archive/Archive_pause_selected ng %} [4]: {% image_buster /assets/img_archive/unarchive_selected.png %} [5]: {% image_buster /assets/img_archive/resume_unarchived.png %}
