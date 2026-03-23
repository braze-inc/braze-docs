---
nav_title: Shopify Angepasste Integration einrichten
article_title: "Shopify Angepasste Integration einrichten"
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Verbindung zu einem Shopify Hydrogen Shop oder einem beliebigen Headless-Shopify-Shop herstellen, indem Sie eine angepasste Storefront verwenden."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Shopify angepasste Integration einrichten

> Auf dieser Seite erfahren Sie, wie Sie Braze mit einem Shopify Hydrogen Shop oder einem beliebigen Headless-Shopify-Shop integrieren können, indem Sie eine angepasste Storefront verwenden.

Dieser Leitfaden verwendet das Hydrogen-Framework von Shopify als Beispiel. Sie können jedoch einen ähnlichen Ansatz verfolgen, wenn Ihre Marke Shopify für das Backend Ihres Shops mit einem „Headless"-Front-End-Setup verwendet.  

Um Ihren Shopify Headless Shop mit Braze zu integrieren, müssen Sie diese beiden Ziele erreichen:

1. **Initialisieren und laden Sie das Braze Web SDK, um das Onsite-Tracking zu ermöglichen**<br><br> Fügen Sie manuell Code in Ihre Shopify-Website ein, um das Braze Onsite-Tracking zu aktivieren. Durch die Implementierung des Braze SDK in Ihrem Shopify Headless Shop können Sie Onsite-Aktivitäten nachverfolgen, einschließlich Sitzungen, anonymes Nutzerverhalten, Aktionen vor dem Checkout und alle [angepassten Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) oder [angepassten Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), die Sie zusammen mit Ihrem Entwicklungsteam einbeziehen möchten. Sie können auch alle Kanäle hinzufügen, die von den SDKs unterstützt werden, wie In-App-Nachrichten oder Content Cards. 

{: start="2"}
2. **Installieren Sie die Braze Shopify-Integration**<br><br> Nachdem Sie Ihren Shopify-Shop mit Braze verbunden haben, erhalten Sie über Shopify-Webhooks Zugriff auf Kundendaten, Checkout-, Bestell- und Produktdaten.

