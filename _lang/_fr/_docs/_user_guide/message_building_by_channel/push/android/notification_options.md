---
nav_title: "Options de notification (Android)"
article_title: Options de notification push
page_order: 2
page_type: Référence
description: "Cet article de référence couvre plusieurs options de notification Android et comment les utiliser au mieux dans les campagnes de Braze."
platform: Android
channel:
  - Pousser
---

# Options de notification Android

> Si vous souhaitez catégoriser vos messages et les regrouper dans la barre de notification de votre utilisateur, vous pouvez utiliser la fonctionnalité des canaux de notification d'Android via Braze.

Créez votre campagne de push Android, puis regardez en haut de l'onglet **Composer** pour la liste déroulante **Canal de Notification**.

!\[notificationchanneldropdown\]\[28\]{: style="max-width:60%;" }

Sélectionnez votre canal de notification dans la liste déroulante. Vous devez également sélectionner un canal de secours dans le cas où vos paramètres de canal de notification ne fonctionneraient pas.

Si vous n'avez aucun [canal de notification]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) listé ici, vous pouvez en ajouter un en utilisant l'ID du canal de notification. Contactez vos développeurs pour identifier vos identifiants de canal de notification ou pour créer de nouveaux identifiants au besoin.

Pour ajouter un ID de notification à votre canal de notification, cliquez sur **Gérer le canal de notification** dans le menu déroulant **Canal de notification** et remplissez les champs obligatoires. Les canaux de notification doivent être définis sur l'application avant de pouvoir être utilisés sur la plateforme Braze.

!\[managenotchannel\]\[29\]{: style="max-width:80%;" }
[28]: {% image_buster /assets/img_archive/notification_channel_dropdown.png %} [29]: {% image_buster /assets/img_archive/notification_channels.png %}
