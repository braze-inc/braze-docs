---
nav_title: Shopify カスタム統合設定
article_title: "Shopify カスタム統合設定"
description: "この参考記事では、カスタムストアフロントを使用してShopify Hydrogen ストアやヘッドレス Shopify ストアに接続する方法を説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Shopify カスタム統合設定

> このページでは、カスタムストアフロントを使用して、Shopify Hydrogen ストアやヘッドレス Shopify ストアと Braze を統合する方法を説明します。

このガイドでは、Shopify の Hydrogen フレームワークを例にしています。ただし、ブランドが「ヘッドレス」フロントエンド設定でストアのバックエンドに Shopify を使用している場合も、同様のアプローチをとることができます。  

Shopify のヘッドレスストアを Braze と統合するには、以下の2つの目標を達成する必要があります。

1. **Braze Web SDK を初期化してロードし、オンサイトトラッキングを有効にする**<br><br> 手動で Shopify Web サイトにコードを追加して、Braze オンサイトトラッキングを有効にします。Shopify ヘッドレスストアに Braze SDK を実装することで、セッション、匿名のユーザー行動、チェックアウト前のショッパーアクション、そして開発チームと一緒に選択した[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)や[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)を含むオンサイトアクティビティをトラッキングできます。また、アプリ内メッセージやコンテンツカードなど、SDK がサポートするチャネルを追加することもできます。 

{: start="2"}
2. **Braze の Shopify 統合をインストールする**<br><br> Shopify ストアを Braze に接続すると、Shopify の Webhook を通じて顧客、チェックアウト、注文、商品データにアクセスできるようになります。

{% alert important %}
統合を開始する前に、Shopify ストアフロントのチェックアウトサブドメインが正しく設定されていることを確認してください。詳細については、[Migrate from the online store to Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate) を参照してください。<br><br> この設定が正しく行われないと、Braze は Shopify チェックアウト Webhook を処理できません。また、ローカルの開発環境で統合をテストすることもできません。ストアフロントとチェックアウトページ間の共有ドメインに依存しているためです。
{% endalert %}

これらの目標を達成するには、以下のステップに従ってください。

## Braze Web SDK を初期化してロードする

### ステップ 1: Braze Web サイトアプリを作成する {#step-1}

Braze で、[**設定**] > [**アプリの設定**] に移動し、[**アプリの追加**] を選択します。アプリ名に「Shopify」と入力します。

{% alert warning %}
ショップ名は「Shopify」にする必要があります。そうしないと、統合が適切に機能しない場合があります。
{% endalert %}

### ステップ 2: サブドメインおよび環境変数の追加 {#step-2}

