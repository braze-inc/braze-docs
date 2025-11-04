---
nav_title: Configuração de integração personalizada da Shopify
article_title: "Configuração de integração personalizada da Shopify"
description: "Este artigo de referência aborda como se conectar a uma loja Shopify Hydrogen ou a qualquer loja Shopify headless usando uma vitrine personalizada."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 2
---

# Configuração da integração personalizada do Shopify

> Esta página o orienta sobre como integrar o Braze a uma loja Shopify Hydrogen ou a qualquer loja Shopify headless usando uma vitrine personalizada.

Este guia usa a estrutura Hydrogen da Shopify como exemplo. No entanto, você pode seguir uma abordagem semelhante se a sua marca usar o Shopify para o back-end da sua loja com uma configuração de front-end "sem cabeça".  

Para integrar sua loja Shopify headless ao Braze, você precisa concluir essas duas metas:

1. **Inicialize e carregue o Braze Web SDK para ativar o rastreamento no local**<br><br> Adicione manualmente o código em seu site do Shopify para ativar o rastreamento no site do Braze. Ao implementar o Braze SDK em sua loja Shopify headless, é possível rastrear as atividades no local, incluindo sessões, comportamento anônimo do usuário, ações do comprador antes do checkout e quaisquer [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) ou [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) que você decida incluir com sua equipe de desenvolvimento. Você também pode adicionar quaisquer canais compatíveis com os SDKs, como mensagens no app ou cartões de conteúdo. 

{: start="2"}
2\. **Instale a integração do Braze com o Shopify**<br><br> Depois de conectar sua loja Shopify ao Braze, você terá acesso aos dados de clientes, checkout, pedidos e produtos por meio de webhooks do Shopify.

