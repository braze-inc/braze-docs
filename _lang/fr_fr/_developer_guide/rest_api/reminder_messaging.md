---
nav_title: Messages de rappel choisis par l'utilisateur
article_title: Messages de rappel choisis par l'utilisateur
page_order: 5
page_type: reference
description: "Cet article de référence explique comment utiliser les pages d'accueil Braze, les attributs personnalisés et les campagnes pour permettre aux utilisateurs de s'inscrire à des messages de rappel personnalisés concernant des événements ou rendez-vous à venir."
---

# Messages de rappel choisis par l'utilisateur

> Utilisez les [pages d'accueil]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) Braze, les attributs personnalisés et les campagnes pour permettre aux utilisateurs de choisir quand ils souhaitent recevoir des messages de rappel concernant des événements ou rendez-vous à venir. Cette approche permet aux utilisateurs non techniques de Braze de créer et modifier le contenu des pages d'inscription aux rappels, tandis que les préférences sélectionnées par les utilisateurs peuvent alimenter la segmentation, le ciblage et la personnalisation de l'ensemble de vos messages propulsés par Braze.

Avec cette approche, vous pouvez :

- Permettre aux utilisateurs de choisir eux-mêmes la date de leur message de rappel par rapport à un événement à venir.
- Recueillir les préférences directement auprès des utilisateurs via une page d'accueil Braze et les enregistrer dans les profils utilisateurs, sans infrastructure backend supplémentaire.
- Envoyer les messages aux dates choisies par les utilisateurs, afin que les messages restent pertinents et basés sur le consentement.
- Étendre le cas d'usage avec des fonctionnalités Braze supplémentaires, telles que les délais de message, le reciblage de suivi et le test A/B.

## Conditions préalables

Pour suivre ce guide, vous avez besoin de :

| Condition | Description |
| --- | --- |
| Accès aux pages d'accueil | Accès et autorisations pour créer des [pages d'accueil]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) dans Braze. |
| Connaissances en HTML et JavaScript | Familiarité de base avec HTML et JavaScript pour personnaliser votre page d'accueil. Requis uniquement pour l'[Option B](#option-b-personal-dates-custom-code-block). |
| Connaissances en Liquid | Familiarité de base avec [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour créer des modèles de variables personnalisées. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 1 : Créer une page d'accueil et y renvoyer depuis un message

Commencez par [créer une page d'accueil Braze]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/). Ensuite, créez un message (par exemple un e-mail) qui redirige les utilisateurs vers la page d'accueil.

{% raw %}
Pour associer automatiquement l'activité de la page d'accueil au profil utilisateur du destinataire, utilisez l'étiquette Liquid `{% landing_page_url %}` lorsque vous créez un lien vers la page depuis un message Braze. Par exemple :

```html
<a href="{% landing_page_url your-page-url-handle %}">Sign up for reminders</a>
```
{% endraw %}

Lorsqu'un utilisateur clique sur ce lien, Braze l'identifie automatiquement, de sorte que toutes les préférences soumises sont enregistrées dans son profil existant, sans paramètres d'URL manuels. Pour un guide complet, consultez [Suivre les utilisateurs via un formulaire]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/).

## Étape 2 : Recueillir les préférences sur la page d'accueil

La manière de recueillir les préférences des utilisateurs dépend de la nature des dates collectées : dates partagées ou dates personnelles. Choisissez l'option qui correspond à votre cas d'usage.

### Option A : Dates partagées (blocs de formulaire par glisser-déposer)

Pour les événements où de nombreux utilisateurs partagent la même date (comme les jours fériés ou les événements sportifs), utilisez les [blocs de formulaire **Case à cocher**]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks) intégrés à l'éditeur par glisser-déposer pour recueillir les préférences. Chaque case à cocher définit nativement un attribut personnalisé de type booléen (`true` ou `false`) sur le profil de l'utilisateur lors de la soumission du formulaire, sans code personnalisé nécessaire.

Par exemple, ajoutez une case à cocher intitulée « Rappel Super Bowl 2026 » qui correspond à l'attribut personnalisé `super_bowl_2026_reminder`. Lorsqu'un utilisateur coche la case et soumet le formulaire, Braze définit :

```
super_bowl_2026_reminder = true
```

Ces attributs booléens peuvent ensuite être utilisés directement dans les [filtres de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) pour constituer votre audience cible.

### Option B : Dates personnelles (bloc de code personnalisé)

Pour les dates propres à chaque utilisateur (comme les anniversaires de naissance ou de mariage), utilisez un [bloc **Code personnalisé**]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#basic-blocks) sur votre page d'accueil pour capturer la date et l'enregistrer dans Braze via l'API `lpBridge`. Cette approche vous offre un champ de saisie de date (ou un sélecteur) et vous permet de stocker les préférences dans un [tableau imbriqué d'objets d'attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/array_of_objects/), ce que les blocs de formulaire par glisser-déposer ne prennent pas en charge.

Lorsque les utilisateurs arrivent via l'étiquette Liquid {% raw %}`{% landing_page_url %}`{% endraw %}, Braze sait déjà qui ils sont, votre script n'a donc qu'à :

1. Écouter le clic sur le bouton de soumission du formulaire.
2. Lire la valeur de date depuis votre champ de saisie personnalisé.
3. Utiliser l'API `lpBridge` pour définir des attributs personnalisés imbriqués et envoyer les données à Braze.

Stockez ces préférences à l'aide d'un tableau imbriqué d'objets d'attributs personnalisés. Cette structure vous permet de stocker plusieurs rappels par utilisateur et d'ajouter ultérieurement des champs dérivés, tels que `next_reminder_name` ou `last_reminder_date`.

#### Exemple de script

L'exemple de script suivant désactive le comportement par défaut du bouton et exécute des méthodes personnalisées au clic. Remplacez les ID d'éléments et les valeurs d'attributs par les vôtres.

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

  // Wait for page content to load
  document.addEventListener("DOMContentLoaded", () => {
    // Remove the default redirect event from the Braze Message Handler Script
    props[registerButtonId].onclickContract[0].brazeEvents =
      props[registerButtonId].onclickContract[0].brazeEvents.filter(
        (event) => event.eventType !== "REDIRECT"
      );

    const registerButton = document.getElementById(registerButtonId);
    if (registerButton) {
      registerButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Set the custom attribute (replace with your actual key/value)
        await window.lpBridge.setCustomUserAttribute("key", "value");

        // Flush data to Braze
        await window.lpBridge.requestImmediateDataFlush();

        // Remove the button and update the message
        registerButton.remove();
        const messageDiv = document.getElementById(messageDivId);
        if (messageDiv) {
          messageDiv.innerHTML = successMessage;
        }
      });
    }
  });