1. Shopify サブドメインを[オンラインストアから Hydrogen にトラフィックをリダイレクト](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic)するように設定します。  
2. ログイン用の[コールバック URI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) を追加します。（ドメインが追加されると、URI は自動的に追加されます。）
3. [Shopify 環境変数](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable)を設定します。
  - [ステップ 1](#step-1) で作成した Web サイトアプリの値を使用して、次の 2 つの環境変数を作成します。
    - `BRAZE_API_KEY` 
    - `BRAZE_API_URL`

### ステップ 3: オンサイトトラッキングを有効にする

まず、Braze Web SDK を初期化します。NPM パッケージをインストールすることをお勧めします。

```java
npm install --save @braze/web-sdk@5.4.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
Braze Web SDK バージョンは 5.4.0 である必要があります。
{% endalert %}

次に、最上位キーとして[この設定]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)を `vite.config.js` ファイルに含めます。

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

NPM パッケージをインストールした後、`Layout` コンポーネント内部の `useEffect` フック内で SDK を初期化する必要があります。Hydrogen のバージョンに応じて、このコンポーネントは `root.jsx` または `layout.jsx` のいずれかのファイルにあります。

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
コンテンツセキュリティポリシー（通常は `entry.server.jsx` Hydrogen ファイルにある）は、ローカル環境でも本番環境でも、Braze スクリプトの機能に影響を与える可能性があります。Oxygen またはカスタムデプロイメントを介して Shopify に送信されるプレビュービルドでテストすることをお勧めします。問題が発生した場合は、CSP を設定して JavaScript が機能するようにする必要があります。
{% endalert %}

### ステップ 4: Shopify アカウントログインイベントの追加 

買い物客がアカウントにサインインし、ユーザー情報を Braze に同期したタイミングを追跡します。これには、`changeUser` メソッドを呼び出して、Braze external ID で顧客を識別することが含まれます。 

{% alert note %}
現在のところ、カスタム Braze external ID をサポートするガイダンスはありません。統合にこれが必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

開始する前に、Hydrogen 内で顧客ログインが動作するようにコールバック URI が設定されていることを確認してください。詳細については、[Using the Customer Account API with Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen) を参照してください。

1. コールバック URI を設定した後、Braze SDK を呼び出す関数を定義します。新しいファイル（`Tracking.jsx` など）を作成し、コンポーネントからインポートします。

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
2. Braze SDK を初期化するのと同じ `useEffect` フックで、この関数の呼び出しを追加します。

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
3. ファイル `app/graphql/customer-account/CustomerDetailsQuery.js` にある Customer API GraphQL クエリで、顧客のメールアドレスと電話番号を取得します。

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
4. 最後に、ローダー関数で顧客データを読み込みます。

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
2. ユーザーが製品ページにアクセスするたびにこの関数を呼び出すには、ファイル `app/routes/products.$handle.jsx` 内の Product コンポーネントに `useEffect` フックを追加します。

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
3. 「storefrontUrl」の値を追加します（デフォルトではコンポーネントローダーに含まれていないため）。

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

#### カート更新イベント

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

1. `cart_updated` イベントを追跡し、カートトークンを設定する関数を定義します。

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
2. フェッチャーアクションから `cart` オブジェクトを返し、Braze がそのプロパティにアクセスできるようにします。`app/routes/cart.jsx` ファイルに移動して、`action` 関数に以下を追加します。

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
3. Hydrogen ストアは通常、カートオブジェクトの状態を管理する `CartForm` コンポーネントを定義します。このコンポーネントは、カート内のアイテムの追加、削除、数量の変更時に使用されます。フォームフェッチャーの状態が変わるたびに（ユーザーカートが更新されるたびに）`trackCartUpdated` 関数を呼び出す `useEffect` フックを `AddToCartButton` コンポーネントに追加します。

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
4. カートから既存の製品を更新するアクションには、同じ `fetcherKey` を使用します。`CartLineRemoveButton` と `CartLineUpdateButton` コンポーネント（デフォルトではファイル `app/components/CartLineItem.jsx` にある）に以下を追加します。

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

Shopify パートナーページに移動して設定を開始します。まず、[**Begin Setup**] を選択し、Shopify App Store から Braze アプリケーションをインストールします。ガイドの手順に従って、インストールプロセスを完了します。

![Braze ダッシュボードの Shopify 統合設定ページ。]({% image_buster /assets/img/Shopify/braze_shopify_integration_page.png %})

### ステップ 2: Braze SDK を有効にする 

Shopify Hydrogen またはヘッドレスストアの場合は、[**カスタム設定**] オプションを選択します。 

オンボーディングプロセスを続行する前に、Shopify Web サイトで Braze SDK が有効になっていることを確認してください。

![Braze SDK を有効にする設定ステップ。]({% image_buster /assets/img/Shopify/enable_braze_sdks_setup.png %})

### ステップ 3: Shopify データを追跡する 

Shopify の Webhook を利用する Shopify イベントと属性をさらに追加することで、統合を強化します。この統合で追跡されるデータの詳細については、[Shopify Data Features]({{site.baseurl}}/shopify_data_features/) を参照してください。 

![Shopify データ追跡の設定ステップ。]({% image_buster /assets/img/Shopify/track_shopify_data_setup.png %})

### ステップ 4: 履歴バックフィル（オプション）

カスタム設定を通じて、Shopify 統合を接続する前の過去 90 日間の Shopify 顧客と注文を読み込むオプションがあります。この初期データ読み込みを含めるには、初期データ読み込みオプションのチェックボックスをオンにします。

後でバックフィルを実行する場合は、ここで初期セットアップを完了し、後からこのステップに戻ることができます。

![履歴データのバックフィルを設定するセクション。]({% image_buster /assets/img/Shopify/historical_backfill_setup.png %})

この表には、バックフィルによって最初に読み込まれるデータが掲載されています。

| Braze 推奨イベント | Shopify カスタムイベント | Braze の標準属性項目 | Braze サブスクリプションステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>行われた注文</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | {::nomarkdown}<ul><li>この Shopify ストアに関連付けられたメールマーケティングサブスクリプション</li><li>この Shopify ストアに関連付けられた SMS マーケティングサブスクリプション</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### ステップ 5: カスタムデータトラッキングの設定（上級） 

Braze SDK を使用すると、この統合でサポートされているデータを超えるカスタムイベントやカスタム属性を追跡できます。カスタムイベントは、以下のようなストアでの固有のインタラクションをキャプチャします。

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

イベントやカスタム属性をログに記録するには、SDK がユーザーのデバイス上で初期化（アクティビティをリッスン）されている必要があります。カスタムデータのロギングについては、[User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) と [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) を参照してください。

### ステップ 6: ユーザーの管理方法の設定（オプション） {#step-6}

ドロップダウンから `external_id` タイプを選択します。

![「サブスクライバーの収集」セクション。]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
メールアドレスまたはハッシュ化されたメールアドレスを Braze external ID として使用することで、データソース全体での ID 管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測可能な情報:** メールアドレスは推測されやすく、攻撃に対して脆弱です。
- **悪用のリスク:** 悪意のあるユーザーが Web ブラウザーを改ざんし、他人のメールアドレスを external ID として送信した場合、機密メッセージやアカウント情報にアクセスされる可能性があります。
{% endalert %}

デフォルトでは、Braze は Shopify から取得したメールを自動的に小文字に変換してから external ID として使用します。メールまたはハッシュメールを external ID として使用している場合は、external ID として割り当てる前、または他のデータソースからハッシュする前に、メールアドレスも小文字に変換されていることを確認してください。これにより、external ID の不一致を防ぎ、Braze での重複ユーザープロファイルの作成を回避できます。

{% alert note %}
次のステップは、external ID の選択によって異なります。<br><br>
- **カスタム external ID タイプを選択した場合:** ステップ 6.1〜6.3 を実行して、カスタム external ID の設定を行います。
- **Shopify 顧客 ID、メール、またはハッシュメールを選択した場合:** ステップ 6.1〜6.3 をスキップし、ステップ 6.4 に直接進みます。
{% endalert %}

#### ステップ 6.1: `braze.external_id` メタフィールドを作成する

1. Shopify の管理パネルで、**Settings** > **Metafields** に移動します。
2. **Customers** > **Add definition** を選択します。
3. **Namespace and key** に `braze.external_id` と入力します。
4. **Type** で **ID Type** を選択します。

メタフィールドが作成されたら、顧客に対して値を入力します。次のアプローチをお勧めします。

- **顧客作成 Webhook をリッスンする:** [`customer/create` イベント](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)をリッスンする Webhook を設定します。これにより、新しい顧客の作成時にメタフィールドを書き込むことができます。
- **既存の顧客をバックフィルする:** [Admin API](https://shopify.dev/docs/api/admin-graphql) または [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) を使用して、以前に作成した顧客のメタフィールドをバックフィルします。

#### ステップ 6.2: external ID を取得するエンドポイントを作成する

Braze が external ID を取得するために呼び出せる公開エンドポイントを作成する必要があります。これにより、Shopify が `braze.external_id` メタフィールドを直接提供できないシナリオでも、Braze が ID を取得できます。

##### エンドポイント仕様

**メソッド:** GET

Braze は、次のパラメーターをエンドポイントに送信します。

| パラメーター            | 必須 | データタイプ | 説明                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | はい      | 文字列    | Shopify 顧客 ID。                                         |
| shopify_storefront   | はい      | 文字列    | リクエストのストアフロント名。例: `<storefront_name>.myshopify.com` |
| email_address        | いいえ       | 文字列    | ログインユーザーのメールアドレス。<br><br>このフィールドは、特定の Webhook シナリオでは欠落している場合があります。エンドポイントロジックでは、ここで null 値を考慮する必要があります（たとえば、内部ロジックで必要な場合は shopify_customer_id を使用してメールを取得します）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### サンプルエンドポイント

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```


##### 期待される応答
Braze は、external ID の JSON を返す `200` ステータスコードを期待します。
```json
{
  "external_id": "my_external_id"
}
```

##### 検証

`shopify_customer_id` と `email_address`（存在する場合）が Shopify の顧客値と一致することを検証することが重要です。[Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) または [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) を使用してこれらのパラメーターを検証し、正しい `braze.external_id` メタフィールドを取得できます。

##### 失敗時の動作とマージ
`200` 以外のステータスコードは失敗と見なされます。

- **マージへの影響:** エンドポイントが失敗した場合（`200` 以外を返す、またはタイムアウトした場合）、Braze は external ID を取得できません。そのため、Shopify ユーザーと Braze ユーザープロファイル間のマージは、その時点では行われません。
- **再試行ロジック:** Braze は標準的な即時ネットワーク再試行を試みますが、失敗が続く場合、マージは次の該当イベントまで延期されます（たとえば、次回ユーザーがプロファイルを更新するか、チェックアウトを完了したとき）。
- **サポート性:** タイムリーなユーザーマージに対応するには、エンドポイントの高可用性を確保し、オプションの `email_address` フィールドを適切に処理するようにしてください。

#### ステップ 6.3: external ID を入力する

[ステップ 6](#step-6) を繰り返し、Braze の external ID タイプとしてカスタム external ID を選択した後、エンドポイント URL を入力します。

##### 考慮事項

- Braze がエンドポイントにリクエストを送信したときに external ID が生成されていない場合、`changeUser` 関数が呼び出されると、統合はデフォルトで Shopify 顧客 ID を使用します。このステップは、匿名ユーザープロファイルと識別済みユーザープロファイルをマージするために重要です。そのため、一時的にワークスペース内にさまざまなタイプの external ID が存在する場合があります。
- external ID が `braze.external_id` メタフィールドで使用可能な場合、統合はこの external ID を優先して割り当てます。 
    - 以前に Shopify 顧客 ID が Braze external ID として設定されていた場合は、`braze.external_id` メタフィールドの値に置き換えられます。 

#### ステップ 6.4: Shopify からメールや SMS のオプトインを収集する（オプション）

Shopify からメールまたは SMS マーケティングのオプトインを収集するオプションもあります。 

メールや SMS チャネルを使用している場合、メールや SMS マーケティングのオプトイン状態を Braze に同期できます。Shopify からメールマーケティングオプトインを同期すると、Braze はその特定のストアに関連付けられたすべてのユーザーのメールサブスクリプショングループを自動的に作成します。このサブスクリプショングループに一意の名前を作成する必要があります。

![「サブスクライバーの収集」セクションで、メールまたは SMS マーケティングのオプトインを収集するオプションがあります。]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
[Shopify 概要]({{site.baseurl}}/shopify_overview/)で説明されているように、サードパーティ製のキャプチャフォームを使用する場合は、開発者が Braze SDK コードを統合する必要があります。これにより、フォーム送信からメールアドレスとグローバルメールサブスクリプションステータスをキャプチャできます。具体的には、`theme.liquid` ファイルに以下のメソッドを実装してテストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): ユーザープロファイルにメールアドレスを設定します
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): グローバルメールサブスクリプションステータスを更新します
{% endalert %}

