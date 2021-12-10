---
nav_title: Azure Active Directory
article_title: Azure Active Directory
page_order: 3
page_type: tutoriel
description: "Cet article vous guidera dans la mise en place de fonctionnalités de signalisation Azure AD avec Braze."
---

# Azure Active Directory

> Cet article vous guidera dans la mise en place de fonctionnalités de signalisation Azure AD avec Braze.

[Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) est le service de gestion de l'accès et de l’identité nuageuse de Microsoft, qui aide votre employé à se connecter et à accéder aux ressources. Vous pouvez utiliser Azure AD pour contrôler l'accès à vos applications et aux ressources de votre application, en fonction des exigences de votre entreprise.

## Exigences

Lors de la configuration, il vous sera demandé de fournir une URL de connexion et une URL de service à la clientèle d'assertion (ACS).

| Exigences                                           | Détails du produit                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **URL de connexion**                                | `https://<SUBDOMAIN>.braze.com/sign_in` <br> Pour le sous-domaine, utilisez le sous-domaine coordonné listé dans [votre URL d'instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). Par exemple, si votre instance est `US-01`, votre URL est `https://dashboard-01.braze.com`. Cela signifie que votre sous-domaine sera `tableau de bord -01`. |
| **URL du service à la clientèle d'assertion (ACS)** | `https://<SUBDOMAIN>/auth/saml/callback` <br> *Pour certains IdPs, ceci peut également être appelé l'URL de réponse, URL d'audience ou URI d'audience.*                                                                                                                                                                                                                               |
| **ID de l'entité**                                  | `Tableau de bord`                                                                                                                                                                                                                                                                                                                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

## Le fournisseur de services (SP) a initié la connexion dans Azure AD

### Étape 1 : Ajouter Braze de la galerie

#### Étape 1a: Allez sur le Répertoire Actif Azure

Allez sur le portail Azure et cliquez sur **Azure Active Directory** dans le panneau de navigation gauche.

![Répertoire Azure actif]({% image_buster /assets/img/azure_1.png %})

#### Étape 1b: Trouver des applications

Naviguez vers **Applications d'entreprise**, puis sélectionnez **Toutes les applications**.

![Application de recherche Azure]({% image_buster /assets/img/azure_2.png %})

#### Étape 1c: Créer une nouvelle application

Ajouter une nouvelle application en cliquant sur **+ Nouvelle application** en haut de la boîte de dialogue.

#### Étape 1: Ajouter Braze

Recherchez **Braze** dans la zone de recherche, puis sélectionnez-la dans le panneau de résultats, puis cliquez sur **Ajouter**.

### Étape 2 : Configurer l'authentification unique Azure AD

#### Étape 2 : Sélectionner une authentification unique

Dans votre portail Azure, allez sur la page **Braze Application Integration** et sélectionnez **Single Sign-on**.

![Azure portal]({% image_buster /assets/img/azure_5.png %})

#### Étape 2b: Sélectionnez la méthode SSO

Sélectionnez **SAML/WS-Fed** comme votre méthode dans la **Sélection d'une méthode de signature** unique pour ouvrir la **Mettre en place Single Sign-On avec la page SAML**.

![SSO Azure]({% image_buster /assets/img/azure_6.png %})

#### Étape 2c: Ouvrir la boîte de dialogue de configuration

À partir de là, cliquez sur l'icône d'édition pour ouvrir la boîte de dialogue **Configuration SAML de base**.

![Configuration Azure]({% image_buster /assets/img/azure_7.png %})

#### Étape 2: Configurer en mode IdP

Si vous voulez configurer l'application en mode initié par IdP, entrez une URL qui combine [votre instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) avec le modèle suivant : `https://<SUBDOMAIN>. raze.com/auth/saml/callback`.

![Idp Azure]({% image_buster /assets/img/azure_8.png %})

#### Étape 2: Configurer en mode SP

Si vous voulez configurer l'application en mode initié par le SP, cliquez sur **Définir des URL supplémentaires** et entrez une URL qui combine [votre instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) avec le modèle suivant : `https://<SUBDOMAIN>. raze.com/sign_in`.

![Mode Azure SP]({% image_buster /assets/img/azure_9.png %})

#### Étape 2 : Formater les assertions SAML

Braze attend les assertions SAML dans un format spécifique. Reportez-vous aux onglets suivants sur les attributs des utilisateurs et les revendications des utilisateurs pour comprendre comment ces attributs et valeurs doivent être formatés.

{% tabs %}
{% tab User Attributes %}
Vous pouvez gérer les valeurs de ces attributs à partir de la section **Attributs utilisateur** sur la page **Intégration d'application**.

![Azure SAML]({% image_buster /assets/img/azure_10.png %})

Utilisez les appairages d'attributs suivants :

- `nom donné` = `user.givenname`
- `nom de famille`= `nom d'utilisateur`
- `adresse e-mail` = `user.userprincipalname`
- `nom` = `user.userprincipalname`
- `Identifiant d'utilisateur unique` = `user.userprincipalname`

{% endtab %}
{% tab User Claims %}

Sur la page **Configurer l'authentification unique avec la page SAML** , cliquez sur **Modifier** pour ouvrir la boîte de dialogue **Attributs utilisateur**. Ensuite, modifiez les réclamations selon le format approprié, affiché ci-dessous.

![SSO Azure]({% image_buster /assets/img/azure_11.png %})

Utilisez les appairages de nom de revendication suivants :

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

Vous pouvez gérer ces revendications et valeurs utilisateur à partir de la boîte de dialogue **Gérer les revendications d'utilisateurs**:

![Revendications de l'utilisateur Azure]({% image_buster /assets/img/azure_12.png %})

{% endtab %}
{% endtabs %}

#### Étape 2g : Télécharger le certificat

Allez à la page **Configurer l'authentification unique avec la page SAML** , puis faites défiler la section **Certificat de signature SAML** et téléchargez le **Certificat (Base64)** en fonction de vos exigences.

![Certificat de téléchargement Azure]({% image_buster /assets/img/azure_13.png %})

#### Étape 2h: Copier les URLs pour la configuration dans Braze

Allez à la section **Configurer Braze** et copiez les URL appropriées à utiliser dans la [configuration de Braze](#step-3-configure-braze-single-sign-on).

![URL Azure pour la configuration]({% image_buster /assets/img/azure_14.png %})

### Étape 3 : Configurer Azure AD dans Braze

Une fois que vous aurez configuré Braze dans votre AD, ils fourniront une URL cible (URL de connexion) et **x. 09** certificat que vous entrerez dans votre compte Braze.

Après que votre gestionnaire de compte ait activé SAML SSO pour votre compte, allez dans **Paramètres de la société** > **Paramètres de sécurité** et basculez la section SAML SSO sur **ON**.

Sur cette page, vous ajouterez les éléments suivants :

| Exigences    | Détails du produit                                                                                                         |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `Nom SAML`   | Cela apparaîtra comme le texte du bouton sur l'écran de connexion. Ceci est généralement votre nom IdP, comme « Azure AD». |
| `Target URL` | Ceci est l'URL de connexion fournie par Azure AD.                                                                          |
| `Certificat` | Le certificat `x.509` PEM encodé est fourni par votre IdP.                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

![Activer SAML SSO]({% image_buster /assets/img/samlsso.gif %})

## Créer et activer une clé API Braze pour la connexion IdP (optionnel)

Pour activer la connexion initiée par IdP, vous devez d'abord créer une clé d'API dans **Console développeur** > **Paramètres API**.

![Configuration SSO]({% image_buster /assets/img/sso2.png %})

Entrez la clé d'API générée en tant que paramètre `RelayState` dans Azure AD, qui sera utilisé pour identifier la société dans laquelle l'utilisateur tente de se connecter.

{% alert tip %}
Si vous voulez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification par authentification unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/restriction/) à partir de la page **Paramètres de la société**.
{% endalert %}
