---
nav_title: "Boutons d'action push"
article_title: "Boutons d'action push"
page_order: 1
page_type: reference
description: "Cet article de référence traite de ce que sont les boutons d'action push et de la différence entre les plateformes iOS et Android."
channel:
  - Push

---

# Boutons d'action push

!Une notification push iOS avec deux boutons d'action push : Accepter et refuser.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Les boutons d'action push vous permettent de définir le contenu et les actions des boutons lorsque vous utilisez les notifications push de Braze iOS et Android. Grâce aux boutons d'action, vos utilisateurs peuvent interagir directement avec votre application depuis une notification sans avoir besoin de cliquer dans une expérience sur l'application.

## Création de boutons d'action

Chaque bouton interactif peut renvoyer à une page web ou à un lien profond ou ouvrir l'appli. 

- Pour les campagnes push standard, vous pouvez spécifier vos boutons d'action push dans la section **Comportement au clic** du compositeur de messages push dans le tableau de bord.
- Pour les [campagnes "quick push"]({{site.baseurl}}/quick_push), les boutons d'action peuvent être configurés séparément pour chaque plateforme sous l'onglet **Paramètres**.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Pour utiliser des boutons d'action dans vos envois push iOS, procédez comme suit :

1. Activez les boutons d'action dans l'onglet **Compose** pour une campagne standard ou dans l'onglet **Settings** pour un quick push.
2. Sélectionnez votre **catégorie de notification iOS** parmi les combinaisons de boutons disponibles suivantes :
 - Accepter / Refuser
 - Oui / Non
 - Confirmer / Annuler
 - Plus d'informations
 - Catégorie iOS personnalisée préenregistrée

\![Menu déroulant de la catégorie de notification iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
En raison de la gestion des boutons par iOS, vous devez effectuer des étapes d'intégration supplémentaires lors de la configuration des boutons d'action push, qui sont décrites dans notre [documentation destinée aux développeurs]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). En particulier, vous devez soit configurer les catégories iOS, soit choisir parmi certaines options de boutons par défaut. Pour les intégrations Android, ces boutons fonctionneront automatiquement.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Pour utiliser des boutons d'action dans vos envois push Android, procédez comme suit :

1. Activez les boutons d'action dans l'onglet **Compose** pour une campagne standard ou dans l'onglet **Settings** pour un quick push.
2. Sélectionnez <i class="fas fa-plus-circle"></i> **Ajouter un bouton** et indiquez le texte de votre bouton et son **comportement au clic.** Vous pouvez sélectionner l'une des actions suivantes :
  - Ouvrir l'application
  - Redirection vers l'URL
  - [Lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) vers l'application

Sélection de "Ouvrir l'application" comme comportement au clic pour un bouton de notification.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Vous pouvez ajouter jusqu'à trois boutons dans votre push.

#### Limites de caractères pour Android

Contrairement aux boutons iOS, qui sont empilés, les boutons Android sont affichés côte à côte dans une rangée. Cela signifie que plus vous ajoutez de boutons (jusqu'à trois), moins vous disposez d'espace pour la copie des boutons. 

\![Boutons d'action push Android avec texte tronqué.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

Le tableau suivant indique le nombre de caractères que vous pouvez ajouter avant que la copie de votre bouton ne soit tronquée, en fonction du nombre de boutons dont vous disposez :

| Nombre de boutons | Caractères maximum par bouton |
| --- | --- |
| 1 | 46 caractères |
| 2 | 20 caractères |
| 3 | 11 caractères |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

