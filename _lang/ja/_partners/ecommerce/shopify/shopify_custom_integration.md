---
nav_title: Shopifyカスタム統合セットアップ
article_title: "Shopifyカスタム統合セットアップ"
description: "この参考記事では、カスタムストアフロントを使用してShopify Hydrogen ストアやヘッドレス Shopify ストアに接続する方法を説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 2
---

# Shopifyカスタム統合セットアップ

> このページでは、カスタムストアフロントを使用して、Shopify HydrogenストアやヘッドレスShopifyストアとBrazeを統合する方法を説明する。

このガイドでは、Shopify の Hydrogen フレームワークを例にしています。しかし、もしあなたのブランドがShopifyをバックエンドに使い、フロントエンドを "ヘッドレス "に設定しているのであれば、同様のアプローチをとることができる。  

ShopifyのヘッドレスストアをBrazeと統合するには、以下の2つの目標を達成する必要がある：

1. **Braze Web SDK を初期化してロードし、オンサイトトラッキングを有効にする**<br><br> Shopifyサイトに手動でコードを追加し、Brazeオンサイトトラッキングを有効にする。ShopifyヘッドレスストアにBraze SDKを実装することで、セッション、匿名のユーザー行動、チェックアウト前のショッパーアクション、そして開発チームと一緒に選択した[カスタムイベントや]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) [カスタム属性を]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)含むオンサイトアクティビティをトラッキングすることができます。また、アプリ内メッセージやコンテンツカードなど、SDK がサポートするチャネルを追加することもできます。 

{: start="2"}
2\.**Braze の Shopify 統合をインストールする**<br><br> ShopifyストアをBrazeに接続すると、ShopifyのWebhookを通して顧客、チェックアウト、注文、商品データにアクセスできるようになる。

{% alert important %}
統合を開始する前に、Shopify ストアフロントのチェックアウトサブドメインが正しく設定されていることを確認します。詳細については、[オンラインストアから Hydrogen への移行](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate)を参照してください。<br><br> この設定が正しく行われていないと、Braze は Shopify のチェックアウト Webhook を処理できません。また、ローカルの開発環境で統合をテストすることもできません。なぜなら、それはあなたのストアフロントとチェックアウトページ間の共有ドメインに依存しているからです。
{% endalert %}

これらの目標を達成するには、以下のステップに従ってください。

## Braze Web SDKを初期化し、読み込む。

### ステップ 1: Braze Web サイトアプリを作成する {#step-1}

Braze で、[**設定**] > [**アプリの設定**] に移動し、[**アプリの追加**] を選択します。アプリ名を「Shopify」とする。

{% alert warning %}
ショップの名前は「Shopify」でなければなりません、そうしないと統合が正しく機能しません。
{% endalert %}

### ステップ2: サブドメインと環境変数を追加する {#step-2}

1. Shopifyのサブドメインを設定し、[オンラインストアからのトラフィックをHydrogenにリダイレクトする](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic/)。  
2. ログイン用の[コールバック URI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) を追加します。(ドメインが追加されると、URI は自動的に追加されます。)
3. [Shopify の環境変数](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable)を設定します
  - [ステップ 1](#step-1) で作成した Web サイトアプリの値を使用して、2 つの環境変数を作成します。
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

### ステップ 3: オンサイトトラッキングを有効にする

最初のステップは、Braze Web SDKを初期化することである。そのためには、NPM パッケージをインストールすることをお勧めします。

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
Braze Web SDK のバージョンは 5.4.0 でなければなりません。
{% endalert %}

次に、[この設定を最上位キーとして]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) `vite.config.js` ファイルに含めます。

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

NPMパッケージをインストールした後、`Layout` コンポーネント内部の`useEffect` フック内でSDKを初期化する必要がある。Hydrogen のバージョンによって、このコンポーネントは `root.jsx` または `layout.jsx` ファイルにある場合があります。

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

