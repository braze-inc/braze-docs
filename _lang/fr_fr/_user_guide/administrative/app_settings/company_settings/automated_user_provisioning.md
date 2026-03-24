---
nav_title: Provisionnement automatisé des utilisateurs
article_title: Provisionnement automatisé des utilisateurs
page_order: 10
page_type: reference
description: "Cet article de référence décrit les informations que vous devez fournir pour le provisionnement automatisé des utilisateurs et explique comment et où utiliser le jeton SCIM (System for Cross-domain Identity Management) que vous avez généré."
alias: /scim/automated_user_provisioning/

---

# Provisionnement automatisé des utilisateurs

> Utilisez le provisionnement SCIM pour créer et gérer automatiquement les utilisateurs de Braze via l'API. Cet article vous explique quelles informations fournir, comment générer votre jeton SCIM et où trouver votre endpoint API SCIM.

{% multi_lang_include early_access_beta_alert.md feature='SCIM provisioning' %}

## Accès aux paramètres de provisionnement SCIM

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Paramètres** > **Paramètres d'administration** > **Provisionnement SCIM**, puis sélectionner **Configurer l'intégration SCIM**.
2. Dans l'étape **de configuration de Braze**, veuillez sélectionner une méthode de provisionnement et fournir les paramètres d'accès.

![Une page permettant de configurer l'intégration SCIM, avec des sections pour sélectionner une méthode de provisionnement et fournir des paramètres d'accès.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Au cours de l'étape **de configuration de l'IdP**, veuillez suivre les étapes indiquées dans la plateforme pour la méthode de provisionnement que vous avez sélectionnée.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Veuillez utiliser l'option **Okta - Braze app** si vous avez configuré l'application Braze pour l'authentification unique (SSO) SAML dans Okta. Si vous configurez une application personnalisée pour l'authentification unique (SSO), veuillez suivre les instructions fournies dans l'onglet [Okta - Intégration d'une application personnalisée]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning).

## Étape 1 : Configurer l'approvisionnement SCIM

### Étape 1.1 : Activer le SCIM

1. Dans Okta, veuillez vous rendre dans **Applications** > **Applications**, puis sélectionner **Créer une intégration d'application**. Veuillez sélectionner **SAML 2.0** comme méthode de connexion.
2. Veuillez remplir les informations suivantes (qui se trouvent dans l'[étape **de configuration**](#accessing-scim-provisioning-settings) Braze [**IdP**](#accessing-scim-provisioning-settings)) pour créer une application personnalisée :
- Logo de l'application
- URL d'authentification unique
- URL de l'audience (ID de l'entité SP)
3. Sélectionnez **Terminer**.
4. Veuillez sélectionner l'onglet **Général**. 
5. Dans la section **Paramètres de l'application**, veuillez sélectionner **Modifier**.
6. Dans le champ **Provisioning**, veuillez sélectionner **SCIM**. 

### Étape 1.2 : Désactiver la visibilité de l'application

1. Dans le champ **Visibilité de l'application**, veuillez cocher la case **Ne pas afficher l'icône de l'application à l'utilisateur**. Cela empêche les utilisateurs d'accéder à l'authentification unique (SSO) via l'application, qui est exclusivement destinée à SCIM. 
2. Sélectionnez **Enregistrer**.

### Étape 1.3 : Configurer l'intégration SCIM

1. Veuillez sélectionner l'onglet **Provisioning**.
2. Dans **Paramètres** > **Intégration** > **Connexion SCIM,** veuillez sélectionner **Modifier** et remplir les champs qui apparaissent dans le tableau de la page **Configuration du provisionnement SCIM**.

### Étape 1.4 : Tester les informations d'identification de l'API

Veuillez sélectionner **les informations d'identification de l'API de test**. Un message de vérification s'affiche si l'intégration est réussie et vous pouvez enregistrer.

### Étape 1.5 : Activer l'approvisionnement de l'application

1. Dans **Provisioning** > **Paramètres** > **Vers l'application** > **Provisioning vers l'application**, veuillez sélectionner **Modifier**.
2. Activez les éléments suivants :
    - Créer des utilisateurs
    - Mettre à jour les attributs des utilisateurs
    - Désactiver des utilisateurs
3. Veuillez examiner et configurer la section **Mappage des attributs** avec les mappages qui apparaissent dans le tableau de la page **de configuration du provisionnement SCIM**.

## Étape 2 : Veuillez attribuer des utilisateurs à l'application.

1. Veuillez sélectionner l'onglet **« Affectation** ».
2. Veuillez sélectionner **« Assigner** » et choisir une option.
3. Veuillez attribuer l'application aux personnes qui devraient avoir accès à Braze.
4. Veuillez sélectionner **Terminé** lorsque vous avez achevé la tâche.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Veuillez utiliser l'option **d'intégration d'application personnalisée Okta** si vous configurez une application personnalisée pour l'authentification unique (SSO). Si vous configurez l'application Braze pour l'authentification unique (SSO) SAML dans Okta, veuillez suivre les instructions fournies dans l'onglet [Okta - Application Braze]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning).

## Étape 1 : Configurer l'approvisionnement SCIM

### Étape 1.1 : Activer le SCIM

1. Dans Okta, veuillez accéder à votre application Braze.
2. Veuillez sélectionner l'onglet **Général**.
3. Dans la section **Paramètres de l'application**, veuillez sélectionner **Modifier**.
4. Dans le champ **Provisioning**, veuillez sélectionner **SCIM**.
5. Sélectionnez **Enregistrer**.

### Étape 1.2 : Configurer l'intégration SCIM

