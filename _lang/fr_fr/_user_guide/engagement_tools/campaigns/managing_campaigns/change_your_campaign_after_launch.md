---
nav_title: Modification de votre campagne après le lancement
article_title: Modification de votre campagne après le lancement
page_order: 1
tool: Campaigns
page_type: reference
description: "Le présent article de référence donne un aperçu du résultat de la modification de certains aspects d’une campagne après son lancement."

---

# Modification de votre campagne après le lancement

> Le présent article donne un aperçu du résultat de la modification de certains aspects d’une campagne après son lancement.

## Arrêter votre campagne

Pour arrêter une campagne, ouvrez la page des **détails de votre campagne** et sélectionnez **Arrêter la campagne**. Lorsqu’une campagne est arrêtée :

- Les messages dont l'envoi est planifié sont annulés.
- Les tests A/B dont le test initial a déjà été envoyé seront définitivement annulés.
- Les événements relatifs aux messages déjà envoyés (par exemple, les clics d'ouverture) feront toujours l'objet d'un suivi.

Pour relancer votre campagne, sélectionnez **Reprendre**. Votre campagne continuera d'envoyer des messages et des tests A/B, mais les messages manqués ne seront pas réenvoyés ou replanifiés.

## Campagnes déclenchées

Toutes les modifications apportées aux campagnes de livraison par événement et aux campagnes de réception/distribution déclenchées par l'API prennent effet immédiatement pour les envois de type "go-forward". 

Si ces campagnes ont été déclenchées mais n'ont pas encore été envoyées (par exemple, une campagne de livraison/distribution avec un délai d'un jour est modifiée pendant la période de délai d'un jour), reportez-vous aux conseils suivants pour les campagnes planifiées.

### Campagnes planifiées

Si vous devez apporter des modifications à une campagne après son lancement, prenez note des éléments suivants lors de la modification de votre campagne pour vérifier que vos modifications ont les effets souhaités.

### Contenu du message

Toute modification du contenu des messages (y compris les titres, les corps et les images) prend effet immédiatement après avoir été enregistrée pour tous les envois de messages à venir. Il n'est pas possible de modifier le contenu des messages qui ont déjà été envoyés.

### Planification et audience

Si vous modifiez l’heure d’envoi planifiée de votre campagne ou son audience, ces changements sont reflétés immédiatement dans la campagne réelle.

### Taux d’envoi

Lorsque vous utilisez une limitation du taux d’envoi, Braze « planifie » vos messages dans des créneaux horaires avec une granularité à l’échelle de la minute, donc si vous souhaitez modifier le débit d’envoi des messages, respectez le processus suivant pour effectuer des changements immédiats.

## Apporter des changements immédiats

Si vous avez besoin que les modifications prennent effet immédiatement, procédez comme suit :

1. Arrêtez la campagne affectée.
2. Dupliquez la campagne.
3. Effectuez des modifications sur la campagne dupliquée.

{% alert important %}
Cela réinitialise l’admissibilité des personnes qui ont déjà reçu la campagne originale, vous devrez donc peut-être filtrer la campagne dupliquée aux personnes qui n’ont pas reçu l’original.
{% endalert %}

## Enregistrer les brouillons des campagnes actives {#campaign-drafts}

Les brouillons sont parfaits pour apporter des modifications à grande échelle aux campagnes actives. En créant un brouillon, vous pouvez piloter les changements prévus avant votre prochain lancement.

{% alert note %}
Une campagne ne peut avoir qu'un seul projet à la fois. En outre, les analyses/analytiques ne sont pas disponibles puisque les modifications de l'avant-projet n'ont pas encore été lancées.
{% endalert %}

Pour créer un brouillon, procédez comme suit :

1. Accédez à votre campagne active.
2. Effectuez vos modifications.
3. Sélectionnez **Enregistrer comme brouillon**. Notez qu'après avoir créé un brouillon, vous ne pouvez pas modifier la campagne active tant que vous n'avez pas lancé ou abandonné votre brouillon.

![Un projet de campagne active avec une option pour visualiser la campagne active.]({% image_buster /assets/img/campaign_draft.png %})

Lorsque vous modifiez le projet, vous pouvez également faire référence à la campagne active dans l'en-tête du projet de campagne ou dans le pied de page de l'analyse/analytique de la campagne. 

Pour revenir à une campagne active, sélectionnez **Modifier le brouillon** dans la vue analytique ou dans la vue de la campagne active.

### Priorité aux messages in-app

La priorité des messages in-app sera mise à jour immédiatement (avant que l'ébauche ne soit lancée) lorsque vous sélectionnez **Définir la priorité exacte** et que vous spécifiez la priorité par rapport à d'autres campagnes ou Canevas.
