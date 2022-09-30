---
nav_title: Aliasage de lien
article_title: Aliasage de lien
alias: /link_aliasing/
page_order: 4
description: "Le présent article décrit la manière dont l’aliasage de lien fonctionnent et à quoi ressembleront vos liens."
channel:
  - E-mail

---

# Aliasage de lien
 
> Utilisez l’aliasage de lien pour créer des noms reconnaissables et générés par l’utilisateur pour identifier les liens envoyés dans les e-mails de Braze. L'aliasage de lien vous permet de recibler les utilisateurs ayant cliqué sur des liens spécifiques, ce qui vous permet de créer des déclencheurs basés sur les actions lorsque les utilisateurs cliquent sur un lien d’alias particulier. 

{% raw %}
L'aliasage de lien crée des noms générés par l’utilisateur qui sont disponibles pour le reciblage de segmentation, le déclenchement basé sur les actions et l’analyse des liens. L'aliasage de lien fonctionnent en décorant un paramètre de requête généré par Braze sur des liens dans le canal d’e-mail. Pour chaque lien connu présent dans le corps de l’e-mail, Braze ajoutera `lid={{placeholder}}` à la fin, où `{{placeholder}}` est une valeur alphanumérique unique générée par Liquid.
{% endraw %}

## Création d’un alias de lien

Pour créer un alias de lien, cliquez sur l’onglet **Link Management (Gestion des liens)** dans une campagne Braze ou un assistant Canvas pour décorer tous les liens connus du corps de l’e-mail. Vous pouvez également définir un alias qui sera utilisé pour référencer ce lien lors de la gestion de rapports ou de segmentation. 

Les alias doivent être nommés de manière unique par Campaign Variant d’e-mail ou Canvas Step. L'aliasage de lien est uniquement pris en charge dans les attributs `href` dans les balises HTML où il est sûr d’ajouter un paramètre de requête. Il est préférable d’inclure un point d’interrogation (?) à la fin de votre lien afin que Braze puisse facilement ajouter la valeur `lid`. Sans l’ajout de la valeur `lid`, Braze ne reconnaît pas l’URL pour l’aliasage de lien.

### Vérification des flux de travail

Braze recommande d’évaluer les liens dans l’e-mail, d’ajouter des modèles de lien et de fournir une convention d'appellation qui fonctionne à des fins de segmentation et de reporting. Cela vous aide à suivre tous les liens ! 

### Extraction des données

Les endpoints suivants sont disponibles pour extraire l’`alias` défini dans chaque variante de message d’une campagne ou d’un e-mail Canvas Step :

- [Endpoint d’alias de lien de campagne][3]
- [Endpoint d’alias de liaison Canvas][4]

## Modèles de lien

Pour les nouvelles variantes de message, les modèles de lien existants peuvent être utilisés depuis l’onglet **Link Management (Gestion des liens)**. Pour les messages envoyés avec un modèle de lien, elles seront toujours appliqués. Si un message existant est modifié, le modèle de lien doit être réappliqué dans l’onglet **Link Management (Gestion des liens)**. 

Notez que les modèles de lien ne peuvent être appliqués que pour les liens visibles dans l’onglet **Link Management (Gestion des liens)**. Cela signifie que les liens sans le paramètre d’URL `lid`, comme les « anciens » blocs de contenu ou les liens qui ne peuvent pas être marqués, ne sera pas éligible pour les modèles de lien. Pour résoudre cela, nous recommandons de copier les « anciens » blocs de contenu ou d’inclure un point d’interrogation (?) ou une esperluette (&) dans l’attribut `href` de l’URL.

## Aliasage de lien dans les blocs de contenu

Les nouveaux blocs de contenu verront leurs liens modifiés lorsque Braze ajoutera un `lid={{placeholder}}` à chaque lien, le cas échéant. Cette valeur de marque substitutive est résolue lorsqu’elle est insérée dans une variante d’e-mail.

Tous les blocs de contenu existants créés avant que Braze n’ait activé cette fonctionnalité ne seront modifiés que lorsque le HTML de ce bloc de contenu sera modifié et que le bloc de contenu sera relancé. Au lieu de relancer le bloc de contenu, nous recommandons de le dupliquer.

Lorsqu’un bloc de contenu sans valeur `lid` est inséré dans un nouveau message, les liens de ce bloc de contenu ne sont pas suivis avec un alias. Lorsqu’un nouveau bloc de contenu est inséré dans une « ancienne » variante de message, les liens de cette variante sont reconnus par l’aliasage de lien. Les liens du bloc de contenu sont également reconnus. Cependant, les « anciens » blocs de contenu ne peuvent pas imbriquer de « nouveaux » blocs de contenu.

{% alert tip %}
Pour les blocs de contenu, Braze recommande de créer des copies des blocs de contenu existants à utiliser dans les nouveaux messages. Cela peut être fait en les dupliquant en masse pour éviter les scénarios où vous pourriez référencer un bloc de contenu qui n’a pas été activé pour l’aliasage de lien dans un nouveau message.
{% endalert %}

## Exemples

Le tableau suivant fournit des exemples de liens dans un corps d’e-mail, des résultats d’aliasage de lien et des explications sur la façon dont le lien d’origine est mis à jour avec l’aliasage de lien.

