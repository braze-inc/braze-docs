---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "Cet article vous expliquera comment configurer Braze pour utiliser OneLogin pour une authentification unique."

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) est une plateforme d'identité en nuage qui offre une solution complète de gestion des identités des utilisateurs. OneLogin s’intègre aux applications cloud et sur site utilisant SAML 2.0, pour l’authentification unique (SSO), provisionnement utilisateur, authentification multifacteurs, etc.

## Conditions

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL d’Assertion Consumer Service (ACS).  

| Condition | Détails |
|---|---|
| Domaine Braze | Vous aurez besoin de votre domaine Braze pour configurer Braze dans OneLogin. Si votre instance est `US-01`, vous devrez saisir votre URL de tableau de bord dans le tableau de bord OneLogin. <br><br> Par exemple, si votre URL de tableau de bord est `https://dashboard-01.braze.com`, vous devez saisir `dashboard-01.braze.com`.  |
| RelayState API key | Pour activer l'identifiant IdP, sélectionnez **Paramètres** > **Clés API** et créez une clé API avec les autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Identifiant initié par l'IdP dans OneLogin

### Étape 1 : Configurer l’application Braze

1. Connectez-vous à [OneLogin.](https://app.onelogin.com/login) Cliquez sur **Administration**.![Page d'administration OneLogin.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. Allez dans **Apps** > **Add Apps** dans la barre de navigation supérieure. Recherchez « Braze » et sélectionnez l’application Braze.![Résultats de recherche pour Braze dans OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Enregistrez l'application Braze dans votre entreprise.![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. Une fois enregistré, allez dans **Configuration** et ajoutez votre **domaine Braze** et votre clé API **RelayState**.![Onglet OneLogin Configuration pour l'application Braze.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze attend les assertions SAML dans un [format spécifique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider). Sous **Paramètres**, les attributs pris en charge par Braze devraient être pré-remplis. Vérifiez qu'ils sont corrects.![Paramètres SAML de Braze dans OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Copiez le **certificat** et l'**endpoint SAML 2.0 (HTTP)** nécessaires à la configuration du tableau de bord de Braze à partir de l'onglet **SSO**.![Certificats à copier à partir de l'onglet SSO de l'application Braze dans OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### Étape 2 : Configurer OneLogin dans Braze

Une fois que vous avez configuré Braze dans votre OneLogin, ils vous fourniront une URL de ciblage (`SAML 2.0 Endpoint (HTTP)`) et un certificat `x.509` que vous introduirez dans votre compte Braze.

Une fois que votre gestionnaire de compte a activé l'authentification SAML pour votre compte, allez dans **Paramètres** > **Paramètres administratifs** > **Paramètres de sécurité** et basculez la section SAML SSO sur **ON (ON)**.

Sur cette page, saisissez les éléments suivants :

| Condition | Détails |
|---|---|
| `SAML Name` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion. Il s'agit généralement du nom de votre fournisseur d'identité, comme « OneLogin ». |
| `Target URL` | C’est l’URL `SAML 2.0 Endpoint (HTTP)` fournie par OneLogin.|
| `Certificate` | Le certificat codé PEM `x.509` est fourni par votre OneLogin. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Paramètres SAML SSO avec la bascule sélectionnée.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification par connexion unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) depuis la page **Paramètres de l'entreprise**.
{% endalert %}

