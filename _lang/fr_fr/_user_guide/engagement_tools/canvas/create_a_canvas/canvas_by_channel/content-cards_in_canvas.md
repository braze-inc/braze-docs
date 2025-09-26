---
nav_title: Cartes de contenu
article_title: Cartes de contenu dans Canvas
page_order: 1
page_type: reference
description: "Cet article de référence décrit les fonctionnalités et les nuances spécifiques à l’utilisation de cartes de contenu, comme canal de communication dans Canvas."
tool: Canvas
channel: content cards

---

# Cartes de contenu dans Canvas

> Des cartes de contenu peuvent être envoyées à vos clients dans le cadre de leur parcours Canvas. Cet article décrit les fonctionnalités et les nuances spécifiques à l’utilisation de cartes de contenu, comme canal de communication dans Canvas.

Comme pour d’autres canaux de communication Canvas, les cartes de contenu seront envoyées sur l’appareil d’un utilisateur, lorsqu’elles répondent aux critères d’audience et de ciblage indiqués pour son étape. Une fois la carte de contenu envoyée, elle sera disponible dans le flux de chaque utilisateur éligible à la prochaine mise à jour du flux de cartes.

![Cartes de contenu sélectionnées comme canal d'envoi de messages pour une étape de message.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

L'[expiration](#content-card-expiration) et la [suppression de](#removal) la carte de contenu sont deux options qui modifient l'interaction de l'étape du canvas.

## Expiration de la carte de contenu {#content-card-expiration}

Lorsque vous composez une nouvelle carte de contenu, vous pouvez choisir la date à laquelle elle doit expirer du flux de l'utilisateur en fonction de son heure d'envoi. Le compte à rebours de l'expiration d'une carte de contenu commence lorsque l'utilisateur atteint l'étape du message dans le canvas où la carte est envoyée. La carte sera active dans le flux de l'utilisateur à partir de ce moment et jusqu'à son expiration. Une carte peut rester dans le flux d'un utilisateur jusqu'à 30 jours. 

![Paramètres d'expiration d'une carte de contenu pour une étape de message qui sera supprimée après trois heures dans le flux d'un utilisateur.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Types d'expiration

Vous avez deux possibilités pour déterminer quand une carte doit disparaître du flux d'un utilisateur : une date relative ou une date absolue.

#### Dates relatives

Lorsque vous choisissez une date relative, comme "Supprimer les cartes envoyées après 5 jours dans le flux d'un utilisateur", vous pouvez définir une date d'expiration allant jusqu'à 30 jours.

#### Dates absolues

Lorsque vous choisissez une date absolue, comme "Retirer les cartes envoyées le 1er décembre 2023 à 16 heures", il y a une nuance à apporter.

Bien que vous puissiez spécifier une durée d'expiration supérieure à 30 jours, la carte de contenu existera dans le flux d'un utilisateur pendant 30 jours maximum. La spécification d'une durée supérieure à 30 jours vous permet de tenir compte d'éventuels retards avant de déclencher l'étape Message, mais elle ne prolonge pas la durée de vie maximale de la carte dans le flux de l'utilisateur.

Soyez prudent lorsque vous fixez une date d'expiration plus de 30 jours avant le lancement du canvas. Si un utilisateur atteint l'étape Message plus de 30 jours avant la date d'expiration spécifiée, la carte ne sera pas envoyée.

### Comportement à l'expiration

La carte de contenu reste disponible dans le flux de l'utilisateur jusqu'à ce qu'elle atteigne sa date d'expiration, même si l'utilisateur passe aux étapes suivantes du canvas. Si vous ne souhaitez pas que la carte de contenu soit en ligne lorsque les étapes suivantes du canvas sont réalisées, vérifiez que l’expiration est plus courte que le délai dans les étapes suivantes.

Lorsqu'une carte de contenu expire, elle est automatiquement supprimée du flux de l'utilisateur lors de la prochaine actualisation, même s'il ne l'a pas encore consultée.

## Retrait de la carte de contenu {#removal}

Les cartes de contenu peuvent être supprimées lorsque les utilisateurs effectuent un achat ou un événement personnalisé. Vous pouvez sélectionner l'un des événements suivants comme événement de suppression : **Réaliser un événement personnalisé** et **effectuer un achat**. Sélectionnez ensuite **Ajouter un événement**.

!["Retirer les cartes lorsque les utilisateurs effectuent un achat ou un événement personnalisé" sélectionné avec le déclencheur pour retirer les cartes pour les utilisateurs qui effectuent un achat spécifique pour "Bracelet".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Reporting et analyses

Après le lancement d’une étape Cartes de contenu dans Canvas, vous pouvez commencer à analyser plusieurs indicateurs différents pour cette étape. Ces indicateurs contiennent le nombre de messages envoyés, les destinataires uniques, les taux de conversion, le revenu total et bien plus.

![Analyse/analytique d'une étape de message avec la carte de contenu message performance.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Pour plus d'informations sur les indicateurs disponibles et leurs définitions, consultez notre [glossaire des indicateurs de rapport.]({{site.baseurl}}/user_guide/data/report_metrics/)

## Cas d’utilisation

#### Offres promotionnelles

Ajoutez des cartes au flux d’un utilisateur lorsqu’il est éligible à des promotions et des publicités spécifiques. Par exemple, si un utilisateur devient éligible pour une nouvelle offre à la suite d’une action ou d’un achat, un Canvas vous permet de lui envoyer une carte de contenu en plus d’autres canaux de communication, de sorte que l’offre soit disponible à sa prochaine connexion à l’application.

#### Boîte de réception de notification push

Il arrive parfois qu’un utilisateur soit amené à rejeter une notification push ou supprimer un e-mail et que vous souhaitiez lui envoyer un rappel ou renouveler l’offre au cas où il change d’avis.

Canvas vous permet d’ajouter un composant pour envoyer une carte de contenu et une notification push pour proposer aux utilisateurs une « boîte de réception » de cartes permanente, pour mieux correspondre aux messages promotionnels envoyés via notification push. 

#### Plusieurs flux en fonction des catégories

Vous pouvez séparer vos cartes de contenu en plusieurs flux, en fonction de catégories, par exemple les différents sujets que les utilisateurs peuvent parcourir ou les flux transactionnels et marketing. Pour plus d'informations sur la création de plusieurs flux à l'aide de paires clé-valeur, consultez notre guide sur la [personnalisation des flux de la carte de contenu.]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds)