{% alert important %}
Antes de iniciar sua integração, confirme que você configurou corretamente o subdomínio de checkout para sua vitrine do Shopify. Para saber mais, consulte [Migrar da loja on-line para o Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Se essa configuração não for feita corretamente, o Braze não poderá processar os webhooks de checkout do Shopify. Também não será possível testar a integração em um ambiente de desenvolvimento local, pois isso depende de um domínio compartilhado entre a loja e a página de checkout.
{% endalert %}

Para concluir essas metas, siga estas etapas:

## Inicializar e carregar o Braze Web SDK

### Etapa 1: Criar um app para o site do Braze {#step-1}

No Braze, acesse **Settings** > **App Settings** > e selecione **Add App**. Nomeie o app como "Shopify".

{% alert warning %}
A loja deve ter o nome "Shopify" ou a integração poderá não funcionar corretamente.
{% endalert %}

### Etapa 2: Adicionar subdomínio e variáveis ambientais {#step-2}

1. Configure seu subdomínio do Shopify para [redirecionar o tráfego da sua loja on-line para o Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic/).  
2. Adicione um [URI de retorno de chamada](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) para login. (O URI será adicionado automaticamente quando o domínio for adicionado).
3. Configure suas [variáveis de ambiente do Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable):
  - Crie duas variáveis de ambiente usando os valores do app do site que você criou na [etapa 1](#step-1).
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

### Etapa 3: Ativar o rastreamento no local

A primeira etapa é inicializar o Braze Web SDK. Recomendamos fazer isso instalando nosso pacote NPM:

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
A versão do Braze Web SDK deve ser 5.4.0.
{% endalert %}

Em seguida, [inclua essa configuração]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) como uma chave de nível superior em seu arquivo `vite.config.js`:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Depois de instalar o pacote NPM, você deve inicializar o SDK em um gancho `useEffect` dentro do componente `Layout`. Dependendo da sua versão do Hydrogen, esse componente pode estar localizado no arquivo `root.jsx` ou `layout.jsx`:

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

Os valores `data.brazeApiKey` e `data.brazeApiUrl` precisam ser incluídos no carregador de componentes usando as variáveis de ambiente criadas na [etapa 2](#step-2):

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
As políticas de segurança de conteúdo (geralmente localizadas no arquivo `entry.server.jsx` Hydrogen) podem afetar a funcionalidade dos scripts do Braze em ambientes locais e de produção. Sugerimos testar por meio de compilações prévias enviadas à Shopify por meio do Oxygen ou de implantações personalizadas. Se tiver problemas, você precisará configurar seu CSP para permitir que nosso JavaScript funcione.
{% endalert %}

### Etapa 4: Adicionar um evento de login de conta do Shopify 

Rastreie quando um comprador faz login em sua conta e sincroniza suas informações de usuário com o Braze. Isso inclui chamar nosso método `changeUser` para identificar clientes com uma ID externa Braze. 

{% alert note %}
No momento, não temos orientação para oferecer suporte a uma ID externa Braze personalizada. Se precisar disso para sua integração agora, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

Antes de começar, certifique-se de ter configurado os URIs de retorno de chamada para que o login do cliente funcione no Hydrogen. Para saber mais, consulte [Usando a API da conta do cliente com o Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Depois de configurar os URIs de retorno de chamada, defina uma função para chamar o SDK do Braze. Crie um novo arquivo (como `Tracking.jsx`) e importe-o de seus componentes:

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
2\. No mesmo gancho `useEffect` que inicializa o SDK do Braze, adicione a chamada a essa função:

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
3\. Obtenha o endereço de e-mail e o número de telefone do cliente em sua consulta da API do cliente GraphQL, localizada no arquivo `app/graphql/customer-account/CustomerDetailsQuery.js`:

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
4\. Finalmente, carregue os dados do cliente em sua função de carregador:

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

### Etapa 5: Adicionar rastreamento para os eventos Product Viewed e Cart Updated

#### Eventos visualizados pelo produto

1. Adicione essa função ao seu arquivo `Tracking.jsx`:

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
2\. Para chamar a função anterior sempre que um usuário visitar uma página de produto, adicione um gancho `useEffect` ao componente Product no arquivo `app/routes/products.$handle.jsx`:

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
3\. Adicione o valor para "storefrontUrl" (porque ele não está no carregador de componentes por padrão):

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

#### Carrinho Eventos atualizados

Além de rastrear o evento `cart_updated`, você precisa enviar o valor do token do carrinho para o Braze. Usamos o valor do token do carrinho para processar webhooks de pedidos recebidos da Shopify. Isso é feito criando um alias de usuário com o token do carrinho do Shopify como seu nome. 

1. Defina funções para o rastreamento do evento `cart_updated` e a configuração do token do carrinho:

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
2\. Retorne o objeto `cart` da ação do fetcher para que o Braze possa acessar suas propriedades acessando seu arquivo `app/routes/cart.jsx` e adicionando o seguinte ao `action`
função:

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

Para saber mais sobre os fetchers do Remix, consulte [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3\. As lojas Hydrogen geralmente definem um componente `CartForm` que gerencia o estado do objeto do carrinho, que é usado ao adicionar, remover e alterar a quantidade de itens em um carrinho. Adicione outro gancho `useEffect` no componente `AddToCartButton` que chamará a função `trackCartUpdated` sempre que o estado do buscador de formulários for alterado (sempre que o carrinho do usuário for atualizado):

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
4\. Use o mesmo endereço `fetcherKey` para as ações responsáveis pela atualização de um produto existente em seu carrinho. Adicione o seguinte aos componentes `CartLineRemoveButton` e `CartLineUpdateButton` (localizados por padrão no arquivo `app/components/CartLineItem.jsx`):

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

## Instale a integração do Braze com o Shopify

### Etapa 1: Conecte sua loja da Shopify

Acesse a página de parceiros do Shopify para iniciar sua configuração. Primeiro, selecione **Begin Setup (Iniciar configuração)** para instalar o aplicativo Braze da Shopify App Store. Siga as etapas guiadas para concluir o processo de instalação.

![Página de configuração da integração com o Shopify no dashboard do Braze.]({% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %})

### Etapa 2: Ativar os SDKs da Braze 

Para lojas Shopify Hydrogen ou headless, selecione a opção **Configuração personalizada**. 

Antes de continuar com o processo de integração, confirme que você ativou o Braze SDK em seu site da Shopify.

![Etapa de configuração para ativar os SDKs do Braze.]({% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %})

### Etapa 3: Rastrear dados da Shopify 

Aprimore sua integração adicionando mais eventos e atribuições do Shopify, que serão alimentados por webhooks do Shopify. Para obter informações detalhadas sobre os dados rastreados por meio dessa integração, consulte [Recursos de dados do Shopify]({{site.baseurl}}/shopify_data_features/). 

![Etapa de configuração para rastrear dados do Shopify.]({% image_buster /assets/img/Shopify/track_shopify_data_setup.png %})

### Etapa 4: Preenchimento histórico (opcional)

Por meio da configuração personalizada, você tem a opção de carregar seus clientes e pedidos do Shopify dos últimos 90 dias antes de conectar sua integração com o Shopify. Para incluir esse carregamento inicial de dados, marque a caixa da opção de carregamento inicial de dados.

Se preferir realizar o preenchimento posteriormente, você pode concluir a configuração inicial agora e retornar a essa etapa mais tarde.

![Seção para configurar o backfill de dados históricos.]({% image_buster /assets/img/Shopify/historical_backfill_setup.png %})

Essa tabela contém os dados que serão inicialmente carregados por meio do backfill.

| Eventos recomendados pelo Braze | Eventos personalizados da Shopify | Atribuições padrão do Braze | Status das inscrições no Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Pedido feito</li></ul>{:/}  | {::nomarkdown}<ul><li>etiquetas_da_loja</li><li>shopify_total_spent</li><li>contagem de pedidos do shopify</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>código postal da loja</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Nome</li><li>Sobrenome</li><li>Telefone</li><li>Cidade</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li>Inscrições de envio de e-mail marketing associadas a esta loja Shopify</li><li>Inscrições de marketing por SMS associadas a esta loja da Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Etapa 5: Configuração de rastreamento de dados personalizado (avançado) 

Com os SDKs da Braze, você pode rastrear eventos personalizados ou atributos personalizados que vão além dos dados suportados para essa integração. Os eventos personalizados capturam interações exclusivas em sua loja, como:

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
          <li>Como usar um código de desconto personalizado</li>
          <li>Como interagir com uma recomendação personalizada de produto</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marcas ou produtos favoritos</li>
          <li>Categorias de compras de preferência</li>
          <li>Status de cadastro ou fidelidade</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

O SDK deve ser inicializado (ouvindo a atividade) no dispositivo de um usuário para registrar eventos ou atributos personalizados. Para saber mais sobre o registro de dados personalizados, consulte [Objeto de usuário](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) e [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Etapa 6: Configurar como gerenciar usuários (opcional)

Selecione seu tipo de `external_id` no menu suspenso.

![Seção "Coletar assinantes".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Usar um endereço de e-mail ou um endereço de e-mail com hash como sua ID externa Braze pode ajudar a simplificar o gerenciamento de identidade em suas fontes de dados. No entanto, é importante considerar os possíveis riscos à privacidade do usuário e à segurança dos dados.<br><br>

- **Informações que podem ser adivinhadas:** Os endereços de e-mail são facilmente adivinháveis, o que os torna vulneráveis a ataques.
- **Risco de exploração:** Se um usuário mal-intencionado alterar seu navegador da Internet para enviar o endereço de e-mail de outra pessoa como sua ID externa, ele poderá acessar mensagens confidenciais ou informações de conta.
{% endalert %}

Se você selecionou um tipo de ID externo personalizado, prossiga para as etapas 6.1 e 6.2. Caso contrário, continue na etapa 6.3.

#### Etapa 6.1: Criar um `external_id`

Primeiro, acesse o Shopify e crie o metacampo `braze.external_id`. Recomendamos seguir as etapas em [Criação de descrições de metacampo personalizadas](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions). Em **Namespace e key**, digite `braze.external_id`. Para **Tipo**, recomendamos que você escolha um tipo de ID.

Depois de criar o metacampo, ouça [`customer/create` webhooks](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) para que você possa escrever o metacampo quando um novo cliente for criado. Em seguida, use a [API do administrador](https://shopify.dev/docs/api/admin-graphql) ou a [API do cliente](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para preencher novamente todos os clientes criados anteriormente com esse metacampo.

#### Etapa 6.2: Criar um ponto de extremidade

Você precisa de um ponto de extremidade GET público para recuperar sua ID externa. Se o Shopify não puder fornecer o metacampo, o Braze chamará esse ponto de extremidade para recuperar o ID externo.

Um exemplo de endpoint é: `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

##### Resposta

O Braze espera um código de status 200. Qualquer outro código é considerado uma falha no endpoint. A resposta deve ser:

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Verifique o endereço `shopify_customer_id` e o endereço de e-mail usando a API de administração ou a API do cliente para confirmar que os valores dos parâmetros correspondem aos valores do cliente na Shopify. Após a validação, você também pode usar as APIs para recuperar o metacampo `braze.external_id` e retornar o valor do ID externo.

#### Etapa 6.3: Colete suas aceitações de e-mail ou SMS do Shopify (opcional)

Você tem a opção de coletar suas aceitações de marketing por e-mail ou SMS no Shopify. 

Se você usar os canais de e-mail ou SMS, poderá sincronizar seus estados de aceitação de marketing por e-mail e SMS no Braze. Se você sincronizar as aceitações de e-mail marketing do Shopify, o Braze criará automaticamente um grupo de inscrições para e-mail para todos os usuários associados a essa loja específica. Você precisa criar um nome exclusivo para esse grupo de inscrições.

![Seção "Collect subscribers" (Coletar assinantes) com opção para coletar aceitação de marketing por e-mail ou SMS.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Conforme mencionado na [visão geral do Shopify]({{site.baseurl}}/shopify_overview/), se você quiser usar um formulário de captura de terceiros, seus desenvolvedores precisarão integrar o código do Braze SDK. Isso permitirá que você capture o endereço de e-mail e o status global da inscrição de e-mail dos envios de formulários. Especificamente, você precisa implementar e testar esses métodos em seu arquivo `theme.liquid`:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Define o endereço de e-mail no perfil do usuário
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Atualiza o status da inscrição global de e-mail
{% endalert %}

### Etapa 7: Sincronizar produtos (opcional)

Você pode sincronizar todos os produtos de sua loja Shopify com um catálogo Braze para uma personalização mais profunda do envio de mensagens. As atualizações automáticas ocorrem quase em tempo real para que seu catálogo sempre reflita os detalhes mais recentes dos produtos. Para saber mais, confira a [sincronização de produtos da Shopify]({{site.baseurl}}/shopify_catalogs/).

![Etapa de configuração para sincronizar os dados do produto com o Braze.]({% image_buster /assets/img/Shopify/sync_product_data.png %})

### Etapa 8: Ativar canais

Para ativar mensagens no app, cartões de conteúdo e Feature Flags usando a integração direta do Shopify, adicione cada canal ao seu SDK. Siga os links de documentação fornecidos para cada canal abaixo:

- **Mensagens no app:** Para ativar mensagens no aplicativo para casos de uso de formulários de captura de leads, consulte [Mensagens no aplicativo]({{site.baseurl}}/developer_guide/in_app_messages/).
- **Cartões de conteúdo:** Para ativar os cartões de conteúdo para casos de uso de caixa de entrada ou banner de site, consulte [Cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/).
- **Feature Flag:** Para ativar os Feature Flags para casos de uso de experimentação no site, consulte [Feature flags]({{site.baseurl}}/developer_guide/feature_flags/).

### Etapa 9: Concluir configuração

Depois de acessar todas as etapas, selecione **Finish Setup (Concluir configuração)** para retornar à página do parceiro. Em seguida, ative a incorporação do app Braze em sua página de administração do Shopify, conforme indicado pelo banner exibido.

![Banner que diz para ativar a incorporação do app Braze no Shopify para que você possa concluir a configuração de sua integração.]({% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %})

#### Exemplo de código

[O Shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) é um app de exemplo do Hydrogen que contém todo o código abordado nas etapas anteriores. 

