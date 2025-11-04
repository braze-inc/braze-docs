---
nav_title: "Prévisualiser les chemins d'accès des utilisateurs"
article_title: "Prévisualisation des chemins d'accès des utilisateurs"
page_order: 0.3
alias: /preview_user_paths/
description: "Cette page explique comment vous pouvez prévisualiser les parcours des utilisateurs dans Canvas."
Tool:
  - Canvas
---

# Prévisualiser les parcours des utilisateurs dans Canvas

> Découvrez l'expérience Canvas que vous avez créée pour vos utilisateurs. Cela inclut la prévisualisation du calendrier et des messages qu'ils recevront. Ces tests permettent de s'assurer que vos messages sont envoyés à la bonne audience, et ce avant l'envoi de votre Canvas.

## Création d'un test

Suivez les étapes suivantes pour prévisualiser votre parcours utilisateur :

1. Allez dans votre générateur de canvas. Enregistrez les modifications non sauvegardées et résolvez les éventuelles erreurs.
2. Sélectionnez **Test Canvas** dans le pied de page.
3. Sélectionnez un utilisateur test.
4. (Facultatif) Sélectionnez un destinataire pour le test.
5. Sélectionnez **Exécuter le test**.

Vous pouvez lancer un aperçu si vous n'avez pas l'autorisation de modifier un canvas, mais cet aperçu sera exécuté avec les modifications non enregistrées s'il y en a.

### Étapes soutenues

Les étapes suivantes sont prises en charge :
- Message 
- Parcours d'audience
- Arbre décisionnel
- Délai
- Parcours d'action
- Chemin d'expérience
- Mise à jour de l'utilisateur (uniquement dans l'éditeur d'interface utilisateur, ce qui signifie que les étapes utilisant l'éditeur JSON seront ignorées)

Si le test chevauche un type d'étape qui n'est pas répertorié ci-dessus, l'étape non prise en charge sera ignorée et l'utilisateur du test passera à l'étape prise en charge suivante.

### Détails de l'étape du canvas

Pour obtenir plus de détails sur les critères d'entrée, sélectionnez **Voir plus.** Les étapes de la segmentation permettent d'indiquer les critères satisfaits ou non satisfaits. Les messages l'indiqueront également pour les validations de réception/distribution et l'éligibilité des canaux. Les étapes du message montreront quels canaux ont été envoyés et lesquels n'ont pas été envoyés.

### Liquide

La logique liquide sera traitée au cours d'une exécution de test, même si vous n'envoyez pas de message de test proprement dit. Cela signifie que la [logique du message d'abandon]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) et d'autres logiques de liquidité sont reflétées et peuvent avoir un impact sur le parcours de l'utilisateur de Canvas.

Si votre aperçu envoie la dernière étape de votre parcours utilisateur au lieu de l'interrompre, il se peut que l'aperçu utilise l'heure actuelle comme heure testée pour l'évaluation du liquide, et non l'heure réelle à laquelle l'utilisateur se trouverait dans l'étape sur la base de l'heure d'entrée dans le Canvas.

## Avant-premières pour le chronométrage

Pour les toiles planifiées, l'utilisateur test entrera à la prochaine heure d'entrée prévue. Pour les canevas basés sur l'action avec des dates de début, l'utilisateur test entrera la date et l'heure de début. 

Si les heures de début par défaut s'appliquent toujours, l'heure d'entrée est configurable dans toutes les instances, ce qui signifie que vous pouvez simuler une date dans le passé ou dans le futur. Cependant, vous ne pouvez pas tester avant la date de début ou après la date de fin du Canvas.

Les étapes Message et Délai indiquent le moment où un utilisateur progresserait ou recevrait le message sans qu'il soit nécessaire de reconfigurer les délais. Notez que si les étapes indiquent si le timing intelligent est utilisé, cet aperçu du parcours de l'utilisateur ne permet pas de calculer une estimation pour un utilisateur test.

## Lorsque les utilisateurs entrent et sortent

Les utilisateurs test entreront dans l'aperçu même s'ils ne sont pas éligibles dans la vie réelle. S'ils ne sont pas éligibles, vous pouvez comprendre pourquoi ils n'ont pas rempli les critères. Lorsqu'un utilisateur test entre dans l'aperçu, nous supposons qu'il a répondu aux critères de l'audience cible et qu'il a effectué les critères de déclenchement de l'action. Par exemple, pour un Canvas qui utilise des événements personnalisés dans les critères d'entrée, l'utilisateur test est supposé avoir effectué l'événement personnalisé comme prévu dans les critères d'entrée. Cependant, si le même événement personnalisé est utilisé ailleurs dans le Canvas (comme dans les critères de sortie), réfléchissez à l'impact que cela pourrait avoir sur votre parcours utilisateur.

Les événements, les déclencheurs API, les attributs personnalisés et les propriétés d'entrée du Canvas sont appliqués en fonction de l'entrée du Canvas. Le test simule le parcours de l'utilisateur sans appliquer ces éléments pour modifier le profil utilisateur réel ou le flux du Canvas. Par exemple, lors des tests, lorsqu'un attribut personnalisé est utilisé comme déclencheur Canvas, les critères de déclenchement sont appliqués à l'aperçu de l'utilisateur **comme s'il** avait déclenché la modification de l'attribut personnalisé.

### Considération

Si vous testez un parcours d'action avec des actions qui correspondent à des critères de sortie (y compris des propriétés d'événement), les critères de sortie seront déclenchés et l'exécution du test se terminera. Si vous testez une étape du message qui correspond à des critères de sortie, les critères de sortie seront déclenchés et l'exécution du test prendra fin. 

