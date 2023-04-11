---
nav_title: Livraison planifiée
article_title: Livraison planifiée
page_order: 0
page_type: reference
description: "Le présent article de référence décrit les différences entre les options de planification temporelle pour la livraison de campagnes."
tool: Campaigns

---

# Livraison planifiée

Les campagnes envoyées à l’aide d’une livraison planifiée temporellement sont livrées à des jours spécifiés.

![][3]

## Option 1 : Envoyer dès que la campagne est lancée

Si vous choisissez d’envoyer un message dès qu’elle est lancée, il commencera à se lancer dès que vous aurez fini de créer votre campagne.

![][10]

Ce type de planification est conçu pour les campagnes ponctuelles que vous souhaitez envoyer immédiatement, telles que les messages concernant un événement en cours. Une application sportive, par exemple, peut planifier des notifications push basées sur les mises à jour des scores en utilisant cette option. En outre, lorsque vous envoyez des messages de test destinés à vous-même ou à votre équipe, cette option vous permet de les livrer immédiatement. 

Si vous prévoyez de modifier la campagne et de la réexpédier après avoir affiché le test, assurez-vous de cocher la case qui permet aux utilisateurs d’êtres [rééligibles][24] à la réception de la campagne. Par défaut, Braze envoie une seule fois une campagne à un utilisateur à moins que cette case ne soit cochée.

## Option 2 : Envoyer à un moment spécifié

La planification d’une campagne à un moment spécifié vous permet de stipuler les jours et les heures auxquels votre campagne sera envoyée. Vous pouvez envoyer un message une fois, une fois par jour, une fois par semaine ou une fois par mois à un certain moment de la journée ainsi que préciser quand votre campagne doit commencer et se terminer. Cette date de fin est inclusive, ce qui signifie que le dernier envoi se fera à la date de fin. 

Si vous sélectionnez **Livraison planifiée** et ne choisissez pas d’envoyer à l’heure locale de l’utilisateur, votre campagne sera envoyée conformément au fuseau horaire spécifié sur votre page **Paramètres de la société**.

![][9]

### Campagnes dans le fuseau horaire local

Vous pouvez envoyer le message dans les fuseaux horaires locaux des utilisateurs afin que les membres de votre audience internationale ne reçoivent pas de notification à des moments inopportuns. Les campagnes dans le fuseau horaire local doivent être planifiées 24 heures à l’avance pour garantir que les utilisateurs éligibles de tous les fuseaux horaires puissent les recevoir. Consultez les [FAQ de campagne][25] pour comprendre comment fonctionnent les campagnes dans le fuseau horaire local ainsi que les règles de livraison associées.

Les segments ciblés par des campagnes dans le fuseau horaire local doivent comprendre une fenêtre de 2 jours au minimum pour incorporer les utilisateurs de tous les fuseaux. Par exemple, si votre campagne est planifiée pour être envoyée le soir mais qu’elle a une fenêtre de seulement 1 jour, certains utilisateurs peuvent avoir quitté le segment lorsque leur fuseau horaire est atteint. Des exemples de filtres qui créent une fenêtre de 2 jours sont « dernière utilisation il y a plus d’un jour » et « dernière utilisation il y a moins de 3 jours » ou « premier achat il y a plus de 7 jours » et « premier achat il y a moins de 9 jours »."

### Cas d’utilisation

Les planifications temporelles spécifiées conviennent mieux aux messages planifiés à l’avance et aux campagnes récurrentes, telles que l’onboarding et la rétention, qui s’exécutent régulièrement pour tous les utilisateurs qualifiés.

## Option 3 : Timing Intelligent

Le [Timing intelligent][8] vous permet de proposer une campagne à chaque utilisateur à un moment différent. Braze calcule le temps pour chaque individu en fonction du moment où l’utilisateur s’engage généralement avec votre application et ses notifications. Vous pouvez éventuellement spécifier que les campagnes au timing intelligent ne soient envoyées qu’à un certain moment de la journée. Par exemple, si vous informez les utilisateurs qu’une promotion se termine à minuit, vous pouvez souhaiter que vos messages soient envoyés à 22 h au plus tard.

![][14]

### Règles de livraison

Étant donné que l’heure optimale pour un utilisateur peut être à tout moment sur 24 heures, toutes les campagnes de timing intelligent doivent être planifiées 24 heures à l’avance. De plus, comme pour les campagnes spécifiées temporellement, les messages ayant une fenêtre de 1 jour manqueront les utilisateurs qui sortent du segment avant que la période optimale de leur fuseau horaire soit atteinte. Les segments pour les campagnes au timing intelligent doivent incorporer au minimum une fenêtre de 3 jours pour en tenir compte.

Si le profil utilisateur ne dispose pas de suffisamment de données pour calculer un temps optimal, vous pouvez choisir une méthode de secours pour envoyer le message au moment le plus populaire d’utilisation de l’application au sein de tous les utilisateurs ou bien régler un temps de secours personnalisé. 

### Cas d’utilisation

Les campagnes au timing intelligent fonctionnent mieux pour les messages ponctuels et récurrents qui disposent d’une certaine flexibilité concernant le temps de livraison, par exemple lorsqu’ils ne sont pas parfaitement adaptés aux actualités ou aux annonces limitées dans le temps.

[3]: {% image_buster /assets/img_archive/time_based.png %}
[7]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[9]: {% image_buster /assets/img_archive/schedule_designated.png %}
[10]: {% image_buster /assets/img_archive/schedule_immediately.png %}
[14]: {% image_buster /assets/img_archive/schedule_intelligent.png %}
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
[25]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
