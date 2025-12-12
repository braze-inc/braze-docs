---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "Cet article vous explique comment configurer les fonctionnalités d'authentification unique de Microsoft Entra avec Braze."

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) est le service de gestion des identités et des accès basé sur le cloud de Microsoft, qui aide vos employés à se connecter et à accéder aux ressources. Vous pouvez utiliser Entra SSO pour contrôler l'accès à vos applications et à vos ressources d'application, en fonction de vos exigences commerciales.

## Exigences

Lors de la configuration, il vous sera demandé de fournir l'URL de l'Assertion Consumer Service (ACS).  

| Exigence | Détails |
|---|---|
| URL du service consommateur d'assertions (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Pour certains fournisseurs d'identité, il peut également s'agir de l'URL de réponse, de l'URL de l'audience ou de l'URI de l'audience. |
| ID de l'entité | `braze_dashboard`|
| Clé API de RelayState | Pour activer l'identifiant du fournisseur d'identité, allez dans **Paramètres** > **Clés API** et créez une clé API avec les autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Identifiant initié par le fournisseur de services (SP) dans le cadre de Microsoft Entra SSO

### Étape 1 : Ajouter Braze à la galerie

1. Dans votre centre d'administration Microsoft Entra, allez dans **Identité** > **Applications** > **Applications d'entreprise**, puis sélectionnez **Nouvelle application**.
2. Recherchez **Braze** dans la zone de recherche, sélectionnez-le dans le panneau de résultats, puis sélectionnez **Ajouter.**

### Étape 2 : Configurer Microsoft Entra SSO

1. Dans votre centre d'administration Microsoft Entra, accédez à la page d'intégration de votre application Braze et sélectionnez **Authentification unique**.
2. Sur la page **Sélectionner une méthode d'authentification unique**, sélectionnez **SAML** comme méthode.
3. Sur la page **Set up Single Sign-On with SAML**, sélectionnez l'icône modifier pour **Basic SAML Configuration.**
4. Configurez l'application en mode IdP-initiated en entrant une **URL de réponse** qui combine votre [instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) avec le modèle suivant : `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Configurez éventuellement RelayState en saisissant votre clé API générée par Relay State dans le champ **Relay State (Optional).** 

{% alert important %}
**Ne** définissez **pas** le champ **Sign-On URL.**  Laissez ce champ vide pour éviter tout problème avec votre authentification SAML unique (SSO) initiée par l'IdP.
{% endalert %}

{: start="6"}
6\. Formatez les assertions SAML dans le format spécifique attendu par Braze. Reportez-vous aux onglets suivants sur les attributs et les revendications de l'utilisateur pour comprendre comment ces attributs et valeurs doivent être formatés.

{% tabs %}
{% tab User Attributes %}
Vous pouvez gérer les valeurs de ces attributs à partir de la section **Attributs de l'utilisateur** de la page **Intégration des applications.** 

Utilisez les combinaisons d'attributs suivantes :

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
Il est essentiel que le champ de l'e-mail corresponde à ce qui est configuré pour vos utilisateurs dans Braze. Dans la plupart des cas, ce sera la même chose que `user.userprincipalname`. Cependant, si vous avez une configuration différente, travaillez avec votre administrateur système pour vous assurer que ces champs correspondent exactement.
{% endalert %}

{% endtab %}
{% tab User Claims %}

Sur la page **Configurer l'authentification unique avec SAML**, sélectionnez **Modifier** pour ouvrir la boîte de dialogue **Attributs de l'utilisateur**. Ensuite, modifiez les revendications des utilisateurs en respectant le format approprié.

Utilisez les paires de noms de revendications suivantes :

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
Il est essentiel que le champ de l'e-mail corresponde à ce qui est configuré pour vos utilisateurs dans Braze. Dans la plupart des cas, ce sera la même chose que `user.userprincipalname`. Cependant, si vous avez une configuration différente, travaillez avec votre administrateur système pour vous assurer que ces champs correspondent exactement.
{% endalert %}

Vous pouvez gérer ces réclamations et valeurs d'utilisateur à partir de la section **Gérer les réclamations**.

{% endtab %}
{% endtabs %}

{: start="8"}
8\. Allez à la page **Configurer l'authentification unique avec SAML**, puis faites défiler jusqu'à la section **Certificat de signature SAML** et téléchargez le **certificat** approprié **(Base64)** en fonction de vos besoins.
9\. Allez à la section **Configurer Braze** et copiez les URL appropriées pour les utiliser dans la [configuration de Braze](#step-3).

### Étape 3 : Configurer Microsoft Entra SSO dans Braze {#step-3}

Après avoir configuré Braze dans le centre d'administration de Microsoft Entra, Microsoft Entra vous fournira une URL cible (URL d'identification) et un certificat que vous devrez introduire dans votre compte Braze. **x.509** que vous introduirez dans votre compte Braze.

Une fois que votre gestionnaire de compte a activé l'authentification unique SAML pour votre compte, procédez comme suit :

1. Allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section authentification unique SAML (SSO) sur **ON**.
2. Sur la même page, ajoutez ce qui suit :

| Exigence | Détails |
|---|---|
| `SAML Name` | Le texte du bouton apparaîtra sur l'écran d'identification. Il s'agit généralement du nom de votre fournisseur d'identité, comme "Microsoft Entra". |
| `Target URL` | Il s'agit de l'URL identifiant fournie par Microsoft Entra.|
| `Certificate` | Le certificat encodé `x.509` PEM est fourni par votre fournisseur d'identité. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification unique à]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) partir de la page **Paramètres de l'entreprise**.
{% endalert %}
