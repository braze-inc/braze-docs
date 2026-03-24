---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "Cet article vous guidera dans la configuration des fonctionnalités d'authentification unique Microsoft Entra avec Braze."

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) est le service de gestion des identités et des accès basé sur le cloud de Microsoft, qui facilite la connexion et l'accès aux ressources pour vos employés. Vous pouvez utiliser Entra SSO pour contrôler l'accès à vos applications et à leurs ressources, en fonction des besoins de votre entreprise.

## Conditions

Lors de la configuration, il vous sera demandé de fournir une URL ACS (Assertion Consumer Service).  

| Condition | Détails |
|---|---|
| URL de l’Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> Pour certains fournisseurs d'identité, cela peut également être appelé URL de réponse, URL d'audience ou URI d'audience. |
| Entity ID | `braze_dashboard`|
| RelayState API key | Pour activer la connexion du fournisseur d'identité, sélectionnez **Paramètres** > **Clés API** et créez une clé API avec des autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Identifiant initié par le fournisseur de services (SP) dans Microsoft Entra SSO

### Étape 1 : Ajouter un Braze à partir de la galerie

1. Dans votre centre d'administration Microsoft Entra, veuillez vous rendre dans **Identité** > **Applications** > **Applications d'entreprise**, puis sélectionner **Nouvelle application**.
2. Veuillez rechercher **Braze** dans la zone de recherche, sélectionnez-le dans le panneau des résultats, puis sélectionnez **Ajouter**.

### Étape 2 : Configurer l'authentification unique Microsoft Entra

1. Dans votre centre d'administration Microsoft Entra, veuillez accéder à la page d'intégration de l'application Braze et sélectionner **« Authentification unique** ».
2. Sur la page **Sélectionner une méthode d'authentification unique**, veuillez sélectionner **SAML** comme méthode.
3. Sur la page **Configurer l'authentification unique avec SAML**, veuillez sélectionner l'icône Modifier pour **la configuration SAML de base**.
4. Configurez l'application en mode initié par IdP en entrant une **URL de réponse** qui combine votre [instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) avec le modèle suivant : `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. Veuillez configurer RelayState en saisissant votre clé API générée par Relay State dans le champ **Relay State**.

{% alert important %}
**Veuillez ne pas** remplir le champ **URL de connexion**. Veuillez laisser ce champ vide afin d'éviter tout problème avec votre authentification unique (SSO) SAML initiée par votre fournisseur d'identité.
{% endalert %}

{: start="6"}
6\. Formater les assertions SAML dans le format spécifique attendu par Braze. Reportez-vous aux onglets suivants sur les attributs utilisateur et les demandes utilisateur pour comprendre comment ces attributs et valeurs doivent être formatés.

{% tabs %}
{% tab User Attributes %}
Vous pouvez gérer les valeurs de ces attributs depuis la section **Attributs Utilisateur** sur la page **Intégration d'Application**.

Utiliser les associations d’attributs suivantes :

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
Il est extrêmement important que le champ d’e-mail corresponde à celui qui est réglé pour vos utilisateurs dans Braze. Il sera le même que `user.userprincipalname` dans la plupart des cas. Cependant, si vous avez une configuration différente, consultez votre administrateur système pour vous assurer que ces champs correspondent exactement.
{% endalert %}

{% endtab %}
{% tab User Claims %}

Sur la page **Configurer l'authentification unique avec SAML**, sélectionnez **Modifier** pour ouvrir la boîte de dialogue **Attributs utilisateur**. Ensuite, modifiez les demandes utilisateur selon le format approprié.

Utiliser les paires de noms de demandes suivantes :

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
Il est extrêmement important que le champ d’e-mail corresponde à celui qui est réglé pour vos utilisateurs dans Braze. Il sera le même que `user.userprincipalname` dans la plupart des cas. Cependant, si vous avez une configuration différente, consultez votre administrateur système pour vous assurer que ces champs correspondent exactement.
{% endalert %}

Vous pouvez gérer ces revendications et valeurs d'utilisateur à partir de la section **Gérer la revendication**.

{% endtab %}
{% endtabs %}

{: start="8"}
8\. Accédez à la page **Configurer l'authentification unique avec SAML**, puis faites défiler jusqu'à la section **Certificat de signature SAML** et téléchargez le **Certificat (Base64)** approprié en fonction de vos besoins.
9\. Allez à la section **Set up Braze** et copiez les URL appropriées à utiliser dans la [Braze configuration](#step-3).

### Étape 3 : Configurer Microsoft Entra SSO dans Braze {#step-3}

Une fois Braze configuré dans le centre d'administration Microsoft Entra, Microsoft Entra vous fournira une URL cible (URL d'identifiant) et**x.509**un certificat que vous devrez saisir dans votre compte Braze.

Une fois que votre gestionnaire de compte a activé l’authentification unique (SSO) SAML pour votre compte, procédez comme suit :

1. Accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et activez la section SAML SSO sur **ACTIVÉ**.
2. Sur la même page, ajoutez ce qui suit :

| Condition | Détails |
|---|---|
| `SAML Name` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion. Il s'agit généralement du nom de votre fournisseur d'identité, tel que « Microsoft Entra ». |
| `Target URL` | Il s'agit de l'identifiant de connexion fourni par Microsoft Entra.|
| `Certificate` | Le certificat encodé PEM `x.509` est fourni par votre fournisseur d'identité. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification par connexion unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) depuis la page **Paramètres de l'entreprise**.
{% endalert %}
