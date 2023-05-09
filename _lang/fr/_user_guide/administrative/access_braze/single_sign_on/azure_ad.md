---
nav_title: Azure Active Directory
article_title: Azure Active Directory
page_order: 3
page_type: tutorial
description: "Cet article vous expliquera comment configurer les fonctionnalités d’ouverture de session Azure AD avec Braze."

---

# Azure Active Directory

> [Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) est le service de gestion d’accès et d’identité basé sur le cloud de Microsoft, qui aide l’employé à se connecter et à accéder aux ressources. Vous pouvez utiliser Azure AD pour contrôler l’accès à vos applications et aux ressources de votre application, en fonction des exigences de votre entreprise.

## Conditions

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL d’Assertion Consumer Service (ACS).  

| Condition | Détails |
|---|---|
| URL de connexion | `https://<SUBDOMAIN>.braze.com/sign_in` <br><br> Pour le sous-domaine, utilisez le sous-domaine de coordination indiqué dans votre [URL de l’instance de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). Par exemple, si votre instance est `US-01`, votre URL est `https://dashboard-01.braze.com`. Cela signifie que votre sous-domaine sera `dashboard-01`. |
| URL de l’Assertion Consumer Service (ACS) | `https://<SUBDOMAIN>/auth/saml/callback` <br> Pour certains IdP, cela peut également être appelé Reply URL, Audience URL ou Audience URI. |
| Entity ID | `braze_dashboard`|
| RelayState API key | Pour activer la connexion IdP, créez une clé API dans la **Developer Console (Console du développeur)** sous **API Settings (Paramètres API)** avec les autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2}

## Le fournisseur de services (SP) a initié une connexion dans Azure AD

### Étape 1 : Ajouter un Braze à partir de la galerie

#### Étape 1a : Accéder Azure Active Directory 

Accédez au portail Azure et cliquez sur **Azure Active Directory** (Répertoire Azure Active) dans le panneau de navigation gauche.

Ensuite, naviguez vers **Enterprise Applications (Applications d’entreprise)**, puis sélectionnez **All applications (Toutes les applications)**.

![Le portail Azure sélectionne toutes les applications d’entreprise.]({% image_buster /assets/img/azure_2.png %})

#### Étape 1b : Créer une nouvelle application

Ajoutez une nouvelle application en cliquant sur **+ New application (+ Nouvelle application)** en haut de la boîte de dialogue.

Recherchez **Braze** dans la zone de recherche, sélectionnez-le dans le panneau de résultats, puis cliquez sur **Add (Ajouter)**.

### Étape 2 : Configurer l’authentification unique Azure AD

#### Étape 2a : Sélectionner une authentification unique

Dans votre portail Azure, allez sur la page **Braze Application Integration (Intégration de l’application Braze)** et sélectionnez **Single sign-on (Authentification unique)**.

Ensuite, sélectionnez **SAML/WS-Fed** comme méthode dans la boîte de dialogue **Select a single sign-on method (Sélectionner une méthode d’authentification unique)** pour accéder à la page **Set up Single Sign-On with SAML (Configurer l’authentification unique avec SAML)**.

![Le portail Azure sélectionne une boîte de dialogue de méthode d’authentification unique.]({% image_buster /assets/img/azure_6.png %})

#### Étape 2b : Boîte de dialogue Configurer

À partir de là, cliquez sur l’icône Edit (Modifier) pour ouvrir la boîte de dialogue **Basic SAML Configuration (Configuration SAML de base)**.

![Portail Azure modifiant la configuration SAML de base.]({% image_buster /assets/img/azure_7.png %})

###### Configurer l’application en mode IdP-initialisé (requis)

Pour configurer l’application en mode IdP-initialisé, saisissez une URL qui combine l’[Instance de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) avec le modèle suivant : `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.

![Portail Azure modifiant la configuration SAML de base.]({% image_buster /assets/img/azure_8.png %})

###### Configurer RelayState (requis)

Dans la boîte RelayState, saisissez la clé API générée par RelayState.

![]({% image_buster /assets/img/relaystate2.png %})

###### Configurer le panneau URL (facultatif)

Pour configurer l’application en mode SP-initialisé, cliquez sur **Set additional URLs** (Saisir une URL supplémentaire) et entrez une URL qui combine l’[Instance de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) avec le modèle suivant : `https://<SUBDOMAIN>.braze.com/sign_in`.

