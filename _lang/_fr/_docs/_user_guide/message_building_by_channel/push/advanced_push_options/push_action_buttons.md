---
nav_title: "Boutons d'Action Push"
article_title: Boutons d'Action Push
page_order: 1
page_type: Référence
description: "Cet article de référence couvre ce que sont les boutons d'action push et la différence entre les plateformes iOS et Android."
channel:
  - Pousser
---

# Appuyer sur les boutons d'action

!\[Boutons d'Action Push\]\[1\]{: style="float:right;max-width:40%;margin-left:15px;"}

> Cet article de référence couvre ce que sont les boutons d'action push et la différence entre les plateformes iOS et Android.

Les boutons d'action push vous permettent de définir du contenu et des actions pour les boutons lors de l'utilisation des notifications push iOS et Android de Braze. Grâce aux boutons d'action, vos utilisateurs peuvent interagir directement avec votre application à partir d'une notification sans avoir à cliquer sur une application pour agir.

## Comment utiliser les boutons d'action

Chaque bouton interactif peut créer un lien vers une page Web, un lien profond, ouvrir l'application ou rejeter la notification. Vous pouvez spécifier vos boutons d'action push dans la section **On Click Behavior** du compositeur de messages push dans le tableau de bord.

### Boutons d'action push iOS {#ios}

Pour utiliser les boutons d'action dans vos messages push iOS, créez une [campagne push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) et activez les boutons d'action dans l'onglet **Composer**.

![Activer les boutons d'action push]({% image_buster /assets/img_archive/push_action_enable.png %}){: style="largeur-max-60%"}

Sélectionnez ensuite votre **Catégorie de Notification**. Vous pouvez sélectionner parmi les combinaisons de boutons disponibles suivantes:

- Accepter / refuser
- Oui / Non
- Confirmer / Annuler
- En savoir plus
- Catégorie personnalisée préenregistrée

![Boutons d'action Push iOS]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="largeur-max-70%"}

> En raison de la gestion des boutons par iOS, vous devrez effectuer des étapes d'intégration supplémentaires lors de la configuration des boutons d'action push, qui sont décrits dans notre [documentation développeur]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/). En particulier, vous devrez soit configurer les catégories iOS, soit sélectionner à partir de certaines options du bouton par défaut. Pour les intégrations Android, ces boutons fonctionneront sans problème.

### Boutons d'action push Android {#android}

Pour utiliser les boutons d'action dans vos messages push Android, créez une [campagne push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) et activez les boutons de notification dans l'onglet **Composer**.

![Activer les boutons d'action push]({% image_buster /assets/img_archive/push_action_enable2.png %}){: style="largeur-max-60%"}

Puis cliquez sur <i class="fas fa-plus-circle"></i> **Ajouter le bouton** et spécifiez le texte de votre bouton et **Comportement au clic sur**. Vous pouvez sélectionner parmi les actions disponibles suivantes :

- Ouvrir l'application
- Rediriger vers l'URL Web
- [Lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) vers l'application
- Rejeter la notification

Vous pouvez ajouter jusqu'à trois boutons à votre appui.

![Boutons d'action de poussée Android]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="largeur-max-70%"}

#### Limites de caractères

Contrairement aux boutons iOS, qui sont empilés, les boutons Android sont affichés côte à côte dans une rangée. Cela signifie que plus vous ajoutez de boutons (jusqu'à trois), moins vous avez d'espace pour votre copie de bouton.

![Boutons d'action push Android avec texte tronqué]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="largeur-max:50%" }

Le tableau suivant indique combien de caractères vous pouvez ajouter avant que la copie de votre bouton soit tronquée, selon le nombre de boutons que vous avez :

| Nombre de boutons | Nombre maximum de caractères par bouton |
| ----------------- | --------------------------------------- |
| 1                 | 46 caractères                           |
| 2                 | 20 caractères                           |
| 3                 | 11 caractères                           |
{: .reset-td-br-1 .reset-td-br-2}
[1]: {% image_buster /assets/img_archive/push_action_example.png %} [2]: {% image_buster /assets/img_archive/push_action_enable.png %}