[ステップ 2](#step-2) で作成した環境変数を使用して、値 `data.brazeApiKey` と `data.brazeApiUrl` をコンポーネントローダーに含める必要があります。

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
コンテンツセキュリティポリシー（通常は`entry.server.jsx` Hydrogenファイルにある）は、ローカライゼーション環境でも本番環境でも、Brazeスクリプトの機能に影響を与える可能性がある。Oxygen またはカスタムデプロイを通じて Shopify に送信されるプレビュービルドを使用してテストすることをお勧めします。問題が発生した場合は、当社の JavaScript が機能するように CSP を設定する必要があります。
{% endalert %}

### ステップ 4: Shopifyアカウントログインイベントを追加する 

買い物客がアカウントにサインインし、ユーザー情報をBrazeに同期したタイミングをトラッキング, 追跡する。これには、`changeUser` メソッドを呼び出して、Braze external ID を持つ顧客を識別することが含まれます。 

{% alert note %}
現在のところ、Brazeのカスタム外部IDをサポートするガイダンスはない。今すぐ統合にこれが必要な場合は、カスタマーサクセスマネージャーに連絡してください。
{% endalert %}

開始する前に、Hydrogen 内で動作する顧客ログインのコールバック URI が設定されていることを確認します。詳細については、[顧客アカウント API を Hydrogen で使用する](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen)を参照してください。

1. コールバックURIを設定した後、Braze SDKを呼び出す関数を定義する。新しいファイル (`Tracking.jsx` など) を作成し、コンポーネントからインポートします。

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
2\.Braze SDK を初期化するのと同じ `useEffect` フックに、この関数の呼び出しを追加します。

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
3\.ファイル `app/graphql/customer-account/CustomerDetailsQuery.js` にある顧客 API GraphQL クエリで、顧客のメールアドレスと電話番号を取得します。

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
4\.最後に、ローダー関数に顧客データを読み込みます。

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

### ステップ 5: 製品の閲覧イベントとカートの更新イベントのトラッキングを追加する

#### 製品の閲覧イベント

1. この関数を `Tracking.jsx` ファイルに追加します。

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
2\.ユーザーが製品ページにアクセスするたびに前の関数を呼び出すには、ファイル `app/routes/products.$handle.jsx` 内の製品コンポーネントに `useEffect` フックを追加します。

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
3\.storefrontUrl" の値を追加する (デフォルトではコンポーネントローダーにないため)

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

#### カート更新済みイベント

`cart_updated` イベントをトラッキングするだけでなく、カートトークンの値を Braze に送信する必要があります。Shopify から受信した注文 Webhook を処理するためにカートークンの値を使用します。これは、Shopify カートトークンを名前とするユーザーエイリアスを作成することで行います。 

1. `cart_updated` イベントをトラッキングし、カートトークンを設定する関数を定義します。

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
2\.フェッチャーアクションから `cart` オブジェクトを返し、`app/routes/cart.jsx` ファイルに移動して `action` に以下を追加することで、Braze がそのプロパティにアクセスできるようにします。
関数

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

Remix フェッチャーの詳細については、[useFetcherを](https://remix.run/docs/ja/main/hooks/use-fetcher)を参照してください。

{: start="3"}
3\.Hydrogen ストアは通常、カートオブジェクトの状態を管理する `CartForm` コンポーネントを定義します。このコンポーネントは、カート内のアイテムの追加、削除、数量の変更時に使用されます。フォームフェッチャーの状態が変わるたびに (ユーザーカートが更新されるたびに) `trackCartUpdated` 関数を呼び出す `useEffect` フックを `AddToCartButton` コンポーネントに追加します。

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
4\.カートから既存の製品を更新するアクションには、同じ `fetcherKey` を使用します。`CartLineRemoveButton` と`CartLineUpdateButton` コンポーネント (デフォルトではファイル `app/components/CartLineItem.jsx` にある) に以下を追加します。

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

## Braze の Shopify 統合をインストールする

### ステップ 1: Shopify ストアを接続する

Shopifyのパートナーページにアクセスし、セットアップを開始する。まず、[**セットアップを開始**] を選択し、Shopify アプリストアから Braze アプリをインストールします。ガイドされたステップに従ってインストールプロセスを完了します。

![Braze ダッシュボードの Shopify 統合設定ページ。]({% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %})

### ステップ2: Braze SDK を有効にする 

Shopify Hydrogen またはヘッドレスストアの場合は、[**カスタム設定**] オプションを選択します。 

オンボーディングプロセスを続ける前に、ShopifyのWebサイトでBraze SDKがイネーブルメントされていることを確認する。

![Braze SDKを有効にするためのセットアップステップ]({% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %})

### ステップ 3: Shopify データを追跡する 

ShopifyのWebhooksを利用して、Shopifyのイベントやアトリビューションを追加して、統合を強化しよう。この統合によってトラッキングされるデータの詳細情報については、[Shopify データの機能]({{site.baseurl}}/shopify_data_features/)を参照してください。 

![Shopify のデータを追跡するための設定ステップ。]({% image_buster /assets/img/Shopify/track_shopify_data_setup.png %})

### ステップ 4: 履歴バックフィル (オプション)

カスタム設定を通じて、Shopify 統合を接続する前に、過去 90 日間の Shopify の顧客と注文を読み込むオプションがあります。この初期データ読み込みを含めるには、初期データ読み込みオプションのボックスをチェックします。

後でバックフィルを実行する場合は、ここで初期設定を完了し、後でこのステップに戻ることができます。

![]({% image_buster /assets/img/Shopify/historical_backfill_setup.png %}) 履歴データバックフィルを設定するセクション。

このテーブルには、バックフィルを通して最初に読み込まれるデータが含まれています。

| Brazeおすすめイベント | Shopify カスタムイベントs | Braze の標準属性項目 | Braze のサブスクリプションステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>行われた注文</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | {::nomarkdown}<ul><li>このShopifyストアに関連するメールマーケティングのサブスクリプション</li><li>このShopifyストアに関連するSMSマーケティングサブスクリプション</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### ステップ 5: 顧客データトラッキングの設定 (高度) 

Braze SDK を使用すると、この統合でサポートされているデータを超えるカスタムイベントやカスタム属性を追跡することができます。カスタムイベントは、以下のようなストアでの固有のインタラクションをキャプチャします。

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

イベントやカスタム属性をログに記録するには、SDKがユーザーのデバイス上で初期化（アクティビティをリッスン）されている必要がある。カスタムデータのロギングについては、[ユーザーオブジェクト](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)と [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) を参照してください。

### ステップ 6: ユーザーの管理方法を設定する（オプション）

ドロップダウンから `external_id` タイプを選択します。

![「サブスクライバーの収集セクション。]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
メールアドレスまたはハッシュ化されたメールアドレスを Braze external ID として使用することで、データソース全体での ID 管理を簡素化できます。しかし、ユーザーのプライバシーやデータ・セキュリティに対する潜在的なリスクを考慮することは重要だ。<br><br>

- **推測可能な情報:**メールアドレスは推測されやすく、攻撃されやすい。
- **悪用のリスク:**悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスを外部IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性がある。
{% endalert %}

カスタム外部IDタイプを選択した場合は、ステップ6.1と6.2に進む。そうでない場合は、ステップ 6.3 に進みます。

#### ステップ6.1：カスタム `external_id` を作成する

まず、Shopifyにアクセスし、`braze.external_id` メタフィールドを作成する。[カスタムのメタフィールド記述を作成する](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions)」のステップに従うことを推奨します。**名前空間とキー**には `braze.external_id` と入力します。**タイプ**については、ID タイプを選択することをします。

メタフィールドを作成したら、[`customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) webhook をリッスンして、新しい顧客が作成されたときにメタフィールドを書き込むことができるようにします。次に、[Admin API](https://shopify.dev/docs/api/admin-graphql) または[顧客 API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) を使用して、以前に作成したすべての顧客をこのメタフィールドで埋め戻してください。

#### ステップ6.2：エンドポイントを作成する

外部IDを取得するには、パブリックなGETエンドポイントが必要だ。Shopifyがメタフィールドを提供できない場合、Brazeはそのエンドポイントを呼び出して外部IDを取得する。

エンドポイントの例: `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

##### 応答

Braze には 200 ステータスコードが想定されています。それ以外のコードはエンドポイントの失敗とみなされます。応答は次のようになるはずです。

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Admin APIまたはCustomer APIを使用して、`shopify_customer_id` 、メールアドレスを確認し、パラメータ値がShopifyの顧客値と一致していることを確認する。検証後、API を使って `braze.external_id` メタフィールドを取得し、外部 ID 値を返すこともできます。

#### ステップ6.3：ShopifyからメールまたはSMSのオプトインを収集する（オプション）

ShopifyからメールまたはSMSマーケティングのオプトインを収集するオプションがある。 

メールや SMS チャネルを使用している場合、メールや SMS マーケティングのオプトイン状態を Braze に同期させることができます。Shopifyからメールマーケティングのオプトインを同期すると、Brazeは自動的にその特定のストアに関連するすべてのユーザーのためのメールサブスクリプショングループを作成する。このサブスクリプショングループには一意な名前を作成する必要がある。

![「サブスクライバーの収集」セクションで、メールまたは SMS マーケティングのオプトインを収集するオプションがある。]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
[Shopifyの概要で]({{site.baseurl}}/shopify_overview/)述べたように、サードパーティのキャプチャフォームを使用したい場合、開発者はBraze SDKコードを統合する必要がある。これにより、フォーム送信からメールアドレスとグローバルメール購読ステータスを取得できます。具体的には、`theme.liquid` ファイルにこれらのメソッドを実装し、テストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail):ユーザープロファイルのメールアドレスを設定する
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype):グローバルメールのサブスクリプションステータスを更新する
{% endalert %}

### ステップ 7:製品を同期 (オプション)

Shopify ストアの全商品を Braze カタログに同期し、より深いメッセージングパーソナライゼーションを実現できます。自動更新はほぼリアルタイムで行われるため、カタログは常に最新の製品詳細を反映します。詳しくは、[Shopify product syncs]({{site.baseurl}}/shopify_catalogs/) を参照してください。

![Braze に商品データを同期するための設定ステップ。]({% image_buster /assets/img/Shopify/sync_product_data.png %})

### ステップ 8:チャネルを有効にする

アプリ内メッセージ、コンテンツカード、フィーチャーフラグをShopify直接統合を使用して有効にするには、SDKに各チャネルを追加する。次の各チャネルに提供されているドキュメントリンクに従ってください。

- **アプリ内メッセージ:**リード獲得フォームのユースケースでアプリ内メッセージを有効にするには、[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/)を参照してください。
- **コンテンツカード:**受信トレイや Web サイトバナーのユースケースでコンテンツカードを有効にするには、[コンテンツカード]({{site.baseurl}}/developer_guide/content_cards/)を参照してください。
- **フィーチャーフラグ:**サイト実験のユースケースでフィーチャーフラグを有効にする方法については、[フィーチャーフラグを]({{site.baseurl}}/developer_guide/feature_flags/)参照のこと。

### ステップ 9:設定完了

すべてのステップを終えたら、**設定を終了**を選択してパートナーページに戻ります。次に、Shopifyの管理ページに表示されるバナーに従って、Brazeアプリの埋め込みをイネーブルメントする。

![ShopifyでBrazeアプリの埋め込みを有効にして、統合設定を完了できるようにするバナー。]({% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %})

#### サンプルコード

[Shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) は、前のステップで説明したすべてのコードを含む Hydrogen アプリの例である。 

