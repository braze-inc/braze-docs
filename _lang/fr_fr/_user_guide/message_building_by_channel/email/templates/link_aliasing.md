---
nav_title: Aliasage de lien
article_title: Aliasage de lien
alias: /link_aliasing/
page_order: 3
description: "Cet article décrit le fonctionnement de l'aliasage de lien et donne des exemples de ce à quoi ressembleront vos liens."
channel:
  - email

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Aliasage de lien
 
> Utilisez l’aliasage de lien pour créer des noms reconnaissables et générés par l’utilisateur pour identifier les liens envoyés dans les e-mails de Braze. Ces liens sont disponibles pour le reciblage de segmentation, le déclenchement basé sur l'action et l'analyse des liens.

## À propos de l'aliasage de lien

Avec l'aliasage de lien, vous pouvez créer des noms générés par l'utilisateur pour identifier et suivre les liens envoyés dans les e-mails. Ainsi, vous pouvez utiliser efficacement ces aliasages de lien reconnaissables dans vos e-mails pour suivre l'engagement et analyser les performances de la campagne, sans avoir besoin de référencer le lien complet.

Avec l'aliasage de lien, vous pouvez :

- **Recibler les utilisateurs qui ont cliqué sur des liens spécifiques :** Identifiez et ciblez les utilisateurs qui ont cliqué sur un lien.
- **Créez des déclencheurs basés sur l'action :** Envoyez un e-mail lorsqu'un utilisateur clique sur un lien.
- **Analyser les indicateurs :** Comparez le nombre d'utilisateurs qui ont cliqué sur le lien A par rapport au lien B.

### Fonctionnement