À ce stade, vous ne pouvez pas sélectionner un événement ou une propriété spécifique au sein d'un parcours d'action pour déclencher des critères de sortie (uniquement le parcours dans son ensemble). Si un utilisateur peut potentiellement répondre à plusieurs critères de sortie, le premier qui est traité et auquel il répond est affiché comme résultat.

## Chemins d'expérience et variante du canvas

- Pour les toiles avec des variantes de niveau supérieur, sélectionnez une variante au début du test.
- Pour les chemins d'expérience, sélectionnez la variante par laquelle l'utilisateur progresse lorsque l'utilisateur test rencontre l'étape.
- Pour les chemins d'expérience utilisant le chemin personnalisé ou la variante gagnante, bien qu'il y ait une période d'attente pour l'utilisateur test dans une étape du message, ce délai n'est pas pris en compte car Braze suppose que l'utilisateur a progressé immédiatement dans la variante sélectionnée.

## Envoi de tests

Vous pouvez opter pour l'envoi de messages de test à un groupe interne de test ou à un utilisateur individuel au fur et à mesure que l'exécution du test se déroule. Cela signifie que seuls les messages que l'utilisateur rencontre sur le chemin du test seront envoyés. Les destinataires recevront les messages avec leurs attributs par défaut, mais vous pouvez les remplacer par les attributs de l'utilisateur test.

Pour envoyer tous les messages de test d'un canvas en une seule fois, quel que soit le chemin, et sans prévisualiser le chemin, vous pouvez sélectionner **Envoyer tous les messages de test** dans l'onglet **Envois de test.** 

## Réactivité

Les étapes du canvas sont sensibles au timing lors de la prévisualisation des parcours utilisateurs. Les mises à jour effectuées via l'étape de mise à jour de l'utilisateur sont reflétées dans les étapes suivantes du flux, mais ne sont pas appliquées au profil utilisateur proprement dit. Les effets de la saisie d'une variante par un utilisateur se reflètent dans les étapes futures d'un aperçu.

De même, les filtres reconnaîtront les actions qui se sont produites à la suite de l'interaction de l'utilisateur test avec d'autres étapes du canvas. Par exemple, ce mode de prévisualisation reconnaît qu'un utilisateur a rencontré une étape du message qui a été "envoyée" plus tôt dans le canvas, et il reconnaîtra que l'utilisateur test a "pris des mesures" pour avancer dans un parcours d'action.

Reportez-vous aux [critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) pour plus de détails sur le comportement réactif.

## Contenu connecté

Le contenu connecté sera exécuté s'il est inclus dans le canvas. Cela signifie que si vous testez un Canvas qui a des appels de contenu connecté ou des blocs de contenu qui contiennent du contenu connecté, le Canvas peut envoyer les appels de contenu connecté, ce qui modifierait les données référencées dans d'autres campagnes ou Canvas.

Lors de la prévisualisation des parcours utilisateurs, pensez à supprimer les contenus connectés qui modifient les profils utilisateurs ou les données référencées dans d'autres Canevas ou campagnes.

## Webhooks

Les webhooks s'exécuteront lors de l'envoi des messages de test, mais pas pendant l'exécution du test. Comme pour le contenu connecté, envisagez de supprimer les webhooks qui modifient les profils utilisateurs ou les données référencées dans d'autres Canevas ou campagnes.

## Cas d'utilisation

Dans ce scénario, le Canvas est mis en place pour cibler les utilisateurs qui n'ont pas eu de session dans une app. Ce parcours comprend une étape Message avec un e-mail de bienvenue, une étape Délai fixée à un jour et une étape Parcours d'audience qui se divise en deux parcours : les utilisateurs ayant au moins une session et tous les autres. En fonction du parcours d'audience dans lequel se trouve l'utilisateur, l'étape Message suivante sera envoyée.

Exemple de canvas avec une étape de message, une étape de délai, une étape de parcours audience et deux étapes de message.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Comme notre utilisateur test répond aux critères d'entrée du Canvas, il peut entrer dans le Canvas et suivre le parcours de l'utilisateur. Cependant, comme notre utilisateur test n'a pas ouvert l'application au cours du dernier jour calendrier, il continuera à suivre le chemin "Tous les autres" et recevra une notification push libellée comme suit : "Dernière chance ! Terminez votre première tâche pour obtenir un bonus exclusif".

La section "Résultats du test" qui montre que l'utilisateur test a satisfait aux critères d'entrée et fournit un résumé de son parcours, y compris les étapes qui lui ont été envoyées.]({% image_buster /assets/img/preview_user_path_results_example.png %})

