---
nav_title: "Documentation de conformité pour les services d'envoi de messages mobiles"
article: Compliance Documentation for Mobile Messages Services
permalink: /compliance_documentation_sms/
description: "Documentation de conformité relative aux canaux de communication mobiles."
page_order: 2
noindex: true
---

# Documentation de conformité pour les services d'envoi de messages mobiles ("canal de communication")

_Date de révision: 9 décembre 2024_

_(En vigueur à partir de la date de révision ; sous réserve de modifications)_

Les conditions supplémentaires suivantes s'appliquent à l'utilisation par le client du canal de messages mobiles :

## Définitions

**" Agrégateurs ",** **" Transporteurs "** ou **" Intermédiaires de messages mobiles "** désigne les intermédiaires tiers (i) qui transmettent les messages mobiles entre les fournisseurs de messages mobiles et les transporteurs ; (ii) qui sont des fournisseurs de services sans fil (e.g., T-Mobile, AT&T, etc.) ; et/ou (iii) qui sont impliqués dans les transmissions de messages RCS des fournisseurs de messages mobiles vers les utilisateurs finaux.

Les **fournisseurs de SMS/MMS** ou **fournisseurs de messages mobiles** désignent les sous-traitants de Braze utilisés pour la transmission de SMS, MMS et/ou messages RCS, tels qu'identifiés à l'[adressewww.braze.com](http://www.braze.com/subprocessors)/subprocessors.

On entend par **"messages SMS/MMS"** ou **"messages mobiles"** les messages SMS, MMS et/ou RCS.

## Normes industrielles et bonnes pratiques

Lorsqu'ils envoient des messages mobiles, les clients doivent se conformer aux politiques d'utilisation acceptable et d'envoi de messages applicables des fournisseurs de messages mobiles, aux normes et directives sectorielles applicables et, le cas échéant, aux codes sectoriels et aux directives des intermédiaires de messages mobiles applicables pour tout pays où le client a l'intention d'envoyer des messages mobiles, comme indiqué plus en détail dans la [politique d'utilisation acceptable de](https://www.braze.com/company/legal/aup/) Braze.

Les tiers impliqués dans l'envoi de messages mobiles, y compris les intermédiaires de messages mobiles, peuvent imposer des frais ou des pénalités en fonction des messages mobiles envoyés en violation de leurs conditions ou des lois applicables. Le Client est responsable du paiement des frais et des pénalités résultant de la violation par le Client de ces conditions de tiers, que ces frais ou pénalités soient imposés au Client ou à Braze.

## Sous-processeurs

Braze peut utiliser tout fournisseur de messages mobiles figurant sur sa liste de sous-traitants secondaires à l'adresse [www.braze.com/subprocessors.](https://www.braze.com/subprocessors/)

Nonobstant ce qui précède, dans le cas où le Client envoie des Messages mobiles en utilisant le modèle " Bring Your Own (BYO) SMS Connector ", les Fournisseurs de messages mobiles impliqués dans l'envoi seront considérés comme des Fournisseurs tiers (tels que définis dans l'Accord) et non comme des Sous-traitants de Braze, et les clauses de non-responsabilité ci-dessous s'appliqueront à ces Fournisseurs tiers.

## Conditions d'exception pour l'utilisation de webhook

Applicable aux Clients qui ont souscrit à des crédits de messages à compter du 9 décembre 2024 (selon la date d'entrée en vigueur du Bon de commande) : les restrictions décrites dans la documentation sur la conformité du canal webhooks ne s'appliquent pas à l'utilisation de webhooks pour l'envoi de messages mobiles par l'intermédiaire d'une plateforme d'un fournisseur tiers vers des destinations identifiées comme " SMS/MMS Global " dans le tableau de ratio de crédit applicable pour les crédits de messages.

## Apportez votre propre connecteur SMS (BYO)

Les clients peuvent envoyer des messages mobiles à partir de Braze en utilisant des fournisseurs tiers grâce au modèle "BYO SMS Connector". Nonobstant ce qui précède, les personnalisés ne doivent pas utiliser le modèle BYO SMS Connector pour envoyer des messages mobiles aux États-Unis et au Canada. 

## Clauses de non-responsabilité

Braze décline toute représentation, garantie, responsabilité et obligation d'indemnisation à l'égard de tout fournisseur tiers ou intermédiaire de messages mobiles impliqué dans l'envoi ou le traitement des messages mobiles, y compris la responsabilité liée à la capacité du système, au débit des messages ou à la réception/distribution effective sur l'appareil d'un utilisateur final.

## Conditions générales

Sans limiter la généralité des obligations de tout Client en vertu de l'Accord, et pour éviter tout doute, le Client est seul responsable de l’obtention de tous les droits, consentements et autorisations nécessaires et de la fourniture des avis de confidentialité adéquats d’un point de vue légal, en relation avec son utilisation de ce Canal, ainsi que de l’obtention de tous les consentements et autorisations légalement requis pour envoyer ou recevoir, selon le cas, des Messages via ce Canal.