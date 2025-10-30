---
nav_title: Acquisition du numéro de téléphone
article_title: Numéro de téléphone Acquisition
page_order: 3
description: "Cet article de référence traite de l'acquisition d'un numéro de téléphone auprès de Twilio et d'Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Acquisition du numéro de téléphone

> Pour utiliser le canal de communication de WhatsApp, vous aurez besoin d'un numéro de téléphone répondant aux exigences de WhatsApp pour son [API dans le nuage](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou son [API sur site.](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)

Vous devez acquérir vous-même votre numéro de téléphone, car Braze ne le fournira pas pour vous. Vous pouvez soit acheter un téléphone physique avec une carte SIM auprès de votre opérateur téléphonique professionnel, soit faire appel à l'un de nos partenaires : Twilio ou Infoblip. **Vous devez disposer de votre propre compte Twilio ou Infobip, car cela ne peut pas se faire par l'intermédiaire de Braze.**

## Exigences de l'API WhatsApp

Votre numéro de téléphone doit répondre à ces exigences de l'API WhatsApp :

- Propriété de votre entreprise 
- Avoir un code de pays et de zone (comme un numéro de téléphone fixe et un numéro de téléphone portable)
- Possibilité de recevoir des appels vocaux ou des SMS
- Accessible lors de la configuration du compte (pour recevoir les codes de vérification)
- Pas un code court
- Non utilisé auparavant avec la plateforme WhatsApp Business
- Pas de connexion à un compte WhatsApp personnel

## Acquisition d'un numéro de téléphone Twilio

### Étape 1 : Acheter un numéro de téléphone à partir de la console ou de l'API Twilio

1. Dans la console Twilio, allez dans **Développer** > **Numéros de téléphone** > **Gérer** > **Acheter un numéro.** Si vous ne voyez pas cette option, sélectionnez **Explorer les produits**, faites défiler jusqu'à **Super Réseaux**, puis sélectionnez **Numéro de téléphone** > **Acheter un numéro.** <br><br>!console Twilio avec l'onglet "Développer" ouvert et l'option "Acheter un numéro".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Saisissez le code régional ou la localité de votre choix (si vous en avez un). Trouvez un numéro, puis sélectionnez **Acheter.** <br><br> !Un bouton pour acheter le numéro de téléphone indiqué.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Après avoir acheté votre numéro de téléphone, allez dans **Numéros actifs** et sélectionnez le numéro de téléphone que vous venez d'acheter. <br><br>\!["Numéros actifs" affichant le numéro de téléphone acheté.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Étape 2 : Configurer votre numéro de téléphone

Suivez les instructions de Twilio pour [configurer votre numéro de téléphone Twilio afin de recevoir le code de vérification par e-mail à l'aide de Twilio Voice Only](https://www.twilio.com/docs/whatsapp/self-sign-up#verify-your-whatsapp-sender). **Ne suivez pas les instructions d'une autre étape, car cela connectera votre numéro de téléphone à Twilio, et non à Braze.**

{% alert warning %}
**Suivez uniquement les instructions de Twilio pour recevoir un code de vérification.**

Si vous suivez les étapes suivantes des instructions de Twilio, vous connecterez votre numéro de téléphone à Twilio. Cela signifie que vous ne pouvez pas connecter ce numéro à Braze, à moins d'effectuer une migration ou d'acheter un autre numéro.
{% endalert %}

### Étape 3 : Complétez le processus d'inscription intégré.

1. Une fois Twilio configuré, accédez à votre tableau de bord Braze > **Partenaires technologiques** > **WhatsApp** et sélectionnez **Commencer l'intégration** ou **Ajouter un compte professionnel WhatsApp**, selon ce qui s'affiche, pour déclencher le [flux de travail d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>À l'étape **Ajouter un numéro de téléphone pour WhatsApp**, sélectionnez **Appel téléphonique** pour savoir comment vérifier votre numéro de téléphone. <br><br>!Section avec les options de vérification de votre numéro de téléphone par message texte ou par appel téléphonique.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Attendez quelques minutes que le code de vérification vous soit envoyé dans votre boîte de réception e-mail, puis saisissez le code de vérification et terminez votre configuration.

## Acquisition d'un numéro de téléphone Infobip 

1. Dans la console Infobip, allez dans **Canaux et Numéros** et sélectionnez **Numéros**.<br><br>\![Infoblip section "Chaînes et numéros" avec "Numéros" listés en dessous.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Sélectionnez **Numéro d'achat** > le pays où vous souhaitez envoyer des messages > SMS.<br><br>!bouton pour acheter un numéro.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. En fonction du pays choisi, il se peut que vous deviez effectuer une procédure d'enregistrement supplémentaire (comme la sélection d'une option 10 DLC ou d'une option gratuite pour les numéros de téléphone américains). Veillez à sélectionner l'option disponible.<br><br>Une page vous demande de sélectionner le type de numéro : 10 DLC ou gratuit.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Sélectionnez l'offre disponible, puis procédez au reste des étapes et attendez que votre demande soit traitée. Vous pouvez vérifier l'état d'avancement de la **demande** en allant dans **Numéros** > **Ma demande.** <br><br>Une offre avec des informations sur les frais et la couverture.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Selon le pays choisi, attendez que l'équipe d'Infobip vous contacte pour obtenir les détails de l'enregistrement (comme pour 10DLC aux États-Unis).<br><br>

6. Lorsque votre numéro de téléphone est prêt dans Infobip, accédez à votre tableau de bord de Braze > **Partenaires technologiques** > **WhatsApp** et sélectionnez **Commencer l'intégration** ou **Ajouter un compte professionnel WhatsApp**, selon ce qui s'affiche, pour déclencher le [flux de travail d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> À l'étape **Ajouter un numéro de téléphone pour WhatsApp**, sélectionnez **Message texte** pour la manière dont vous souhaitez vérifier votre numéro de téléphone.<br><br>!Section avec les options de vérification de votre numéro de téléphone par message texte ou par appel téléphonique.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Vérifiez les [journaux d'analyse d'](https://www.infobip.com/docs/analyze/analyze-logs) Infobip dans leur portail client pour le code de vérification, qui peut prendre quelques minutes à apparaître, puis entrez le code de vérification et terminez la configuration.




