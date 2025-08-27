---
nav_title: Approvisionnement SAML Just-in-Time
article_title: Approvisionnement SAML Just-in-Time
page_order: 1
page_type: tutorial
description: "Cet article vous expliquera comment configurer le provisionnement SAML juste-à-temps pour permettre aux nouveaux utilisateurs du tableau de bord de créer un compte Braze lors de leur première connexion." 

---

# Approvisionnement SAML juste-à-temps 

> L'approvisionnement juste-à-temps fonctionne avec [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) pour permettre aux nouveaux utilisateurs du tableau de bord de créer un compte Braze lors de leur première connexion. Cela élimine le besoin pour les administrateurs de créer manuellement un compte pour un nouvel utilisateur de tableau de bord, de choisir leurs autorisations, de les affecter à un espace de travail et d'attendre qu'ils activent leur compte.

## Conditions préalables

Cette fonctionnalité nécessite que l’authentification unique (SSO) SAML soit configurée et intégrée, et n'est pas compatible avec l’authentification unique de Google.

## Configuration du provisionnement juste-à-temps SAML

Demandez à un administrateur Braze de faire ce qui suit :

1. Accédez à **Paramètres** > **Paramètres de sécurité**.
2. Dans la section **SAML SSO**, activez l'option **Approvisionnement automatique des utilisateurs**.
3. Sélectionnez un espace de travail par défaut pour ajouter un nouvel utilisateur de tableau de bord.
4. Sélectionnez l'ensemble d'autorisations par défaut à attribuer à ce nouvel utilisateur du tableau de bord. Pour savoir comment créer un ensemble d'autorisations, consultez [Définition des autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/).
6. Sélectionnez **Enregistrer les modifications** en bas de la page
7. Dans les paramètres de votre fournisseur SSO, ajoutez tous les utilisateurs qui ont besoin d'accéder à Braze dans le répertoire de votre fournisseur SSO.
8. Maintenant, les utilisateurs peuvent s'inscrire ou se connecter.
