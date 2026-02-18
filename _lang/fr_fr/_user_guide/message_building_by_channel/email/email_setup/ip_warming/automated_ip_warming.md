---
nav_title: IP warming automatisé
article_title: IP warming automatisé
page_order: 1
page_type: reference
description: "Cet article de référence traite du réchauffement d'adresses IP automatisé et de la manière de surveiller votre réchauffement d'adresses IP."
channel: email
---

# IP warming automatisé

> Utilisez le réchauffement d'adresses IP automatisé pour augmenter progressivement le volume d'e-mails à partir d'une nouvelle adresse IP afin de créer une réputation d'expéditeur auprès des fournisseurs de boîtes de réception.

{% include early_access_beta_alert.md feature='Automated IP warming' %}

## Fonctionnement

Vous pouvez utiliser le réchauffement d'adresses IP automatisé pour augmenter progressivement votre volume d'envoi quotidien, ce qui permet aux fournisseurs de boîtes de réception d'apprendre et de faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la tuile **Réchauffement** **IP automatisé** dans la section **Reprendre là où vous vous êtes arrêté de** votre tableau de bord d'accueil, et cette tuile reste ici pendant 60 jours.

Braze envoie d'abord à vos abonnés les plus engagés, ce qui permet au volume quotidien d'augmenter à un rythme correspondant aux meilleures pratiques. Ensuite, Braze suit les signaux d'engagement et de livrabilité. Si Braze détecte un problème, le système ajuste automatiquement votre planification.

{% alert note %}
Vous ne pouvez effectuer qu'un seul réchauffement d'adresses IP.
{% endalert %}

## Conditions préalables

Pour effectuer un réchauffement d'adresses IP automatisé, vous devez disposer des éléments suivants :

- Sous-domaine vérifié et adresses IP actives
- Permissions d'afficher et de lancer un échauffement IP
    - "Voir les données d'utilisation" pour consulter la section sur le réchauffement IP.
    - "Voir les modèles d'e-mail" pour afficher et sélectionner les modèles d'e-mail pour le réchauffement d'adresses IP.
    - "Gérer les paramètres de l'e-mail" pour lancer le préchauffage de l'IP.
- "Campagnes d'accès" 
- "Approuver et refuser les campagnes" si le flux de travail d'approbation des campagnes est activé. 
    - Braze approuve automatiquement les campagnes créées à partir du réchauffement d'adresses IP automatisé en votre nom.

## Mettre en place un plan de réchauffement d'adresses IP automatisé

### Étape 1 : Fixer une planification

1. Dans la section **Informations d'envoi**, sélectionnez l'**adresse De** pour réchauffer les adresses IP.
2. Saisissez le volume d'envoi quotidien actuel et le volume d'envoi cible.
3. Sélectionnez la date de début du réchauffement d'adresses IP automatisé. Cette date doit se situer au moins un jour après le lancement du plan.
4. Saisissez l'heure d'envoi. Les messages sont ainsi envoyés dans le fuseau horaire de l'entreprise.
5. Sélectionnez **Next : Segments** pour poursuivre la configuration.

