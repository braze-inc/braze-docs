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

1. Allez sur la page de votre **certificat Apple** et autorisez l'adresse e-mail que vous souhaitez utiliser pour l'envoi via le service de relais e-mail d'Apple (l'adresse "From" que vous souhaitez).
- L'adresse doit être formatée comme suit : `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(par exemple : `bounces+1234567@braze.online.docs.com`). 

![Option permettant d’autoriser des adresses e-mail individuelles sur la page du certificat Apple.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

{:start="2"}
2\. Une fois l'adresse ajoutée à votre page de certificat Apple, les e-mails de ce domaine seront délivrés via le système Apple Private Relay.

{% alert important %}
Si l’adresse d’expédition souhaitée est une adresse `abmail`, y compris dans votre sous-domaine. Par exemple, utilisez `abmail.docs.braze.com` au lieu de `docs.braze.com`.
{% endalert %}

### À partir des valeurs d’adresse

Reportez-vous à ce tableau pour les composants utilisés lors de l’ajout d’adresses e-mail avec le relais privé Apple.

| Valeur | Description |
|---|---|
| UID | Cette valeur est indiquée dans vos enregistrements DNS fournis par Braze (à partir de SendGrid). N’incluez pas la lettre « u » dans votre UID dans l’adresse e-mail. Par exemple, si votre UID est présenté dans SendGrid comme `u1234567.wl134.sendgrid.net`, alors `1234567` est la valeur UID. <br><br> Si vous n’avez pas accès à vos dossiers DNS, contactez votre gestionnaire du succès des clients Braze pour fournir votre UID. |
| Sous-domaine et domaine marqué comme Whitelabel | Le domaine et sous-domaine initiaux que vous avez saisis dans SendGrid. Vous pouvez également utiliser la **valeur HOST** dans vos enregistrements DNS dans Sendgrid. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Envoi d’e-mails pour SparkPost

Pour configurer le relais privé Apple pour SparkPost, procédez comme suit : 

1. Connectez-vous avec Apple.
2. Suivez la [documentation d'Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) pour enregistrer les domaines d'e-mail.
3. Apple vérifiera automatiquement les domaines et montrera ceux qui sont vérifiés, et fournira la possibilité de revérifier ou de supprimer les domaines.

{% alert important %}
Veillez à effectuer cette opération dans les deux ou trois jours suivant la création des fichiers de vérification, faute de quoi ils expireront. Apple ne divulgue pas leur durée de validité.
{% endalert %}

### Considérations

Si un domaine d'envoi est également utilisé comme domaine de rebond, vous ne pourrez pas stocker d'enregistrements et devrez suivre ces étapes supplémentaires :

1. Si le domaine a déjà été vérifié sur SparkPost, vous **devez** créer les enregistrements MX et TXT : 

| Instance | Enregistrement MX                   | Enregistrement TXT                                    |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Pour éviter les échecs SPF, vous devez créer les enregistrements MX et TXT et les propager dans le DNS **avant de** supprimer l'enregistrement CNAME.
{% endalert %}

{:start="2"}
2\. Supprimez l'enregistrement CNAME.
3\. Remplacez-les par les enregistrements MX et TXT pour un routage correct.
4\. Créez votre enregistrement A pour qu'il pointe vers votre réseau de diffusion de contenu ou votre hébergement de fichiers.

Si vous avez d'autres questions, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).
