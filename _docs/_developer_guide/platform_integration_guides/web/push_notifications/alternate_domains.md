---
nav_title: Alternate Domains
article_title: Alternate Push Notification Domains for the Braze Web SDK
platform: Web
page_order: 20
page_type: reference
description: "This article covers how to integrate Braze Web Push on an alternate domain."
channel: push

---

# Alternate push notification domains

> To integrate web push, your domain must be [secure](https://w3c.github.io/webappsec-secure-contexts/), which generally means `https`, `localhost`, and other exceptions as defined in the [W3C push standard](https://www.w3.org/TR/service-workers/#security-considerations). You'll also need to be able to register a Service Worker at the root of your domain, or at least be able to control the HTTP headers for that file. This article covers how to integrate Braze Web Push on an alternate domain.

## Use cases

If you can't meet all of the criteria outlined in the [W3C push standard](https://www.w3.org/TR/service-workers/#security-considerations), you can use this method to add a push prompt dialog to your website instead. This can be helpful if you want to let your users opt-in from an `http` website or a browser extension popup thats preventing your push prompt from displaying.

## Considerations

Keep in mind, like many workarounds on the web, browsers continually evolve, and this method may not be viable in the future. Before continuing, ensure that:

- You own a separate secure domain (`https://`) and permissions to register a Service Worker on that domain.
- Users are logged in to your website which ensures push tokens are match to the correct profile.

{% alert important %}
You cannot use this method to implement push notifications for Shopify. Shopify will automatically remove the headers need to deliver push this way.
{% endalert %}

## Setting up an alternate push domain

To make the following example clear, we'll use use `http://insecure.com` and `https://secure.com` as our two domains with the goal of getting visitors to register for push on `http://insecure.com`. This example could also be applied to a `chrome-extension://` scheme for a browser extension's popup page.

### Step 1: Initiate prompting flow

On `insecure.com`, open a new window to your secure domain using a URL parameter to pass the currently logged-in user's Braze external ID.

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

### Step 2: Register for push

At this point, `secure.com` will open a popup window in which you can initialize the Braze Web SDK for the same user ID and request the user's permission for Web push.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Step 3: Communicate between domains (optional)

Now that users can opt-in from this workflow originating on `insecure.com`, you may want to modify your site based on if the user is already opted-in or not. There's no point in asking the user to register for push if they already are.

You can use iFrames and the [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API to communicate between your two domains. 

**insecure.com**

On our `insecure.com` domain, we will ask the secure domain (where push is _actually_ registered) for information on the current user's push registration:

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

