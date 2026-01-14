# Foire aux questions

> Cet article fournit des réponses à des questions fréquemment posées sur les indicateurs de fonctionnalité.

## Fonctionnalité et support

### Sur quelles plateformes les indicateurs de fonctionnalité Braze sont-ils pris en charge ? {#platforms}

Braze prend en charge les indicateurs de fonctionnalité sur les plateformes iOS, Android et Web avec les exigences suivantes en termes de versions de SDK :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Avez-vous besoin d’assistance sur d’autres plateformes ? Envoyez un e-mail à notre équipe : [fonctionnalité-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Quel est le niveau d’effort requis lors de la mise en œuvre d’un indicateur de fonctionnalité ? {#level-of-effort}

Un indicateur de fonctionnalité peut être créé et intégré en quelques minutes. 

La plupart des efforts impliqués seront liés à la création par votre équipe d’ingénieurs de la nouvelle fonctionnalité que vous prévoyez de déployer. Mais lorsqu’il s’agit d’ajouter un indicateur de fonctionnalité, il s’agit simplement d’un énoncé `IF`/`ELSE` dans le code de votre application ou de votre site Web :

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### Comment les indicateurs de fonctionnalité peuvent-ils bénéficier aux équipes marketing ? {#marketing-teams}

Les équipes marketing peuvent utiliser des indicateurs de fonctionnalité pour coordonner les annonces de produit (comme les e-mails de lancement de produit) lorsqu'une fonctionnalité n'est activée que pour un faible pourcentage d'utilisateurs.

Par exemple, avec les drapeaux de fonctionnalité de Braze, vous pouvez déployer un nouveau programme de fidélisation des clients pour 10 % des utilisateurs de votre application, et envoyer un e-mail, un push ou un autre message à ces mêmes 10 % d'utilisateurs activés à l'aide de l'étape du drapeau de fonctionnalité de Canvas. 

### Comment les indicateurs de fonctionnalité peuvent-ils bénéficier aux équipes produit ? {#product-teams}

Les équipes produit peuvent utiliser des indicateurs de fonctionnalité pour effectuer des déploiements progressifs ou des lancements en douceur de nouvelles fonctionnalités afin de surveiller les indicateurs de performance clés et les commentaires des clients avant de les mettre à la disposition de tous les utilisateurs.

Les équipes produit peuvent utiliser les [propriétés des drapeaux de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties) pour alimenter à distance le contenu d'une application, comme des liens profonds, du texte, des images ou d'autres contenus dynamiques.

À l'aide de l'étape Canvas Feature Flag, les équipes Produit peuvent également effectuer un test A/B fractionné pour mesurer l'impact d'une nouvelle fonctionnalité sur les taux de conversion par rapport aux utilisateurs dont la fonctionnalité est désactivée. 

### En quoi les fonctionnalités peuvent-elles être utiles aux équipes d’ingénierie ? {#engineering-teams}

Les équipes d'ingénieurs peuvent utiliser des drapeaux de fonctionnalité pour réduire le risque inhérent au lancement de nouvelles fonctionnalités et éviter de déployer précipitamment des correctifs de code au milieu de la nuit.

En publiant un nouveau code caché derrière un indicateur de fonctionnalité, votre équipe peut activer ou désactiver la fonctionnalité à distance à partir du tableau de bord de Braze, évitant ainsi le retard inhérent à la suppression d’un nouveau code ou à l’attente de l’approbation de mise à jour par l’App Store.

## Déploiements et ciblage des fonctionnalités

### Un indicateur de fonctionnalité peut-il être déployé uniquement pour un groupe sélectionné d’utilisateurs ? {#target-users}

Oui, il vous suffit de créer un segment dans Braze qui cible des utilisateurs spécifiques par adresse e-mail, `user_id` ou tout autre attribut de vos profils utilisateur. Ensuite, déployez l’indicateur de fonctionnalité pour atteindre 100 % de ce segment.

### Comment l’ajustement du pourcentage de déploiement affecte-t-il les utilisateurs qui étaient précédemment inclus dans le groupe activé ? {#random-buckets}

Les déploiements de drapeaux de fonctionnalité restent cohérents pour les utilisateurs, quels que soient les appareils et les sessions.

- Lorsqu’un indicateur de fonctionnalité est déployé pour 10 % d’utilisateurs aléatoires, ce pourcentage reste activé et persiste pendant toute la durée de vie de cet indicateur de fonctionnalité.
- Si vous augmentez le déploiement de 10 % à 20 %, les 10 % d’origine conserveront l’activation et 10 % d’utilisateurs supplémentaires seront ajoutés au groupe « activé ».
- Si vous réduisez le déploiement de 20 % à 10 %, seuls les 10 % d’utilisateurs d’origine resteront activés.

Cette stratégie permet de s'assurer que les utilisateurs bénéficient d'une expérience sur votre application cohérente et qu'ils ne basculent pas d'une session à l'autre. Bien entendu, la désactivation d'une fonctionnalité jusqu'à 0 % supprimera tous les utilisateurs du drapeau de la fonctionnalité, ce qui est utile si vous découvrez un bogue ou si vous avez besoin de désactiver complètement la fonctionnalité.

## Sujets techniques

### Les indicateurs de fonctionnalité peuvent-ils être utilisés pour contrôler quand le SDK Braze est initialisé ? {#initialization}

Non, le SDK doit être initialisé afin de télécharger et de synchroniser les indicateurs de fonctionnalités pour l’utilisateur actuel. Cela signifie que vous ne pouvez pas utiliser les indicateurs de fonctionnalité pour limiter les utilisateurs créés ou suivis dans Braze.

### À quelle fréquence le SDK actualise-t-il les indicateurs de fonctionnalités ? {#refresh-frequency}

Les indicateurs de fonctionnalité sont actualisés au début de la session et lors du changement d’utilisateurs actifs. Les indicateurs de fonctionnalités peuvent également être actualisés manuellement à l'aide de la [méthode d'actualisation]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing) du SDK. L'actualisation des drapeaux de fonctionnalité est limitée à une fois toutes les cinq minutes (sous réserve de modifications).

