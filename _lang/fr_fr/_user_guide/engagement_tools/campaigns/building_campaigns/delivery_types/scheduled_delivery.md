---
nav_title: Réception/distribution planifiée
article_title: Réception/distribution planifiée
page_order: 0
page_type: reference
description: "Cet article de référence décrit les différences entre les options de planification temporelle pour la réception/distribution des campagnes."
tool: Campaigns

---

# Réception/distribution planifiée

> Les campagnes envoyées à l'aide de la réception/distribution programmée en fonction de l'heure sont livrées aux jours spécifiés.

## Option 1 : Envoyer dès que la campagne est lancée

Si vous choisissez d'envoyer un message dès qu'il est lancé, votre message commencera à être envoyé dès que vous aurez fini de créer votre campagne.

La section "Réception/distribution" avec l'option "Planifié" sélectionnée et l'option de planification temporelle de l'envoi dès que la campagne est lancée.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Ce type de planification est conçu pour des campagnes ponctuelles que vous souhaitez envoyer immédiatement, comme des messages sur un événement d'actualité. Une application sportive, par exemple, peut planifier des notifications push sur les mises à jour des scores à l'aide de cette option. En outre, lorsque vous envoyez des messages de test destinés uniquement à vous-même ou à votre équipe, cette option vous permet de les délivrer immédiatement. 

Si vous envisagez de modifier la campagne et de l'envoyer à nouveau après avoir vu le test, veillez à cocher la case qui rend les utilisateurs à [nouveau éligibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) pour recevoir la campagne. Par défaut, Braze n'envoie qu'une seule fois une campagne à un utilisateur, sauf si cette case est cochée.

## Option 2 : Envoyer à une heure donnée

La planification d'une campagne pour une période donnée vous permet de spécifier les jours et les heures d'envoi de votre campagne. Vous pouvez envoyer un message une seule fois, tous les jours, toutes les semaines ou tous les mois à un moment précis de la journée, et spécifier quand votre campagne doit commencer et se terminer. Cette date de fin est inclusive, ce qui signifie que le dernier envoi aura lieu à la date de fin. 

Si vous sélectionnez la **réception/distribution planifiée** et que vous ne choisissez pas d'envoyer à l'heure locale de l'utilisateur, votre campagne sera envoyée en fonction du fuseau horaire spécifié sur la page **Paramètres de l'entreprise**.

\![Les options de planification basées sur le temps permettent d'envoyer une campagne à une heure donnée.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campagnes sur les fuseaux horaires locaux

Vous pouvez envoyer le message en tenant compte des fuseaux horaires des utilisateurs, de sorte que les membres de votre audience internationale ne reçoivent pas de notification à des moments inopportuns. Les campagnes sur les fuseaux horaires locaux doivent être planifiées 24 heures à l'avance pour que les utilisateurs éligibles de tous les fuseaux horaires puissent les recevoir. Consultez la [FAQ sur les]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/) campagnes pour comprendre le fonctionnement des campagnes sur les fuseaux horaires locaux et les règles de réception/distribution associées.

Les segments ciblés par des campagnes sur les fuseaux horaires locaux devraient inclure, au minimum, une fenêtre de deux jours pour intégrer les utilisateurs de tous les fuseaux horaires. Par exemple, si votre campagne est planifiée pour être envoyée le soir mais qu'elle n'a qu'une fenêtre d'un jour, certains utilisateurs peuvent être sortis du segment lorsque leur fuseau horaire est atteint. Les filtres qui créent une fenêtre de 2 jours sont par exemple "dernière utilisation il y a plus d'un jour" et "dernière utilisation il y a moins de 3 jours", ou "premier achat il y a plus de 7 jours" et "premier achat il y a moins de 9 jours".

### Cas d'utilisation

Les plages horaires désignées conviennent mieux aux messages planifiés à l'avance et aux campagnes récurrentes, telles que l'onboarding et la rétention, qui s'exécutent régulièrement sur tous les utilisateurs qualifiés.

## Option 3 : Le timing intelligent

Le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) vous permet de diffuser une campagne à chaque utilisateur à un moment différent. Braze calcule le temps de chaque individu en fonction du moment où cet utilisateur s'engage généralement avec votre appli et ses notifications. Vous pouvez éventuellement spécifier que les campagnes de timing intelligent ne sont envoyées que pendant une certaine partie de la journée. Par instance, si vous informez les utilisateurs d'une promotion qui se termine à minuit, vous voudrez peut-être que vos messages soient envoyés au plus tard à 22 heures.

Les options de planification basées sur le temps pour utiliser le timing intelligent afin d'envoyer une campagne au moment où l'utilisation de l'application est la plus populaire parmi tous les utilisateurs.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Règles de réception/distribution

Étant donné que l'heure optimale d'un utilisateur peut se situer à n'importe quel moment au cours d'une période de 24 heures, toutes les campagnes de timing intelligent doivent être planifiées 24 heures à l'avance. En outre, à l'instar des campagnes à heure fixe, les messages avec une fenêtre d'un jour manqueront les utilisateurs qui sortent du segment avant d'avoir atteint l'heure optimale dans leur fuseau horaire. Les segments des campagnes de timing intelligent doivent comporter au moins une fenêtre de trois jours pour tenir compte de ce facteur.

Si le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer une heure optimale, vous pouvez choisir une méthode de secours qui consiste à envoyer l'application pendant l'heure la plus populaire parmi tous les utilisateurs ou à définir une heure de repli personnalisée. 

### Cas d'utilisation

Les campagnes de timing intelligent conviennent mieux aux messages uniques et récurrents pour lesquels il existe une certaine flexibilité en ce qui concerne le délai de réception/distribution, par exemple lorsqu'elles ne sont pas bien adaptées aux nouvelles de dernière minute ou aux annonces programmées.

