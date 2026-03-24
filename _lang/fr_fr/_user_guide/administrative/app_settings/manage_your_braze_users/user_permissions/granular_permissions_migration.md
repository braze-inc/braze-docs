---
nav_title: Migration des autorisations granulaires
article_title: Migration vers des autorisations granulaires
page_order: 3
page_type: reference
alias: /granular_permissions_migration/
description: "Cet article de référence explique comment se préparer à la migration vers les autorisations utilisateur granulaires dans Braze."
tool: Dashboard
---

# Migration vers des autorisations granulaires

> Contrôler qui peut accéder à votre compte et effectuer des actions spécifiques est essentiel, tant pour la sécurité que pour l'efficacité opérationnelle. Afin de vous offrir davantage de contrôle, Braze met en place des autorisations granulaires : une méthode plus flexible et plus précise pour gérer l'accès des utilisateurs à votre compte.

La migration offre les avantages suivants :

- **Contrôle plus précis :** Les autorisations granulaires offrent un contrôle accru, une sécurité renforcée et une supervision plus claire. Les utilisateurs n'obtiennent que l'accès dont ils ont besoin.
- **Mappage automatique :** Toutes les autorisations actuelles font l'objet d'un mappage automatique vers leurs [équivalents granulaires](#legacy-to-granular-permissions-mapping). Vos utilisateurs conservent le même niveau d'accès, sauf si vous le modifiez.

## Ce qu'il faut vérifier

Lorsque la migration est planifiée pour votre entreprise, vos administrateurs Braze recevront des e-mails et des bannières sur le tableau de bord les informant de la migration des autorisations granulaires. Pour préparer la migration, nous recommandons qu'un administrateur Braze procède comme suit.

1. Identifiez les utilisateurs, les rôles ou les ensembles d'autorisations qui pourraient nécessiter une mise à jour afin d'offrir un accès plus adapté après la migration vers le nouveau cadre d'autorisations. 
2. Si votre entreprise a automatisé le provisionnement des utilisateurs à l'aide de SCIM ou d'outils de conformité qui s'appuient sur des [chaînes de caractères d'autorisation]({{site.baseurl}}/scim_api_appendix/), mettez-les à jour pour qu'ils correspondent à la nouvelle structure granulaire. 
3. Informez vos utilisateurs Braze de tout changement à venir afin d'éviter toute confusion.
4. À la date et à l'heure prévues pour la migration, votre entreprise passera automatiquement aux autorisations granulaires. Aucune autre action n'est requise de la part des administrateurs de l'entreprise.

{% alert important %}
La possibilité de mettre à jour les autorisations sera verrouillée dans les 15 minutes précédant l'heure prévue de la migration. Cela signifie que vous ne pourrez modifier aucune autorisation tant que la migration ne sera pas terminée, ce qui devrait prendre environ 15 minutes.
{% endalert %}

## Mappage des autorisations héritées vers les autorisations granulaires

Ce tableau présente le mappage entre chaque autorisation héritée et les autorisations granulaires correspondantes. Consultez-le lorsque vous mettez à jour vos autorisations. Par exemple, pour accorder à un utilisateur les mêmes droits d'accès que l'autorisation héritée « Gérer les paramètres d'e-mail », cet utilisateur doit disposer à la fois des autorisations granulaires « Afficher les paramètres d'e-mail » et « Modifier les paramètres d'e-mail ».

