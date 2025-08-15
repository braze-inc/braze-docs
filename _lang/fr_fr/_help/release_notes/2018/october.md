---
nav_title: octobre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version d’octobre 2018."
---
# Octobre 2018

{% comment %}
  À ajouter ultérieurement...
  Activation/Désactivation du groupe de contrôle selon une sélection intelligente
  La boîte de sélection intelligente comporte désormais une case à cocher qui vous permet de [basculer l'utilisation d'un groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group). Si activé, le groupe de contrôle fera 20 % de la taille de l'audience et évoluera pendant que la sélection intelligente optimise ainsi les tailles d'audience en fonction des variantes.
  Assistant de paramètres de Canvas Entry (Bêta)
  L’interface utilisateur de Canvas sera simplifiée pour éviter les tâches manquées et les erreurs résultantes. Les configurations de canvas, en particulier, seront désormais affichées dans un assistant, similaire à la conception de l'assistant de campagnes. Ce n’est pas reflété dans notre documentation actuellement, car c’est déployé progressivement. Revenez bientôt pour en savoir plus !
  API Groupe d’abonnement (masqué)
  Braze a mis à disposition un nouvel appel GET pour vous permettre de faire des requêtes basées sur un identifiant externe ou une adresse électronique. Vous recevrez ensuite tous les groupes d’abonnement associés à cet utilisateur.
{% endcomment %}

## Calculer les statistiques exactes de l'audience des campagnes

Vous pouvez maintenant vous rendre dans **Campaign Analytics** et calculer les statistiques exactes pour votre audience. Cliquez sur **Calculer les statistiques exactes** dans le pied de page de la section **Audiences cibles**, et les statistiques exactes de l'audience s'afficheront. Vous devrez enregistrer la campagne avant le calcul (les ébauches de campagnes seront enregistrées sous forme de brouillons).

## Obsolescence de Windows 8

Braze ne prend plus en charge Windows 8 à compter du 10 octobre 2018.

## Centre des partenariats

Vous trouverez désormais la liste de vos intégrations sur la plateforme Braze sous **Intégrations**, ainsi que les clés d'intégration et les instructions.

## Calculs des analyses pour l’e-mail

Braze calcule désormais toutes les analyses d’e-mails à l’aide des données d’événements de notre partenaire d’envoi (ESP) afin d’améliorer considérablement l’exactitude de nos analyses pour l’e-mail. Cette solution utilise Postgres, une base de données open source, pour garantir l’intégrité des données.

{% alert important %}
Les ouvertures uniques et les clics uniques dépendent actuellement des données agrégées fournies par nos partenaires d’envoi d’e-mails. Des travaux sont en cours pour calculer ces statistiques d’unicité en utilisant la même infrastructure introduite dans cette version.
{% endalert %}

## Commandes du panneau Composer

Les commandes du Message Composer ont été actualisées en ajoutant du texte aux icônes pour une meilleure utilisation et une meilleure navigation.

## Azure pour Currents

Les clients de Braze qui utilisent Currents peuvent désormais considérer [Azure]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents#microsoft-azure-blob-storage) comme une intégration potentielle.

## Extensions des champs d’entrée

Vous pouvez maintenant développer les champs d’entrée pour les lignes d’objet des e-mails et les titres des notifications push.
