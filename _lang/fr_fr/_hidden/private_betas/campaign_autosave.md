---
nav_title: Sauvegarde automatique pour les campagnes
article_title: Sauvegarde automatique pour les campagnes
permalink: "/campaign_autosave/"
hidden: true
description: "Cet article de référence explique en détail le fonctionnement de la sauvegarde automatique pour les campagnes."
page_type: reference
---

# Sauvegarder automatiquement les campagnes

> Lorsque vous créez vos campagnes dans Braze, vos modifications sont désormais automatiquement enregistrées. Ainsi, vous pouvez vous concentrer sur le perfectionnement de vos campagnes en toute confiance, sachant que vos modifications sont préservées.

{% alert important %}
L’enregistrement automatique est actuellement en version bêta et n'est disponible que pour les campagnes. Si vous souhaitez participer à cet essai bêta, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

{% alert warning %}
Lorsque vous modifiez un message dans un éditeur plein écran, tel qu'un e-mail ou un message in-app, les modifications apportées au message ne sont pas enregistrées automatiquement. Lorsque vous sélectionnez **Terminé** pour quitter l'éditeur et revenir à la campagne, les modifications apportées au message seront enregistrées lors de la prochaine sauvegarde automatique. Par précaution, vous pouvez également enregistrer manuellement votre message.
{% endalert %}

## Fonctionnement

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Vos campagnes s'enregistrent automatiquement et périodiquement à mesure que vous les modifiez et passez d'un onglet à l'autre dans l'éditeur de campagne.

Les modifications sont enregistrées en tant que brouillon, tant pour les campagnes à l’état d’ébauche que pour les campagnes déjà actives. Pour les campagnes arrêtées, vos modifications seront enregistrées, mais la campagne restera arrêtée.

Si vous et un autre utilisateur apportez des modifications à une campagne, la première série de modifications sera enregistrée. Si vous êtes la deuxième personne à enregistrer des modifications, vous devrez actualiser la page pour voir les dernières mises à jour de la campagne.

[1]: {% image_buster /assets/img/campaign_autosave.png %}
