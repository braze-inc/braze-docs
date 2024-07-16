---
nav_title: Amplitude
article_title:Amplitude コホートインポート
description:「この参考記事では、製品分析およびビジネスインテリジェンスプラットフォームであるAmplitude のコホートインポート機能について概説しています。「
page_type: partner
search_tag:Partner
---

# Amplitude コホートインポート

> この記事では、[ユーザーコホートをAmplitude](https://amplitude.com/) からBrazeにインポートする方法について説明します。[Amplitude とその他の機能の統合について詳しくは、AAmplitude のメイン記事を参照してください。]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/)

## データインポート統合

{% multi_lang_include video.html id="8a57e44be7da423e9699cedd6c241eae" source="loom"%}

設定したインテグレーションはすべて、アカウントデータポイント量に加算されます。

### ステップ1:Braze データインポートキーを取得

**Braze で \[**パートナー統合] > \[**テクノロジーパートナー****] に移動し、\[Amplitude] を選択します。**ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

生成したら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーと REST エンドポイントは、ステップで Amplitude のダッシュボードでポストバック設定するときに使用されます。<br><br>![] ({% image_buster /assets/img/amplitude3.png %})

### ステップ2:Amplitude で Braze インテグレーションをセットアップする

Amplitude で、\[**ソースとデスティネーション**] > **\[プロジェクト名] > \[**デスティネーション**]** > \[**Braze**] に移動します。表示されるプロンプトで、Braze データインポートキーと REST エンドポイントを入力し、\[**保存**] をクリックします。

![] ({% image_buster /assets/img/amplitude.png %})

### ステップ3:Amplitude コホートを Braze にエクスポート

まず、Amplitude からBrazeにユーザーをエクスポートするには、[エクスポートしたいユーザーのコホートを作成します](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts)。Amplitude は、次の識別子を使用してコホートをBrazeに同期できます。
- ユーザーエイリアス
- デバイス ID
- ユーザ ID (外部 ID)

コホートを作成したら、「**Sync** to...」をクリックします。これらのユーザーを Braze にエクスポートします。

#### 同期頻度の定義

コホート同期は、1 回限りの同期、毎日または毎時、または毎分更新されるリアルタイム同期に設定できます。[データポイントの消費にも注意しながら]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/)、ビジネスニーズに合ったオプションを選択してください。

### ステップ 4:Braze のセグメントユーザー

**Brazeでこれらのユーザーのセグメントを作成するには、「**エンゲージメント**」の下の「Segment」に移動し、Segment に名前を付け、フィルターとして「**Amplitude Chorts**」を選択します。**次に、「含む」オプションを使用して、Amplitude で作成したコホートを選択します。 

![In the Braze segment builder, the filter "amplitude_cohorts" is set to "includes_value" and "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

保存したら、キャンバスまたはキャンペーン作成時にユーザーをターゲット設定するステップでこのSegment を参照できます。