</script>
```

Pour trouver les ID d'éléments de vos composants de page d'accueil, prévisualisez votre page, faites un clic droit et sélectionnez **Inspecter** dans votre navigateur. Repérez les ID du bouton et des composants de message dans le HTML.

## Étape 3 : Configurer et déclencher les messages de rappel

Après avoir collecté les attributs personnalisés via la page d'accueil, créez des campagnes pour envoyer des messages aux utilisateurs concernant les événements à venir.

### Option A : Dates partagées {#step-3-option-a-shared-dates}

Si vous avez utilisé des attributs personnalisés booléens (Option A de l'[Étape 2](#option-a-shared-dates-dnd-form-blocks)), utilisez cet attribut comme filtre de segment pour constituer l'audience de votre message de rappel. Créez ensuite une nouvelle campagne, planifiée avant l'événement, pour cibler ce groupe avec le contenu de votre choix.

### Option B : Dates personnelles {#step-3-option-b-personal-dates}

Si vous avez utilisé des attributs personnalisés imbriqués (Option B de l'[Étape 2](#option-b-personal-dates-custom-code-block)), utilisez le filtre d'audience **Attribut personnalisé imbriqué** pour sélectionner tous les utilisateurs dont la date de rappel se situe dans une fenêtre spécifique, par exemple dans deux jours.

Pour envoyer des rappels de manière continue, configurez une campagne récurrente quotidienne afin que chaque jour, les utilisateurs dont les rappels à venir se situent dans votre fenêtre reçoivent leurs messages.

## Étape 4 : Vérifier votre intégration

Une fois la configuration terminée, vérifiez votre intégration :

1. Envoyez-vous un lien vers la page d'accueil et remplissez le formulaire.
2. Accédez à votre profil utilisateur dans le tableau de bord de Braze et confirmez que l'attribut personnalisé apparaît.
3. Envoyez un message de rappel test à votre profil et vérifiez que les détails personnalisés s'affichent correctement.
4. Surveillez attentivement les résultats lors du lancement de votre campagne.

## Points à prendre en compte

- Pour un exemple détaillé d'envoi de messages basés sur des attributs personnalisés de type date, consultez le cas d'usage e-mail dans le [guide d'envoi de messages via l'API REST]({{site.baseurl}}/developer_guide/rest_api/messaging/).
- Si vous dupliquez une page d'accueil ou remplacez des champs, les ID des composants changent. Mettez à jour votre bloc de code personnalisé pour refléter les nouveaux ID.
- Les attributs personnalisés imbriqués consomment des [points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) pour chaque clé du tableau d'objets. La mise à jour d'un objet d'attribut personnalisé à null consomme également un point de donnée.
- Le code présenté dans ce guide est fourni à titre d'exemple illustratif. Testez minutieusement l'ensemble du code et des composants dans votre environnement avant tout déploiement en production.