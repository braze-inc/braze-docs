---
nav_title: Faire correspondre les critères de sortie aux événements d'entrée
article_title: Faire correspondre les critères de sortie aux événements d'entrée
page_order: 5
page_type: tutorial
description: "Découvrez comment configurer des critères de sortie et des parcours d'action qui comparent les propriétés d'événement aux propriétés d'entrée du Canvas, afin que les utilisateurs ne sortent ou ne bifurquent que lorsqu'ils accomplissent l'action spécifique avec laquelle ils sont entrés."
tool: Canvas
---

# Faire correspondre les critères de sortie aux événements d'entrée

> Cet article explique comment configurer des critères de sortie et des parcours d'action directement corrélés à l'événement d'entrée du Canvas, afin que les utilisateurs ne sortent ou ne bifurquent que lorsqu'ils effectuent une action spécifique liée à la raison de leur entrée dans le Canvas.

En comparant les propriétés d'événement aux [propriétés d'entrée du Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/), vous pouvez créer des flux hautement ciblés. Par exemple, dans un Canvas d'abandon de panier, vous pouvez configurer la sortie d'un utilisateur uniquement lorsqu'il achète l'article exact qu'il a abandonné, tout en continuant à lui envoyer des messages de rappel s'il achète un article différent.

Cette approche utilise les [variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) pour comparer les propriétés entre les événements. Ce modèle s'applique à de nombreux scénarios au-delà du e-commerce, notamment les renouvellements de polices, les rappels de réservation et la gestion des abonnements.

## Critères de sortie : quitter le Canvas lorsqu'une action correspondante se produit

Utilisez les [critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/) lorsque vous souhaitez qu'un utilisateur quitte entièrement le Canvas après avoir effectué une action correspondant à son événement d'entrée.

### Exemple : achat de billet abandonné

Dans ce scénario, un utilisateur entre dans le Canvas lorsqu'il effectue l'événement personnalisé `Selected Ticket`, qui contient une propriété appelée `event_id`. Les critères de sortie sont configurés de sorte que lorsqu'un utilisateur déclenche l'événement personnalisé `Purchased Ticket` — qui inclut également une propriété nommée `event_id` — la propriété de l'événement de sortie est comparée à la propriété de l'événement d'entrée. Si les deux correspondent, l'utilisateur quitte le Canvas.

Concrètement :

- Si l'utilisateur achète le même billet qu'il avait initialement sélectionné, il quitte le Canvas et cesse de recevoir des rappels.
- Si l'utilisateur achète un billet différent, il reste dans le Canvas et continue de recevoir des messages de suivi concernant le billet d'origine.

Pour configurer cela :

1. Configurez une entrée de Canvas basée sur une action avec l'événement personnalisé déclencheur (tel que `Selected Ticket`) et sa propriété pertinente (telle que `event_id`).
2. Dans l'étape **Audience cible**, configurez l'événement d'exception des critères de sortie avec l'événement personnalisé d'achèvement (tel que `Purchased Ticket`).
3. Sélectionnez **Ajouter des filtres de propriété**, puis ajoutez un filtre où la comparaison de la propriété de base `event_id` est définie sur `equals`.
4. Activez le bouton **Personnaliser la valeur**, définissez le **Type de personnalisation** sur `Context Variables` et définissez l'**Attribut** sur `event_id`.

Cela compare le `event_id` de l'événement `Purchased Ticket` au `event_id` enregistré lors de l'événement d'entrée d'origine du Canvas. Pour plus de détails sur la configuration de ces filtres, consultez [Exemples de critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#exit-criteria-examples).

## Parcours d'action : bifurquer en fonction d'une action correspondante

Utilisez les [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) lorsque vous souhaitez qu'un utilisateur reste dans le Canvas mais suive un chemin différent selon que son action ultérieure correspond ou non à l'événement d'entrée.

### Exemple : abandon de panier avec chemins de bifurcation

Dans ce scénario, un utilisateur qui a sélectionné un article mais n'a pas finalisé son achat reçoit d'abord un message d'abandon de panier. L'utilisateur est ensuite maintenu dans une étape de parcours d'action pendant une semaine avant d'être orienté vers l'un des trois chemins en fonction de ses actions pendant cette période :

- **Achat d'origine effectué :** L'ID de propriété de l'événement personnalisé est égal à l'ID de propriété d'entrée. Ces utilisateurs peuvent recevoir un message de remerciement ou une recommandation de vente croisée.
- **Achat différent effectué :** L'ID de propriété de l'événement personnalisé n'est pas égal à l'ID de propriété d'entrée. Ces utilisateurs peuvent recevoir un rappel concernant l'article d'origine.
- **Aucun achat effectué :** Redirigé vers le groupe **Tous les autres**. Ces utilisateurs peuvent recevoir une incitation plus forte ou un rappel final.

Pour configurer cela :

1. Ajoutez une étape [Parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) et définissez la fenêtre d'évaluation (par exemple, une semaine).
2. Pour le premier groupe d'actions (achat d'origine), ajoutez un déclencheur pour l'événement personnalisé d'achèvement (tel que `Purchased_Ticket`). Sélectionnez **Ajouter des filtres de propriété**, puis ajoutez un filtre où la comparaison de la propriété de base `event_id` est définie sur `equals`. Activez **Personnaliser la valeur**, définissez le **Type de personnalisation** sur `Context Variables` et définissez l'**Attribut** sur `event_id`.
3. Pour le deuxième groupe d'actions (achat différent), ajoutez le même événement déclencheur mais définissez la comparaison sur `does not equal` avec la même configuration de variable de contexte.
4. Utilisez le groupe **Tous les autres** pour les utilisateurs qui n'ont pas du tout effectué l'événement d'achèvement.

Pour plus de détails sur la configuration de ces filtres, consultez [Exemples de parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-examples).

## Autres applications

Bien que cet article utilise un exemple d'achat abandonné, vous pouvez appliquer le même modèle à tout scénario où une action d'achèvement doit être corrélée à l'action d'entrée, notamment :

- **Renouvellements de polices :** Faire sortir les utilisateurs qui renouvellent la police spécifique ayant déclenché le Canvas.
- **Rappels de réservation :** Orienter les utilisateurs selon qu'ils ont confirmé ou modifié leur réservation d'origine.
- **Gestion des abonnements :** Diriger les utilisateurs différemment selon qu'ils ont mis à niveau le plan spécifique qui leur avait été proposé.
- **Inscriptions à des événements :** Faire sortir les utilisateurs qui finalisent leur inscription à l'événement spécifique pour lequel ils avaient manifesté de l'intérêt.

## Bon à savoir

- Les configurations présentées dans cet article sont des exemples illustratifs. Testez tous les composants dans votre environnement de développement avant le lancement.
- Vérifiez que les noms de propriétés et les types de données de vos événements d'entrée correspondent à ceux utilisés dans vos critères de sortie ou parcours d'action.
- Consultez la documentation sur les [variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) pour en savoir plus sur le fonctionnement des comparaisons de propriétés entre événements.