| | Autorisations héritées | Autorisations granulaires |
|---------------|---------------|---------------|
| **Niveau** | **Nom** | **Nom** |
| Admin | Admin | Admin |
| Espace de travail | Administrateur de l'espace de travail | Administrateur de l'espace de travail |
| Société | Créer et supprimer des espaces de travail | Créer et supprimer des espaces de travail |
| Société | Gérer les paramètres de la société | Gérer les paramètres de la société |
| Espace de travail | Accéder aux campagnes, Canvas, cartes, blocs de contenu, indicateurs de fonctionnalité, segments, bibliothèque multimédia, emplacements, codes de promotion et centres de préférences | Afficher les campagnes<br>Modifier les campagnes<br>Archiver les campagnes<br>Afficher les Canvas<br>Modifier les Canvas<br>Archiver les Canvas<br>Afficher les règles de limite de fréquence<br>Modifier les règles de limite de fréquence<br>Afficher l'ordre de priorité des messages<br>Modifier l'ordre de priorité des messages<br>Afficher les blocs de contenu<br>Afficher les indicateurs de fonctionnalité<br>Modifier les indicateurs de fonctionnalité<br>Archiver les indicateurs de fonctionnalité<br>Afficher les segments<br>Modifier les segments<br>Modifier le groupe de contrôle global<br>Afficher les modèles IAM<br>Modifier les modèles IAM<br>Archiver les modèles IAM<br>Afficher les modèles d'e-mail<br>Modifier les modèles d'e-mail<br>Archiver les modèles d'e-mail<br>Afficher les modèles de webhook<br>Modifier les modèles de webhook<br>Archiver les modèles de webhook<br>Afficher les modèles de lien e-mail<br>Modifier les modèles de lien e-mail<br>Afficher les ressources de la bibliothèque multimédia<br>Afficher les emplacements<br>Modifier les emplacements<br>Archiver les emplacements<br>Afficher les codes de promotion<br>Modifier les codes de promotion<br>Exporter les codes de promotion<br>Afficher les centres de préférences<br>Modifier les centres de préférences<br>Modifier les rapports<br>Afficher les modèles de bannières<br>Afficher les paramètres multilingues<br>Utiliser l'opérateur<br>Afficher les agents Decisioning Studio<br>Afficher l'événement de conversion Decisioning Studio |
| Espace de travail | Accéder à la console de développement | Afficher les clés API<br>Modifier les clés API<br>Afficher les groupes internes<br>Modifier les groupes internes<br>Supprimer les groupes internes<br>Afficher le journal d'activité des messages<br>Afficher le journal des événements utilisateurs<br>Afficher les identifiants de l'API<br>Afficher le tableau de bord d'utilisation de l'API<br>Afficher les limites de l'API<br>Afficher les alertes d'utilisation de l'API<br>Modifier les alertes d'utilisation de l'API<br>Afficher le débogueur SDK<br>Modifier le débogueur SDK |
| Espace de travail | Approuver et refuser des campagnes | Approuver les campagnes |
| Espace de travail | Approuver et refuser des Canvas | Approuver les Canvas |
| Espace de travail | Exporter les données utilisateur | Exporter les données utilisateur |
| Espace de travail | Importer et mettre à jour les données utilisateur | Afficher les importations d'utilisateurs<br>Importer des utilisateurs<br>Modifier les données utilisateur |
| Espace de travail | Modifier les segments | Archiver les segments |
| Espace de travail | Lancer et gérer les blocs de contenu | Modifier les blocs de contenu<br>Archiver les blocs de contenu<br>Lancer les blocs de contenu |
| Espace de travail | Gérer la bibliothèque multimédia | Modifier les ressources de la bibliothèque multimédia<br>Supprimer les ressources de la bibliothèque multimédia |
| Espace de travail | Lancer les centres de préférences | Lancer les centres de préférences |
| Espace de travail | Gérer les applications | Afficher les paramètres de l'application<br>Modifier les paramètres de l'application<br>Afficher les paramètres des notifications push<br>Modifier les paramètres des notifications push<br>Modifier les modèles de bannières<br>Archiver les modèles de bannières |
| Espace de travail | Gérer les autorisations du tableau de bord des catalogues | Afficher les catalogues<br>Modifier les catalogues<br>Exporter les catalogues<br>Supprimer les catalogues |
| Espace de travail | Gérer les utilisateurs du tableau de bord | Modifier les utilisateurs du tableau de bord |
| Espace de travail | Gérer les paramètres d'e-mail | Afficher les paramètres d'e-mail<br>Modifier les paramètres d'e-mail |
| Espace de travail | Gérer les événements, attributs et achats | Afficher les attributs personnalisés<br>Modifier les attributs personnalisés<br>Ajouter des attributs personnalisés à la liste de blocage<br>Supprimer les attributs personnalisés<br>Exporter les attributs personnalisés<br>Afficher les événements personnalisés<br>Modifier les événements personnalisés<br>Ajouter des événements personnalisés à la liste de blocage<br>Supprimer les événements personnalisés<br>Exporter les événements personnalisés<br>Modifier la segmentation des propriétés d'événements personnalisés<br>Afficher les produits<br>Modifier les produits<br>Ajouter des produits à la liste de blocage<br>Modifier la segmentation des propriétés d'achat |
| Espace de travail | Gérer les intégrations externes | Modifier les partenaires technologiques<br>Modifier l'ingestion de données cloud |
| Espace de travail | Gérer les paramètres multilingues | Modifier les paramètres de localisation<br>Supprimer les paramètres de localisation |
| Espace de travail | Gérer les groupes d'abonnement | Modifier les abonnements |
| Espace de travail | Gérer les étiquettes | Afficher les étiquettes<br>Modifier les étiquettes<br>Supprimer les étiquettes |
| Espace de travail | Gérer les équipes | Afficher les équipes<br>Modifier les équipes<br>Archiver les équipes |
| Espace de travail | Afficher les transformations de données | Afficher la transformation des données |
| Espace de travail | Modifier les transformations de données | Modifier la transformation des données |
| Espace de travail | Gérer le chiffrement des données utilisateur | Modifier le chiffrement au niveau du champ d'identifiant |
| Espace de travail | Envoyer des campagnes et des Canvas | Lancer des campagnes<br>Lancer des Canvas |
| Espace de travail | Afficher les détails de facturation | Afficher les détails de facturation |
| Espace de travail | Afficher les intégrations Currents | Afficher les intégrations Currents |
| Espace de travail | Modifier les intégrations Currents | Modifier les intégrations Currents |
| Espace de travail | Afficher les attributs personnalisés marqués comme PII | Afficher les attributs personnalisés marqués comme PII |
| Espace de travail | Afficher les données d'identification | Afficher les données d'identification |
| Espace de travail | Afficher les profils utilisateur conformes aux PII | Afficher les profils utilisateur conformes aux PII |
| Espace de travail | Afficher les données d'utilisation | Afficher les données d'utilisation |
| Espace de travail | Fusionner les utilisateurs dupliqués | Fusionner les utilisateurs dupliqués |
| Espace de travail | Afficher les utilisateurs dupliqués | Afficher les utilisateurs dupliqués |
| Espace de travail | Créer et modifier des modèles Canvas | Modifier les modèles Canvas |
| Espace de travail | Afficher les modèles Canvas | Afficher les modèles Canvas |
| Espace de travail | Archiver les modèles Canvas | Archiver les modèles Canvas |
| Espace de travail | Publier les pages d'accueil | Publier les pages d'accueil |
| Espace de travail | Créer des brouillons de page d'accueil | Modifier les brouillons de page d'accueil |
| Espace de travail | Accéder aux pages d'accueil | Afficher les pages d'accueil |
| Espace de travail | Créer et modifier des modèles de pages d'accueil | Modifier les modèles de pages d'accueil |
| Espace de travail | Afficher les modèles de pages d'accueil | Afficher les modèles de pages d'accueil |
| Espace de travail | Archiver les modèles de pages d'accueil | Archiver les modèles de pages d'accueil |
| Espace de travail | Afficher les agents d'intelligence artificielle personnalisés | Afficher les agents d'intelligence artificielle personnalisés |
| Espace de travail | Modifier les agents d'intelligence artificielle personnalisés | Modifier les agents d'intelligence artificielle personnalisés<br> Archiver les agents d'intelligence artificielle personnalisés |
| Espace de travail | Afficher les placements | Afficher les placements |
| Espace de travail | Modifier les placements | Modifier les placements |
| Espace de travail | Archiver les placements | Archiver les placements |
| Espace de travail | Nouveau | Afficher la fusion des utilisateurs |
| Espace de travail | Nouveau | Afficher les enregistrements de suppression d'utilisateurs |
| Espace de travail | Nouveau | Supprimer des utilisateurs du tableau de bord |
| Espace de travail | Nouveau | Afficher les modèles de bannières |
| Espace de travail | Nouveau | Modifier les modèles de bannières |
| Espace de travail | Nouveau | Archiver les modèles de bannières |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Foire aux questions

### Puis-je refuser ou annuler la migration ?

Braze ne prend pas en charge l'annulation de la migration. Nous vous accompagnerons tout au long du processus et surveillerons la migration de près afin de résoudre rapidement tout problème éventuel.

### Les utilisateurs existants perdront-ils l'accès à Braze pendant la migration ?

Non, il n'y aura aucun temps d'arrêt sur Braze pendant la migration. Cependant, les mises à jour des autorisations seront verrouillées pendant toute la durée de la migration. Nous estimons que celle-ci devrait prendre environ 15 minutes.