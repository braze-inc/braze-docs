---
nav_title: Modifier votre campagne après son lancement
article_title: Modifier votre campagne après son lancement
page_order: 1
tool: Campaigns
page_type: reference
description: "Le présent article de référence donne un aperçu du résultat de la modification de certains aspects d’une campagne après son lancement."

---

# Modifier votre campagne après son lancement

> Le présent article donne un aperçu du résultat de la modification de certains aspects d’une campagne après son lancement.

## Campagnes déclenchées

Toutes les modifications apportées aux campagnes de livraison par événement et déclenchées par API prennent effet immédiatement pour les envois directs.

Si ces campagnes ont été déclenchées mais pas encore envoyées (par exemple, une campagne de livraison par événement avec un délai de 1 jour est modifiée pendant la période de délai de 1 jour), reportez-vous aux directives suivantes pour les campagnes planifiées.

## Campagnes planifiées

Si vous devez apporter des modifications à une campagne après son lancement, prenez en compte les éléments suivants lors de la modification de votre campagne afin de vous assurer que vos modifications ont les effets souhaités.

### Contenu du message

Tout changement de contenu du message (y compris les titres, les corps, les images, etc.) prend effet immédiatement lors de l’enregistrement pour tous les messages envoyés à l’avenir. Il n’est pas possible de modifier le contenu des messages déjà envoyés.

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
