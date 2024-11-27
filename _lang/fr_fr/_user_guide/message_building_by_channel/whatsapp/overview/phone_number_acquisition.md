---
nav_title: Acquisition de numéro de téléphone
article_title: Acquisition de numéro de téléphone
page_order: 3
description: "Cet article de référence explique comment obtenir un numéro de téléphone de Twilio et Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Acquisition de numéro de téléphone

> Pour utiliser le canal de messagerie WhatsApp, vous aurez besoin d'un numéro de téléphone qui répond aux exigences de WhatsApp pour son [API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [API sur site](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Vous devez acquérir votre numéro de téléphone vous-même, car Braze ne fournira pas le numéro pour vous. Vous pouvez soit acheter un téléphone physique avec une carte SIM auprès de votre fournisseur de téléphonie professionnelle, soit utiliser l'un de nos partenaires : Twilio ou Infoblip. **Vous devez disposer de votre propre compte Twilio ou Infobip car cela ne peut pas être fait via Braze.**

## Exigences de l'API WhatsApp

Votre numéro de téléphone doit répondre à ces exigences de l'API WhatsApp :

- Appartenant à votre entreprise 
- Avoir un indicatif de pays et de zone (comme un numéro de téléphone fixe et portable)
- Capable de recevoir des appels vocaux ou des SMS
- Accessible lors de la configuration du compte (pour recevoir des codes de vérification)
- Pas un code court
- Pas utilisé précédemment avec la plateforme WhatsApp Business
- Non connecté à un compte WhatsApp personnel

## Acquisition d'un numéro de téléphone Twilio

### Étape 1 : Achetez un numéro de téléphone depuis la console ou l'API Twilio

1. Depuis la console Twilio, allez dans **Développer** > **Numéros de téléphone** > **Gérer** > **Acheter un numéro**. Si vous ne voyez pas cette option, sélectionnez **Explorer les produits**, faites défiler jusqu'à **Super réseaux**, puis sélectionnez **Numéro de téléphone** > **Acheter un numéro**. <br><br>![Console Twilio avec l'onglet « Develop (Développer) » ouvert et l'option « Buy a number (Acheter un numéro) ».][1]{: style="max-width:20%;"}<br><br>

2. Entrez votre indicatif régional ou la localité souhaitée (le cas échéant). Trouvez un numéro, puis sélectionnez **Buy (Acheter)**. <br><br> ![Un bouton pour acheter le numéro de téléphone répertorié.][2]<br><br>

3. Après avoir acheté votre numéro de téléphone, allez dans **Numéros actifs** et sélectionnez le numéro de téléphone que vous venez d'acheter. <br><br>!["Numéros actifs" montrant le numéro de téléphone acheté.][3]{: style="max-width:70%;"}<br><br>

### Étape 2 : Configurez votre numéro de téléphone

Suivez les instructions de Twilio pour [configurer votre numéro de téléphone Twilio afin de recevoir le code de vérification par e-mail en utilisant la transcription de la messagerie vocale](https://www.twilio.com/docs/whatsapp/self-sign-up#setting-up-your-twilio-phone-number-to-receive-the-verification-code-via-email-using-voicemail-transcription). **Ne suivez pas les instructions des autres étapes, car cela connectera votre numéro de téléphone à Twilio, pas à Braze.**

{% alert warning %}
**Suivez uniquement les instructions de Twilio pour recevoir un code de vérification.**

Si vous suivez les prochaines étapes des instructions de Twilio, vous connecterez votre numéro de téléphone à Twilio. Cela signifie que vous ne pouvez pas connecter ce numéro à Braze à moins de faire une migration ou d'acheter un autre numéro.
{% endalert %}

### Étape 3 : Complétez le flux de travail d'inscription intégré

1. Après avoir configuré Twilio, allez sur votre tableau de bord Braze > **Partenaires technologiques** > **WhatsApp** et sélectionnez **Commencer l'intégration** ou **Ajouter un compte WhatsApp Business**, selon ce qui s'affiche, pour déclencher le [flux de travail d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>À l'étape **Ajouter un numéro de téléphone pour WhatsApp**, sélectionnez **Appel téléphonique** pour la méthode de vérification de votre numéro de téléphone. <br><br>![Section avec les options pour vérifier votre numéro de téléphone par SMS ou par appel téléphonique.][4]{: style="max-width:50%;"}<br><br>

2. Attendez quelques minutes pour que le code de vérification soit envoyé à votre boîte de réception, puis entrez le code de vérification et terminez votre configuration.

## Acquisition d'un numéro de téléphone Infobip 

1. Dans la console Infobip, allez à **Canaux et Numéros** et sélectionnez **Numéros**.<br><br>![Section "Canaux et numéros" d'Infoblip avec "Numéros" listés ci-dessous.][5]{: style="max-width:30%;"}<br><br>

2. Sélectionnez **Acheter un numéro** > le pays où vous souhaitez envoyer des messages > **SMS**.<br><br>![Bouton pour acheter un numéro.][6]<br><br>

3. En fonction de votre pays sélectionné, vous devrez peut-être compléter un processus d'enregistrement supplémentaire (comme choisir une option 10 DLC ou sans frais pour les numéros de téléphone américains). Assurez-vous de sélectionner l'option disponible.<br><br>![Une page vous demandant de sélectionner le type de numéro : soit 10 DLC ou numéro vert.][7]{: style="max-width:70%;"}<br><br>

4. Sélectionnez l'offre disponible, puis effectuez les étapes restantes et attendez que votre demande soit traitée. Vous pouvez vérifier le statut en allant sur **Numbers** > **Ma demande**. <br><br>![Une offre avec des informations incluant les frais et la couverture.][8]{: style="max-width:70%;"}<br><br>

5. Selon votre pays sélectionné, attendez que l'équipe Infobip vous contacte pour obtenir les détails de l'enregistrement (comme pour le 10DLC aux États-Unis).<br><br>

6. Lorsque votre numéro de téléphone est prêt dans Infobip, allez sur votre tableau de bord Braze > **Partenaires technologiques** > **WhatsApp** et sélectionnez **Commencer l'intégration** ou **Ajouter un compte WhatsApp Business**, selon ce qui s'affiche, pour déclencher le [flux de travail d'inscription intégré]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> Dans l'étape **Ajouter un numéro de téléphone pour WhatsApp**, sélectionnez **Message texte** pour la méthode de vérification de votre numéro de téléphone.<br><br>![Section avec les options pour vérifier votre numéro de téléphone par SMS ou par appel téléphonique.][9]<br><br>

7. Vérifiez les [journaux d'analyse](https://www.infobip.com/docs/analyze/analyze-logs) d'Infobip dans leur portail client pour le code de vérification. L’affichage peut prendre quelques minutes. Ensuite, entrez le code de vérification et terminez la configuration.




[1]: {% image_buster /assets/img/whatsapp/develop_buy_number.png %}
[2]: {% image_buster /assets/img/whatsapp/buy.png %}
[3]: {% image_buster /assets/img/whatsapp/active_numbers.png %}
[4]: {% image_buster /assets/img/whatsapp/verify.png %}
[5]: {% image_buster /assets/img/whatsapp/infoblip_numbers.png %}
[6]: {% image_buster /assets/img/whatsapp/infoblip_buy.png %}
[7]: {% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}
[8]: {% image_buster /assets/img/whatsapp/infoblip_offer.png %}
[9]: {% image_buster /assets/img/whatsapp/infoblip_verify.png %}