### ステップ 7: 製品を同期する（オプション）

Shopify ストアの全商品を Braze カタログに同期し、より詳細なメッセージングのパーソナライゼーションを実現できます。自動更新はほぼリアルタイムで行われるため、カタログには常に最新の商品詳細が反映されます。詳細については、[Shopify product sync]({{site.baseurl}}/shopify_catalogs/) を参照してください。

![商品データを Braze に同期する設定ステップ。]({% image_buster /assets/img/Shopify/sync_product_data.png %})

### ステップ 8: チャネルを有効にする

Shopify 直接統合を使用してアプリ内メッセージ、コンテンツカード、およびフィーチャーフラグを有効にするには、各チャネルを SDK に追加します。以下の各チャネルのドキュメントリンクに従ってください。

- **アプリ内メッセージ:** リード獲得フォームのユースケースでアプリ内メッセージを有効にするには、[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/)を参照してください。
- **コンテンツカード:** 受信トレイや Web サイトバナーのユースケースでコンテンツカードを有効にするには、[コンテンツカード]({{site.baseurl}}/developer_guide/content_cards/)を参照してください。
- **フィーチャーフラグ:** サイト実験のユースケースでフィーチャーフラグを有効にするには、[フィーチャーフラグ]({{site.baseurl}}/developer_guide/feature_flags/)を参照してください。

### ステップ 9: 設定を完了する

すべてのステップを終えたら、[**設定を終了**] を選択してパートナーページに戻ります。次に、表示されるバナーの指示に従って、Shopify 管理ページで Braze アプリの埋め込みを有効にします。

![統合の設定を完了するために、Shopify で Braze アプリの埋め込みを有効にするよう促すバナー。]({% image_buster /assets/img/Shopify/shopify_app_embed_banner.png %})

#### サンプルコード

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) は、前のステップで説明したすべてのコードを含む Hydrogen アプリの例です。