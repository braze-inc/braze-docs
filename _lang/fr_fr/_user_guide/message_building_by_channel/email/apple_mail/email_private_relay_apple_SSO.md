---
nav_title: Envoi d’e-mails au relais privé d’Apple
article_title: Envoi d’e-mails au relais privé d’Apple
alias: /email_relay/
page_order: 0
description: "Le présent article explique le processus d’envoi d’e-mails au relais privé d’Apple."
channel:
  - email
  
---

# Envoi d’e-mails au relais privé d’Apple

> La fonctionnalité d'authentification unique (SSO) d'Apple permet aux utilisateurs de partager leur adresse e-mail (`example@icloud.com`) ou de la dissimuler en masquant ce qui est fourni aux marques (`tq1234snin@privaterelay.appleid.com`) au lieu de leur adresse e-mail personnelle. Apple transfère alors les messages envoyés aux adresses relais vers l'adresse e-mail réelle de l'utilisateur. 

Pour envoyer des e-mails au relais d'e-mail privé d'Apple, enregistrez vos domaines d'envoi auprès d'Apple. Si vous ne configurez pas vos domaines avec Apple, les e-mails envoyés à des adresses relais seront rejetés.

Si un utilisateur décide de désactiver le transfert par e-mail vers l’e-mail de relais de votre application, Braze recevra des informations de rebond d’e-mail comme d’habitude. Ces utilisateurs peuvent gérer les applications qui utilisent la connexion avec Apple à partir de leur page de paramètres de l'ID Apple (voir la [documentation d'Apple](https://support.apple.com/en-us/HT210426)).

## Envoi d’e-mails pour SendGrid

Si vous utilisez SendGrid comme fournisseur de messagerie, vous pouvez envoyer des e-mails à Apple sans modifier le DNS. 

1. 
2. 
3. 
4. 

 

## Envoi d’e-mails pour SparkPost

Pour configurer le relais privé Apple pour SparkPost, procédez comme suit : 

1. Connectez-vous avec Apple.
2. Suivez la [documentation d'Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) pour enregistrer les domaines d'e-mail.
3. 

### Considérations

Si un domaine d'envoi est également utilisé comme domaine de rebond, vous ne pourrez pas stocker d'enregistrements et devrez suivre ces étapes supplémentaires :

1. Si le domaine a déjà été vérifié sur SparkPost, vous **devez** créer les enregistrements MX et TXT : 

| Instance | Enregistrement MX                   | Enregistrement TXT                                    |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}

{% endalert %}

{:start="2"}
2\. Supprimez l'enregistrement CNAME.
3\. Remplacez-les par les enregistrements MX et TXT pour un routage correct.
4\. Créez votre enregistrement A pour qu'il pointe vers votre réseau de diffusion de contenu ou votre hébergement de fichiers.

Si vous avez d'autres questions, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).
