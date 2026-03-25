---
nav_title: Envoyer des e-mails à Apple Private Relay
article_title: Envoyer des e-mails à Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Cet article décrit le processus d'envoi d'e-mails au relais privé d'Apple."
channel:
  - email
toc_headers: h2
---

# Envoyer des e-mails à Apple Private Relay

> La fonctionnalité d'authentification unique (SSO) d'Apple permet aux utilisateurs de partager leur adresse e-mail (`example@icloud.com`) ou de la masquer en fournissant aux marques une adresse anonymisée (`tq1234snin@privaterelay.appleid.com`) au lieu de leur adresse e-mail personnelle. Apple transfère ensuite les messages envoyés aux adresses relais vers l'adresse e-mail réelle de l'utilisateur. 

Pour envoyer des e-mails au relais d'e-mail privé d'Apple, enregistrez vos domaines d'envoi auprès d'Apple. Si vous ne configurez pas vos domaines avec Apple, les e-mails envoyés à des adresses relais entraîneront des rebonds.

Si un utilisateur décide de désactiver le transfert d'e-mails vers l'adresse relais de votre application, Braze recevra les informations de rebond comme d'habitude. Ces utilisateurs peuvent gérer les applications qui utilisent la connexion avec Apple depuis leur page de paramètres Apple ID (voir la [documentation d'Apple](https://support.apple.com/en-us/HT210426)).

{% tabs %}
{% tab SendGrid %}

## Configurer Sendgrid 

Si vous utilisez Sendgrid comme fournisseur d'e-mail, vous pouvez envoyer des e-mails à Apple sans modifier le dns. 

1. Connectez-vous au [portail des développeurs Apple](https://developer.apple.com/).
2. Accédez à la page **Certificates, Identifiers & Profiles**.
3. Sélectionnez **Services** > **Sign in with Apple for Email Communication**.
4. Dans la section **Email Sources**, ajoutez les domaines et sous-domaines.
- L'adresse doit être au format suivant : `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (par exemple : `bounces+1234567@braze.online.docs.com`). 

Si l'adresse d'expédition souhaitée est une adresse `abmail`, incluez-la dans votre sous-domaine. Par exemple, utilisez `abmail.docs.braze.com` au lieu de `docs.braze.com`.

{% endtab %}
{% tab SparkPost %}

## Configurer SparkPost 

Pour configurer Apple Private Relay avec SparkPost, procédez comme suit : 

1. Connectez-vous avec Apple.
2. Suivez la [documentation d'Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) pour enregistrer les domaines d'e-mail.
3. Apple vérifiera automatiquement les domaines, indiquera ceux qui sont vérifiés et offrira la possibilité de les revérifier ou de les supprimer.

### Lorsque le domaine d'envoi est aussi le domaine de rebond

Si un domaine d'envoi est également utilisé comme domaine de rebond, vous ne pourrez pas stocker d'enregistrements et devrez suivre ces étapes supplémentaires :

1. Si le domaine a déjà été vérifié sur SparkPost, vous **devez** créer les enregistrements MX et TXT : 

| Instance | Enregistrement MX                   | Enregistrement TXT                                    |
|----------|-----------------------------|-----------------------------------------------|
| États-Unis       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| UE       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Pour éviter les échecs SPF, vous devez créer les enregistrements MX et TXT et les faire propager dans le dns **avant** de supprimer l'enregistrement CNAME.
{% endalert %}

{:start="2"}
2. Supprimez l'enregistrement CNAME.
3. Remplacez-le par les enregistrements MX et TXT pour un routage correct.
4. Créez votre enregistrement A pour qu'il pointe vers votre réseau de diffusion de contenu ou votre hébergement de fichiers.

{% endtab %}
{% tab Amazon SES %}

## Configurer Amazon SES

### Configurer un domaine MAIL FROM personnalisé

Pour configurer Apple Private Relay avec Amazon Simple Email Service (SES), vous devez d'abord configurer un domaine MAIL FROM personnalisé dans SES. Pour plus de détails, consultez la [documentation d'AWS](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html).

### Enregistrer les domaines auprès d'Apple

1. Connectez-vous avec Apple.
2. Suivez la [documentation d'Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) pour enregistrer les domaines d'e-mail.
3. Apple vérifiera automatiquement les domaines, indiquera ceux qui sont vérifiés et offrira la possibilité de les revérifier ou de les supprimer.

{% endtab %}
{% endtabs %}

Si vous avez d'autres questions, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).