Braze identifie de manière unique les liens contenus dans les e-mails en ajoutant un paramètre supplémentaire appelé `lid` (également connu sous le nom d'identifiant de lien) à chaque URL de lien. Cette valeur de `lid` permet à Braze de suivre, de contrôler et d'agréger les interactions des utilisateurs avec le lien, même si les autres paramètres de l'URL peuvent être différents. Cela permet de fournir des informations sur la façon dont les utilisateurs s'engagent avec le contenu de vos campagnes d'e-mail.

## Création d’un alias de lien

Pour créer un alias de lien, suivez ces étapes : 

1. Dans votre campagne ou dans le composant Canvas, allez dans le corps de votre e-mail.
2. Sélectionnez l'onglet **Gestion des liens**.
3. Braze génère automatiquement des alias de lien par défaut uniques pour chacun de vos liens.
4. Donnez un nom à l'alias. Les alias doivent être nommés de manière unique par variante de campagne ou composant Canvas d’e-mail. 

Vous pouvez également définir un alias qui sera utilisé pour référencer un lien spécifique lors de la gestion des rapports ou de la segmentation. 

![Page de gestion des liens avec quatre alias de liens.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
L'aliasing de lien est uniquement pris en charge dans les attributs `href` des balises HTML où il est possible d’ajouter sans risque un paramètre de requête. La meilleure pratique consiste à inclure un point d'interrogation ( ?) à la fin de votre lien afin que Braze puisse facilement ajouter la valeur `lid`. Sans l’ajout de la valeur `lid`, Braze ne reconnaît pas l’URL pour l’aliasage de lien.
{% endalert %}

## Gestion des alias de lien

Pour afficher tous vos aliasages de liens suivis, procédez comme suit :

1. Accédez à **Paramètres** > **Préférences de messagerie** sous **Paramètres de l'espace de travail**.
2. Sélectionnez l'onglet **Paramètres d'aliasage de lien**.

{% alert important %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), ces paramètres se trouvent sous **Gérer les paramètres**.
{% endalert %}

Vous pouvez y effectuer des tris, des recherches et désactiver le suivi des aliasages de liens.

![La page Alias de liens suivis qui montre deux alias de liens nommés "TechPartners" et "Help" qui sont associés à une campagne nommée "Email_Survey".]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Utilisez les endpoints [List link alias for campaign]({{site.baseurl}}/get_campaign_link_alias/) et [List link alias for Canvas]({{site.baseurl}}/get_canvas_link_alias/) pour extraire l'ensemble `alias` dans chaque variante du message d'une campagne ou d'un composant Canvas spécifique à l'e-mail.
{% endalert %}

Braze recommande d’évaluer les liens dans l’e-mail, d’ajouter des modèles de lien et de fournir une convention d'appellation qui fonctionne à des fins de segmentation et de reporting. Cela vous aide à garder une trace de tous les liens.

Lorsque l'aliasage de lien est activé, les messages, les blocs de contenu et les modèles de lien ne sont pas modifiés. Tous les messages existants utilisant des modèles de liens ou des blocs de contenu seront les mêmes. Cependant, lorsque vous mettez à jour un message, le balisage d'alias de lien s'appliquera à tous les liens, vous devrez donc réappliquer les modèles de lien pour que les liens soient visibles.

## Comment les liens sont mis à jour avec l'aliasage de lien

Les tableaux suivants présentent des exemples de liens dans le corps d'un e-mail, les résultats de l'aliasage de lien et des explications sur la manière dont le lien original est mis à jour avec l'aliasage de lien.

### Permalink

**Logique :** Braze insère un point d’interrogation (?) et ajoute le premier paramètre de requête dans l’URL.

| Lien dans le corps de l’e-mail    | Lien avec aliasage                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien avec plus de paramètres de requête

**Logique :** Braze détecte d’autres paramètres de requête et ajoute `lid=` à la fin de l’URL.

| Lien dans le corps de l’e-mail                                            | Lien avec aliasage                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien HTML

**Logique :** Braze reconnaît qu'un lien est une URL et qu'il contient déjà un point d'interrogation ( ?). Le paramètre de requête `lid` est donc ajouté après le point d'interrogation.

| Lien dans le corps de l’e-mail                                                | Lien avec aliasage                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien avec ancre

**Logique :** Braze attend de l’URL qu’elle utilise une structure standard où les ancres (#) sont présentes après un point d’interrogation (?). Comme Braze lit de gauche à droite, le point d'interrogation et la valeur `lid` sont ajoutés avant l'ancre.

| Lien dans le corps de l’e-mail                               | Lien avec aliasage                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien avec étiquette d'ancrage et de capture

**Logique :** Lorsque vous utilisez l'aliasage de lien avec des URL contenant des ancres (#), Braze s'attend à ce que l'ancre soit placée après les paramètres de la requête. Cela signifie que la valeur `lid` doit être ajoutée avant l'ancre pour un suivi correct, et comme Braze lit l'URL de gauche à droite, le point d'interrogation ( ?) et `lid` doivent être placés avant l'ancre.

| Lien dans le corps de l’e-mail                                                                        | Lien avec aliasage                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Aliasage de lien de suivi

Dans l'onglet **Gestion des liens**, sélectionnez les alias que vous souhaitez « suivre » à des fins de segmentation et qui doivent être présents dans les filtres de segmentation. Notez que les alias suivis le sont uniquement à des fins de segmentation et n’auront aucun impact sur votre lien suivi à des fins de reporting.

{% alert tip %}
Pour suivre les métriques d'engagement des liens, assurez-vous que votre lien commence par HTTP ou HTTPS. Pour désactiver le suivi des clics pour des liens spécifiques, reportez-vous aux rubriques [Liens universels et Liens d'application.]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis)
{% endalert %}

Braze vous permet de sélectionner un nombre illimité de liens à suivre, bien que vous ne puissiez recibler les utilisateurs que sur les liens les plus récents qu'ils ont ouverts. Les profils d'utilisateur incluent leurs 100 liens les plus récemment cliqués. Par exemple, si vous assurez le suivi de 500 liens et qu'un utilisateur clique sur ces 500 liens, vous pouvez recibler ou créer des segments en fonction des 100 liens les plus récemment cliqués.

{% tabs local %}
{% tab Éditeur par glisser-déposer %}

![Onglet Gestion des liens de l'éditeur d'e-mails par glisser-déposer.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab Éditeur HTML %}

![Onglet de gestion des liens de l'éditeur d'e-mails HTML.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze suit uniquement les 100 derniers alias de liaison cliqués au niveau du profil.
{% endalert %}

### Filtres basés sur des actions
 
Vous pouvez créer des messages basés sur des actions ciblant n'importe quel lien (suivi ou non) ou recibler les utilisateurs selon qu'ils ont cliqué ou non sur un alias dans n'importe quelle campagne e-mail ou composant Canvas.

![Options basées sur l'action pour cibler les utilisateurs qui ont cliqué sur un alias dans un composant Canvas ou qui ont interagi avec une campagne.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Filtres de segmentation

Dans Braze, si vous avez un alias de lien dans votre e-mail et qu'un utilisateur clique dessus, l'événement est enregistré dans le profil de l'utilisateur avec l'alias.

Si vous utilisez le filtre de segmentation "Alias cliqué dans n'importe quelle campagne ou étape du canvas" et que vous décidez par la suite de renommer cet alias de lien, les données relatives aux clics précédents dans le profil utilisateur **ne seront pas** mises à jour, ce qui signifie qu'il s'agira toujours de l'ancien alias de lien. Ainsi, si vous ciblez des utilisateurs sur la base du nouvel alias de lien, les données de l'alias de lien précédent ne seront pas prises en compte.

Si vous utilisez le filtre de segmentation "Alias cliqué dans la campagne" ou "Alias cliqué dans le canevas", vos utilisateurs seront filtrés selon qu'ils ont cliqué sur un alias spécifique dans une campagne ou un canevas spécifique. Si plusieurs utilisateurs partagent la même adresse e-mail et que l'on clique sur l'alias du lien, tous les autres utilisateurs qui partagent l'adresse e-mail verront leur profil utilisateur mis à jour. 

Les filtres de segmentation suivants s'appliquent aux événements de clics qui sont suivis au moment du traitement de l'événement. Cela signifie que les liens non suivis ne supprimeront pas les données existantes et que le suivi d'un lien ne remplira pas les données. Pour plus de détails, voir [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Abandon du suivi des liens

La suppression d'un lien n'entraînera pas la réaffectation des segments existants avec le filtre à l'alias supprimé. Les anciennes données resteront dans les profils utilisateurs jusqu'à ce qu'elles soient remplacées par des données plus récentes. 

Les liens dans les messages archivés ne seront automatiquement plus suivis. Cependant, si les messages archivés sont désarchivés, les liens devront être resuivis. Lorsque des alias de liaison sont suivis, les rapports de liens sont indexés par l’alias plutôt que par des domaines de niveau supérieur ou des URL complètes.

![L'onglet Analyse/analytique de la campagne affiche trois alias de lien et le nombre total de clics.]({% image_buster /assets/img/link_aliasing_click_table.png %})

### Événement de clic sur un e-mail

Si vous exportez vos données d'engagement avec Currents, un événement de clic d'e-mail sera légèrement différent si vous avez activé l'aliasage de lien. Il comportera deux champs supplémentaires pour l'[événement de clic d'e-mail]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) lorsque l'aliasage de lien est activé : `link_id` et `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». Découvrez le [ comportement du `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans les canvas et les campagnes.

_Mise à jour notée en août 2019._
{% endalert %}

## Aliasage de lien dans les blocs de contenu

Les nouveaux blocs de contenu verront leurs liens modifiés lorsque Braze ajoutera un `lid={{placeholder}}` à chaque lien, le cas échéant. Cette valeur de marque substitutive est résolue lorsqu’elle est insérée dans une variante d’e-mail.

Pour modifier les liens dans les blocs de contenu existants créés avant que Braze n'active l'aliasing des liens, dupliquez les blocs de contenu existants, puis modifiez les liens dans les blocs de contenu dupliqués.

Lorsqu’un bloc de contenu sans valeur `lid` est inséré dans un nouveau message, les liens de ce bloc de contenu ne sont pas suivis avec un alias. Lorsqu’un nouveau bloc de contenu est inséré dans une « ancienne » variante de message, les liens de cette variante sont reconnus par l’aliasage de lien. Les liens du bloc de contenu sont également reconnus. Cependant, les « anciens » blocs de contenu ne peuvent pas imbriquer de « nouveaux » blocs de contenu.

{% alert tip %}
Pour les blocs de contenu, Braze recommande de créer des copies des blocs de contenu existants à utiliser dans les nouveaux messages. Cela peut être fait en les dupliquant en masse pour éviter les scénarios où vous pourriez référencer un bloc de contenu qui n’a pas été activé pour l’aliasage de lien dans un nouveau message.
{% endalert %}

## Aliasage de lien pour les URL générées par Liquid

Pour les URL générées par Liquid, telles que les déclarations `assign` dans le HTML ou à partir d'un bloc de contenu, vous devez ajouter un point d'interrogation (`?`) à l'étiquette Liquid. Cela permet à Braze d'ajouter des paramètres de requête (`lid = somevalue`) afin que l'aliasage de lien puisse fonctionner correctement. Si vous ne savez pas où ajouter les paramètres de requête, l'aliasage de lien ne reconnaîtra pas ces URL et les modèles de lien ne s'appliqueront pas.

### Exemple

Consultez cet exemple d'aliasage de lien pour connaître le formatage recommandé du lien :

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

Si le lien contient des paramètres avec un point d'interrogation (`?`), vous pouvez le remplacer dans la balise d'ancrage par une esperluette (`&`), comme dans cet exemple :

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}


