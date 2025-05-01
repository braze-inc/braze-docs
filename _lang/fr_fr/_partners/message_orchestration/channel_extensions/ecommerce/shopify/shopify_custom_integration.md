---
nav_title: "Configuration de l'intégration personnalisée de Shopify"
article_title: "Configuration de l'intégration personnalisée de Shopify"
description: "Cet article de référence explique comment se connecter à une boutique Shopify Hydrogen ou à n'importe quelle boutique Shopify sans tête en utilisant une vitrine personnalisée."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 2
toc_headers: h2
---

# Configuration de l'intégration personnalisée de Shopify

> Cette page vous explique comment intégrer Braze à une boutique Shopify Hydrogen ou à n'importe quelle boutique Shopify sans tête en utilisant une vitrine personnalisée.

Ce guide utilise le cadre Hydrogen de Shopify comme exemple. Cependant, vous pouvez suivre une approche similaire si votre marque utilise Shopify pour le backend de votre boutique avec une configuration frontale " sans tête ".  

Pour intégrer votre boutique Shopify headless à Braze, vous devez remplir ces deux objectifs :

1. **Initialiser et charger le SDK Web de Braze pour permettre le suivi sur site.**<br><br> Ajoutez manuellement un code dans votre site Shopify pour activer le suivi sur site de Braze. En mettant en œuvre le SDK de Braze sur votre boutique Shopify headless, vous pouvez suivre les activités sur site, notamment les sessions, le comportement anonyme des utilisateurs, les actions des acheteurs avant le passage en caisse, ainsi que tout [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) ou [attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) que vous choisissez d'inclure avec votre équipe de développement. Vous pouvez également ajouter tous les canaux pris en charge par les SDK, tels que les messages in-app ou les cartes de contenu. 

{: start="2"}
2\. **Connectez votre magasin à l'intégration native de Braze**<br><br> Après avoir connecté votre boutique Shopify à Braze, vous aurez accès aux données des clients, des caisses, des commandes et des produits grâce aux webhooks de Shopify.

{% alert important %}
Avant de commencer votre intégration, confirmez que vous avez correctement configuré le sous-domaine de la caisse pour votre vitrine Shopify. Pour plus d'informations, reportez-vous à la section [Migrer de la boutique en ligne vers Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Si cette configuration n'est pas effectuée correctement, Braze ne peut pas traiter les webhooks de paiement de Shopify. Il ne sera pas non plus possible de tester l'intégration dans un environnement de développement local, car cela suppose un domaine partagé entre votre vitrine et la page de paiement.
{% endalert %}

Pour atteindre ces objectifs, suivez les étapes suivantes :

## Étape 1 : Créer une application pour le site web de Braze {#step-1}

Dans Braze, accédez à **Paramètres** > **Paramètres des applications** > puis sélectionnez **Ajouter une application.** Nommez l'application "Shopify".

{% alert warning %}
La boutique doit être nommée "Shopify", sinon l'intégration risque de ne pas fonctionner correctement.
{% endalert %}

## Étape 2 : Ajouter un sous-domaine et des variables environnementales {#step-2}

1. Configurez votre sous-domaine Shopify pour [rediriger le trafic de votre boutique en ligne vers Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic/).  
2. Ajoutez un [URI de rappel](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) pour l'identifiant. (L'URI sera automatiquement ajouté lors de l'ajout du domaine).
3. Configurez vos [variables d'environnement Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable):
  - Créez deux variables d'environnement en utilisant les valeurs de l'application de site web que vous avez créée à l'[étape 1.](#step-1)
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

## Étape 3 : Permettre le suivi sur place

La première étape consiste à initialiser le SDK Web de Braze. Nous vous recommandons de le faire en installant notre paquetage NPM :

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
La version du SDK Web de Braze doit être la 5.4.0.
{% endalert %}

[Incluez]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) ensuite [ce paramètre]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) en tant que clé de premier niveau dans votre fichier `vite.config.js`:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Après avoir installé le paquetage NPM, vous devez initialiser le SDK dans un crochet `useEffect` à l'intérieur du composant `Layout`. Selon votre version de Hydrogen, ce composant peut être situé dans le fichier `root.jsx` ou `layout.jsx`:

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

