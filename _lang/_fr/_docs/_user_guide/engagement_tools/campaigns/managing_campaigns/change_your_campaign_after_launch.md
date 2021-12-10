---
nav_title: Changement de votre campagne après le lancement
article_title: Changement de votre campagne après le lancement
page_order: 0
tool: Campagnes
page_type: Référence
description: "Cet article de référence donne un aperçu du résultat de l'édition de certains aspects d'une campagne après le lancement."
---

# Modification de votre campagne après le lancement

> Cet article donne un aperçu du résultat de l'édition de certains aspects d'une campagne après le lancement.

## Campagnes déclenchées

Tous les changements apportés aux campagnes de livraison par Action-Based Delivery et aux campagnes de livraison déclenchées par l'API prennent effet immédiatement pour les envois directs.

Si ces campagnes ont été déclenchées, mais pas encore envoyées (par exemple, une campagne de livraison avec un délai de 1 jour est éditée pendant la période de retard de 1 jour), veuillez vous référer aux conseils pour les campagnes planifiées ci-dessous.

## Campagnes planifiées

Si vous avez besoin d'apporter des modifications à une campagne après le lancement, Veuillez prendre note des éléments ci-dessous lors de l'édition de votre campagne pour vous assurer que vos changements ont les effets souhaités.

### Contenu du message

Tout changement de contenu du message (y compris les titres, les corps, les images, etc.) prend effet immédiatement après l'enregistrement de tous les messages envoyés vers l'avenir. Il n'est pas possible de modifier le contenu des messages qui ont déjà été envoyés.

### Planification et audience

Si vous modifiez l'heure d'envoi prévue de votre campagne, ou son public, ces changements ne seront pas reflétés dans la campagne actuelle avant la fin de la période actuelle de 24 heures.

### Taux d'envoi

Lorsque vous utilisez une limite de taux d'envoi, Braze "planifie" vos messages en minute-granularité, donc si vous voulez modifier le taux d'envoi des messages, vous devriez suivre le processus ci-dessous pour des changements immédiats.

## Effectuer des changements immédiats

Si vous avez besoin de changements pour prendre effet immédiatement, faites ce qui suit :

1. Arrêter la campagne concernée.
2. Dupliquer la campagne.
3. Effectuer des modifications sur la campagne en double.

{% alert important %}
Cela réinitialise l'éligibilité des personnes qui ont déjà reçu la campagne initiale, pour que vous ayez besoin de filtrer la campagne en double pour les personnes qui n'ont pas reçu l'original.
{% endalert %}
