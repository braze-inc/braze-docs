---
nav_title: Paramètres TTL (Durée de vie) de notification push
article_title: Paramètres TTL (Durée de vie) de notification push
page_order: 4
page_type: reference
description: "Cet article de référence couvre les paramètres de notification Push Time to Live (TTL, durée de vie) du tableau de bord de Braze."
channel: push

---

# Paramètres de notification Push TTL

L’onglet **Push TTL Settings** (Paramètres TTL de notification push) dans **Manage Settings** (Gérer les paramètres) vous permet de contrôler la durée de la tentative de distribution pour les périphériques hors ligne. Cela signifie que si l’appareil d’un utilisateur est hors ligne lorsque votre campagne est en cours de diffusion, Braze tente de transmettre le message jusqu’à l’heure définie.

Cette fonctionnalité ne supprimera pas une notification de réception par l’appareil de l’utilisateur ; il ne contrôlera que la durée pendant laquelle le fournisseur de notification push tentera d’envoyer une notification.

![Onglet Push Time to Live Settings (Paramètres de notification Push TTL) sous Manage Settings (Gérer les paramètres)][1]

{% alert tip %}
N’oubliez pas de cliquer sur **Save** (Enregistrer) avant de quitter la page !
{% endalert %}

[1]: {% image_buster /assets/img/push_ttl.png %}