![Exemple de détails de planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et classer les segments

1. Sélectionnez ensuite les segmentations à cibler. Pendant le réchauffement d'adresses IP, Braze commence à envoyer à vos utilisateurs les plus engagés et augmente progressivement le volume d'envoi au fil du temps et ajoute peu à peu des segments moins engagés. 
2. Ensuite, glissez-déposez les segments pour les classer de l'engagement le plus élevé à l'engagement le plus faible. Un taux d'engagement élevé comprend les destinataires qui ouvrent et cliquent régulièrement sur vos e-mails. Les destinataires à faible taux d'engagement sont ceux qui ne s'engagent pas régulièrement dans vos e-mails ou qui ne s'y sont pas engagés depuis très longtemps.
3. Sélectionnez **Next : Messages** pour poursuivre la configuration.

![Deux segments ont été sélectionnés pour le réchauffement d'adresses IP automatisé.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Étape 3 : Sélectionnez les messages à envoyer

1. Sélectionnez **Sélectionner les modèles d'e-mail**.
2. Choisissez les modèles d'e-mail pour les messages à envoyer. Le contenu que vous envoyez pendant le réchauffement d'adresses IP doit encourager les ouvertures et les clics. Nous vous recommandons de choisir un contenu qui a été bien accueilli dans le passé. Par exemple, vous pouvez utiliser des offres promotionnelles pour encourager l'engagement immédiat et les achats.
3. Sélectionnez **Sélectionner les modèles**. Braze calcule le nombre de modèles requis avant que vous ne puissiez lancer l'opération. Nous vous recommandons de fournir plus de modèles que le minimum requis pour permettre au système de s'adapter aux problèmes de livrabilité sans s'arrêter.
4. Après avoir ajouté le nombre requis de modèles, sélectionnez **Next : Résumé**.

{% alert important %}
Les modifications apportées aux campagnes créées à partir de l'outil de réchauffement IP (telles que la modification de la date de planification, du segment, du volume) ne seront pas reflétées sur la page **récapitulative** du réchauffement IP.
{% endalert %}

### Étape 4 : Vérifier et lancer le test

Passez en revue les détails de votre plan de réchauffement d'adresses IP. Sélectionnez ensuite **Lancer**.

## Pendant le réchauffement d'adresses IP actives

Les campagnes de réchauffement d'adresses IP sont créées 1 à 2 jours à l'avance, sauf si vous lancez un réchauffement d'adresses IP le lendemain. Ces campagnes sont automatiquement nommées avec le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif d'envoi quotidien ciblé est atteint, le système arrête l'envoi pour cette journée afin de protéger votre réputation. 

Le système surveille votre santé sur la base des critères de référence suivants : 

- Taux de réception/distribution inférieur ou égal à 90%.
- Taux d'ouverture inférieur à 10%.
- Rebonds supérieurs à 5
- Taux de plaintes pour spam supérieur à 0,1

Si les statistiques sont inférieures à nos critères de référence, le système retient le volume le lendemain au lieu de l'augmenter afin de limiter les risques pour la réputation de votre expéditeur.

## Arrêter un plan d'échauffement IP

Braze vous permet d'arrêter le réchauffement d'adresses IP et la création de futures campagnes, mais si une campagne est déjà active ou planifiée pour les 24 à 48 heures à venir, il se peut que vous deviez arrêter la campagne spécifique manuellement. L'arrêt d'un plan de réchauffement d'adresses IP entraîne également l'arrêt de toutes les campagnes associées.

Cependant, lorsqu'il est arrêté, le préchauffage de l'IP ne peut pas être repris. Au lieu de cela, vous devez établir un nouveau plan pour reprendre là où vous vous étiez arrêté :

- Téléchargement des données existantes pour votre plan arrêté à conserver pour vos archives, car dès que vous commencerez un nouvel échauffement IP, le traceur précédent sera supprimé.
- Mise à jour du **volume d'envoi quotidien actuel** par rapport au volume le plus récent
- Ajout d'un filtre à un segment si vous envisagez d'utiliser le même segment que celui du dernier IP warmup en excluant les utilisateurs qui ont déjà reçu des campagnes antérieures.

## Lorsqu'un préchauffage IP est terminé

Le réchauffement d'adresses IP est marqué comme terminé lorsque le dernier jour de réchauffement d'adresses IP se termine à minuit dans le fuseau horaire de votre entreprise. Par exemple, si la dernière campagne envoyée dans le cadre du plan de réchauffement d'adresses IP est envoyée à 20 heures, le plan est marqué comme terminé après quatre heures.

Le tracker reste sur la page d'accueil pendant 90 jours après la fin du plan. Après 90 jours, le traceur est retiré. Le téléchargement des données inclut les indicateurs standards de l'e-mail :

- _Envoyé_	
- _Délivré_	
- _Rebonds_	
- _Signalement de courrier indésirable_	
- _Nombre total d’ouvertures_	
- _Ouverture unique_	
- _Cliqué_	
- _Désabonné_

Si une journée comprend plusieurs campagnes utilisées pour répondre à des exigences de volume, celles-ci sont agrégées dans la vue quotidienne.

![Suivi du réchauffement d'adresses IP avec le volume d'envoi pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})