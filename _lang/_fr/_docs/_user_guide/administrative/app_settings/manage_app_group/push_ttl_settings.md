---
nav_title: Paramètres Push TTL
article_title: Paramètres Push TTL
page_order: 4
page_type: Référence
description: "Cet article de référence couvre la page des paramètres de Push Time to Live dans le tableau de bord Braze."
channel: Pousser
---

# Temps de push pour les paramètres de live

L'onglet **Push TTL** dans **Gérer les paramètres** vous permet de contrôler la durée de la tentative de livraison pour les appareils hors ligne. Cela signifie que si l'appareil d'un utilisateur est hors ligne lorsque votre campagne envoie, Braze tentera de transmettre le message à l'heure que vous avez définie sur cette page.

Cette fonctionnalité ne supprimera pas une notification si elle a déjà été reçue par l’appareil de l’utilisateur – elle ne contrôlera que la durée pendant laquelle le fournisseur de push tentera de livrer une notification.

!\[Time to Live\]\[1\]

{% alert tip %}
N'oubliez pas de cliquer sur **Enregistrer** avant de quitter la page !
{% endalert %}
[1]: {% image_buster /assets/img/push_ttl.png %}
