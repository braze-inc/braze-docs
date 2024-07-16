---
nav_title: Adobe
article_title:Adobe
description:「この参考記事では、Brazeと顧客データプラットフォームであるAdobeのパートナーシップについて概説しています。これにより、ブランドはアドビのデータ（カスタム属性とセグメント）をBrazeにリアルタイムで接続してマッピングできます。その後、ブランドはこのデータに基づいて行動を起こし、パーソナライズされたターゲットを絞ったエクスペリエンスをそれらのユーザーに提供できます。「
page_type: partner
page_order:1
search_tag:Partner

---

# Adobe

> Adobe Experience Platform上に構築されたアドビのリアルタイム顧客データプラットフォームは、企業が複数の企業ソースからの既知のデータと匿名データをまとめて顧客プロファイルを作成するのに役立ちます。その後、これらのプロファイルを使用して、すべてのチャネルとデバイスでパーソナライズされたエクスペリエンスをリアルタイムで提供できます。

BrazeとAdobe CDPの統合により、ブランドはアドビのデータ（カスタム属性とセグメント）をBrazeにリアルタイムで接続してマッピングできます。その後、ブランドはこのデータに基づいて行動を起こし、パーソナライズされたターゲットを絞ったエクスペリエンスをそれらのユーザーに提供できます。アドビでは、統合は直感的に行えます。[アドビの任意のIDを取得し](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en)、それをBraze外部IDにマッピングして、Brazeプラットフォームに送信するだけです。送信されたすべてのデータには、`AdobeExperiencePlatformSegments`新しい属性を使用してBrazeでアクセスできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Adobeアカウント | このパートナーシップを利用するには、[アドビアカウントが必要です](https://account.adobe.com/)。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Brazeインスタンス | Brazeインスタンスは Braze オンボーディングマネージャーから入手するか、[API]({{site.baseurl}}/api/basics/#endpoints) 概要ページにあります。 |
| Braze REST エンドポイント | あなたの REST エンドポイント URL。エンドポイントは、[インスタンスの Braze URL]({{site.baseurl}}/api/basics/#endpoints) によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
追加のカスタム属性を送信すると、データポイント使用量増えることに注意してください。この潜在的なデータポイントの増加をよりよく理解するために、顧客サクセスマネージャーに相談することをお勧めします。
{% endalert %}

## 統合

### ステップ1:Braze 送信先の設定

Adobe **設定ページから**、「**コレクション**」の「**宛先**」を選択します。そこから、**Braze** タイルを見つけて「**設定**」を選択します。 

![][1]

{% alert note %}
Braze との接続が既に存在する場合は、接続送信先カードに **Activate** ボタンが表示されます。アクティベートとコンフィグの違いについて詳しくは、アドビの送信先ワークスペース[ドキュメントのカタログセクションを参照してください](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog)。
{% endalert %}

### ステップ2:Braze トークン提供

**アカウントステップで** Braze API キーを入力し、\[**送信先に接続**] をクリックします。

![][3]{: style="max-width:60%"}

### ステップ3:認証

次に、**認証ステップで**、Braze 接続の詳細を入力する必要があります。
- **名前**:今後この送信先を認識させたい名前を入力してください。
- **目的地**:この送信先識別に役立つ説明を入力してください。
- **エンドポイントインスタンス**:Braze エンドポイントインスタンスを入力します。
- **マーケティングのユースケース**:マーケティングのユースケースは、データを送信先にエクスポートする目的を示します。アドビが定義したマーケティングユースケースから選択することも、独自のマーケティングユースケースを作成することもできます。アドビのマーケティングユースケースについて詳しくは、Adobe Experience [Platformのデータガバナンスをご覧ください](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations)。

![][4]{: style="max-width:60%;"}

### ステップ 4:送信先作成
\[**送信先を作成**] をクリックします。送信先が作成されました。「**保存して終了**」をクリックして後でセグメントをアクティブ化するか、「**次へ**」をクリックしてワークフローを続行し、有効にするセグメントを選択できます。 

### ステップ 5: セグメントをアクティブ化
セグメントを Braze 送信先にマッピングして、Adobe リアルタイム CDP にあるデータを有効にします。

以下のリストは、Segment をアクティブ化するために必要な一般的な手順をまとめたものです。アドビセグメントとSegment アクティベーションワークフローの詳細なガイダンスについては、[アドビをご覧ください](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites)。

1. Braze 送信先を選択してアクティブにします。
2. 該当するセグメントを選択します。
4. エクスポートする各Segment のスケジュールとファイル名を設定します。
5. Braze に送信する属性を選択します。
6. アクティベーションを確認して確認します。

### ステップ 6: フィールドマッピング

Adobe Experience PlatformからBrazeにオーディエンスデータを正しく送信するには、フィールドマッピングのステップを完了する必要があります。マッピングにより、Adobe Experience データモデルフィールドと対応する Braze プラットフォームフィールドとの間にリンクが作成されます。

1. マッピングステップで、「**新規マッピングを追加**」をクリックします。<br>![][5]{: style="max-width:50%;"}<br><br>
2. ソースフィールドセクションで、空のフィールドフィールドの横にある矢印ボタンをクリックします。これにより、ソースフィールド選択ウィンドウが開きます。<br>![][6]<br><br>
3. このウィンドウで、Braze 属性にマップするアドビ属性を選択する必要があります。<br>![][7]{: style="max-width:70%;"}<br><br>次に、ID 名前空間を選択する必要があります。このオプションは、プラットフォームID名前空間をBraze名前空間にマップするために使用されます。<br>![][8]{: style="max-width:80%;"}<br> ソースフィールドを選択し、\[**選択**] をクリックします。<br><br>
4. ターゲットフィールドセクションで、フィールド横にあるマッピングアイコンをクリックします。<br>![][9]{: style="max-width:90%;"}<br><br>
5. 「ターゲットフィールドを選択」ウィンドウでは、ターゲットフィールドの 3 つのカテゴリから選択できます。<br><br>• **アイデンティティー名前空間の選択**:このオプションを使用して、プラットフォームID名前空間をBrazeID名前空間にマップします。<br>• **カスタム属性を選択**:このオプションを使用して、Adobe XDM 属性を Braze アカウントで定義したカスタム Braze 属性にマップします。<br><br>![][10]{: style="max-width:60%;"}<br><br>**このオプションを使用して、既存の XDM アトリビュートの名前を Braze に変更することもできます。**たとえば、`lastname` XDM 属性を Braze `Last_Name` のカスタム属性にマッピングすると、`Last_Name`その属性性がまだ存在しない場合は Braze に作成され、`lastname` XDM 属性それにマップされます。<br><br> ターゲットフィールドを選択し、\[**選択**] をクリックします。<br><br>
6. これで、リストにフィールドマッピングが表示されます。<br>![][11]<br><br>
7. さらにマッピングを追加するには、必要に応じて手順 1 ～ 6 を繰り返します。 

## ユースケース

XDM プロファイルスキーマと Brazeインスタンスに次の属性とアイデンティティが含まれているとします。

|     | XDM プロファイルスキーマ | Brazeインスタンス |
| --- | ------------------ | -------------- |
| 属性 | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| アイデンティティ | - `Email`<br>-グーグル広告 ID (`GAID`)<br>-広告主様向けApple ID () `IDFA` | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

正しいマッピングは次のようになります。

![デスティネーションマッピング:IdentityMap:IDFA が Identity Map: external_ID にマップされている IDFA、IdentityMap: External_ID、Identity Map: Email Map: Identity Map にマップされた電子メール:external_ID, xDM: mobilePhone. カスタム属性にマップされた番号:電話番号, XDM: Person.name. CustomAttribute にマップされた姓:姓, LastName, XDM: Person.Name。カスタム属性にマップされた名前:FirstName][12]

## エクスポートされたデータ
データが Braze に正常にエクスポートされたかどうかを確認するには、Braze アカウントを確認してください。アドビエクスペリエンスプラットフォームセグメントは、`AdobeExperiencePlatformSegments`この属性で Braze にエクスポートされます。

## データ使用とガバナンス
Adobe Experience Platformのすべての宛先は、データを処理する際のデータ使用ポリシーに準拠しています。Adobe Experience [Platformがデータガバナンスを実施する方法について詳しくは、「リアルタイムCDPにおけるデータガバナンス](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en)」を参照してください。 

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