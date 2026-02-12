---
nav_title: Flux WhatsApp
article_title: Flux WhatsApp
page_order: 1
description: "Cet article de référence présente les étapes à suivre pour créer un message WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# Flux WhatsApp

> WhatsApp Flows est une amélioration du canal WhatsApp existant, qui vous permet de créer des expériences d'envoi de messages interactives et dynamiques. Cette page fournit des instructions étape par étape pour l'utilisation de WhatsApp Flows.

## Configurer les flux WhatsApp

1. Connectez-vous à votre compte Meta.
2. Créez des flux à partir de l'un des deux emplacements/localisations principaux :
    - **Outils de compte :** Allez dans l'onglet **Flux** pour afficher l'ID du flux et créer un nouveau flux.
    - **Gérer les modèles :** C'est la méthode recommandée pour créer des flux. Ici, vous pouvez générer des modèles et sélectionner une option de flux au cours du processus de création du modèle.

![WhatsApp Manager avec une page pour créer un modèle de flux.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Sélectionnez un flux existant ou créez-en un. Si vous créez un flux, vous avez le choix entre deux options :
  - **Formulaire personnalisé :** Pour des besoins spécifiques
  - **Éléments préconçus :** Pour une configuration plus rapide

## Configurer les messages et les réponses de WhatsApp Flow

{% tabs local %}
{% tab Template message %}

1. Dans un canvas de Braze, créez une étape du message canvas qui utilise le message modèle contenant le Flow correspondant.
2. Poursuivez la création de votre modèle. Si nécessaire, ajoutez des médias, un contenu variable ou les deux à votre message. Votre sélection de flux est choisie lors de la création du modèle, il n'est donc pas nécessaire de fournir des informations supplémentaires pour l'expérience de flux.

![Composez votre message WhatsApp à l'aide d'un modèle de flux WhatsApp.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Dans un canvas de Braze, créez une étape du message canvas qui utilise un message de réponse et un message de flux.

![Une étape de message pour un type de message de réponse WhatsApp et la présentation du message Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Sélectionnez le flux correspondant, puis continuez à créer votre message. 

![Un compositeur de réponse de message de flux avec une liste déroulante étendue pour la sélection d'un flux.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Prévisualisation du flux

Avant de lancer un Canvas avec un Flow, vous pouvez sélectionner Aperçu **du Flow** pour prévisualiser le Flow directement dans Braze afin de confirmer qu'il se comporte comme prévu. Vous pouvez également interagir avec le flux dans l'aperçu pour expérimenter la manière dont un utilisateur naviguerait dans le flux, puis procéder à des ajustements en temps réel. Si un flux contient plusieurs pages, vous pouvez interagir avec chaque page.

![Fenêtre de prévisualisation affichant un formulaire permettant à un utilisateur de terminer son inscription.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Enregistrer l'intégralité de la réponse au flux {#full-flow}

Lorsque vous intégrez un message WhatsApp Flow dans un canvas ou une campagne de Braze, vous pouvez vouloir capturer et utiliser des informations spécifiques que les utilisateurs soumettent par le biais du Flow. Braze a besoin de recevoir des informations supplémentaires concernant la structure de la réponse de l'utilisateur, en particulier la forme attendue de la réponse JSON, pour générer le schéma d'attribut personnalisé imbriqué (NCA) requis.

### Étape 1 : Générer l'attribut personnalisé Flow

{% tabs local %}
{% tab Recommended method %}

Le moyen le plus simple de fournir à Braze les informations relatives à la structure de la réponse est d'enregistrer la réponse au flux en tant qu'attribut personnalisé et d'effectuer un envoi test.

#### Utilisation d'un flux qui n'a pas été utilisé dans Braze

Si vous utilisez un flux qui n'a jamais été utilisé auparavant dans Braze, il se peut qu'aucune information ne s'affiche dans la section **Attribut personnalisé** du **flux** dans les **messages de composition.** Cela signifie que le schéma n'a pas encore été généré.

![Section Meta Flow avec une option permettant d'afficher l'attribut personnalisé du flux.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Pour résoudre ce problème, procédez comme suit :

1. Terminez l'étape de configuration de votre message WhatsApp.
2. Confirmez que vous avez coché la case **Enregistrer les réponses au flux en tant qu'attribut personnalisé**.

![Section Meta Flow avec une case à cocher permettant d'enregistrer les réponses au flux en tant qu'attribut personnalisé.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Envoyez un message test et complétez le flux en tant qu'utilisateur.

Maintenant, Braze dispose de la forme de la réponse JSON du flux et peut générer l'attribut personnalisé.

{% endtab %}
{% tab Alternative methods %}

Utilisez l'éditeur JSON avancé pour enregistrer les attributs de la réponse au flux dans des attributs personnalisés, ou utilisez un Canvas en plusieurs étapes pour enregistrer la réponse dans un attribut personnalisé imbriqué. 

{% subtabs %}
{% subtab Advanced JSON editor %}

Dans l'éditeur JSON avancé, entrez {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, où “flow_1” est l'attribut personnalisé dans lequel vous souhaitez que le flux soit enregistré.

![Étape de mise à jour par l'utilisateur avec un éditeur JSON avancé.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Confirmez que vous avez déjà créé un attribut personnalisé avec le type de données d'objet ("flow_1" dans cet exemple) dans les paramètres de données de votre espace de travail.
2. Dans l'éditeur d'interface utilisateur, utilisez Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` pour remplir l'attribut personnalisé et enregistrer l'intégralité de la réponse Flow de l'utilisateur. Vous devez renseigner la valeur de la clé à l'adresse ```{{whats_app.${inbound_flow_response}}}```{% endraw %} avant de sélectionner l'attribut personnalisé que vous avez créé.

![Étape de mise à jour de l'utilisateur qui utilise l'éditeur d'interface utilisateur.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Une fois que Braze a reçu une réponse de Flow, nous enregistrons l'attribut personnalisé imbriqué avec le nom prescrit dans le profil utilisateur. Cet attribut personnalisé peut être utilisé lorsque vous créez des toiles. 

![Une fenêtre affichant le contenu d'un attribut personnalisé "flow_1".]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 2 : Visualiser la réponse au flux enregistrée

Lorsque le flux est terminé, Braze crée automatiquement un attribut personnalisé de flux dont le nom est basé sur l'ID du flux. Vous pouvez ensuite accéder au profil utilisateur pour afficher la réponse Flow enregistrée sous la forme d'un objet imbriqué dans la section **Attributs personnalisés**.

Une fois le schéma généré, la section **Attribut personnalisé** du flux affiche la structure attendue, y compris les types de données prévus pour chaque réponse (par exemple, "Chaîne" ou "Tableau de chaînes").

![Fenêtre de détail des attributs personnalisés du flux avec liste déroulante des schémas.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Considérations

- **Attributs existants :** Si un attribut personnalisé pour un flux particulier est déjà généré, le flux se chargera avec les informations d'attribut disponibles. Dans ces cas, vous n'avez pas besoin d'envoyer un message de test pour générer le schéma, car Braze reconnaît déjà les messages de réponse attendus.
- **Changements de flux :** Si vous apportez des modifications au flux après la génération du schéma, vous devez envoyer un message de test supplémentaire pour que Braze puisse comprendre que la forme de la réponse au flux a changé et ajuster la structure des attributs en conséquence. Cette action est limitée à une fois toutes les 24 heures. 
- **Cohérence :** L'attribut personnalisé du flux généré est cohérent et sera le même attribut pour ce flux spécifique, quel que soit le canevas dans lequel il est utilisé.
- **Option manuelle :** Vous n'êtes pas obligé de cocher la case **Enregistrer les réponses au flux en tant qu'attribut personnalisé**. Vous pouvez générer manuellement l'attribut personnalisé en [enregistrant des champs spécifiques des réponses au flux dans un attribut personnalisé spécifique](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), ce qui évite de dupliquer les étapes de l'utilisateur.

## Enregistrer des champs spécifiques des réponses au flux dans un attribut personnalisé spécifique 

### Étape 1 : Créer un parcours d'action

Créez une étape du [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) Canvas ou une campagne basée sur l'action. Sélectionnez un déclencheur d'**envoi d'un message entrant WhatsApp** et une condition de **flux répondu**, puis sélectionnez le flux concerné ou **N'importe quel flux**.

![Un déclencheur pour les utilisateurs qui ont envoyé un message WhatsApp entrant et répondu à un quelconque Flow.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Étape 2 : Extraire les champs des réponses au flux

Vous pouvez utiliser des attributs personnalisés imbriqués ou l'étiquette Liquid `json_parse` pour extraire des champs spécifiques des réponses au flux.

{% tabs %}
{% tab Nested custom attributes %}

Pour enregistrer des parties spécifiques de la réponse de l'utilisateur au flux, suivez toutes les étapes de la section [Enregistrement de la réponse complète au flux](#full-flow), **y compris le lancement du Canvas**. Le Canvas doit être lancé pour créer l'attribut personnalisé imbriqué auquel vous ferez référence. Après avoir lancé le canvas et terminé un flux, effectuez les étapes suivantes :

1. Créez une étape ultérieure de mise à jour de l'utilisateur qui utilise l'éditeur d'interface utilisateur.
2. Sélectionnez **Ajouter une personnalisation**, puis sélectionnez **Attribut personnalisé imbriqué** et l'attribut de niveau supérieur correspondant où le flux est stocké.  

![Étape de mise à jour de l'utilisateur avec une personnalisation par attributs personnalisés imbriqués.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Sélectionnez l'attribut clé que vous souhaitez enregistrer et insérez le liquide dans le champ **Valeur clé.** 

![Fenêtre pour "flow_1" avec des attributs à sélectionner.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Choisissez l'attribut dans lequel vous souhaitez le stocker.
5\. Envoyez un message d'essai pour tester le flux.

{% endtab %}
{% tab Parse function %}

Utilisez l'étiquette Liquid de `json_parse` pour extraire des réponses spécifiques du flux. Par exemple, vous pouvez sortir le jeton de flux et les options sélectionnées pour personnaliser un message de suivi.

Dans l'éditeur d'interface utilisateur, sélectionnez les éléments suivants : 

- **Nom de l'attribut :** YOUR_CUSTOM_ATTRIBUTE (dans cet exemple : “First_name”)
- **Action :** Mettre à jour
- **Valeur clé :** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![Compositeur de messages WhatsApp avec un composant "Ajouter une personnalisation" pour insérer une personnalisation des propriétés WhatsApp avec l'attribut personnalisé `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Lorsque vous êtes prêt, envoyez un message d'essai pour tester le flux. Ensuite, lancez le Canvas !

{% endtab %}
{% endtabs %}

{% alert note %}
Un nouveau message WhatsApp " efface " la capacité du Canvas à utiliser (et à réutiliser) la réponse Liquid Flow. Veillez donc à ce que les messages de suivi soient envoyés après toutes les étapes de mise à jour de l'utilisateur, les webhooks ou les autres étapes qui utilisent la réponse Liquid Flow.
{% endalert %}

## Ajout d'une étiquette de personnalisation du flux

Pour utiliser la réponse Flow via Liquid avec les [étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), procédez comme suit :

1. Lors de la composition de votre message WhatsApp, sélectionnez l'icône plus pour ouvrir la fenêtre **Ajouter une personnalisation** 
2. Sélectionnez **Propriétés WhatsApp** pour le type de personnalisation et **inbound_flow_response** pour l'attribut personnalisé. Cela permet d'enregistrer des informations dans les profils utilisateurs, de les inclure dans des messages ou de les transmettre à d'autres services, comme les webhooks.

![Compositeur de messages WhatsApp avec un composant "Ajouter une personnalisation" pour insérer une personnalisation des propriétés WhatsApp avec l'attribut personnalisé inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Pour toute question ou assistance supplémentaire, contactez le [service d'assistance.]({{site.baseurl}}/braze_support/)