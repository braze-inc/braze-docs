---
nav_title: Provisionnement automatisé des utilisateurs
article_title: Provisionnement automatisé des utilisateurs
page_order: 10
page_type: reference
description: "Cet article de référence décrit les informations que vous devez fournir pour le provisionnement automatisé des utilisateurs et explique comment et où utiliser le jeton SCIM (System for Cross-domain Identity Management) que vous avez généré."
alias: /scim/automated_user_provisioning/

---

# Provisionnement automatisé des utilisateurs

> Découvrez ce que vous devez fournir pour le provisionnement automatisé des utilisateurs et comment et où utiliser votre jeton SCIM (System for Cross-domain Identity Management) généré et l'endpoint de l'API SCIM. Vous pouvez ensuite appeler cet endpoint avec votre API pour approvisionner automatiquement les nouveaux utilisateurs du tableau de bord.

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres d'administration** > **Provisionnement SCIM.**

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), sélectionnez le menu déroulant de votre compte et allez dans **Paramètres de l'entreprise** > **Provisionnement automatisé des utilisateurs**.
{% endalert %}

## Comment obtenir votre jeton SCIM ?

Vous devrez fournir les informations suivantes pour obtenir votre jeton SCIM :

1. Sélectionnez un espace de travail par défaut auquel seront ajoutés les nouveaux développeurs de tableaux de bord. Si vous ne spécifiez pas d'espace de travail dans l'[appel API SCIM de création d'utilisateurs](/docs/post_create_user_account/), ils seront ajoutés ici.
2. Fournir une origine de service. L’origine du service est la façon dont Braze identifie l’origine de la demande.
3. Vous pouvez éventuellement fournir une liste séparée par des virgules ou une plage d’adresses IP autorisées pour les demandes SCIM. Les en-têtes `X-Origin-Request` dans chaque demande seront utilisés pour vérifier l’adresse IP par rapport à la liste des autorisations.<br><br>

{% alert note %}
Cet endpoint SCIM ne s'intègre pas directement aux fournisseurs d'identité.
{% endalert %}

![][1]

Après avoir rempli les champs obligatoires, vous pouvez générer un jeton SCIM et voir votre endpoint API SCIM. **Ce jeton ne sera présenté qu'une seule fois.** Braze attend de toutes les requêtes SCIM qu’elles contiennent le jeton de porteur de l’API SCIM joint via un en-tête `Authorization` HTTP.

[1]: {% image_buster /assets/img/scim.png %}
