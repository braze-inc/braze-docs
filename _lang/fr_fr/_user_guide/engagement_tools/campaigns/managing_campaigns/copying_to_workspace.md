---
nav_title: "Copie d'un espace de travail à l'autre"
article_title: "Copie d'un espace de travail à l'autre"
alias: "/copying_to_workspaces/"
page_order: 0.5
page_type: reference
description: "Cet article donne un aperçu de la manière de copier des campagnes dans différents espaces de travail."
tool: Campaigns
---

# Copie entre espaces de travail

> La copie de campagnes entre espaces de travail vous permet d'accélérer la composition de vos messages en commençant par une copie d'une campagne dans un espace de travail différent. Ce texte restera à l'état de projet jusqu'à ce que vous le modifiiez et le lanciez, ce qui vous permettra de conserver et de créer des stratégies d'envoi de messages qui ont fait leurs preuves.<br><br>Cette page explique comment copier des campagnes dans différents espaces de travail et indique ce qui est copié et ce qui ne l'est pas.

{% alert important %}
La copie de campagnes entre espaces de travail est généralement disponible pour les canaux pris en charge suivants : SMS, messages in-app, e-mails, modèles d'e-mails et blocs de contenu. La prise en charge d'autres canaux (tels que les cartes de contenu et les cartes push) n'est pas encore disponible.
{% endalert %}

## Comment copier une campagne dans un autre espace de travail ?

![Menu avec l'option "Copier dans l'espace de travail".][1]{: style="float:right;max-width:25%;margin-left:15px;"}

Sélectionnez l'icône d'engrenage <i class="fas fa-cog"></i> en regard de la campagne sélectionnée, puis sélectionnez **Copier dans l'espace de travail**. Après la copie, nous vous recommandons de revoir et de tester votre campagne pour confirmer que tous les champs fonctionnent correctement.

Lorsque vous copiez une campagne dans plusieurs espaces de travail, les champs tels que le nom et la description de la campagne, les variantes, le type de planification de la réception/distribution et les comportements de conversion sont copiés. Pour les campagnes d'e-mails, les champs tels que le corps de l'e-mail, l'objet et l'accroche sont également copiés dans l'espace de travail de destination. 

Notez que les campagnes multicanales dont les canaux ne sont pas pris en charge ne peuvent pas être copiées dans un autre espace de travail.

### Ce qui est copié dans les espaces de travail

Notez que ce qui suit ne constitue pas une liste exhaustive de ce qui est copié entre les espaces de travail et de ce qui est omis. En guise de bonne pratique, vérifiez les détails de la campagne et testez pour confirmer que votre campagne fonctionne comme prévu.

{% tabs %}
{% tab Campagnes %}

| Copié | Omis |
|---|---|
| Description | Territoires | 
| Type | Balises | 
| Actions (imbriquées) | Segments | 
| Comportements de conversion (imbriqués) | Approbations | 
| Configurations de l'heure de repos | Planification des déclencheurs | 
| Configurations de limite de fréquence | Résumés de campagne | 
| État de l'abonnement du destinataire |  | 
| Planification récurrente |  | 
| Est transactionnel |  | 

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Comportements de conversion %}

| Copié | Omis |
|---|---|
| Type de comportement | ID de l'espace de travail |
| Interaction avec la campagne |  ID de campagne | 
| Nom de l’événement personnalisé |  | 
| Nom du produit |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Actions %}

| Copié | Omis |
|---|---|
| Types d'actions | Nombre d’envois |
| Variantes de messages |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variantes de messages %}

| Copié | Omis |
|---|---|
| Envoyer le pourcentage | ID de l’API |
| Type |  ID des groupes initiateurs | 
|  |  ID des modèles de liens | 
|  |  ID des groupes internes d'utilisateurs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variante de message par e-mail %}

| Copié | Omis |
|---|---|
| [Corps de l’e-mail]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | Adresse De |
| Suppléments de message |  Répondre à | 
| Titre |  CCI | 
| Objet |  Modèles de liens | 
|  |  Aliasage de lien |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Corps de l'e-mail %}

| Copié | Omis |
|---|---|
| Texte en clair | Aliasage de lien |
| Contenu HTML et glisser-déposer |  | 
| Accroche |  | 
| Insertion CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modèles d'e-mail %}

| Copié | Omis |
|---|---|
| [Corps de l’e-mail]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | ID de l'API |
| Description | ID des images | 
| Objet | Territoires | 
| En-têtes | Balises | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Blocs de contenu %}

| Copié | Omis |
|---|---|
| Nom | Aliasage de lien |
| Description | Clés API | 
| Contenu | Territoires | 
| Contenu HTML et glisser-déposer | Balises | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variante de message par SMS %}

| Copié | Omis |
|---|---|
| Corps | Service d'envoi de messages |
| Raccourcissement de lien | Éléments de média VCF | 
| Suivi des clics |  | 
| Articles de presse |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Copier des campagnes contenant du code Liquid

Pour les corps de message qui incluent des références Liquid, les références sont copiées dans l'espace de travail de destination, mais il se peut qu'elles ne fonctionnent pas comme prévu. Cela signifie que si une campagne de l'espace de travail A est copiée dans l'espace de travail B, l'espace de travail B ne peut pas faire référence aux détails de l'espace de travail A, y compris aux références Liquid. Par exemple, les champs tels que les actions de déclenchement et les filtres d'audience ne sont pas copiés.

Notez les références liquides suivantes avec les dépendances lorsque vous copiez des campagnes entre espaces de travail :

- Étiquettes des articles du catalogue
- Tags du contenu connecté
- Blocs de contenu
- Attributs personnalisés
- Centres de préférence
- Recommandations produits
- Tags d'état de l'abonnement
- Étiquettes de bons d'achat et de promotions

Lorsque vous copiez une campagne entre espaces de travail, les blocs de contenu ne sont pas copiés. Toutefois, un bloc de contenu peut être référencé dans l'espace de travail de destination s'il existe un bloc portant le même nom. Vous pouvez également créer le bloc de contenu (ou ces références liquides) dans l'espace de travail de destination afin d'éviter les erreurs lors du lancement d'une campagne.

### Copier des campagnes avec des drapeaux de fonctionnalité

Pour copier une campagne d'indicateurs de fonctionnalité entre des espaces de travail, assurez-vous que l'espace de travail de destination dispose d'une [expérience d'indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurée avec un ID correspondant à l'indicateur de fonctionnalité référencé dans la campagne d'origine. Si vous copiez une campagne mais qu'un ID de fonctionnalité correspondant n'existe pas dans l'espace de travail de destination, la sélection de l'indicateur de fonctionnalité dans la campagne sera vide lors de la copie et vous devrez en sélectionner un autre.

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

