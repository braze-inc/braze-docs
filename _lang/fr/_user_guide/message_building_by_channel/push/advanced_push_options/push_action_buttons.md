---
nav_title: "Boutons d'action push"
article_title: Boutons d'action push
page_order: 1
page_type: reference
description: "Le présent article de référence couvre les boutons d’action push et la différence entre les plates-formes iOS et Android."
channel:
  - Notification push

---

# Boutons d'action push

![Une notification push iOS avec deux boutons d’action push : Accepter et Refuser.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

> Le présent article de référence couvre les boutons d’action push et la différence entre les plates-formes iOS et Android. 

Les boutons d’action push vous permettent de définir du contenu et des actions pour les boutons lorsque vous utilisez les notifications push iOS et Android de Braze. Avec les boutons d’action, vos utilisateurs peuvent interagir directement avec votre application à partir d’une notification sans avoir besoin de cliquer sur une expérience sur l’application pour prendre des mesures.

## Comment utiliser les boutons d’action

Chaque bouton interactif peut se connecter à une page Web, un lien profond, ouvrir l’application ou rejeter la notification. Vous pouvez spécifier vos boutons d’action push dans la section **On Click Behavior** (Comportement lors du clic) du composeur de message de notification push dans le tableau de bord.

### Boutons d’action push iOS {#ios}

Pour utiliser des boutons d’action dans vos messages de notification push iOS, créez une [campagne de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) et activez les boutons d’action dans l’onglet **Compose** (Composer).

Sélectionnez ensuite votre **Notification Category** (Catégorie de notification). Vous pouvez sélectionner parmi les combinaisons de boutons disponibles suivantes :

- Accepter/Refuser
- Oui/Non
- Confirmer/Annuler
- Plus
- Catégorie personnalisée pré-enregistrée

![Menu déroulant Catégorie de notification iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

>  En raison de la façon dont sont traités les boutons par iOS, vous devrez effectuer des étapes d’intégration supplémentaires lors de la configuration des boutons d’action push, qui sont décrits dans notre [documentation du développeur]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/). En particulier, vous devrez configurer des catégories iOS ou vous devrez sélectionner parmi certaines options de bouton par défaut. Pour les intégrations Android, ces boutons fonctionnent automatiquement.

### Boutons d’action push Android {#android}

Pour utiliser des boutons d’action dans vos messages de notification push Android créez une [campagne de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) et activez les boutons de notification dans l’onglet **Compose** (Composer).

Cliquez ensuite sur <i class="fas fa-plus-circle"></i> **Add Button** (Ajouter un bouton) et spécifiez votre texte de bouton et le **On-Click Behavior** (Comportement lors du clic). Vous pouvez choisir parmi les actions disponibles suivantes :

- Ouvrir l’application
- Rediriger vers une URL Web
- [Lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) dans l’application
- Rejeter la notification

![]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Vous pouvez ajouter jusqu’à trois boutons dans votre notification push.

#### Limites de caractères

Contrairement aux boutons iOS qui sont empilés, les boutons Android sont affichés côte à côte dans une rangée. Cela signifie que plus vous ajoutez de boutons (jusqu’à trois), plus l’espace que vous avez pour votre texte de bouton est réduit. 

![Boutons d’action push Android avec texte tronqué.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%" }

Le tableau suivant donne le nombre de caractères que vous pouvez ajouter avant que votre texte de bouton soit tronqué, selon le nombre de boutons que vous avez :

| Nombre de boutons | Nombre max. de caractères par bouton |
| --- | --- |
| 1 | 46 caractères |
| 2 | 20 caractères |
| 3 | 11 caractères |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {% image_buster /assets/img_archive/push_action_example.png %}

