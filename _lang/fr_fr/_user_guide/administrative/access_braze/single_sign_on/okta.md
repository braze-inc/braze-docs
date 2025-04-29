---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "Cet article vous expliquera comment configurer Braze pour utiliser Okta pour une authentification unique." 

---

# Okta 

![Connexion au tableau de bord de Braze avec l’authentification unique Okta activée.][4]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;"}

> Okta connecte toute personne à n’importe quelle application sur n’importe quel appareil. Il s’agit d’un service de gestion d’identité, de qualité professionnelle, conçu pour le cloud, mais compatible avec de nombreuses applications sur site. Avec Okta, votre équipe informatique peut gérer l'accès de n’importe quel employé à toute application ou à tout appareil.
<br>

## Conditions

| Condition | Détails |
| ----------- | ------- |
| Okta a activé votre compte | Contactez votre gestionnaire de compte Braze pour activer cette fonctionnalité pour votre compte. |
| Privilèges d’administrateur Okta | Assurez-vous d'avoir les privilèges d'administrateur avant de configurer Okta. |
| Privilèges administrateur Braze | Assurez-vous d'avoir les privilèges d'administrateur avant de configurer Okta. |
| RelayState API key | Pour activer l'identifiant IdP, sélectionnez **Paramètres** > **Clés API** et créez une clé API avec les autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous pouvez trouver vos clés API sous **Paramètres** dans **Console Développeur** > **Paramètres API**.
{% endalert %}

## Étape 1 : Configurer Braze

### Étape 1a : Accédez aux Paramètres de sécurité dans Braze

Après que votre gestionnaire de compte a activé SAML SSO pour votre compte, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section SAML SSO sur **ACTIVÉ**.

{% alert note %}
Si vous utilisez l[a navigation plus ancienne]({{site.baseurl}}/navigation), sélectionnez l'icône de votre compte et allez dans **Paramètres de l'entreprise** > **Paramètres de sécurité** pour trouver la section SSO SAML.
{% endalert %}

![Authentification unique (SSO) SAML Okta activée sur la page Paramètres de sécurité.][1]

### Étape 1b : Modifier les paramètres de l’Authentification unique (SSO) SAML

Depuis votre tableau de bord d'administration Okta, vous recevrez une URL cible (URL de connexion) et `x.509` certificat, que vous devez saisir dans la page **Sécurité** de votre compte Braze.

![][7]{: style="max-width:75%"}

| Condition | Détails |
|---|---|
| `SAML Name` | Cela apparaîtra comme le texte du bouton sur l’écran de connexion. C'est généralement le nom de votre fournisseur d'identité, par exemple, "Okta". |
| `Target URL` | Ceci est l'URL de connexion fournie par le tableau de bord d'administration Okta. Trouvez-le en allant dans **Applications** > votre application > onglet **Général** > **Lien d'intégration de l'application** > **Lien d'intégration**. |
| `Certificate` | Le certificat encodé PEM `x.509` est fourni par votre fournisseur d'identité. Vous devez le copier et coller dans ce champ. Récupérez-le dans Okta en allant dans **Certificats de signature SAML** et en sélectionnant **Actions** > **Télécharger le certificat**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sélectionnez **Enregistrer les modifications** en bas de la page une fois terminé.

## Étape 2 : Configurer Okta

Dans Okta, sélectionnez l'onglet **Connexion** pour l'application Braze SAML, puis cliquez sur **Modifier**. 

Ensuite, entrez la clé API RelayState avec l’autorisation `sso.saml.login` dans le champ **État du RelayState par défaut**. 

![État du RelayState par défaut d'Okta dans l'onglet Connexion.][2]{: style="max-width:75%"}

Assurez-vous d’enregistrer ces nouveaux paramètres.

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification par connexion unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) depuis la page **Paramètres de l'entreprise**.
{% endalert %}

## Étape 3 : Se connecter

Vous devriez maintenant pouvoir vous connecter à Braze en utilisant Okta !

[1]: {% image_buster/assets/img/Okta/okta1.png %}
[2]: {% image_buster /assets/img/Okta/okta2.png %}
[4]: {% image_buster /assets/img/Okta/okta4.png %}
[7]: {% image_buster /assets/img/Okta/okta5.png %}
[5]: {% image_buster /assets/img/sso2.png %}
[6]: {% image_buster /assets/img/samlsso.gif %}