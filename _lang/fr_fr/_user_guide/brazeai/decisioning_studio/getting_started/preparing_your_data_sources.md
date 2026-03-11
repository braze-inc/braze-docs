---
nav_title: Préparation de vos sources de données
article_title: Préparation de vos sources de données
page_order: 2
page_type: reference
description: "Cet article de référence traite des ressources critiques nécessaires pour boucler la boucle décisionnelle de l'intelligence artificielle et permettre à votre agent d'apprendre et de s'améliorer en permanence."
---

# Préparation de vos sources de données

> Cet article de référence traite des ressources critiques nécessaires pour boucler la boucle décisionnelle de l'intelligence artificielle et permettre à votre agent d'apprendre et de s'améliorer en permanence.

## Clôture du cycle décisionnel de l'intelligence artificielle

Bien que toutes les données client soient importantes pour l'agent (voir [Connecter les sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), les ressources les plus importantes sont celles qui indiquent à l'agent ce qui s'est passé après l'envoi des décisions d'engagement client.

Ces ressources créent la boucle de rétroaction qui permet à l'agent d'apprendre.

{% alert note %}
Si l'agent est intégré de manière native à la plateforme d'engagement client (telle que Braze, SFMC ou Klaviyo), aucune étape de configuration supplémentaire n'est nécessaire pour les données de feedback, car celles-ci peuvent être envoyées automatiquement avec les données client.
{% endalert %}

## Données critiques relatives aux commentaires en tant que ressources

Trois ressources essentielles sont nécessaires pour créer la boucle de rétroaction :

1. Données de conversion
2. Données relatives à l'engagement
3. Données d'activation

### Données de conversion

La ressource de conversion décrit ce qui est arrivé au client après l'orchestration. Par exemple, supposons qu'un agent optimise la valeur actuelle nette (VAN) pour les clients bénéficiant de campagnes optimisées. La ressource de conversion pourrait alors inclure une mise à jour quotidienne des variations de la VAN.

| Condition | Raison |
|-------------|------|
| Chaque enregistrement contient un identifiant client unique qui est cohérent avec l'ensemble des ressources. | Decisioning Studio doit suivre le parcours client individuel, depuis la recommandation jusqu'à la conversion, en passant par l'activation. |
| Chaque enregistrement est associé à un horodatage. | Il est extrêmement important de comprendre le délai entre la communication et la séquence des actions du client pour la formation des agents et le calcul des indicateurs. |
| Si vous utilisez un indicateur cible non binaire (par exemple, converti ou non converti), la valeur de l'indicateur cible est fournie avec chaque événement de conversion. | Decisioning Studio utilise la valeur de l'indicateur cible pour générer des expériences d'apprentissage afin de récompenser ou de pénaliser de manière appropriée l'agent en fonction des résultats des actions recommandées. |
| Si les conversions peuvent être attribuées de manière unique aux communications (e.gpar exemple, utilisation d'un coupon), les champs nécessaires pour faire correspondre les conversions aux activations sont fournis. | Si un événement de conversion peut être associé à une communication particulière, cela permet une attribution claire et précise. L'attribution directe fournit l'indication la plus claire à l'agent, mais si cela n'est pas possible (ce qui est souvent le cas), l'attribution basée sur la proximité sera utilisée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Données relatives à l'engagement

La ressource d'engagement décrit les interactions des clients, notamment les clics, les ouvertures et autres impressions. Les données d'engagement peuvent être incluses dans les données de conversion ou être séparées. Il joue un rôle similaire à celui des données de conversion : il informe l'agent de ce qui s'est passé après l'engagement client.

| Condition | Raison |
|-------------|------|
| Chaque enregistrement contient un identifiant client unique qui est cohérent avec l'ensemble des ressources. | Decisioning Studio doit suivre les événements d'engagement pour chaque client individuel. |
| Chaque enregistrement est associé à un horodatage. | Il est extrêmement important de comprendre le délai entre la communication et la séquence des actions du client pour la formation des agents et le calcul des indicateurs. |
| Si les clics, les ouvertures ou d'autres données d'engagement peuvent être attribués de manière unique aux communications, les champs nécessaires pour faire correspondre l'engagement aux activations sont fournis. | Comme pour les données de conversion, si l'engagement peut être associé à une communication particulière, cela permet une attribution claire et précise. L'attribution directe fournit le signal le plus clair à l'agent. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Données d'activation

La ressource « activations » indique à l'agent quelles communications ont été envoyées. Cela est souvent nécessaire selon la configuration de l'orchestration. Si l'agent effectue l'orchestration via une intégration directe avec Braze, SFMC ou Klaviyo, il peut alors être en mesure d'extraire directement les données d'activation.

{% alert note %}
Les données relatives à l'engagement et à l'activation se trouvent très souvent dans la même ressource.
{% endalert %}

| Condition | Raison |
|-------------|------|
| Chaque enregistrement contient un identifiant client unique qui est cohérent avec l'ensemble des ressources. | Decisioning Studio doit suivre le parcours client individuel, depuis la recommandation jusqu'à la conversion, en passant par l'activation. |
| Chaque enregistrement est associé à un horodatage. | Il est extrêmement important de comprendre le délai entre la communication et la séquence des actions du client pour la formation des agents et le calcul des indicateurs. |
| Les champs nécessaires pour faire correspondre le contenu de la communication aux événements d'activation sont fournis (tels que `event_id`) | Il est essentiel d'adapter correctement les caractéristiques de communication aux envois pour l'attribution et la formation des agents. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

