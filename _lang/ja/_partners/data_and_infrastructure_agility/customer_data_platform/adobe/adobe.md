---
nav_title: Adobe
article_title: Adobe
description: "このページでは、顧客データプラットフォームであるBraze とAdobe のパートナーシップの概要を説明します。これにより、ブランドは自身のAdobe データ(カスタム属性とセグメント)をリアルタイムでBraze に接続し、マップできます。そうすれば、ブランドはこの情報に基づいて行動し、パーソナライズされたなターゲットを絞った体験をユーザーに提供することができる。"
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Adobe Experience Platform に構築されているAdobe のリアルタイムカスタマーデータプラットフォームは、複数のエンタープライズソースからの既知の匿名データをまとめてカスタマープロファイルを作成します。その後、これらのプロファイルを使用して、パーソナライズされたエクスペリエンスをすべてのチャネルおよびデバイスでリアルタイムで提供できます。

Braze とAdobe CDP の統合により、ブランドのAdobe データ(カスタム属性とセグメント) がリアルタイムでBraze に接続され、マッピングされます。その後、このデータに基づいて行動し、ユーザーにパーソナライズされたターゲットを絞った体験を提供できます。Adobeでは、統合は直感的です。Adobe の任意の [ID](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) を Braze の external ID にマッピングし、Braze プラットフォームに送信するだけです。Braze では、新しい `AdobeExperiencePlatformSegments` 属性を使用して、送信されるすべてのデータにアクセスできます。

