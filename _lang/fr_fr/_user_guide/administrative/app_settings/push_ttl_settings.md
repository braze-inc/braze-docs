---
nav_title: Paramètres de durée de vie des notifications push
article_title: Paramètres de durée de vie des notifications push
page_order: 16
page_type: reference
description: "Cet article de référence couvre les paramètres de notification Push Time to Live (TTL, durée de vie) du tableau de bord de Braze."
channel: push

---

# Paramètres TTL (Durée de vie) de notification push

> Découvrez la page de paramètres Durée de vie des notifications push dans le tableau de bord de Braze.

La page **TTL (Time-To-Live) Push** vous permet de contrôler la durée des tentatives de réception/distribution pour les appareils hors ligne. Cela signifie que si l’appareil d’un utilisateur est hors ligne lorsque votre campagne est en cours de diffusion, Braze tente de transmettre le message jusqu’à l’heure définie.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez cette page sous **Paramètres** > **Gérer les paramètres** > **Paramètres de durée de vie des notifications push**.
{% endalert %}

Cette fonctionnalité ne supprimera pas une notification de réception par l’appareil de l’utilisateur ; il ne contrôlera que la durée pendant laquelle le fournisseur de notification push tentera d’envoyer une notification.

![Onglet Paramètres de durée de vie (TTL) des notifications push sous Gérer les paramètres][1]

{% alert tip %}
N'oubliez pas de cliquer sur **Enregistrer** avant de quitter la page !
{% endalert %}

[1]: {% image_buster /assets/img/push_ttl.png %}
