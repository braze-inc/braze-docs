---
nav_title: Créer une campagne par MMS
article_title: Créer une campagne par MMS
page_order: 2
description: "Cet article de référence couvre les étapes impliquées dans la création, l’envoi et la prévisualisation d’un message MMS."
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# Créer une campagne MMS

> Cet article contient des informations spécifiques à la composition de MMS, qui fait partie du compositeur de SMS. Pour plus d'informations sur le compositeur de SMS/MMS, reportez-vous au [compositeur de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).

## Principes de base d’envoi MMS

### Sélectionnez votre groupe d'abonnement

Vous devez désigner un groupe d’abonnement avec des numéros de téléphone MMS activés à cibler (il peut s’agir de codes courts ou longs).

### Corps du message d'entrée

Saisissez des types d'images PNG, JPEG, GIF et VCF à partir de la bibliothèque multimédia ou indiquez une URL. Une seule image est prise en charge.

### Comprenez comment sont envoyés les MMS

Les MMS sont facturés à un tarif différent de celui des SMS, et tous les opérateurs n'acceptent pas les MMS. Dans ces cas spécifiques, Twilio convertit automatiquement le MMS en un lien d’image sur lequel l’utilisateur peut cliquer.

### Utilisez des cartes de contact

Les cartes de contact (parfois appelées vCard ou Virtual Contact Files (vcf)) sont un format de fichier standardisé pour l'envoi d'informations professionnelles et de contacts qui peuvent être facilement importées dans des carnets d'adresses ou des carnets de contacts. Ces cartes peuvent être créées de [manière programmatique](https://www.twilio.com/blog/send-vcard-twilio-sms) et téléchargées dans la bibliothèque multimédia de Braze ou créées via notre [générateur de cartes de contact]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) intégré.

## Création d’un message MMS

Pour créer un message MMS, votre groupe d'abonnement doit être configuré pour l'envoi de MMS. Pour le savoir, consultez la balise MMS lors de la sélection d’un groupe d’abonnement. Lorsque vous sélectionnez un groupe d'abonnement compatible MMS, vous avez la possibilité de télécharger une image, de faire référence à l'URL d'une image ou d'inclure une carte de contact.

![L'onglet "Composer" pour rédiger votre message.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Spécifications des images

| **Spécifications de l'image** | **Propriétés recommandées** |
|--------------------------|----------------------------|
| Taille                     | Jusqu'à 600 KB        |
| Types de fichiers               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Prévisualisation d’un message MMS

Braze fournit un aperçu de l'image que vous avez téléchargée dans le panneau d'**aperçu** du compositeur de messages. 

{% alert note %}
L’ordre des ressources SMS/MMS ne peut pas être personnalisé. L’ordre dépend du téléphone qui reçoit ce message.
{% endalert %}

![Exemple de message : "Prêt pour la maison gym...at?". L'aperçu montre le message et l'image envoyés en tant que textes.]({% image_buster /assets/img/sms/mms_preview.png %})
