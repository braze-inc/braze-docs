---
nav_title: Rééligibilité
article_title: Rééligibilité
page_order: 10
page_type: reference
description: "Cet article de référence définit la rééligibilité pour les campagnes et les toiles."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Rééligibilité pour les campagnes et Canvas

> Lorsque vous planifiez une campagne récurrente ou déclenchée ou un Canvas, vous avez la possibilité de permettre aux utilisateurs de s'y réinscrire. La rééligibilité signifie que les utilisateurs peuvent entrer dans la campagne ou le Canvas plusieurs fois en fonction du déclencheur.

## Fonctionnement

Par défaut, Braze n'envoie qu'un seul message à un utilisateur, même s'il se requalifie plusieurs fois, car la rééligibilité doit être activée séparément. Une fois cette option activée, les membres qualifiés seront autorisés à recevoir à nouveau des messages après avoir reçu la première instance de la campagne ou du Canvas. Vous pouvez indiquer la chronologie selon laquelle les utilisateurs peuvent devenir rééligibles.

## Retour sur la rééligibilité

{% tabs local %}
{% tab campaign %}
Pour activer la rééligibilité pour une campagne, cochez la case **Autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne** dans la section **Contrôles de livraison**. Le délai maximum pour la rééligibilité à une campagne est de 720 jours.

