---
nav_title: Flux WhatsApp
article_title: Flux WhatsApp
page_order: 1
description: "Cet article de référence décrit les étapes nécessaires à la création et à la conception d'un message WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# Flux WhatsApp

> WhatsApp Flows est une amélioration du canal de communication WhatsApp existant, qui vous permet de créer des expériences de communication interactives et dynamiques. Cette page fournit des instructions détaillées pour l'utilisation de WhatsApp Flows.

## Configuration de WhatsApp Flows

1. Veuillez vous connecter à votre compte Meta.
2. Veuillez créer des flux à partir de l'un des deux emplacements/localisations principaux :
    - **Outils de gestion de compte :** Veuillez vous rendre dans l'onglet **Flux** pour afficher l'ID du flux et créer un nouveau flux.
    - **Gestion des modèles :** Il s'agit de la méthode recommandée pour créer des flux. Ici, vous pouvez générer des modèles et sélectionner une option Flow pendant le processus de création du modèle.

![Gestionnaire WhatsApp avec une page permettant de créer un modèle Flows.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Veuillez sélectionner un flux existant ou en créer un. Lors de la création d'un flux, veuillez choisir parmi deux options :
  - **Formulaire personnalisé :** Pour des exigences spécifiques
  - **Éléments prédéfinis :** Pour une configuration plus rapide

## Configuration des messages et des réponses WhatsApp Flow

{% tabs local %}
{% tab Template message %}

1. Dans Braze Canvas, veuillez créer une étape de message WhatsApp qui utilise le modèle de message contenant le flux correspondant.
2. Veuillez poursuivre la création de votre modèle. Si nécessaire, veuillez ajouter des médias, du contenu variable ou les deux à votre message. Votre sélection de flux est choisie lors de la création du modèle, donc aucune information supplémentaire n'est requise pour l'expérience de flux.

![Compositeur de messages WhatsApp utilisant un modèle WhatsApp Flow.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Dans Braze Canvas, veuillez créer une étape de message WhatsApp qui utilise un message de réponse et un message de flux.

![Étape de message pour un type de message de réponse WhatsApp et une mise en page de message Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Veuillez sélectionner le flux approprié, puis poursuivez la création de votre message. 

![Un éditeur de réponse de message Flow avec un menu déroulant étendu permettant de sélectionner un flux.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Prévisualisation du flux

Avant de lancer un canvas avec un flux, vous pouvez sélectionner **« Aperçu du flux** » pour prévisualiser le flux directement dans Braze et vérifier qu'il se comporte comme prévu. Vous pouvez également interagir avec le flux dans l'aperçu afin de découvrir comment un utilisateur naviguerait dans le flux, puis effectuer des ajustements en temps réel. Si un flux contient plusieurs pages, vous pouvez interagir avec chacune d'entre elles.

![Fenêtre d'aperçu affichant un formulaire permettant à l'utilisateur de finaliser son inscription.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Enregistrement de la réponse Flow complète {#full-flow}

Lorsque vous intégrez un message WhatsApp Flow dans un Braze Canvas ou une campagne, vous pouvez souhaiter capturer et utiliser des informations spécifiques que les utilisateurs soumettent via le Flow. Braze a besoin de recevoir des informations supplémentaires concernant la structure de la réponse utilisateur, en particulier la forme attendue de la réponse JSON, afin de générer le schéma d'attributs personnalisés imbriqués (NCA) requis.

### Étape 1 : Générer l'attribut personnalisé Flow

{% tabs local %}
{% tab Recommended method %}

La méthode la plus simple pour fournir à Braze les informations relatives à la structure de réponse consiste à enregistrer la réponse Flow en tant qu'attribut personnalisé et à effectuer un envoi test.

#### Utilisation d'un flux qui n'a pas été utilisé dans Braze

Si vous utilisez un flux qui n'a jamais été utilisé auparavant dans Braze, il est possible que vous ne voyiez aucune information lorsque vous consultez la section **Attributs personnalisés du flux** dans la fenêtre **Composer des messages**. Cela signifie que le schéma n'a pas encore été généré.

![Section Meta Flow avec une option permettant d'afficher l'attribut personnalisé Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Pour résoudre ce problème, veuillez suivre les étapes suivantes :

1. Veuillez terminer la configuration de votre étape de message WhatsApp.
2. Veuillez vérifier que vous avez coché **Enregistrer les réponses au flux en tant qu'attribut personnalisé**.

![Section Meta Flow avec une case à cocher pour enregistrer les réponses Flow en tant qu'attribut personnalisé.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Veuillez vous envoyer un message test et terminer le flux en tant qu'utilisateur.

Braze dispose désormais de la forme du JSON de réponse Flow et peut générer l'attribut personnalisé.

{% endtab %}
{% tab Alternative methods %}

Veuillez utiliser l'éditeur JSON avancé pour enregistrer les attributs de la réponse Flow dans des attributs personnalisés, ou utilisez un canvas en plusieurs étapes pour enregistrer la réponse dans un attribut personnalisé imbriqué. 

{% subtabs %}
{% subtab Advanced JSON editor %}

Dans l'éditeur JSON avancé, veuillez saisir {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, où“flow_1”  est l'attribut personnalisé sous lequel vous souhaitez enregistrer le flux.

![Étape de mise à jour utilisateur avec un éditeur JSON avancé.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Veuillez vérifier que vous avez déjà créé un attribut personnalisé avec le type de ("flow_1"données d'objet (dans cet exemple) dans les paramètres de données de votre espace de travail.
2. Dans l'éditeur d'interface utilisateur, veuillez utiliser Liquid{% raw %}```{{whats_app.${inbound_flow_response}}}```pour remplir l'attribut personnalisé et enregistrer l'intégralité de la réponse Flow de l'utilisateur. Il est nécessaire de remplir la valeur de la clé ```{{whats_app.${inbound_flow_response}}}```{% endraw %}avant de sélectionner l'attribut personnalisé que vous avez créé.

![Étape de mise à jour utilisateur qui utilise l'éditeur d'interface utilisateur.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Une fois que Braze aura reçu une réponse Flow, nous enregistrerons l'attribut personnalisé imbriqué avec le nom prescrit dans le profil utilisateur. Cet attribut personnalisé peut être utilisé lors de la création de canevas. 

![Une fenêtre affichant le contenu d'un "flow_1"attribut personnalisé.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 2 : Afficher la réponse Flow enregistrée

Une fois le flux terminé, Braze crée automatiquement un attribut personnalisé pour le flux, dont le nom est basé sur l'ID du flux. Vous pouvez ensuite vous rendre dans le profil utilisateur pour afficher la réponse Flow enregistrée en tant qu'objet imbriqué dans la section **Attributs personnalisés**.

Une fois le schéma généré, la section **Attribut personnalisé** du flux affichera la structure attendue, y compris les types de données prévus pour chaque réponse (par exemple, « Chaîne de caractères » ou « Tableau de chaînes de caractères »).

![Fenêtre de détails des attributs personnalisés du flux avec menu déroulant du schéma.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Considérations

- **Attributs existants :** Si un attribut personnalisé pour un flux particulier a déjà été généré, le flux se chargera avec les informations d'attribut disponibles. Dans ces cas, il n'est pas nécessaire d'envoyer un message test pour générer le schéma, car Braze reconnaît déjà les messages de réponse attendus.
- **Modifications du débit :** Si vous apportez des modifications au flux après la génération du schéma, il est nécessaire d'envoyer un message de test supplémentaire afin que Braze puisse détecter que la forme de la réponse du flux a changé et ajuster la structure des attributs en conséquence. Cette action est limitée à une fois toutes les 24 heures. 
- **Cohérence :** L'attribut personnalisé Flow généré est cohérent et sera le même pour ce Flow spécifique, quel que soit le canvas dans lequel il est utilisé.
- **Option manuelle :** Il n'est pas nécessaire de cocher la case **Enregistrer les réponses au flux en tant qu'attribut personnalisé**. Vous pouvez générer manuellement l'attribut personnalisé en [enregistrant des champs spécifiques provenant des réponses Flow dans un attribut personnalisé spécifique](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), ce qui évite de dupliquer les étapes utilisateur.

## Enregistrement de champs spécifiques provenant des réponses Flow dans un attribut personnalisé spécifique 

### Étape 1 : Créer un parcours d’action

Veuillez créer une étape du canvas [du parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) ou une campagne basée sur une action. Veuillez sélectionner un déclencheur **« Envoyer un message WhatsApp entrant** » et une condition **de flux « Répondu »**, puis sélectionnez le flux pertinent ou **« Tout flux** ».

![Déclencheur pour les utilisateurs ayant envoyé un message WhatsApp entrant et répondu à un flux.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Étape 2 : Extraire des champs à partir des réponses Flow

Vous pouvez utiliser des attributs personnalisés imbriqués ou l'étiquette`json_parse`Liquid pour extraire des champs spécifiques des réponses Flow.

{% tabs %}
{% tab Nested custom attributes %}

Pour enregistrer des parties spécifiques de la réponse Flow de l'utilisateur, veuillez suivre toutes les étapes décrites dans [la section Enregistrement de la réponse Flow complète](#full-flow), **y compris le lancement du canvas**. Il est nécessaire de lancer Canvas pour créer l'attribut personnalisé imbriqué auquel vous ferez référence. Après avoir lancé Canvas et terminé un flux, veuillez suivre les étapes suivantes :

1. Veuillez créer une étape de mise à jour utilisateur supplémentaire à l'aide de l'éditeur d'interface utilisateur.
2. Veuillez sélectionner **Ajouter une personnalisation**, puis sélectionnez **Attribut personnalisé imbriqué** et l'attribut de niveau supérieur correspondant où le flux est stocké.  

![Étape de mise à jour utilisateur avec personnalisation des attributs personnalisés imbriqués.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Veuillez sélectionner l'attribut clé que vous souhaitez enregistrer et insérer le liquid dans le champ **Valeur clé**.

![Fenêtre pour"flow_1"  avec des attributs à sélectionner.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Veuillez sélectionner l'attribut dans lequel vous souhaitez l'enregistrer.
5\. Veuillez envoyer un message test afin de vérifier le bon fonctionnement du flux.

{% endtab %}
{% tab Parse function %}

Veuillez utiliser l'étiquette`json_parse`Liquid pour extraire des réponses spécifiques du flux. Par exemple, vous pouvez extraire le jeton Flow et les options sélectionnées pour créer un message de suivi personnalisé.

Dans l'éditeur d'interface utilisateur, veuillez sélectionner les éléments suivants : 

- **Nom de l'attribut :**YOUR_CUSTOM_ATTRIBUTE(dans cet exemple : “First_name”)
- **Action :** Mettre à jour
- **Valeur clé :** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![Éditeur de messages WhatsApp avec un composant « Ajouter une personnalisation » permettant d'insérer une personnalisation des propriétés WhatsApp avec l'attribut personnalisé`inbound_flow_response`.]({%image_buster/assets/img/whatsapp/flows/parsed_json.png %})

Une fois que vous êtes prêt, veuillez envoyer un message test pour vérifier le bon fonctionnement du flux. Veuillez ensuite lancer Canvas.

{% endtab %}
{% endtabs %}

{% alert note %}
Un nouveau message WhatsApp « efface » la capacité du Canvas à utiliser (et réutiliser) la réponse Liquid Flow. Veuillez donc vous assurer que les messages de suivi sont envoyés après toutes les étapes de mise à jour utilisateur, les webhooks ou autres étapes qui utilisent la réponse Liquid Flow.
{% endalert %}

## Ajout d'une étiquette de personnalisation Flow

Pour utiliser la réponse Flow via Liquid avec [les étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), veuillez suivre les étapes suivantes :

1. Lorsque vous rédigez votre message WhatsApp, veuillez sélectionner l'icône « + » pour ouvrir la fenêtre **« Ajouter une personnalisation ».**
2. Veuillez sélectionner **les propriétés WhatsApp** pour le type de personnalisation et**inbound_flow_response**pour l'attribut personnalisé. Cette fonctionnalité peut être utilisée pour enregistrer des informations dans les profils utilisateurs, les inclure dans les messages ou les transférer vers d'autres services, tels que les webhooks.

![Éditeur de messages WhatsApp avec un composant « Ajouter une personnalisation » permettant d'insérer une personnalisation des propriétés WhatsApp avec l'attribut personnaliséinbound_flow_response.]({%image_buster/assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Pour toute question ou assistance supplémentaire, veuillez contacter [le service d'assistance]({{site.baseurl}}/braze_support/).