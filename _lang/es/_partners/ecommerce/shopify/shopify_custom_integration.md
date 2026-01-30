---
nav_title: Configuración de la integración personalizada de Shopify
article_title: "Configuración de la integración personalizada de Shopify"
description: "Este artículo de referencia explica cómo conectar con una tienda Shopify Hydrogen o cualquier tienda Shopify headless utilizando un escaparate personalizado."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Configuración de la integración personalizada de Shopify

> Esta página te explica cómo integrar Braze con una tienda Hydrogen de Shopify o con cualquier tienda sin tienda de Shopify utilizando un escaparate personalizado.

Esta guía utiliza el framework Hydrogen de Shopify como ejemplo. Sin embargo, puedes seguir un enfoque similar si tu marca utiliza Shopify para el backend de tu tienda con una configuración de frontend "sin cabeza".  

Para integrar tu tienda Shopify headless con Braze, necesitas completar estos dos objetivos:

1. **Inicializa y carga el SDK Web de Braze para habilitar el seguimiento in situ**<br><br> Añade manualmente código en tu sitio web de Shopify para habilitar el seguimiento in situ de Braze. Al implementar el SDK de Braze en tu tienda headless de Shopify, puedes hacer un seguimiento de las actividades in situ, incluidas las sesiones, el comportamiento del usuario anónimo, las acciones del comprador previas al pago y cualquier [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) o [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) que decidas incluir con tu equipo de desarrolladores. También puedes añadir cualquier canal admitido por los SDK, como mensajes dentro de la aplicación o tarjetas de contenido. 

{: start="2"}
2\. **Instala la integración Braze Shopify**<br><br> Cuando conectes tu tienda Shopify a Braze, tendrás acceso a los datos de clientes, pagos, pedidos y productos a través de los webhooks de Shopify.

