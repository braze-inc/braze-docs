---
nav_title: Apteligent
article_title: Apteligent
alias: /fr/partners/apteligent/
description: "Cet article décrit le partenariat entre Braze et Apteligent, qui détaille les rapports de plantage, vous permettant d'enregistrer des données critiques dans votre solution Braze existante."
page_type: partenaire
search_tag: Partenaire
---

# Apteligent

> Braze est dédié à la création d’intégrations de partenaires qui fournissent des approches basées sur des données pour améliorer l’expérience utilisateur de votre application. Le partenariat [Apteligent][1] et Braze combine l'automatisation de l'engagement multicanal de Braze avec le rapport détaillé de plantage d'Apteligent, vous permettant d'enregistrer des données critiques dans votre solution Braze existante. Ensemble, Apteligent et Braze peuvent vous aider à segmenter, comprendre et engager avec vos utilisateurs qui ont connu des plantages d'applications.

{% alert warning %}
Cette intégration n'est actuellement prise en charge que sur iOS.
{% endalert %}

## Intégration iOS {#apteligent-ios-integration}

Pour intégrer Apteligent à Braze sur iOS, faites ce qui suit :

### Étape 1

Enregistrer un observateur. Assurez-vous que cela est fait avant d'initialiser Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Étape 2

Le SDK Apteligent lancera une notification lorsque l'utilisateur chargera l'application après un crash. La notification contiendra le nom du plantage, la raison et la date d'occurrence.

Lors de la réception de la notification, enregistrer un événement de plantage personnalisé et mettre à jour les attributs de l'utilisateur avec l'analyse de rapport de plantage d'Apteligent :

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance]. ser setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDate:crashInfo[@"crashDate"]];
}
```

Voilà! Maintenant, vous pourrez exploiter la puissance de la segmentation, de l'analyse et de l'engagement de Braze en utilisant les informations de crash fournies par Apteligent.

[1]: https://www.apteligent.com/
