---
nav_title: IP warming automatisé
article_title: IP warming automatisé
page_order: 1
page_type: reference
description: "Cet article de référence traite du réchauffement d’adresses IP automatisé et explique comment surveiller votre réchauffement d’adresses IP."
channel: email
---

# IP warming automatisé

> Utilisez le réchauffement d’adresses IP automatisé pour augmenter progressivement le volume d'e-mails provenant d'une nouvelle adresse IP afin de créer la réputation de l’expéditeur auprès des fournisseurs de boîtes de réception.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Fonctionnement

Vous pouvez utiliser le réchauffement d’adresses IP automatisé pour augmenter progressivement votre volume d'envoi quotidien, ce qui permet aux fournisseurs de boîtes de réception d'apprendre à connaître et à faire confiance à vos habitudes d'envoi. Lorsque vous ajoutez un domaine à votre espace de travail, vous pouvez sélectionner la vignette **« Réchauffement d’adresses IP automatisé** » dans la section **« Pick up where you left off** » (Reprenez là où vous vous êtes arrêté) de votre tableau de bord d'accueil. Cette vignette restera affichée pendant 60 jours.

Braze envoie d'abord vos messages aux utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien d'augmenter à un rythme conforme aux meilleures pratiques. Ensuite, Braze suit les signaux d'engagement et de livrabilité. Si Braze détecte un problème, le système ajuste automatiquement votre planification.

{% alert note %}
Vous ne pouvez effectuer qu'un seul réchauffement d’adresses IP.
{% endalert %}

## Conditions préalables

Pour effectuer un réchauffement d’adresses IP automatisé, vous devez disposer des éléments suivants :

- Sous-domaine vérifié et adresses IP actives
- Autorisations pour afficher et lancer un préchauffage IP
    - Veuillez consulter la section « Afficher les données d’utilisation » pour examiner la section relative au réchauffement d’adresses IP.
    - Veuillez consulter les modèles d'e-mails pour visualiser et sélectionner les modèles d'e-mails destinés au réchauffement d’adresses IP.
    - Veuillez gérer les paramètres de e-mail pour initier le préchauffage IP.
- « Campagnes d'accès » 
- « Approuver et refuser les campagnes » si le processus d'approbation des campagnes est activé. 
    - Braze approuve automatiquement les campagnes créées à partir du réchauffement d’adresses IP automatisé en votre nom.

## Mettre en place un plan de réchauffement d’adresses IP automatisé

### Étape 1 : Établir une planification

1. Dans la section **Envoi d'informations**, veuillez sélectionner l'**adresse** **d'expéditeur** pour le réchauffement d’adresses IP.
2. Veuillez indiquer le volume quotidien actuel et le volume cible.
3. Veuillez sélectionner la date de début du réchauffement d’adresses IP automatisé. Cette date doit être au moins un jour après le lancement du plan.
4. Veuillez saisir l'heure d'envoi. Cela permet d'envoyer les messages dans le fuseau horaire de l'entreprise.
5. Sélectionnez **Next : Segments** pour poursuivre la configuration.

