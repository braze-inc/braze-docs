---
nav_title: Optimiseur de contenu
article_title: "Étape de l'agent d'optimisation de contenu"
alias: "/content_optimizer_step/"
page_order: 5
description: "L'étape Agent d'optimisation de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu en une seule étape. Elle vous aide à expérimenter différentes variantes de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps."
page_type: reference

---

# Étape de l'agent d'optimisation de contenu

> L'étape Agent d'optimisation de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu en une seule étape. Elle vous aide à expérimenter différentes variantes de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps. Pour une introduction, consultez [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer est actuellement en version bêta. Pour obtenir de l'aide pour démarrer, contactez votre Customer Success Manager.
{% endalert %}

## Création d'une étape Content Optimizer

Pour obtenir les meilleurs résultats, utilisez l'agent Content Optimizer dans les Canvas où les utilisateurs entrent dans l'étape progressivement au fil du temps. Si tous les utilisateurs entrent dans l'étape en même temps, l'agent n'aura pas le temps de tirer des enseignements des premiers résultats.

### Étape 1 : Ajouter une étape

Glissez-déposez le composant **Content Optimizer** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape, puis sélectionnez **Content Optimizer**.

### Étape 2 : Créer votre message de base

Le message de base constitue le point de départ de votre étape. Les variantes de chaque composant de contenu sont insérées dynamiquement en fonction des combinaisons définies dans l'onglet **Content Optimizer Settings**.

{% alert note %}
Pendant la période bêta, l'e-mail est le seul canal pris en charge.
{% endalert %}

Dans l'onglet **Canaux de communication**, sélectionnez **E-mail** et créez votre e-mail de base. Consultez notre section dédiée aux [e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email) pour obtenir de l'aide.

L'agent Content Optimizer utilise les paramètres d'envoi (tels que le domaine d'e-mail et l'adresse de réponse) spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit partir d'un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux composants du message que vous souhaitez optimiser. Vous les définirez à [l'étape 4](#step-4).

Les composants pris en charge pour l'optimisation comprennent :

- Objet
- En-tête du corps du message
- Contenu du corps du message
- CTA principal

### Étape 3 : Spécifier les paramètres de réception/distribution

Dans l'onglet **Paramètres de réception/distribution**, vous pouvez indiquer si l'étape doit utiliser le timing intelligent ou les validations de réception/distribution. Pour plus de détails, consultez [Modifier les paramètres de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) dans l'étape Message.

### Étape 4 : Ajouter des composants de contenu et des variantes {#step-4}

Les composants de contenu sont les éléments individuels de votre message que vous souhaitez tester, tels que différentes lignes d'objet, titres, corps de texte ou appels à l'action principaux. Ces composants vous permettent de générer plusieurs versions d'un message et de les optimiser automatiquement en fonction des performances au fil du temps.

Vous pouvez ajouter jusqu'à trois composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 125 combinaisons de contenu uniques.

![Options permettant d'ajouter et de configurer des composants de contenu dans l'interface Content Optimizer. L'interface affiche les composants sélectionnables tels que l'objet, l'en-tête du corps, le contenu du corps et le CTA principal, chacun avec des champs permettant de saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Étape 4.1 : Configurer les composants de contenu

Pour configurer les composants :

1. Rendez-vous dans l'onglet **Content Optimizer Settings**.
2. Choisissez les composants que vous souhaitez optimiser. Options prises en charge :
  - Objet
  - En-tête du corps du message
  - Contenu du corps du message
  - CTA principal
3. Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela permet à Content Optimizer d'identifier plus efficacement les éléments les plus performants. Vous pouvez :
  - Rédiger vos propres variantes manuellement.
  - Utiliser les suggestions générées par l'intelligence artificielle pour explorer rapidement de nouvelles options.

![Interface Content Optimizer Settings présentant les options permettant d'ajouter et de configurer des composants de contenu pour l'optimisation des e-mails. Chaque composant dispose de champs de saisie permettant d'entrer différentes variantes. Le texte visible comprend les noms des composants et les champs permettant de saisir du texte variant.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Étape 4.2 : Ajouter du Liquid à votre message

Après avoir défini au moins deux variantes pour chaque composant, copiez l'étiquette Liquid associée à chacun d'eux et collez-la à l'emplacement correspondant dans votre message de base.

- Par exemple, si vous optimisez la ligne d'objet, collez l'étiquette {% raw %}`{% message_component "Subject" %}`{% endraw %} dans le champ Objet de l'éditeur d'e-mails.
- Vous pouvez également inclure des étiquettes de composant dans un texte plus long afin de tester uniquement une partie du composant. Par exemple : {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Options permettant d'ajouter et de configurer des composants de contenu tels que l'objet, l'en-tête du corps, le contenu du corps et le CTA principal. Chaque composant comporte des champs permettant de saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si vous n'ajoutez pas d'étiquette Liquid pour un composant de contenu sélectionné, un avertissement s'affichera dans l'onglet **Content Optimizer Settings** et une erreur apparaîtra dans l'onglet **Canaux de communication**. Le Canvas ne peut pas être lancé tant que tous les composants sélectionnés n'ont pas été correctement ajoutés à votre message de base.

Au fur et à mesure que le Canvas s'exécute, l'agent combine et associe les variantes entre les composants pour générer différentes combinaisons de contenu. Au fil du temps, les combinaisons les plus performantes sont privilégiées pour la distribution, ce qui vous aide à améliorer les performances sans intervention manuelle.

#### Référence Liquid

| Composant | Extrait de code Liquid |
| --- | --- | 
| Objet | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| En-tête du corps du message | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Contenu du corps du message | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 5 : Sélectionner l'événement d'optimisation

L'événement d'optimisation détermine la manière dont l'agent Content Optimizer évalue les performances et répartit le trafic vers les combinaisons de contenu au fil du temps.

Pour les e-mails, vous pouvez optimiser pour l'un des événements suivants. L'agent utilise les ouvertures et les clics enregistrés dans les 7 jours suivant l'envoi d'un message pour orienter la distribution vers les combinaisons de contenu les plus performantes.

| Événement | Description | Cas d'utilisation |
| --- | --- | --- |
| Ouvertures | Optimise les combinaisons qui incitent les destinataires à ouvrir l'e-mail. | Tester les lignes d'objet ou chercher à accroître la visibilité |
| Clics | Optimise les combinaisons qui favorisent l'engagement avec les liens. N'inclut pas les clics effectués par des robots ni les clics de désabonnement reconnus par Braze. | Générer du trafic, de l'engagement ou des conversions à partir de liens |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

L'événement d'optimisation sélectionné s'applique à tous les composants de contenu de cette étape.

## Bonnes pratiques

- De manière générale, nous recommandons de tester plus d'un composant pour l'étape Content Optimizer.
- Si vous optimisez pour les clics, incluez les lignes d'objet dans vos tests, car des lignes d'objet plus percutantes peuvent contribuer à augmenter les ouvertures et créer davantage d'opportunités de clics.
- Si vous optimisez pour les ouvertures, concentrez vos tests sur la ligne d'objet.

## Analyse

Pour examiner les performances, ouvrez le panneau d'analyse au niveau de l'étape afin de consulter les indicateurs par variante de contenu et les performances globales des combinaisons. L'étape Content Optimizer utilise les [mêmes analyses que l'étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics).

![Analyse de Content Optimizer pour trois boutons et le pourcentage d'attribution des envois, qui affiche une tendance à la hausse.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

## Résolution des problèmes

| Problème | Description | Correctif |
| --- | --- | --- |
| Étiquettes Liquid manquantes | Si vous ajoutez un composant de contenu (tel que l'objet ou le CTA) mais que vous n'insérez pas l'étiquette Liquid correspondante dans votre message de base, vous verrez : <br>- Un avertissement dans l'onglet **Content Optimizer Settings** <br>- Une erreur dans l'onglet **Canaux de communication** | Copiez l'extrait de code Liquid affiché sous chaque composant dans l'onglet **Content Optimizer Settings** et collez-le à l'endroit approprié dans votre message. |
| Étiquettes Liquid orphelines | Si vous supprimez un composant de contenu mais laissez son étiquette Liquid dans le message de base, le message risque de ne pas s'afficher comme prévu lors de l'envoi. | Supprimez toutes les étiquettes `message_component` inutilisées de votre message de base avant le lancement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }