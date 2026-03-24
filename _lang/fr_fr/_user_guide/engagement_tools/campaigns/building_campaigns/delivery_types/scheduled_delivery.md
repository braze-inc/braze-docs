---
nav_title: Livraison planifiée
article_title: Livraison planifiée
page_order: 0
page_type: reference
description: "Le présent article de référence décrit les différences entre les options de planification temporelle pour la livraison de campagnes."
tool: Campaigns

---

# Livraison planifiée

> Les campagnes envoyées à l'aide d'une livraison planifiée temporellement sont livrées à des jours spécifiés.

## Option 1 : Envoyer dès que la campagne est lancée

Si vous choisissez d'envoyer un message dès qu'il est lancé, il commencera à être envoyé dès que vous aurez fini de créer votre campagne.

![La section « Réception/distribution » avec l'option « Planifié » sélectionnée et l'option de planification temporelle d'envoi dès que la campagne est lancée.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Ce type de planification est conçu pour les campagnes ponctuelles que vous souhaitez envoyer immédiatement, comme les messages concernant un événement en cours. Une application sportive, par exemple, peut planifier des notifications push sur les mises à jour des scores en utilisant cette option. De même, lorsque vous envoyez des messages de test destinés à vous-même ou à votre équipe, cette option vous permet de les distribuer immédiatement. 

Si vous envisagez de modifier la campagne et de l'envoyer à nouveau après avoir consulté le test, veillez à cocher la case qui rend les utilisateurs à [nouveau éligibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) pour recevoir la campagne. Par défaut, Braze n'envoie une campagne qu'une seule fois à un utilisateur, sauf si cette case est cochée.

## Option 2 : Envoyer à un moment spécifié

La planification d'une campagne à un moment spécifié vous permet de définir les jours et les heures auxquels votre campagne sera envoyée. Vous pouvez envoyer un message une fois, quotidiennement, hebdomadairement ou mensuellement à un certain moment de la journée, et préciser quand votre campagne doit commencer et se terminer. Cette date de fin est inclusive, ce qui signifie que le dernier envoi aura lieu à la date de fin.

Si vous sélectionnez une planification mensuelle récurrente, notez que certains mois peuvent ne pas comporter le jour sélectionné. Par exemple, imaginons que vous configurez une campagne pour un envoi mensuel le 31. Dans ce cas, Braze envoie le dernier jour du mois concerné, comme le 30 avril, puisque le 31 avril n'existe pas.

Si vous sélectionnez la **réception/distribution planifiée** et que vous ne choisissez pas d'envoyer à l'heure locale de l'utilisateur, votre campagne sera envoyée en fonction du fuseau horaire spécifié sur la page **Paramètres de la société**.

![Les options de planification temporelle pour envoyer une campagne à une heure donnée.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campagnes dans le fuseau horaire local

Vous pouvez envoyer le message dans les fuseaux horaires locaux des utilisateurs afin que les membres de votre audience internationale ne reçoivent pas de notification à des moments inopportuns. Les campagnes dans le fuseau horaire local doivent être planifiées 24 heures à l'avance pour garantir que les utilisateurs éligibles de tous les fuseaux horaires puissent les recevoir. Consultez la [FAQ sur les campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/) pour comprendre le fonctionnement des campagnes sur les fuseaux horaires locaux et les règles de réception/distribution associées.

Les segments ciblés par des campagnes dans le fuseau horaire local doivent comprendre une fenêtre de 2 jours au minimum pour couvrir les utilisateurs de tous les fuseaux horaires. Par exemple, si votre campagne est planifiée pour être envoyée le soir mais qu'elle a une fenêtre de seulement 1 jour, certains utilisateurs peuvent avoir quitté le segment au moment où leur fuseau horaire est atteint. Voici des exemples de filtres qui créent une fenêtre de 2 jours : « dernière utilisation il y a plus d'un jour » et « dernière utilisation il y a moins de 3 jours », ou « premier achat il y a plus de 7 jours » et « premier achat il y a moins de 9 jours ».

### Cas d'utilisation

Les planifications à un moment spécifié conviennent particulièrement aux messages planifiés à l'avance et aux campagnes récurrentes, telles que l'onboarding et la rétention, qui s'exécutent régulièrement pour tous les utilisateurs qualifiés.

## Option 3 : Timing intelligent

Le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) vous permet de diffuser une campagne à chaque utilisateur à un moment différent. Braze calcule le moment optimal pour chaque individu en fonction de ses habitudes d'interaction avec votre application et ses notifications. Vous pouvez également spécifier que les campagnes au timing intelligent ne soient envoyées que pendant une certaine plage horaire de la journée. Par exemple, si vous informez les utilisateurs qu'une promotion se termine à minuit, vous pouvez souhaiter que vos messages soient envoyés à 22 h au plus tard.

![Les options de planification temporelle pour utiliser le timing intelligent afin d'envoyer une campagne au moment où l'utilisation de l'appli est la plus populaire parmi tous les utilisateurs.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Règles de distribution

Étant donné que le moment optimal pour un utilisateur peut se situer à n'importe quelle heure sur 24 heures, toutes les campagnes au timing intelligent doivent être planifiées 24 heures à l'avance. De plus, comme pour les campagnes à moment spécifié, les messages ayant une fenêtre de 1 jour manqueront les utilisateurs qui sortent du segment avant que le moment optimal dans leur fuseau horaire ne soit atteint. Les segments pour les campagnes au timing intelligent doivent intégrer au minimum une fenêtre de 3 jours pour en tenir compte.

Si le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer un moment optimal, vous pouvez choisir une méthode de secours : envoyer le message au moment le plus populaire d'utilisation de l'application parmi tous les utilisateurs, ou bien définir un horaire de secours personnalisé. 

### Cas d'utilisation

Les campagnes au timing intelligent sont idéales pour les messages ponctuels et récurrents qui offrent une certaine flexibilité quant au moment de distribution, c'est-à-dire lorsqu'ils ne sont pas adaptés aux actualités de dernière minute ou aux annonces limitées dans le temps.