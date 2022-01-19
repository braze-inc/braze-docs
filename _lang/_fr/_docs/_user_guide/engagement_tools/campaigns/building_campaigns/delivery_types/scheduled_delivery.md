---
nav_title: Livraison programmée
article_title: Livraison programmée
page_order: 0
page_type: Référence
description: "Cet article de référence décrit les différences entre les options de planification basées sur le temps pour la livraison de la campagne."
tool: Campagnes
---

# Livraison planifiée

Les campagnes envoyées en fonction des délais de livraison sont livrées les jours précisés.

!\[Time-based\]\[3\]

## Option 1 : Envoyer dès que la campagne est lancée

Si vous choisissez d'envoyer un message dès son lancement, votre message commencera à être envoyé dès que vous aurez fini de créer votre campagne.

!\[Immediately\]\[10\]

Ce type de calendrier est conçu pour les campagnes ponctuelles que vous souhaitez envoyer immédiatement, comme les messages sur un événement en cours. Une application sport, par exemple, peut planifier des notifications push sur les mises à jour des scores en utilisant cette option. De plus, lorsque vous envoyez des messages de test destinés à vous ou à votre équipe, cette option vous permet de les livrer immédiatement.

Si vous prévoyez de modifier la campagne et de la renvoyer après avoir consulté le test, Assurez-vous de cocher la case qui fait que les utilisateurs \[re-eligible\]\[24\] pour recevoir la campagne. Par défaut, Braze envoie une campagne à un utilisateur une seule fois sauf si cette case est cochée.

## Option 2 : Envoyer à une heure désignée

Planifier une campagne pour une période désignée vous permet de spécifier les jours et les heures d'envoi de votre campagne. Vous pouvez envoyer un message une fois, quotidien, hebdomadaire ou mensuel à une certaine heure de la journée, ainsi que spécifier quand votre campagne doit commencer et se terminer. Cette date de fin est inclusive, ce qui signifie que le dernier envoi sera à la date de fin.

Si vous sélectionnez **Livraison planifiée** et ne choisissez pas d'envoyer à l'heure locale de l'utilisateur, votre campagne sera envoyée en fonction du fuseau horaire spécifié sur votre page **Paramètres de la société**.

!\[Temps désigné\]\[9\]

### Campagnes de fuseau horaire local

Vous pouvez envoyer le message dans les fuseaux horaires locaux des utilisateurs afin que les membres de votre audience internationale ne reçoivent pas de notification à des moments inopportuns. Les campagnes locales de fuseaux horaires doivent être planifiées 24 heures à l'avance afin de s'assurer que les utilisateurs admissibles de tous les fuseaux horaires puissent les recevoir. Consultez [FAQ Campagnes][25] pour comprendre comment fonctionnent les campagnes locales de fuseau horaire et les règles de livraison associées.

Les segments ciblés sur les campagnes locales de fuseaux horaires devraient inclure, au minimum, une fenêtre de 2 jours pour incorporer les utilisateurs de tous les fuseaux horaires. Par exemple, si votre campagne est programmée pour être envoyée dans la soirée, mais n'a qu'une fenêtre d'1 jour, certains utilisateurs sont peut-être tombés hors du segment lorsque leur fuseau horaire est atteint. Des exemples de filtres qui créent une fenêtre de 2 jours sont "dernière utilisation il y a plus d'un jour" et "dernière utilisation il y a moins de 3 jours" ou "pour la première fois acheté il y a plus de 7 jours" et "acheté il y a moins de 9 jours".

### Cas d'utilisation

Les horaires indiqués sont mieux adaptés aux messages programmés à l'avance et aux campagnes récurrentes, comme l'intégration et la rétention qui fonctionnent régulièrement sur tous les utilisateurs qualifiés.

## Option 3 : Timing intelligent

[Le Timing Intelligent][8] vous permet de livrer une campagne à chaque utilisateur à un moment différent. Braze calcule l'heure de chaque personne en fonction du moment où cet utilisateur s'engage généralement avec votre application et ses notifications. Vous pouvez éventuellement spécifier que les campagnes Intelligent Timing n'envoient que pendant une certaine partie de la journée. Par exemple, si vous avertissez les utilisateurs d'une promotion qui se termine à minuit, il est possible que vos messages soient envoyés au plus tard à 22h.

!\[Intelligent Timing\]\[14\]

### Règles de livraison

Parce que le temps optimal d'un utilisateur peut être à n'importe quel moment au cours de 24 heures, toutes les campagnes de Timing Intelligent doivent être planifiées 24 heures à l'avance. En outre, similaire aux campagnes de temps désigné, avec une fenêtre de 1 jour manquera les utilisateurs qui sortent du segment avant que leur temps optimal dans leur fuseau horaire soit atteint. Les segments pour les campagnes intelligentes de Timing devraient inclure au minimum une fenêtre de 3 jours pour rendre compte de cela.

Si le profil d'un utilisateur n'a pas assez de données pour calculer un temps optimal, vous pouvez choisir une méthode de sauvegarde à envoyer pendant la période la plus populaire pour utiliser l'application parmi tous les utilisateurs ou un temps de repli personnalisé défini.

### Cas d'utilisation

Les campagnes intelligentes de Timing fonctionnent mieux pour les messages ponctuels et récurrents où il y a une certaine flexibilité en ce qui concerne le délai de livraison, par exemple quand elles ne sont pas bien adaptées pour les nouvelles ou les annonces chronométrées.
[3]: {% image_buster /assets/img_archive/time_based.png %} [9]: {% image_buster /assets/img_archive/schedule_designated.png %} [10]: {% image_buster /assets/img_archive/schedule_immediately. ng %} [14]: {% image_buster /assets/img_archive/schedule_intelligent.png %} [24]: {% image_buster /assets/img_archive/Religible. ng %} [34]: {% image_buster /assets/img_archive/customEventProperties.png %}

[8]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[25]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/
