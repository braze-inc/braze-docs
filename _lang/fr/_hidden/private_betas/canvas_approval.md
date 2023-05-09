---
nav_title: Approuver des Canvas
permalink: "/canvas_approval/"
hidden: true
layout: dev_guide
---

# Approuver des Canvas

L’approbation des Canvas ajoute un processus de révision à votre flux de travail avant de le lancer. Vous pouvez maintenant vous assurer que chaque confirmation est approuvée afin de lancer le Canvas.

{% alert important %}
Le flux de travail d’approbation pour les Canvas est actuellement en accès anticipé. Contactez votre CSM Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Activer l’approbation Canvas

Pour activer le flux de travail d’approbation pour Canvas, allez dans **Manage Settings > Approval Settings (Gérer les paramètres > Paramètres d’approbation)**. Cette fonctionnalité est désactivée par défaut.

![Les paramètres du flux de travail d’approbation dans lesquels l’option d’utilisation du flux de travail d’approbation pour les campagnes et les Canvas est activée.][1]

{% alert note %}
Seuls les administrateurs et utilisateurs disposant d’autorisations pour gérer les paramètres d’approbation verront cette page. Assurez-vous de vérifier que vous disposez des [autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/) appropriées pour approuver les Canvas.
{% endalert %}

## Utiliser les approbations

Lorsque le flux de travail d’approbation est activé, vous aurez accès à l’étape **Résumé** du créateur Canvas. Cette page fournit un résumé des principaux détails de Canvas avec la possibilité d’approuver ou de refuser ces détails, y compris les événements de conversion, la planification d’entrée, ainsi que le type et la quantité de composants dans votre Canvas. Notez que l’état d’approbation par défaut du Canvas est **Approbation en attente**.

Une fois que les statuts d’approbation sont définis à l’étape **Résumé**, toutes les modifications ultérieures apportées au Canvas réinitialiseront tous les statuts d’approbation une fois enregistrés. Cela s’applique à toutes les modifications effectuées dans une ébauche de Canvas ou un Canvas après lancement. Par exemple, si vous apportez uniquement des modifications à l’audience cible, l'étape **Résumé** rétablira les statuts d'approbation pour toutes les sections à l'état par défaut, en attente.

![Un exemple de flux de travail d’approbation Canvas où les détails des événements de conversion et de planification d’entrée ont été marqués comme approuvés.][2]{: style="max-width:85%" }

Une fois que chaque section est approuvée, le bouton **Launch (Lancer)** sera disponible et vous pourrez lancer votre Canvas.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}