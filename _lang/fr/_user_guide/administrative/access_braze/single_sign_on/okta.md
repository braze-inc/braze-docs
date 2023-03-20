---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "Cet article vous expliquera comment configurer Braze pour utiliser Okta pour une authentification unique. 

---

# Okta 

![Connexion du tableau de bord de Braze avec l’authentification unique Okta activée][4]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;"}

> Cet article vous expliquera comment configurer Braze pour utiliser Okta pour une authentification unique.

Okta connecte toute personne à n’importe quelle application sur n’importe quel appareil. Il s’agit d’un service de gestion d’identité, de qualité professionnelle, conçu pour le cloud, mais compatible avec de nombreuses applications sur site. Avec Okta, l’informatique peut gérer l’accès de tout employé à toute application ou tout appareil.
<br>

## Conditions

| Condition | Détails |
| ----------- | ------- |
| RelayState API key | Créez une clé API dans la **Developer Console** sous **API Settings** (Paramètres API) avec les autorisations `sso.saml.login`. |
| Okta a activé votre compte | Contactez votre gestionnaire de compte Braze pour que cela soit activé pour votre compte |
| Privilèges d’administrateur Okta | Assurez-vous de disposer des privilèges d’administrateur avant de configurer Okta |
| Privilèges administrateur Braze | Assurez-vous de disposer des privilèges d’administrateur avant de configurer Okta |
{: .reset-td-br-1 .reset-td-br-2}

## Étape 1 : Configurer Braze

### Étape 1a : Accédez aux Security Settings (Paramètres de sécurité) dans Braze

1. Connectez-vous au compte Braze en utilisant un compte administrateur.
2. Cliquez sur votre nom d’utilisateur et sélectionnez **Company Settings (Paramètres de l’entreprise)** > **Security Settings (Paramètres de sécurité)**. 
3. Basculez le bouton **SAML SSO (Authentification unique (SSO) SAML)** sur activé.

![Authentification unique (SSO) SAML Okta activée sur la page Security Settings (Paramètres de sécurité)][1]

### Étape 1b : Modifier les paramètres de l’Authentification unique (SSO) SAML

À partir du tableau de bord Administrateur Okta, vous recevrez un `Target URL` (URL de connexion) et un certificat `x.509` que vous devez saisir sur votre compte Braze.

| Condition | Détails |
|---|---|
| `SAML Name` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion. Il s’agit généralement de votre nom IdP, par exemple « Okta ». |
| `Target URL` | Il s’agit de l’URL de connexion fournie par le tableau de bord Admin Okta.|
| `Certificate` | Le certificat codé PEM `x.509` est fourni par votre IdP. Vous devez le copier et coller dans ce champ. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Sélectionnez **Save Changes (Enregistrer les modifications)** au bas de la page une fois terminé.

## Étape 2 : Configurer Okta

Dans Okta, sélectionnez **Sign On (Connexion)** pour l’application Braze SAML, puis cliquez sur **Edit (Modifier)**. 

Entrez ensuite la clé API RelayState avec l’autorisation `sso.saml.login` dans le champ **Default Relay State (État du Relay State par défaut)**. 

![Okta Default RelayState dans l’onglet Sign On (Connexion).][2]{: style="max-width:75%"}

Assurez-vous d’enregistrer ces nouveaux paramètres.

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec l’authentification unique (SSO) SAML, vous pouvez [limiter l’authentification de connexion unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) depuis la page **Company Settings (Paramètres de l’entreprise)**.
{% endalert %}

## Étape 3 : Se connecter

Vous devriez maintenant pouvoir vous connecter à Braze en utilisant Okta !


[1]: {% image_buster/assets/img/Okta/okta1.png %}
[2]: {% image_buster /assets/img/Okta/okta2.png %}
[4]: {% image_buster /assets/img/Okta/okta4.png %}
[5]: {% image_buster /assets/img/sso2.png %}
[6]: {% image_buster /assets/img/samlsso.gif %}