---
nav_title: Copie entre espaces de travail
article_title: "Copier d'un espace de travail à l'autre"
page_order: 4.5
alias: "/copying_to_workspaces/"
page_type: reference
description: "Cet article de référence donne un aperçu de la manière de copier des campagnes et des toiles dans différents espaces de travail."
tool:
    - Campaigns
    - Canvas
---

# Copie des campagnes et des toiles dans les espaces de travail

> La copie de campagnes entre espaces de travail vous permet d'accélérer la composition de vos messages en commençant par une copie d'une campagne dans un espace de travail différent. Cette page explique comment copier des campagnes dans différents espaces de travail et indique ce qui est copié et ce qui ne l'est pas.

Lorsque vous copiez une campagne ou un Canvas dans un autre espace de travail, la copie reste à l'état de brouillon jusqu'à ce que vous la modifiiez et la lanciez, ce qui vous permet de conserver et de créer des stratégies d'envoi de messages qui ont fait leurs preuves.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
La copie de campagnes entre espaces de travail est généralement disponible. La prise en charge des canaux pour les cartes de contenu n'est pas encore disponible.
{% endalert %}

Vous pouvez copier des campagnes entre les espaces de travail pour ces canaux pris en charge : SMS, messages in-app, notifications push, e-mail et webhooks. Vous pouvez également copier des modèles d'e-mail, des drapeaux de fonctionnalité et des blocs de contenu. Notez que les campagnes multicanales dont les canaux ne sont pas pris en charge ne peuvent pas être copiées dans un autre espace de travail.

Pour copier une campagne dans un autre espace de travail :

1. Sélectionnez l'icône d'engrenage <i class="fas fa-cog"></i> à côté de la campagne sélectionnée.
2. Sélectionnez **Copier dans l'espace de travail**. 
3. Après la copie, examinez et testez votre campagne pour confirmer que tous les champs fonctionnent correctement.

{% endtab %}
{% tab canvas %}

{% alert important %}
La copie de toiles entre espaces de travail est généralement disponible. Les canaux suivants ne sont pas pris en charge actuellement : LINE, cartes de contenu et WhatsApp.
{% endalert %}

Vous pouvez copier des toiles entre les espaces de travail pour ces canaux pris en charge : e-mail, messages in-app, push, webhooks et SMS.

Pour copier un canvas dans un autre espace de travail :

1. Sélectionnez le menu <i class="fa-solid fa-ellipsis-vertical"></i> en regard du Canvas sélectionné.
2. Sélectionnez **Copier dans l'espace de travail**. 
3. Après la copie, vérifiez et testez votre Canvas pour confirmer que tous les champs fonctionnent correctement.

Lorsque vous copiez un canvas avec des étapes Audience Sync, les paramètres ne sont pas copiés dans l'espace de travail de destination, mais les étapes du parcours le sont.

{% endtab %}
{% endtabs %}

## Ce qui est copié dans les espaces de travail

Notez que la liste suivante n'est pas une liste exhaustive de ce qui est copié entre les espaces de travail et de ce qui est omis. En tant que meilleure pratique, vérifiez les détails de la campagne et de Canvas et testez pour confirmer que votre message fonctionne comme prévu.

