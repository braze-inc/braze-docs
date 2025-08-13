---
nav_title: Configuration Authentification unique (SSO) SAML
article_title: Configuration Authentification unique (SSO) SAML
page_order: 0
page_type: tutorial
description: "Cet article vous expliquera comment activer l’authentification unique SAML pour votre compte Braze."

---

# Le fournisseur de services (SP) a initié une connexion

> Cet article vous explique comment activer l'authentification unique SAML pour votre compte Braze et comment obtenir une trace SAML.

## Conditions

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL d’Assertion Consumer Service (ACS).  

| Condition | Détails |
|---|---|
| URL de l’Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> Pour les domaines de l'Union européenne, l'URL ASC est `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`. <br><br> Pour certains IdP, il peut également s'agir de l'URL de réponse, de l'URL de connexion, de l'URL d'audience ou de l'URI d'audience. |
| Entity ID | `braze_dashboard` |
| RelayState API key | Sélectionnez **Paramètres** > **Clés API** et créez une clé API avec les autorisations `sso.saml.login`, puis saisissez la clé API générée comme paramètre `RelayState` dans votre IdP. Pour plus de détails, reportez-vous à la section [Configuration de votre RelayState](#setting-up-your-relaystate). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuration de l'authentification unique SAML (SSO)

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

Sur la même page, saisissez les données suivantes :

| Condition | Détails |
|---|---|
| Nom SAML | Cela apparaîtra comme le texte du bouton sur l’écran de connexion.<br>Il s'agit généralement du nom de votre fournisseur d'identité, comme « Okta ». |
| URL cible | Ceci est fourni après la configuration de Braze au sein de votre IdP.<br> Certains IdP font référence à l’URL d’authentification unique ou à l’endpoint SAML 2.0. |
| Certificat | Le certificat `x.509` fourni par votre fournisseur d'identité.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Assurez-vous que votre certificat `x.509` respecte ce format lorsque vous l'ajoutez au tableau de bord :

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Paramètres SAML SSO avec la bascule sélectionnée.]({% image_buster /assets/img/samlsso.png %})

### Étape 3 : Se connecter à Braze

Enregistrez vos paramètres de sécurité et déconnectez-vous. Ensuite, reconnectez-vous avec votre fournisseur d'identité.

![Écran de connexion du tableau de bord avec authentification unique activée]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## Mise en place de votre RelayState

1. Dans Braze, allez dans **Paramètres** > **API et identifiants**.
2. Dans l'onglet **Clés API**, sélectionnez le bouton **Créer une clé API**.
3. Dans le champ **Nom de la clé API**, saisissez un nom pour votre clé.
4. Développez la liste déroulante **SSO** sous **Permissions** et cochez **sso.saml.login**.<br><br>![La section "Permissions" avec sso.saml.login coché.]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. Sélectionnez **Créer une clé API**.
6. Dans l'onglet **Clés API**, copiez l'identifiant à côté de la clé API que vous avez créée.
7. Collez la clé API RelayState dans le RelayState de votre IdP (elle peut également apparaître comme "Relay State" ou "Default Relay State" en fonction de votre IdP).

## Comportement d’authentification unique (SSO)

Les membres qui choisissent d’utiliser l’authentification unique ne pourront plus utiliser leur mot de passe comme ils l’ont fait auparavant. Les utilisateurs qui continuent à utiliser leur mot de passe seront en mesure de ne pas les utiliser à moins que les paramètres suivants les limitent.

## Restriction 

Vous pouvez également choisir de limiter les membres de votre organisation pour qu’ils se connectent uniquement avec l’authentification unique de Google ou l’authentification unique (SSO) SAML. Pour activer les restrictions, allez dans **Paramètres de sécurité** et sélectionnez soit **Appliquer la connexion Google SSO unique**, soit **Appliquer la connexion SAML SSO personnalisée (SSO SAML) unique.**

![Exemple de configuration de la section "Règles d'authentification" avec un mot de passe d'une longueur minimale de 8 caractères et une possibilité de réutilisation du mot de passe de 3 fois. Les mots de passe expireront après 180 jours et les utilisateurs seront déconnectés après 1 440 minutes d'inactivité.]({% image_buster /assets/img/sso3.png %})

En activant les restrictions, les utilisateurs de Braze de votre entreprise ne pourront plus se connecter à l'aide d'un mot de passe, même s'ils se sont déjà connectés avec un mot de passe auparavant.

## Obtenir une trace SAML

Si vous rencontrez des problèmes d'identification liés au SSO, l'obtention d'une trace SAML peut vous aider à dépanner votre connexion SSO en identifiant ce qui est envoyé dans les requêtes SAML.

### Conditions préalables

Pour exécuter une trace SAML, vous avez besoin d'un traceur SAML. Voici deux options possibles en fonction de votre navigateur :

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### Étape 1 : Ouvrez le traceur SAML

Sélectionnez le traceur SAML dans la barre de navigation de votre navigateur. Assurez-vous que l'option **Pause** n'est pas sélectionnée, car cela empêcherait le traceur SAML de capturer ce qui est envoyé dans les demandes SAML. Lorsque le traceur SAML est ouvert, vous verrez qu'il remplit la trace.

