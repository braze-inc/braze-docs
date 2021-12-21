---
nav_title: Relais privé Apple
article_title: Envoi d'e-mails au Relais privé Apple
alias: /fr/email_relay/
page_order: 9
description: "Cet article traite du processus d’envoi de courriels à Apple Private Relay. Cela permettra aux utilisateurs de Sendgrid de mettre en liste blanche sans avoir à faire de modifications DNS."
channel:
  - Email
---

# Envoi d'e-mails au Relais privé Apple

Avec la version iOS 13, Apple a introduit des fonctionnalités pour les clients d'Apple, ce qui a un impact sur la façon dont les e-mails leur sont envoyés. La nouvelle fonctionnalité d'authentification unique d'Apple (SSO) permet aux clients Apple de partager leur adresse e-mail (`exemple@icloud. om`) ou de cacher leur adresse e-mail, auquel cas une adresse email "masquée" (`tq1234snin@privaterelay. ppleid.com`) sera fourni aux marques (par opposition à l'adresse e-mail personnelle de l'utilisateur).

## Désactiver le transfert

Les utilisateurs peuvent gérer les applications en utilisant Se connecter avec Apple à partir de leur page de paramètres Apple ID (voir la [Documentation d'Apple](https://support.apple.com/en-us/HT210426)).

Si un utilisateur choisit de désactiver la redirection de courriel vers l'e-mail de votre application, Braze recevra comme d'habitude des informations de rebond par e-mail.

## Envoi d'emails à l'Apple Private Relay pour SendGrid

Les clients qui utilisent SendGrid comme fournisseur de messagerie peuvent maintenant «[whitelist](https://help.apple.com/developer-account/?lang=en#/devf822fb8fc)» avec Apple sans avoir à apporter de modifications DNS.

Rendez-vous sur votre page [Certificat Apple](https://help.apple.com/developer-account/?lang=en#/devf822fb8fc) et mettez en liste blanche l'adresse e-mail que vous souhaitez utiliser pour envoyer via le service de relais de courrier électronique d'Apple (votre adresse souhaitée `De`).

![Etiquette blanche de l'adresse]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

Pour trouver la bonne adresse, allez dans votre enregistrement DNS Sendgrid et copiez l'UID, le sous-domaine Whitelabel et le domaine dans la colonne Valeur de l'hôte.

![HOST valeur des enregistrements DNS]({% image_buster /assets/img/email-relay-dns-records.png %})

L'adresse doit être formatée comme :

`bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`

Par exemple : `bounces+1234567@braze.online.docs.com`.

Une fois ajouté à votre page de certificat Apple, les e-mails de ce domaine `De` adresse seront livrés via le système Apple Private Relay.

Si vous avez d'autres questions, veuillez ouvrir un [ticket d'assistance]({{site.baseurl}}/braze_support/).

{% alert important %}
Si l'adresse `De` que vous souhaitez est une adresse `abmail` , veuillez l'inclure dans votre sous-domaine. Par exemple, utilisez `abmail.docs.braze.com` au lieu de `docs.braze.com`.

Cela pourrait ne pas être le cas pour votre adresse. Veuillez vérifier vos enregistrements DNS dans Sendgrid.
{% endalert %}

### Composants d'adresse pour la liste blanche avec le relais de messagerie Apple

| Valeur                                    | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UID                                       | Cette valeur est fournie par Sendgrid dans vos enregistrements DNS. N'incluez pas le caractère "U" dans votre UID dans l'adresse e-mail que vous utilisez sur la marque blanche. Par exemple, si votre UID est présenté dans Sendgrid comme `u1234567.wl134.sendgrid.net`, alors `1234567` est la valeur UID. <br> <br> _Vous pouvez également demander à votre représentant Braze de fournir votre UID, si vous n'avez pas accès à vos enregistrements DNS._ |
| Sous-domaine et domaine en marque blanche | Il s'agit du domaine initial et du sous-domaine que vous avez entré dans Sendgrid. Vous pouvez également utiliser la valeur HOST dans vos enregistrements DNS dans Sendgrid. <br> <br> ![HOST valeur des enregistrements DNS]({% image_buster /assets/img/email-relay-dns-records.png %})                                                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2}

## Envoi d'e-mails à l'Apple Private Relay pour Sparkpost

Les clients de Braze qui utilisent Sparkpost peuvent également configurer Apple Private Relay. Pour ce faire, effectuez les étapes suivantes :

1. Créez les fichiers de vérification nécessaires selon la documentation d'Apple sur [Connectez-vous avec Apple](https://developer.apple.com/sign-in-with-apple/get-started/).
2. Hébergez les fichiers dans le répertoire `/.well-known/` des domaines donnés. Assurez-vous que votre réseau de distribution de contenu (CDN) est accessible au public via Internet.
3. Ajoutez un enregistrement A dans le DNS qui pointe vers le domaine où votre fichier de vérification est hébergé. Il s'agit d'un processus de vérification unique.
4. Sélectionnez la vérification à la fin d'Apple.

{% alert important %}
Assurez-vous que vous terminez ce processus dans les 2 à 3 jours suivant la création des fichiers de vérification sinon ils expireront. Apple ne révèle pas combien de temps ils sont valides.
{% endalert %}