---
nav_title: Cartes de visite
article_title: Cartes de visite
page_order: 3
description: "Cet article de référence explique comment créer une carte de contact à inclure dans vos envois MMS et SMS."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS
  
---

# Cartes de contact 

> Les cartes de contact (parfois appelées vCard ou Virtual Contact Files (VCF)) sont un format de fichier standardisé pour l'envoi d'informations professionnelles et de contacts qui peuvent être facilement importées dans des carnets d'adresses ou des carnets de contacts. 

Les cartes de contact peuvent être créées de [manière programmatique](https://www.twilio.com/blog/send-vcard-twilio-sms) et téléchargées dans la [bibliothèque multimédia de]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) Braze ou créées via notre générateur de cartes de contact intégré. Ces cartes peuvent recevoir des propriétés communes, telles que le nom de votre entreprise, le numéro de téléphone, l’adresse, l’e-mail et une petite photo. Pour commencer à créer des cartes de contact, assurez-vous d'abord que vous êtes configuré pour utiliser les MMS dans Braze.

## Générateur de cartes de contact

### Étape 1 : Attribuer un nom

Des cartes de contact peuvent être créées à partir du compositeur de SMS et de MMS. Sélectionnez l'onglet **Générateur de carte de contact** pour commencer.

Vous serez ensuite invité à saisir le nom ou surnom de votre entreprise. Il s’agit du nom que vos utilisateurs verront lorsqu’ils enregistrent la carte. Une limite de 20 caractères est imposée pour garantir que l'utilisateur puisse voir le nom complet de votre entreprise ou alias dans ses contacts et son application de messagerie. 

![L'onglet du générateur de cartes de contact.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Étape 2 : Attribuer un numéro de téléphone

Sélectionnez le groupe d'abonnement et le numéro de téléphone souhaité dans les options déroulantes disponibles. Ce numéro figurera dans votre carte de contact et sera disponible sur leur téléphone pour envoyer un SMS après avoir été enregistré.

Notez que les codes alphanumériques ne sont pas compatibles avec l'envoi de messages bidirectionnels et ne sont pas pris en charge pour les cartes de contact.

### Étape 3 : Champs facultatifs

![Champs facultatifs pour le générateur de cartes de contact.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Télécharger la carte de contact photo de contact

Vous pouvez télécharger une photo miniature facultative pour votre carte de contact. Nous recommandons une image JPEG ou PNG de 240 x 240 px. Toutes les images haute résolution téléchargées seront redimensionnées à 240 x 240 px pour garantir la délivrabilité de votre message, car les messages MMS de plus de 5 Mo peuvent échouer.

#### Ajouter un complément d'information

D'autres champs vous permettent d'insérer votre nom, votre sous-titre, votre adresse et d'autres informations de contact que votre utilisateur pourrait souhaiter avoir à sa disposition. 

### Étape 4 : Enregistrer votre carte de visite

Une fois que vous avez saisi tous les champs nécessaires, cliquez sur **Générer une carte de contact** et elle sera automatiquement jointe à votre campagne ou Canvas. À partir de là, vous pouvez ajouter un message, tester votre carte de contact et lancer votre campagne ou Canvas.

La carte de contact sera également enregistrée dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) pour être facilement réutilisée dans de futures campagnes et toiles.

## Ajout d’une carte de visite existante

Pour ajouter une carte de contact existante, créez une campagne ou un canvas et sélectionnez le groupe d'abonnement de votre choix. L’option **Ajouter un média** apparaît alors dans la fenêtre de l’éditeur de messages. Ici, vous pouvez télécharger un fichier de carte de contact existant ou en trouver un dans la bibliothèque multimédia.
