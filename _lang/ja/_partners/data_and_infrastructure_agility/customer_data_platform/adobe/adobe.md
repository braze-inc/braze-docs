---
nav_title: Adobe
article_title: Adobe
description: "このリファレンス記事では、Braze と顧客データプラットフォーム であるAdobe との提携について説明します。これにより、ブランドは、Adobe データ(カスタム属性 s およびSegment s) をリアルタイムでBrazeに接続し、マップできます。そうすれば、ブランドはこの情報に基づいて行動し、パーソナライズされたなターゲットを絞った体験をユーザーに提供することができる。"
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Adobe Experience プラットフォームに基づいて構築されたAdobeのリアルタイム顧客データプラットフォームは、企業が複数のエンタープライズソースからの既知の匿名データをまとめて顧客 プロファイルを作成するのに役立ちます。これらのプロファイルを使用すると、すべてのチャネルおよび機器にリアルタイムでパーソナライズされた体験を提供できます。

Braze とAdobe CDP インテグレーションを使用すると、ブランドはAdobe データ(カスタム属性 s およびSegment s) をリアルタイムでBrazeに接続してマッピングできます。そうすれば、ブランドはこの情報に基づいて行動し、パーソナライズされたなターゲットを絞った体験をユーザーに提供することができる。Adobeでは、統合は直感的です。Adobe [identity](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) を使用して、Brazeの外部ID にマッピングし、Braze プラットフォームに送信するだけです。送信されるすべてのデータは、新しい`AdobeExperiencePlatformSegments` 属性を介してBrazeでアクセスできます。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| Adobeアカウント | この提携の事前タグを行うには、[Adobeアカウント](https://account.adobe.com/)が必要です。 |
| Braze REST API キー | `users.track` 権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Brazeインスタンス | Brazeインスタンスは、Braze オンボーディング マネージャーから取得するか、[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints) にあります。 |
| Braze REST エンドポイント | REST エンドポイントのURL。エンドポイントは、インスタンス の[ Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
追加のカスタム属性s を送信すると、データポイント使用量が増えることに注意してください。この潜在的なデータポイント上昇をより良く理解するために、あなたの顧客サクセスマネージャーと話すことをお勧めします。
{% endalert %}

## 統合

### ステップ1:Braze 送信先の設定

Adobe **Settings**ページで、**Destinations**を**Collections**から選択します。そこから、**Braze**タイルを見つけ、**Configure**を選択します。 

![][1]

{% alert note %}
Braze との接続がすでに存在する場合は、送信先 カードに**Activate** が表示されます。activateとconfigureの違いについては、Adobe 送信先 ワークスペース [ドキュメント](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog)のカタログを参照してください。
{% endalert %}

### ステップ2:Braze トークンの提供

**アカウント**ステップで、Braze API キーを入力し、**送信先**に接続します。

![][3]{: style="max-width:60%"}

### ステップ3:認証

次に、**Authentication**ステップで、Brazeコネクションの詳細を入力する必要があります。
- **名前**:今後この送信先を認識したい名前を入力します。
- **宛先**:この送信先の識別に役立つ説明を入力します。
- **エンドポイントインスタンス**:Braze エンドポイントを入力します。
- **販売ユースケース**:マーケティングユースケースは、データを送信先にエクスポートする目的を示します。Adobe定義のマーケティング ユースケースから選択するか、独自のマーケティング ユースケースを作成できます。Adobe マーケティング ユースケース sの詳細については、Adobe Experience Platformの[データガバナンスを参照してください。

![][4]{: style="max-width:60%;"}

### ステップ4:送信先の作成
**送信先の作成**を押します。送信先が作成されました。**Save & Exit** をクリックしてSegment s 以降を有効にするか、**Next** をクリックしてワークフローを続行し、Segment s を選択して有効にします。 

### ステップ 5: Segmentの有効化
Braze 送信先にs をアプリすることで、Adobe リアルタイムCDP にあるデータを有効にします。

次の一覧では、Segmentを有効にするために必要な全般的なステップを示します。Adobe Segment s とSegmentアクティベーションワークフローの詳細なガイダンスについては、[Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites) をご覧ください。

1. Braze 送信先を選択して有効にします。
2. アプリライセンス可能Segmentsを選択します。
4. エクスポートするSegmentごとにスケジュールとファイル名を設定します。
5. Brazeに送信する属性sを選択します。
6. アクティベーションを確認して確認します。

### ステップ 6: 照射野mのアプリ値

Adobe Experience Platform からBraze にオーディエンスを正しく送信するには、フィールド m アプリ の実行ステップを完了する必要があります。Mアプリingは、Adobe Experienceデータモデルフィールドsと対応するBraze プラットフォーム フィールドsの間にリンクを作成します。

1. m アプリ ing ステップで、**新しいm アプリを追加**を選択します。<br>![][5]{: style="max-width:50%;"}<br><br>
2. ソースフィールド部分で、空のフィールドの横にある矢印ボタンをクリックすると、ソースフィールドの選択ウィンドウが開封されます。<br>![][6]<br><br>
3. このウィンドウでは、Adobe 属性 s を選択してBraze 属性s にマップする必要があります。<br>![][7]{: style="max-width:70%;"}<br><br>次に、ID ネームスペースを選択する必要があります。この項目は、プラットフォーム ID ネームスペースをBraze ネームスペースにマップするために使用されます。<br>![][8]{: style="max-width:80%;"}<br> 入力フィールドを選択し、****を選択します。<br><br>
4. 対象フィールドで、フィールドの横にあるmアプリのアイコンを選択します。<br>![][9]{: style="max-width:90%;"}<br><br>
5. ターゲットフィールドの選択ウィンドウで、ターゲットフィールドs の3つのカテゴリから選択できます。<br><br>• **アイデンティティ名前空間を選択**:このオプションを使用して、プラットフォームアイデンティティネームスペースをBrazeアイデンティティネームスペースにマップします。<br>• **カスタム属性を選択s**:このオプションを使用して、Adobe XDM 属性s をBraze アカウントで定義したカスタムBraze 属性s にマップします。<br><br>![][10]{: style="max-width:60%;"}<br><br>**また、XDM 属性の名前をBrazeに変更することもできます。**たとえば、`lastname` XDM 属性をカスタム`Last_Name` 属性にBrazeでm アプリすると、`Last_Name` 属性がまだ存在しない場合はBraze で作成され、`lastname` XDM 属性がマップされます。<br><br> 目的のフィールドsを選択し、**Select**をクリックします。<br><br>
6. これで、一覧にフィールドm アプリが表示されます。<br>![][11]<br><br>
7. さらにm個のアプリを追加するには、必要に応じてステップ1～6を繰り返します。 

## ユースケース

たとえば、XDM プロファイル スキーマとBrazeインスタンスに次の属性s とID が含まれているとします。

|     | XDM プロファイルスキーマ | Brazeインスタンス |
| --- | ------------------ | -------------- |
| 属性 | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| ID | - `Email`<br>\- Google Ad ID (`GAID`)<br>\- Apple ID Advertisers 用(`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

正しいm アプリ ing は次のようになります。

![デスティネーションm アプリ:IdentityMap:IDFA m がIdentityMap:external_id にアプリしたIdentityMap:external_id:GAID m アプリがIdentityMap:external_id、IdentityMap:email m アプリがIdentityMap:external_id、xdm:mobilePhone.number m アプリがカスタム属性:電話番号、xdm:person.name.lastName m カスタム属性:FirstName に設定されたAtrribute:LastName、xdm:<meta id="4"][12]

## エクスポートされたデータ
Braze に正常にエクスポートされたかどうかを確認するには、Braze アカウントを確認します。Adobe Experience Platform Segmentは、`AdobeExperiencePlatformSegments`属性でBrazeにエクスポートされます。

## データの使用とガバナンス
すべてのAdobe Experience Platform 送信先は、データの処理時にデータ使用ポリシーに準拠しています。Adobe Experience Platform によるデータガバナンスの実施方法の詳細については、[リアルタイムCDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en)のデータガバナンスを参照してください。 

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