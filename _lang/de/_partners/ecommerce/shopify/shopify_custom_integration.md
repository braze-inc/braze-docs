---
nav_title: Shopify Angepasste Integration einrichten
article_title: "Shopify Angepasste Integration einrichten"
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie eine Verbindung zu einem Shopify Hydrogen Shop oder einem beliebigen Shopify Shop ohne Kopfzeile herstellen, indem Sie eine angepasste Storefront verwenden."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 2
---

# Shopify angepasste Integration einrichten

> Auf dieser Seite erfahren Sie, wie Sie Braze mit einem Shopify Hydrogen Shop oder einem beliebigen Shopify Shop ohne Kopfzeile integrieren können, indem Sie eine angepasste Storefront verwenden.

Dieser Leitfaden verwendet das Hydrogen-Framework von Shopify als Beispiel. Sie können jedoch einen ähnlichen Ansatz verfolgen, wenn Ihre Marke Shopify für das Backend Ihres Shops mit einer "headless" Front-End-Einrichtung verwendet.  

Um Ihren Shopify Headless Shop mit Braze zu integrieren, müssen Sie diese beiden Ziele erreichen:

1. **Initialisieren und laden Sie das Braze Internet SDK, um das Tracking vor Ort zu ermöglichen.**<br><br> Fügen Sie manuell Code in Ihre Shopify Website ein, um das Braze Onsite Tracking zu aktivieren. Durch die Implementierung des Braze SDK in Ihrem Shopify Headless Store können Sie Aktivitäten vor Ort nachverfolgen, einschließlich Sitzungen, anonymes Kundenverhalten, Aktionen vor dem Checkout und alle [angepassten Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) oder [angepassten Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), die Sie zusammen mit Ihrem Entwicklungsteam einbeziehen möchten. Sie können auch alle Kanäle hinzufügen, die von den SDKs unterstützt werden, wie In-App-Nachrichten oder Content-Cards. 

{: start="2"}
2\. **Installieren Sie die Braze Shopify Integration**<br><br> Nachdem Sie Ihren Shopify-Shop mit Braze verbunden haben, erhalten Sie über Shopify-Webhooks Zugriff auf Kund:in-, Kassen-, Bestell- und Produktdaten.

