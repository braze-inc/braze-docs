---
nav_title: Configuration Authentification unique (SSO) SAML
article_title: Configuration Authentification unique (SSO) SAML
page_order: 0
page_type: tutorial
description: "Cet article vous expliquera comment activer l’authentification unique SAML pour votre compte Braze."

---

# Le fournisseur de services (SP) a initié une connexion

> Cet article vous expliquera comment activer l’authentification unique SAML pour votre compte Braze.

## Conditions

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL d’Assertion Consumer Service (ACS).  

| Condition | Détails |
|---|---|
| URL de connexion | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> Pour le sous-domaine, utilisez le sous-domaine de coordination indiqué dans votre [URL de l’instance de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). Par exemple, si votre instance est `US-01`, votre URL est `https://dashboard-01.braze.com`. Cela signifie que votre sous-domaine sera `dashboard-01`. |
| URL de l’Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>/auth/saml/callback` <br><br> Pour certains IdP, cela peut également être appelé Reply URL, Audience URL ou Audience URI. |
| Entity ID | `braze_dashboard` |
| RelayState API key | Créez une clé API dans la **Developer Console** sous **API Settings (Paramètres API)** avec les autorisations `sso.saml.login`, puis saisissez la clé API générée comme paramètre `RelayState` au sein de votre IdP. |
{: .reset-td-br-1 .reset-td-br-2}

## Configuration Authentification unique (SSO) SAML

### Configurer votre fournisseur d’identité

Tout d’abord, vous devez configurer Braze en tant que prestataire de services (SP) dans votre fournisseur d’identité (IdP) avec les informations suivantes.

De plus, vous devrez configurer le mappage d’attribut SAML.

| Attribut SAML | Requis ? | Attributs SAML acceptés |
|---|---|---|
|`email` | Requis | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Facultatif | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Facultatif | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze n’exige que `email` dans l’assertion SAML.
{% endalert %}

### Configurer Braze

Une fois que vous avez configuré Braze dans votre IdP, il vous fournira une URL cible et un certificat `x.509` que vous saisirez sur votre compte Braze.

Une fois que votre gestionnaire de compte a activé l’Authentification unique (SSO) SAML pour votre compte, allez à `Company Settings (Paramètres de l’entreprise)` > `Security Settings (Paramètres de sécurité)` et basculez la section SAML SSO (Authentification unique (SSO) SAML) sur `ON`.

Sur cette page, vous avez saisi :

| Condition | Détails |
|---|---|
| `Nom SAML` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion.<br>Il s’agit généralement de votre nom d’IdP, comme « Okta ». |
| `URL cible` | Ceci est fourni après la configuration de Braze au sein de votre IdP.<br> Certains IdP font référence à l’URL d’authentification unique ou à l’endpoint SAML 2.0. |
| `Certificate` | Le certificat `x.509` est fourni par votre IdP.|
{: .reset-td-br-1 .reset-td-br-2}

Assurez-vous que votre certificat suit ce format lorsque vous l’ajoutez au tableau de bord :

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Ouverture des paramètres de sécurité et ajout des détails de l’Authentification unique (SSO) SAML]({% image_buster /assets/img/samlsso.gif %})

Lorsque vous enregistrez vos paramètres de sécurité et vous déconnectez, vous devriez maintenant pouvoir vous connecter avec votre IdP.

![Écran de connexion du tableau de bord avec l’authentification unique activée]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## Comportement SSO

Les membres qui choisissent d’utiliser l’authentification unique ne pourront **plus utiliser leur mot de passe comme ils l’ont fait auparavant**. Les utilisateurs qui continuent à utiliser leur mot de passe seront en mesure de ne pas les utiliser à moins que les paramètres suivants les limitent. 

## Restriction 

Vous pouvez également choisir de limiter les membres de votre organisation à se connecter avec l’authentification unique de Google ou l’authentification unique (SSO) SAML. Pour activer, allez à **Company Settings (Paramètres de l’entreprise)**  > **Security Settings (Paramètres de sécurité)** et sélectionnez **Enforce Google SSO only login [Appliquer la connexion Authentification unique (SSO) SAML de Google uniquement]** ou **Enforce custom SAML SSO only login [Appliquer la connexion Authentification unique (SSO) SAML personnalisée uniquement]**.

![Section Règles d’authentification de la page Security Settings (Paramètres de sécurité)]({% image_buster /assets/img/sso3.png %})

En activant cette option, les utilisateurs Braze de votre entreprise ne pourront plus se connecter à l’aide d’un mot de passe, même s’ils se sont connectés avec un mot de passe auparavant.
