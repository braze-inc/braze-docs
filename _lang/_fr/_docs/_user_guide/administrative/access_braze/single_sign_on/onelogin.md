---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutoriel
description: "Cet article vous guidera dans la façon de configurer Braze pour utiliser OneLogin pour l'authentification unique."
---

# OneLogin

> Cet article vous guidera à travers la façon de configurer braze pour utiliser onelogin pour une seule signature.

[OneLogin](https://www.onelogin.com/) est une plateforme d’identité cloud qui fournit une solution complète pour la gestion des identités des utilisateurs. OneLogin s'intègre avec les applications cloud et sur site en utilisant SAML 2.0, pour Single Sign-On (SSO), l'authentification multi-facteurs, et plus encore.

## Exigences

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL de service à la clientèle d'assertion (ACS).

| Exigences            | Détails du produit                                                                                                                                                                                                                                                                                                                           |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Domaine de Braze** | Vous aurez besoin de votre domaine Braze pour installer Braze dans OneLogin. Si votre instance est `US-01`, vous devrez entrer l'URL de votre tableau de bord dans le tableau de bord OneLogin . <br> Par exemple, si l'URL de votre tableau de bord est `https://dashboard-01.braze.com`, vous devez entrer `dashboard-01.braze.com`. |
{: .reset-td-br-1 .reset-td-br-2}

## Le fournisseur de services (SP) a initié la connexion depuis OneLogin

### Étape 1 : Configurer l'application Braze

1. Connectez-vous à [OneLogin](https://app.onelogin.com/login). Cliquez sur **Administration**.<br><br> ![Administration]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>

2. Allez à **Applications** > **Ajouter des applications** dans la barre de navigation supérieure. Recherchez "Braze" et sélectionnez l'application Braze.<br><br> ![Résultat du Braze]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>

3. Enregistrez l'application Braze dans votre entreprise.<br><br> ![Appli Braze]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>

4. Une fois enregistré, allez à **Configuration** et ajoutez votre **domaine Braze**.<br><br> ![Configuration]({% image_buster /assets/img/onelogin_4.png %})<br><br>

5. Braze attend les assertions SAML dans un [format spécifique][1]. Sous **Paramètres** les attributs [][1] supportés par Braze doivent être pré-remplis. Vérifiez simplement que cela est correct.<br><br> ![SAML]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>

6. Copiez le **Certificat** et **SAML 2. Point de terminaison (HTTP)** nécessaire pour mettre en place le tableau de bord Braze sous l'onglet **SSO**.<br><br> ![Certifications]({% image_buster /assets/img/onelogin_6.jpg %})

### Étape 2 : Configurer OneLogin dans Braze

Once you have set up Braze within your OneLogin, they will provide a Target URL (`SAML 2.0 Endpoint (HTTP)`) and `x.509` certificate which you will input into your Braze account.

Après que votre gestionnaire de compte ait activé SAML SSO pour votre compte, allez dans **Paramètres de la société** > **Paramètres de sécurité** et basculez la section SAML SSO sur **ON**.

Sur cette page, vous saisissez :

| Exigences    | Détails du produit                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `Nom SAML`   | Cela apparaîtra comme le texte du bouton sur l'écran de connexion. Ceci est généralement votre nom IdP, comme "OneLogin". |
| `Target URL` | Ceci est l'URL `SAML 2.0 Endpoint (HTTP)` fournie par OneLogin.                                                           |
| `Certificat` | Le certificat `x.509` PEM encodé est fourni par votre OneLogin.                                                           |
{: .reset-td-br-1 .reset-td-br-2}

![Activer SAML SSO]({% image_buster /assets/img/samlsso.gif %})

## Créer et activer une clé API Braze pour la connexion IdP (optionnel)

Pour activer la connexion initiée par IdP, vous devez d'abord créer une clé d'API dans **Console développeur** > **Paramètres API**.

![Configuration SSO]({% image_buster /assets/img/sso2.png %})

Entrez la clé d'API générée en tant que paramètre `RelayState` dans OneLogin sous **Configuration**, qui sera utilisé pour identifier la société dans laquelle l'utilisateur tente de se connecter.

{% alert tip %}
Si vous voulez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification par authentification unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) à partir de la page **Paramètres de la société**.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider
