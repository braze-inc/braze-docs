---
nav_title: Cartes de contact
article_title: Cartes de contact
page_order: 3
description: "Cet article de référence traite de la façon de créer une carte de contact à inclure dans vos messages MMS et SMS."
page_type: Référence
channel:
  - MMS
---

# Cartes de contact

> Les Cartes de contact (parfois appelées vCard ou fichiers de contact virtuel (VCF)) sont un format de fichier normalisé pour envoyer des informations commerciales et de contact qui peuvent être facilement importées dans des carnets d'adresses ou des carnets de contacts.

Les fiches de contact peuvent être créées [par programme](https://www.twilio.com/blog/send-vcard-twilio-sms) et téléchargées dans la médiathèque [Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) ou créées via notre générateur de carte de contact intégré. Vous pouvez assigner des propriétés communes à ces cartes, telles que le nom de votre entreprise, le numéro de téléphone, l'adresse, l'e-mail et une petite photo.

## Générateur de carte de contact

<script src="https://fast.wistia.com/embed/medias/7m77mdfr4y.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_7m77mdfr4y videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/7m77mdfr4y/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

### Étape 1 : Assigner un nom

Les fiches de contact peuvent être créées à partir du composant SMS et MMS. Sélectionnez l'onglet **Générateur de carte de contact** pour commencer.

Ensuite, vous serez invité à entrer le nom ou le pseudo de votre entreprise. C'est le nom que vos utilisateurs verront quand ils enregistreront la carte. Une limite de 20 caractères est appliquée pour s'assurer que l'utilisateur peut voir le nom ou l'alias de votre entreprise dans son application de contacts et de messagerie.

![Contacter le compositeur de la carte]({% image_buster /assets/img/sms/contact_card1.png %})

### Étape 2 : Assigner un numéro de téléphone

Sélectionnez le groupe d'abonnement et le numéro de téléphone désiré dans les options déroulantes disponibles. Ce numéro sera répertorié dans votre carte de contact et disponible sur leur téléphone à texte une fois enregistré.

Notez que les codes alphanumériques ne sont pas compatibles avec la messagerie bidirectionnelle et ne sont pas pris en charge pour les Cartes de contact.

### Étape 3 : Champs optionnels

![Options de la carte de contact]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

**Contact Card Photo**<br> Vous pouvez télécharger une photo de contact miniature facultative pour votre fiche de contact. Nous recommandons une image de 240x240 jpeg ou png. Toutes les images haute résolution téléchargées seront redimensionnées à 240x240 pour assurer la délivrabilité de votre message, car les messages MMS de plus de 5 Mo peuvent échouer.

**Autres informations**<br> D'autres champs vous permettent d'insérer votre nom, sous-en-tête, adresse et autres informations de contact que votre utilisateur peut vouloir avoir à portée de main.

<br>

### Étape 4 : Enregistrement de votre fiche de contact

Une fois que vous aurez entré tous les champs nécessaires, cliquez sur **Générer la fiche de contact**et elle sera automatiquement jointe à votre campagne ou à votre Canvas. À partir de là, vous pouvez ajouter un message, tester votre carte de contact, et lancer votre campagne ou Canvas.

La fiche de contact sera également enregistrée dans la [Médiathèque]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) pour la réutiliser facilement dans les futures campagnes et Canvases.

## Ajout d'une fiche de contact existante

Pour ajouter une fiche de contact existante, créez une campagne ou Canvas et sélectionnez le groupe d'abonnement souhaité. Ensuite, une option **Ajouter un média** apparaîtra dans la fenêtre du compositeur de messages. Ici, vous pouvez télécharger un fichier de Contact Card existant ou en trouver un dans la médiathèque.