![Exemple de détails de la planification.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Étape 2 : Sélectionner et réaliser le classement des segments

1. Ensuite, veuillez sélectionner les segments à cibler. Pendant le réchauffement d’adresses IP, Braze commence par envoyer des messages à vos utilisateurs les plus engagés, puis augmente progressivement le volume d'envoi au fil du temps et ajoute lentement des segments moins engagés. 
2. Ensuite, veuillez glisser-déposer les segments afin de les classer par ordre décroissant d'engagement. Un engagement élevé inclut les destinataires qui ouvrent et cliquent régulièrement sur vos e-mails. Un faible engagement concerne les destinataires qui ne sont pas réguliers dans leur interaction avec vos e-mails ou qui n'ont pas interagi avec vos e-mails depuis très longtemps.
3. Sélectionnez **Next : Veuillez** continuer la configuration.

![Deux segments ont été sélectionnés pour faire l'objet d'un ciblage pour le réchauffement d’adresses IP automatisé.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Étape 3 : Veuillez sélectionner les messages à envoyer.

1. Veuillez sélectionner **les modèles d'e-mails**.
2. Veuillez sélectionner les modèles d'e-mails pour les messages à envoyer. Le contenu que vous envoyez pendant le réchauffement d’adresses IP doit encourager les ouvertures et les clics. Nous vous recommandons de sélectionner du contenu qui a déjà reçu un accueil favorable par le passé. Par exemple, vous pouvez utiliser des offres promotionnelles pour encourager l'engagement immédiat et les achats.
3. Veuillez sélectionner** les modèles**. Braze évalue le nombre de modèles nécessaires avant que vous puissiez procéder au lancement. Nous recommandons de fournir davantage de modèles que le minimum requis afin de permettre au système de s'adapter aux problèmes de livrabilité sans interruption.
4. Après avoir ajouté le nombre requis de modèles, veuillez sélectionner **Suivant : Résumé**.

{% alert important %}
Les modifications apportées aux campagnes créées à partir de l'outil de réchauffement d’adresses IP (telles que la modification de la date de planification, du segment, du volume) ne seront pas reflétées sur la page **Résumé** du réchauffement d’adresses IP.
{% endalert %}

### Étape 4 : Vérifier et lancer le test

Veuillez examiner les détails de votre plan de réchauffement d’adresses IP. Ensuite, veuillez sélectionner **Lancer**.

## Pendant le réchauffement actif d’adresses IP

Les campagnes de réchauffement d’adresses IP sont créées 1 à 2 jours à l’avance, sauf si vous lancez un réchauffement d’adresses IP le lendemain. Ces campagnes sont automatiquement nommées selon le format suivant : `IP Warming Day [X] - [Date] - [Template Name]`.

Lorsque l'objectif quotidien d'envoi est atteint, le système cesse d'envoyer des messages pour la journée afin de préserver votre réputation. 

Le système surveille votre santé en se basant sur les critères de référence suivants : 

- Le taux de réception/distribution diminue de 90 % ou moins
- Taux d’ouverture inférieur à 10 %
- Rebonds supérieurs à 5 %
- Taux de plaintes pour spam supérieur à 0,1 %

Si les statistiques sont inférieures à nos critères de référence, le système maintient le volume le lendemain au lieu de l'augmenter afin de limiter les risques pour la réputation de l’expéditeur.

## Veuillez interrompre le plan de préchauffage IP.

Braze vous permet d'interrompre le réchauffement d’adresses IP et la création de futures campagnes. Toutefois, si une campagne est déjà active ou en phase de planification pour les prochaines 24 à 48 heures, il peut être nécessaire d'interrompre manuellement la campagne en question. L'arrêt d'un plan de réchauffement d’adresses IP entraîne également l'arrêt de toutes les campagnes associées.

Cependant, une fois interrompu, le préchauffage IP ne peut pas être repris. Au lieu de cela, il est nécessaire de mettre en place un nouveau plan pour reprendre là où vous vous êtes arrêté en :

- Veuillez télécharger les données existantes de votre plan interrompu afin de les conserver dans vos archives, car une fois que vous lancerez un nouveau réchauffement IP, l'ancien tracker sera supprimé.
- Mise à jour du **volume quotidien actuel** vers le volume le plus récent
- Ajouter un filtre à un segment si vous envisagez d'utiliser le même segment que lors du dernier préchauffage IP en excluant les utilisateurs qui ont déjà reçu des campagnes précédentes.

## Lorsqu'un préchauffage IP est terminé

Le réchauffement d’adresses IP est considéré comme terminé lorsque le dernier jour du réchauffement d’adresses IP prend fin à minuit, heure locale de votre entreprise. Par exemple, si la dernière campagne envoyée dans le cadre du plan de réchauffement d’adresses IP est envoyée à 20 h, le plan est alors marqué comme terminé après quatre heures.

Le suivi reste sur la page d'accueil pendant 90 jours après la fin du plan. Au bout de 90 jours, le dispositif de suivi est retiré. Le téléchargement des données comprend les indicateurs de performance clés (KPI) standard suivants pour les e-mails :

- _Envoyé_	
- _Délivré_	
- _Rebonds_	
- _Signalement de courrier indésirable_	
- _Nombre total d’ouvertures_	
- _Ouverture unique_	
- _Cliqué_	
- _Désabonné_

Si une journée comprend plusieurs campagnes utilisées pour répondre aux exigences de volume, celles-ci sont regroupées dans la vue quotidienne.

![Suivi du réchauffement d’adresses IP avec volume envoyé pour la semaine du 16 janvier.]({% image_buster /assets/img/automated_ip_warming_example.png %})