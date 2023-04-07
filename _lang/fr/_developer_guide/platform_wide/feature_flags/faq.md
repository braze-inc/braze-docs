---
nav_title: Foire aux questions
article_title: Foire aux questions
page_order: 40
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les campagnes."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# Foire aux questions

## Fonctionnalité et support

### Comment puis-je rejoindre le programme bêta des indicateurs de fonctionnalité ? {#join-beta}

Les indicateurs de fonctionnalité de Braze sont actuellement en version bêta ouverte. Veuillez demander à votre équipe de compte Braze pour en savoir plus sur l’adhésion au programme bêta.

### Sur quelles plateformes les indicateurs de fonctionnalité Braze sont-ils pris en charge ? {#platforms}

Braze prend en charge les indicateurs de fonctionnalité sur les plateformes iOS, Android et Web avec les exigences de version SDK suivantes :

{% sdk_min_versions android:24.2.0 web:4.6.0 swift:5.9.0 %}

Avez-vous besoin d’assistance sur d’autres plateformes ? Envoyez un e-mail à notre équipe : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Quel est le niveau d’effort requis lors de la mise en œuvre d’un indicateur de fonctionnalité ? {#level-of-effort}

Un indicateur de fonctionnalité peut être créé et intégré en quelques minutes. 

La plupart des efforts impliqués seront liés à la création par votre équipe d’ingénieurs de la nouvelle fonctionnalité que vous prévoyez de déployer. Mais lorsqu’il s’agit d’ajouter un indicateur de fonctionnalité, il s’agit simplement d’un énoncé `IF`/`ELSE` dans le code de votre application ou de votre site Web :

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

### Comment les indicateurs de fonctionnalité peuvent-ils bénéficier aux équipes marketing ? {#marketing-teams}

Les équipes marketing peuvent utiliser des indicateurs de fonctionnalité pour coordonner les annonces de produit (comme les e-mails de lancement de produit) lorsqu'une fonctionnalité n'est activée que pour un faible pourcentage d'utilisateurs.

<!-- TO BE ADDED ONCE CANVAS FEATURE FLAG STEP IS COMPLETE: For example, with Braze feature flags you can rollout a new Customer Loyalty program to 10% of users in your app, and send an email, push, or other messaging to that same 10% of enabled users using the Canvas Feature Flag step. -->

### Comment les indicateurs de fonctionnalité peuvent-ils bénéficier aux équipes produit ? {#product-teams}

Les équipes produit peuvent utiliser des indicateurs de fonctionnalité pour effectuer des déploiements progressifs ou des lancements en douceur de nouvelles fonctionnalités afin de surveiller les indicateurs de performance clés et les commentaires des clients avant de les mettre à la disposition de tous les utilisateurs.

Les équipes produit peuvent utiliser les [propriétés de l'indicateur de fonctionnalité][properties] pour remplir à distance le contenu d'une application, comme des liens profonds, du texte, des images ou d'autres contenus dynamiques.

<!-- TO BE ADDED ONCE CANVAS FEATURE FLAG STEP IS COMPLETE: Using the Canvas Feature Flag step, Product teams can also run an A/B split test to measure how a new feature impacts conversion rates compared to users with the feature disabled. -->

### Comment les indicateurs de fonctionnalité peuvent-ils bénéficier aux équipes d’ingénierie ? {#engineering-teams}

Les équipes d'ingénierie peuvent utiliser des indicateurs de fonctionnalité pour réduire le risque inhérent au lancement de nouvelles fonctionnalités et éviter de se précipiter pour déployer des correctifs de code au milieu de la nuit.

En publiant un nouveau code caché derrière un indicateur de fonctionnalité, votre équipe peut activer ou désactiver la fonctionnalité à distance à partir du tableau de bord de Braze, évitant ainsi le retard inhérent à la suppression d’un nouveau code ou à l’attente de l’approbation de mise à jour par l’App Store.

## Déploiements et ciblage des fonctionnalités

### Un indicateur de fonctionnalité peut-il être déployé uniquement pour un groupe sélectionné d’utilisateurs ? {#target-users}

Oui, il vous suffit de créer un segment dans Braze qui cible des utilisateurs spécifiques &mdash; par adresse e-mail, `user_id` ou tout autre attribut de vos profils utilisateur. Ensuite, déployez l’indicateur de fonctionnalité pour atteindre 100 % de ce segment.

### Comment l’ajustement du pourcentage de déploiement affecte-t-il les utilisateurs qui étaient précédemment inclus dans le groupe activé ? {#random-buckets}

Les déploiements d’indicateurs de fonctionnalité restent cohérents pour les utilisateurs, que ce soit au niveau des appareils ou des sessions.

- Lorsqu’un indicateur de fonctionnalité est déployé pour 10 % d’utilisateurs aléatoires, ce pourcentage reste activé et persiste pendant toute la durée de vie de cet indicateur de fonctionnalité.
- Si vous augmentez le déploiement de 10 % à 20 %, les 10 % d’origine conserveront l’activation et 10 % d’utilisateurs supplémentaires seront ajoutés au groupe « activé ».
- Si vous réduisez le déploiement de 20 % à 10 %, seuls les 10 % d’utilisateurs d’origine resteront activés.

Cette stratégie permet de garantir que les utilisateurs bénéficient d’une expérience cohérente au sein de votre application et ne basculent pas entre les expériences d’une session à l’autre. Bien sûr, la désactivation d’une fonctionnalité jusqu’à 0 % supprimera tous les utilisateurs de l’indicateur de fonctionnalité, ce qui est utile au cas où vous découvriez un bug ou auriez besoin de désactiver complètement la fonctionnalité.

### Puis-je créer un segment d’utilisateurs qui se trouvent actuellement dans un indicateur de fonctionnalité ? {#feature-flag-filter}

C’est sur notre feuille de route produit. Pour vous aider à faire passer cette fonction en priorité, veuillez faire part de vos commentaires à votre équipe de compte Braze ou envoyer un e-mail à notre équipe : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

## Sujets techniques

### Les indicateurs de fonctionnalité peuvent-ils être utilisés pour contrôler quand le SDK Braze est initialisé ? {#initialization}

Non, le SDK doit être initialisé afin de télécharger et de synchroniser les indicateurs de fonctionnalité pour l’utilisateur actuel. Cela signifie que vous ne pouvez pas utiliser les indicateurs de fonctionnalité pour limiter les utilisateurs créés ou suivis dans Braze.

### À quelle fréquence les indicateurs de fonctionnalité sont-ils actualisés par le SDK ? {#refresh-frequency}

Les indicateurs de fonctionnalité sont actualisés au début de la session et lors du changement d’utilisateurs actifs. Les indicateurs de fonctionnalité peuvent également être actualisés manuellement à l'aide de la [méthode d'actualisation][refreshing] du SDK.

Gardez à l’esprit que les bonnes pratiques en matière de données recommandent de ne pas actualiser les indicateurs de fonctionnalité trop rapidement (avec une limitation du taux potentielle si c’est le cas), il est donc préférable d’actualiser seulement avant qu’un utilisateur interagisse avec de nouvelles fonctionnalités ou périodiquement dans l’application si nécessaire.

### Les indicateurs de fonctionnalité sont-ils disponibles lorsqu’un utilisateur est hors ligne ? {#offline}

Oui, une fois que les indicateurs de fonctionnalité sont actualisés, ils sont stockés localement sur l'appareil de l'utilisateur et sont accessibles hors ligne.

### Que se passe-t-il si les indicateurs de fonctionnalité sont actualisés en cours de session ? {#listen-for-updates}

Les indicateurs de fonctionnalité peuvent être actualisés en cours de session. Dans certains cas, vous pouvez mettre à jour votre application si certaines variables ou votre configuration doivent changer. Il existe d’autres scénarios dans lesquels vous ne souhaitez peut-être pas mettre à jour votre application, afin d’éviter un changement choquant dans la façon dont votre IU s’affiche.

Pour le contrôler, [écoutez les mises à jour][listen-for-updates] des indicateurs de fonctionnalité et prenez la décision de réafficher ou non votre application en fonction des indicateurs de fonctionnalité qui ont été modifiés. 

## Questions ?

Vous avez des questions ou des commentaires ? Envoyez un e-mail à notre équipe : [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

[properties]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties
[refreshing]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing
[listen-for-updates]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates