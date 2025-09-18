---
nav_title: Constructeur
article_title: Constructeur
description: "Cet article de référence présente le partenariat entre Braze et Constructor. Ce partenariat vous permet de tirer parti de la découverte de produits hors site de Constructor pour générer et fournir de manière dynamique des recommandations de produits personnalisées dans les messages Braze."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructeur

> [Constructor](https://constructor.com/) est une plateforme de recherche et de découverte de produits qui utilise l'intelligence artificielle et le machine learning pour offrir des recherches, des recommandations et des expériences de navigation personnalisées pour les sites web de eCommerce et de retailing.

Grâce à l'intégration entre Braze et Constructor, vous pouvez utiliser la découverte de produits hors site de Constructor pour générer et fournir de manière dynamique des recommandations de produits personnalisées dans les messages Braze.

## Cas d’utilisation

- **Suivi des paniers abandonnés et des commandes passées**: Générez des recommandations de produits dynamiques basées sur le comportement de l'utilisateur et le contenu du panier pour envoyer des rappels de panier abandonné personnalisés ou des suggestions après la commande.
- **Recommandations de produits similaires pour les articles du panier abandonné**: Suggérez des produits similaires aux articles laissés dans le panier d'un utilisateur afin de maintenir son intérêt et de lui proposer des alternatives.
- **Rappels des articles récemment consultés**: Notifiez aux utilisateurs les articles qu'ils ont récemment consultés mais qu'ils n'ont pas encore achetés, afin de les encourager à finaliser leur achat.
- **Campagnes de promotion**: Envoyez des messages promotionnels personnalisés avec des recommandations de produits adaptées aux préférences des utilisateurs pour les ventes saisonnières ou les offres spéciales.
- **Propositions de produits visuellement similaires**: Recommandez des articles visuellement similaires à ceux que l'utilisateur a récemment consultés, afin de l'aider à découvrir les options connexes qu'il pourrait préférer.

## Conditions préalables

| Condition | Description |
|-------------|-------------|
| Compte du constructeur | Un compte Constructor avec son service de découverte hors site activé est nécessaire pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Travaillez avec votre équipe d'onboarding Constructor pour compléter le processus d'intégration. Assurez-vous que les données comportementales de votre site web ou d'autres sources de données pertinentes sont disponibles pour permettre des recommandations de produits personnalisées. Votre équipe d'onboarding Constructor vous aidera également à configurer les extraits de code HTML nécessaires à l'utilisation dans les messages de Braze.

## URL de l'API de découverte hors site du constructeur

Vous pouvez utiliser l'URL de l'API de découverte hors site de Constructor pour rendre les images des produits et diriger les utilisateurs vers la page détaillée du produit approprié. Vous trouverez ci-dessous une description de la structure de l'endpoint et un exemple d'utilisation :

### Exemple

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img 
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200" 
    border="0" 
    alt="Shop Now" 
  />
</a>
```

### Paramètres

| Paramètres | Description |
|-------------|-------------|
| `position` | Fait référence au classement de l'élément recommandé spécifique dans la liste suggérée (par exemple, `position = 2`). <br>![Classement de la position de l'article.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Représente l'identifiant de l'utilisateur, crucial pour personnaliser les résultats des recommandations. Définissez le paramètre `ui` comme étant le `external_id` du client dans Braze. S'il est omis, le Constructeur renverra des recommandations générales au lieu de recommandations spécifiques à l'utilisateur. |
| `pod_id` | Identifiant du pod contenant la stratégie et les règles de searchandising pour les recommandations (par exemple, un pod avec une stratégie bestseller génère un bestseller personnalisé). |
| `key` | La clé d'index du constructeur pour ce client. |
| `style_id` | Détermine les images à afficher pour la fiche produit. Par exemple, différents sites `style_ids` affichent des images uniques de fiches produits. |
| `campaign_id` | ID unique pour la campagne d'e-mail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Entrées optionnelles

| Entrée | Description |
|-------------|-------------|
| `item_id` | Représente l'élément initiateur. Nécessaire pour les stratégies basées sur les éléments, telles que les offres alternatives, complémentaires et groupées. Par exemple, le premier élément d'un e-mail est l'élément initiateur, les éléments suivants constituant des alternatives. |
| `num_results` | Nombre de produits à ajouter à l'e-mail. La valeur par défaut est de 10, jusqu'à 100. Par exemple, `num_results = 3` signifie que trois recommandations sont ajoutées. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