Gardez à l'esprit que les bonnes pratiques en matière de données recommandent de ne pas actualiser les fonctionnalités trop rapidement (au risque de limiter le débit). Il est donc préférable de n'actualiser les fonctionnalités qu'avant que l'utilisateur n'interagisse avec de nouvelles fonctionnalités ou périodiquement dans l'application, si nécessaire.

### Les indicateurs de fonctionnalité sont-ils disponibles lorsqu’un utilisateur est hors ligne ? {#offline}

Oui, après avoir été actualisés, les indicateurs de fonctionnalité sont stockés localement sur l'appareil de l'utilisateur et peuvent être consultés lorsqu'il n'est pas en ligne.

### Que se passe-t-il si les indicateurs de fonctionnalité sont actualisés en cours de session ? {#listen-for-updates}

Les indicateurs de fonctionnalité peuvent être actualisés en cours de session. Dans certains cas, vous pouvez mettre à jour votre application si certaines variables ou votre configuration doivent changer. Il existe d'autres scénarios dans lesquels vous ne souhaitez pas mettre à jour votre application, afin d'éviter un changement choquant dans la manière dont votre interface utilisateur est rendue.

Pour contrôler cela, [écoutez les mises à jour]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates) des indicateurs de fonctionnalités et déterminez si vous devez générer ou non un nouveau rendu de votre application en fonction des indicateurs de fonctionnalités qui ont changé. 

### Pourquoi les utilisateurs de mon groupe de contrôle global ne reçoivent-ils pas les expérimentations d’indicateurs de fonctionnalité ?

Vous ne pouvez pas activer les indicateurs de fonctionnalité pour les utilisateurs de votre [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/). Cela signifie que les utilisateurs de votre groupe de contrôle global ne peuvent pas non plus participer à des expériences d'indicateur de fonctionnalité.

## Des questions supplémentaires ?

Vous avez des questions ou des commentaires ? Envoyez un e-mail à notre équipe : [fonctionnalité-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

