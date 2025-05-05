---
nav_title: Contentsquare
article_title: Contentsquare
description: "Cet article de référence décrit le partenariat entre Braze et Contentsquare, une plateforme d'analyse de l'expérience numérique qui vous permet d'améliorer la pertinence et les taux de conversion de vos campagnes en ciblant les messages en fonction de l'expérience numérique de vos clients."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) est une plateforme d'analyse de l'expérience numérique qui permet de comprendre efficacement l'expérience client.

_Cette intégration est assurée par Contentsquare._

## À propos de l'intégration

L'intégration de Braze et Contentsquare vous permet d'envoyer des Signaux en ligne (fraude, signaux de frustration, etc.) en tant que custom events dans Braze. Exploitez les informations d'expérience de Contentsquare pour améliorer la pertinence de vos campagnes et les taux de conversion en ciblant les messages en fonction de l'expérience numérique et du langage corporel de vos clients.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Contentsquare | Un compte Contentsquare est requis pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. Pour créer une nouvelle clé dans le tableau de bord de Braze, allez dans **Paramètres** > **Clés API.** |
| Endpoint REST Braze | [Votre URL de l’endpoint REST][1].] Votre endpoint dépendra de l'URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Voici quelques cas d'utilisation courants de Braze et Contentsquare :
- Hyper-personnalisez les messages en fonction de l'intention du client en faisant apparaître les données d'expérience client dans Braze.
- Reciblez les clients en fonction de leur comportement numérique, de leurs hésitations, de leur frustration et de leur intention.
- Identifiez les mauvaises expériences au sein de Contentsquare et récupérez les clients avec des messages ciblés et des offres de rétention.
- Récupérez les clients à risque en envoyant des messages plus pertinents et empathiques au bon moment et au bon endroit.

## Intégration

Pour intégrer Contentsquare dans Braze, vous devez demander l'installation d'une intégration "Signaux en ligne" à partir du catalogue d'intégration de Contentsquare :

1. Dans Contentsquare, cliquez sur **Console** dans le menu **Paramètres**. Cela vous redirigera vers le projet sur lequel vous travaillez actuellement. 
2. Sur la page **Projets**, allez à l'onglet **Intégrations** et cliquez sur le bouton **\+ Ajouter une intégration**.
3. Dans le catalogue des intégrations, recherchez l'intégration **Signaux en ligne** et cliquez sur **Ajouter**. L'équipe Contentsquare vous contactera ensuite pour configurer l'extrait de code afin d'envoyer des signaux en ligne à Braze.
4. Contentsquare va maintenant traiter votre intégration. Le texte de l'indicateur sera mis à jour après que l'intégration aura été complétée.

Pour plus d'informations, consultez la section [Demander une intégration Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Utilisation de cette intégration

Une fois l'intégration terminée, les custom events Contentsquare seront disponibles pour être utilisés dans vos campagnes et Canvases. Vous pouvez vérifier quels événements sont envoyés à Braze depuis **Paramètres des données** > **Événements personnalisés**.

![Données de signaux en ligne de Contentsquare dans l'onglet Événements personnalisés de Braze][1]


[1]: {% image_buster /assets/img/contentsquare_custom_events.png %} 