1. Veuillez sélectionner l'onglet **Provisioning**.
2. Dans **Paramètres** > **Intégration** > **Connexion SCIM**, veuillez sélectionner **Modifier** et remplir les champs qui apparaissent dans le tableau de la page **Configuration du provisionnement SCIM**.
3. Veuillez tester les informations d'identification de l'API en sélectionnant **« Tester les informations d'identification de l'API** ».
4. Sélectionnez **Enregistrer**.

### Étape 1.3 : Activer l'approvisionnement de l'application

1. Dans **Provisioning** > **Paramètres** > **Vers l'application** > **Provisioning vers l'application**, veuillez sélectionner **Modifier**.
2. Activez les éléments suivants :
    - Créer des utilisateurs
    - Mettre à jour les attributs des utilisateurs
    - Désactiver des utilisateurs
3. Veuillez examiner et configurer la section **Mappage des attributs** avec les mappages qui apparaissent dans le tableau de la page **de configuration du provisionnement SCIM**.

## Étape 2 : Veuillez attribuer des utilisateurs à l'application.

1. Veuillez sélectionner l'onglet **« Affectation** ».
2. Veuillez sélectionner **« Assigner** » et choisir une option.
3. Veuillez attribuer l'application aux personnes qui devraient avoir accès à Braze.
4. Veuillez sélectionner **Terminé**.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include early_access_beta_alert.md feature='The Entra ID integration' %}

## Étape 1 : Configurer l'application de provisionnement SCIM

### Étape 1.1 : Veuillez vous connecter au centre d'administration Microsoft Entra.

Veuillez vous connecter à votre centre d'administration Microsoft Entra.

### Étape 1.2 : Veuillez créer et configurer votre application SCIM.

1. Dans le menu de navigation, veuillez vous rendre dans **Entra ID** > **Applications d'entreprise**.
2. Veuillez sélectionner **Nouvelle demande**.
3. Veuillez sélectionner **« Créer votre propre application** ».
4. Dans le panneau, veuillez saisir un nom pour votre application.
5. Dans la section **« Que souhaitez-vous faire avec votre application ? »**, veuillez sélectionner **« Intégrer une application qui ne figure pas dans la galerie (Hors galerie)** ».
6. Sélectionnez **Créer**.

### Étape 1.3 : Configurer l'intégration SCIM

1. Veuillez vous rendre dans la section **Gestionnaire** > **Provisionnement** de votre application SCIM.
2. Veuillez sélectionner **« Connecter votre application** » ou **« Nouvelle configuration** » et remplir les champs qui apparaissent dans le tableau de la page **« Configuration du provisionnement SCIM** ».

### Étape 1.4 : Activer l'approvisionnement de l'application

1. Veuillez vous rendre dans la section **Gestionnaire** > **Mappage des attributs (Aperçu)** de votre application SCIM.
2. Veuillez sélectionner **la provision des utilisateurs Microsoft Entra ID**.
3. Veuillez examiner et configurer la section **Mappage des attributs** afin de faire correspondre les attributs qui apparaissent dans le tableau de la page **de configuration du provisionnement SCIM**.
4. Veuillez fermer la page **Mappage des attributs**.

## Étape 2 : Veuillez attribuer des utilisateurs à l'application.

1. Veuillez vous rendre dans **la section de gestion** > **Utilisateurs et groupes**.
2. Veuillez sélectionner **Ajouter un utilisateur/groupe**.
3. Veuillez sélectionner **Aucun utilisateur sélectionné** pour attribuer des utilisateurs à l'application.
4. Veuillez cliquer sur le bouton **Sélectionner** pour confirmer l'attribution.

{% endtab %}
{% tab Custom %}

## Étape 1 : Configurez vos paramètres SCIM

- **Espace de travail par défaut :** Veuillez sélectionner l'espace de travail où les nouveaux utilisateurs doivent être ajoutés par défaut. Si vous ne spécifiez pas d'espace de travail dans votre [demande d'API SCIM]({{site.baseurl}}/post_create_user_account/), Braze affecte les utilisateurs à cet espace de travail.
- **Origine du service :** Saisissez le domaine d'origine de vos demandes SCIM. Braze l'utilise dans l'en-tête `X-Request-Origin` pour vérifier l'origine des demandes.
- **IP Allowlisting (optionnel) :** Vous pouvez limiter les requêtes SCIM à des adresses IP spécifiques. Saisissez une liste ou une plage d'adresses IP à autoriser, séparées par des virgules. L'en-tête`X-Request-Origin` de chaque requête est utilisé pour vérifier l'adresse IP de la requête par rapport à la liste blanche.

![Formulaire de paramétrage du provisionnement du SCIM avec trois champs : Espace de travail par défaut, origine du service et liste blanche IP facultative. Le bouton « Générer un jeton SCIM » est désactivé.]({% image_buster /assets/img/scim_unfilled.png %})

## Étape 2 : Générer un jeton SCIM

Après avoir rempli les champs obligatoires, appuyez sur **Generate SCIM token** pour générer un jeton SCIM et voir votre endpoint API SCIM. Veillez à copier le jeton SCIM avant de naviguer. **Ce jeton n'apparaît qu'une seule fois.** 

![Champs SCIM API Endpoint et SCIM Token affichés avec des valeurs masquées et des boutons de copie. Sous le champ du jeton se trouve un bouton « Réinitialiser le jeton ».]({% image_buster /assets/img/scim.png %})

Braze attend de toutes les requêtes SCIM qu’elles contiennent le jeton de porteur de l’API SCIM joint via un en-tête `Authorization` HTTP.

{% endtab %}
{% endtabs %}
