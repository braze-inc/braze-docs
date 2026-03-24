---
nav_title: Provisionnement SAML juste à temps
article_title: Approvisionnement SAML Just-in-Time
page_order: 1
page_type: tutorial
description: "Cet article vous guidera dans la configuration du provisionnement SAML juste à temps afin de permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion." 

---

# Approvisionnement SAML juste-à-temps 

> L'approvisionnement juste à temps fonctionne avec [l'authentification unique (SSO) SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) pour permettre aux nouveaux utilisateurs de l'entreprise de créer un compte Braze lors de leur première connexion. Cela évite aux administrateurs de devoir créer manuellement un compte pour un nouvel utilisateur de l'entreprise, de choisir ses autorisations, de l'affecter à un espace de travail et d'attendre qu'il active son compte.

Par mesure de sécurité, l'approvisionnement SAML juste à temps (JITP) ne fonctionne que pour les utilisateurs dont les domaines de e-mail existent déjà dans votre entreprise. Le JITP n'est possible que pour les domaines où il existe déjà au moins un développeur confirmé et non usurpateur au sein de l'entreprise. 

Par exemple, supposons que le compte```jon.smith@decorumsoft.com```puisse utiliser JITP pour se connecter à Decorumsoft. Le compte```jane.smith@decorumsoft.com```partage le même domaine et peut également être autorisé à effectuer des provisionnements. Cependant, si vous essayez d'utiliser JITP avec ```jon.smith@decorumsoft.eu```, l'approvisionnement ne sera pas autorisé car il n'existe pas de```decorumsoft.eu```compte dans le tableau de bord de Braze. 

Pour faire une exception pour une entreprise, veuillez contacter [le service d'assistance]({{site.baseurl}}/braze_support/).

## Conditions préalables

SAML JITP nécessite que l’authentification unique (SSO) SAML soit configurée et intégrée. Il n'est pas compatible avec Google SSO et n'est pris en charge que pour les workflows d'identification initiés par le fournisseur d'identité (IdP).

## Configuration du provisionnement SAML juste à temps (JITP)

Demandez à un administrateur Braze de faire ce qui suit :

1. Veuillez vous rendre dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité**.
2. Dans la section **SAML SSO**, activez l'option **Approvisionnement automatique des utilisateurs**.
3. Veuillez sélectionner un espace de travail par défaut pour ajouter un nouvel utilisateur de l'entreprise.
4. Veuillez sélectionner l'ensemble d'autorisations par défaut à attribuer à ce nouvel utilisateur de l'entreprise. Pour savoir comment créer un ensemble d'autorisations, consultez [Définition des autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Sélectionnez **Enregistrer les modifications** en bas de la page
7. Dans les paramètres de votre fournisseur SSO, ajoutez tous les utilisateurs qui ont besoin d'accéder à Braze dans le répertoire de votre fournisseur SSO.
8. Veuillez informer les utilisateurs qu'ils doivent accéder à Braze via votre portail IdP lors de leur premier identifiant. Par la suite, le bouton d'authentification unique SAML s'affichera pour les prochaines connexions.

## Foire aux questions

### Comment puis-je désactiver SAML JITP ?

Après avoir configuré JITP, il est nécessaire de [contacter le service d'assistance]({{site.baseurl}}/braze_support/) pour le désactiver.

## Résolution des problèmes

### Le bouton de connexion unique n'apparaît pas avec Microsoft Entra ID

Le champ **URL de connexion** dans le formulaire **de configuration SAML de base** de Microsoft Entra pour Braze peut entraîner que les utilisateurs ne voient qu'une option de mot de passe, et non un bouton d'authentification unique (SSO), lors de l'identifiant initié par l'IdP. Pour éviter ce problème, veuillez laisser le champ **URL de connexion** vide lorsque vous configurez Braze dans votre centre d'administration Microsoft Entra.