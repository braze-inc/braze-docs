---
nav_title: Copier entre les espaces de travail
article_title: Copier entre les espaces de travail
page_order: 4
alias: "/copying_to_workspaces/"
page_type: reference
description: "Cet article de référence donne un aperçu de la manière de copier des campagnes et des Canvas dans différents espaces de travail."
tool:
    - Campaigns
    - Canvas
---

# Copier des campagnes et des Canvas entre les espaces de travail

> La copie de campagnes entre espaces de travail vous permet d'accélérer la composition de vos messages en partant d'une copie d'une campagne existante dans un autre espace de travail. Cette page explique comment copier des campagnes dans différents espaces de travail et indique ce qui est copié et ce qui ne l'est pas.

Lorsque vous copiez une campagne ou un Canvas dans un autre espace de travail, la copie reste à l'état de brouillon jusqu'à ce que vous la modifiiez et la lanciez, ce qui vous permet de conserver et de développer vos stratégies d'envoi de messages qui ont fait leurs preuves.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
La copie de campagnes entre espaces de travail est disponible de manière générale. La prise en charge du canal Cartes de contenu n'est pas encore disponible.
{% endalert %}

Vous pouvez copier des campagnes entre les espaces de travail pour les canaux pris en charge suivants : SMS, messages in-app, notifications push, e-mail et webhooks. Vous pouvez également copier des modèles d'e-mail, des indicateurs de fonctionnalité et des blocs de contenu. Notez que les campagnes multicanal dont les canaux ne sont pas pris en charge ne peuvent pas être copiées dans un autre espace de travail.

Pour copier une campagne dans un autre espace de travail :

1. Sélectionnez l'icône d'engrenage <i class="fas fa-cog"></i> à côté de la campagne sélectionnée.
2. Sélectionnez **Copier dans l'espace de travail**. 
3. Après la copie, vérifiez et testez votre campagne pour confirmer que tous les champs fonctionnent correctement.

{% endtab %}
{% tab canvas %}

{% alert important %}
La copie de Canvas entre espaces de travail est disponible de manière générale. Les canaux suivants ne sont pas pris en charge actuellement : LINE, Cartes de contenu et WhatsApp.
{% endalert %}

Vous pouvez copier des Canvas entre les espaces de travail pour les canaux pris en charge suivants : e-mail, messages in-app, push, webhooks et SMS.

Pour copier un Canvas dans un autre espace de travail :

1. Sélectionnez le menu <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;à côté du Canvas sélectionné.
2. Sélectionnez **Copier dans l'espace de travail**. 
3. Après la copie, vérifiez et testez votre Canvas pour confirmer que tous les champs fonctionnent correctement.

Lorsque vous copiez un Canvas avec des étapes Audience Sync, les paramètres ne sont pas copiés dans l'espace de travail de destination, mais les étapes du parcours le sont.

{% endtab %}
{% endtabs %}

## Ce qui est copié entre les espaces de travail

La liste suivante n'est pas exhaustive concernant ce qui est copié entre les espaces de travail et ce qui est omis. Nous vous recommandons de vérifier les détails de la campagne et du Canvas, puis de tester pour confirmer que votre message fonctionne comme prévu.