![Traceur SAML pour Google Chrome.]({% image_buster /assets/img/saml_tracer_example.png %})

### Étape 2 : Connectez-vous à Braze à l'aide du SSO

Rendez-vous sur votre tableau de bord de Braze et essayez de vous connecter à l'aide du SSO. Si vous rencontrez une erreur, ouvrez le traceur SAML et réessayez. Une trace SAML a été collectée avec succès s'il y a une ligne avec une URL comme `https://dashboard-XX.braze.com/auth/saml/callback` et une étiquette SAML orange.

### Étape 3 : Exporter et envoyer à Braze

Sélectionnez **Exporter**. Pour **Sélectionner un profil de filtrage des cookies**, sélectionnez **Aucun.** Sélectionnez ensuite **Exporter**. Cela générera un fichier JSON que vous pourrez envoyer à l'assistance de Braze pour une résolution des problèmes plus poussée.

![Menu "Export SAML-trace preferences" avec l'option "None" sélectionnée.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## Résolution des problèmes

### L'adresse e-mail de l'utilisateur est-elle correctement configurée ?

Si vous obtenez l'erreur `ERROR_CODE_SSO_INVALID_EMAIL`, l'adresse e-mail de l'utilisateur n'est pas valide. Confirmez dans la trace SAML que le champ `saml2:Attribute Name="email"` correspond à l'adresse e-mail utilisée par l'utilisateur pour se connecter. Si vous utilisez Microsoft ID (anciennement Azure active directory), le mappage des attributs est `email = user.userprincipalname`.

L'adresse e-mail est sensible à la casse et doit correspondre exactement à celle qui a été configurée dans Braze, y compris celle configurée dans votre fournisseur d'identité (comme Okta, OneLogin, Microsoft Entra ID, et autres).

D'autres erreurs indiquent que vous avez des problèmes avec l'adresse e-mail de l'utilisateur :
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST` : L'adresse e-mail de l'utilisateur ne figure pas dans le tableau de bord.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING` : L'adresse e-mail de l'utilisateur est vide ou mal configurée.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` ou `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: L'adresse e-mail de l'utilisateur ne correspond pas à celle utilisée pour configurer le SSO.

### Disposez-vous d'un certificat SAML valide (certificatx.509 ) ?

Vous pouvez valider votre certificat SAML en utilisant [cet outil de validation SAML](https://www.samltool.com/validate_response.php). Notez qu'un certificat SAML expiré est également un certificat SAML invalide.

### Avez-vous téléchargé un certificat SAML correct (x.509 certificate) ?

Confirmez que le certificat figurant dans la section `ds:X509Certificate` de la trace SAML correspond à celui que vous avez téléchargé vers Braze. Cela n'inclut pas l'en-tête `-----BEGIN CERTIFICATE-----` et le pied de page `-----END CERTIFICATE-----`.

### Avez-vous mal saisi ou mal formaté votre certificat SAML (x.509 certificate) ?

Confirmez qu'il n'y a pas d'espaces blancs ou de caractères supplémentaires dans le certificat que vous avez soumis dans le tableau de bord de Braze.

Lorsque vous entrez votre certificat dans Braze, il doit être codé en PEM (Privacy Enhanced Mail) et formaté correctement (y compris l'en-tête `-----BEGIN CERTIFICATE-----` et le pied de page `-----END CERTIFICATE-----` ). 

Voici un exemple de certificat correctement formaté :

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### Le jeton de session de l'utilisateur est-il valide ?

Demandez à l'utilisateur concerné d' [effacer le cache et les cookies de son navigateur](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser), puis essayez à nouveau de vous connecter avec SAML SSO.

### Avez-vous défini votre RelayState ?

Si vous obtenez l'erreur `ERROR_CODE_SSO_INVALID_RELAY_STATE`, il se peut que votre RelayState soit mal configuré ou inexistant. Si vous ne l'avez pas encore fait, vous devez définir votre RelayState dans votre système de gestion IdP. Pour connaître la marche à suivre, reportez-vous à la section [Configuration de votre RelayState](#setting-up-your-relaystate). 

### L'utilisateur est-il coincé dans une boucle d'ouverture de session entre Okta et Braze ?

Si un utilisateur ne peut pas se connecter parce qu'il est bloqué entre le SSO d'Okta et le tableau de bord de Braze, vous devez aller sur Okta et définir la destination de l'URL SSO sur votre [instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) (par exemple, `https://dashboard-07.braze.com`). 

Si vous utilisez un autre IdP, vérifiez si votre entreprise a téléchargé le bon certificat SAML ou x.509 sur Braze.

### Utilisez-vous une intégration manuelle ?

Si votre entreprise n'a pas téléchargé l'app Braze depuis l'app store de votre IdP, vous devez télécharger l'intégration préconstruite. Par exemple, si Okta est votre IdP, vous téléchargerez l'application Braze depuis leur [page d'intégration](https://www.okta.com/integrations/braze/).
