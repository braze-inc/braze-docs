---
nav_title: Création d'une campagne MMS
article_title: Création d'une campagne MMS
page_order: 2
description: "Cet article de référence couvre les étapes impliquées dans la création, l'envoi et la prévisualisation d'un message MMS."
page_type: Référence
tool:
  - Campagnes
channel:
  - MMS
---

# Envoi du message MMS

> Cette page contient uniquement des informations spécifiques à la composition MMS qui fait partie du compositeur de SMS. Pour plus d'informations sur le compositeur SMS/MMS, consultez le \[Compositeur de SMS\]\[1\].

## MMS envoyant des bases

Envoi de MMS avec Braze :

- __Sélectionnez votre groupe d'abonnement__
  - Vous devez désigner un groupe d'abonnement avec les numéros de téléphone avec MMS à cibler (peut être court ou long).<br><br>
- __Corps du message de saisie__
  - Entrez les types d'images PNG, JPG, GIF, et VCF à partir de la bibliothèque multimédia ou spécifiez une URL.
  - Une seule image est prise en charge<br><br>
- __Comprendre l'envoi de MMS__
  - Les MMS sont facturés à un tarif différent par rapport au SMS texte.
  - Tous les transporteurs ne peuvent pas accepter les MMS. Dans ces cas, Twilio convertira automatiquement le MMS en un lien d'image sur lequel l'utilisateur peut cliquer.

### Cartes de contact

Les Cartes de contact (parfois appelées vCard ou fichiers de contact virtuel (vcf)) sont un format de fichier normalisé pour envoyer des informations commerciales et de contact qui peuvent être facilement importées dans des carnets d'adresses ou des carnets de contacts. Ces cartes peuvent être créées [par programme](https://www.twilio.com/blog/send-vcard-twilio-sms) et téléchargées dans la bibliothèque médiatique de Braze ou créées via notre [générateur de cartes de contact]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/) intégré.

## Création d'un MMS

La création d'un message MMS nécessite que votre groupe d'abonnement soit configuré pour l'envoi de MMS. Ceci est indiqué en voyant la balise MMS lors de la sélection d'un groupe d'abonnement. Lorsque vous sélectionnez un groupe d'abonnement avec MMMS, vous aurez la possibilité de télécharger une image, de référencer une URL d'image ou d'inclure une fiche de contact.

!\[picture\]\[2\]

### Caractéristiques de l'image

| **Caractéristiques de l'image** | **Propriétés recommandées** |
| ------------------------------- | --------------------------- |
| Taille                          | 5 Mo maximum                |
| Types de fichiers               | PNG, JPG, GIF               |
{: .reset-td-br-1 .reset-td-br-2}

## Aperçu d'un MMS

Braze fournit un aperçu de l'image que vous avez téléchargée.

{% alert note %}
La commande des actifs SMS/MMS ne peut pas être personnalisée. La commande dépend du téléphone recevant ce message.
{% endalert %}

!\[picture\]\[3\]
[1]: {{ site.baseurl }}/user_guide/message_building_by_channel/sms/create/ [2]: {% image_buster /assets/img/sms/mms_composer.png %} [3]: {% image_buster /assets/img/sms/mms_preview. ng %} [4]: {% image_buster /assets/img/sms/contact_card1.png %} [5]: {% image_buster /assets/img/sms/contact_card2.png %}
