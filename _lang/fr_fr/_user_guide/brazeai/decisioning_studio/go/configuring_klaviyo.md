---
nav_title: Configurer avec Klaviyo
article_title: Configurer avec Klaviyo pour BrazeAI Decisioning Studio
page_order: 3
description: "Découvrez comment configurer un flux Klaviyo pour l'utiliser avec BrazeAI Decisioning <sup>StudioTM</sup> Go."
toc_headers: h2
---

# Configurer avec Klaviyo pour BrazeAI Decisioning Studio™ Go

> Configurez un modèle substitutif et un flux dans Klaviyo pour déclencher des activations via BrazeAI Decisioning Studio™ Go.

{% alert important %}
Vous devez créer un nouveau flux dans Klaviyo pour chaque nouvel expérimentateur que vous mettez en place. Si vous avez précédemment créé un flux marque substitutive pour importer vos modèles, vous devez créer un nouveau flux et ne pouvez pas réutiliser le flux marque substitutive précédent.
{% endalert %}

Avant de créer un flux dans Klaviyo, vous devez disposer des détails suivants de votre portail BrazeAI Decisioning Studio™ Go à titre de référence :

- Nom du flux
- Nom de l'événement déclencheur

## Créer un modèle substitutif dans Klaviyo

BrazeAI Decisioning Studio™ Go importe des modèles qui sont associés à des flux existants dans votre compte Klaviyo. Pour utiliser un modèle qui n'est associé à aucun flux, vous pouvez créer un flux marque substitutive contenant les modèles que vous souhaitez utiliser. Le flux peut être laissé à l'état de projet ; il n'a pas besoin d'être en ligne/en production/instantané.

### Étape 1 : Configurez votre flux

{% alert note %}
L'objectif de ces flux substitutifs est d'importer le contenu de votre choix dans BrazeAI Decisioning Studio™ Go. Vous devez créer un flux distinct à une étape ultérieure, que BrazeAI Decisioning Studio™ Go utilise pour déclencher des activations une fois que votre expérimentateur est en ligne/en production/instantané.
{% endalert %}

1. Dans Klaviyo, sélectionnez **Flux.** 
2. Sélectionnez **Créer un flux** > **Créer à partir de zéro**.
3. Donnez au marqueur substitutif Flow un nom que vous reconnaîtrez, puis sélectionnez **Create Flow (Créer un flux)**.

![Un flux nommé "OFE Placeholder Flow".]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Sélectionnez n'importe quel déclencheur, puis enregistrez le flux.
5\. Sélectionnez **Confirmer et enregistrez**. 

### Étape 2 : Créer le modèle marque substitutive

Créez ensuite le modèle de marque substitutive : 

1. Glissez-déposez un nœud d'**e-mail** après le **déclencheur**.

