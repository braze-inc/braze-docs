---
nav_title: Provisionnement automatisé des utilisateurs
article_title: Provisionnement automatisé des utilisateurs
page_order: 10
page_type: reference
description: "Cet article de référence couvre les informations que vous devez fournir pour le provisionnement automatisé des utilisateurs, la façon dont et quand utiliser votre jeton SCIM généré."
alias: /scim/automated_user_provisioning/

---

# Provisionnement automatisé des utilisateurs

> Pour configurer le provisionnement automatisé des utilisateurs, rendez-vous sur **Company Settings** (Paramètres de l’entreprise) dans le tableau de bord en déployant les options trouvées en cliquant sur votre nom d’utilisateur. De là, allez à **Automated User Provisioning** (Provisionnement automatisé des utilisateurs) pour commencer la configuration. 

Vous devrez fournir les informations suivantes pour obtenir votre jeton SCIM :
1. Sélectionnez un groupe d’apps par défaut pour les nouveaux développeurs de tableaux de bord à ajouter. Si vous ne spécifiez pas un groupe d’apps dans [créer un appel API SCIM utilisateurs](/docs/post_create_user_account/), elles seront ajoutées ici.<br><br>
2. Fournir une origine de service. L’origine du service est la façon dont Braze identifie l’origine de la demande. <br><br>
3. Vous pouvez éventuellement fournir une liste séparée par des virgules ou une plage d’adresses IP autorisées pour les demandes SCIM. Les en-têtes `X-Origin-Request` dans chaque demande seront utilisés pour vérifier l’adresse IP par rapport à la liste des autorisations. 

![][1]

Une fois les champs requis remplis, vous pouvez générer un jeton SCIM et voir votre endpoint API SCIM. **Ce jeton ne sera présenté qu’une seule fois.** Braze attend de toutes les requêtes SCIM qu’elles contiennent le jeton de porteur de l’API SCIM joint via un en-tête `Authorization` HTTP.

[1]: {% image_buster /assets/img/scim.png %}
