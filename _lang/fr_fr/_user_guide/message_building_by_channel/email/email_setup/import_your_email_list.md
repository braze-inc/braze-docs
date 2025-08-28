---
nav_title: Importation de votre liste d’e-mails
article_title: Importer votre liste d’e-mails dans Braze
page_order: 4
page_type: reference
description: "Le présent article de référence couvre les bonnes pratiques d’importation de votre liste d’e-mails dans Braze."
channel: email

---

# Importer votre liste d’e-mails dans Braze {#importing-email-lists}

> Une étape importante pour vous définir comme un expéditeur de courrier électronique à succès est de vous assurer que vous avez une liste de courriels de haute qualité. Une gestion appropriée de la liste des courriels peut améliorer votre capacité de livrabilité et vous donner des résultats de campagne plus précis et plus propres.

## Considérations à prendre en compte avant l’importation

{% multi_lang_include email-via-sms-warning.md %}

### Validez vos listes d’e-mails

Avant d’importer votre liste d’e-mails dans Braze, vérifiez qu’elle comprend uniquement des adresses e-mail authentiques. Un taux de rebond élevé peut endommager votre réputation d’expéditeur de courrier électronique. 

Les services de nettoyage des listes d’e-mails peuvent faire cela pour vous en déterminant si l’adresse e-mail respecte la syntaxe correcte et possède les propriétés physiques d’une adresse e-mail, en vérifiant le domaine de messagerie et en se connectant au serveur de messagerie pour s’authentifier si l’adresse e-mail existe.

### Identifier vos utilisateurs engagés

Afin d’identifier vos utilisateurs les plus engagés, supprimez d’abord les utilisateurs inactifs depuis longtemps. Il est recommandé de ne pas envoyer de courrier électronique à des utilisateurs qui n’ont pas fait l’objet d’un e-mail dans plus de six mois, car cela peut endommager votre réputation d’expéditeur de courrier électronique. Lors de l'importation de votre liste d'e-mails, veillez à n'inclure que les utilisateurs qui ont ouvert un e-mail de votre part au cours des six derniers mois.

À long terme, vous devriez également envisager de mettre en œuvre une [politique de temporisation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).

### Éviter les listes de suppression

Si vous mettez en transition un fournisseur d’e-mails existant, assurez-vous de ne pas importer les utilisateurs à partir d’une liste de suppression. Les listes de suppression contiennent des adresses e-mail qui se sont désabonnées, qui ont traité vos e-mails comme des courriers indésirables ou qui ont généré un échec d'envoi définitif.

## Méthodes d’importation

Une fois que vous avez préparé votre liste d’e-mails, il existe plusieurs façons d’importer des utilisateurs dans Braze, par exemple via l’API REST de Braze ou des fichiers CSV. Pour en savoir plus, consultez notre article consacré à l ['importation d'utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

