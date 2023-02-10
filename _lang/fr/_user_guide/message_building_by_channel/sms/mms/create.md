---
nav_title: Créer une campagne par MMS
article_title: Créer une campagne par MMS
page_order: 2
description: "Cet article de référence couvre les étapes impliquées dans la création, l’envoi et la prévisualisation d’un message MMS."
page_type: reference
tool:
  - Campagnes
channel:
  - MMS
search_rank: 2  
---

# Envoi de message MMS

> Cette page contient uniquement des informations spécifiques à la création de MMS dans l’éditeur SMS. Pour plus d’informations sur l’éditeur de SMS/MMS, consultez la section [Éditeur de SMS][1].

## Principes de base d’envoi MMS

Envoi de MMS avec Braze :

- **Sélectionnez votre groupe d’abonnement**
  - Vous devez désigner un groupe d’abonnement avec des numéros de téléphone MMS activés à cibler (il peut s’agir de codes courts ou longs).<br><br>
- **Saisissez le corps du message**
  - Entrez les types d’images PNG, JPG, GIF et VCF à partir de la médiathèque ou spécifiez une URL.
  - Une seule image est prise en charge<br><br>
- **Comprenez comment sont envoyés les MMS**
  - Les MMS sont facturés à un tarif différent des SMS avec uniquement du texte.
  - Tous les opérateurs n’acceptent pas les MMS. Dans ces cas spécifiques, Twilio convertit automatiquement le MMS en un lien d’image sur lequel l’utilisateur peut cliquer.

### Cartes de visite

Les cartes de visite (parfois appelées vCard ou Virtual Contact Files (VCF)) sont un format de fichier normalisé pour l’envoi d’informations professionnelles et de contact qui peuvent être facilement importées dans des carnets d’adresses ou de contacts. Ces cartes peuvent être créées [par programmation](https://www.twilio.com/blog/send-vcard-twilio-sms) et chargées dans la médiathèque de Braze, ou créées à l’aide de notre [générateur de cartes de visite]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/).

## Création d’un message MMS

La création d’un message MMS nécessite que votre groupe d’abonnement soit configuré pour l’envoi de MMS. Pour le savoir, consultez la balise MMS lors de la sélection d’un groupe d’abonnement. Lorsque vous sélectionnez un groupe d’abonnement compatible MMS, vous pouvez charger une image, faire référence à une URL d’image ou inclure une carte de visite.

![][2]

### Spécifications de l’image

**Spécifications de l’image** | **Propriétés recommandées**
--- | ---
Taille | 5 Mo maximum
Types de fichiers | PNG, JPG, GIF
{: .reset-td-br-1 .reset-td-br-2}

## Prévisualisation d’un message MMS

Braze propose un aperçu de l’image que vous avez chargée dans le panneau **Preview** (Aperçu) du message. 

{% alert note %}
L’ordre des ressources SMS/MMS ne peut pas être personnalisé. L’ordre dépend du téléphone qui reçoit ce message.
{% endalert %}

![][3]


[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/
[2]: {% image_buster /assets/img/sms/mms_composer.png %}
[3]: {% image_buster /assets/img/sms/mms_preview.png %}
[4]: {% image_buster /assets/img/sms/contact_card1.png %}
[5]: {% image_buster /assets/img/sms/contact_card2.png %}