Les valeurs `data.brazeApiKey` et `data.brazeApiUrl` doivent être incluses dans le chargeur de composants à l'aide des variables d'environnement créées à l'[étape 2 :](#step-2)

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
Les politiques de sécurité du contenu (généralement situées dans le fichier `entry.server.jsx` Hydrogen) peuvent avoir un impact sur la fonctionnalité des scripts Braze, tant dans les environnements locaux que dans les environnements de production. Nous vous suggérons de faire des tests à l'aide de versions préliminaires envoyées à Shopify par l'intermédiaire d'Oxygen ou de déploiements personnalisés. Si vous rencontrez des problèmes, vous devrez configurer votre CSP pour permettre à notre JavaScript de fonctionner.
{% endalert %}

## Étape 4 : Ajouter un événement d'identification de compte Shopify 

Suivez le moment où un acheteur se connecte à son compte et synchronise ses informations d'utilisateur avec Braze. Il s'agit notamment d'appeler notre méthode `changeUser` pour identifier les clients disposant d'un ID externe Braze. 

{% alert note %}
Nous ne disposons pas actuellement de conseils pour la prise en charge d'un ID externe Braze personnalisé. Si vous en avez besoin pour votre intégration actuelle, contactez votre gestionnaire de satisfaction client.
{% endalert %}

Avant de commencer, assurez-vous que vous avez configuré les URI de rappel pour l'identifiant du client afin qu'ils fonctionnent dans Hydrogen. Pour plus d'informations, reportez-vous à la section [Utilisation de l'API de compte client avec Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Après avoir configuré les URI de rappel, définissez une fonction permettant d'appeler le SDK de Braze. Créez un nouveau fichier (tel que `Tracking.jsx`) et importez-le à partir de vos composants :

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
2\. Dans le même crochet `useEffect` qui initialise le SDK de Braze, ajoutez l'appel à cette fonction :

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
3\. Récupérez l'e-mail et le numéro de téléphone du client dans votre requête GraphQL de l'API Client, située dans le fichier `app/graphql/customer-account/CustomerDetailsQuery.js`:

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
4\. Enfin, chargez les données personnalisées dans votre fonction loader :

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

## Étape 5 : Ajouter le suivi des événements Produit vu et Panier mis à jour

### Produits vus lors d'événements

1. Ajoutez cette fonction à votre fichier `Tracking.jsx`:

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
2\. Pour appeler la fonction précédente chaque fois qu'un utilisateur visite une page de produit, ajoutez un crochet `useEffect` au composant Produit dans le fichier `app/routes/products.$handle.jsx`:

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
3\. Ajoutez la valeur pour "storefrontUrl" (parce qu'elle n'est pas dans le chargeur de composants par défaut) :

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

### Panier Événements mis à jour

Outre le suivi de l'événement `cart_updated`, vous devez envoyer la valeur du jeton du panier à Braze. Nous utilisons la valeur du jeton de panier pour traiter les webhooks de commande reçus de Shopify. Pour ce faire, vous devez créer un alias d'utilisateur dont le nom est le jeton de panier de Shopify. 

1. Définissez les fonctions permettant de suivre l'événement `cart_updated` et de définir le jeton du panier :

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
2\. Renvoyez l'objet `cart` à partir de l'action de récupération afin que Braze puisse accéder à ses propriétés en allant dans votre fichier `app/routes/cart.jsx` et en ajoutant ce qui suit à la ligne de commande `action`
fonction :

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

