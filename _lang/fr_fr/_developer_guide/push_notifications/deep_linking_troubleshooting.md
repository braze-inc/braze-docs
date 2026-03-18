---
nav_title: Résolution des problèmes de création de liens profonds
article_title: Résolution des problèmes de création de liens profonds
description: "Problèmes courants liés à la création de liens profonds sur iOS et comment les diagnostiquer, y compris les liens personnalisés, les liens universels, les liens e-mail et les fournisseurs tiers tels que Branch."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Résolution des problèmes de création de liens profonds

> Cette page traite des problèmes courants liés à la création de liens profonds sur iOS et explique comment les diagnostiquer. Pour obtenir de l'aide afin de choisir le type de lien approprié, veuillez consulter [le guide sur la création de liens profonds iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Pour plus de détails sur la mise en œuvre, veuillez consulter [la section Création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## Le lien profond du schéma personnalisé n'ouvre pas la vue appropriée.

Si un lien profond personnalisé (par exemple, `myapp://products/123`) ouvre votre application mais ne vous redirige pas vers l'écran souhaité :

1. **Veuillez vérifier que le programme est bien enregistré.** Dans Xcode, veuillez vérifier que votre schéma est répertorié sous`CFBundleURLTypes`  dans `Info.plist`.
2. **Veuillez vérifier votre gestionnaire.** Veuillez définir un point d'arrêt dans`application(_:open:options:)`afin de vérifier qu'il est bien appelé et inspecter le`url`paramètre.
3. **Veuillez vérifier le lien de manière indépendante.** Veuillez exécuter la commande suivante depuis le terminal afin de tester le lien profond en dehors de Braze :
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Si le lien ne fonctionne pas ici, le problème provient de la gestion des URL de votre application, et non de Braze.
4. **Veuillez vérifier le format de l'URL.** Veuillez vérifier que l'URL de votre campagne correspond à celle attendue par votre gestionnaire. Les erreurs courantes incluent des composants de chemin manquants ou une casse incorrecte.

## Le lien universel s'ouvre dans Safari au lieu de l'application.

Si un lien universel (par exemple, `https://myapp.com/products/123`) s'ouvre dans Safari au lieu de votre application :

### Vérifiez les droits associés aux domaines.

Dans Xcode, veuillez vous rendre dans la cible de votre application > **Capacités& de signature** et vérifiez que`applinks:yourdomain.com`est répertorié sous **Domaines associés**.

### Vérifier le fichier AASA

Votre fichier Apple App Site Association (AASA) doit être hébergé à l'un des emplacements/localisations suivants :

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Veuillez vérifier les éléments suivants :

- Le fichier est fourni via HTTPS avec un certificat valide.
- Le`Content-Type`  est `application/json`.
- La taille du fichier est inférieure à 128 Ko.
- Correspond`appID`à votre ID d'équipe et à votre ID de bundle (par exemple, `ABCDE12345.com.example.myapp`).
- Le `paths`tableau  `components`ou  comprend les modèles d'URL auxquels vous vous attendez.

Vous pouvez valider votre AASA à l'aide de [l'outil de validation de recherche d'Apple](https://search.developer.apple.com/appsearch-validation-tool/) ou en exécutant :

```bash
swcutil dl -d yourdomain.com
```

### Veuillez vérifier le `AppDelegate`

Veuillez vérifier que`application(_:continue:restorationHandler:)`  est implémenté dans votre`AppDelegate`  et qu'il gère correctement `NSUserActivity`le  :

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Vérifiez la configuration du SDK Braze.

Si vous utilisez des liens universels à partir de notifications push, de messages in-app ou de cartes de contenu fournis par Braze, veuillez vérifier que`forwardUniversalLinks`l'option est activée :

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
Le transfert de lien universel nécessite l'accès aux droits de l'application. Lorsqu'il est exécuté dans un simulateur, ces droits ne sont pas directement disponibles. Pour effectuer des tests dans un simulateur, veuillez ajouter le`.entitlements`fichier à la phase pour créer **le** bundle **« Copy Bundle Resources** ».
{% endalert %}

### Veuillez vérifier le problème lié à l'appui long.