{%raw%}
| Lien dans le corps de l’e-mail | Lien avec aliasage| Logique |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Braze insère un point d’interrogation (?) et ajoute le premier paramètre de requête dans l’URL. |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze détecte d’autres paramètres de requête et ajoute `lid=` à la fin de l’URL. |
| `<a href="{{custom_attribute.{product_url}}?">` | `<a href=”{{custom_attribute.{product_url}}?lid=ac7a548g5kl7”>` | Braze reconnaît qu’il s’agit d’une URL et qu’elle contient déjà un point d’interrogation (?). Ensuite, il ajoute paramètre de requête `lid` après le point d’interrogation. |
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email | Braze attend de l’URL qu’elle utilise une structure standard où les ancres (#) sont présentes après un point d’interrogation (?).  Comme Braze lit de gauche à droite, nous ajoutons le point d’interrogation et la valeur `lid` avant l’ancre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{%endraw%}

## Aliasage de lien pour les URL générées via Liquid

Pour les URL générées par une instruction `assign` dans le HTML ou dans un bloc de contenu, nous vous recommandons d’ajouter un point d’interrogation (?) dans la balise d’ancrage. Cela aidera Braze à ajouter les paramètres de requête (`lid = somevalue`) pour que l’aliasage de lien puisse fonctionner correctement. Sans identifier là où ajouter les paramètres de requête, l’aliasage de lien ne reconnaîtra pas ces URL.

### Exemple

Consultez l’exemple de l’aliasage de lien suivant pour le formatage recommandé de la balise d’ancrage :

{% raw %}

```liquid
{% assign link1 = https://www.braze1.com %}

<a href="{{link1}}?">{{link1}}?</a>
```


{% endraw %}

## Segmentation des liens

Le reciblage des filtres d’alias vous permet de créer des filtres de segmentation en fonction de vos clients, en cliquant sur un alias spécifiquement suivi d’une campagne par e-mail ou de Canvas Step. Ce filtre n’est disponible que pour les campagnes ou Canvas qui ont suivi des alias.

### Suivi des liens

Lors de la rédaction de votre e-mail, une nouvelle colonne apparaîtra dans l’onglet **Link Management (Gestion des liens)**. Ici, vous pouvez indiquer à Braze quel alias vous souhaitez « suivre » à des fins de segmentation. Vous pouvez suivre un nombre illimité de liens.

{% alert note %}
Braze suit uniquement les 100 derniers alias de liaison cliqués au niveau du profil. 
{% endalert %}

Seuls les alias que vous avez indiqués comme étant à suivre seront présents dans les filtres de segmentation. Notez que les alias suivis le sont uniquement à des fins de segmentation et n’auront aucun impact sur votre lien suivi à des fins de reporting.

### Abandon du suivi des liens

L’abandon du suivi des liens ne permet pas de désaffecter les segments existants avec le filtre de l’alias non suivi. Les anciennes données resteront sur les profils utilisateur jusqu’à ce qu’elles soient supprimées par des données plus récentes. Les filtres de segmentation suivants continuent d’exister, mais de nouveaux segments ne peuvent pas être créés avec ce filtre.

À des fins de segmentation, seuls 100 liens peuvent être suivis par groupe d’apps par défaut. Les liens dans les messages archivés ne seront automatiquement plus suivis. Cependant, si les messages archivés sont désarchivés, les liens devront être resuivis.

Lorsque des alias de liaison sont suivis, les rapports de liens sont indexés par l’alias plutôt que par des domaines de niveau supérieur ou des URL complètes.

![][1]

### Filtres de segment

#### Alias cliqué dans la campagne

Reciblez les utilisateurs sur la base d’un alias qui a été cliqué dans une campagne. Seules les campagnes qui disposent d’alias qui ont été suivis seront reflétées ici.

#### Alias cliqué dans Canvas Step

Reciblez les utilisateurs sur la base d’un alias qui a été cliqué dans Canvas Step. Une option de filtre délimité par le pipe affiche Canvas et Canvas Step, suivie de l’alias dans Canvas Step. Seules les Canvas Steps avec des alias suivis seront affichées ici.

#### Alias cliqué dans la campagne ou Canvas

Reciblez les utilisateurs sur la base d’un alias qui a été cliqué dans la campagne ou Canvas Step. Étant donné que les alias sont considérés comme « globaux », tous les alias globaux ciblent les clics de lien de toutes les campagnes et Canvas Steps.

![][5]

### Filtres basés sur des actions
 
En plus de créer des filtres de segment, vous pouvez également créer des messages basés sur les actions ciblant les liens (suivis ou non) dans toutes les campagnes par e-mail ou dans Canvas Step.

![][6]

### Événement de clic sur un e-mail

L’[événement de clic sur un e-mail][7] se produit lorsqu’un utilisateur clique sur un e-mail. Plusieurs événements peuvent être générés pour une même campagne si un utilisateur clique plusieurs fois sur un lien ou clique sur plusieurs liens dans l’e-mail. Il existe deux champs supplémentaires dans l’événement de clic sur un e-mail lorsque l’aliasage de lien est activé : `link_id` et `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur le[ comportement de `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans Canvas et les campagnes.

_Mis à jour en août 2019._
{% endalert %}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/ 
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/