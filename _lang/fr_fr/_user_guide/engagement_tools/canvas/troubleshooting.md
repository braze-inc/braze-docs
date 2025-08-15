---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des toiles
page_order: 11
page_type: reference
description: "Cette page présente les étapes de résolution des problèmes pour les toiles."
tool: Canvas
---

# Résolution des problèmes des toiles

> Cette page vous aide à résoudre les problèmes liés à vos toiles.

## Pourquoi un utilisateur n'a-t-il pas reçu une étape du canvas déclenchée ?

Tout d'abord, confirmez que l'événement personnalisé est transmis à Braze. Accédez à **Analyse/analytique** > **Rapport sur les événements personnalisés**, puis sélectionnez l'événement personnalisé et la plage de dates correspondants. Si l'événement ne s'affiche pas, vérifiez qu'il est correctement configuré et que l'utilisateur a effectué la bonne action.

Si l'événement personnalisé s'affiche, poursuivez la résolution des problèmes en procédant comme suit :

- Vérifiez le téléchargement du profil utilisateur pour confirmer qu'il a déclenché l'événement et quand il l'a fait. Si l'événement a été déclenché, comparez l'horodatage du déclenchement de l'événement à la durée en ligne/en production/instantanée du Canvas. L'événement peut avoir été déclenché avant que la toile ne soit mise en ligne/en production/instantanée.
- Examinez les journaux des modifications pour le Canvas et tous les segments utilisés dans le ciblage afin de déterminer si l'utilisateur se trouvait dans le segment lorsque son événement personnalisé a été déclenché. S'ils n'étaient pas dans le segment, ils n'auraient pas reçu l'étape du canvas.
- Vérifiez si l'utilisateur a été intégré dans un groupe de contrôle par le biais de la segmentation et, par conséquent, s'il n'a pas pu bénéficier de l'étape du canvas.
- En cas de retard planifié, vérifiez si l'événement personnalisé de l'utilisateur a été déclenché avant le retard. Si l'événement avait été déclenché avant le délai, ils n'auraient pas reçu l'étape du canvas.

{% alert note %}
Les messages in-app ne peuvent être déclenchés que par des événements envoyés via le SDK, et non via l'API REST.
{% endalert %}