---
nav_title: SAML Just-in-Time provisioning
article_title: Approvisionnement SAML Just-in-Time
page_order: 1
page_type: tutorial
description: "Cet article vous explique comment configurer le provisionnement SAML juste à temps pour permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion." 

---

# Approvisionnement SAML juste-à-temps 

> Le provisionnement juste à temps fonctionne avec l'[authentification SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) pour permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion. Les administrateurs n'ont donc plus besoin de créer manuellement un compte pour un nouvel utilisateur de l'entreprise, de choisir ses autorisations, de l'affecter à un espace de travail et d'attendre qu'il active son compte.

Par mesure de sécurité, le provisionnement SAML juste à temps (JITP) ne fonctionne que pour les utilisateurs dont les domaines d'e-mail existent déjà dans votre entreprise. La JITP n'est possible que pour les domaines où il y a déjà au moins un développeur confirmé, sans usurpation d'identité, dans l'entreprise. 

Par exemple, disons que le compte ```jon.smith@decorumsoft.com``` peut utiliser JITP pour se connecter à Decorumsoft. Le compte ```jane.smith@decorumsoft.com``` a le même domaine et peut également être autorisé à provisionner. Cependant, si vous essayez d'utiliser JITP avec ```jon.smith@decorumsoft.eu```, le provisionnement ne sera pas autorisé parce qu'il n'y a pas de compte ```decorumsoft.eu``` dans le tableau de bord de Braze de Decorumsoft. 

Pour faire une exception pour une entreprise, contactez le [service d'assistance.]({{site.baseurl}}/braze_support/)

## Conditions préalables

SAML JITP exige que l'authentification unique (SSO) SAML soit mise en place et intégrée. Il n'est pas compatible avec Google SSO et n'est pris en charge que pour les flux d'identifiants initiés par le fournisseur d'identité (IdP-initiated).

## Mise en place de SAML just-in-time provisioning (JITP)

Demandez à un administrateur Braze de faire ce qui suit :

1. Naviguez vers **Paramètres** > **Paramètres administratifs** > **Paramètres de sécurité**.
2. Dans la section **SAML SSO**, activez l'option **Approvisionnement automatique des utilisateurs**.
3. Sélectionnez un espace de travail par défaut pour ajouter un nouvel utilisateur de l'entreprise.
4. Sélectionnez le jeu de permissions par défaut à attribuer à ce nouvel utilisateur de l'entreprise. Pour savoir comment créer un ensemble d'autorisations, consultez [Définition des autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Sélectionnez **Enregistrer les modifications** en bas de la page
7. Dans les paramètres de votre fournisseur SSO, ajoutez tous les utilisateurs qui ont besoin d'accéder à Braze dans le répertoire de votre fournisseur SSO.
8. Demandez aux utilisateurs d'accéder à Braze via votre portail IdP pour leur premier identifiant. Ensuite, le bouton d'authentification unique SAML s'affiche pour les identifiants ultérieurs.

## Foire aux questions

### Comment désactiver SAML JITP ?

Après avoir configuré le système JITP, vous devez [contacter le service d'assistance]({{site.baseurl}}/braze_support/) pour le désactiver.

## Résolution des problèmes

### Le bouton de signature unique n'apparaît pas avec Microsoft Entra ID

Le champ **Sign-On URL** dans le formulaire **Basic SAML Configuration de** Microsoft Entra pour Braze peut faire en sorte que les utilisateurs ne voient qu'une option de mot de passe, et non un bouton SSO, lors d'un identifiant initié par l'IdP. Pour éviter ce problème, laissez le champ **Sign-On URL** vide lors de la configuration de Braze dans votre centre d'administration Microsoft Entra.