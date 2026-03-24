---
nav_title: IP warming automatisé
article_title: IP warming automatisé
page_order: 1
page_type: reference
description: "Cet article de référence traite du réchauffement d'adresses IP automatisé et explique comment surveiller votre réchauffement d'adresses IP."
channel: email
---

# IP warming automatisé

> Utilisez le réchauffement d'adresses IP automatisé pour augmenter progressivement le volume d'e-mails envoyés depuis une nouvelle adresse IP et ainsi construire votre réputation de l'expéditeur auprès des fournisseurs de boîtes de réception.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Fonctionnement

Le réchauffement d'adresses IP automatisé vous permet d'augmenter progressivement votre volume d'envoi quotidien, afin que les fournisseurs de boîtes de réception apprennent à connaître et à faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la vignette **Automated IP Warming** dans la section **Pick up where you left off** de votre tableau de bord d'accueil. Cette vignette reste affichée pendant 60 jours.

Braze envoie d'abord vos messages aux utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien d'augmenter à un rythme conforme aux meilleures pratiques. Braze suit ensuite les signaux d'engagement et de livrabilité. Si un problème est détecté, le système ajuste automatiquement votre planification.

{% alert note %}
Vous ne pouvez effectuer qu'un seul réchauffement d'adresses IP.
{% endalert %}

## Conditions préalables

Pour effectuer un réchauffement d'adresses IP automatisé, vous devez disposer des éléments suivants :

- Un sous-domaine vérifié et des adresses IP actives
- Les autorisations nécessaires pour afficher et lancer un réchauffement d'adresses IP
    - « View Usage Data » pour consulter la section relative au réchauffement d'adresses IP
    - « View Email Templates » pour visualiser et sélectionner les modèles d'e-mails destinés au réchauffement d'adresses IP
    - « Manage Email Settings » pour lancer le réchauffement d'adresses IP
- « Access Campaigns » 
- « Approve and Deny Campaigns » si le processus d'approbation des campagnes est activé 
    - Braze approuve automatiquement les campagnes créées à partir du réchauffement d'adresses IP automatisé en votre nom.

## Mettre en place un plan de réchauffement d'adresses IP automatisé

### Étape 1 : Établir une planification

1. Dans la section **Sending information**, sélectionnez l'adresse **From address** pour laquelle réchauffer les adresses IP.
2. Saisissez le volume d'envoi quotidien actuel et le volume cible.
3. Sélectionnez la date de début du réchauffement d'adresses IP automatisé. Cette date doit être au moins un jour après le lancement du plan.
4. Saisissez l'heure d'envoi. Les messages seront envoyés dans le fuseau horaire de votre entreprise.
5. Sélectionnez **Next: Segments** pour poursuivre la configuration.

