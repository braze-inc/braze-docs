---
nav_title: FAQ
article_title: よくある質問
page_order: 50
description: "このページにはフィーチャーフラグに関するよくある質問とその回答を掲載しています。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# よくある質問

> この記事ではフィーチャーフラグに関するよくある質問にお答えします。

## 機能性とサポート

### Brazeの機能フラッグはどのプラットフォームでサポートされているのか？ {#platforms}

Braze は、以下の SDK バージョン要件で iOS、Android、および Web プラットフォームでフィーチャーフラグをサポートします。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

他のプラットフォームでのサポートが必要か？Eメール：[feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### フィーチャーフラグを実装するときに必要となる作業のレベルはどれくらいですか? {#level-of-effort}

フィーチャーフラグは数分で作成し、統合できます。 

必要な作業のほとんどは、ロールアウトを計画している新機能を構築する開発チームに関連するものです。しかし、機能フラグを追加するとなると、アプリやウェブサイトのコードに`IF`/`ELSE` ステートメントを記述するくらい簡単だ：

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

### 機能フラグはマーケティングチームにどのようなメリットをもたらすのか？ {#marketing-teams}

マーケティングチームは、ある機能がごく一部のユーザーにしか有効でない場合、機能フラグを使用して製品アナウンス（製品発表メールなど）を調整することができる。

例えば、Braze のフィーチャーフラグを使えば、アプリ内の10%のユーザーに新しいカスタマーロイヤルティプログラムをロールアウトし、キャンバスのフィーチャーフラグのステップを使って、同じ10%の有効なユーザーにメールやプッシュなどのメッセージングを送ることができます。 

### 機能フラグは製品チームにどのようなメリットをもたらすのか？ {#product-teams}

製品チームは、フィーチャーフラグを使用して、新機能の段階的なロールアウトやソフトローンチを行い、重要業績評価指標や顧客からのフィードバックをモニターしてから、全ユーザーに提供することができます。

製品チームは、[機能フラグのプロパティを]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties)使用して、ディープリンク、テキスト、画像、その他の動的コンテンツなど、アプリ内のコンテンツをリモートで入力することができる。

キャンバスのフィーチャーフラッグステップを使って、製品チームはA/Bスプリットテストを実施し、新機能が、その機能を無効にしたユーザーと比較して、コンバージョン率にどのような影響を与えるかを測定することもできる。 

### フィーチャー・フラッグはエンジニアリング・チームにどのようなメリットをもたらすのか？ {#engineering-teams}

エンジニアリングチームは、機能フラグを使用することで、新機能の立ち上げに内在するリスクを軽減し、夜中に慌ててコード修正をデプロイすることを避けることができる。

機能フラグに隠された新しいコードをリリースすることで、チームはBrazeのダッシュボードからリモートで機能のオン/オフを切り替えることができ、新しいコードのプッシュアウトやアプリストアのアップデート承認待ちの遅延を回避できる。

## 機能のロールアウトとターゲティング

### フィーチャーフラグを一部のユーザーだけにロールアウトすることは可能ですか? {#target-users}

はい、Braze で特定のユーザーをターゲットとするセグメントを作成します (メールアドレス、`user_id`、またはユーザープロファイルのその他の属性で対象を指定)。次に、そのセグメントの100%に対してフィーチャーフラグをロールアウトします。

### ロールアウト率を調整することで、以前は有効グループにバケットされていたユーザーにどのような影響があるのか？ {#random-buckets}

機能フラグのロールアウトは、デバイスやセッションを問わず、ユーザーにとって一貫したものとなる。

- あるフィーチャーフラグがランダムなユーザーの10%にロールアウトされると、その10%は有効なままになり、そのフィーチャーフラグの有効期間中は保持されます。
- ロールアウト率を10%から20%に増やすと、同じ10%が有効なままとなり、さらに新たな10%のユーザーが有効なグループに追加されます。
- ロールアウト率を20%から10%に下げると、元の10%のユーザーだけが有効なままになります。

この戦略により、アプリ内で一貫した体験がユーザーに提供され、セッション間を行ったり来たりすることがなくなります。もちろん、機能を0%まで無効にすると、すべてのユーザーがフィーチャーフラグから削除されます。これは、バグを発見した場合や、機能を完全に無効にする必要がある場合に役立ちます。

## 技術トピック

### フィーチャーフラグを使用して、Braze SDK が初期化されるタイミングをコントロールできますか? {#initialization}

いいえ、現在のユーザーのフィーチャーフラグをダウンロードして同期するには、SDK を初期化する必要があります。つまり、機能フラグを使用して、Brazeで作成または追跡されるユーザーを制限することはできない。

### SDK はどのくらいの頻度でフィーチャーフラグを更新しますか? {#refresh-frequency}

フィーチャーフラグは、セッション開始時とアクティブユーザー変更時に更新されます。フィーチャーフラグは、SDK の [refresh メソッド]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing)を使用して手動で更新することもできます。フィーチャーフラグの更新は5分に1回に制限されています (変更される可能性があります)。

優れたデータ・プラクティスでは、機能フラグをあまり早くリフレッシュしないことを推奨している（リフレッシュするとレートが制限される可能性がある）ので、ユーザーが新機能とインタラクトする前にリフレッシュするか、必要であればアプリ内で定期的にリフレッシュするのがベストであることに留意してほしい。

### ユーザーがオフラインの間、機能フラグは利用可能か？ {#offline}

機能フラグがリフレッシュされると、ユーザーの端末にローカルに保存され、オフラインの状態でもアクセスできる。

### セッションの途中でフィーチャーフラグが更新された場合はどうなりますか? {#listen-for-updates}

フィーチャーフラグはセッションの途中で更新されることがあります。特定の変数やコンフィギュレーションが変更された場合、アプリをアップデートしたくなるシナリオもあるだろう。UI のレンダリング方法の大幅な変更を避けるために、アプリを更新しない方がよい場合もあります。

これをコントロールするには、フィーチャーフラグの[更新をリッスン]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates)し、変更されたフィーチャーフラグに基づいてアプリを再レンダリングするかどうかを決定します。 

### グローバルコントロールグループのユーザーがフィーチャーフラグ実験を受信しないのはなぜですか?

[Global Control Group]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/)では、ユーザーの機能フラグを有効にすることはできません。これは、グローバルコントロールグループのユーザーもフィーチャーフラグ実験に参加できないことを意味します。

## その他の質問は？

ご質問やフィードバックはありますか?Eメール：[feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

