---
nav_title: Archiver des campagnes
article_title: Archiver des campagnes
page_order: 2
page_type: reference
description: "Le présent article de référence explique comment archiver une campagne préexistante, les effets de l’archivage d’une campagne et comment relancer cette campagne si nécessaire."
tool:
  - Campaigns

---

# Archiver des campagnes

> Si vous souhaitez empêcher une campagne de s’envoyer ou l’effacer de votre tableau de bord, vous pouvez l’archiver. Accédez à la page **Campaigns**, cliquez sur l’icône d’engrenage en regard de la campagne et cliquez sur **Archive** (Archiver).

![][1]

Lorsque vous archivez une campagne, aucun autre message de cette campagne ne sera envoyé. Dans le cas des messages in-app, aucun autre message in-app de cette campagne ne sera affiché aux utilisateurs.

Il existe également des actions par lot que vous pouvez utiliser, telles que la désactivation et l’archivage de plusieurs campagnes en cochant les cases situées à côté des campagnes et en cliquant sur le bouton approprié.

![][3]

Pour afficher les messages archivés depuis la page **Campaigns**, sélectionnez le dossier **Archived** (Archivé).

![][2]

## Désarchiver des campagnes

Lorsque vous cliquez sur une campagne archivée, vous pourrez afficher ses résultats passés. Vous ne pourrez pas modifier la campagne. Vous devrez désarchiver la campagne afin de la modifier. Pour désarchiver une campagne, vous devez sélectionner la campagne dans le dossier **Archived** (Archivé) et cliquer sur **Unarchive Selected** (Désarchiver la sélection).

![][4]

Désarchiver une campagne ne le rend pas active. Elle sera seulement déplacée vers me dossier de campagne **Active** (Active) où vous pouvez réaliser des modifications et revoir la manière dont elle est configurée. À ce stade, votre campagne sera arrêtée et n’enverra aucun message. 

Si vous souhaitez reprendre la campagne et commencer à envoyer des messages, cliquez sur l’icône d’engrenage à côté de la campagne et sélectionnez **Resume** (Reprendre).

![][5]

{% alert warning %}
Lorsque vous archivez un segment, toutes les campagnes qui l’utilisent seront également archivées.
{% endalert %}

[1]: {% image_buster /assets/img_archive/Archiving.png %}
[2]: {% image_buster /assets/img_archive/Include_archived.png %}
[3]: {% image_buster /assets/img_archive/Archive_pause_selected.png %}
[4]: {% image_buster /assets/img_archive/unarchive_selected.png %}
[5]: {% image_buster /assets/img_archive/resume_unarchived.png %}
