---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "Cet article vous expliquera comment configurer Braze pour utiliser OneLogin pour une authentification unique."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) est une plateforme d’identité du cloud qui fournit une solution complète pour gérer les identités des utilisateurs. OneLogin s’intègre aux applications cloud et sur site utilisant SAML 2.0, pour l’authentification unique (SSO), provisionnement utilisateur, authentification multifacteurs, etc.

## Conditions

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL d’Assertion Consumer Service (ACS).  

| Condition | Détails |
|---|---|
| Domaine Braze | Vous aurez besoin de votre domaine Braze pour configurer Braze dans OneLogin. Si votre instance est `US-01`, vous devrez saisir votre URL de tableau de bord dans le tableau de bord OneLogin. <br><br> Par exemple, si votre URL de tableau de bord est `https://dashboard-01.braze.com`, vous devez saisir `dashboard-01.braze.com`.  |
| RelayState API key | Pour activer la connexion IdP, créez une clé API dans la **Developer Console (Console du développeur)** sous **API Settings (Paramètres API)** avec les autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2}

## Connexion initiée par IdP dans OneLogin

### Étape 1 : Configurer l’application Braze

1. Connectez-vous à [OneLogin](https://app.onelogin.com/login). Cliquez sur la **page Administration**OneLogin Administration (Administration OneLogin)![.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Allez sur **Apps** > **Add Apps (Ajouter des apps)** dans la barre de navigation supérieure. Recherchez « Braze » et sélectionnez l’application Braze.![Recherchez les résultats de Braze dans OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Enregistrez l’application Braze dans votre entreprise.![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Une fois enregistrée, allez sur **Configuration** et ajoutez **Braze Domain (Domaine Braze)** et la clé API **RelayState**.![Onglet Configuration OneLogin pour l’application Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze requiert des assertions SAML dans un [format spécifique][1]. Sous **Parameters (Paramètres)**, les attributs supportés par Braze doivent être préremplis. Vérifiez qu’ils sont corrects.![Paramètres SAML de Braze  dans OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copiez le **Certificat** et l’**endpoint SAML 2.0 (HTTP)** nécessaire pour configurer le tableau de bord de Braze sous l’onglet **SSO**.![Certificats à copier depuis l’onglet SSO de l’application Braze dans OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Étape 2 : Configurer OneLogin dans Braze

Une fois que vous avez configuré Braze dans votre OneLogin, il vous fournira une URL cible (`SAML 2.0 Endpoint (HTTP)`) et `x.509` que vous saisirez sur votre compte Braze.

Une fois que votre gestionnaire de compte a activé l’Authentification unique (SSO) SAML pour votre compte, allez à **Company Settings (Paramètres de l’entreprise)** > **Security Settings (Paramètres de sécurité)** et basculez la section SAML SSO (Authentification unique (SSO) SAML) sur **ON**.

Sur cette page, saisissez les éléments suivants :

| Condition | Détails |
|---|---|
| `SAML Name` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion. Il s’agit généralement de votre nom d’IdP, comme « OneLogin ». |
| `Target URL` | C’est l’URL `SAML 2.0 Endpoint (HTTP)` fournie par OneLogin.|
| `Certificate` | Le certificat codé PEM `x.509` est fourni par votre OneLogin. |
{: .reset-td-br-1 .reset-td-br-2}

![Ouverture des paramètres de sécurité dans Braze et ajout des détails de l’Authentification unique (SSO) SAML]({% image_buster /assets/img/samlsso.gif %})

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec l’authentification unique (SSO) SAML, vous pouvez [limiter l’authentification de connexion unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) depuis la page **Company Settings (Paramètres de l’entreprise)**.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider
