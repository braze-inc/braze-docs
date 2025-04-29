---
nav_title: Shopify カスタム統合設定
article_title: "Shopify カスタム統合設定"
description: "このリファレンス記事では、Shopify Hydrogen ストアまたはカスタムストアフロントを使用したヘッドレスShopify ストアとの接続方法について説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 2
toc_headers: h2
---

# Shopifyカスタム統合設定

> このページでは、カスタムストアフロントを使用して、Braze をShopify Hydrogen ストアまたはヘッドレスShopify ストアと統合する方法について説明します。

このガイドでは、Shopify のHydrogen フレームワークを例として使用します。ただし、ブランドが"headless"フロントエンド設定で店舗のバックエンドにShopifyを使用している場合も、同様のアプローチをとることができます。  

Shopify ヘッドレスストアをBraze と統合するには、次の2 つの目標を達成する必要があります。

1. **Braze Web SDKを初期化してロードし、オンサイトトラッキングを有効にします**<br><br> 手動でShopify Web サイトにコードを追加して、Braze オンサイトのトラッキングを有効にします。Shopify ヘッドレスストアにBraze SDK を実装することで、セッション、匿名ユーザーの動作、ショッパーの事前チェックアウトアクション、および開発チームに含めることを選択した[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) または[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) などのオンサイトアクティビティを追跡できます。また、アプリ内メッセージやコンテンツカードなど、SDK でサポートされているチャネルを追加することもできます。 

{: start="2"}
2\.**お店をBraze ネイティブ統合に接続します**<br><br> Shopify ストアをBraze に接続すると、Shopify ウェブフックを使用して、顧客、チェックアウト、注文、製品データにアクセスできます。

{% alert important %}
統合を開始する前に、Shopify ストアフロントのチェックアウトサブドメインが正しく設定されていることを確認します。詳細については、[オンラインストアから水素への移行](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate)を参照してください。<br><br> この設定が正しく行われない場合、Braze はShopify チェックアウトWebhook を処理できません。また、ローカル開発環境で統合をテストすることもできません。これは、ストアフロントとチェックアウトページの間の共有ドメインに依存しているためです。
{% endalert %}

これらの目標を達成するには、次の手順に従います。

## ステップ1:ブレーズウェブサイトアプリを作成する {#step-1}

ブレーズで、**Settings** > **App Settings** > に移動し、**App** を追加を選択します。アプリに"Shopify" という名前を付けます。

{% alert warning %}
ショップ名は「Shopify」にする必要があります。そうしないと、統合が適切に機能しない場合があります。
{% endalert %}

## ステップ2: サブドメインおよび環境変数の追加 {#step-2}

1. Shopifyサブドメインを[オンラインストアからHydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic/)にトラフィックをリダイレクトするように設定します。  
2. ログイン用に[コールバックURI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) を追加します。(ドメインが追加されると、自動的にURI が追加されます。)
3. [Shopify環境変数](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable)を設定します。
  - [ステップ1](#step-1) で作成したウェブサイトアプリの値を使用して、2 つの環境変数を作成します。
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

## ステップ 3:オンサイトトラッキングを有効にする

まず、Braze Web SDK を初期化します。NPMパッケージをインストールすることをお勧めします。

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
Braze Web SDK バージョンは5.4.0 である必要があります。
{% endalert %}

次に、[この設定]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) を最上位キーとして`vite.config.js` ファイルに含めます。

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

NPMパッケージをインストールした後、`useEffect`フック内の`Layout`コンポーネント内でSDKを初期化する必要があります。Hydrogen のバージョンに応じて、このコンポーネントは`root.jsx` または`layout.jsx` ファイルのいずれかにあります。

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

[ステップ2](#step-2)で作成した環境変数を使用して、`data.brazeApiKey`と`data.brazeApiUrl`の値をコンポーネントローダーに含める必要があります。

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
コンテンツセキュリティポリシー(通常は`entry.server.jsx` Hydrogen ファイルにあります) は、ローカル環境と本番環境の両方でBraze スクリプトの機能に影響を与える可能性があります。Oxygen またはカスタムデプロイメントを介してShopify に送信されるプレビュービルドによるテストをお勧めします。問題が発生した場合は、CSP を設定してJavaScript が機能するようにする必要があります。
{% endalert %}

## ステップ 4:Shopifyアカウントログインイベントの追加 

買い物客が自分のアカウントにサインインし、自分のユーザー情報をBrazeに同期した時点を追跡します。これには、`changeUser` メソッドを呼び出して、ブレーズ外部ID で顧客を識別することも含まれます。 

{% alert note %}
現在、カスタムのろう付け外部IDをサポートするためのガイダンスはありません。統合に必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

開始する前に、顧客ログインがHydrogen 内で動作するようにコールバックURI を設定していることを確認してください。詳細については、[水素を使用したカスタマーアカウントAPI の使用](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen)を参照してください。

1. コールバックURI を設定した後、Braze SDK を呼び出す関数を定義します。新しいファイル(`Tracking.jsx` など) を作成し、コンポーネントからインポートします。

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
2\.Braze SDK を初期化する同じ`useEffect` フックで、この関数の呼び出しを追加します。

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
3\.`app/graphql/customer-account/CustomerDetailsQuery.js` ファイルにあるCustomer API GraphQL クエリで顧客のメールアドレスと電話番号を取得します。

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
4\.最後に、ローダー関数でカスタマーデータをロードします。

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

## ステップ 5: Product Viewed およびCart Updated イベントのトラッキングの追加

### 製品ビューイベント

1. この関数を`Tracking.jsx` ファイルに追加します。

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
2\.ユーザが製品ページにアクセスするたびに以前の関数を呼び出すには、`useEffect` フックをファイル`app/routes/products.$handle.jsx` 内の製品コンポーネントに追加します。

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
3\.「storefrontUrl」の値を追加します(デフォルトではコンポーネントローダーにはないため)。

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

### カート更新イベント

`cart_updated` イベントの追跡に加えて、カートトークン値をBraze に送信する必要があります。Shopifyから受け取った注文ウェブフックを処理するためにカートトークン値を使用します。これを行うには、Shopifyカートトークンを名前として使用してユーザーエイリアスを作成します。 

1. `cart_updated` イベントを追跡し、カートトークンを設定するための関数を定義します。

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
2\.フェッチャーアクションから`cart` オブジェクトを返します。これにより、Braze は`app/routes/cart.jsx` ファイルに以下を追加し、そのプロパティにアクセスできます `action`
機能:

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

Remix フェッチャーの詳細については、[useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher) を参照してください。

{: start="3"}
3\.水素ストアは通常、カートオブジェクトの状態を管理する`CartForm`コンポーネントを定義します。このコンポーネントは、カート内のアイテムの追加、削除、および数量の変更時に使用されます。`AddToCartButton` コンポーネントに別の`useEffect` フックを追加します。これにより、フォームフェッチャーの状態が変更されるたびに(ユーザーカートが更新されるたびに) `trackCartUpdated` 関数が呼び出されます。

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
4\.カートから既存の製品を更新するアクションには、同じ`fetcherKey` を使用します。以下を`CartLineRemoveButton` および`CartLineUpdateButton` コンポーネントに追加します(デフォルトでは`app/components/CartLineItem.jsx` ファイルにあります)。

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

## ステップ 6: Braze Shopify インテグレーションのインストール

### ステップ6.1：Shopify ストアを接続する

Shopify パートナーページに移動してセットアップを開始します。まず、**Begin Setup**を選択し、Shopify App StoreからBrazeアプリケーションをインストールします。ガイドの手順に従って、インストールプロセスを完了します。

![Braze ダッシュボードのShopify 統合設定ページ。][2]

### ステップ6.2：Braze SDK を有効にする 

Shopify Hydrogen またはヘッドレスストアの場合は、**Custom setup** オプションを選択します。 

オンボーディングプロセスを続行する前に、Shopify Web サイトでBraze SDK が有効になっていることを確認します。

![Braze SDK を有効にするためのセットアップ手順。][3]

### ステップ6.3：Shopify データを追跡する 

Shopify のWebhook が利用するShopify イベントと属性をさらに追加することで、統合を強化します。この統合によって追跡されるデータの詳細については、[Shopify Data Features]({{site.baseurl}}/shopify_data_features/)を参照してください。 

![Shopifyデータを追跡するためのセットアップ手順。][4]

### ステップ6.4：過去のバックフィル(オプション)

カスタム設定を使用すると、Shopify 統合を接続する前に、過去90 日間のShopify 顧客と注文をロードすることができます。この初期データロードを含めるには、初期データロードオプションのチェックボックスをオンにします。

後でバックフィルを実行する場合は、ここで初期セットアップを完了し、後でこのステップに戻ることができます。

![履歴データのバックフィルを設定するセクション。][5]

この表には、バックフィルによって最初にロードされるデータが含まれています。

| ろう付け推奨イベント | Shopify カスタムイベントs | Braze の標準属性項目 | Braze サブスクリプションステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>発注</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | {::nomarkdown}<ul><li>このShopifyストアに関連付けられたメールマーケティングサブスクリプション</li><li>Shopifyストアに関連付けられたSMSマーケティングサブスクリプション</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### ステップ6.5：カスタムデータ追跡設定(詳細) 

Braze SDK を使用すると、この統合でサポートされているデータを超えるカスタムイベントまたはカスタム属性を追跡できます。カスタムイベントは、次のような独自のインタラクションをストアにキャプチャします。

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">カスタムイベント</th>
      <th style="width: 50%;">カスタム属性</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>カスタム割引コードの使用</li>
          <li>パーソナライズされたおすすめ商品とのインタラクション</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>お気に入りのブランドまたは製品</li>
          <li>優先ショッピングカテゴリ</li>
          <li>メンバーシップまたはロイヤルティステータス</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

イベントまたはカスタム属性を記録するには、ユーザーのデバイスでSDK を初期化(アクティビティの待機) する必要があります。カスタムデータのロギングの詳細については、[User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)および[logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を参照してください。

### ステップ6.6:ユーザーの管理方法の設定(オプション)

まず、ドロップダウンから`external_id` を選択します。 

![「サブスクライバーの収集」セクション。][6]

{% alert important %}
E メールアドレスまたはハッシュされたE メールアドレスをブレーズの外部ID として使用すると、データソース全体のID 管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測できる情報:**メールアドレスは推測されやすく、攻撃されやすい。
- **搾取の危険:**悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスを外部IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性がある。
{% endalert %}

次に、ShopifyからメールまたはSMSマーケティングのオプトインを収集するオプションがあります。 

メールまたはSMS チャネルを使用する場合は、メールおよびSMS マーケティングのオプトイン状態をBraze に同期できます。Shopify からメールマーケティングオプトインを同期すると、Braze はその特定のストアに関連付けられているすべてのユーザのメールサブスクリプションググループを自動的に作成します。このサブスクリプショングループに一意の名前を作成する必要があります。

![「サブスクライバの収集」セクションで、電子メールまたはSMS マーケティングのオプトインを収集するオプションがあります。][9]

{% alert note %}
[Shopify概要]({{site.baseurl}}/shopify_overview/)で説明されているように、サードパーティ製のキャプチャフォームを使用する場合は、開発者がBraze SDK コードを統合する必要があります。これにより、フォーム送信からメールアドレスとグローバルメールサブスクリプションステータスをキャプチャできます。具体的には、`theme.liquid` ファイルにこれらのメソッドを実装してテストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail):ユーザープロファイルのメールアドレスを設定します
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype):グローバルメールサブスクリプションステータスを更新します
{% endalert %}

