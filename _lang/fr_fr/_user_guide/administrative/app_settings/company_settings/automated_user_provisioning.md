---
nav_title: Approvisionnement automatisé des utilisateurs
article_title: Approvisionnement automatisé des utilisateurs
page_order: 10
page_type: reference
description: "Cet article de référence décrit les informations que vous devez fournir pour le provisionnement automatisé des utilisateurs et explique comment et où utiliser le jeton SCIM (System for Cross-domain Identity Management) que vous avez généré."
alias: /scim/automated_user_provisioning/

---

# Approvisionnement automatisé des utilisateurs

> Utilisez le provisionnement SCIM pour créer et gérer automatiquement les utilisateurs de Braze via l'API. Cet article vous explique quelles informations fournir, comment générer votre jeton SCIM et où trouver votre endpoint API SCIM.

## Étape 1 : Accéder aux paramètres de privioning du SCIM

Dans le tableau de bord de Braze, accédez à **Paramètres** > **Paramètres d'administration** > **Provisionnement SCIM**.

## Étape 2 : Configurez vos paramètres SCIM

Pour activer le provisionnement du SCIM, fournissez les informations suivantes :

- **Espace de travail par défaut :** Sélectionnez l'espace de travail dans lequel les nouveaux utilisateurs seront ajoutés par défaut. Si vous ne spécifiez pas d'espace de travail dans votre [demande d'API SCIM]({{site.baseurl}}/post_create_user_account/), Braze affecte les utilisateurs à cet espace de travail.
- **Origine du service :** Saisissez le domaine d'origine de vos demandes SCIM. Braze l'utilise dans l'en-tête `X-Request-Origin` pour vérifier l'origine des demandes.
- **IP Allowlisting (optionnel) :** Vous pouvez limiter les requêtes SCIM à des adresses IP spécifiques.
Saisissez une liste ou une plage d'adresses IP à autoriser, séparées par des virgules. L'en-tête `X-Request-Origin` de chaque requête sera utilisé pour vérifier l'adresse IP de la requête par rapport à la liste d'autorisation.

{% alert note %}
Cet endpoint SCIM ne s'intègre pas directement aux fournisseurs d'identité.
{% endalert %}

\![Formulaire de paramétrage du provisionnement du SCIM avec trois champs : Espace de travail par défaut, Origine du service, et liste d'autorisations IP en option. Le bouton "Générer un jeton SCIM" est désactivé.]({% image_buster /assets/img/scim_unfilled.png %})

## Étape 3 : Obtenez votre jeton SCIM et votre endpoint

Après avoir rempli les champs obligatoires, appuyez sur **Generate SCIM token** pour générer un jeton SCIM et voir votre endpoint API SCIM. Veillez à copier le jeton SCIM avant de naviguer. **Ce jeton ne sera présenté qu'une seule fois.** 

Les champs "SCIM API Endpoint" et "SCIM Token" sont affichés avec des valeurs masquées et des boutons de copie. Sous le champ du jeton se trouve un bouton "Réinitialiser le jeton".]({% image_buster /assets/img/scim.png %})

Braze s'attend à ce que toutes les demandes SCIM contiennent le jeton de l'API SCIM attaché via un en-tête HTTP `Authorization`.

