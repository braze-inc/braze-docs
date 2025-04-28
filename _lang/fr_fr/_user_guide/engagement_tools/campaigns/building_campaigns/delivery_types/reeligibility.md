---
nav_title: Rééligibilité pour la campagne et le Canvas
article_title: Rééligibilité pour la campagne et le Canvas
page_order: 3
page_type: reference
description: "Le présent article de référence donne un aperçu de ce que signifie permettre aux utilisateurs de devenir rééligibles pour recevoir ou rentrer à nouveau au sein d’une campagne ou d’un Canvas."
tool:
  - Campaigns
  - Canvas

---

# Rééligibilité pour la campagne et le Canvas

> Chaque fois que vous planifiez une campagne récurrente ou déclenchée ou une Canvas, vous avez la possibilité de permettre aux utilisateurs de redevenir éligibles (afin que les utilisateurs puissent entrer dans la campagne ou la Canvas plusieurs fois en fonction du déclencheur). Par défaut, Braze envoie un message à un utilisateur une seule fois, même s'il se requalifie plusieurs fois, car la rééligibilité doit être activée séparément. 

Si vous activez la rééligibilité, vous remplacez ce comportement par défaut et permettez aux membres qualifiés de recevoir à nouveau des messages après avoir reçu la première instance de la campagne ou du Canvas. Vous pouvez indiquer la chronologie selon laquelle les utilisateurs peuvent devenir rééligibles.

## Canvas

Pour activer la rééligibilité pour un Canvas, cochez **Autoriser les utilisateurs à rentrer à nouveau dans ce Canvas** dans la section **Contrôles d'entrée**. Vous pouvez choisir entre permettre aux utilisateurs de rentrer après la durée maximale du Canvas, ou après une fenêtre spécifiée.

![Contrôles d’entrée][2]

La rééligibilité pour les Canvas Variant est liée à l’entrée dans le Canvas plutôt qu’à la réception du message. Les utilisateurs qui entrent dans un Canvas et ne reçoivent aucun message ne pourront pas rentrer dans le Canvas à moins que la rééligibilité soit activée. 

Par exemple, imaginons qu’un utilisateur sans adresse e-mail entre dans un Canvas récurrent quotidien qui contient une étape dans le parcours utilisateur. Le composant Canvas ne contient qu’un message e-mail, de sorte que l’utilisateur ne reçoit pas l’engagement. Cet utilisateur ne pourra plus entrer dans le Canvas à moins que la rééligibilité du Canvas soit activée. Si vous avez un Canvas récurent ou déclenché actif sans rééligibilité et que vous souhaitez que les utilisateurs puissent entrer à nouveau à l’intérieur jusqu’à ce qu’ils reçoivent un message de lui, vous pouvez envisager de permettre aux utilisateurs d’être rééligibles pour l’entrée en ajoutant un filtre aux critères d’entrée qui exclue les clients qui ont reçu un message de Canvas.

Si la rééligibilité d’un Canvas est définie comme étant moins longue que la durée de celui-ci, il est possible que les utilisateurs y entrent plus d’une fois, ce qui peut entraîner un comportement trompeur pour les Canvas qui utilisent des messages in-app avec des délais particulièrement longs. Étant donné que plusieurs messages in-app de Canvas peuvent être déclenchés par le même démarrage de session, l’utilisateur pourrait potentiellement expérimenter la réception du même message de manière répétée, si un composant spécifique est livré plus vite que les autres.

## Campagnes

Pour activer la rééligibilité pour une campagne, cochez la case **Autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne** dans la section **Contrôles de livraison**. Le délai maximum pour la rééligibilité à une campagne est de 720 jours.

![][1]

Dans le cas de campagnes déclenchées avec rééligibilité activée, les utilisateurs qui [n'ont pas réellement reçu le message de la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (malgré avoir complété l'événement déclencheur) seront automatiquement éligibles pour le message la prochaine fois qu'ils complètent l'événement déclencheur, même si vous n'avez pas rendu les utilisateurs rééligibles. Ceci est dû au fait que la rééligibilité est basée sur la réception des messages et non sur l'entrée de la campagne. En rendant les utilisateurs à nouveau éligibles pour une campagne déclenchée, vous leur permettez de recevoir effectivement (et non simplement déclencher) le message plus d'une fois.

De plus, si vous essayez d’envoyer un message immédiatement avec une rééligibilité de zéro minute, nous tenterons toujours de le planifier immédiatement, indépendamment de la manière dont un utilisateur a reçu les versions précédentes de la campagne ou du Canvas.

![][24]

## Calculs du délai de rééligibilité

La rééligibilité pour les campagnes et les Canvas est calculée en secondes et non pas en jours calendaires. Cela signifie qu’un jour compte pour 24 heures (ou 86 400 secondes) à partir du moment où un utilisateur reçoit le message et non pas le jour calendaire suivant à minuit.

De même, un mois compte exactement 2 592 000 secondes, soit environ 30 jours.

### Cas d’utilisation

Considérez le scénario suivant :
* Une campagne est prévue pour être envoyée mensuellement le 15 avec une rééligibilité fixée à 30 jours.
* Il y a moins de 30 jours entre le 15 février et le 15 mars. 

Cela signifie que les utilisateurs qui ont reçu la campagne le 15 février ne seront pas éligibles pour la campagne envoyée le 15 mars.

Si la campagne est programmée pour être envoyée quotidiennement à 8 heures avec une rééligibilité de 1 jour et qu'il y a une latence dans l'envoi du message, les utilisateurs qui ont reçu la campagne à 8h30, par exemple, ne seront pas encore rééligibles le lendemain à 8 heures.

## Tests multivariés

En ce qui concerne les tests multivariés, Braze détermine la rééligibilité de la variante pour toutes les campagnes, les messages in-app déclenchés et les Canvas en utilisant les règles suivantes :

- Lorsque les pourcentages de variantes ne sont pas modifiés, chaque utilisateur entrera toujours dans la même variante d’une campagne, du message in-app déclenché ou d’un Canvas, à chaque fois qu’il est rééligible.
- Si les pourcentages de variante changent, les utilisateurs peuvent être répartis sur d’autres variantes.
- Les groupes de contrôle resteront cohérents si le pourcentage de variante est inchangé et aucun utilisateur ayant reçu précédemment des messages n’entrera dans le groupe de contrôle sur un envoi ultérieur. De plus, aucun utilisateur du groupe de contrôle ne recevra de message.

[1]: {% image_buster /assets/img_archive/reeligibility_controls_campaign.png %}
[2]: {% image_buster /assets/img_archive/reeligibility_controls_canvas.png %}
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