{% alert important %}
Adobe Experience Platform 統合では、現在、動的なオーディエンスメンバーシップはサポートされていません。つまり、ユーザープロファイルには値を追加できますが、削除することはできません。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Adobeアカウント | このパートナーシップを活用するには、[Adobe アカウント](https://account.adobe.com/)が必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Brazeインスタンス | Brazeインスタンスは、Braze オンボーディング マネージャーから取得するか、[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints) にあります。 |
| Braze REST エンドポイント | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
追加のカスタム属性を送信すると、データポイントの使用量が増加します。この潜在的なデータポイントの増加をよりよく理解するために、カスタマーサクセスマネージャーと話すことをお勧めします。
{% endalert %}

## 統合

### ステップ1:Braze 宛先を設定する

Adobe **Settings**ページで、**Destinations**を**Collections**から選択します。そこから、**Braze**タイルを見つけ、**Configure**を選択します。 

![][1]

{% alert note %}
Braze との接続がすでに存在する場合は、宛先カードに**Activate** ボタンが表示されます。[Activate] と [Configure] の違いの詳細については、Adobe 宛先ワークスペースの[ドキュメント](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog)の「カタログ」セクションを参照してください。
{% endalert %}

### ステップ2:Braze トークンの提供

**アカウント**ステップで、Braze APIキーを入力し、**接続先**を選択します。

![][3]{: style="max-width:60%"}

### ステップ3:認証

次に、**Authentication**ステップで、ブレーズ接続の詳細を入力します。
- **Name**:今後この宛先を認識したい名前を入力します。
- **Destination**:この宛先を特定するのに役立つ説明を入力します。
- **エンドポイントインスタンス**:Braze エンドポイントを入力します。
- **マーケティングユースケース**:マーケティングユースケースは、データを送信先にエクスポートする目的を示します。Adobe定義のマーケティング ユースケースから選択するか、独自のマーケティング ユースケースを作成できます。Adobe マーケティングユースケースの詳細については、[Adobe Experience Platform のデータガバナンス](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations)を参照してください。

![][4]{: style="max-width:60%;"}

### ステップ4:宛先を作成する
**Create destination**を選択します。宛先が作成されました。You can select **Save & Exit** to activate segments later or **Next** to continue the workflow and select segments to activate. 

### ステップ 5: Segmentの有効化
Adobe Real-Time CDP で使用しているデータをアクティブにするには、セグメントを Braze 宛先にマッピングします。

次の一覧では、Segmentを有効にするために必要な全般的なステップを示します。Adobe のセグメントとセグメントアクティベーションワークフローの詳細なガイダンスについては、[Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites) を参照してください。

1. Braze 宛先を選択してアクティブ化します。
2. 該当するセグメントを選択します。
4. エクスポートするSegmentごとにスケジュールとファイル名を設定します。
5. Brazeに送信する属性sを選択します。
6. アクティベーションを確認します。

### ステップ 6: フィールドマッピング

Adobe Experience Platform から Braze にオーディエンスデータを正しく送信するには、フィールドマッピングステップを完了する必要があります。マッピングにより、Adobe Experience データモデルのフィールドと対応する Braze プラットフォームのフィールドの間にリンクが作成されます。

1. マッピングステップで、**Add new mapping** を選択します。<br>![][5]{: style="max-width:50%;"}<br><br>
2. ソースフィールドセクションで、空のフィールドの横にある矢印ボタンを選択して、ソースの選択フィールドウィンドウを開きます。<br>![][6]<br><br>
3. ウィンドウでAdobe 属性を選択し、ブレーズ属性にマップします。<br>![][7]{: style="max-width:70%;"}<br><br>次に、ID ネームスペースを選択します。この項目は、プラットフォーム ID ネームスペースをBraze ネームスペースにマップするために使用されます。<br>![][8]{: style="max-width:80%;"}<br> ソースフィールドを選択し、****を選択します。<br><br>
4. ターゲットフィールドセクションで、フィールドの横にあるマッピングアイコンを選択します。<br>![][9]{: style="max-width:90%;"}<br><br>
5. ターゲットフィールド選択ウィンドウでは、ターゲットフィールドの3つのカテゴリから選択できます。<br><br>• **Select identity namespace**:Platform の ID 名前空間を Braze の ID 名前空間にマッピングするには、このオプションを使用します。<br>• **Select custom attributes**:Adobe XDM 属性を、Braze アカウントで定義したカスタム Braze 属性にマッピングするには、このオプションを使用します。<br><br>![][10]{: style="max-width:60%;"}<br><br>**このオプションを使用して、既存の XDM 属性の名前を Braze で変更することもできます。**たとえば、XDM 属性 `lastname` を Braze のカスタム属性 `Last_Name` にマッピングすると、Braze に属性 `Last_Name` がまだ存在しない場合はこの属性が作成され、XDM 属性 `lastname` がそれにマッピングされます。<br><br> ターゲットフィールドを選択し、****を選択します。<br><br>
6. フィールドマッピングがリストに表示されます。<br>![][11]<br><br>
7. マッピングをさらに追加するには、必要に応じて手順1～6を繰り返します。 

## ユースケース

たとえば、XDM プロファイル スキーマとBrazeインスタンスに次の属性s とID が含まれているとします。

|     | XDM プロファイルスキーマ | Brazeインスタンス |
| --- | ------------------ | -------------- |
| 属性 | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| ID | - `Email`<br>\- Google 広告 ID (`GAID`)<br>\- Apple ID Advertisers 用(`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

正しいマッピングは次のようになります。

![宛先マッピング:IdentityMap:IDFA が IdentityMap:external_id に、IdentityMap:GAID が IdentityMap:external_id に、IdentityMap:Email が IdentityMap:external_id に、xdm:mobilePhone.number が CustomAttribute:PhoneNumber に、xdm:person.name.lastName が CustomAtrribute:LastName に、xdm:person.name.firstName が CustomAttribute:FirstName にマッピングされている][12]

## エクスポートされたデータ
データが正常に Braze にエクスポートされたかどうかを確認するには、Braze アカウントをチェックします。Adobe Experience Platform Segmentは、`AdobeExperiencePlatformSegments`属性でBrazeにエクスポートされます。

## データの使用とガバナンス
データの処理時に、Adobe Experience Platform のすべての宛先はデータ使用ポリシーに準拠します。Adobe Experience Platform によるデータガバナンスの実施方法の詳細については、[Real-Time CDP のデータガバナンス](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en)を参照してください。 

[1]: {% image_buster /assets/img/adobe/braze-destination-configure.png %}
[3]: {% image_buster /assets/img/adobe/braze-destination-account.png %}
[4]: {% image_buster /assets/img/adobe/braze-destination-authentication.png %}
[5]: {% image_buster /assets/img/adobe/braze-destination-mapping.png %}
[6]: {% image_buster /assets/img/adobe/braze-destination-mapping-source.png %}
[7]: {% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}
[8]: {% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}
[9]: {% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}
[10]: {% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}
[11]: {% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %}
[12]: {% image_buster /assets/img/adobe/braze-destination-mapping-example.png %} 