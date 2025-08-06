---
nav_title: Configuração de Integração Personalizada do Shopify
article_title: "Configuração de Integração Personalizada do Shopify"
description: "Este artigo de referência cobre como se conectar a uma loja Shopify Hydrogen ou qualquer loja Shopify headless usando uma vitrine personalizada."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 2
toc_headers: h2
---

# configuração de integração personalizada do Shopify

> Esta página orienta você sobre como integrar o Braze com uma loja Shopify Hydrogen ou qualquer loja Shopify headless usando uma vitrine personalizada.

Este guia usa o framework Hydrogen do Shopify como exemplo. No entanto, você pode seguir uma abordagem semelhante se sua marca usar o Shopify para o backend de sua loja com uma configuração de front-end "headless".  

Para integrar sua loja Shopify headless com o Braze, você precisa completar estes dois objetivos:

1. **Inicializar e carregar o SDK Web do Braze para ativar o rastreamento no site**<br><br> Adicione manualmente o código ao seu site Shopify para ativar o rastreamento no site do Braze. Ao implementar o SDK do Braze em sua loja Shopify headless, você pode rastrear atividades no site, incluindo sessões, comportamento de usuários anônimos, ações de compradores antes do checkout e quaisquer [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) ou [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) que você escolher incluir com sua equipe de desenvolvimento. Você também pode adicionar quaisquer canais suportados pelos SDKs, como mensagens no aplicativo ou Cartões de Conteúdo. 

{: start="2"}
2\. **Conectar sua loja à integração nativa do Braze**<br><br> Depois de conectar sua loja Shopify ao Braze, você terá acesso a dados de clientes, checkout, pedidos e produtos através de webhooks do Shopify.

