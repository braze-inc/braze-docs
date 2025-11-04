---
nav_title: Rééligibilité
article_title: Rééligibilité
page_order: 8
page_type: reference
description: "Cet article de référence définit la rééligibilité pour les campagnes et les toiles."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# Rééligibilité pour les campagnes et Canvas

> Lorsque vous planifiez une campagne récurrente ou déclenchée ou un Canvas, vous avez la possibilité de permettre aux utilisateurs de s'y réinscrire. La rééligibilité signifie que les utilisateurs peuvent entrer dans la campagne ou le Canvas plusieurs fois en fonction du déclencheur.

## Comment cela fonctionne-t-il ?

Par défaut, Braze n'envoie qu'un seul message à un utilisateur, même s'il se requalifie plusieurs fois, car la rééligibilité doit être activée séparément. Une fois cette option activée, les membres qualifiés seront autorisés à recevoir à nouveau des messages après avoir reçu la première instance de la campagne ou du Canvas. Vous pouvez indiquer le délai dans lequel les utilisateurs seront finalement rééligibles.

## Retour sur la rééligibilité

{% tabs local %}
{% tab campaign %}
Pour activer la rééligibilité à une campagne, cochez la case **Autoriser les utilisateurs à devenir rééligibles pour recevoir une campagne** dans la section **Contrôles de réception/distribution**. La durée maximale de rééligibilité pour une campagne est de 720 jours.

