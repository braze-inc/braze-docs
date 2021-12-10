---
nav_title: Octa
article_title: Octa
page_order: 4
page_type: tutoriel
description: "Cet article vous guidera à travers la façon de configurer Braze pour utiliser Okta pour une seule signature."
---

# Octa

!\[Okta SAML\]\[4\]{: style="float:right;height:200px;margin-left:15px;margin-bottom:15px;"}

> Cet article vous guidera à travers la façon de configurer Braze pour utiliser Okta pour une seule signature.

Okta connecte n'importe quelle personne avec n'importe quelle application sur n'importe quel appareil. C'est un service de gestion d'identité, de niveau entreprise, construit pour le cloud, mais compatible avec de nombreuses applications sur place. Avec Okta, l'informatique peut gérer l'accès de n'importe quel employé à n'importe quelle application ou périphérique.
<br>

## Exigences

| Exigence                      | Détails                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| Okta activé pour votre compte | Contactez votre gestionnaire de compte Braze pour activer cette option pour votre compte |
| Privilèges Admin Okta         | Veuillez vous assurer d'avoir les privilèges d'administrateur avant de configurer Okta   |
| Privilèges Admin Braze        | Veuillez vous assurer d'avoir les privilèges d'administrateur avant de configurer Okta   |
{: .reset-td-br-1 .reset-td-br-2}

## Étape 1 : Configurer Braze

### Étape 1: Connectez-vous à votre compte Braze et accédez aux paramètres de sécurité

Connectez-vous à votre compte Braze en utilisant un compte admin.

Cliquez sur votre nom d'utilisateur et sélectionnez **Paramètres de la société** dans le menu déroulant. Ensuite, sélectionnez l'onglet **Paramètres de sécurité**.

Activer/désactiver le commutateur **SAML SSO** vert à **ON** depuis le côté droit de la page.

!\[SAML Okta\]\[1\]

### Étape 1b : Modifier les paramètres SAML SSO

Depuis votre tableau de bord d'administration Okta, vous recevrez une `URL cible` (URL de connexion) et `x. 09` certificat que vous devez entrer dans votre compte Braze.

| Exigences    | Détails du produit                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `Nom SAML`   | Cela apparaîtra comme le texte du bouton sur l'écran de connexion. C'est généralement votre nom IdP, par exemple, "Okta". |
| `Target URL` | Ceci est l'URL de connexion fournie par Okta Admin Dashboard.                                                             |
| `Certificat` | Le certificat `x.509` PEM encodé est fourni par votre IdP. Vous devez le copier et le coller dans ce champ.               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

!\[Activer SAML SSO\]\[5\]

Sélectionnez **Enregistrer les modifications** en bas de la page une fois terminé.

## Étape 2 : Activer le flux initié par l'IdP

Ensuite, vous devez créer votre clé API Braze avec la permission `sso.saml.login` activée.

- Si vous n'avez pas déjà une telle clé API Braze, on peut être créé en allant dans la **Console développeur** dans **Réglages**, puis cliquez sur **Créer une nouvelle clé API**.<br>D'ici, faites défiler jusqu'à la section SSO et vérifiez l'option `sso.saml.login` puis enregistrez la clé API.<br>

!\[SSO Set Up\]\[5\]{: style="max-width:80%"}

## Étape 3 : Configurer Okta

!\[Okta SAML\]\[2\]{: style="float:right;max-width:45%;margin-left:15px;"}

### Étape 3 : Accédez à Okta

Dans Okta, sélectionnez l'onglet **Sign On** pour l'application Braze SAML, puis cliquez sur **Edit**.

### Étape 3b: Mettre à jour l'état du relais par défaut

Entrez la clé API avec la permission `sso.saml.login` que vous avez faite à l'étape 2, dans le champ **État du relais par défaut**.

__Enregistrer ces nouveaux paramètres.__

{% alert tip %}
Si vous voulez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification par authentification unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) à partir de la page **Paramètres de la société**.
{% endalert %}

## Étape 4 : Connectez-vous

Vous devriez maintenant pouvoir vous connecter à Braze en utilisant Okta!
[1]: {% image_buster/assets/img/Okta/okta1.png %} [2]: {% image_buster /assets/img/Okta/okta2.png %} [4]: {% image_buster /assets/img/Okta/okta4.png %} [5]: {% image_buster /assets/img/sso2.png %} [6]: {% image_buster /assets/img/samlsso.gif %}