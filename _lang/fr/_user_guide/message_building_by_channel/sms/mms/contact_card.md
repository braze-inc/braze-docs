---
nav_title: Cartes de visite
article_title: Cartes de visite
page_order: 3
description: "Cet article de référence explique comment créer une carte de visite à inclure dans vos messages MMS et SMS."
page_type: reference
channel:
  - MMS
  
---

# Cartes de visite 

> Les cartes de visite (parfois appelées vCard ou Virtual Contact Files (VCF)) sont un format de fichier normalisé pour l’envoi d’informations professionnelles et de contact qui peuvent être facilement importées dans des carnets d’adresses ou de contacts. 

Les cartes de visite peuvent être créées [par programmation](https://www.twilio.com/blog/send-vcard-twilio-sms) et chargées dans la [médiathèque]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) de Braze, ou créées via notre générateur intégré de cartes de visite. Ces cartes peuvent recevoir des propriétés communes, telles que le nom de votre entreprise, le numéro de téléphone, l’adresse, l’e-mail et une petite photo. Pour commencer à créer des cartes de contact, assurez-vous d’abord d’avoir paramétré l’utilisation de MMS dans Braze.

## Générateur de cartes de visite

<script src="https://fast.wistia.com/embed/medias/7m77mdfr4y.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_7m77mdfr4y videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/7m77mdfr4y/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

### Étape 1 : Attribuer un nom

Les cartes de visite peuvent être créées à partir de l’éditeur de SMS et MMS. Cliquez sur l’onglet **Générateur de cartes de visite** pour commencer.

Vous serez ensuite invité à saisir le nom ou surnom de votre entreprise. Il s’agit du nom que vos utilisateurs verront lorsqu’ils enregistrent la carte. Une limite de 20 caractères est appliquée pour que l’utilisateur puisse voir le nom ou l’alias complet de l’entreprise dans ses contacts et son application de messagerie. 

![]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Étape 2 : Attribuer un numéro de téléphone

Sélectionnez le groupe d’abonnement et le numéro de téléphone souhaités dans les options déroulantes disponibles. Ce numéro est indiqué sur votre carte de visite et disponible sur le téléphone pour recevoir des messages texte une fois enregistré.

Notez que les codes alphanumériques ne sont pas compatibles avec les messages bidirectionnels et ne sont pas pris en charge par les cartes de contact.

### Étape 3 : Champs facultatifs

![]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

**Photo du contact de la carte de visite**<br>
Vous pouvez télécharger une photo miniature pour votre carte de visite. Nous recommandons d’utiliser une image JPEG ou PNG de 240x240. Toutes les images haute résolution téléchargées seront redimensionnées en 240x240 pour garantir la livraison de votre message, sachant que les messages MMS de plus de 5 Mo peuvent engendrer une erreur.

**Autres informations**<br>
D’autres champs vous permettent d’insérer votre nom, sous-en-tête, adresse et autres coordonnées pouvant s’avérer utiles pour votre utilisateur. 

<br>

### Étape 4 : Enregistrer votre carte de visite

Une fois que vous avez renseigné tous les champs nécessaires, cliquez sur **Générer une carte de visite** pour qu’elle soit automatiquement jointe à votre campagne ou Canvas. À partir de là, vous pouvez ajouter un message, tester votre carte de visite et lancer votre campagne ou Canvas.

La carte de visite est également enregistrée dans la [médiathèque]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) pour être facilement réutilisée dans les campagnes et les Canvas à venir.

## Ajout d’une carte de visite existante

Pour ajouter une carte de visite existante, créez une campagne ou un Canvas et sélectionnez le groupe d’abonnement souhaité. L’option **Ajouter un média** apparaît dans la fenêtre de l’éditeur de messages. Vous pouvez y télécharger un fichier de carte de visite existant ou en rechercher un dans la médiathèque.
