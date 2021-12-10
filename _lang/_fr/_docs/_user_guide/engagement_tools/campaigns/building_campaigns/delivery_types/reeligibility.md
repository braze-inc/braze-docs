---
nav_title: Rééligibilité à la campagne et à la toile
article_title: Rééligibilité à la campagne et à la toile
page_order: 3
page_type: Référence
description: "Cet article de référence donne un aperçu de ce que signifie permettre aux utilisateurs de redevenir éligibles pour recevoir ou réinscrire une campagne ou un Canvas."
tool:
  - Campagnes
  - Toile
---

# Rééligibilité avec des campagnes et Canvas

Chaque fois que vous planifiez une campagne récurrente ou déclenchée ou une campagne Canvas, vous avez la possibilité de permettre aux utilisateurs de devenir de nouveau éligibles. Par défaut, Braze n'envoie un message à un utilisateur qu'une seule fois, même s'il se qualifie. Si vous activez la rééligibilité, vous remplacez ce comportement par défaut et permettez aux membres qualifiés de recevoir à nouveau des messages une fois qu'ils ont reçu la première instance de la campagne ou de Canvas. Vous pouvez indiquer le calendrier sur lequel les utilisateurs deviendraient finalement rééligibles.

## Toile

Pour activer la réelibility pour une toile, cochez **permettre aux utilisateurs de ré-entrer sur cette toile** dans la section **contrôle d'entrée** de l'étape 3. Vous pouvez choisir entre permettre aux utilisateurs de ré-entrer après la durée maximale de la toile, ou après une fenêtre spécifiée.

!\[Contrôles d'entrée\]\[2\]

La réadmissibilité aux variantes de Canvas est liée à l'entrée de Canvas plutôt qu'à la réception de messages. Les utilisateurs qui entrent dans un Canvas et ne reçoivent aucun message ne seront pas en mesure d'entrer à nouveau sur le Canvas à moins que la rééligibilité ne soit activée.

Par exemple, supposons qu'un utilisateur sans adresse de courriel entre un Canvas quotidien récurrent qui contient une étape. L'étape de Canvas ne contient que des messages électroniques, de sorte que l'utilisateur ne reçoit pas l'engagement. Cet utilisateur ne sera pas en mesure d'entrer à nouveau sur Canvas à moins que la rééligibilité de Canvas n'ait été activée. Si vous avez un Canvas actif récurrent ou déclenché sans rééligibilité, et vous souhaitez que les utilisateurs réintègrent le Canvas jusqu'à ce qu'ils reçoivent un message de ce dernier, vous pouvez envisager de permettre aux utilisateurs d'être de nouveau admissibles à l'inscription en ajoutant un filtre aux critères d'entrée qui exclut les clients qui ont reçu un message de la Canvas.

Si la rééligibilité à un Canvas est définie sur une durée plus courte que la durée du Canvas, il est possible pour les utilisateurs d'entrer sur le Canvas plus d'une fois, qui peuvent conduire à des comportements trompeurs pour les Canvases qui utilisent des messages dans l'application avec des délais particulièrement longs. Puisque plusieurs messages Canvas dans l'application peuvent être déclenchés par le même démarrage de la session, l'utilisateur pourrait potentiellement avoir l'expérience de recevoir le même message à plusieurs reprises, si une étape spécifique s'affiche plus rapidement que d'autres.

## Campagnes

Pour permettre la rééligibilité à une campagne, cochez **permettre aux utilisateurs de devenir rééligibles pour recevoir la campagne** dans la section **contrôle de la livraison** de l'étape 2.

!\[Contrôles de livraison\]\[1\]

Dans le cas de campagnes déclenchées avec rééligibilité activée, les utilisateurs qui [n'ont pas réellement reçu la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (malgré la fin de l'événement de déclenchement) se qualifieront automatiquement pour le message la prochaine fois qu'ils termineront l'événement de déclenchement même si vous n'avez pas rendu les utilisateurs rééligibles. En rendant les utilisateurs rééligibles pour une campagne déclenchée, vous leur permettez de recevoir (et pas simplement de déclencher) le message plus d'une fois.

De plus, si vous essayez d'envoyer un message immédiatement avec une rééligibilité de 0 minutes, nous essaierons toujours de le planifier tout de suite, indépendamment de la façon dont un utilisateur a reçu des versions précédentes de la campagne ou de Canvas.

!\[re-eligible\]\[24\]

## Calcul du délai de rééligibilité

La réadmissibilité aux deux campagnes et aux Canvases est calculée en secondes, et non en jours calendaires. Cela signifie qu'un jour compte comme 24 heures (ou 86, 00 secondes) à partir du moment où un utilisateur reçoit le message, pas le prochain jour du calendrier à minuit.

De même, un mois compte exactement 2 592 000 secondes, soit environ 30 jours.

## Tests multivariés

En ce qui concerne les tests multivariés, Braze détermine la rééligibilité de variante pour toutes les campagnes, déclenché dans l'application, et les Canvases en utilisant les règles suivantes :

- Lorsque les pourcentages de variante ne sont pas modifiés, chaque utilisateur entrera toujours dans la même variante d'une campagne, a déclenché un message dans l'application, ou l'entrée Canvas chaque fois qu'ils sont rééligibles.
- Si les pourcentages de variante changent, les utilisateurs peuvent être redistribués à d'autres variantes.
- Les groupes de contrôle resteront cohérents si le pourcentage de variante est inchangé, et aucun utilisateur qui a déjà reçu des messages n'entrera jamais dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne recevra jamais de message.
[1]: {% image_buster /assets/img_archive/reeligibility_controls_campaign.png %} [2]: {% image_buster /assets/img_archive/reeligibility_controls_canvas.png %}
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
