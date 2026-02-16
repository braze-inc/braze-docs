---
nav_title: Préparer vos sources de données
article_title: Préparer vos sources de données
page_order: 2
page_type: reference
description: "Cet article de référence traite des ressources de données de retour d'information essentielles nécessaires pour fermer la boucle décisionnelle de l'intelligence artificielle et permettre à votre agent d'apprendre et de s'améliorer en permanence."
---

# Préparer vos sources de données

> Cet article de référence traite des ressources de données de retour d'information essentielles nécessaires pour fermer la boucle décisionnelle de l'intelligence artificielle et permettre à votre agent d'apprendre et de s'améliorer en permanence.

## Boucler la boucle de la prise de décision en matière d'intelligence artificielle

Si toutes les données clients sont importantes pour l'agent (voir [Connecter les sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), les ressources de données les plus importantes sont celles qui indiquent à l'agent ce qui s'est passé après l'envoi des décisions relatives à l'engagement client.

Ces ressources créent la boucle de rétroaction qui permet à l'agent d'apprendre.

{% alert note %}
Si l'agent est nativement intégré à la plateforme d'engagement client (comme Braze, SFMC ou Klaviyo), il se peut qu'aucune étape de configuration supplémentaire ne soit nécessaire pour les données de retour d'expérience, car celles-ci peuvent être envoyées automatiquement avec les données client.
{% endalert %}

## Retour d'information critique sur les ressources en données

Il existe trois ressources essentielles pour créer la boucle de rétroaction :

1. Données sur les conversions
2. Données sur l'engagement
3. Données relatives aux activations

### Données sur les conversions

La ressource de conversion décrit ce qui est arrivé au client après l'orchestration. Par exemple, si un agent optimise la valeur actuelle nette (VAN) des clients recevant des campagnes optimisées, la ressource de conversion peut inclure une mise à jour quotidienne des changements de VAN.

| Condition | Raison |
|-------------|------|
| Chaque enregistrement contient un identifiant de client unique qui est cohérent avec toutes les ressources de données. | Decisioning Studio doit suivre le parcours client individuel, de la recommandation à la conversion, en passant par l'activation. |
| Chaque enregistrement est associé à un horodatage | Il est extrêmement important de comprendre le temps écoulé entre les communications et la séquence des actions du client pour la formation des agents et le calcul des indicateurs. |
| En cas d'utilisation d'un indicateur cible non binaire (tel que converti ou non converti), la valeur de l'indicateur cible est fournie avec chaque événement de conversion. | Decisioning Studio utilise la valeur de l'indicateur cible pour générer des expériences de formation afin de récompenser/pénaliser l'agent de manière appropriée en fonction des résultats des actions recommandées. |
| Si les conversions peuvent être attribuées de manière unique aux communications (e.g., échange de coupons), les champs nécessaires pour faire correspondre les conversions aux activations sont fournis | Si un événement de conversion peut être lié à une communication particulière, cela permet une attribution nette et précise. L'attribution directe fournit le signal le plus clair à l'agent, mais si cela n'est pas possible (comme c'est souvent le cas), l'attribution basée sur la proximité sera utilisée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Données sur l'engagement

La ressource d'engagement décrit les interactions avec les clients, notamment les clics, les ouvertures et autres impressions. Les données d'engagement peuvent être incluses dans les données de conversion ou être séparées. Elles jouent un rôle similaire à celui des données sur les conversions - elles indiquent à l'agent ce qui s'est passé après l'engagement du client.

| Condition | Raison |
|-------------|------|
| Chaque enregistrement contient un identifiant de client unique qui est cohérent avec toutes les ressources de données. | Decisioning Studio doit assurer le suivi des événements d'engagement pour chaque client. |
| Chaque enregistrement est associé à un horodatage | Il est extrêmement important de comprendre le temps écoulé entre les communications et la séquence des actions du client pour la formation des agents et le calcul des indicateurs. |
| Si les clics, les ouvertures ou d'autres données d'engagement peuvent être attribués de manière unique aux communications, les champs nécessaires pour faire correspondre l'engagement aux activations sont fournis | Comme pour les données de conversion, si l'engagement peut être lié à une communication particulière, cela permet une attribution nette et précise. L'attribution directe constitue le signal le plus clair pour l'agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Données relatives aux activations

La ressource activations indique à l'agent quelles communications ont été envoyées. Cela est souvent nécessaire en fonction de la manière dont l'orchestration est configurée. Si l'agent orchestre via une intégration directe avec Braze, SFMC ou Klaviyo, alors l'agent peut être en mesure de tirer des données d'activation directement.

{% alert note %}
Les données d'engagement et les données d'activations se retrouvent très couramment dans la même ressource de données.
{% endalert %}

| Condition | Raison |
|-------------|------|
| Chaque enregistrement contient un identifiant de client unique qui est cohérent avec toutes les ressources de données. | Decisioning Studio doit suivre le parcours client individuel, de la recommandation à la conversion, en passant par l'activation. |
| Chaque enregistrement est associé à un horodatage | Il est extrêmement important de comprendre le temps écoulé entre les communications et la séquence des actions du client pour la formation des agents et le calcul des indicateurs. |
| Les champs nécessaires pour faire correspondre le contenu de la communication aux événements d'activation sont fournis (tels que `event_id`). | La correspondance correcte entre les caractéristiques de la communication et les envois est nécessaire pour l'attribution et la formation des agents. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