![Un flux avec un nœud de déclencheur suivi d'un nœud d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. Dans le nœud **E-mail**, sélectionnez **Sélectionner un modèle**.
3\. Choisissez ensuite le modèle à utiliser et sélectionnez **Utiliser le modèle.**
4\. Sélectionnez **Enregistrer** > **Terminé**.
5\. (Facultatif) Pour ajouter d'autres modèles à utiliser dans BrazeAI Decisioning Studio™ Go, ajoutez un autre nœud d'**e-mail** et répétez les étapes 2 à 4.
6\. Laissez tous les e-mails en mode **brouillon** et quittez le flux.

Dans le portail BrazeAI Decisioning Studio™ Go, vos modèles devraient pouvoir être sélectionnés sous votre flux marque substitutive.

![Exemple de marque substitutive d'un modèle Klaviyo dans le portail Decisioning Studio Go.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

## Créer un flux dans Klaviyo

### Étape 1 : Mise en place du flux

1. Dans Klaviyo, sélectionnez **Flux** > **Créer un flux.**
2. Sélectionnez **Créez le vôtre**.
3. Pour **Nom**, saisissez le nom du flux à partir de votre portail BrazeAI Decisioning Studio™ Go. Sélectionnez ensuite **Créer manuellement**.

![L'option "Créer manuellement" est sélectionnée pour un exemple de flux.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Sélectionnez le déclencheur.
5\. Faites correspondre le nom de l'indicateur au nom de l'événement déclencheur de votre portail BrazeAI Decisioning Studio™ Go.

![Exemple de nom de métrique correspondant au nom de l'événement déclencheur "OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6\. Sélectionnez **Enregistrer**.

{% alert note %}
Si votre expérimentateur dispose d'un seul modèle de base, passez aux étapes suivantes. Si votre expérimentateur dispose de deux modèles de base ou plus, passez à l'étape 3 du site [: Ajoutez un déclencheur à votre flux](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

### Étape 2 : Ajouter un e-mail à votre flux 

1. Glissez-déposez un nœud d'**e-mail** après le nœud de **déclenchement**.
2. Dans les **détails de** l'**e-mail**, sélectionnez **Sélectionner un modèle**.

![Option "Sélectionner un modèle" dans la section "Détails de l'e-mail".]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Recherchez et sélectionnez votre modèle de base. Vous pouvez rechercher votre modèle par son nom dans la section **Ressources à utiliser du** portail BrazeAI Decisioning Studio™ Go.

![Un exemple de modèle de base dans Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Sélectionnez **Utiliser le modèle** > **Enregistrer.**
5\. Pour la **ligne d'objet**, saisissez {% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. Pour le **nom de l'expéditeur** et l' **adresse e-mail de l'expéditeur**, entrez les détails que vous souhaitez utiliser.

![Exemple de ligne d'objet, de nom de l'expéditeur et d'adresse e-mail de l'expéditeur pour l'"e-mail 1".]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Sélectionnez **Terminé**.
8\. Décochez la case **Ignorer les profils récemment envoyés par e-mail**, puis sélectionnez **Enregistrer.**
9\. Dans le nœud de l'e-mail, mettez à jour le mode de **brouillon** en **ligne/en production/instantanée**.

![L'éditeur de flux de Klaviyo montre un nœud de déclencheur connecté à un nœud d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

Vous êtes prêt ! Vous pouvez désormais déclencher des activations par l'intermédiaire de BrazeAI Decisioning Studio™ Go. 

### Étape 3 : Ajoutez un déclencheur à votre flux 

1. Glissez-déposez un nœud de **déclenchement** après le **nœud de déclenchement**.
2. Sélectionnez le nœud de **fractionnement Déclencheur** et définissez la **Dimension** sur **EmailTemplateID**.

![Diagramme de flux Klaviyo montrant un nœud Trigger alimentant un Trigger split configuré avec Dimension EmailTemplateID.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

#### Étape 3.1 : Ajoutez votre modèle d'e-mail

1. Dans le portail BrazeAI Decisioning Studio™ Go, trouvez l'**ID du modèle d'e-mail** pour votre premier modèle dans la section **Ressources à utiliser**. Saisissez l'**ID du modèle d'e-mail** pour le champ **Dimension**, puis sélectionnez **Enregistrer.**
2. Glissez-déposez un nœud **E-mail** dans la branche **Oui** du **déclencheur**. 

![Un flux Klaviyo avec un nœud de fractionnement Trigger, qui a une branche Yes menant à un nœud Email et une branche No se connectant à un autre fractionnement Trigger.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. Dans les **détails de** l'**e-mail**, sélectionnez **Sélectionner un modèle**.
4\. Recherchez et sélectionnez votre modèle de base. Vous pouvez rechercher votre modèle par le nom du modèle de base dans la section **Ressources à utiliser** du portail BrazeAI Decisioning Studio™ Go.
5\. Sélectionnez **Utiliser le modèle** > **Enregistrer.**
6\. Pour la **ligne d'objet**, saisissez {% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. Pour le **nom de l'expéditeur** et l' **adresse e-mail de l'expéditeur**, entrez les détails que vous souhaitez utiliser.

![Un modèle d'e-mail sélectionné et des champs pour la ligne d'objet, le nom de l'expéditeur et l'adresse e-mail de l'expéditeur.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Sélectionnez **Terminé**.
9\. Décochez la case **Ignorer les profils récemment envoyés par e-mail**, puis sélectionnez **Enregistrer.**
10\. Dans le nœud de l'e-mail, mettez à jour le mode de **brouillon** en **ligne/en production/instantanée**.

#### Étape 3.2 : Ajouter un nouveau déclencheur

Ensuite, créez un nouveau nœud de **déclencheur** et un nœud d'**e-mail** pour chaque modèle de base supplémentaire que votre expérimentateur utilisera. 

1. Glissez-déposez un autre nœud de **déclencheur** dans la branche **No** du nœud de **déclencheur** précédent.
2. Réglez la **dimension** sur **EmailTemplateID** et complétez la valeur de la **dimension** avec l' **ID** du modèle de base que vous êtes en train de configurer.
3. Sélectionnez **Enregistrer**.

![Diagramme d'un éditeur de flux Klaviyo montrant un nœud Trigger menant à un Trigger split. Le déclencheur a une branche "Oui" qui mène à un nœud d'e-mail et une branche "Non" qui se connecte à un autre déclencheur qui mène à d'autres nœuds d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Glissez-déposez un nœud **E-mail** dans la branche **Oui** de votre nouveau déclencheur.
5\. Répétez les étapes 1 à 5 de l'[étape 3.1](#step-31-add-your-email-template) pour sélectionner le modèle correspondant.
5\. Réglez la **ligne d'objet** sur {% raw %}`{{event.SubjectLine}}`{% endraw %}, et décochez la case **Ignorer les profils récemment envoyés par e-mail.** 
6\. Répétez ce processus jusqu'à ce que vous disposiez d'un nœud de **déclenchement** et d'un nœud d'**e-mail** pour chaque modèle de base utilisé par votre expérimentateur. Votre dernier déclencheur ne doit rien contenir dans la branche "Non".

![Un flux Klaviyo avec plusieurs nœuds de déclenchement qui se ramènent à plusieurs nœuds d'e-mail.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="7"}
7\. Dans chacun de vos nœuds d'**e-mail**, mettez à jour le mode en passant de **Brouillon** à **Production/instantané**.

![L'option permettant de mettre à jour le statut du nœud en ligne/en production/instantané.]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

Vous êtes prêt ! Vous pouvez désormais déclencher des activations par l'intermédiaire de BrazeAI Decisioning Studio™ Go. 