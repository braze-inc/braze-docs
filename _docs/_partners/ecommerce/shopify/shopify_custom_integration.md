---
nav_title: Shopify Custom Integration Setup
article_title: "Shopify Custom Integration Setup"
description: "This reference article covers how to connect with a Shopify Hydrogen store or any headless Shopify store by using a custom storefront."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Shopify custom integration setup

> This page walks you through how to integrate Braze with a Shopify Hydrogen store or any headless Shopify store by using a custom storefront.

This guide uses Shopify’s Hydrogen framework as an example. However, you can follow a similar approach if your brand uses Shopify for the backend of your store with a "headless" front-end setup.  

To integrate your Shopify headless store with Braze, you need to complete these two goals:

1. **Initialize and load the Braze Web SDK to enable onsite tracking**<br><br> Manually add code into your Shopify website to enable Braze onsite tracking. By implementing the Braze SDK on your Shopify headless store, you can track onsite activities, including sessions, anonymous user behavior, pre-checkout shopper actions, and any [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) or [custom attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) you choose to include with your development team. You can also add any channels supported by the SDKs, such as in-app messages or Content Cards. 

{: start="2"}
2. **Install the Braze Shopify integration**<br><br> After you connect your Shopify store to Braze, you'll gain access to customer, checkout, order, and product data through Shopify webhooks.

