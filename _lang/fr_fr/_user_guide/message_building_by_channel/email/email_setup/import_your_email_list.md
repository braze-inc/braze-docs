---
nav_title: "Importation de votre liste d'e-mails"
article_title: "Importer votre liste d'e-mails dans Braze"
page_order: 4
page_type: reference
description: "Cet article de référence couvre les meilleures pratiques pour l'importation de votre liste d'e-mails dans Braze."
channel: email

---

# Importer votre liste d'e-mails dans Braze {#importing-email-lists}

> Une étape importante pour devenir un expéditeur d'e-mails performant consiste à s'assurer que vous disposez d'une liste d'e-mails de grande qualité. Une bonne gestion des listes d'e-mails peut améliorer votre livrabilité et vous permettre d'obtenir des résultats de campagne plus précis et plus nets.

## Points à prendre en compte avant d'importer

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Validez vos listes d'e-mails

Avant d'importer votre liste d'e-mails dans Braze, vérifiez qu'elle ne contient que des adresses e-mail authentiques. Un taux de rebond élevé peut nuire à la réputation de votre expéditeur d'e-mails. 

Les services de nettoyage de listes d'e-mails peuvent le faire pour vous en déterminant si l'adresse e-mail suit la syntaxe correcte et possède les propriétés physiques d'une adresse e-mail, en vérifiant le domaine de l'e-mail et en se connectant au serveur d'e-mail pour authentifier l'existence de l'adresse e-mail.

### Vérifier si une adresse e-mail est déjà associée à un utilisateur

Avant de créer un utilisateur via l'API ou le SDK, appelez le point de terminaison [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) et spécifiez l'adresse `email_address` de l'utilisateur. S'il renvoie un profil utilisateur, cela signifie que l'utilisateur de Braze est déjà associé à cette adresse e-mail.

Nous vous recommandons vivement de rechercher des adresses e-mail uniques lors de la création de nouveaux utilisateurs et d'éviter de transmettre ou d'importer des utilisateurs ayant la même adresse e-mail. Dans le cas contraire, vous risquez d'avoir des conséquences imprévues sur l'envoi de messages, le ciblage, la création de rapports et d'autres fonctionnalités.

Par exemple, supposons que vous ayez des profils en double, mais que certains événements et attributs personnalisés ne se trouvent que sur un seul profil. Lorsque vous essayez de déclencher des campagnes ou des Canvases avec plusieurs critères, Braze ne peut pas identifier l'utilisateur comme éligible parce qu'il y a deux profils utilisateur. Par ailleurs, si une campagne cible une adresse e-mail partagée par deux utilisateurs, la page **Recherche d'utilisateurs** indiquera que les deux profils utilisateurs ont reçu la campagne.

### Identifiez vos utilisateurs engagés

Afin d'identifier les utilisateurs les plus engagés, commencez par supprimer les utilisateurs les plus inactifs. La meilleure pratique consiste à ne pas envoyer d'e-mail aux utilisateurs qui n'ont pas répondu à un e-mail depuis plus de six mois, car cela peut nuire à votre réputation d'expéditeur d'e-mails. Lors de l'importation de votre liste d'e-mails, veillez à n'inclure que les utilisateurs qui ont ouvert un e-mail de votre part au cours des six derniers mois.

À long terme, vous devriez également envisager de mettre en œuvre une [politique de temporisation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).

### Évitez les listes de suppression

Si vous quittez un fournisseur d'e-mail existant, veillez à ne pas importer d'utilisateurs à partir d'une liste de suppression. Les listes de suppression ont pour fonctionnalité de répertorier les adresses e-mail qui se sont désabonnées, qui ont marqué vos e-mails comme spam ou qui ont fait l'objet d'un échec d'envoi définitif.

## Méthodes d'importation

Une fois votre liste d'e-mails préparée, il existe plusieurs façons d'importer des utilisateurs dans Braze, notamment via l'API REST de Braze ou des fichiers CSV. Pour en savoir plus, consultez notre article consacré à l ['importation d'utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