![Portail Azure définissant une URL de connexion supplémentaire.]({% image_buster /assets/img/azure_9.png %})

#### Étape 2c : Formater les assertions SAML

Braze requiert des assertions SAML dans un format spécifique. Reportez-vous aux onglets suivants sur les attributs utilisateur et les demandes utilisateur pour comprendre comment ces attributs et valeurs doivent être formatés.

{% tabs %}
{% tab User Attributes %}
Vous pouvez gérer les valeurs de ces attributs à partir de la section **User Attributes (Attributs utilisateur)** de la page **Application Integration (Intégration d’applications)**.

![Attributs utilisateur de la page Intégration d’applications dans Azure.]({% image_buster /assets/img/azure_10.png %})

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

Sur la page **Set up Single Sign-On with SAML (Configurer une authentification unique avec SAML)**, cliquez sur **Edit (Modifier)** pour ouvrir la boîte de dialogue **User Attributes (Attributs utilisateur)**. Modifiez ensuite les demandes selon le format approprié.

![Boîte de dialogue Attributs utilisateur dans Azure.]({% image_buster /assets/img/azure_11.png %})

Utiliser les paires de noms de demandes suivantes :

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
Il est extrêmement important que le champ d’e-mail corresponde à celui qui est réglé pour vos utilisateurs dans Braze. Il sera le même que `user.userprincipalname` dans la plupart des cas. Cependant, si vous avez une configuration différente, consultez votre administrateur système pour vous assurer que ces champs correspondent exactement.
{% endalert %}

Vous pouvez gérer ces demandes d’utilisateurs et valeurs depuis la boîte de dialogue **Manage user claims (Gérer les demandes utilisateur)** :

![Gérer la boîte de dialogue de demandes dans Azure]({% image_buster /assets/img/azure_12.png %})

{% endtab %}
{% endtabs %}

#### Étape 2d : Télécharger le certificat

Allez à la page **Set up Single Sign-On with SAML (Configurer l’authentification unique avec SAML)**, puis faites défiler jusqu’à **SAML Signing Certificate (Certificat de signature SAML)** et téléchargez le **Certificat (Base64)** selon vos exigences.

![Téléchargement du certificat de signature SAML Azure.]({% image_buster /assets/img/azure_13.png %})

#### Étape 2e : Copier les URL pour la configuration à Braze

Allez à la section **Set up Braze (Configurer Braze)** et copiez les URL appropriées pour une utilisation dans la [Braze configuration (Configuration de Braze)](#step-3-configure-braze-single-sign-on).

![URL Azure pour la configuration.]({% image_buster /assets/img/azure_14.png %})

### Étape 3 : Configurer Azure AD au sein du Braze

Une fois que Braze est configuré dans AD Azure, une URL cible (URL de connexion) et un certificat **x.509** seront fournis, que vous saisirez sur votre compte Braze.

Une fois que votre gestionnaire de compte a activé l’Authentification unique (SSO) SAML pour votre compte, allez à **Company Settings (Paramètres de l’entreprise)** > **Security Settings (Paramètres de sécurité)** et basculez la section SAML SSO (Authentification unique (SSO) SAML) sur **ON**.

Sur cette page, vous ajouterez ce qui suit :

| Condition | Détails |
|---|---|
| `SAML Name` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion. Il s’agit généralement de votre nom d’IdP, comme « Azure AD ». |
| `Target URL` | Il s’agit de l’URL de connexion fournie par Azure AD.|
| `Certificate` | Le certificat codé PEM `x.509` est fourni par votre IdP. |
{: .reset-td-br-1 .reset-td-br-2}

![Ouverture des paramètres de sécurité et ajout des détails de l’Authentification unique (SSO) SAML.]({% image_buster /assets/img/samlsso.gif %})

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec l’authentification unique (SSO) SAML, vous pouvez [limiter l’authentification de connexion unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) depuis la page **Company Settings (Paramètres de l’entreprise)**.
{% endalert %}
