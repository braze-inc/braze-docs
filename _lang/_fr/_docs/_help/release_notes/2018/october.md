---
nav_title: Octobre
page_order: 4
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour octobre 2018."
---

# Octobre 2018

{% comment %}
  Ajoutez-les plus tard... Activer/désactiver le groupe de contrôle de sélection intelligente La case de sélection intelligente a maintenant une case à cocher qui vous permet [d'activer/désactiver l'utilisation d'un groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group). Quand activé, le groupe de contrôle sera 20 % de la taille du public et changera à mesure que la fonction de sélection intelligente optimise la taille du public par variante. Assistant de configuration des entrées de Canvas (Beta) L'interface utilisateur de Canvas sera simplifiée pour éviter les tâches manquées et les erreurs qui en résultent. Les configurations sur le canevas sont maintenant affichées dans un assistant similaire à l'assistant Campagnes. Cela ne se reflète pas actuellement dans notre documentation, car il est déployé progressivement. Revenez voir pour plus de détails à ce sujet bientôt! Groupe d'abonnement API (masqué) Braze a fait un nouvel appel GET disponible pour vous permettre de demander en fonction d'un ID externe ou d'une adresse e-mail. Vous recevrez alors tous les groupes d'abonnement associés à cet utilisateur.
{% endcomment %}

## Calculer les statistiques d'audience exactes pour les campagnes

Vous pouvez maintenant aller à **Analyses de campagne** et calculer les statistiques exactes de votre public. Appuyez sur __Calculer les statistiques exactes__ dans le pied de page de la section __Utilisateurs cibles__ et les statistiques d'audience exactes se rempliront. Vous devrez enregistrer la campagne avant de calculer (les brouillons de campagnes seront enregistrés comme brouillons).

## Dépréciation de Windows 8

Braze ne prend plus en charge Windows 8 depuis le 10 octobre 2018.

## Hub Partenariats

Vous pouvez maintenant trouver une liste de vos intégrations sur la plateforme Braze sous __Intégrations__, ainsi que des clés et des instructions d'intégration.

## Calcul de l'analytique des emails

Braze est maintenant en train de calculer toutes les analyses de courrier électronique à l’aide des données de l’événement de notre partenaire (EP), afin d’améliorer considérablement la précision de nos analyses de courriel. Cette solution utilise Postgres, une solution de base de données open source, pour assurer l'intégrité des données.

{% alert important %}
Les ouvertures uniques et les clics uniques dépendent toujours des données agrégées fournies par nos partenaires d'envoi de courriels. Il y a du travail en cours pour calculer ces statistiques d'unicité en utilisant la même infrastructure introduite dans cette version.
{% endalert %}

## Contrôles du panneau des compositeurs

Les contrôles du compositeur de messages ont été actualisés pour inclure le libellé associé aux icônes afin de permettre une meilleure convivialité et une meilleure navigation.

## Azure pour les courants

Les clients Braze utilisant les courants peuvent maintenant voir [Azure]({{site.baseurl}}/partners/braze_currents/data_storage_integrations/partners/microsoft_azure_blob_storage/) comme une intégration potentielle.

## Expansion du champ de saisie

Vous pouvez maintenant étendre les champs de saisie pour les lignes de sujet de courriel et les titres de poussage.
