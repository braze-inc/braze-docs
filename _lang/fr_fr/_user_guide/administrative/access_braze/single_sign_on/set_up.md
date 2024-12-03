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
| URL de l’Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Pour les domaines de l'Union européenne, l'URL ASC est `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Pour certains IdP, il peut également s'agir de l'URL de réponse, de l'URL de connexion, de l'URL d'audience ou de l'URI d'audience. |
| Entity ID | `braze_dashboard` |
| RelayState API key | Sélectionnez **Paramètres** > **Clés API** et créez une clé API avec les autorisations `sso.saml.login`, puis saisissez la clé API générée comme paramètre `RelayState` dans votre IdP. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous pouvez trouver vos clés API sous **Paramètres** dans **Console Développeur** > **Paramètres API**.
{% endalert %}

## Configuration Authentification unique (SSO) SAML

### Étape 1 : Configurer votre fournisseur d’identité

Configurez Braze en tant que fournisseur de services (SP) dans votre fournisseur d'identité (IdP) à l'aide des informations suivantes. En outre, configurez le mappage des attributs SAML.

{% alert important %}
Si vous prévoyez d'utiliser Okta comme fournisseur d'identité, assurez-vous d'utiliser l'intégration prédéfinie disponible sur le [site d'Okta](https://www.okta.com/integrations/braze/).
{% endalert %}

| Attribut SAML | Requis ? | Attributs SAML acceptés |
|---|---|---|
|`email` | Requis | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | Facultatif | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | Facultatif | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze n’exige que `email` dans l’assertion SAML.
{% endalert %}

### Étape 2 : Configurer Braze

Lorsque vous aurez fini de configurer Braze dans votre fournisseur d'identité, celui-ci vous fournira une URL cible et un certificat `x.509` à introduire dans votre compte Braze.

Une fois que votre gestionnaire de compte a activé l'authentification SAML pour votre compte, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section SAML SSO sur **ON (activé)**.

{% alert note %}
Si vous utilisez l[a navigation plus ancienne]({{site.baseurl}}/navigation), sélectionnez l'icône de votre compte et allez dans **Paramètres de l'entreprise** > **Paramètres de sécurité** pour trouver la section SSO SAML.
{% endalert %}

Sur la même page, saisissez les données suivantes :

| Condition | Détails |
|---|---|
| `SAML Name` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion.<br>Il s'agit généralement du nom de votre fournisseur d'identité, comme « Okta ». |
| `Target URL` | Ceci est fourni après la configuration de Braze au sein de votre IdP.<br> Certains IdP font référence à l’URL d’authentification unique ou à l’endpoint SAML 2.0. |
| `Certificate` | Le certificat `x.509` fourni par votre fournisseur d'identité.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Assurez-vous que votre certificat `x.509` respecte ce format lorsque vous l'ajoutez au tableau de bord :

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Ouverture des paramètres de sécurité et ajout des détails de l'authentification unique (SSO) SAML]({% image_buster /assets/img/samlsso.gif %})

### Étape 3 : Se connecter à Braze

Enregistrez vos paramètres de sécurité et déconnectez-vous. Ensuite, reconnectez-vous avec votre fournisseur d'identité.

![Écran de connexion du tableau de bord avec authentification unique activée]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## Comportement d’authentification unique (SSO)

Les membres qui choisissent d’utiliser l’authentification unique ne pourront plus utiliser leur mot de passe comme ils l’ont fait auparavant. Les utilisateurs qui continuent à utiliser leur mot de passe seront en mesure de ne pas les utiliser à moins que les paramètres suivants les limitent.

## Restriction 

Vous pouvez également choisir de limiter les membres de votre organisation pour qu’ils se connectent uniquement avec l’authentification unique de Google ou l’authentification unique (SSO) SAML. Pour activer les restrictions, allez dans **Paramètres de sécurité** et sélectionnez soit **Appliquer la connexion Google SSO unique**, soit **Appliquer la connexion SAML SSO personnalisée (SSO SAML) unique.**

![Section Règles d'authentification de la page Paramètres de sécurité]({% image_buster /assets/img/sso3.png %})

En activant les restrictions, les utilisateurs de Braze de votre entreprise ne pourront plus se connecter à l'aide d'un mot de passe, même s'ils se sont déjà connectés avec un mot de passe auparavant.
