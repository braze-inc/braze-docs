{% multi_lang_include archive/web-v4-rename.md %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Protocoles de poussée

Les notifications push web sont mises en œuvre à l'aide de la [norme push du W3C](http://www.w3.org/TR/push-api/), prise en charge par la plupart des grands navigateurs. Pour plus d'informations sur les normes spécifiques du protocole push et la prise en charge des navigateurs, vous pouvez consulter les ressources d'[Apple](https://developer.apple.com/notifications/safari-push-notifications/) [, de Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility) et de [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/).

## Mise en place des notifications push

### Étape 1 : Configurez votre service de traitement

Dans le fichier `service-worker.js` de votre projet, ajoutez l'extrait de code suivant et définissez l'option d'initialisation à lors de l'initialisation du SDK Web. [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) à `true` lors de l'initialisation du SDK Web.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Votre serveur Web doit renvoyer un `Content-Type: application/javascript` lorsqu’il notifie votre fichier de service de traitement. En outre, si votre fichier de service de traitement n'est pas nommé `service-worker.js`, vous devrez utiliser l' [option d'initialisation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation`.
{% endalert %}

### Étape 2 : Enregistrer le navigateur

Pour demander immédiatement des autorisations push à un utilisateur afin que son navigateur puisse recevoir des notifications push, appelez `braze.requestPushPermission()`. Pour vérifier si la fonction "push" est prise en charge dans leur navigateur, appelez `braze.isPushSupported()`.

Vous pouvez également [envoyer une invitation à pousser à]({{site.baseurl}}/developer_guide/push_notifications/soft_push_prompts/?sdktab=web) l'utilisateur avant de demander l'autorisation de pousser pour afficher votre propre interface utilisateur liée à la poussée.

{% alert important %}
Sur macOS, **Google Chrome** et **Google Chrome Helper (Alertes)** doivent tous deux être activés par l'utilisateur final dans **Paramètres système > Notifications** avant que les notifications push puissent être affichées - même si des autorisations sont accordées.
{% endalert %}

### Étape 3 : Désactiver `skipWaiting` (optionnel)

Le fichier du service de traitement de Braze appellera automatiquement `skipWaiting` lors de l'installation. Si vous souhaitez désactiver cette fonctionnalité, ajoutez le code suivant à votre fichier de service de traitement, après avoir importé Braze :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Désinscription d'un utilisateur

Pour désinscrire un utilisateur, appelez `braze.unregisterPush()`.

{% alert important %}
Les versions récentes de Safari et de Firefox exigent que vous appeliez cette méthode à partir d'un gestionnaire d'événements de courte durée (tel qu'un gestionnaire de clic sur un bouton ou une invite de type soft push). Ceci est cohérent avec les [meilleures pratiques de Chrome en matière d’expérience utilisateur](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) pour l’enregistrement de notifications push.
{% endalert %}

## Domaines alternatifs

Pour intégrer une notification push web, votre domaine doit être [sécurisé](https://w3c.github.io/webappsec-secure-contexts/), ce qui signifie généralement `https`, `localhost`, et d'autres exceptions telles que celles définies dans la [norme de notification push W3C](https://www.w3.org/TR/service-workers/#security-considerations). Vous devrez également pouvoir enregistrer un service de traitement à la racine de votre domaine, ou au moins pouvoir contrôler les en-têtes HTTP pour ce fichier. Cet article explique comment intégrer les notifications push Braze pour le Web sur un domaine alternatif.

### Cas d’utilisation

Si vous ne pouvez pas répondre à tous les critères énoncés dans la [norme "push" du W3C](https://www.w3.org/TR/service-workers/#security-considerations), vous pouvez utiliser cette méthode pour ajouter une boîte de dialogue "push" à votre site web. Cela peut s'avérer utile si vous souhaitez permettre à vos utilisateurs de s'abonner à partir d'un site web `http` ou d'un popup d'extension de navigateur qui empêche votre demande d'abonnement de s'afficher.

### Considérations

Gardez à l'esprit que, comme beaucoup de solutions de contournement sur le web, les navigateurs évoluent continuellement et que cette méthode pourrait ne plus être viable à l'avenir. Avant de poursuivre, assurez-vous que

- Vous possédez un domaine sécurisé séparé (`https://`) et vous avez l'autorisation d'enregistrer un Service Worker sur ce domaine.
- Les utilisateurs sont connectés à votre site web, ce qui garantit que les jetons sont associés au bon profil.

{% alert important %}
Vous ne pouvez pas utiliser cette méthode pour mettre en œuvre des notifications push pour Shopify. Shopify supprimera automatiquement les en-têtes nécessaires à la livraison de push de cette manière.
{% endalert %}

### Mise en place d'un domaine push alternatif

Pour expliquer l’exemple suivant, nous utiliserons `http://insecure.com` et `https://secure.com` comme nos deux domaines dans le but d’amener les visiteurs à s’inscrire pour les notifications push sur `http://insecure.com`. Cet exemple peut également être appliqué à un système `chrome-extension://` pour la page contextuelle d’une extension de navigateur.

#### Étape 1 : Initier le flux de demande

Sur `insecure.com`, ouvrez une nouvelle fenêtre vers votre domaine sécurisé en utilisant un paramètre URL pour transmettre l’ID externe Braze de l’utilisateur actuellement connecté.

**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// the same ID you would use with `braze.changeUser`:
const user_id = getUserIdSomehow();
// pass the user ID into the secure domain URL:
const secure_url = `https://secure.com/push-registration.html?external_id=${user_id}`;

// when the user takes some action, open the secure URL in a new window
document.getElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window.alert('The popup was blocked by your browser');
    } else {
        // user is shown a popup window
        // and you can now prompt for push in this window
    }
}
</script>
```

#### Étape 2 : Enregistrer la notification push

À ce stade, `secure.com` ouvre une fenêtre contextuelle dans laquelle vous pouvez initialiser le SDK Braze pour le Web pour le même ID utilisateur et demander l’autorisation de l’utilisateur pour la notification push Web.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Étape 3 : Communiquer entre les domaines (facultatif)

Maintenant que les utilisateurs peuvent s’abonner à partir de ce flux de travail provenant de `insecure.com`, vous pouvez modifier votre site selon le fait que l’utilisateur est déjà abonné ou pas. Demander à l’utilisateur de s’enregistrer pour les notifications push alors qu’il l’est déjà est inutile.

Vous pouvez utiliser iFrames et l'API [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) pour communiquer entre vos deux domaines. 

**insecure.com**

Sur notre domaine `insecure.com`, nous demanderons au domaine sécurisé (où push est _effectivement_ enregistré) des informations sur l'enregistrement push de l'utilisateur actuel :

```html
<!-- Create an iframe to the secure domain and run getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
function getPushStatus(event){
    // send a message to the iframe asking for push status
    event.target.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure.com');
    // listen for a response from the iframe's domain
    window.addEventListener("message", (event) => {
        if (event.origin === "http://insecure.com" && event.data.type === 'set_push_status') {
            // update the page based on the push permission we're told
            window.alert(`Is user registered for push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/push-status.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Questions fréquemment posées (FAQ)

### Service de traitement

#### Que se passe-t-il si je ne peux pas enregistrer un service de traitement dans le répertoire racine ?

Par défaut, un service de traitement ne peut être utilisé que dans le même répertoire que celui dans lequel il est enregistré. Par exemple, si votre fichier de service de traitement existe dans `/assets/service-worker.js`, vous ne pouvez l’enregistrer que dans `example.com/assets/*` ou un sous-répertoire du dossier `assets` mais pas sur votre page d’accueil (`example.com/`). Pour cette raison, il est recommandé d’héberger et d’enregistrer le service de traitement dans le répertoire racine (par exemple, `https://example.com/service-worker.js`).

Si vous ne pouvez pas enregistrer un service de traitement dans votre domaine racine, une autre approche consiste à utiliser l’en-tête HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) lorsque vous notifiez votre fichier de service de traitement. En configurant votre serveur pour renvoyer `Service-Worker-Allowed: /` en réponse au service de traitement, le navigateur recevra l’instruction d’élargir la portée et d’autoriser l’utilisation dans un répertoire différent.

#### Puis-je créer un service de traitement à l’aide d’un Gestionnaire de balises ?

Non, il faut héberger les services de traitement sur le serveur de votre site Web et il n’est pas possible de les charger à l’aide d’un Gestionnaire de balises.

### Sécurité du site

#### Le protocole HTTPS est-il nécessaire ?

Oui. Les normes Web exigent que le domaine demandant l’autorisation de notification push soit sécurisé.

#### Quand un site est-il considéré comme "sûr" ?

Un site est considéré comme sûr s'il correspond à l'un des modèles d'origine sécurisés suivants. Les notifications push Web de Braze sont créées sur la base de cette norme ouverte, ce qui permet d'éviter les attaques de type man-in-the-middle.

- `(https, , *)`
- `(wss, *, *)`
- `(, localhost, )`
- `(, .localhost, *)`
- `(, 127/8, )`
- `(, ::1/128, *)`
- `(file, *, —)`
- `(chrome-extension, *, —)`

#### Que se passe-t-il si un site sécurisé n’est pas disponible ?

Bien que les meilleures pratiques du secteur soient de rendre votre site sûr, les clients qui ne peuvent pas sécuriser leur domaine de site peuvent contourner l’exigence en utilisant un modal sécurisé. Pour en savoir plus, consultez notre guide d’utilisation [Notification push sur un domaine alternatif]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) ou visionnez une [démonstration de travail](http://appboyj.com/modal-test.html).
