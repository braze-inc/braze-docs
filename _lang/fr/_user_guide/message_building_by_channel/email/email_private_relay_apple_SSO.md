---
nav_title: Relais privé d’Apple
article_title: Envoi d’e-mails au relais privé d’Apple
alias: /email_relay/
page_order: 9
description: "Le présent article explique le processus d’envoi d’e-mails au relais privé d’Apple. Cela permettra aux utilisateurs de SendGrid de figurer sur la liste blanche sans avoir à modifier le DNS."
channel:
  - E-mail
  
---

# Envoi d’e-mails au relais privé d’Apple

Avec la version iOS 13, Apple a introduit des fonctionnalités pour les clients Apple, ce qui a un impact sur la manière dont les e-mails leur sont envoyés. La nouvelle fonctionnalité d’authentification unique Apple permet aux clients Apple de partager leur adresse e-mail (`example@icloud.com`) ou de masquer leur adresse e-mail, auquel cas une adresse e-mail « masquée » (`tq1234snin@privaterelay.appleid.com`) sera fourni aux marques (plutôt que l’adresse e-mail personnelle de l’utilisateur).

## Désactiver le transfert

Les utilisateurs peuvent gérer les applications en utilisant la connexion avec Apple à partir de leur page de paramètres Apple ID (voir [Documentation d’Apple](https://support.apple.com/en-us/HT210426)).

Si un utilisateur choisit de désactiver le transfert par e-mail vers l’e-mail de relais de votre application, Braze recevra des informations de rebond d’e-mail comme d’habitude.

## Envoi d’e-mails au relais privé d’Apple pour SendGrid

Les clients de Braze qui utilisent SendGrid comme fournisseur d’e-mail peuvent désormais figurer sur la «"[ liste blanche](https://help.apple.com/developer-account/?lang=en#/devf822fb8fc) » avec Apple sans avoir à modifier le DNS.

Accédez à la page de votre [Certificat Apple](https://help.apple.com/developer-account/?lang=en#/devf822fb8fc) et ajoutez à la liste blanche l’adresse e-mail que vous souhaitez utiliser pour envoyer depuis le service de relais d’e-mail d’Apple (votre adresse d’expédition).`From` 

![Option permettant de faire figurer dans la liste blanche des adresses e-mail individuelles sur la page du certificat Apple.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

Pour trouver l’adresse correcte, allez dans votre dossier DNS Sendgrid et copiez l’**UID**, le **Whitelabel Subdomain (Sous-domaine de Whitelabel)**, et le **Domaine** de la colonne **Host Value (Valeur hôte)**. 

![Colonne HOST Value (Valeur HÔTE) dans la section des enregistrements DNS Sendgrid.]({% image_buster /assets/img/email-relay-dns-records.png %})

L’adresse doit être formatée comme suit : `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`

Voici un exemple : `bounces+1234567@braze.online.docs.com`.

Une fois ajoutés à votre page de certificat Apple, les e-mails provenant du domaine de cette `From`adresse d’expédition seront livrés depuis le système de relais privé d’Apple.

Si vous avez d’autres questions, ouvrez un [ticket d’assistance]({{site.baseurl}}/braze_support/).

{% alert important %}
Si `From`l’adresse d’expédition souhaitée est une adresse`abmail`, y compris dans votre sous-domaine. Par exemple, utiliser `abmail.docs.braze.com` au lieu de `docs.braze.com`.

Ce n’est peut-être pas le cas de votre adresse. Vérifiez vos enregistrements DNS dans Sendgrid. 
{% endalert %}

### Composants des adresses d’expédition pour la liste blanche avec le relais d’e-mail d’Apple

| Valeur | Description |
|---|---|
| UID | Cette valeur est fournie par Sendgrid dans vos enregistrements DNS. N’incluez pas le caractère « U » dans votre UID dans l’adresse e-mail que vous marquez comme Whitelabel. Par exemple, si votre UID est présenté dans Sendgrid comme `u1234567.wl134.sendgrid.net`, alors `1234567` est la valeur UID. <br>
 <br>
 Vous pouvez également contacter votre conseiller Braze pour qu’il vous fournisse votre UID si vous n’avez pas accès à vos enregistrements DNS. |
| Sous-domaine et domaine marqué comme Whitelabel | Il s’agit du domaine et du sous-domaine initiaux que vous avez saisis dans Sendgrid. Vous pouvez également utiliser la **HOST Value (Valeur HÔTE)** dans vos enregistrements DNS dans Sendgrid.|
{: .reset-td-br-1 .reset-td-br-2}

## Envoi d’e-mails au relais privé d’Apple pour Sparkpost

Les clients Braze qui utilisent Sparkpost peuvent également configurer le relais privé d’Apple. Pour cela, suivez ces étapes : 

1. Créez les fichiers de vérification nécessaires conformément à la documentation d’Apple, [Se connecter avec Apple](https://developer.apple.com/sign-in-with-apple/get-started/).
2. Hébergez les fichiers dans le répertoire `/.well-known/` des domaines donnés. Assurez-vous que votre réseau de diffusion de contenu (CDN) est accessible au public via Internet.
3. Ajoutez un enregistrement A dans le DNS qui pointe vers le domaine où votre fichier de vérification est hébergé. Il s’agit d’un processus de vérification unique. 
4. Sélectionnez Verify on Apple's end (Vérifier sur Apple).

{% alert important %}
Assurez-vous de terminer ce processus dans les 2 à 3 jours qui suivent la création des fichiers de vérification, sinon ils disparaîtront. Apple ne divulgue pas leur durée de validité.
{% endalert %}