Pour plus d'informations sur les récupérateurs Remix, reportez-vous à [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3\. Les magasins Hydrogen définissent généralement un composant `CartForm` qui gère l'état de l'objet panier, utilisé lors de l'ajout, de la suppression et de la modification de la quantité d'articles dans un panier. Ajoutez un autre crochet `useEffect` dans le composant `AddToCartButton` qui appellera la fonction `trackCartUpdated` chaque fois que l'état de l'extracteur de formulaires changera (chaque fois que le panier de l'utilisateur sera mis à jour) :

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
4\. Utilisez la même adresse `fetcherKey` pour les actions responsables de la mise à jour d'un produit existant dans votre panier. Ajoutez les éléments suivants aux composants `CartLineRemoveButton` et `CartLineUpdateButton` (situés par défaut dans le fichier `app/components/CartLineItem.jsx`) :

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

## Étape 6 : Installez l'intégration de Braze dans Shopify.

### Étape 6.1 : Connectez votre boutique Shopify

Rendez-vous sur la page partenaire de Shopify pour commencer votre configuration. Tout d'abord, sélectionnez **Commencer la configuration** pour installer l'application Braze à partir de l'App Store de Shopify. Suivez les étapes guidées pour terminer le processus d'installation.

![Page de configuration de l'intégration de Shopify sur le tableau de bord de Braze.][2]

### Étape 6.2 : Activer les SDK de Braze 

Pour les boutiques Shopify Hydrogen ou headless, sélectionnez l'option de **configuration personnalisée**. 

Avant de poursuivre le processus d'onboarding, confirmez que vous avez activé le SDK de Braze sur votre site Shopify.

![Étape de configuration pour activer les SDK de Braze.][3]

### Étape 6.3 : Assurer le suivi des données Shopify 

Améliorez votre intégration en ajoutant davantage d'événements et d'attributs Shopify, qui seront alimentés par les webhooks de Shopify. Pour obtenir des informations détaillées sur les données suivies par le biais de cette intégration, reportez-vous aux [Fonctionnalités des données de Shopify]({{site.baseurl}}/shopify_data_features/). 

![Étape de configuration pour le suivi des données de Shopify.][4]

### Étape 6.4 : Remblai historique (facultatif)

Grâce à la configuration personnalisée, vous avez la possibilité de charger vos clients et commandes Shopify des 90 derniers jours avant de connecter votre intégration Shopify. Pour inclure ce chargement initial de données, cochez la case de l'option de chargement initial de données.

Si vous préférez effectuer le remblayage plus tard, vous pouvez terminer la configuration initiale maintenant et revenir à cette étape ultérieurement.

![Section pour mettre en place le remplissage des données historiques.][5]

Cette table contient les données qui seront initialement chargées par le biais du remblai.

| Événements recommandés par Braze | Événements personnalisés de Shopify | Attributs standard de Braze | État des abonnements à Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Commande passée</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Prénom</li><li>Nom de famille</li><li>Téléphone</li><li>Ville</li><li>Pays</li></ul>{:/} | {::nomarkdown}<ul><li>Abonnements au marketing par e-mail associés à cette boutique Shopify.</li><li>Abonnements au marketing parms associés à cette boutique Shopify.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Étape 6.5 : Configuration personnalisée du suivi des données (avancée) 

Avec les SDK de Braze, vous pouvez suivre des événements personnalisés ou des attributs personnalisés qui vont au-delà des données prises en charge pour cette intégration. Les événements personnalisés capturent les interactions uniques dans votre magasin, comme par exemple :

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Événements personnalisés</th>
      <th style="width: 50%;">Attributs personnalisés</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Utilisation d’un code de réduction personnalisé</li>
          <li>Interagir avec une recommandation produit personnalisée</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marques ou produits favoris</li>
          <li>Catégories d’achat préférées</li>
          <li>Statut d’adhésion ou de fidélité</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Le SDK doit être initialisé (à l'écoute de l'activité) sur l'appareil d'un utilisateur pour enregistrer des événements et des attributs personnalisés. Pour en savoir plus sur l'enregistrement des données personnalisées, reportez-vous à l'[objet personnalisé](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) et à [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Étape 6.6 : Configurer la gestion des utilisateurs (facultatif)

Tout d'abord, sélectionnez votre `external_id` dans la liste déroulante. 

![Section "Recueillir les abonnés".][6]

{% alert important %}
L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut contribuer à simplifier la gestion des identités dans l'ensemble de vos sources de données. Toutefois, il est important de prendre en compte les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.<br><br>

- **Informations à deviner :** Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail de quelqu'un d'autre comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.
{% endalert %}

Deuxièmement, vous avez la possibilité de collecter vos abonnements marketing par e-mail ou SMS depuis Shopify. 

Si vous utilisez les canaux e-mail ou SMS, vous pouvez synchroniser vos états d'abonnement au marketing parketeur sms et e-mail dans Braze. Si vous synchronisez des abonnements de marketing par e-mail depuis Shopify, Braze créera automatiquement un groupe d'abonnement e-mail pour tous les utilisateurs associés à ce magasin spécifique. Vous devez créer un nom unique pour ce groupe d'abonnement.

![Section "Collecte des abonnés" avec option de collecte des opt-ins de marketing par e-mail ou SMS.][9]

{% alert note %}
Comme indiqué dans l'[aperçu de Shopify]({{site.baseurl}}/shopify_overview/), si vous souhaitez utiliser un formulaire de capture tiers, vos développeurs doivent intégrer le code SDK de Braze. Cela vous permettra de capturer l'adresse e-mail et l'état global de l'abonnement à l'e-mail à partir des soumissions de formulaire. Plus précisément, vous devez mettre en œuvre et tester ces méthodes dans votre fichier `theme.liquid`:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Définit l'adresse e-mail dans le profil utilisateur.
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Mise à jour de l'état de l'abonnement global à l'e-mail
{% endalert %}

### Étape 6.7 : Synchroniser les produits (facultatif)

Vous pouvez synchroniser tous les produits de votre boutique Shopify avec un catalogue Braze pour une personnalisation plus poussée des messages. Les mises à jour automatiques s'effectuent quasiment en temps réel, de sorte que votre catalogue reflète toujours les détails les plus récents sur les produits. Pour en savoir plus, consultez le site [Shopify product sync]({{site.baseurl}}/shopify_catalogs/).

![Étape de configuration pour synchroniser les données du produit avec Braze.][7]

### Étape 6.8 : Activer les canaux

Pour activer les messages in-app, les cartes de contenu et les drapeaux de fonctionnalité à l'aide de l'intégration directe de Shopify, ajoutez chaque canal à votre SDK. Suivez les liens de documentation fournis pour chaque canal ci-dessous :

- **Messages in-app :** Pour activer les messages in-app pour les cas d'utilisation des formulaires de capture de prospects, reportez-vous à [Messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/).
- **Cartes de contenu (Content cards) :** Pour activer les cartes de contenu pour les cas d'utilisation de la boîte de réception ou de la bannière de site web, reportez-vous aux [cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/).
- **Drapeaux de fonctionnalité :** Pour activer les drapeaux de fonctionnalité dans les cas d'utilisation pour l'expérimentation sur site, reportez-vous à la section [Drapeaux de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/).

### Étape 6.9 : Terminer la configuration

Une fois toutes les étapes franchies, sélectionnez **Terminer la configuration** pour revenir à la page partenaire. Ensuite, activez l'intégration de l'appli Braze dans votre page d'administration Shopify, comme indiqué par la bannière qui s'affiche.

![Bannière qui dit d'activer l'intégration de l'appli Braze dans Shopify pour que vous puissiez finir de paramétrer votre intégration.][8]

### Exemple de code

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) est un exemple d'application Hydrogen qui contient tout le code couvert dans les étapes précédentes. 

[1]: {% image_buster /assets/img/Shopify/add_new_app.png %}
[2]: {% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %}
[3]: {% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %}
[4]: {% image_buster /assets/img/Shopify/track_shopify_data_setup.png %}
[5]: {% image_buster /assets/img/Shopify/historical_backfill_setup.png %}
[6]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[7]: {% image_buster /assets/img/Shopify/sync_product_data.png %}
[8]: {% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %}
[9]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}