{% alert important %}
Bevor Sie mit der Integration beginnen, vergewissern Sie sich, dass Sie die Checkout-Subdomain für Ihre Shopify-Storefront korrekt eingerichtet haben. Weitere Informationen finden Sie unter [Migration vom Online-Shop zu Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Wenn diese Einrichtung nicht korrekt vorgenommen wird, kann Braze keine Shopify-Checkout-Webhooks verarbeiten. Es ist auch nicht möglich, die Integration in einer lokalen Entwicklungsumgebung zu testen, da dies von einer gemeinsamen Domain zwischen Ihrer Storefront und der Checkout-Seite abhängt.
{% endalert %}

Um diese Ziele zu erreichen, gehen Sie folgendermaßen vor:

## Initialisieren und laden Sie das Braze Web SDK

### 1. Schritt: Erstellen Sie eine Braze-Website-App {#step-1}

Gehen Sie in Braze zu **Einstellungen** > **App-Einstellungen** und wählen Sie dann **App hinzufügen**. Geben Sie „Shopify" als App-Namen ein.

{% alert warning %}
Der Shop muss „Shopify" heißen, sonst funktioniert die Integration möglicherweise nicht richtig.
{% endalert %}

### 2. Schritt: Subdomain und Umgebungsvariablen hinzufügen {#step-2}

1. Richten Sie Ihre Shopify-Subdomain ein, um [den Traffic von Ihrem Online-Shop auf Hydrogen umzuleiten](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic).  
2. Fügen Sie einen [Callback-URI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) für die Anmeldung hinzu. (Der URI wird automatisch hinzugefügt, wenn die Domain hinzugefügt wird.)
3. Richten Sie Ihre [Shopify-Umgebungsvariablen](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable) ein:
  - Erstellen Sie zwei Umgebungsvariablen mit den Werten aus der Website-App, die Sie in [Schritt 1](#step-1) erstellt haben.
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

### 3. Schritt: Onsite-Tracking aktivieren

Der erste Schritt besteht darin, das Braze Web SDK zu initialisieren. Wir empfehlen, dazu unser NPM-Paket zu installieren:

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
Die Version des Braze Web SDK muss 5.4.0 sein.
{% endalert %}

[Nehmen Sie dann diese Einstellung]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) als Top-Level-Schlüssel in Ihre `vite.config.js`-Datei auf:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Nach der Installation des NPM-Pakets müssen Sie das SDK in einem `useEffect`-Hook innerhalb der `Layout`-Komponente initialisieren. Je nach Ihrer Hydrogen-Version kann sich diese Komponente entweder in der Datei `root.jsx` oder `layout.jsx` befinden:

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

Die Werte `data.brazeApiKey` und `data.brazeApiUrl` müssen mithilfe der in [Schritt 2](#step-2) erstellten Umgebungsvariablen in den Komponentenlader aufgenommen werden:

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
Content-Security-Policies (die sich normalerweise in der Hydrogen-Datei `entry.server.jsx` befinden) können die Funktionalität von Braze-Skripten sowohl in lokalen als auch in Produktionsumgebungen beeinflussen. Wir empfehlen, mit Vorschau-Builds zu testen, die über Oxygen an Shopify gesendet werden, oder mit angepassten Deployments. Wenn Sie auf Probleme stoßen, müssen Sie Ihre CSP so konfigurieren, dass unser JavaScript funktioniert.
{% endalert %}

### 4. Schritt: Ein Shopify-Konto-Anmelde-Event hinzufügen 

Verfolgen Sie, wann sich Käufer:innen bei ihrem Konto anmelden, und synchronisieren Sie ihre Nutzerinformationen mit Braze. Dazu gehört der Aufruf unserer `changeUser`-Methode, um Kund:innen mit einer externen Braze-ID zu identifizieren. 

{% alert note %}
Wir haben derzeit keine Anleitung zur Unterstützung einer angepassten externen Braze-ID. Wenn Sie dies jetzt für Ihre Integration benötigen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

Bevor Sie beginnen, vergewissern Sie sich, dass Sie die Callback-URIs für die Kundenanmeldung so eingerichtet haben, dass sie in Hydrogen funktionieren. Weitere Informationen finden Sie unter [Verwendung der Customer Account API mit Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Nachdem Sie die Callback-URIs eingerichtet haben, definieren Sie eine Funktion für den Aufruf des Braze SDK. Erstellen Sie eine neue Datei (z. B. `Tracking.jsx`) und importieren Sie sie aus Ihren Komponenten:

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
2. Fügen Sie in demselben `useEffect`-Hook, der das Braze SDK initialisiert, den Aufruf dieser Funktion hinzu:

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
3. Rufen Sie die E-Mail-Adresse und Telefonnummer der Kund:innen in Ihrer Customer-API-GraphQL-Abfrage ab, die sich in der Datei `app/graphql/customer-account/CustomerDetailsQuery.js` befindet:

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
4. Laden Sie abschließend die Kundendaten in Ihrer Loader-Funktion:

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

### 5. Schritt: Tracking für die Events „Produkt angesehen" und „Warenkorb aktualisiert" hinzufügen

#### Events „Produkt angesehen"

1. Fügen Sie diese Funktion in Ihre `Tracking.jsx`-Datei ein:

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
2. Um die vorherige Funktion immer dann aufzurufen, wenn Nutzer:innen eine Produktseite besuchen, fügen Sie der Product-Komponente in der Datei `app/routes/products.$handle.jsx` einen `useEffect`-Hook hinzu:

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
3. Fügen Sie den Wert für „storefrontUrl" hinzu (da er standardmäßig nicht im Komponentenlader enthalten ist):

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

#### Events „Warenkorb aktualisiert"

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

1. Definieren Sie Funktionen für das Tracking des `cart_updated`-Events und das Setzen des Warenkorb-Tokens:

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
2. Geben Sie das `cart`-Objekt von der Fetcher-Aktion zurück, damit Braze auf seine Eigenschaften zugreifen kann. Gehen Sie dazu in Ihre Datei `app/routes/cart.jsx` und fügen Sie Folgendes zur `action`-Funktion hinzu:

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
3. Hydrogen-Shops definieren in der Regel eine `CartForm`-Komponente, die den Zustand des Warenkorb-Objekts verwaltet. Diese wird beim Hinzufügen, Entfernen und Ändern der Menge von Artikeln im Warenkorb verwendet. Fügen Sie einen weiteren `useEffect`-Hook in die `AddToCartButton`-Komponente ein, der die Funktion `trackCartUpdated` aufruft, sobald sich der Zustand des Formular-Fetchers ändert (d. h. wenn der Warenkorb aktualisiert wird):

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
4. Verwenden Sie denselben `fetcherKey` für die Aktionen, die für das Update eines bestehenden Produkts in Ihrem Warenkorb verantwortlich sind. Fügen Sie Folgendes zu den Komponenten `CartLineRemoveButton` und `CartLineUpdateButton` hinzu (die sich standardmäßig in der Datei `app/components/CartLineItem.jsx` befinden):

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

## Installieren Sie die Braze Shopify-Integration

### 1. Schritt: Verbinden Sie Ihren Shopify-Shop

Rufen Sie die Shopify-Partnerseite auf, um Ihre Einrichtung zu starten. Wählen Sie zunächst **Einrichtung beginnen**, um die Braze-Anwendung aus dem Shopify App Store zu installieren. Folgen Sie den geführten Schritten, um den Installationsvorgang abzuschließen.

![Einrichtungsseite für die Shopify-Integration im Braze-Dashboard.]({% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %})

### 2. Schritt: Braze SDKs aktivieren 

Für Shopify Hydrogen oder Headless-Shops wählen Sie die Option **Angepasste Einrichtung**. 

Bevor Sie mit dem Onboarding-Prozess fortfahren, vergewissern Sie sich, dass Sie das Braze SDK auf Ihrer Shopify-Website aktiviert haben.

![Einrichtungsschritt zur Aktivierung der Braze SDKs.]({% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %})

### 3. Schritt: Shopify-Daten tracken 

Verbessern Sie Ihre Integration, indem Sie weitere Shopify-Events und -Attribute hinzufügen, die von Shopify-Webhooks unterstützt werden. Ausführliche Informationen zu den Daten, die durch diese Integration getrackt werden, finden Sie unter [Shopify-Daten-Features]({{site.baseurl}}/shopify_data_features/). 

![Einrichtungsschritt zum Tracking von Shopify-Daten.]({% image_buster /assets/img/Shopify/track_shopify_data_setup.png %})

### 4. Schritt: Historisches Backfill (optional)

Durch die angepasste Einrichtung haben Sie die Möglichkeit, Ihre Shopify-Kund:innen und -Bestellungen aus den letzten 90 Tagen zu laden, bevor Sie Ihre Shopify-Integration verbinden. Um diesen initialen Datenladevorgang einzubeziehen, aktivieren Sie das Kontrollkästchen für die Option zum initialen Datenladen.

Wenn Sie das Backfill lieber später durchführen möchten, können Sie die Ersteinrichtung jetzt abschließen und zu einem späteren Zeitpunkt zu diesem Schritt zurückkehren.

![Abschnitt zum Einrichten des historischen Daten-Backfills.]({% image_buster /assets/img/Shopify/historical_backfill_setup.png %})

Diese Tabelle enthält die Daten, die initial über das Backfill geladen werden.

| Von Braze empfohlene Events | Angepasste Shopify-Events | Braze-Standardattribute | Braze-Abo-Status |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Bestellung aufgegeben</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail</li><li>Vorname</li><li>Nachname</li><li>Telefon</li><li>Ort</li><li>Land</li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail-Marketing-Abos, die mit diesem Shopify-Shop verknüpft sind</li><li>SMS-Marketing-Abos, die mit diesem Shopify-Shop verknüpft sind</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### 5. Schritt: Angepasstes Daten-Tracking einrichten (erweitert) 

Mit den Braze SDKs können Sie angepasste Events oder angepasste Attribute tracken, die über die für diese Integration unterstützten Daten hinausgehen. Angepasste Events erfassen eindeutige Interaktionen in Ihrem Shop, wie zum Beispiel:

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
          <li>Mit einer personalisierten Produktempfehlung interagieren</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Bevorzugte Marken oder Produkte</li>
          <li>Bevorzugte Einkaufskategorien</li>
          <li>Mitgliedschafts- oder Treuestatus</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Das SDK muss auf dem Gerät der Nutzer:innen initialisiert sein (auf Aktivitäten lauschen), um Events oder angepasste Attribute zu protokollieren. Weitere Informationen zur Protokollierung angepasster Daten finden Sie unter [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) und [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### 6. Schritt: Konfigurieren Sie, wie Sie Nutzer:innen verwalten (optional) {#step-6}

Wählen Sie Ihren `external_id`-Typ aus der Dropdown-Liste aus.

![Abschnitt „Abonnent:innen sammeln".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe Braze-ID kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit zu berücksichtigen.<br><br>

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten, was sie anfällig für Angriffe macht.
- **Risiko des Missbrauchs:** Wenn böswillige Nutzer:innen ihren Webbrowser so manipulieren, dass die E-Mail-Adresse einer anderen Person als externe ID gesendet wird, könnten sie möglicherweise auf sensible Nachrichten oder Kontoinformationen zugreifen.
{% endalert %}

Standardmäßig wandelt Braze E-Mails von Shopify automatisch in Kleinbuchstaben um, bevor sie als externe ID verwendet werden. Wenn Sie E-Mail oder gehashte E-Mail als externe ID verwenden, vergewissern Sie sich, dass Ihre E-Mail-Adressen ebenfalls in Kleinbuchstaben umgewandelt werden, bevor Sie sie als externe ID zuweisen oder bevor Sie sie aus anderen Datenquellen hashen. Dies hilft, Diskrepanzen bei externen IDs zu vermeiden und die Erstellung doppelter Nutzerprofile in Braze zu verhindern.

{% alert note %}
Die nächsten Schritte hängen von Ihrer Auswahl der externen ID ab:<br><br>
- **Wenn Sie einen angepassten externen ID-Typ ausgewählt haben:** Führen Sie die Schritte 6.1–6.3 aus, um Ihre angepasste externe ID-Konfiguration einzurichten.
- **Wenn Sie Shopify-Kunden-ID, E-Mail oder gehashte E-Mail ausgewählt haben:** Überspringen Sie die Schritte 6.1–6.3 und fahren Sie direkt mit Schritt 6.4 fort.
{% endalert %}

#### Schritt 6.1: Das Metafeld `braze.external_id` erstellen

1. Gehen Sie in Ihrem Shopify-Admin-Panel zu **Einstellungen** > **Metafelder**.
2. Wählen Sie **Kunden** > **Definition hinzufügen**.
3. Geben Sie für **Namespace und Schlüssel** den Wert `braze.external_id` ein.
4. Wählen Sie unter **Typ** den **ID-Typ** aus.

Nachdem das Metafeld erstellt wurde, befüllen Sie es für Ihre Kund:innen. Wir empfehlen die folgenden Ansätze:

- **Auf Webhooks zur Kundenerstellung lauschen:** Richten Sie einen Webhook ein, um auf [`customer/create`-Events](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) zu lauschen. So können Sie das Metafeld schreiben, wenn neue Kund:innen angelegt werden.
- **Bestehende Kund:innen nachträglich befüllen:** Verwenden Sie die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um das Metafeld für zuvor erstellte Kund:innen zu befüllen.

#### Schritt 6.2: Einen Endpunkt zum Abrufen Ihrer externen ID erstellen

Sie müssen einen öffentlichen Endpunkt erstellen, den Braze zum Abrufen der externen ID aufrufen kann. Dadurch kann Braze die ID in Szenarien abrufen, in denen Shopify das Metafeld `braze.external_id` nicht direkt bereitstellen kann.

##### Endpunkt-Spezifikationen

**Methode:** GET

Braze sendet die folgenden Parameter an Ihren Endpunkt:

| Parameter            | Erforderlich | Datentyp | Beschreibung                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Ja      | String    | Die Shopify-Kunden-ID.                                         |
| shopify_storefront   | Ja      | String    | Der Storefront-Name für die Anfrage. Beispiel: `<storefront_name>.myshopify.com` |
| email_address        | Nein       | String    | Die E-Mail-Adresse der angemeldeten Nutzer:innen. <br><br>Dieses Feld kann in bestimmten Webhook-Szenarien fehlen. Ihre Endpunkt-Logik sollte hier Null-Werte berücksichtigen (z. B. die E-Mail über die shopify_customer_id abrufen, wenn Ihre interne Logik dies erfordert). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Beispiel-Endpunkt

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```


##### Erwartete Antwort
Braze erwartet einen `200`-Statuscode, der die externe ID als JSON zurückgibt:
```json
{
  "external_id": "my_external_id"
}
```

##### Validierung

Es ist entscheidend, dass `shopify_customer_id` und `email_address` (falls vorhanden) mit den Kundenwerten in Shopify übereinstimmen. Sie können die [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) verwenden, um diese Parameter zu validieren und das korrekte `braze.external_id`-Metafeld abzurufen.

##### Fehlerverhalten und Zusammenführung
Jeder andere Statuscode als `200` wird als Fehler betrachtet.

- **Auswirkungen auf die Zusammenführung:** Wenn der Endpunkt fehlschlägt (nicht `200` zurückgibt oder ein Timeout auftritt), kann Braze die externe ID nicht abrufen. Folglich wird die Zusammenführung zwischen dem Shopify-Nutzer und dem Braze-Nutzerprofil zu diesem Zeitpunkt nicht stattfinden.
- **Wiederholungslogik:** Braze kann standardmäßige sofortige Netzwerk-Wiederholungsversuche unternehmen. Wenn der Fehler jedoch weiterhin besteht, wird die Zusammenführung bis zum nächsten qualifizierenden Event aufgeschoben (z. B. wenn Nutzer:innen ihr Profil aktualisieren oder einen Checkout abschließen).
- **Unterstützbarkeit:** Um eine zeitnahe Zusammenführung von Nutzer:innen zu gewährleisten, stellen Sie sicher, dass Ihr Endpunkt hochverfügbar ist und das optionale Feld `email_address` zuverlässig verarbeitet.

#### Schritt 6.3: Ihre externe ID eingeben

Wiederholen Sie [Schritt 6](#step-6) und geben Sie Ihre Endpunkt-URL ein, nachdem Sie die angepasste externe ID als Ihren externen Braze-ID-Typ ausgewählt haben.

##### Hinweise

- Wenn Ihre externe ID zum Zeitpunkt der Braze-Anfrage an Ihren Endpunkt noch nicht generiert wurde, verwendet die Integration standardmäßig die Shopify-Kunden-ID, wenn die Funktion `changeUser` aufgerufen wird. Dieser Schritt ist entscheidend für die Zusammenführung des anonymen Nutzerprofils mit dem identifizierten Nutzerprofil. Daher kann es vorübergehend vorkommen, dass verschiedene Arten von externen IDs in Ihrem Workspace existieren.
- Wenn die externe ID im Metafeld `braze.external_id` verfügbar ist, wird die Integration diese externe ID priorisieren und zuweisen. 
    - Wenn die Shopify-Kunden-ID zuvor als externe Braze-ID festgelegt wurde, wird sie durch den Wert des Metafelds `braze.external_id` ersetzt. 

#### Schritt 6.4: Ihre E-Mail- oder SMS-Opt-ins von Shopify sammeln (optional)

Sie haben die Möglichkeit, Ihre E-Mail- oder SMS-Marketing-Opt-ins von Shopify zu sammeln. 

Wenn Sie die E-Mail- oder SMS-Kanäle nutzen, können Sie Ihre E-Mail- und SMS-Marketing-Opt-in-Status mit Braze synchronisieren. Wenn Sie E-Mail-Marketing-Opt-ins von Shopify synchronisieren, erstellt Braze automatisch eine E-Mail-Abo-Gruppe für alle Nutzer:innen, die mit diesem Shop verknüpft sind. Sie müssen einen eindeutigen Namen für diese Abo-Gruppe erstellen.

![Abschnitt „Abonnent:innen sammeln" mit der Option, E-Mail- oder SMS-Marketing-Opt-ins zu sammeln.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Wie in der [Shopify-Übersicht]({{site.baseurl}}/shopify_overview/) erwähnt, müssen Ihre Entwickler:innen den Braze-SDK-Code integrieren, wenn Sie ein Erfassungsformular eines Drittanbieters verwenden möchten. So können Sie die E-Mail-Adresse und den globalen E-Mail-Abo-Status aus Formularübermittlungen erfassen. Konkret müssen Sie diese Methoden in Ihrer `theme.liquid`-Datei implementieren und testen:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Legt die E-Mail-Adresse im Nutzerprofil fest
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Aktualisiert den globalen E-Mail-Abo-Status
{% endalert %}

### 7. Schritt: Produkte synchronisieren (optional)

Sie können alle Produkte aus Ihrem Shopify-Shop mit einem Braze-Katalog synchronisieren, um die Personalisierung von Nachrichten zu vertiefen. Automatische Updates erfolgen nahezu in Realtime, sodass Ihr Katalog immer die neuesten Produktdetails enthält. Weitere Informationen finden Sie unter [Shopify-Produktsynchronisation]({{site.baseurl}}/shopify_catalogs/).

![Einrichtungsschritt zur Synchronisierung von Produktdaten mit Braze.]({% image_buster /assets/img/Shopify/sync_product_data.png %})

### 8. Schritt: Kanäle aktivieren

Um In-App-Nachrichten, Content Cards und Feature-Flags über die direkte Shopify-Integration zu aktivieren, fügen Sie jeden Kanal zu Ihrem SDK hinzu. Folgen Sie den unten stehenden Dokumentationslinks für jeden Kanal:

- **In-App-Nachrichten:** Informationen zur Aktivierung von In-App-Nachrichten für Lead-Capture-Formular-Anwendungsfälle finden Sie unter [In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/).
- **Content Cards:** Informationen zur Aktivierung von Content Cards für Posteingangs- oder Website-Banner-Anwendungsfälle finden Sie unter [Content Cards]({{site.baseurl}}/developer_guide/content_cards/).
- **Feature-Flags:** Informationen zur Aktivierung von Feature-Flags für Website-Experimentier-Anwendungsfälle finden Sie unter [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/).

### 9. Schritt: Einrichtung abschließen

Nachdem Sie alle Schritte durchlaufen haben, wählen Sie **Einrichtung beenden**, um zur Partnerseite zurückzukehren. Aktivieren Sie dann die Braze-App-Einbettung auf Ihrer Shopify-Admin-Seite, wie durch das angezeigte Banner angezeigt.

![Banner, das Sie auffordert, die Braze-App-Einbettung in Shopify zu aktivieren, damit Sie die Einrichtung Ihrer Integration abschließen können.]({% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %})

#### Beispiel-Code

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) ist eine beispielhafte Hydrogen-App, die den gesamten Code enthält, der in den vorherigen Schritten behandelt wurde.