---
nav_title: Content Security Policy
platform: Web
page_order: 50
page_type: reference
description: "This article covers Content-Security-Policy headers needed with the Braze Web SDK"
---

# Content Security Policy Headers

Content-Security-Policy provides added security by restricting how and where content can be loaded on your website.

For example, you can restrict 3rd party tags, or prevent the use of `eval` to reduce the risk of XSS.

{% alert important %}
This article is intended for developers working on websites that enforce CSP rules, and how to integrate with Braze. It is not intended as advice on how you should approach security.
{% endalert %}

The following directives may be required when CSP is enforced:

| Directive     | Value                                               | Description                                                                                                                                                                     |
| ------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect-src` | Your SDK API endpoint (i.e. `sdk.iad-01.braze.com`) | This should be the same endpoint set in the `baseUrl` initialization option, as found [here](https://www.braze.com/docs/user_guide/administrative/access_braze/sdk_endpoints/). |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

If you use our CDN-hosted SDK, the following directive is required:

| Directive    | Value                      | Description                          |
| ------------ | -------------------------- | ------------------------------------ |
| `script-src` | `https://js.appboycdn.com` | Required if using our CDN-hosted SDK |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

If you use a `nonce` value in your `script-src` or `style-src` directives, you can pass that `nonce` value using the `contentSecurityNonce` initialization option:

```javascript
import braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YWJjMTIz", // assumes a "nonce-YWJjMTIz" CSP value
});
```

If you use the integration snippet which contains reference to `appboyQueue`, the following directive is required:

| Directive    | Value         | Description                                                                                                                                 |
| ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `script-src` | `unsafe-eval` | Required to use the `appboyQueue` replay snippet. Alternatively, use our NPM integration or load the SDK as a `<script src="..."></script>` |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

If you use the built-in Font Awesome library, the following CSP directives are required.

Note: The use of Font Awesome can be disabled using the `doNotLoadFontAwesome: true` initialization option.

| Directive | Value | Description|
| `style-src` | `https://use.fontawesome.com` | Also requires either `unsafe-inline` or a `nonce` value. |
| `font-src` | `https://use.fontawesome.com` | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
