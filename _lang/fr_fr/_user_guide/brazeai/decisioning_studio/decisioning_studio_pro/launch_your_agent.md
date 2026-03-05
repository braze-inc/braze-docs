---
nav_title: Lancez votre agent
article_title: Lancez votre agent
page_order: 4
description: "Apprenez à lancer votre agent Decisioning Studio Pro et à fermer la boucle de décision de l'intelligence artificielle pour une optimisation par auto-apprentissage."
---

# Lancez votre agent

> Une fois que vous avez connecté les sources de données, configuré l'orchestration et conçu votre agent, vous êtes prêt à vous lancer. Cet article traite de l'activation de votre agent et de la fermeture de la boucle de décision de l'intelligence artificielle afin que l'agent puisse apprendre et s'améliorer en permanence.

## Lancement de votre agent

Après avoir effectué toutes les étapes de configuration avec votre équipe de services décisionnels de l'intelligence artificielle :

1. Vérifiez la configuration de votre agent pour vous assurer que tous les paramètres sont corrects.
2. Vérifiez que vos connexions de données et vos intégrations d'orchestration sont actives.
3. Travaillez avec votre équipe de services décisionnels de l'intelligence artificielle pour activer l'agent.

Une fois lancé, votre agent sera :
- Commencer à recevoir des données sur l'audience et les clients.
- Commencez à faire des recommandations personnalisées pour chaque client.
- Orchestrer des actions par le biais de votre CEP configuré
- Recueillir des données de retour d'information pour apprendre et s'améliorer au fil du temps.

## Boucler la boucle de la prise de décision en matière d'intelligence artificielle

Une fois lancé, votre agent a besoin de données de retour pour apprendre et s'améliorer. Il s'agit notamment des données de conversion, des données d'engagement et des données d'activation qui indiquent à l'agent ce qui s'est passé après l'envoi des décisions d'engagement client.

Pour obtenir des informations détaillées sur la préparation de ces ressources de données de retour d'information essentielles, voir [Préparer vos sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/).

{% alert note %}
Si l'agent est nativement intégré à la plateforme d'engagement client (comme Braze, SFMC ou Klaviyo), il se peut qu'aucune étape de configuration supplémentaire ne soit nécessaire pour les données de retour d'expérience, car celles-ci peuvent être envoyées automatiquement avec les données client.
{% endalert %}

## Suivi de votre agent

Après le lancement, collaborez avec votre équipe de services décisionnels d'intelligence artificielle pour surveiller les performances :

- **Indicateurs de performance**: Suivez vos indicateurs de réussite à travers les groupes d'expérimentation.
- **Progression de l'apprentissage**: Observer l'évolution des recommandations de l'agent dans le temps
- **Informations**: Comprendre quelles sont les dimensions et les options qui génèrent des résultats pour les différents segments de clientèle.

## Optimisation continue

Votre équipe de services d'intelligence artificielle continuera à travailler avec vous pour :

- Analyser les performances des agents et identifier les possibilités d'optimisation
- Augmenter les dimensions ou les options selon les besoins
- Adjust constraints based on business rule changes (Ajustez les contraintes en fonction des modifications des règles de gestion)
- Appliquer à d'autres cas d'utilisation les agents qui ont fait leurs preuves

{% alert tip %}
L'agent apprend et s'améliore continuellement au fil du temps. Laissez suffisamment de temps à l'agent pour recueillir des données et optimiser avant d'apporter des modifications importantes à la configuration.
{% endalert %}

