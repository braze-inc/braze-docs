---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "Cet article vous explique comment configurer Braze pour qu'il utilise Okta pour l'authentification unique." 

---

# Okta 

> Okta connecte n'importe quelle personne avec n'importe quelle application sur n'importe quel appareil. Il s'agit d'un service de gestion des identités de niveau professionnel, créé pour le cloud, mais compatible avec de nombreuses applications sur site. Avec Okta, votre équipe informatique peut gérer l'accès de n'importe quel employé à n'importe quelle application ou appareil.

## Exigences

| Exigence | Détails |
| ----------- | ------- |
| Okta activé pour votre compte | Contactez votre gestionnaire de compte Braze pour activer cette fonction pour votre compte. |
| Privilèges d'administrateur Okta | Assurez-vous d'avoir les privilèges d'administrateur avant de configurer Okta. |
| Privilèges d'administration de Braze | Assurez-vous d'avoir les privilèges d'administrateur avant de configurer Okta. |
| Clé API de RelayState | Pour activer l'identifiant IdP, allez dans **Paramètres** > **Clés API** et créez une clé API avec les autorisations `sso.saml.login`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 1 : Configurer Braze

### Étape 1a : Accédez aux paramètres de sécurité dans Braze

Une fois que votre gestionnaire de compte a activé l'authentification SAML pour votre compte, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez la section SAML SSO sur **ON (activé)**.

\![Okta SAML SSO activé sur la page Paramètres de sécurité.]({% image_buster/assets/img/Okta/okta1.png %})

### Étape 1b : Modifier les paramètres de l'authentification SAML unique (SSO)

Depuis votre tableau de bord Okta Admin, vous recevrez une URL cible (URL d'identification) et un certificat `x.509`, que vous devez saisir dans la page **Paramètres de sécurité** de votre compte Braze.

\![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| Exigence | Détails |
|---|---|
| `SAML Name` | Le texte du bouton apparaîtra sur l'écran d'identification. Il s'agit généralement du nom de votre fournisseur d'identité, par exemple "Okta". |
| `Target URL` | Il s'agit de l'URL d'identification fournie par le tableau de bord Okta Admin. Trouvez-le en allant dans **Applications** > votre application > onglet **Général** > **App Embed** **Link**> **Embed Link**. |
| `Certificate` | Le certificat encodé `x.509` PEM est fourni par votre fournisseur d'identité. Vous devez le copier et le coller dans ce champ. Récupérez-le dans Okta en allant sur **SAML Signing Certificates** et en sélectionnant **Actions** > **Download certificate.** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sélectionnez **Enregistrer les modifications** en bas de la page lorsque vous avez terminé.

## Étape 2 : Configurer Okta

Dans Okta, sélectionnez l'onglet **Sign On** pour l'app SAML de Braze, puis cliquez sur **Modifier**. 

Ensuite, saisissez la clé API RelayState avec l'autorisation `sso.saml.login` dans le champ **État relais par défaut.**  

\![Okta Default RelayState dans l'onglet Sign On.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

Veillez à enregistrer ces nouveaux paramètres.

{% alert tip %}
Si vous souhaitez que les utilisateurs de votre compte Braze se connectent uniquement avec SAML SSO, vous pouvez [restreindre l'authentification unique à]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) partir de la page **Paramètres de l'entreprise**.
{% endalert %}

## Étape 3 : Se connecter

Vous devriez maintenant être en mesure de vous connecter à Braze à l'aide d'Okta !

!Identifiant du tableau de bord de Braze avec Okta SSO activé.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}