### ステップ6.7:同期製品(オプション)

Shopifyストアのすべての製品をBrazeカタログに同期して、より詳細なメッセージングパーソナライゼーションを行うことができます。自動更新はほぼリアルタイムで行われるため、カタログには常に最新の製品詳細が反映されます。詳しくは、[Shopify product sync]({{site.baseurl}}/shopify_catalogs/)を参照してください。

![製品データをブレーズに同期するためのセットアップ手順。][7]

### ステップ6.8:チャネルを有効にする

Shopify 直接統合を使用してアプリ内メッセージ、コンテンツカード、および機能フラグを有効にするには、各チャネルをSDK に追加します。以下の各チャンネルのマニュアルリンクに従ってください。

- **アプリ内メッセージ:**リードキャプチャフォームの使用ケースでアプリ内メッセージを有効にするには、[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/)を参照してください。
- **コンテンツカード:**受信トレイまたはウェブサイトバナーの使用ケースでコンテンツカードを有効にするには、[コンテンツカード]({{site.baseurl}}/developer_guide/content_cards/)を参照してください。
- **機能フラグ:**サイト実験の使用ケースで機能フラグを有効にするには、[機能フラグ]({{site.baseurl}}/developer_guide/feature_flags/)を参照してください。

### ステップ6.9:設定完了

すべての手順を実行したら、**Finish Setup**を選択してパートナーページに戻ります。次に、表示されるバナーに示されているように、Shopify 管理ページでBraze アプリの埋め込みを有効にします。

![Braze アプリをShopify に組み込んでアクティベートして統合の設定を完了できるようにすると言うBanner。][8]

### サンプルコード

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) は、前の手順で説明したすべてのコードを含むHydrogen アプリの例です。 

[1]: {% image_buster /assets/img/Shopify/add_new_app.png %}
[2]: {% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %}
[3]: {% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %}
[4]: {% image_buster /assets/img/Shopify/track_shopify_data_setup.png %}
[5]: {% image_buster /assets/img/Shopify/historical_backfill_setup.png %}
[6]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[7]: {% image_buster /assets/img/Shopify/sync_product_data.png %}
[8]: {% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %}
[9]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}