### Détails

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Description | Territoires | 
| Type | Étiquettes | 
| Actions (imbriquées) | Segments | 
| Comportements de conversion (imbriqués) | Approbations | 
| Configurations de l'heure calme | Planification des déclencheurs | 
| Configurations de limite de fréquence | Résumés de campagne | 
| État de l'abonnement du destinataire | Filtres | 
| Planification récurrente |  | 
| Est transactionnel |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Description | Territoires | 
| Type | Étiquettes | 
| Actions (imbriquées) | Segments | 
| Comportements de conversion (imbriqués) | Approbations | 
| Configurations de l'heure calme | Planification des déclencheurs | 
| Configurations de limite de fréquence | Résumés du Canvas | 
| État de l'abonnement du destinataire | Filtres | 
| Planification récurrente | Critères de sortie | 
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
| Interaction avec la campagne |  ID de campagne | 
| Nom de l'événement personnalisé |  | 
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID de l'espace de travail |
| Interaction avec le Canvas |  ID du Canvas | 
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
| Interaction avec la campagne |  ID de campagne | 
| Nom de l'événement personnalisé |  | 
| Nom du produit |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Type de comportement | ID de l'espace de travail |
| Interaction avec le Canvas |  ID du Canvas | 
| Nom de l'événement personnalisé |  | 
| Nom du produit |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variantes de messages

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Pourcentage d'envoi | ID de l'API |
| Type |  ID des groupes initiateurs | 
|  |  ID des modèles de liens | 
|  |  ID des groupes internes d'utilisateurs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Pourcentage d'envoi | ID de l'API |
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
| Corps de l'e-mail | Adresse d'expédition |
| Suppléments de message |  Répondre à | 
| Titre |  CCI | 
| Objet |  Modèle de lien | 
|  |  Aliasage de lien |
|  | Traductions |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | Adresse d'expédition |
| Suppléments de message |  Répondre à | 
| Titre |  CCI | 
| Objet |  Modèle de lien | 
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
| Texte brut | Aliasage de lien |
| Contenu HTML et glisser-déposer | Traductions | 
| Accroche |  | 
| CSS intégré |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Texte brut | Aliasage de lien |
| Contenu HTML et glisser-déposer | Traductions | 
| Accroche |  | 
| CSS intégré |  | 
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
| Objet | Territoires | 
| En-têtes | Étiquettes | 
| | Traductions |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps de l'e-mail | ID de l'API |
| Description | ID des images | 
| Objet | Territoires | 
| En-têtes | Étiquettes | 
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
| Description | Clés API | 
| Contenu | Territoires | 
| Contenu HTML et glisser-déposer | Étiquettes | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Nom | Aliasage de lien |
| Description | Clés API | 
| Contenu | Territoires | 
| Contenu HTML et glisser-déposer | Étiquettes | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variation du message SMS

{% tabs local %}
{% tab campaigns %}

| Copié | Omis |
|---|---|
| Corps | Service d'envoi de messages |
| Raccourcissement de lien | Éléments de média VCF | 
| Suivi des clics |  | 
| Éléments de média |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copié | Omis |
|---|---|
| Corps | Service d'envoi de messages |
| Raccourcissement de lien | Éléments de média VCF | 
| Suivi des clics |  | 
| Éléments de média |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Copie des messages contenant du Liquid

Les références Liquid contenues dans les corps de message sont copiées dans l'espace de travail de destination, mais il se peut qu'elles ne fonctionnent pas comme prévu. Autrement dit, si un Canvas de l'espace de travail A est copié dans l'espace de travail B, ce dernier ne peut pas faire référence aux détails de l'espace de travail A, y compris aux références Liquid. Par exemple, les champs tels que les actions de déclenchement et les filtres d'audience ne sont pas copiés.

Gardez une trace des références Liquid suivantes avec leurs dépendances lorsque vous copiez des campagnes et des Canvas entre différents espaces de travail :

- Étiquettes des articles du catalogue
- Balises de contenu connecté
- Blocs de contenu
- Attributs personnalisés
- Centres de préférence
- Recommandations produits
- Balises d'état de l'abonnement
- Étiquettes de bons d'achat et de promotions

## Copier des messages avec des indicateurs de fonctionnalité

Pour copier une campagne d'indicateur de fonctionnalité et un Canvas avec une étape d'indicateur de fonctionnalité entre des espaces de travail, assurez-vous que l'espace de travail de destination dispose d'une [expérience d'indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurée avec un ID correspondant soit à l'indicateur de fonctionnalité référencé dans la campagne d'origine, soit à l'étape d'indicateur de fonctionnalité référencée dans le Canvas d'origine.

Si vous copiez une campagne ou un Canvas comportant une étape d'indicateur de fonctionnalité dont l'ID n'existe pas dans l'espace de travail de destination, l'étape sera copiée mais son contenu ne le sera pas.

## Copier des messages avec des blocs de contenu

Lorsque vous copiez une campagne entre espaces de travail, les blocs de contenu ne sont pas copiés. Toutefois, un bloc de contenu peut être référencé dans l'espace de travail de destination s'il existe un bloc portant le même nom. Vous pouvez également créer le bloc de contenu (ou ces références Liquid) dans l'espace de travail de destination afin d'éviter les erreurs lors du lancement d'une campagne.

Pour les Canvas qui font référence à un bloc de contenu, ce dernier doit d'abord être copié dans l'espace de travail de destination.