{% alert important %}
Before starting your integration, confirm you have correctly set up the checkout subdomain for your Shopify storefront. For more information, refer to [Migrate from the online store to Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> If this setup isn't done correctly, Braze can't process Shopify checkout webhooks. It also won't be possible to test the integration in a local development environment, because that relies on a shared domain between your storefront and the checkout page.
{% endalert %}

To complete these goals, follow these steps:

## Initialize and load the Braze Web SDK

### Step 1: Create a Braze website app {#step-1}

In Braze, go to **Settings** > **App Settings** > and then select **Add App**. Name the app as "Shopify".

{% alert warning %}
The shop must be named “Shopify” or the integration may not work properly.
{% endalert %}

### Step 2: Add subdomain and environmental variables {#step-2}

1. Set up your Shopify subdomain to [redirect traffic from your online store to Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic).  
2. Add a [callback URI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) for login. (The URI will automatically be added when the domain is added.)
3. Set up your [Shopify environment variables](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable):
  - Create two environment variables using the values from the website app you created in [Step 1](#step-1).
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

### Step 3: Enable onsite tracking

The first step is to initialize the Braze Web SDK. We recommend doing that by installing our NPM package:

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
The Braze Web SDK version must be 5.4.0.
{% endalert %}

Then, [include this setting]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) as a top-level key in your `vite.config.js` file:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

After installing the NPM package, you must initialize the SDK within a `useEffect` hook inside the `Layout` component. Depending on your Hydrogen version, this component may be located in either the `root.jsx` or `layout.jsx` file:

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

The values `data.brazeApiKey` and `data.brazeApiUrl` need to be included in the component loader using the environment variables created in [Step 2](#step-2):

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
Content security policies (usually located in the `entry.server.jsx` Hydrogen file) can impact the functionality of Braze scripts both in local and production environments. We suggest testing through preview builds sent to Shopify through Oxygen or custom deployments. If you encounter issues, you’ll need to configure your CSP to allow our JavaScript to function.
{% endalert %}

### Step 4: Add a Shopify Account Login event 

Track when a shopper signs into their account and syncs their user information to Braze. This includes calling our `changeUser` method to identify customers with a Braze external ID. 

{% alert note %}
We currently don't have guidance to support a custom Braze external ID. If you require this for your integration now, contact your customer success manager.
{% endalert %}

Before you start, make sure you've set up the callback URIs for the customer login to work within Hydrogen. For more information, refer to [Using the Customer Account API with Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. After setting up the callback URIs, define a function for calling the Braze SDK. Create a new file (such as `Tracking.jsx`) and import it from your components:

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
2. In the same `useEffect` hook that initializes the Braze SDK, add the call to this function:

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
3. Fetch the customer email address and phone number in your Customer API GraphQL query, located in the file `app/graphql/customer-account/CustomerDetailsQuery.js`:

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
4. Finally, load the customer data in your loader function:

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

### Step 5: Add tracking for Product Viewed and Cart Updated events

#### Product Viewed events

1. Add this function to your `Tracking.jsx` file:

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
2. To call the prior function whenever a user visits a product page, add a `useEffect` hook to the Product component within the file `app/routes/products.$handle.jsx`:

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
3. Add the value for “storefrontUrl” (because it's not in the component loader by default):

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

#### Cart Updated events

In addition to tracking the `cart_updated` event, you need to send the cart token value over to Braze. We use the cart token value to process order webhooks received from Shopify. This is done by creating a user alias with the Shopify cart token as its name. 

1. Define functions for tracking the `cart_updated` event and setting the cart token:

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
2. Return the `cart` object from the fetcher action so Braze can access its properties by going to your `app/routes/cart.jsx` file an adding the following to the `action`
function:

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

For more information on Remix fetchers, refer to [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3. Hydrogen stores usually define a `CartForm` component that manages the cart object state, which gets used when adding, removing, and changing quantity of items in a cart. Add another `useEffect` hook in the `AddToCartButton` component that will call the `trackCartUpdated` function whenever the form fetcher state changes (whenever the user cart is updated):

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
4. Use the same `fetcherKey` for the actions responsible for updating an existing product from your cart. Add the following to the `CartLineRemoveButton` and `CartLineUpdateButton` components (located by default in the file `app/components/CartLineItem.jsx`):

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

## Install the Braze Shopify integration

### Step 1: Connect your Shopify store

Go to the Shopify partner page to start your setup. First, select **Begin Setup** to install the Braze application from the Shopify App Store. Follow the guided steps to complete the installation process.

![Shopify integration setup page on the Braze dashboard.]({% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %})

### Step 2: Enable Braze SDKs 

For Shopify Hydrogen or headless stores, select the **Custom setup** option. 

Before continuing with the onboarding process, confirm that you've enabled the Braze SDK on your Shopify website.

![Setup step to enable Braze SDKs.]({% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %})

### Step 3: Track Shopify data 

Enhance your integration by adding more Shopify events and attributes, which will be powered by Shopify webhooks. For detailed information on the data tracked through this integration, refer to [Shopify Data Features]({{site.baseurl}}/shopify_data_features/). 

![Setup step to track Shopify data.]({% image_buster /assets/img/Shopify/track_shopify_data_setup.png %})

### Step 4: Historical backfill (optional)

Through the custom setup, you have the option to load your Shopify customers and orders from the past 90 days before connecting your Shopify integration. To include this initial data load, check the box for the initial data load option.

If you prefer to perform the backfill later, you can complete the initial setup now and return to this step at a later time.

![Section to set up historical data backfill.]({% image_buster /assets/img/Shopify/historical_backfill_setup.png %})

This table contains the data that will be initially loaded through the backfill.

| Braze recommended events | Shopify custom events | Braze standard attributes | Braze subscription statuses |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li></ul>{:/} | {::nomarkdown}<ul><li>Email marketing subscriptions associated with this Shopify store</li><li>SMS marketing subscriptions associated with this Shopify store</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Step 5: Custom data tracking setup (advanced) 

With the Braze SDKs, you can track custom events or custom attributes that go beyond supported data for this integration. Custom events capture unique interactions in your store, such as:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Custom events</th>
      <th style="width: 50%;">Custom attributes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Using a custom discount code</li>
          <li>Interacting with a personalized product recommendation</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Favorite brands or products</li>
          <li>Preferred shopping categories</li>
          <li>Membership or loyalty status</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

The SDK must be initialized (listening for activity) on a user’s device to log events or custom attributes. To learn more about logging custom data, refer to [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) and [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Step 6: Configure how you manage users (optional) {#step-6}

Select your `external_id` type from the dropdown.

![“Collect subscribers” section.]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Using an email address or a hashed email address as your Braze external ID can help simplify identity management across your data sources. However, it's important to consider the potential risks to user privacy and data security.<br><br>

- **Guessable Information:** Email addresses are easily guessable, making them vulnerable to attacks.
- **Risk of Exploitation:** If a malicious user alters their web browser to send someone else's email address as their external ID, they could potentially access sensitive messages or account information.
{% endalert %}

By default, Braze automatically converts emails from Shopify to lowercase before using them as the external ID. If you’re using email or hashed email as your external ID, confirm that your email addresses are also converted to lowercase before you assign them as your external ID or before hashing them from other data sources. This helps prevent discrepancies in external IDs and avoid creating duplicate user profiles in Braze.

If you selected a custom external ID type, proceed to steps 6.1—6.3. Otherwise, continue to step 6.4.

#### Step 6.1: Create the `braze.external_id` metafield

1. In your Shopify admin panel, go to **Settings** > **Metafields**.
2. Select **Customers** > **Add definition**.
3. For **Namespace and key**, enter `braze.external_id`.
4. For **Type**, select **ID Type**.

After the metafield is created, populate it for your customers. We recommend the following approaches:

- **Listen to customer creation webhooks:** Set up a webhook to listen for [`customer/create` events](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). This allows you to write the metafield when a new customer is created.
- **Backfill existing customers:** Use the [Admin API](https://shopify.dev/docs/api/admin-graphql) or [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) to backfill the metafield for previously created customers.

#### Step 6.2: Create an endpoint to retrieve your external ID

You need to create a public endpoint that Braze can call to retrieve the external ID. This is necessary for scenarios where Shopify can't provide the `braze.external_id` metafield. 

##### Endpoint specifications

**Method:** `GET`

| Parameters | Description |
| --- | --- |
| `shopify_customer_id` | The Shopify customer ID. |
| `email_address` | The email address of the logged-in user. |
| `shopify_storefront` | The storefront for the request. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Example endpoint

```
GET 
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

##### Expected response

Braze expects a `200` status code. Any other code is considered a failure.

{% raw %}
```json
{ 
    "external_id": "my_external_id" 
}
```
{% endraw %}

{% alert important %}
It's important to validate that the `shopify_customer_id` and `email_address` match the customer values in Shopify. You can use the [Admin API](https://shopify.dev/docs/api/admin-graphql) or [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) to validate these parameters and retrieve the `braze.external_id` metafield.
{% endalert %}

#### Step 6.3: Input your external ID

Repeat [Step 6](#step-6), and enter your endpoint URL after selecting custom external ID as your Braze external ID type.

##### Considerations

- If your external ID isn't generated when Braze sends a request to your endpoint, the integration will default to using the Shopify customer ID when the `changeUser` function is called. This step is crucial for merging the anonymous user profile with the identified user profile. As a result, there may be a temporary period during which different types of external IDs exist within your workspace.
- When the external ID is available in the `braze.external_id` metafield, the integration will prioritize and assign this external ID. 
    - If the Shopify customer ID was previously set as the Braze external ID, it will be replaced with the `braze.external_id` metafield value. 

#### Step 6.4: Collect your email or SMS opt-ins from Shopify (optional)

You have the option to collect your email or SMS marketing opt-ins from Shopify. 

If you use the email or SMS channels, you can sync your email and SMS marketing opt-in states into Braze. If you sync email marketing opt-ins from Shopify, Braze will automatically create an email subscription group for all users associated with that specific store. You need to create a unique name for this subscription group.

![“Collect subscribers” section with option to collect email or SMS marketing opt-ins.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
As mentioned in [Shopify overview]({{site.baseurl}}/shopify_overview/), if you want to use a third-party capture form, your developers need to integrate Braze SDK code. This will let you capture the email address and global email subscription status from form submissions. Specifically, you need to implement and test these methods to your `theme.liquid` file:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Sets the email address on the user profile
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Updates the global email subscription status
{% endalert %}

### Step 7: Sync products (optional)

You can sync all products from your Shopify store to a Braze catalog for deeper messaging personalization. Automatic updates occur in near real-time so your catalog always reflects the latest product details. To learn more, check out [Shopify product sync]({{site.baseurl}}/shopify_catalogs/).

![Setup step to sync product data to Braze.]({% image_buster /assets/img/Shopify/sync_product_data.png %})

### Step 8: Activate channels

To activate in-app messages, Content Cards, and Feature Flags using the Shopify direct integration, add each channel to your SDK. Follow the documentation links provided for each channel below:

- **In-app messages:** For enabling in-app messages for lead capture form use cases, refer to [In-app messages]({{site.baseurl}}/developer_guide/in_app_messages/).
- **Content Cards:** For enabling Content Cards for inbox or website banner use cases, refer to [Content Cards]({{site.baseurl}}/developer_guide/content_cards/).
- **Feature flags:** For enabling Feature Flags for site experimentation use cases, refer to [Feature flags]({{site.baseurl}}/developer_guide/feature_flags/).

### Step 9: Finish setup

After you've gone through all the steps, select **Finish Setup** to return to the partner page. Then, enable the Braze app embed in your Shopify admin page as indicated by the banner that displays.

![Banner that says to activate the Braze app embed in Shopify so that you can finish setting up your integration.]({% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %})

#### Example code

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) is an example Hydrogen app that contains all the code covered in the prior steps. 

