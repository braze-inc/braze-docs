---
nav_title: Denada
article_title: Denada
alias: /partners/denada/
description: "Cet article de référence présente le partenariat entre Braze et Denada, une plateforme créative marketing alimentée par l'intelligence artificielle qui vous permet de créer des modèles d'e-mail conformes à votre identité de marque par le biais d'une conversation naturelle et de les exporter directement vers Braze."
page_type: partner
search_tag: Partner
---

# Denada

> [Denada](https://heydenada.com) est une plateforme créative marketing alimentée par l'intelligence artificielle qui permet aux experts métier de créer des supports marketing conformes à l'identité de marque par le biais d'une conversation naturelle. Avec Denada, les équipes peuvent passer de l'idéation au contenu d'e-mail finalisé sans avoir besoin de compétences en design.

_Cette intégration est maintenue par Denada._

## À propos de l'intégration

L'intégration entre Braze et Denada vous permet d'exporter des modèles d'e-mail créés dans Denada directement vers Braze, avec téléchargement automatique des images dans la bibliothèque multimédia de Braze. Cela simplifie le passage de l'idéation créative à l'exécution de campagne.

## Conditions préalables

Les éléments suivants sont requis pour utiliser cette intégration :

| Condition | Description |
| ----------- | ----------- |
| Compte Denada | Un [compte Denada](https://app.heydenada.com) est requis pour utiliser cette intégration. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations complètes pour les **modèles**. <br><br>Vous pouvez la créer dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Denada est conçu pour les marketeurs et les experts métier qui souhaitent créer du contenu d'e-mail conforme à leur identité de marque sans compétences en design ou en programmation. Il est idéal pour ceux qui :
- Veulent utiliser l'intelligence artificielle conversationnelle pour générer rapidement des modèles d'e-mail et les envoyer directement vers Braze
- Ont besoin d'itérer sur des modèles d'e-mail Braze existants en les réexportant depuis Denada avec détection de conflits et prise en charge de l'écrasement
- Souhaitent bénéficier du téléchargement et de la gestion automatiques des images dans la bibliothèque multimédia de Braze lors de l'export

## Intégration

### Étape 1 : Configurer votre intégration

Dans Denada, sélectionnez le nom de votre société dans le coin inférieur gauche, puis sélectionnez **Team settings** > **Add integration**.

Sélectionnez **Braze** comme intégration, puis saisissez votre **clé API** Braze et sélectionnez votre **endpoint API REST** dans la liste des régions disponibles.

{% alert note %}
Il s'agit d'une configuration unique. Une fois vos identifiants validés, votre configuration est enregistrée pour tous les exports futurs.
{% endalert %}

### Étape 2 : Exporter un modèle vers Braze

Dans Denada, ouvrez un modèle d'e-mail dans l'éditeur et sélectionnez **Export** > **Braze**.

Saisissez un nom de modèle et une ligne d'objet pour l'e-mail. Choisissez votre préférence de gestion des images :
- **Upload new :** Télécharge toutes les images dans la bibliothèque multimédia de Braze.
- **Use existing :** Réutilise les images précédemment téléchargées lorsqu'elles sont disponibles.

Si un modèle portant le même nom existe déjà dans Braze, Denada détecte le conflit et vous invite à confirmer si vous souhaitez écraser le modèle existant ou en créer un nouveau.

Sélectionnez **Export**. Denada convertit le modèle en HTML, télécharge les images vers Braze et crée ou met à jour le modèle d'e-mail dans votre compte Braze.

## Utiliser l'intégration

Vous trouverez vos e-mails Denada dans Braze sous **modèles et médias** > **Modèles d'e-mail**. Ils sont prêts à être utilisés dans n'importe quelle campagne ou Canvas Braze.

Denada conserve un historique des exports précédents, de sorte que les exports ultérieurs d'un même modèle peuvent mettre à jour le modèle Braze existant plutôt que de créer des doublons.