Pour les campagnes déclenchées dont la rééligibilité est activée, les utilisateurs qui [n'ont pas reçu le message de la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) (bien qu'ils aient effectué l'événement déclencheur) se qualifieront automatiquement pour le message la prochaine fois qu'ils effectueront l'événement déclencheur. En effet, la rééligibilité est basée sur la réception des messages et non sur l'entrée en campagne. En rendant les utilisateurs rééligibles pour une campagne déclenchée, vous leur permettez de recevoir réellement (et non simplement de déclencher) le message plus d'une fois.

En outre, si vous essayez d'envoyer un message immédiatement avec une rééligibilité de zéro minute, nous essaierons toujours de le planifier immédiatement, quelle que soit la façon dont l'utilisateur a reçu les versions précédentes de la campagne ou de Canvas.

#### Rééligibilité avec des campagnes déclenchées par l'API

Le nombre de fois qu'un utilisateur reçoit une campagne déclenchée par l'API peut être limité à l'aide des paramètres de rééligibilité. Cela signifie que l'utilisateur ne recevra la campagne qu'une seule fois ou une seule fois dans une fenêtre donnée, quel que soit le nombre de fois où le déclencheur de l'API est déclenché.

Par exemple, disons que vous utilisez une campagne déclenchée par l'API pour envoyer à l'utilisateur une campagne sur un article qu'il a récemment consulté. Dans ce cas, vous pouvez limiter la campagne à l'envoi d'un message par jour, quel que soit le nombre d'articles consultés, tout en déclenchant l'API pour chaque article. En revanche, si votre campagne déclenchée par l'API est transactionnelle, vous voudrez vous assurer que l'utilisateur reçoit la campagne à chaque fois qu'il effectue la transaction en définissant le délai à zéro minute.
{% endtab %}

{% tab canvas %}

Pour activer la rééligibilité pour un Canvas, sélectionnez **Autoriser les utilisateurs à saisir à nouveau ce Canvas** dans la section **Contrôles de saisie.**  Vous pouvez choisir d'autoriser les utilisateurs à se réinscrire après la durée maximale de la toile ou après une fenêtre spécifiée.

La rééligibilité pour les variantes du canvas est liée à l'entrée dans le canvas plutôt qu'à la réception du message. Les utilisateurs qui entrent dans un canvas et ne reçoivent aucun message ne pourront pas entrer à nouveau dans le canvas, à moins que la rééligibilité ne soit activée.

Notez qu'un utilisateur n'a pas besoin de quitter un canvas avant d'y revenir si la rééligibilité est fixée à zéro seconde, ce qui signifie qu'il est possible pour un utilisateur d'entrer à nouveau dans le même canvas. Vous pouvez ajouter des filtres supplémentaires pour éviter que les utilisateurs ne reçoivent plusieurs fois la même étape ou le même message. Cependant, lorsqu'un utilisateur revient dans un canvas pour la deuxième fois, les étapes reçues lors de sa première visite dans le canvas ne sont pas visibles pour l'utilisateur. Cela signifie que l'utilisateur peut recevoir à nouveau le même message. Pour éviter cela, vous pouvez configurer le Canvas de manière à empêcher la réinscription ou définir la rééligibilité pour la durée maximale du Canvas.

Vous pouvez également utiliser un [composant de mise à jour de l']({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) utilisateur pour que l'utilisateur qui reçoit l'étape l'enregistre en tant qu'attribut personnalisé, ce qui peut être utilisé pour filtrer les utilisateurs qui ont reçu l'étape au cours de leur parcours Canvas.

### Exemple

Par exemple, supposons qu'un utilisateur sans adresse e-mail entre dans un canvas récurrent quotidien qui contient une étape du canvas. Cette étape ne contient qu'un message e-mail, de sorte que l'utilisateur ne reçoit pas d'engagement. Cet utilisateur ne pourra plus entrer dans le Canvas à moins que la rééligibilité ne soit activée dans le Canvas. 

Si vous avez un Canvas récurrent ou déclenché actif sans rééligibilité, et que vous souhaitez que les utilisateurs entrent à nouveau dans le Canvas jusqu'à ce qu'ils reçoivent un message de celui-ci, vous pouvez envisager d'autoriser les utilisateurs à être rééligibles en ajoutant un filtre aux critères d'entrée qui exclut les clients qui ont reçu un message du Canvas.

Si la durée de la rééligibilité pour un Canvas est inférieure à la durée du Canvas, les utilisateurs peuvent entrer dans le Canvas plusieurs fois, ce qui peut entraîner un comportement trompeur pour les Canvas qui utilisent des messages in-app avec des délais particulièrement longs. Étant donné que plusieurs messages in-app Canvas peuvent être déclenchés par le même démarrage de session, l'utilisateur pourrait avoir l'expérience sur-app de recevoir le même message à plusieurs reprises, si un composant spécifique a un rendu plus rapide que les autres.
{% endtab %}
{% endtabs %}

## Calcul du délai de réadmissibilité

La rééligibilité pour les campagnes et les canevas est calculée en secondes, et non en jours calendaires. Cela signifie qu'un jour compte pour 24 heures (ou 86 400 secondes) à partir du moment où l'utilisateur reçoit le message, et non le jour calendaire suivant à minuit. De même, un mois compte exactement 2 592 000 secondes, soit environ 30 jours.

### Exemple

Considérez le scénario suivant :

* Une campagne est programmée pour un envoi mensuel le 15 et la rééligibilité est fixée à 30 jours.
* Il y a moins de 30 jours entre le 15 février et le 15 mars. 

Cela signifie que les utilisateurs qui ont reçu la campagne le 15 février ne seront pas éligibles pour la campagne qui sera envoyée le 15 mars. Si la campagne est paramétrée pour être envoyée quotidiennement à 8 heures du matin avec une rééligibilité d'un jour et qu'il y a un temps de latence dans l'envoi du message, les utilisateurs qui ont reçu la campagne à 8h30 ne seront pas encore rééligibles le lendemain à 8 heures du matin.

## Test multivarié

Pour les tests multivariés, Braze détermine la rééligibilité des variantes pour toutes les campagnes, les messages in-app déclenchés et les Canvases à l'aide des règles suivantes :

- Lorsque les pourcentages de variante ne sont pas modifiés, chaque utilisateur saisira toujours la même variante d'une campagne, d'un message in-app déclenché ou d'une entrée Canvas à chaque fois qu'il sera à nouveau éligible.
- Si les pourcentages des variantes changent, les utilisateurs peuvent être redistribués vers d'autres variantes.
- Les groupes de contrôle resteront cohérents si le pourcentage de variante est inchangé, et aucun utilisateur ayant déjà reçu des messages n'entrera jamais dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne recevra jamais de message.

