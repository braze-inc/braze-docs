---
nav_title: Octobre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version d’octobre 2018."
---
# Octobre 2018

{% comment %}
  À ajouter ultérieurement...
  Activation/Désactivation du groupe de contrôle selon une sélection intelligente
  La section Sélection intelligente comporte maintenant une case à cocher qui vous permet d’[activer ou désactiver l’utilisation d’un groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group). Si activé, le groupe de contrôle fera 20 % de la taille du public et évoluera pendant que la sélection intelligente optimise ainsi les tailles de public en fonction des variantes.
  Assistant de paramètres de Canvas Entry (Bêta)
  L’interface utilisateur de Canvas sera simplifiée pour éviter les tâches manquées et les erreurs résultantes. Les configurations Canvas, en particulier, seront désormais affichées dans un assistant, comme pour la création des Campagnes. Ce n’est pas reflété dans notre documentation actuellement, car c’est déployé progressivement. Revenez bientôt pour en savoir plus !
  API Groupe d’abonnement (masqué)
  Braze a mis à disposition un nouvel appel GET pour vous permettre de faire des requêtes basées sur un identifiant externe ou une adresse électronique. Vous recevrez ensuite tous les groupes d’abonnement associés à cet utilisateur.
{% endcomment %}

## Calculer les statistiques exactes du public pour les campagnes

Vous pouvez maintenant aller sur **Campaign Analytics** (Analyse de campagne) et calculer les statistiques exactes pour votre public. Cliquez sur **Calculate Exact Stats (Calculer les statistiques exactes)** dans le pied de page de la section **Target Users (Utilisateurs cibles)** pour afficher les statistiques exactes du public. Vous devrez enregistrer la campagne avant le calcul (les ébauches de campagnes seront enregistrées sous forme de brouillons).

## Obsolescence de Windows 8

Braze ne prend plus en charge Windows 8 à compter du 10 octobre 2018.

## Centre des partenariats

Vous pouvez maintenant trouver une liste de vos intégrations sur la plateforme Braze sous **Integrations** (Intégrations), ainsi que les instructions et clés d’intégration.

## Calculs des analyses pour l’e-mail

Braze calcule désormais toutes les analyses d’e-mails à l’aide des données d’événements de notre partenaire d’envoi (ESP) afin d’améliorer considérablement l’exactitude de nos analyses pour l’e-mail. Cette solution utilise Postgres, une base de données open source, pour garantir l’intégrité des données.

{% alert important %}
Les ouvertures uniques et les clics uniques dépendent actuellement des données agrégées fournies par nos partenaires d’envoi d’e-mails. Des travaux sont en cours pour calculer ces statistiques d’unicité en utilisant la même infrastructure introduite dans cette version.
{% endalert %}

## Commandes du panneau Composer

Les commandes du Message Composer ont été actualisées en ajoutant du texte aux icônes pour une meilleure utilisation et une meilleure navigation.

## Azure pour Currents

Les clients Braze qui utilisent Currents peuvent maintenant envisager d’intégrer [Azure]({{site.baseurl}}/partners/braze_currents/data_storage_integrations/partners/microsoft_azure_blob_storage/).

## Extensions des champs d’entrée

Vous pouvez maintenant développer les champs d’entrée pour les lignes d’objet des e-mails et les titres des notifications push.