{% alert important %}
Antes de iniciar sua integração, confirme se você configurou corretamente o subdomínio de checkout para sua vitrine Shopify. Para mais informações, consulte [Migrar da loja online para o Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Se esta configuração não for feita corretamente, o Braze não poderá processar os webhooks de checkout do Shopify. Também não será possível testar a integração em um ambiente de desenvolvimento local, pois isso depende de um domínio compartilhado entre sua vitrine e a página de checkout.
{% endalert %}

Para completar esses objetivos, siga estas etapas:

## Etapa 1: Crie um aplicativo de site Braze {#step-1}

No Braze, vá para **Configurações** > **Configurações do App** > e então selecione **Adicionar App**. Nomeie o aplicativo como "Shopify".

{% alert warning %}
A loja deve ser nomeada como “Shopify” ou a integração pode não funcionar corretamente.
{% endalert %}

## Etapa 2: Adicione subdomínio e variáveis ambientais {#step-2}

1. Configure seu subdomínio Shopify para [redirecionar o tráfego da sua loja online para o Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic/).  
2. Adicione um [URI de retorno de chamada](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) para login. (O URI será adicionado automaticamente quando o domínio for adicionado.)
3. Configure suas [variáveis ambientais Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable):
  - Crie duas variáveis ambientais usando os valores do aplicativo do site que você criou em [Etapa 1](#step-1).
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

## Etapa 3: Ativar rastreamento no local

A primeira etapa é inicializar o SDK Web da Braze. Recomendamos fazer isso instalando nosso pacote NPM:

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
A versão do SDK Web da Braze deve ser 5.4.0.
{% endalert %}

Em seguida, [inclua esta configuração]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) como uma chave de nível superior no seu `vite.config.js` arquivo:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Após instalar o pacote NPM, você deve inicializar o SDK dentro de um `useEffect` hook dentro do componente `Layout`. Dependendo da sua versão do Hydrogen, este componente pode estar localizado no arquivo `root.jsx` ou `layout.jsx`:

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

Os valores `data.brazeApiKey` e `data.brazeApiUrl` precisam ser incluídos no carregador de componentes usando as variáveis ambientais criadas em [Etapa 2](#step-2):

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
As políticas de segurança de conteúdo (geralmente localizadas no arquivo `entry.server.jsx` Hydrogen) podem impactar a funcionalidade dos scripts da Braze tanto em ambientes locais quanto de produção. Sugerimos testar através de builds de prévia enviadas para Shopify através do Oxygen ou implantações personalizadas. Se você encontrar problemas, precisará configurar seu CSP para permitir que nosso JavaScript funcione.
{% endalert %}

## Etapa 4: Adicione um evento de login da conta Shopify 

Rastreie quando um comprador faz login em sua conta e sincroniza suas informações de usuário com o Braze. Isso inclui chamar nosso método `changeUser` para identificar clientes com um ID externo do Braze. 

{% alert note %}
Atualmente, não temos orientações para suportar um ID externo do Braze personalizado. Se você precisar disso para sua integração agora, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

Antes de começar, certifique-se de que você configurou os URIs de retorno de chamada para que o login do cliente funcione dentro do Hydrogen. Para saber mais, consulte [Usando a API de Conta do Cliente com o Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Após configurar os URIs de retorno de chamada, defina uma função para chamar o SDK do Braze. Crie um novo arquivo (como `Tracking.jsx`) e importe-o de seus componentes:

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
2\. No mesmo hook `useEffect` que inicializa o SDK do Braze, adicione a chamada para esta função:

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
3\. Recupere o endereço de e-mail e o número de telefone do cliente em sua consulta GraphQL da API do Cliente, localizada no arquivo `app/graphql/customer-account/CustomerDetailsQuery.js`:

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
4\. Por fim, carregue os dados do cliente em sua função de carregamento:

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

## Etapa 5: Adicione rastreamento para eventos de Produto Visualizado e Carrinho Atualizado

### Eventos de Produto Visualizado

1. Adicione esta função ao seu arquivo `Tracking.jsx`:

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
2\. Para chamar a função anterior sempre que um usuário visitar uma página de produto, adicione um hook `useEffect` ao componente Produto dentro do arquivo `app/routes/products.$handle.jsx`:

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
3\. Adicione o valor para “storefrontUrl” (porque não está no carregador do componente por padrão):

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

### Eventos de Carrinho Atualizado

Além de rastrear o evento `cart_updated`, você precisa enviar o valor do token do carrinho para o Braze. Usamos o valor do token do carrinho para processar webhooks de pedidos recebidos do Shopify. Isso é feito criando um alias de usuário com o token do carrinho do Shopify como seu nome. 

1. Defina funções para rastreamento do evento `cart_updated` e configuração do token do carrinho:

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
2\. Retorne o objeto `cart` da ação fetcher para que o Braze possa acessar suas propriedades acessando seu arquivo `app/routes/cart.jsx` e adicionando o seguinte ao `action`
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
3\. As lojas Hydrogen geralmente definem um componente `CartForm` que gerencia o estado do objeto do carrinho, que é usado ao adicionar, remover e alterar a quantidade de itens em um carrinho. Adicione outro hook `useEffect` no componente `AddToCartButton` que chamará a função `trackCartUpdated` sempre que o estado do fetcher do formulário mudar (sempre que o carrinho do usuário for atualizado):

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
4\. Use o mesmo `fetcherKey` para as ações responsáveis por atualizar um produto existente no seu carrinho. Adicione o seguinte aos componentes `CartLineRemoveButton` e `CartLineUpdateButton` (localizados por padrão no arquivo `app/components/CartLineItem.jsx`):

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

## Etapa 6: Instale a integração Braze Shopify

### Etapa 6.1: Conecte sua loja da Shopify

Acessar a página de parceiros do Shopify para iniciar sua configuração. Primeiro, selecione **Iniciar Configuração** para instalar o aplicativo Braze da Shopify App Store. Siga os passos guiados para concluir o processo de instalação.

![Página de configuração da integração Shopify no dashboard do Braze.][2]

### Etapa 6.2: Ativar os SDKs da Braze 

Para lojas Shopify Hydrogen ou headless, selecione a opção **Configuração personalizada**. 

Antes de continuar com o processo de integração, confirme que você ativou o SDK do Braze em seu site Shopify.

![Etapa de configuração para ativar os SDKs do Braze.][3]

### Etapa 6.3: Rastrear dados da Shopify 

Aprimore sua integração adicionando mais eventos e atributos do Shopify, que serão alimentados por webhooks do Shopify. Para informações detalhadas sobre os dados rastreados por meio desta integração, consulte [Recursos de Dados do Shopify]({{site.baseurl}}/shopify_data_features/). 

![Etapa de configuração para rastrear dados do Shopify.][4]

### Etapa 6.4: Preenchimento histórico (opcional)

Através da configuração personalizada, você tem a opção de carregar seus clientes e pedidos do Shopify dos últimos 90 dias antes de conectar sua integração Shopify. Para incluir essa carga inicial de dados, marque a caixa para a opção de carga inicial de dados.

Se você preferir realizar o preenchimento posterior, pode concluir a configuração inicial agora e retornar a esta etapa mais tarde.

![Seção para configurar o preenchimento de dados históricos.][5]

Esta tabela contém os dados que serão carregados inicialmente através do preenchimento.

| Eventos recomendados pela Braze | Eventos personalizados da Shopify | Atribuições padrão do Braze | Status de inscrição da Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Pedido realizado</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Nome</li><li>Sobrenome</li><li>Telefone</li><li>Cidade</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li>Inscrições de marketing por e-mail associadas a esta loja Shopify</li><li>Inscrições de marketing por SMS associadas a esta loja Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Etapa 6.5: Configuração de rastreamento de dados personalizados (avançado) 

Com os SDKs da Braze, você pode rastrear eventos personalizados ou atributos personalizados que vão além dos dados suportados para esta integração. Eventos personalizados capturam interações únicas em sua loja, como:

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

O SDK deve ser inicializado (ouvindo a atividade) no dispositivo de um usuário para registrar eventos ou atributos personalizados. Para saber mais sobre como registrar dados personalizados, consulte [Objeto do usuário](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) e [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Etapa 6.6: Configure como você gerencia usuários (opcional)

Primeiro, selecione seu `external_id` no menu suspenso. 

Seção ![“Coletar assinantes”][6].

{% alert important %}
Usar um endereço de e-mail ou um endereço de e-mail hash como seu ID externo do Braze pode ajudar a simplificar a gestão de identidade entre suas fontes de dados. No entanto, é importante considerar os riscos potenciais à privacidade do usuário e à segurança dos dados.<br><br>

- **Informações Adivinháveis:** Os endereços de e-mail são facilmente adivinháveis, o que os torna vulneráveis a ataques.
- **Risco de Exploração:** Se um usuário mal-intencionado alterar seu navegador da Internet para enviar o endereço de e-mail de outra pessoa como sua ID externa, ele poderá acessar mensagens confidenciais ou informações de conta.
{% endalert %}

Em segundo lugar, você tem a opção de coletar suas aceitações de marketing por e-mail ou SMS do Shopify. 

Se você usar os canais de e-mail ou SMS, pode sincronizar seus estados de aceitação de marketing por e-mail e SMS no Braze. Se você sincronizar as aceitações de marketing por e-mail do Shopify, o Braze criará automaticamente um grupo de inscrições para e-mail para todos os usuários associados a essa loja específica. Você precisa criar um nome único para este grupo de inscrições.

Seção ![“Coletar assinantes” com opção de coletar aceitações de marketing por e-mail ou SMS.][9]

{% alert note %}
Como mencionado em [visão geral do Shopify]({{site.baseurl}}/shopify_overview/), se você quiser usar um formulário de captura de terceiros, seus desenvolvedores precisam integrar o código do SDK do Braze. Isso permitirá que você capture o endereço de e-mail e o status global de inscrição por e-mail a partir das submissões do formulário. Especificamente, você precisa implementar e testar esses métodos no seu arquivo `theme.liquid`:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Define o endereço de e-mail no perfil do usuário
- [definirTipoDeInscriçãoDeNotificaçãoPorEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Atualiza o status global de inscrição por e-mail
{% endalert %}

### Etapa 6.7: Sincronizar produtos (opcional)

Você pode sincronizar todos os produtos da sua loja Shopify para um catálogo Braze para uma personalização de mensagens mais profunda. As atualizações automáticas ocorrem em quase tempo real, para que seu catálogo sempre reflita os detalhes mais recentes dos produtos. Para saber mais, confira [sincronização de produtos Shopify]({{site.baseurl}}/shopify_catalogs/).

![Etapa de configuração para sincronizar dados de produtos com Braze.][7]

### Etapa 6.8: Ativar canais

Para ativar mensagens no aplicativo, Cartões de Conteúdo e Flags de Recursos usando a integração direta do Shopify, adicione cada canal ao seu SDK. Siga os links da documentação fornecidos para cada canal abaixo:

- **Mensagens no aplicativo:** Para habilitar mensagens no aplicativo para casos de uso de formulários de captura de leads, consulte [Mensagens no aplicativo]({{site.baseurl}}/developer_guide/in_app_messages/).
- **Cartões de conteúdo:** Para habilitar Cartões de Conteúdo para casos de uso de banner de caixa de entrada ou site, consulte [Cartões de Conteúdo]({{site.baseurl}}/developer_guide/content_cards/).
- **Flags de recursos:** Para habilitar Flags de Recursos para casos de uso de experimentação no site, consulte [Flags de recursos]({{site.baseurl}}/developer_guide/feature_flags/).

### Etapa 6.9: Concluir configuração

Depois de passar por todas as etapas, selecione **Concluir Configuração** para retornar à página do parceiro. Em seguida, ative a incorporação do aplicativo Braze na sua página de administração do Shopify, conforme indicado pelo banner que é exibido.

![Banner que diz para ativar a incorporação do aplicativo Braze no Shopify para que você possa concluir a configuração da sua integração.][8]

### Exemplo de código

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) é um exemplo de app Hydrogen que contém todo o código abordado nas etapas anteriores. 

[1]: {% image_buster /assets/img/Shopify/add_new_app.png %}
[2]: {% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %}
[3]: {% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %}
[4]: {% image_buster /assets/img/Shopify/track_shopify_data_setup.png %}
[5]: {% image_buster /assets/img/Shopify/historical_backfill_setup.png %}
[6]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[7]: {% image_buster /assets/img/Shopify/sync_product_data.png %}
[8]: {% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %}
[9]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}