{% alert important %}
Antes de iniciar la integración, confirma que has configurado correctamente el subdominio de pago para tu tienda de Shopify. Para más información, consulta [Migrar de la tienda online a Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Si esta configuración no se realiza correctamente, Braze no podrá procesar los webhooks de pago de Shopify. Tampoco será posible probar la integración en un entorno de desarrollo local, porque eso depende de un dominio compartido entre tu tienda y la página de pago.
{% endalert %}

Para completar estos objetivos, sigue estos pasos:

## Inicializar y cargar el SDK Web de Braze

### Paso 1: Crear una aplicación para el sitio web de Braze {#step-1}

En Braze, ve a **Configuración** > **Configuración de la aplicación** > y selecciona **Añadir aplicación**. Nombra la aplicación como "Shopify".

{% alert warning %}
La tienda debe llamarse "Shopify" o la integración podría no funcionar correctamente.
{% endalert %}

### Paso 2: Añadir subdominio y variables de entorno {#step-2}

1. Configura tu subdominio de Shopify para [redirigir el tráfico de tu tienda online a Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic).  
2. Añade una [URI de devolución de llamada](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) para iniciar sesión. (La URI se añadirá automáticamente cuando se añada el dominio).
3. Configura tus [variables de entorno de Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable):
  - Crea dos variables de entorno utilizando los valores de la aplicación del sitio web que creaste en [el Paso 1](#step-1).
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

### Paso 3: Habilitar el seguimiento in situ

El primer paso es inicializar el SDK Web de Braze. Te recomendamos que lo hagas instalando nuestro paquete NPM:

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
La versión del SDK Web de Braze debe ser 5.4.0.
{% endalert %}

A continuación, [incluye esta configuración]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) como clave de nivel superior en tu archivo `vite.config.js`:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Después de instalar el paquete NPM, debes inicializar el SDK dentro de un gancho `useEffect` dentro del componente `Layout`. Dependiendo de tu versión de Hydrogen, este componente puede estar ubicado en el archivo `root.jsx` o `layout.jsx`:

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

Los valores `data.brazeApiKey` y `data.brazeApiUrl` deben incluirse en el cargador de componentes mediante las variables de entorno creadas en [el Paso 2](#step-2):

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
Las políticas de seguridad de contenido (normalmente ubicadas en el archivo `entry.server.jsx` Hydrogen) pueden afectar a la funcionalidad de los scripts Braze tanto en entornos locales como de producción. Te sugerimos que pruebes las versiones de vista previa enviadas a Shopify a través de Oxygen o de despliegues personalizados. Si tienes problemas, tendrás que configurar tu CSP para permitir que funcione nuestro JavaScript.
{% endalert %}

### Paso 4: Añadir un evento de Iniciar sesión en la cuenta de Shopify 

Realiza un seguimiento de cuándo un comprador inicia sesión en su cuenta y sincroniza su información de usuario con Braze. Esto incluye llamar a nuestro método `changeUser` para identificar a los clientes con un ID externo de Braze. 

{% alert note %}
Actualmente no disponemos de orientación para admitir un ID externo personalizado de Braze. Si necesitas esto para tu integración ahora, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

Antes de iniciar, asegúrate de que has configurado las URI de devolución de llamada para que la sesión del cliente funcione dentro de Hydrogen. Para más información, consulta [Utilizar la API de cuenta de cliente con Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Tras configurar las URI de devolución de llamada, define una función para llamar al SDK de Braze. Crea un nuevo archivo (como `Tracking.jsx`) e impórtalo desde tus componentes:

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
2\. En el mismo hook `useEffect` que inicializa el SDK de Braze, añade la llamada a esta función:

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
3\. Obtén la dirección de correo electrónico y el número de teléfono del cliente en tu consulta GraphQL de la API de clientes, ubicada en el archivo `app/graphql/customer-account/CustomerDetailsQuery.js`:

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
4\. Por último, carga los datos de clientes en tu función de carga:

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

### Paso 5: Añadir seguimiento para los eventos Producto Visto y Cesta Actualizada

#### Producto Eventos vistos

1. Añade esta función a tu archivo `Tracking.jsx`:

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
2\. Para llamar a la función anterior cada vez que un usuario visite una página de producto, añade un hook `useEffect` al componente Producto dentro del archivo `app/routes/products.$handle.jsx`:

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
3\. Añade el valor de "storefrontUrl" (porque no está predeterminado en el cargador de componentes):

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

#### Cesta Eventos actualizados

Además de realizar el seguimiento del evento `cart_updated`, tienes que enviar el valor del token del carrito a Braze. Utilizamos el valor del token del carrito para procesar los webhooks de pedido recibidos de Shopify. Esto se hace creando un alias de usuario con el token del carrito de Shopify como nombre. 

1. Define funciones para el seguimiento del evento `cart_updated` y la configuración del token del carrito:

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
2\. Devuelve el objeto `cart` desde la acción de obtención para que Braze pueda acceder a sus propiedades yendo a tu archivo `app/routes/cart.jsx` y añadiendo lo siguiente al campo `action`
función:

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

Para más información sobre los fetchers Remix, consulta [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3\. Las tiendas Hydrogen suelen definir un componente `CartForm` que gestiona el estado del objeto carrito, que se utiliza al añadir, eliminar y cambiar la cantidad de artículos de un carrito. Añade otro gancho `useEffect` en el componente `AddToCartButton` que llamará a la función `trackCartUpdated` cada vez que cambie el estado de obtención del formulario (cada vez que se actualice el carrito del usuario):

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
4\. Utiliza el mismo `fetcherKey` para las acciones responsables de actualizar un producto existente de tu carrito. Añade lo siguiente a los componentes `CartLineRemoveButton` y `CartLineUpdateButton` (ubicados por defecto en el archivo `app/components/CartLineItem.jsx`):

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

## Instala la integración Braze Shopify

### Paso 1: Conecta tu tienda Shopify

Ve a la página del socio de Shopify para iniciar tu configuración. Primero, selecciona **Iniciar configuración** para instalar la aplicación Braze desde la tienda de aplicaciones de Shopify. Sigue los pasos guiados para completar el proceso de instalación.

![Página de configuración de la integración de Shopify en el panel de Braze.]({% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %})

### Paso 2: Habilitación de los SDK de Braze 

Para tiendas Shopify Hydrogen o headless, selecciona la opción **Configuración personalizada**. 

Antes de continuar con el proceso de incorporación, confirma que has habilitado el SDK de Braze en tu sitio web de Shopify.

![Paso de configuración para habilitar los SDK de Braze.]({% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %})

### Paso 3: Rastrear datos de Shopify 

Mejora tu integración añadiendo más eventos y atributos de Shopify, que se activarán mediante webhooks de Shopify. Para obtener información detallada sobre los datos de seguimiento a través de esta integración, consulta [Características de los datos de Shopify]({{site.baseurl}}/shopify_data_features/). 

![Paso de configuración para el seguimiento de los datos de Shopify.]({% image_buster /assets/img/Shopify/track_shopify_data_setup.png %})

### Paso 4: Relleno histórico (opcional)

A través de la configuración personalizada, tienes la opción de cargar tus clientes y pedidos de Shopify de los últimos 90 días antes de conectar tu integración con Shopify. Para incluir esta carga inicial de datos, marca la casilla de la opción Carga inicial de datos.

Si prefieres realizar el relleno más tarde, puedes completar la configuración inicial ahora y volver a este paso más adelante.

![Sección para configurar el relleno de datos históricos.]({% image_buster /assets/img/Shopify/historical_backfill_setup.png %})

Esta tabla contiene los datos que se cargarán inicialmente a través del relleno.

| Eventos recomendados por Braze | Shopify eventos personalizados | Atributos estándar Braze | Estados de suscripción Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Pedido realizado</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Correo electrónico</li><li>Nombre</li><li>Apellido</li><li>Teléfono</li><li>Localidad</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li>Suscripciones de correo electrónico de marketing asociadas a esta tienda Shopify</li><li>Suscripciones de marketing por SMS asociadas a esta tienda Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Paso 5: Configuración personalizada de seguimiento de datos (avanzada) 

Con los SDK de Braze, puedes hacer un seguimiento de eventos personalizados o atributos personalizados que vayan más allá de los datos admitidos para esta integración. Los eventos personalizados capturan interacciones únicas en tu tienda, como:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Eventos personalizados</th>
      <th style="width: 50%;">Atributos personalizados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Usar un código de descuento personalizado</li>
          <li>Interactuar con una recomendación de productos personalizada</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marcas o productos favoritos</li>
          <li>Categorías de compra preferidas</li>
          <li>Membresía o estado de fidelización</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

El SDK debe estar inicializado (a la escucha de la actividad) en el dispositivo de un usuario para registrar eventos o atributos personalizados. Para saber más sobre el registro de datos personalizados, consulta [Objeto usuario](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) y [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Paso 6: Configura cómo administras a los usuarios (opcional) {#step-6}

Selecciona tu tipo de `external_id` en el desplegable.

![Sección "Recoger suscriptores".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Utilizar una dirección de correo electrónico o una dirección de correo electrónico con hash como tu ID externo de Braze puede ayudarte a simplificar la gestión de identidades en todos tus orígenes de datos. Sin embargo, es importante tener en cuenta los riesgos potenciales para la privacidad de los usuarios y la seguridad de los datos.<br><br>

- **Información adivinable:** Las direcciones de correo electrónico son fáciles de adivinar, lo que las hace vulnerables a los ataques.
- **Riesgo de explotación:** Si un usuario malintencionado altera su navegador web para enviar la dirección de correo electrónico de otra persona como ID externo, podría acceder potencialmente a mensajes confidenciales o a información de la cuenta.
{% endalert %}

Por defecto, Braze convierte automáticamente los correos electrónicos de Shopify a minúsculas antes de utilizarlos como ID externo. Si utilizas el correo electrónico o el correo electrónico con hash como ID externo, confirma que tus direcciones de correo electrónico también se convierten a minúsculas antes de asignarlas como ID externo o antes de aplicarles hash desde otros orígenes de datos. Esto ayuda a prevenir discrepancias en los ID externos y a evitar la creación de perfiles de usuario duplicados en Braze.

{% alert note %}
Los siguientes pasos dependen de tu selección de ID externo:<br><br>
- **Si seleccionaste un tipo de ID externo personalizado:** Completa los pasos 6.1-6.3 para establecer la configuración personalizada de tu ID externo.
- **Si seleccionaste ID de cliente de Shopify, correo electrónico o correo electrónico con hash:** Sáltate los pasos 6.1-6.3 y continúa directamente con el paso 6.4.
{% endalert %}

#### Paso 6.1: Crea el metacampo `braze.external_id` 

1. En tu panel de administración de Shopify, ve a **Configuración** > **Metacampos**.
2. Selecciona **Clientes** > **Añadir definición**.
3. Para **Espacio de nombres y clave**, introduce `braze.external_id`.
4. En **Tipo**, selecciona **Tipo de ID**.

Una vez creado el metacampo, rellénalo para tus clientes. Recomendamos los siguientes enfoques:

- **Escucha los webhooks de creación de clientes:** Configura un webhook para escuchar [los eventos de`customer/create` ](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Esto te permite escribir el metacampo cuando se crea un nuevo cliente.
- **Rellena a los clientes existentes:** Utiliza [la Admin API](https://shopify.dev/docs/api/admin-graphql) o la [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para rellenar el metacampo de los clientes creados previamente.

#### Paso 6.2: Crea un endpoint para recuperar tu ID externo

Debes crear un punto final público al que Braze pueda llamar para recuperar el ID externo. Esto permite a Braze obtener el ID en situaciones en las que Shopify no puede proporcionar directamente el metacampo `braze.external_id`.

##### Especificaciones del punto final

**Método:** OBTENER

Braze envía los siguientes parámetros a tu punto final:

| Parámetro            | Obligatoria | Tipo de datos | Descripción                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Sí      | Cadena    | El ID de cliente de Shopify.                                         |
| shopify_storefront   | Sí      | Cadena    | El nombre de la tienda para la solicitud. Ex: `<storefront_name>.myshopify.com` |
| email_address        | No       | Cadena    | La dirección de correo electrónico del usuario conectado. <br><br>Este campo puede faltar en algunos escenarios de webhook. Tu lógica de punto final debe tener en cuenta los valores nulos aquí (por ejemplo, obtener el correo electrónico utilizando shopify_customer_id si tu lógica interna lo requiere). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Ejemplo de punto final

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```


##### Respuesta esperada
Braze espera un código de estado `200` que devuelva el ID externo JSON:
```json
{
  "external_id": "my_external_id"
}
```

##### Validación

Es fundamental validar que `shopify_customer_id` y `email_address` (si existen) coinciden con los valores del cliente en Shopify. Puedes utilizar [la API de administración de Shopify](https://shopify.dev/docs/api/admin-graphql) o [la API de cliente](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar estos parámetros y recuperar el metacampo `braze.external_id` correcto.

##### Comportamiento en caso de fallo y fusión
Cualquier código de estado distinto de `200` se considera un fallo.

- **Implicaciones de la fusión:** Si el punto final falla (devuelve no`200` o se agota el tiempo de espera), Braze no puede recuperar el ID externo. En consecuencia, la fusión entre el usuario de Shopify y el perfil de usuario de Braze no se producirá en ese momento.
- **Lógica de reintento:** Braze puede intentar reintentos de red estándar inmediatos, pero si el fallo persiste, la fusión se aplazará hasta el siguiente evento que cumpla los requisitos (por ejemplo, la próxima vez que el usuario actualice su perfil o complete una compra).
- **Apoyabilidad:** Para poder fusionar usuarios a tiempo, asegúrate de que tu endpoint tiene una alta disponibilidad y gestiona el campo opcional `email_address` con elegancia.

#### Paso 6.3: Introduce tu ID externo

Repite [el paso 6](#step-6) e introduce la URL de tu punto final después de seleccionar ID externo personalizado como tipo de ID externo Braze.

##### Consideraciones

- Si tu ID externo no se genera cuando Braze envía una solicitud a tu punto final, la integración utilizará por defecto el ID de cliente de Shopify cuando se llame a la función `changeUser`. Este paso es crucial para fusionar el perfil de usuario anónimo con el perfil de usuario identificado. Como resultado, puede haber un periodo temporal durante el cual existan diferentes tipos de ID externos dentro de tu espacio de trabajo.
- Cuando el ID externo esté disponible en el metacampo `braze.external_id`, la integración priorizará y asignará este ID externo. 
    - Si el ID de cliente de Shopify estaba previamente configurado como ID externo de Braze, se sustituirá por el valor del metacampo `braze.external_id`. 

#### Paso 6.4: Recoger tus adhesiones voluntarias por correo electrónico o SMS desde Shopify (opcional)

Tienes la opción de recopilar tus adhesiones voluntarias de marketing por correo electrónico o SMS desde Shopify. 

Si utilizas los canales de correo electrónico o SMS, puedes sincronizar tus estados de adhesión voluntaria por correo electrónico y marketing por SMS en Braze. Si sincronizas las adhesiones voluntarias de marketing por correo electrónico desde Shopify, Braze creará automáticamente un grupo de suscripción por correo electrónico para todos los usuarios asociados a esa tienda específica. Tienes que crear un nombre único para este grupo de suscripción.

![Sección "Recoger suscriptores" con opción de recoger las adhesiones voluntarias por correo electrónico o marketing por SMS.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Como se menciona en el [resumen de Shopify]({{site.baseurl}}/shopify_overview/), si quieres utilizar un formulario de captura de terceros, tus desarrolladores necesitan integrar el código del SDK de Braze. Esto te permitirá capturar la dirección de correo electrónico y el estado global de suscripción por correo electrónico de los envíos de formularios. Concretamente, tienes que implementar y probar estos métodos en tu archivo `theme.liquid`:<br><br>
- [establecerCorreo](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Establece la dirección de correo electrónico en el perfil de usuario
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Actualiza el estado de la suscripción global por correo electrónico
{% endalert %}

### Paso 7: Sincronizar productos (opcional)

Puedes sincronizar todos los productos de tu tienda Shopify con un catálogo Braze para una mayor personalización de la mensajería. Las actualizaciones automáticas se producen casi en tiempo real para que tu catálogo refleje siempre los detalles más recientes de los productos. Para saber más, consulta la [sincronización de productos de Shopify]({{site.baseurl}}/shopify_catalogs/).

![Paso de configuración para sincronizar los datos del producto con Braze.]({% image_buster /assets/img/Shopify/sync_product_data.png %})

### Paso 8: Activar canales

Para activar los mensajes dentro de la aplicación, las tarjetas de contenido y las banderas de características utilizando la integración directa de Shopify, añade cada canal a tu SDK. Sigue los enlaces de documentación que se indican a continuación para cada canal:

- **Mensajes dentro de la aplicación:** Para habilitar los mensajes dentro de la aplicación para casos de uso de formularios de captación de clientes potenciales, consulta [Mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/).
- **Tarjetas de contenido:** Para habilitar las tarjetas de contenido para casos de uso de buzón de entrada o banner de sitio web, consulta [Tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/).
- **Banderas de características:** Para habilitar las banderas [de]({{site.baseurl}}/developer_guide/feature_flags/) características para casos de uso de experimentación en el sitio, consulta [Banderas de características]({{site.baseurl}}/developer_guide/feature_flags/).

### Paso 9: Configuración de acabado

Cuando hayas realizado todos los pasos, selecciona **Finalizar configuración** para volver a la página del socio. A continuación, habilita la incrustación de la aplicación Braze en tu página de administración de Shopify, tal y como indica el banner que aparece.

![Banner que dice que actives la incrustación de la aplicación Braze en Shopify para que puedas terminar de configurar tu integración.]({% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %})

#### Ejemplo de código

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) es una aplicación Hydrogen de ejemplo que contiene todo el código descrito en los pasos anteriores. 

