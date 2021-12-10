---
nav_title: Configuration SAML SSO
article_title: Configuration SAML SSO
page_order: 0
page_type: tutoriel
description: "Cet article vous guidera à travers la façon d'activer SAML authentification unique pour votre compte Braze."
---

# Connexion initiée par le fournisseur de services (SP)

> Cet article vous guidera à travers la façon d'activer SAML authentification unique pour votre compte Braze.

## Exigences

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL de service à la clientèle d'assertion (ACS).

| Exigences                                           | Détails du produit                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **URL de connexion**                                | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> Pour le sous-domaine, utilisez le sous-domaine coordonné répertorié dans [votre URL d'instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). Par exemple, si votre instance est `US-01`, votre URL est `https://dashboard-01.braze.com`. Cela signifie que votre sous-domaine sera `tableau de bord -01`. |
| **URL du service à la clientèle d'assertion (ACS)** | `https://<SUBDOMAIN>/auth/saml/callback` <br><br> *Pour certains IdPs, ceci peut également être appelé l'URL de réponse, URL d'audience ou URI d'audience.*                                                                                                                                                                                                                                    |
| **ID de l'entité**                                  | `Tableau de bord`                                                                                                                                                                                                                                                                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

## Configuration SAML SSO

### Configurer votre fournisseur d'identité

Tout d'abord, vous devez configurer Braze comme fournisseur de services (SP) dans votre fournisseur d'identité (IdP) avec les informations ci-dessous.

De plus, vous devrez configurer le mapping d'attributs SAML.

| Attribut SAML    | Requis ?  | Attributs SAML acceptés                                                                                                                                         |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Email`          | Requis    | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email`                                                              |
| `prénom`         | Optionnel | `prénom` <br> `prénom` <br> `prénom`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name`                                    |
| `nom_de famille` | Optionnel | `nom_de famille` <br> `nom-famille` <br> `nom-du-famille` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nom_du_de_du_du_famille` |

{% alert note %}
Braze nécessite seulement `email` dans l'Assertion SAML.
{% endalert %}

### Configurer Braze

Une fois que vous aurez configuré Braze dans votre IdP, ils fourniront une URL cible et `x. 09` certificat que vous entrerez dans votre compte Braze.

Après que votre gestionnaire de compte ait activé SAML SSO pour votre compte, allez dans `Paramètres de la société` > `Paramètres de sécurité` et basculez la section SAML SSO sur `ON`.

Sur cette page, vous saisissez :

| Exigences    | Détails du produit                                                                                                                                    |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Nom SAML`   | Cela apparaîtra comme le texte du bouton sur l'écran de connexion.<br>Ceci est généralement votre nom IdP, comme « Okta».                       |
| `Target URL` | Ceci est fourni après avoir configuré Braze dans votre IdP.<br> Certains IdP référencent ceci comme l'URL SSO ou le point d'extrémité SAML 2.0. |
| `Certificat` | Le certificat `x.509` est fourni par votre IdP.                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

Veuillez vous assurer que votre certificat respecte ce format lors de son ajout au tableau de bord :
```
-----BÉGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![Activer SAML SSO]({% image_buster /assets/img/samlsso.gif %})

Lorsque vous enregistrez vos paramètres de sécurité et que vous vous déconnectez, vous devriez maintenant être en mesure de vous connecter avec votre IdP.

![Page de connexion avec SSO]({% image_buster /assets/img/sso1.png %}){: style="largeur-max:40%;"}

### Créer et activer une clé API Braze pour la connexion IdP (optionnel)

Pour activer la connexion initiée par IdP, vous devez d'abord créer une clé d'API dans **Console développeur** > **Paramètres API**.

![Configuration SSO]({% image_buster /assets/img/sso2.png %})

Entrez la clé API générée en tant que paramètre `RelayState` dans votre IdP, qui sera utilisé pour identifier la société dans laquelle l'utilisateur tente de se connecter.

## Comportement SSO

Members who opt to use SSO will __no longer be able to use their password as they did prior__. Les utilisateurs qui continuent à utiliser leur mot de passe seront en mesure de le faire, sauf dans les paramètres ci-dessous.

## Restriction

Vous pouvez également choisir de restreindre les membres de votre organisation à se connecter avec Google SSO ou SAML SSO. Pour activer, allez dans **Paramètres de la société** > **Paramètres de sécurité** et sélectionnez soit __Forcer Google SSO seulement se connecter__ ou __Forcer la connexion personnalisée SAML SSO seulement__.

![Restriction SSO]({% image_buster /assets/img/sso3.png %})

En activant cette option, les utilisateurs de Braze de votre entreprise ne pourront plus se connecter en utilisant un mot de passe, même s'ils se sont connectés avec un mot de passe avant.