{% alert important %}
Bevor Sie mit der Integration beginnen, vergewissern Sie sich, dass Sie die Checkout-Subdomain für Ihr Shopify Schaufenster korrekt eingerichtet haben. Weitere Informationen finden Sie unter [Migration vom Online Shop zu Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Wenn diese Einrichtung nicht korrekt vorgenommen wird, kann Braze keine Webhooks für Shopify-Kassen verarbeiten. Es ist auch nicht möglich, die Integration in einer lokalen Entwicklungsumgebung zu testen, da dies von einer gemeinsamen Domain zwischen Ihrem Schaufenster und der Kassenseite abhängt.
{% endalert %}

Um diese Ziele zu erreichen, gehen Sie folgendermaßen vor:

## Initialisieren und laden Sie das Braze Web SDK

### Schritt 1: Erstellen Sie eine Braze Website App {#step-1}

Gehen Sie in Braze zu **Einstellungen** > **App-Einstellungen** > und wählen Sie dann **App hinzufügen**. Benennen Sie die App als "Shopify".

{% alert warning %}
Der Shop muss "Shopify" heißen, sonst funktioniert die Integration möglicherweise nicht richtig.
{% endalert %}

### Schritt 2: Subdomain und Umgebungsvariablen hinzufügen {#step-2}

1. Richten Sie Ihre Shopify-Subdomain ein, um [den Traffic von Ihrem Shop auf Hydrogen umzuleiten](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic/).  
2. Fügen Sie einen [Callback URI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) für die Anmeldung hinzu. (Die URI wird automatisch hinzugefügt, wenn die Domain hinzugefügt wird.)
3. Richten Sie Ihre [Shopify Umgebungsvariablen](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable) ein:
  - Erstellen Sie zwei Umgebungsvariablen mit den Werten aus der Website App, die Sie in [Schritt 1](#step-1) erstellt haben.
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

### Schritt 3: Enablement von Tracking vor Ort

Der erste Schritt besteht darin, das Braze Web SDK zu initialisieren. Wir empfehlen, dazu unser NPM-Paket zu installieren:

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
Die Version des Braze Web SDK muss 5.4.0 sein.
{% endalert %}

[Nehmen Sie diese Einstellung]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) dann als Top-Level-Schlüssel in Ihre `vite.config.js` Datei auf:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Nach der Installation des NPM-Pakets müssen Sie das SDK in einem `useEffect` -Hook innerhalb der Komponente `Layout` initialisieren. Je nach Ihrer Hydrogen-Version kann sich diese Komponente entweder in der Datei `root.jsx` oder `layout.jsx` befinden:

```java
// Add these imports
import * as braze from "@braze/web-sdk";
import { useEffect } from 'react';

export function Layout({children}) {
  const nonce = useNonce();
  // @type {RootLoader} 
  const data = useRouteLoaderData('root');
  
  // Add useEffect call to initialize Braze SDK
  useEffect(() => {
    if(!braze.isInitialized()) {
      braze.initialize(data.brazeApiKey, {
        baseUrl: data.brazeApiUrl,
      });
      braze.openSession()    
    }
  }, [data]) 

  return (...);
}
```

Die Werte `data.brazeApiKey` und `data.brazeApiUrl` müssen mit Hilfe der in [Schritt 2](#step-2) erstellten Umgebungsvariablen in den Komponentenlader aufgenommen werden:

```java
export async function loader(args) {
  // Start fetching non-critical data without blocking time to first byte
  const deferredData = loadDeferredData(args);

  // Await the critical data required to render initial state of the page
  const criticalData = await loadCriticalData(args);

  const {storefront, env} = args.context;

  return {
    ...deferredData,
    ...criticalData,
    publicStoreDomain: env.PUBLIC_STORE_DOMAIN,
    // Add the two properties below to the returned value
    brazeApiKey: env.BRAZE_API_KEY,
    brazeApiUrl: env.BRAZE_API_URL,
    shop: getShopAnalytics({
      storefront,
      publicStorefrontId: env.PUBLIC_STOREFRONT_ID,
    }),
    consent: {
      checkoutDomain: env.PUBLIC_CHECKOUT_DOMAIN,
      storefrontAccessToken: env.PUBLIC_STOREFRONT_API_TOKEN,
      withPrivacyBanner: false,
      // Localize the privacy banner
      country: args.context.storefront.i18n.country,
      language: args.context.storefront.i18n.language,
    },
  };
}
```

{% alert note %}
Richtlinien zur Sicherheit von Inhalten (die sich normalerweise in der Datei `entry.server.jsx` Hydrogen befinden) können die Funktionalität von Braze-Skripten sowohl in lokalen als auch in Produktionsumgebungen beeinflussen. Wir empfehlen Ihnen, mit Vorschau-Builds, die über Oxygen an Shopify gesendet werden, oder angepassten Implementierungen zu testen. Wenn Sie Probleme haben, müssen Sie Ihr CSP so konfigurieren, dass unser JavaScript funktioniert.
{% endalert %}

### Schritt 4: Ein Shopify Konto Anmeldung Ereignis hinzufügen 

Tracking, wenn sich ein Käufer bei seinem Konto anmeldet und seine Nutzer:innen mit Braze synchronisiert. Dazu gehört der Aufruf unserer Methode `changeUser`, um Kund:in mit einer externen ID von Braze zu identifizieren. 

{% alert note %}
Wir haben derzeit keine Anleitung zur Unterstützung einer angepassten externen ID von Braze. Wenn Sie dies jetzt für Ihre Integration benötigen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

Bevor Sie beginnen, vergewissern Sie sich, dass Sie die Callback URIs für die Anmeldung der Kund:in so eingerichtet haben, dass sie in Hydrogen funktionieren. Weitere Informationen finden Sie unter [Verwendung der Kundenkonto-API mit Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Nachdem Sie die Callback URIs eingerichtet haben, definieren Sie eine Funktion für den Aufruf des Braze SDK. Erstellen Sie eine neue Datei (z.B. `Tracking.jsx`) und importieren Sie sie aus Ihren Komponenten:

```java
import * as braze from "@braze/web-sdk";

export function trackCustomerLogin(customerData, storefrontUrl) {
  const customerId = customerData.id.substring(customerData.id.lastIndexOf('/') + 1)
  const customerSessionKey = `ab.shopify.shopify_customer_${customerId}`;
  const alreadySetCustomerInfo = sessionStorage.getItem(customerSessionKey);
  
  if(!alreadySetCustomerInfo) {
    const user = braze.getUser()

    // To use Shopify customer ID as Braze External ID, use:
    // braze.changeUser(customerId)

    // To use Shopify customer email as Braze External ID, use:
      // braze.changeUser(customerData.emailAddress?.emailAddress)
        // To use hashing for email addresses, apply hashing before calling changeUser

    // To use your own custom ID as the Braze External ID, pass that value to the changeUser call.

    user.setFirstName(customerData.firstName);
    user.setLastName(customerData.lastName);
    if(customerData.emailAddress.emailAddress) {
      user.setEmail(customerData.emailAddress?.emailAddress);
    }

    if(customerData.phoneNumber?.phoneNumber) {
      user.setPhoneNumber(customerData.phoneNumber?.phoneNumber);
    }
    braze.logCustomEvent(
      "shopify_account_login",
      { source: storefrontUrl }
    )
    sessionStorage.setItem(customerSessionKey, customerId);
  }
}
```

{: start="2"}
2\. Fügen Sie in demselben `useEffect` -Hook, der das Braze SDK initialisiert, den Aufruf dieser Funktion hinzu:

```java
import { trackCustomerLogin } from './Tracking';

export function Layout({children}) {
  const nonce = useNonce();
  // @type {RootLoader}
  const data = useRouteLoaderData('root');

  useEffect(() => {
    if(!braze.isInitialized()) {
      braze.initialize(data.brazeApiKey, {
        baseUrl: data.brazeApiUrl,
        enableLogging: true,
      });
      braze.openSession()    
    }

    // Add call to trackCustomerLogin function
    data.isLoggedIn.then((isLoggedIn) => {
      if(isLoggedIn) {
        trackCustomerLogin(data.customerData, data.publicStoreDomain)
      }
    })

  }, [data])
```

{: start="3"}
3\. Holen Sie die E-Mail Adresse und Telefonnummer des Kunden in Ihrer Kunden API GraphQL Abfrage, die sich in der Datei `app/graphql/customer-account/CustomerDetailsQuery.js` befindet:

```java
export const CUSTOMER_FRAGMENT = `#graphql
  fragment Customer on Customer {
    id
    firstName
    lastName
    emailAddress {
      emailAddress
    }
    phoneNumber {
      phoneNumber
    }
    defaultAddress {
      ...Address
    }
    addresses(first: 6) {
      nodes {
        ...Address
      }
    }
  }
  fragment Address on CustomerAddress {
    id
    formatted
    firstName
    lastName
    company
    address1
    address2
    territoryCode
    zoneCode
    city
    zip
    phoneNumber
  }
`;
```

{: start="4"}
4\. Laden Sie schließlich die Kundendaten in Ihre Loader-Funktion:

```java
// Add import for GraphQL Query 
import { CUSTOMER_DETAILS_QUERY } from './graphql/customer-account/CustomerDetailsQuery';

export async function loader(args) {
  // Start fetching non-critical data without blocking time to first byte
  const deferredData = loadDeferredData(args);

  // Await the critical data required to render initial state of the page
  const criticalData = await loadCriticalData(args);

  const {storefront, env} = args.context;

  // Add GraphQL call to Customer API
  const isLoggedIn = await deferredData.isLoggedIn;
  let customerData;
  if (isLoggedIn) {
    const { data, errors } = await args.context.customerAccount.query(
        CUSTOMER_DETAILS_QUERY,
    );
    customerData = data.customer
  } else {
    customerData = {}
  }

  return {
    ...deferredData,
    ...criticalData,
    publicStoreDomain: env.PUBLIC_STORE_DOMAIN,
    brazeApiKey: env.BRAZE_API_KEY,
    brazeApiUrl: env.BRAZE_API_URL,
    // Add the property below to the returned value 
    customerData: customerData,
    shop: getShopAnalytics({
      storefront,
      publicStorefrontId: env.PUBLIC_STOREFRONT_ID,
    }),
    consent: {
      checkoutDomain: env.PUBLIC_CHECKOUT_DOMAIN,
      storefrontAccessToken: env.PUBLIC_STOREFRONT_API_TOKEN,
      withPrivacyBanner: false,
      // Localize the privacy banner
      country: args.context.storefront.i18n.country,
      language: args.context.storefront.i18n.language,
    },
  };
}
```

### Schritt 5: Tracking für die Ereignisse "Produkt angesehen" und "Warenkorb aktualisiert" hinzufügen

#### Produkt Gesehene Ereignisse

1. Fügen Sie diese Funktion in Ihre `Tracking.jsx` Datei ein:

```java
export function trackProductViewed(product, storefrontUrl) {
  const eventData = {
    product_id: product.id.substring(product.id.lastIndexOf('/') + 1),
    product_name: product.title,
    variant_id: product.selectedOrFirstAvailableVariant.id.substring(product.selectedOrFirstAvailableVariant.id.lastIndexOf('/') + 1),
    image_url: product.selectedOrFirstAvailableVariant.image?.url,
    product_url: `${storefrontUrl}/products/${product.handle}`,
    price: product.selectedOrFirstAvailableVariant.price.amount,
    currency: product.selectedOrFirstAvailableVariant.price.currencyCode,
    source: storefrontUrl,
    type: ["price_drop", "back_in_stock"],
    metadata: {
    sku: product.selectedOrFirstAvailableVariant.sku
  }

  }
  braze.logCustomEvent(
    "ecommerce.product_viewed",
    eventData 
  )
}
```

{: start="2"}
2\. Um die vorherige Funktion immer dann aufzurufen, wenn ein Nutzer:in eine Produktseite geht, fügen Sie der Komponente Produkt in der Datei `app/routes/products.$handle.jsx` einen `useEffect` -Hook hinzu:

```java
import { trackProductViewed } from '~/tracking';
import { useEffect } from 'react';

export default function Product() {
  // @type {LoaderReturnData} 
  // retrieve storefrontUrl to be passed into trackProductViewed 
  const {product, storefrontUrl} = useLoaderData();
  
  // Add useEffect hook for tracking product_viewed event 
  useEffect(() => {
    trackProductViewed(product, storefrontUrl)
  }, [])

  return (...)
}
```

{: start="3"}
3\. Fügen Sie den Wert für "storefrontUrl" hinzu (da er standardmäßig nicht im Komponentenlader enthalten ist):

```java
async function loadCriticalData({context, params, request}) {
  const {handle} = params;
  const {storefront} = context;

  if (!handle) {
    throw new Error('Expected product handle to be defined');
  }

  const [{product}] = await Promise.alll([
    storefront.query(PRODUCT_QUERY, {
      variables: {handle, selectedOptions: getSelectedProductOptions(request)},
    }),
    // Add other queries here, so that they are loaded in parallel
  ]);

  if (!product?.id) {
    throw new Response(null, {status: 404});
  }

  return {
    product,
   // Add this property to the returned value
    storefrontUrl: context.env.PUBLIC_STORE_DOMAIN,
  };
}
```

#### Warenkorb Aktualisierte Ereignisse

Zusätzlich zum Tracking des Ereignisses `cart_updated` müssen Sie den Wert des Tokens für den Warenkorb an Braze senden. Wir verwenden den Wert des Warenkorb-Tokens, um die von Shopify erhaltenen Webhooks für Bestellungen zu verarbeiten. Dazu erstellen Sie einen Nutzer-Alias mit dem Shopify Warenkorb-Token als Namen. 

1. Definieren Sie Funktionen für das Tracking des Ereignisses `cart_updated` und das Setzen des Warenkorb-Tokens:

```java
export function trackCartUpdated(cart, storefrontUrl) {
  const eventData = {
    cart_id: cart.id,
    total_value: cart.cost.totalAmount.amount,
    currency: cart.cost.totalAmount.currencyCode,

    products: cart.lines.nodes.map((line) => {
      return {
        product_id: line.merchandise.product.id.toString(),
        product_name: line.merchandise.product.title,
        variant_id: line.merchandise.id.toString(),
        image_url: line.merchandise.image.url,
        product_url: `${storefrontUrl}/products/${line.merchandise.product.handle}`,
        quantity: Number(line.quantity),
        price: Number(line.cost.totalAmount.amount / Number(line.quantity))
      }
    }),
    source: storefrontUrl,
    metadata: {},
  };
  
  braze.logCustomEvent(
    "ecommerce.cart_updated",
    eventData 
  )
}

export function setCartToken(cart) {
  const cartId = cart.id.substring(cart.id.lastIndexOf('/') + 1) 
  const cartToken = cartId.substring(0, cartId.indexOf("?key="));
  if (cartToken) {
    const cartSessionKey = `ab.shopify.shopify_cart_${cartToken}`;
    const alreadySetCartToken = sessionStorage.getItem(cartSessionKey);

    if (!alreadySetCartToken) {
      braze.getUser().addAlias("shopify_cart_token", `shopify_cart_${cartToken}`)
      braze.requestImmediateDataFlush();
      sessionStorage.setItem(cartSessionKey, cartToken);
    }
  }
}
```

{: start="2"}
2\. Geben Sie das Objekt `cart` von der Abrufaktion zurück, so dass Braze auf seine Eigenschaften zugreifen kann. Gehen Sie dazu in Ihre Datei `app/routes/cart.jsx` und fügen Sie Folgendes zur Datei `action`
Funktion:

```java
export async function action({request, context}) {
  const {cart} = context;

  ...

  switch (action) {
    case CartForm.ACTIONS.LinesAdd:
      result = await cart.addLines(inputs.lines);
      break;
    ... 
  }

  const cartId = result?.cart?.id;
  const headers = cartId ? cart.setCartId(result.cart.id) : new Headers();
  const {cart: cartResult, errors, warnings} = result;

  const redirectTo = formData.get('redirectTo') ?? null;
  if (typeof redirectTo === 'string') {
    status = 303;
    headers.set('Location', redirectTo);
  }
  
  return data(
    {
      cart: cartResult,
      // Add these two properties to the returned value 
      updatedCart: await cart.get(),
      storefrontUrl: context.env.PUBLIC_STORE_DOMAIN,
      errors,
      warnings,
      analytics: {
        cartId,
      },
    },
    {status, headers},
  );
}
```

Weitere Informationen zu Remix-Fetchern finden Sie unter [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3\. Hydrogen Shops definieren in der Regel eine `CartForm` Komponente, die den Zustand des Warenkorb-Objekts verwaltet, das beim Hinzufügen, Entfernen und Ändern der Menge von Artikeln im Warenkorb verwendet wird. Fügen Sie einen weiteren `useEffect` -Hook in die Komponente `AddToCartButton` ein, der die Funktion `trackCartUpdated` aufruft, sobald sich der Zustand des Formulars ändert (wenn der Nutzer:in-Warenkorb aktualisiert wird):

```java
// Add imports 
import { trackCartUpdated, setCartToken } from '~/tracking';
import { useEffect } from 'react';
import { useFetcher } from '@remix-run/react';

export function AddToCartButton({
  analytics,
  children,
  disabled,
  lines,
  onClick,
}) {
	
  // Define a new Fetcher to be used for tracking cart updates 
  const fetcher = useFetcher({ key: "cart-fetcher" });
  
  // Add useEffect hook for tracking cart_updated event and setting cart token alias
  useEffect(() => {
    if(fetcher.state === "idle" && fetcher.data) {
      trackCartUpdated(fetcher.data.updatedCart, fetcher.data.storefrontUrl)
      setCartToken(fetcher.data.updatedCart);
    }
  }, [fetcher.state, fetcher.data])

  // Add the fetcherKey prop to the CartForm component
  return (
    <CartForm route="/cart" inputs={{lines}} fetcherKey="cart-fetcher" action={CartForm.ACTIONS.LinesAdd}>
      {(fetcher) => (
        <>
          <input
            name="analytics"
            type="hidden"
            value={JSON.stringify(analytics)}
          />
          <button
            type="submit"
            onClick={onClick}
            disabled={disabled ?? fetcher.state !== 'idle'}
          >
            {children}
          </button>
        </>
      )}
    </CartForm>
  );
}
```

{: start="4"}
4\. Verwenden Sie dieselbe `fetcherKey` für die Aktionen, die für das Update eines bestehenden Produkts aus Ihrem Warenkorb verantwortlich sind. Fügen Sie Folgendes zu den Komponenten `CartLineRemoveButton` und `CartLineUpdateButton` hinzu (die sich standardmäßig in der Datei `app/components/CartLineItem.jsx` befinden):

```java
function CartLineRemoveButton({lineIds, disabled}) {
  // Add the fetcherKey prop to the CartForm component
  return (
    <CartForm
      fetcherKey="cart-fetcher"
      route="/cart"
      action={CartForm.ACTIONS.LinesRemove}
      inputs={{lineIds}}
    >
      <button disabled={disabled} type="submit">
        Remove
      </button>
    </CartForm>
  );
}

function CartLineUpdateButton({children, lines}) {
  // Add the fetcherKey prop to the CartForm component
  return (
    <CartForm
      route="/cart"
      fetcherKey="cart-fetcher"
      action={CartForm.ACTIONS.LinesUpdate}
      inputs={{lines}}
    >
      {children}
    </CartForm>
  );
}
```

## Installieren Sie die Braze Shopify Integration

### Schritt 1: Verbinden Sie Ihren Shopify Shop

Rufen Sie die Shopify Partnerseite auf, um Ihre Einrichtung zu starten. Wählen Sie zunächst **Einrichtung beginnen**, um die Braze Anwendung aus dem Shopify App Store zu installieren. Folgen Sie den geführten Schritten, um den Installationsvorgang abzuschließen.

![Einrichtungsseite für die Integration von Shopify auf dem Braze-Dashboard.]({% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %})

### Schritt 2: Enablement von Braze SDKs 

Für Shopify Hydrogen oder Headless Shops wählen Sie die Option **Angepasste Einrichtung**. 

Bevor Sie mit dem Onboarding fortfahren, vergewissern Sie sich, dass Sie das Braze SDK auf Ihrer Shopify Website aktiviert haben.

![Einrichtungsschritt zur Aktivierung der Braze SDKs.]({% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %})

### Schritt 3: Shopify-Daten verfolgen 

Verbessern Sie Ihre Integration, indem Sie weitere Shopify-Ereignisse und -Attribute hinzufügen, die von Shopify Webhooks unterstützt werden. Ausführliche Informationen zu den Daten, die durch diese Integration getrackt werden, finden Sie unter [Shopify Data Features]({{site.baseurl}}/shopify_data_features/). 

![Einrichtungsschritt zum Tracking von Shopify Daten.]({% image_buster /assets/img/Shopify/track_shopify_data_setup.png %})

### Schritt 4: Historische Verfüllung (optional)

Durch die angepasste Einrichtung haben Sie die Möglichkeit, Ihre Shopify Kunden und Bestellungen aus den letzten 90 Tagen zu laden, bevor Sie Ihre Shopify Integration anschließen. Wenn Sie diese ersten Daten laden möchten, aktivieren Sie das Kontrollkästchen für die Option zum Laden der ersten Daten.

Wenn Sie die Auffüllung lieber später vornehmen möchten, können Sie die Ersteinrichtung jetzt abschließen und zu einem späteren Zeitpunkt zu diesem Schritt zurückkehren.

![Abschnitt zum Einrichten des Backfill von historischen Daten.]({% image_buster /assets/img/Shopify/historical_backfill_setup.png %})

Diese Tabelle enthält die Daten, die anfänglich über das Backfill geladen werden sollen.

| Braze empfohlene Veranstaltungen | Shopify angepasste Events | Braze Standard Attribute | Braze Abo-Status |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Bestellung aufgegeben</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_provinz</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail</li><li>Vorname</li><li>Nachname</li><li>Telefon</li><li>Ort</li><li>Land</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail Marketing Abos, die mit diesem Shopify Shop verbunden sind</li><li>SMS-Marketing Abos, die mit diesem Shopify Shop verbunden sind</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Schritt 5: Angepasstes Tracking von Daten (Fortschritt) 

Mit den Braze SDKs können Sie angepasste Events oder angepasste Attribute verfolgen, die über die für diese Integration unterstützten Daten hinausgehen. Angepasste Events erfassen eindeutige Interaktionen in Ihrem Shop, wie zum Beispiel:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Angepasste Events</th>
      <th style="width: 50%;">Angepasste Attribute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Einen angepassten Rabattcode verwenden</li>
          <li>Mit personalisierter Produktempfehlung interagiert</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Bevorzugte Marken oder Produkte</li>
          <li>Bevorzugte Einkaufskategorien</li>
          <li>Zugehörigkeit oder Treuestatus</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Das SDK muss auf dem Gerät eines Nutzers initialisiert werden (auf Aktivitäten warten), um Events oder angepasste Attribute zu protokollieren. Um mehr über die Protokollierung angepasster Daten zu erfahren, lesen Sie [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) und [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Schritt 6: Konfigurieren Sie, wie Sie Nutzer:innen verwalten (optional)

Wählen Sie Ihren `external_id` Typ aus der Dropdown-Liste aus.

![Abschnitt "Abonnent:innen sammeln".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe ID von Braze kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit der Nutzer:innen zu berücksichtigen.<br><br>

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko der Ausbeutung:** Wenn ein böswilliger Nutzer:innen seinen Webbrowser so verändert, dass er die E-Mail-Adresse einer anderen Person als externe ID verwendet, kann er möglicherweise auf sensible Nachrichten oder Kontoinformationen zugreifen.
{% endalert %}

Wenn Sie einen angepassten externen ID-Typ ausgewählt haben, fahren Sie mit den Schritten 6.1 und 6.2 fort. Andernfalls fahren Sie mit Schritt 6.3 fort.

#### Schritt 6.1: Erstellen Sie eine angepasste `external_id`

Gehen Sie zunächst zu Shopify und erstellen Sie das Metafeld `braze.external_id`. Wir empfehlen Ihnen, die Schritte unter [Anpassen von Metafeldbeschreibungen](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions) zu befolgen. Geben Sie für **Namensraum und Schlüssel** `braze.external_id` ein. Für **Typ** empfehlen wir Ihnen, einen ID-Typ zu wählen.

Nachdem Sie das Metafelder erstellt haben, hören Sie auf [`customer/create` Webhooks](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks), damit Sie das Metafelder schreiben können, wenn eine neue Kund:in erstellt wird. Verwenden Sie dann die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um alle Ihre zuvor erstellten Kund:in mit diesem Metafeld zu versehen.

#### Schritt 6.2: Einen Endpunkt erstellen

Sie benötigen einen öffentlichen GET-Endpunkt, um Ihre externe ID abzurufen. Wenn Shopify das Metafeld nicht bereitstellen kann, ruft Braze diesen Endpunkt auf, um die externe ID abzurufen.

Ein Beispiel für einen Endpunkt ist: `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

##### Antwort

Braze erwartet einen 200 Status Code. Jeder andere Code wird als Fehler des Endpunkts betrachtet. Die Antwort sollte lauten:

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Passen Sie die `shopify_customer_id` und die E-Mail Adresse mit Hilfe der Admin API oder der Customer API an, um sicherzustellen, dass die Parameterwerte mit den Kunden:in in Shopify übereinstimmen. Nach der Validierung können Sie auch die APIs verwenden, um das Metafeld `braze.external_id` abzurufen und den Wert der externen ID zurückzugeben.

#### Schritt 6.3: Sammeln Sie Ihre E-Mail- oder SMS-Opt-ins von Shopify (optional)

Sie haben die Möglichkeit, Ihre Opt-ins für E-Mail- oder SMS-Marketing in Shopify zu sammeln. 

Wenn Sie die Kanäle E-Mail oder SMS nutzen, können Sie Ihre Opt-in-Status für E-Mail- und SMS-Marketing mit Braze synchronisieren. Wenn Sie Opt-ins für das E-Mail Marketing von Shopify synchronisieren, erstellt Braze automatisch eine Abo-Gruppe für alle Nutzer:innen, die mit diesem Shop verbunden sind. Sie müssen einen eindeutigen Namen für diese Abo-Gruppe erstellen.

![Abschnitt "Abonnent:innen sammeln" mit der Option, Opt-ins für E-Mail- oder SMS-Marketing zu sammeln.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Wie in der [Übersicht von Shopify]({{site.baseurl}}/shopify_overview/) erwähnt, müssen Ihre Entwickler:in den Code für das Braze SDK integrieren, wenn Sie ein Erfassungsformular eines Drittanbieters verwenden möchten. Auf diese Weise können Sie die E-Mail Adresse und den Status des globalen E-Mail Abos von Formularen erfassen. Genauer gesagt, müssen Sie diese Methoden in Ihre `theme.liquid` Datei implementieren und testen:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Legt die E-Mail Adresse im Nutzerprofil fest
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Aktualisiert den Status des globalen E-Mail-Abos
{% endalert %}

### Schritt 7: Produkte synchronisieren (optional)

Sie können alle Produkte aus Ihrem Shopify Shop mit einem Braze Katalog synchronisieren, um die Personalisierung von Nachrichten zu vertiefen. Automatische Updates erfolgen nahezu in Realtime, so dass Ihr Katalog immer die neuesten Produktdaten enthält. Wenn Sie mehr darüber erfahren möchten, lesen Sie [Shopify Produkt-Synchronisation]({{site.baseurl}}/shopify_catalogs/).

![Einrichtungsschritt zur Synchronisierung von Produktdaten mit Braze.]({% image_buster /assets/img/Shopify/sync_product_data.png %})

### Schritt 8: Kanäle aktivieren

Um In-App-Nachrichten, Content-Cards und Feature-Flags über die Shopify Direktintegration zu aktivieren, fügen Sie jeden Kanal zu Ihrem SDK hinzu. Folgen Sie den unten stehenden Links zur Dokumentation der einzelnen Kanäle:

- **In-App-Nachrichten:** Für das Enablement von In-App-Nachrichten für Lead Capture-Formular-Anwendungsfälle siehe [In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/).
- **Content-Cards:** Um Content-Cards für Posteingang oder Website-Banner zu aktivieren, referenzieren Sie [Content-Cards]({{site.baseurl}}/developer_guide/content_cards/).
- **Feature-Flags:** Zum Enablement von Feature-Flags für Anwendungsfälle von Site-Experimenten referenzieren Sie auf [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/).

### Schritt 9: Einrichtung abschließen

Nachdem Sie alle Schritte durchlaufen haben, wählen Sie **Einrichtung beenden**, um zur Partnerseite zurückzukehren. Aktivieren Sie dann die Einbettung der Braze App auf Ihrer Shopify-Administrationsseite, wie durch das eingeblendete Banner angezeigt wird.

![Banner, das Sie auffordert, die Einbettung der Braze App in Shopify zu aktivieren, damit Sie Ihre Integration fertigstellen können.]({% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %})

#### Beispiel-Code

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) ist eine beispielhafte Hydrogen App, die den gesamten Code enthält, der in den vorherigen Schritten behandelt wurde. 