Pour les campagnes déclenchées dont la rééligibilité est activée, les utilisateurs qui [n'ont pas reçu le message de la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (bien qu'ils aient effectué l'événement déclencheur) se qualifieront automatiquement pour le message la prochaine fois qu'ils effectueront l'événement déclencheur. Ceci est dû au fait que la rééligibilité est basée sur la réception des messages et non sur l'entrée de la campagne. En rendant les utilisateurs à nouveau éligibles pour une campagne déclenchée, vous leur permettez de recevoir effectivement (et non simplement déclencher) le message plus d'une fois.

En outre, si vous essayez d'envoyer un message immédiatement avec une rééligibilité de zéro minute, nous essaierons toujours de le planifier immédiatement, indépendamment de la façon dont l'utilisateur a reçu les versions précédentes de la campagne ou de Canvas.

#### Rééligibilité aux campagnes déclenchées par les API

Le nombre de fois où un utilisateur reçoit une campagne déclenchée par API peut être limité en utilisant des paramètres de rééligibilité. Cela signifie que l’utilisateur recevra la campagne une seule fois ou une seule fois dans une période donnée, indépendamment du nombre de fois où le déclencheur API est activé.

Par exemple, disons que vous utilisez une campagne déclenchée par l'API pour envoyer à l'utilisateur une campagne sur un article qu'il a récemment consulté. Dans ce cas, vous pouvez limiter la campagne à l'envoi d'un message par jour, quel que soit le nombre d'éléments consultés, tout en déclenchant l'API pour chaque élément. D’autre part, si votre campagne déclenchée par API est transactionnelle, vous devez vous assurer que l’utilisateur reçoive la campagne chaque fois qu’il effectue la transaction en définissant le délai sur zéro minute.
{% endtab %}

{% tab canvas %}

Pour activer la rééligibilité pour un Canvas, sélectionnez **Autoriser les utilisateurs à saisir à nouveau ce Canvas** dans la section **Contrôles de saisie.**  Vous pouvez choisir d'autoriser les utilisateurs à se réinscrire après la durée maximale de la toile ou après une fenêtre spécifiée.

La rééligibilité pour les Canvas Variant est liée à l’entrée dans le Canvas plutôt qu’à la réception du message. Les utilisateurs qui entrent dans un Canvas et ne reçoivent aucun message ne pourront pas rentrer dans le Canvas à moins que la rééligibilité soit activée.

Notez qu'un utilisateur n'a pas besoin de quitter un canvas avant d'y revenir si la rééligibilité est fixée à zéro seconde, ce qui signifie qu'un utilisateur peut entrer à nouveau dans le même canvas. Autre exemple, si la durée du Canvas est fixée à 7 jours et la période de rééligibilité à 3 jours, un utilisateur peut réintégrer le Canvas avant d'avoir terminé son premier parcours.

Vous pouvez ajouter des filtres supplémentaires pour éviter que les utilisateurs ne reçoivent plusieurs fois la même étape ou le même message. Cependant, lorsqu'un utilisateur revient dans un canvas pour la deuxième fois, les étapes reçues lors de sa première visite dans le canvas ne sont pas visibles pour l'utilisateur. Cela signifie que l'utilisateur peut recevoir à nouveau le même message. Pour éviter cela, vous pouvez configurer le Canvas de manière à empêcher la réinscription ou définir la rééligibilité pour la durée maximale du Canvas.

Vous pouvez également utiliser une [étape de mise à jour de l']({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) utilisateur pour que l'utilisateur qui reçoit l'étape l'enregistre en tant qu'attribut personnalisé, ce qui peut être utilisé pour filtrer les utilisateurs qui ont reçu l'étape au cours de leur parcours Canvas.

### Exemple

Par exemple, imaginons qu’un utilisateur sans adresse e-mail entre dans un Canvas récurrent quotidien qui contient une étape dans le parcours utilisateur. Cette étape ne contient qu'un message e-mail, de sorte que l'utilisateur ne reçoit pas d'engagement. Cet utilisateur ne pourra plus entrer dans le Canvas à moins que la rééligibilité ne soit activée dans le Canvas. 

Si vous avez un Canvas récurent ou déclenché actif sans rééligibilité et que vous souhaitez que les utilisateurs puissent entrer à nouveau à l’intérieur jusqu’à ce qu’ils reçoivent un message de lui, vous pouvez envisager de permettre aux utilisateurs d’être rééligibles pour l’entrée en ajoutant un filtre aux critères d’entrée qui exclue les clients qui ont reçu un message de Canvas.

Si la rééligibilité d’un Canvas est définie comme étant moins longue que la durée de celui-ci, il est possible que les utilisateurs y entrent plus d’une fois, ce qui peut entraîner un comportement trompeur pour les Canvas qui utilisent des messages in-app avec des délais particulièrement longs. Étant donné que plusieurs messages in-app Canvas pourraient être déclenchés par le même démarrage de session, l'utilisateur pourrait avoir l'expérience sur l'application du même message à plusieurs reprises si un composant spécifique rend plus rapidement que les autres.
{% endtab %}
{% endtabs %}

## Calculs du délai de rééligibilité

La rééligibilité pour les campagnes et les canevas est calculée en secondes, et non en jours calendaires. Cela signifie qu’un jour compte pour 24 heures (ou 86 400 secondes) à partir du moment où un utilisateur reçoit le message et non pas le jour calendaire suivant à minuit. De même, un mois compte exactement 2 592 000 secondes, soit environ 30 jours.

### Exemple

Considérez le scénario suivant :

* Une campagne est prévue pour être envoyée mensuellement le 15 avec une rééligibilité fixée à 30 jours.
* Il y a moins de 30 jours entre le 15 février et le 15 mars. 

Cela signifie que les utilisateurs qui ont reçu la campagne le 15 février ne seront pas éligibles pour la campagne envoyée le 15 mars. Si la campagne est paramétrée pour être envoyée quotidiennement à 8 heures du matin avec une rééligibilité d'un jour, et qu'il y a un temps de latence dans l'envoi du message, les utilisateurs qui ont reçu la campagne à 8h30 ne seront pas encore rééligibles le lendemain à 8 heures du matin.

## Tests multivariés

Pour les tests multivariés, Braze détermine la rééligibilité des variantes pour toutes les campagnes, les messages in-app déclenchés et les Canvases à l'aide des règles suivantes :

- Lorsque les pourcentages de variantes ne sont pas modifiés, chaque utilisateur entrera toujours dans la même variante d’une campagne, du message in-app déclenché ou d’un Canvas, à chaque fois qu’il est rééligible.
- Si les pourcentages de variante changent, les utilisateurs peuvent être répartis sur d’autres variantes.
- Les groupes de contrôle resteront cohérents si le pourcentage de variante est inchangé et aucun utilisateur ayant reçu précédemment des messages n’entrera dans le groupe de contrôle sur un envoi ultérieur. De plus, aucun utilisateur du groupe de contrôle ne recevra de message.