### Détails

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Description | Territoires | 
| Type | Tags | 
| Actions (imbriquées) | Segmentations | 
| Comportements de conversion (imbriqués) | Agréments | 
| Configurations de l'heure de repos | Planification des déclencheurs | 
| Configurations de limite de fréquence | Résumés de campagne | 
| État de l'abonnement du destinataire |  | 
| Planification récurrente |  | 
| Est transactionnel |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Description | Territoires | 
| Type | Tags | 
| Actions (imbriquées) | Segmentations | 
| Comportements de conversion (imbriqués) | Agréments | 
| Configurations de l'heure de repos | Planification des déclencheurs | 
| Configurations de limite de fréquence | Résumés de Canvas | 
| État de l'abonnement du destinataire |  | 
| Planification récurrente |  | 
| Est transactionnel |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Comportements de conversion

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Type de comportement | ID de l'espace de travail |
| Interaction avec la campagne |  ID de la campagne | 
| Nom de l'événement personnalisé |  | 
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID de l'espace de travail |
| Interaction avec le canvas |  Canvas ID | 
| Nom de l'événement personnalisé |  | 
| Nom du produit |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Actions

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Type de comportement | ID de l'espace de travail |
| Interaction avec la campagne |  ID de la campagne | 
| Nom de l'événement personnalisé |  | 
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID de l'espace de travail |
| Interaction avec le canvas |  Canvas ID | 
| Nom de l'événement personnalisé |  | 
| Nom du produit |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variations des messages

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Envoyer le pourcentage | ID API |
| Type |  ID des groupes initiateurs | 
|  |  ID des modèles de liens | 
|  |  ID des groupes internes d'utilisateurs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Envoyer le pourcentage | ID API |
| Type |  ID des groupes initiateurs | 
|  |  ID des modèles de liens | 
|  |  ID des groupes internes d'utilisateurs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### Variation du message e-mail

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | De l'adresse |
| Envoi de messages supplémentaires |  Répondre à | 
| Titre |  CCI | 
| Sujet |  Modèle de lien | 
|  |  Aliasage de lien |
|  | Traductions |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | De l'adresse |
| Envoi de messages supplémentaires |  Répondre à | 
| Titre |  CCI | 
| Sujet |  Modèle de lien | 
|  |  Aliasage de lien |
|  | Traductions |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Corps de l'e-mail

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Texte en clair | Aliasage de lien |
| Contenu HTML et glisser-déposer | Traductions | 
| Accroche |  | 
| Insertion CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Texte en clair | Aliasage de lien |
| Contenu HTML et glisser-déposer | Traductions | 
| Accroche |  | 
| Insertion CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Modèles d'e-mail

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | ID de l'API |
| Description | ID des images | 
| Sujet | Territoires | 
| En-têtes | Tags | 
| | Traductions |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | ID de l'API |
| Description | ID des images | 
| Sujet | Territoires | 
| En-têtes | Tags | 
| | Traductions |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Blocs de contenu

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Nom | Aliasage de lien |
| Description | clés API | 
| Contenu | Territoires | 
| Contenu HTML et glisser-déposer | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Nom | Aliasage de lien |
| Description | clés API | 
| Contenu | Territoires | 
| Contenu HTML et glisser-déposer | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variation des messages SMS

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps | Service d'envoi de messages |
| Raccourcissement des liens | Éléments de média VCF | 
| Suivi des clics |  | 
| Articles de presse |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps | Service d'envoi de messages |
| Raccourcissement des liens | Éléments de média VCF | 
| Suivi des clics |  | 
| Articles de presse |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Copie des messages contenant du Liquid

Les références liquides contenues dans les corps de message sont copiées dans l'espace de travail de destination, mais il se peut que les références ne fonctionnent pas comme prévu. Cela signifie que si un canvas de l'espace de travail A est copié dans l'espace de travail B, l'espace de travail B ne peut pas faire référence aux détails de l'espace de travail A, y compris aux références liquides. Par exemple, les champs tels que les actions de déclenchement et les filtres d'audience ne sont pas copiés.

Gardez une trace des références liquides suivantes avec les dépendances lorsque vous copiez des campagnes et des toiles dans des espaces de travail différents :

- Étiquettes des articles du catalogue
- Tags du contenu connecté
- Blocs de contenu
- Attributs personnalisés
- Centres de préférence
- Recommandations produits
- Tags d'état de l'abonnement
- Étiquettes de bons d'achat et de promotions

## Copier des messages avec des drapeaux de fonctionnalité

Pour copier une campagne de drapeaux de fonctionnalités et un canvas avec une étape de drapeau de fonctionnalités entre des espaces de travail, assurez-vous que l'espace de travail de destination dispose d'une [expérience]({{site.baseurl}}/developer_guide/feature_flags/experiments) Canvas configurée avec un ID qui correspond soit au drapeau de fonctionnalités référencé dans la campagne d'origine, soit à l'étape du canvas référencée dans le canvas d'origine.

Si vous copiez une campagne ou un canevas comportant une étape de drapeau de fonctionnalité dont l'ID n'existe pas dans l'espace de travail de destination, l'étape de drapeau de fonctionnalité sera copiée mais son contenu ne le sera pas.

## Copier des messages avec des blocs de contenu

Lorsque vous copiez une campagne dans plusieurs espaces de travail, les blocs de contenu ne sont pas copiés. Toutefois, un bloc de contenu peut être référencé dans l'espace de travail de destination s'il existe un bloc portant le même nom. Vous pouvez également créer le bloc de contenu (ou ces références liquides) dans l'espace de travail de destination afin d'éviter les erreurs lors du lancement d'une campagne.

Pour les toiles qui font référence à un bloc de contenu, ce dernier doit d'abord être copié dans l'espace de travail de destination.