Si vous appuyez longuement sur un lien universel et sélectionnez **Ouvrir**, iOS peut « rompre » l'association du lien universel pour ce domaine. Il s'agit d'un comportement connu d'iOS. Pour le réinitialiser, veuillez appuyer longuement sur le lien à nouveau et sélectionner **Ouvrir dans [Nom de l'application]**.

## Le lien profond provenant de l'e-mail n'ouvre pas l'application.

Les liens contenus dans les e-mails passent par le système de suivi des clics de votre ESP, qui encapsule les liens dans un domaine de suivi (par exemple, `https://click.yourdomain.com/...`). Pour que les liens universels fonctionnent à partir des e-mails, il est nécessaire de configurer le fichier AASA sur votre domaine de suivi des clics, et non uniquement sur votre domaine principal.

### Vérifier le domaine de suivi des clics AASA

1. Veuillez identifier votre domaine de suivi des clics à partir des paramètres de votre ESP (Sendgrid, SparkPost ou Amazon SES).
2. Veuillez héberger le fichier AASA à l'adresse `https://your-click-tracking-domain/.well-known/apple-app-site-association`suivante : .
3. Veuillez vous assurer que le fichier AASA sur le domaine de suivi des clics contient les mêmes modèles de `appID`chemin d'accès valides.

Pour obtenir des instructions de configuration spécifiques à ESP, veuillez consulter [les liens universels et les liens vers les applications]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

### Veuillez vérifier la chaîne de redirection.

Certains ESP effectuent une redirection de l'URL de suivi des clics vers votre URL finale. Les liens universels ne fonctionnent que si iOS reconnaît le domaine *initial* (le domaine de suivi des clics) comme étant associé à votre application. Si la redirection contourne la vérification AASA, le lien s'ouvre dans Safari.

Pour tester :

1. Veuillez vous envoyer un e-mail de test.
2. Appuyez longuement sur le lien et examinez l'URL — il s'agit de l'URL de suivi des clics.
3. Veuillez vérifier que ce domaine dispose d'un fichier AASA valide.

## Les liens profonds fonctionnent à partir des notifications push, mais pas à partir des messages in-app (ou vice versa).

### Veuillez vérifier le BrazeDelegate.

Si vous implémentez cette `BrazeDelegate.braze(_:shouldOpenURL:)`fonctionnalité, veuillez vérifier qu'elle gère les liens de manière cohérente sur tous les canaux. Le`context`paramètre inclut le canal source. Veuillez rechercher toute logique conditionnelle susceptible de filtrer accidentellement les liens provenant de canaux spécifiques.

### Activer la jounalisation verbeuse

[Veuillez activer la journalisation détaillée]({{site.baseurl}}/developer_guide/verbose_logging) et reproduire le problème. Veuillez rechercher l'entrée`Opening`de journal suivante :

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Veuillez comparer les résultats du journal pour le canal opérationnel et le canal non opérationnel. Les différences dans`useWebView`  ou`isUniversalLink`  indiquent comment le SDK interprète différemment le lien.

### Vérifier les délégués d'affichage personnalisés

Si vous utilisez un délégué d'affichage de messages in-app personnalisé dans l'application ou un gestionnaire de clics sur les cartes de contenu, veuillez vérifier qu'il transmet correctement les événements de lien au SDK Braze pour traitement.

## « Ouvrir l'URL Web dans l'application » affiche une page vide ou endommagée

Si vous sélectionnez **« Ouvrir l'URL Web dans l'application** » et que la vue Web est vide ou ne fonctionne pas correctement :

1. **Veuillez vérifier que l'URL utilise le protocole HTTPS.** La WebView du SDK nécessite des URL conformes à ATS. Les liens HTTP échouent de manière silencieuse.
2. **Veuillez vérifier les en-têtes de la politique de sécurité du contenu.** Si la page Web cible définit`X-Frame-Options: DENY`ou une restriction`Content-Security-Policy`, elle empêche l'affichage dans une WebView.
3. **Veuillez vérifier les redirections vers des schémas personnalisés.** Si la page Web redirige vers un schéma personnalisé (par exemple, `myapp://`), WebView ne peut pas le gérer.
4. **Veuillez tester l'URL dans Safari.** Si la page ne se charge pas dans Safari sur l'appareil, elle ne se chargera pas non plus dans WebView.

## Résolution des problèmes de la branche avec Braze {#branch}

Si vous utilisez [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) comme fournisseur de liens :

### Veuillez vérifier les routes BrazeDelegate vers Branch.

Veuillez`BrazeDelegate` intercepter les liens Branch et les transmettre au SDK Branch. Veuillez vérifier les éléments suivants :

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Si`shouldOpenURL`des retours sont générés`true`pour les liens Branch, Braze les traite directement au lieu de les acheminer vers Branch.

### Veuillez vérifier le domaine du lien de la succursale.

Veuillez vérifier que le domaine Branch dans votre`BrazeDelegate`correspond bien au domaine réel de votre lien Branch. Branch utilise plusieurs formats de domaine :

- `yourapp.app.link` (par défaut)
- `yourapp-alternate.app.link` (alternatif)
- Domaines personnalisés (s'ils sont configurés dans le tableau de bord Branch)

### Activer la journalisation des deux SDK

Pour déterminer où se trouve la rupture dans la chaîne :

1. Activez [la journalisation détaillée Braze]({{site.baseurl}}/developer_guide/verbose_logging) — recherchez`Opening '<URL>':`les entrées pour vérifier que le SDK a bien reçu le lien.
2. Activez [le mode test Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) — veuillez vérifier le tableau de bord Branch pour les événements de clic sur les liens.
1. Activez [la journalisation détaillée de Braze]({{site.baseurl}}/developer_guide/verbose_logging). Veuillez vérifier`Opening '<URL>':`les entrées pour vous assurer que le SDK a bien reçu le lien.
2. Veuillez activer [le mode test de la succursale](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Veuillez consulter le tableau de bord Branch pour les événements de clic sur les liens.
3. Si Braze enregistre le lien, mais que Branch ne détecte aucun clic, le problème provient probablement de la logique`BrazeDelegate` de routage.

### Veuillez vérifier la configuration du tableau de bord de la succursale.

Dans le tableau de bord de la succursale, veuillez vérifier les éléments suivants :

- **L'ID de bundle** et **l'ID d'équipe** de votre application correspondent à ceux de votre projet Xcode.
- Vos **domaines associés** comprennent le domaine du lien de succursale.
- Votre fichier AASA de branche est valide (la branche l'héberge automatiquement sur`app.link`les domaines).

### Tester les liens de la branche de manière indépendante

Veuillez tester le lien Branch en dehors de Braze afin d'isoler le problème :

1. Veuillez ouvrir le lien Branch dans Safari sur votre appareil. Si l'application ne s'ouvre pas, le problème provient de votre configuration Branch ou AASA, et non de Braze.
2. Veuillez coller le lien Branch dans l'application Notes et appuyez dessus. Les liens universels fonctionnent de manière plus fiable à partir de Notes qu'à partir de la barre d'adresse de Safari.

## Conseils généraux pour le débogage

### Utiliser la journalisation détaillée

[Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/verbose_logging) pour observer précisément comment le SDK traite les liens. Éléments clés à rechercher :

| Entrée de journal | Ce que cela signifie |
|---|---|
| `Opening '<URL>': - channel: notification` | Le SDK traite actuellement un lien provenant d'une notification push. |
| `Opening '<URL>': - channel: inAppMessage` | Le SDK traite actuellement un lien provenant d'un message in-app. |
| `Opening '<URL>': - channel: contentCard` | Le SDK traite actuellement un lien provenant d'une carte de contenu. |
| `useWebView: true` | Le SDK ouvre l'URL dans la vue Web intégrée à l'application. |
| `isUniversalLink: true` | Le SDK a identifié l'URL comme un lien universel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'informations sur la lecture de ces journaux, veuillez consulter [la section Lecture des journaux détaillés]({{site.baseurl}}/developer_guide/verbose_logging).

### Vérifier les liens de manière isolée

Avant de procéder à des tests via Braze, veuillez vérifier que votre lien profond ou lien universel fonctionne correctement de manière autonome :

- **Schéma personnalisé** : Veuillez exécuter`xcrun simctl openurl booted "myapp://path"`dans le terminal.
- **Lien universel** : Veuillez coller l'URL dans l'application Notes sur un appareil physique et appuyez dessus. Veuillez ne pas effectuer de test à partir de la barre d'adresse Safari, car iOS traite les URL saisies différemment des liens sur lesquels on clique.
- **Lien vers la succursale** : Veuillez ouvrir le lien Branch à partir de l'application Notes sur un appareil.

### Veuillez effectuer un test sur un appareil physique.

Les liens universels sont pris en charge de manière limitée dans le simulateur iOS. Veuillez toujours effectuer des tests sur un appareil physique pour obtenir des résultats précis. Si vous devez effectuer des tests dans un simulateur, veuillez ajouter le`.entitlements`fichier à la phase pour créer le** **bundle **« Copy Bundle Resources** ».