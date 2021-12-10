---
nav_title: Domaine de Push Web alternatif
article_title: Domaine de Push Web alternatif
platform: Web
page_order: 20
page_type: Référence
description: "Cet article explique comment intégrer Braze Web Push dans un domaine alternatif."
channel: Pousser
---

# Domaine de push web alternatif

Pour intégrer Push sur le web, votre domaine doit être [sécurisé][2], ce qui signifie généralement `https`, `localhost`, et d'autres exceptions telles que définies dans le [W3C Push Standard][1]. Vous devrez également pouvoir enregistrer un Service Worker à la racine de votre domaine, ou au moins être en mesure de contrôler les en-têtes HTTP pour ce fichier.

_Si vous ne pouvez pas répondre à tous ces critères_, utilisez ce guide pour configurer une solution de contournement qui vous permet d'ajouter une boîte de dialogue Push Prompt à votre site web.

Par exemple, si vous voulez que l'utilisateur opte pour un site web `http` (non sécurisé) ou à partir d'une fenêtre pop-up d'extension de navigateur qui empêche l'affichage de la notification push, continuez à lire!

**met en garde**: Gardez à l'esprit que comme beaucoup de contournements sur le web, les navigateurs évoluent continuellement et, à l'avenir, cela pourrait ne pas fonctionner comme prévu.

* Cela nécessite que vous possédiez un domaine sécurisé séparé (`https://`) et que vous ayez accès pour enregistrer un Service Worker sur ce domaine.
* Cela nécessite que les utilisateurs soient connectés à votre site web, pour s'assurer que les jetons push sont liés aux mêmes profils.

Pour rendre l'exemple ci-dessous plus clair, nous utiliserons `http://insecure.com` et `https://secure. om` comme nos deux domaines dans le but de faire s'inscrire les visiteurs sur `http://insecure.com`. Cet exemple pourrait également être appliqué à un schéma `chrome-extension://` pour une page popup d'une extension de navigateur.

## Étape 1 : Lancer le flux de demande

Sur `non sécurisé. om`, ouvrez une nouvelle fenêtre sur votre domaine sécurisé en utilisant un paramètre d'URL pour passer l'ID externe de l'utilisateur connecté à Braze.


**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// le même ID que vous utiliseriez avec `appboy. hangeUser`:
const user_id = getUserIdSomehow();
// transmettent l'identifiant utilisateur dans l'URL du domaine sécurisé :
const secure_url = `https://secure. om/push-registration.html?external_id=${user_id}`;

// lorsque l'utilisateur prend une action, ouvrez l'URL sécurisée dans une nouvelle fenêtre
document. etElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window. lert('La popup a été bloquée par votre navigateur');
    } else {
        // l'utilisateur est affiché une fenêtre popup
        // et vous pouvez maintenant demander un push dans cette fenêtre
    }
}
</script>
```

## Étape 2 : S'inscrire pour pousser

À ce stade, `sécurisé. om` ouvrira une fenêtre popup dans laquelle vous pourrez initialiser le Braze Web SDK pour le même ID d'utilisateur, et demander la permission de l'utilisateur pour Web Push.

**https://secure.com/push-registration.html**
```html
<html>
    <head>
        <title>Opt-In pour Push</title>
        <script src="https://js.appboycdn.com/web-sdk/3.1/appboy.min.js"></script>
    </head>
    <body>
    <button id="opt-in">Opt In for Push</button>
    <script>
        // initialise Braze
        appboy. nitialize("VOTRE-API-KEY", {
            baseUrl: "VOTRE-SDK-BASE-URL",
            enableLogging: true
        });
        // analyse le `external_id` à partir des paramètres d'URL
        const external_id = (location. earch.substring(1).split('&').find(param => param.startsWith('external_id=')) || ''). plit('=')[1] || '';
        if (external_id) {
            appboy. hangeUser(external_id);
        }
        appboy. penSession();
        appboy.display. utomatifyShowNewInAppMessages();

        // lorsque l'utilisateur clique sur notre bouton Opt In, demande l'autorisation
        document. etElementById("opt-in").onclick = function(){
            appboy. egisterAppboyPushMessages(() => {
                fenêtre. lert(`Vous êtes enregistré pour push!`);
                fenêtre. perdre();
            }, () => {
                fenêtre. lert(`Quelque chose s'est mal passé. );
            });
        };
    </script>
    </body>
</html>
```

## Étape 3 : Communiquer entre les domaines (facultatif)

Maintenant que les utilisateurs peuvent opter pour ce flux de travail à partir de `non sécurisé. om`, vous voudrez peut-être modifier votre site en fonction du fait que l'utilisateur est déjà inscrit ou non. Il ne sert à rien de demander à l'utilisateur de s'inscrire pour push s'ils le sont déjà.

Vous pouvez utiliser iFrames et l'API [`postMessage`][3] pour communiquer entre vos deux domaines.

**insecure.com**

Sur notre `non sécurisé. om` domaine, nous demanderons au domaine sécurisé (où push est _en fait_ enregistré) des informations sur l'enregistrement push de l'utilisateur actuel :

```html
<! - Créer un iframe pour le domaine sécurisé et exécuter getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
fonction getPushStatus(event){
    // envoyer un message à l'iframe demandant le statut push
    événement. arget.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure. om');
    // écoute une réponse depuis la fenêtre du domaine
    . ddEventListener("message", (event) => {
        if (event.origin === "http://insecure. om" && event.data. ype === 'set_push_status') {
            // met à jour la page en fonction de la permission push que nous avons reçue
            fenêtre. lert(`L'utilisateur est-il enregistré pour push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/push-status.html**

```html
<script src="https://js.appboycdn.com/web-sdk/3.1/appboy.min.js"></script>
<script>
// initialise Braze
appboy. nitialize("VOTRE-API-KEY", {
    baseUrl: "VOTRE-SDK-BASE-URL",
    enableLogging: true
});

// écoute une requête depuis notre fenêtre non sécurisée
. ddEventListener("message", (event) => {
    if (event.origin === "http://insecure. om") {
        // quand ils demandent le statut push, récupérer de Braze SDK
        if (événement). ata.type === 'get_push_status') {
            // envoie la fenêtre parente (non sécurisée. om) la fenêtre de résultats
            . op.postMessage({
                type: 'set_push_status',
                isPushPermissiongranted : appboy. sPushPermissionGranted()
            }, événement. rigin);
        }
    }
});
</script>
```



[1]: https://www.w3.org/TR/service-workers/#security-considerations
[2]: https://w3c.github.io/webappsec-secure-contexts/
[3]: https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage
