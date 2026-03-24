---
nav_title: Acquisition de numéro de téléphone
article_title: Acquisition de numéro de téléphone
page_order: 4
description: "Cet article de référence explique comment obtenir un numéro de téléphone auprès de Twilio et Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Acquisition de numéro de téléphone

> Pour utiliser le canal de communication WhatsApp, vous aurez besoin d'un numéro de téléphone conforme aux exigences de WhatsApp pour son [API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou son [API On-Premises](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Vous devez acquérir votre numéro de téléphone vous-même, car Braze ne le fournira pas. Vous pouvez soit acheter un téléphone physique avec une carte SIM auprès de votre fournisseur de téléphonie professionnelle, soit utiliser l'un de nos partenaires : Twilio ou Infobip. **Vous devez disposer de votre propre compte Twilio ou Infobip, car cette opération ne peut pas être effectuée via Braze.**

## Exigences de l'API WhatsApp

Votre numéro de téléphone doit répondre aux exigences suivantes de l'API WhatsApp :

- Appartenir à votre entreprise 
- Avoir un indicatif de pays et de zone (comme un numéro de téléphone fixe ou portable)
- Pouvoir recevoir des appels vocaux ou des SMS
- Être accessible lors de la configuration du compte (pour recevoir les codes de vérification)
- Ne pas être un code court
- Ne pas avoir été utilisé précédemment avec la plateforme WhatsApp Business
- Ne pas être connecté à un compte WhatsApp personnel

## Acquisition d'un numéro de téléphone Twilio

### Étape 1 : Achetez un numéro de téléphone depuis la console ou l'API Twilio

1. Depuis la console Twilio, allez dans **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Si vous ne voyez pas cette option, sélectionnez **Explore Products**, faites défiler jusqu'à **Super Networks**, puis sélectionnez **Phone Number** > **Buy a number**. <br><br>![Console Twilio avec l'onglet « Develop » ouvert et l'option « Buy a number ».]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Entrez l'indicatif régional ou la localité souhaitée (le cas échéant). Trouvez un numéro, puis sélectionnez **Buy**. <br><br> ![Un bouton pour acheter le numéro de téléphone affiché.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Après avoir acheté votre numéro de téléphone, allez dans **Active Numbers** et sélectionnez le numéro que vous venez d'acheter. <br><br>![« Active Numbers » affichant le numéro de téléphone acheté.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Étape 2 : Configurez votre numéro de téléphone

Suivez les instructions de Twilio pour configurer votre numéro de téléphone Twilio afin de recevoir le code de vérification par e-mail en utilisant **uniquement** [Twilio Voice](https://www.twilio.com/docs/whatsapp/self-sign-up#add-your-whatsapp-phone-number). **Ne suivez pas les instructions des autres étapes.**

{% alert warning %}
Suivez uniquement les instructions de Twilio pour recevoir un code de vérification.
Si vous suivez les étapes suivantes, vous connecterez votre numéro de téléphone à Twilio, ce qui signifie que vous ne pourrez pas connecter ce numéro à Braze à moins d'effectuer une migration ou d'acheter un autre numéro.
{% endalert %}

1. Dans la console Twilio, allez sur la [page Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) et sélectionnez le numéro de téléphone que vous avez acheté.
2. Allez dans la section **Voice Configuration** et dans le menu déroulant **Configure with**, sélectionnez **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. Dans la ligne **A call comes in**, sélectionnez **Webhook** et définissez l'URL sur `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, en remplaçant `YOUR_EMAIL_ADDRESS` par votre adresse e-mail.
4. Dans la console Twilio, allez dans **2. Link WhatsApp Business Account with your number** > **2. Copy the phone number you register**, et sélectionnez **Copy** à côté du numéro de téléphone.
5. Dans la fenêtre **Self Sign-up**, sur la page **Add your WhatsApp phone number**, sélectionnez **Add a new phone number** et collez le numéro de téléphone.
6. Sélectionnez **Phone call** comme méthode de vérification, puis sélectionnez **Next**.
7. Vous recevrez le code de vérification par e-mail dans les 10 minutes.

### Étape 3 : Complétez le flux d'inscription intégré

1. Une fois Twilio configuré, allez sur votre tableau de bord de Braze > **Technology Partners** > **WhatsApp** et sélectionnez **Begin integration** ou **Add WhatsApp Business Account**, selon ce qui s'affiche, pour déclencher le [flux d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>À l'étape **Add a phone number for WhatsApp**, sélectionnez **Phone call** pour la méthode de vérification de votre numéro de téléphone. <br><br>![Section avec les options pour vérifier votre numéro de téléphone par SMS ou par appel téléphonique.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Attendez quelques minutes que le code de vérification soit envoyé dans votre boîte de réception, puis entrez le code de vérification et terminez la configuration.

## Acquisition d'un numéro de téléphone Infobip 

1. Dans la console Infobip, allez dans **Channels and Numbers** et sélectionnez **Numbers**.<br><br>![Section « Channels and Numbers » d'Infobip avec « Numbers » listé en dessous.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Sélectionnez **Buy Number** > le pays où vous souhaitez envoyer des messages > **SMS**.<br><br>![Bouton pour acheter un numéro.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. En fonction du pays sélectionné, vous devrez peut-être compléter un processus d'enregistrement supplémentaire (comme choisir une option 10DLC ou numéro vert pour les numéros de téléphone américains). Assurez-vous de sélectionner l'option disponible.<br><br>![Une page vous demandant de sélectionner le type de numéro : soit 10DLC, soit numéro vert.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Sélectionnez l'offre disponible, puis effectuez les étapes restantes et attendez que votre demande soit traitée. Vous pouvez vérifier l'état en allant dans **Numbers** > **My Request**. <br><br>![Une offre avec des informations incluant les frais et la couverture.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. En fonction du pays choisi, attendez que l'équipe d'Infobip vous contacte pour les détails d'enregistrement (comme pour le 10DLC aux États-Unis).<br><br>

6. Lorsque votre numéro de téléphone est prêt dans Infobip, allez sur votre tableau de bord de Braze > **Technology Partners** > **WhatsApp** et sélectionnez **Begin integration** ou **Add WhatsApp Business Account**, selon ce qui s'affiche, pour déclencher le [flux d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> À l'étape **Add a phone number for WhatsApp**, sélectionnez **Text message** pour la méthode de vérification de votre numéro de téléphone.<br><br>![Section avec les options pour vérifier votre numéro de téléphone par SMS ou par appel téléphonique.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Consultez les [journaux d'analyse](https://www.infobip.com/docs/analyze/analyze-logs) d'Infobip dans leur portail client pour trouver le code de vérification, qui peut prendre quelques minutes à apparaître, puis entrez le code de vérification et terminez la configuration.