![Exemple de détails de la planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et classer les segments

1. Sélectionnez ensuite les segments à cibler. Pendant le réchauffement d'adresses IP, Braze commence par envoyer des messages à vos utilisateurs les plus engagés, puis augmente progressivement le volume d'envoi au fil du temps en ajoutant petit à petit des segments moins engagés. 
2. Glissez-déposez les segments afin de les classer par ordre décroissant d'engagement. Un engagement élevé correspond aux destinataires qui ouvrent et cliquent régulièrement sur vos e-mails. Un faible engagement concerne les destinataires dont les interactions avec vos e-mails sont irrégulières, ou qui n'ont pas interagi avec vos e-mails depuis très longtemps.
3. Sélectionnez **Next: Messages** pour poursuivre la configuration.

![Deux segments sélectionnés pour le ciblage du réchauffement d'adresses IP automatisé.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Étape 3 : Sélectionner les messages à envoyer

1. Sélectionnez **Select email templates**.
2. Choisissez les modèles d'e-mails pour les messages à envoyer. Le contenu envoyé pendant le réchauffement d'adresses IP doit encourager les ouvertures et les clics. Nous vous recommandons de choisir du contenu qui a déjà reçu un accueil favorable par le passé. Par exemple, vous pouvez utiliser des offres promotionnelles pour encourager l'engagement immédiat et les achats.
3. Sélectionnez **Select templates**. Braze calcule le nombre de modèles nécessaires avant que vous puissiez procéder au lancement. Nous recommandons de fournir davantage de modèles que le minimum requis afin de permettre au système de s'adapter aux problèmes de livrabilité sans interruption.
4. Après avoir ajouté le nombre requis de modèles, sélectionnez **Next: Summary**.

{% alert important %}
Les modifications apportées aux campagnes créées à partir de l'outil de réchauffement d'adresses IP (telles que la modification de la date de planification, du segment ou du volume) ne seront pas reflétées sur la page **Summary** du réchauffement d'adresses IP.
{% endalert %}

### Étape 4 : Vérifier et lancer

Examinez les détails de votre plan de réchauffement d'adresses IP, puis sélectionnez **Launch**.

## Pendant le réchauffement actif d'adresses IP

Les campagnes de réchauffement d'adresses IP sont créées 1 à 2 jours à l'avance, sauf si vous lancez un réchauffement d'adresses IP le lendemain. Ces campagnes sont automatiquement nommées selon le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif quotidien d'envoi est atteint, le système cesse d'envoyer des messages pour la journée afin de préserver votre réputation. 

Le système surveille la santé de vos envois en se basant sur les critères de référence suivants : 

- Taux de distribution inférieur ou égal à 90 %
- Taux d'ouverture inférieur à 10 %
- Rebonds supérieurs à 5 %
- Taux de signalement de courrier indésirable supérieur à 0,04 %

Si les statistiques sont en dessous de ces critères, le système maintient le volume le lendemain au lieu de l'augmenter, afin de limiter les risques pour votre réputation de l'expéditeur.

## Interrompre un plan de réchauffement d'adresses IP

Braze vous permet d'interrompre le réchauffement d'adresses IP et la création de futures campagnes. Toutefois, si une campagne est déjà active ou planifiée pour les prochaines 24 à 48 heures, il peut être nécessaire de l'interrompre manuellement. L'arrêt d'un plan de réchauffement d'adresses IP entraîne également l'arrêt de toutes les campagnes associées.

Une fois interrompu, le réchauffement d'adresses IP ne peut pas être repris. Vous devez mettre en place un nouveau plan pour reprendre là où vous vous êtes arrêté en :

- Téléchargeant les données existantes de votre plan interrompu afin de les conserver dans vos archives, car une fois que vous lancerez un nouveau réchauffement d'adresses IP, l'ancien suivi sera supprimé
- Mettant à jour le **Current daily send volume** avec le volume le plus récent
- Ajoutant un filtre à un segment si vous envisagez d'utiliser le même segment que lors du dernier réchauffement d'adresses IP, en excluant les utilisateurs qui ont déjà reçu des campagnes précédentes

## Lorsqu'un réchauffement d'adresses IP est terminé

Le réchauffement d'adresses IP est considéré comme terminé lorsque le dernier jour du réchauffement prend fin à minuit dans le fuseau horaire de votre entreprise. Par exemple, si la dernière campagne envoyée dans le cadre du plan de réchauffement est envoyée à 20 h, le plan est marqué comme terminé quatre heures plus tard.

Le suivi reste sur la page d'accueil pendant 90 jours après la fin du plan. Au bout de 90 jours, il est supprimé. Le téléchargement des données comprend les indicateurs e-mail standard suivants :

- _Envoyé_	
- _Distribué_	
- _Rebonds_	
- _Signalements de courrier indésirable_	
- _Nombre total d'ouvertures_	
- _Ouvertures uniques_	
- _Cliqué_	
- _Désabonné_

Si une journée comprend plusieurs campagnes utilisées pour atteindre les exigences de volume, celles-ci sont regroupées dans la vue quotidienne.

![Suivi du réchauffement d'adresses IP avec le volume d'envoi pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})