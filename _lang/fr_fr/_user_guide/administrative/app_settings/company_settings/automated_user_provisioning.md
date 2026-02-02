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

## Accès aux paramètres de provisionnement du SCIM

1. Dans le tableau de bord de Braze, accédez à **Paramètres** > **Paramètres d'administration** > **Provisionnement SCIM** et ajoutez un fournisseur d'identité.
2. Dans l'étape de **provisionnement de Braze**, sélectionnez une méthode de provisionnement et fournissez les paramètres d'accès.

![Une page pour configurer l'intégration SCIM avec des sections pour sélectionner une méthode d'approvisionnement et fournir des paramètres d'accès.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Dans l'étape de **configuration de l'IdP**, suivez les étapes de la plateforme pour la méthode de provisionnement que vous avez choisie.

{% tabs %}
{% tab Okta - Braze app %}

{% alert important %}
L'intégration d'Okta est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Étape 1 : Configurer le provisionnement du SCIM

### Étape 1.1 : Activer le SCIM

1. Accédez à votre application Braze dans Okta.
2. Sélectionnez l'onglet **Général**.
3. Dans la section **Paramètres de l'application**, sélectionnez **Modifier**.
4. Dans le champ **Provisionnement**, sélectionnez **SCIM**, puis cliquez sur **Enregistrer.**

### Étape 1.2 : Mise en place de l'intégration du SCIM

1. Sélectionnez l'onglet **Provisionnement**.
2. Dans **Configuration** > **Intégration** > **Connexion SCIM**, sélectionnez **Modifier** et renseignez les valeurs des champs qui s'affichent dans le tableau de la page de **configuration du provisionnement SCIM**.

### Étape 1.3 : Tester les informations d'identification de l'API

Sélectionnez **Test API Credentials**. Un message de vérification apparaît si l'intégration est réussie et vous pouvez enregistrer.

### Étape 1.4 : Activer le provisionnement de l'application

1. Dans **Provisioning** > **Settings** > **To App** > **Provisioning to App**, sélectionnez **Modifier**.
2. Activez les éléments suivants :
    - Créer des utilisateurs
    - Mettre à jour les attributs des utilisateurs
    - Désactiver des utilisateurs
3. Passez en revue et configurez la section **Attribute Mapping (mappage d'attributs** ) avec les mappages qui apparaissent dans le tableau de la page **Setup SCIM provisioning (Configuration du SCIM** ).

## Étape 2 : Affecter des utilisateurs à l'application

1. Sélectionnez l'onglet **Affectation**.
2. Sélectionnez **Attribuer** et choisissez une option.
3. Attribuez l'application aux personnes qui doivent avoir accès à Braze.
4. Sélectionnez **Terminé** lorsque vous avez terminé le travail.

{% endtab %}
{% tab Okta - Custom app integration %}

{% alert important %}
L'intégration d'Okta est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Étape 1 : Configurer le provisionnement du SCIM

### Étape 1.1 : Activer le SCIM

1. Dans Okta, accédez à votre application Braze.
2. Sélectionnez l'onglet **Général**.
3. Dans la section **Paramètres de l'application**, sélectionnez **Modifier**.
4. Dans le champ **Provisionnement**, sélectionnez **SCIM**.
5. Sélectionnez **Enregistrer**.

### Étape 1.2 : Mise en place de l'intégration du SCIM

1. Sélectionnez l'onglet **Provisionnement**.
2. Dans **Configuration** > **Intégration** > **Connexion SCIM**, sélectionnez **Modifier** et renseignez les valeurs des champs qui s'affichent dans le tableau de la page de **configuration du provisionnement SCIM**.
3. Testez les informations d'identification de l'API en sélectionnant **Tester les informations d'identification de l'API**.
4. Sélectionnez **Enregistrer**.

### Étape 1.3 : Activer le provisionnement de l'application

1. Dans **Provisioning** > **Settings** > **To App** > **Provisioning to App**, sélectionnez **Modifier**.
2. Activez les éléments suivants :
    - Créer des utilisateurs
    - Mettre à jour les attributs des utilisateurs
    - Désactiver des utilisateurs
3. Passez en revue et configurez la section **Attribute Mapping (mappage d'attributs** ) avec les mappages qui apparaissent dans le tableau de la page **Setup SCIM provisioning (Configuration du SCIM** ).

## Étape 2 : Affecter des utilisateurs à l'application

1. Sélectionnez l'onglet **Affectation**.
2. Sélectionnez **Attribuer** et choisissez une option.
3. Attribuez l'app aux personnes qui doivent avoir accès à Braze.
4. Sélectionnez **Terminé**.

{% endtab %}
{% tab Entra ID %}

{% alert important %}
L'intégration d'Entra ID est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Étape 1 : Configurer l'application de provisionnement SCIM

### Étape 1.1. Connectez-vous au centre d'administration de Microsoft Entra
Connectez-vous à votre centre d'administration Microsoft Entra.

### Étape 1.2 : Créez et configurez votre application SCIM

1. Dans le menu de navigation, allez à **Entra ID** > **Enterprise apps**.
2. Sélectionnez **Nouvelle application**.
3. Sélectionnez **Créer votre propre application**.
4. Dans le panneau, saisissez un nom pour votre application.
5. Dans la section **Que cherchez-vous à faire avec votre application ?**, sélectionnez **Intégrer une application que vous ne trouvez pas dans la galerie (Non-gallery)**.
6. Sélectionnez **Créer**.

### Étape 1.3 : Mise en place de l'intégration du SCIM

1. Allez dans la section **Gestion** > **Provisionnement de** votre application SCIM.
2. Sélectionnez **Connecter votre application** ou **Nouvelle configuration** et renseignez les valeurs des champs qui s'affichent dans le tableau de la page de **configuration du SCIM**.

### Étape 1.4 : Activer le provisionnement de l'application

1. Allez dans la section **Gestion** > **Mappage d'attributs (Aperçu)** de votre application SCIM.
2. Sélectionnez **Provisionner les utilisateurs Microsoft Entra ID.**
3. Passez en revue et configurez la section **Mappage d'attributs** pour qu'elle corresponde aux attributs qui apparaissent dans le tableau de la page de **configuration du SCIM**.
4. Fermez la page de **mappage d'attributs**.

## Étape 2 : Affecter des utilisateurs à l'application

1. Allez dans **Gestion** > **Utilisateurs et groupes**.
2. Sélectionnez **Ajouter un utilisateur/groupe**.
3. Sélectionnez **Aucune sélection** pour affecter des utilisateurs à l'application.
4. Appuyez sur le bouton **Select** pour confirmer l'affectation.

{% endtab %}
{% tab Custom %}

## Étape 1 : Configurez vos paramètres SCIM

- **Espace de travail par défaut :** Sélectionnez l'espace de travail dans lequel les nouveaux utilisateurs doivent être ajoutés par défaut. Si vous ne spécifiez pas d'espace de travail dans votre [demande d'API SCIM]({{site.baseurl}}/post_create_user_account/), Braze affecte les utilisateurs à cet espace de travail.
- **Origine du service :** Saisissez le domaine d'origine de vos demandes SCIM. Braze l'utilise dans l'en-tête `X-Request-Origin` pour vérifier l'origine des demandes.
- **IP Allowlisting (optionnel) :** Vous pouvez limiter les requêtes SCIM à des adresses IP spécifiques. Saisissez une liste ou une plage d'adresses IP à autoriser, séparées par des virgules. L'en-tête `X-Request-Origin` de chaque requête est utilisé pour vérifier l'adresse IP de la requête par rapport à la liste d'autorisation.

![Formulaire de paramétrage du provisionnement du SCIM avec trois champs : Espace de travail par défaut, Origine du service, et liste d'autorisations IP en option. Le bouton "Générer un jeton SCIM" est désactivé.]({% image_buster /assets/img/scim_unfilled.png %})

## Étape 2 : Générer un jeton SCIM

Après avoir rempli les champs obligatoires, appuyez sur **Generate SCIM token** pour générer un jeton SCIM et voir votre endpoint API SCIM. Veillez à copier le jeton SCIM avant de naviguer. **Ce jeton n'apparaît qu'une seule fois.** 

![Champs SCIM API Endpoint et SCIM Token affichés avec des valeurs masquées et des boutons de copie. Sous le champ du jeton se trouve un bouton "Réinitialiser le jeton".]({% image_buster /assets/img/scim.png %})

Braze attend de toutes les requêtes SCIM qu’elles contiennent le jeton de porteur de l’API SCIM joint via un en-tête `Authorization` HTTP.

{% endtab %}
{% endtabs %}
