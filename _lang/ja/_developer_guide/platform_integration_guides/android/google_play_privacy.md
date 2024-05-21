---
nav_title: Google Play プライバシーアンケート
article_title: Google Play ストアのプライバシーに関する質問に対する回答
page_order: 9
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Google Play のプライバシーに関する質問への回答方法について説明します。"

---
<style>
table td {
    word-break: break-word;
}
</style>

# Google Play プライバシーアンケート

> 2022年4月現在、Android 開発者は、プライバシーとセキュリティの方針を開示するために、Google Play の[データセーフティフォーム][4]に記入する必要があります。このガイドでは、Braze によるアプリデータの処理方法に関する情報をこの新しいフォームに記入する方法について説明します。 

アプリ開発者は、どのデータを Braze に送信するかを制御しています。Braze が受け取ったデータは、指示に従って処理されます。これは、Google が[サービスプロバイダー][3]として分類したものです。 

{% alert important %}
この記事では、Google のセーフティセクションのアンケートについて、Braze SDK により処理されるデータに関連する情報を提供します。この記事は法律上のアドバイスを提供していないため、Google に情報を提出する前に、法務チームに相談することをお勧めします。
{% endalert %}

## 質問

|質問|Braze SDK の回答|
|---|---|
|アプリは必要なユーザーデータタイプのいずれかを収集または共有していますか?|はい、Braze Android SDK はアプリ開発者によって設定されたデータを収集しています。|
|アプリによって収集されたすべてのユーザーデータが転送中に暗号化されていますか?|はい。|
|ユーザーがデータの削除を要求する方法を提供していますか?|はい。|

データおよび削除に対するユーザー要求の処理の詳細については、[Braze データのリテンション情報][1]を参照してください。

## データ収集

Braze によって収集されるデータは、特定の統合と収集するユーザーデータによって決まります。デフォルトで収集されるデータの詳細、および特定の属性を無効にする方法については、[SDK データ収集オプション][5]を参照してください。

<table id="datatypes">
    <thead>
        <tr>
            <th width="25%">カテゴリー</th>
            <th width="25%">データタイプ</th>
            <th width="50%">Braze 使用状況</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">位置情報</td>
            <td>だいたいの位置情報</td>
            <td rowspan="15">デフォルトでは収集されません。</td>
        </tr>
        <tr>
            <td>正確な位置情報</td>
        </tr>
        <tr>
            <td rowspan="9">個人情報</td>
            <td>名前</td>
        </tr>
        <tr>
            <td>メールアドレス</td>
        </tr>
        <tr>
            <td>ユーザー ID</td>
        </tr>
        <tr>
            <td>住所</td>
        </tr>
        <tr>
            <td>電話番号</td>
        </tr>
        <tr>
            <td>人種と民族</td>
        </tr>
        <tr>
            <td>政治的または宗教的信条</td>
        </tr>
        <tr>
            <td>性的指向</td>
        </tr>
        <tr>
            <td>その他の情報</td>
        </tr>
        <tr>
            <td rowspan="4">財務情報</td>
            <td>ユーザー決済情報</td>
        </tr>
        <tr>
            <td>購入履歴</td>
        </tr>
        <tr>
            <td>クレジットスコア</td>
        </tr>
        <tr>
            <td>その他財務情報</td>      
        </tr>
        <tr>
            <td rowspan="2">ヘルスとフィットネス</td>
            <td>ヘルス情報</td>
            <td rowspan="2">デフォルトでは収集されません。</td>
        </tr>
        <tr>
            <td>フィットネス情報</td>     
        </tr>
        <tr>
            <td rowspan="3">メッセージ</td>
            <td>メール</td>
            <td rowspan="2">デフォルトでは収集されません。</td>
        </tr>
        <tr>
            <td>SMS または MMS</td>          
        </tr>
        <tr>
            <td>その他のアプリ内メッセージ</td>
            <td>Braze を通じてアプリ内メッセージを送信したり、プッシュ通知を送信する場合、ユーザがこれらのメッセージをいつ開いたか、またはいつ読んだかに関する情報を収集します。</td>
        </tr>
        <tr>
            <td rowspan="2">写真と動画</td>
            <td>写真</td>
            <td rowspan="8">収集されません。</td>
        </tr>
        <tr>
            <td>ビデオ</td>
        </tr>
        <tr>
            <td rowspan="3">オーディオファイル</td>
            <td>音声やサウンドの録音</td>
        </tr>        
        <tr>
            <td>音楽ファイル</td>
        </tr>
        <tr>
            <td>その他のオーディオファイル</td>
        </tr>
        <tr>
            <td>ファイルとドキュメント</td>
            <td>ファイルとドキュメント</td>
        </tr>
        <tr>
            <td>カレンダー</td>
            <td>カレンダーイベント</td>
        </tr>
        <tr>
            <td>連絡先</td>
            <td>連絡先</td>
        </tr>
        <tr>
            <td rowspan="5">アプリアクティビティ</td>
            <td>アプリのインタラクション</td>
            <td>Braze は、デフォルトでセッションアクティビティデータを収集します。他のすべてのインタラクションとアクティビティは、アプリのカスタム統合によって決定されます。</td>
        </tr>
        <tr>
            <td>アプリ内検索履歴</td>
            <td>収集されません。</td>            
        </tr>
        <tr>
            <td>インストール済みアプリ</td>
            <td>収集されません。</td>            
        </tr>
        <tr>
            <td>その他のユーザー生成コンテンツ</td>
            <td rowspan="2">デフォルトでは収集されません。</td>            
        </tr>
        <tr>
            <td>その他のアクション</td>
        </tr>
        <tr>
            <td>Web ブラウジング</td>
            <td>Web 閲覧履歴</td>
            <td>収集されません。</td>
        </tr>
        <tr>
            <td rowspan="3">アプリの情報とパフォーマンス</td>
            <td>クラッシュログ</td>
            <td>Braze は、SDK 内で発生したエラーのクラッシュログを収集します。これには、ユーザの電話機モデルと OS レベル、および Braze 固有のユーザ ID が含まれます。</td>
        </tr>
        <tr>
            <td>診断</td>
            <td>収集されません。</td>            
        </tr>
        <tr>
            <td>その他のアプリパフォーマンスデータ</td>
            <td>収集されません。</td>
        </tr>
        <tr>
            <td>デバイスまたはその他の ID</td>
            <td>デバイスまたはその他の ID</td>
            <td>Braze は、ユーザーのデバイスを区別するためにデバイス ID を生成し、メッセージが意図したデバイスに送信されるかどうかをチェックします。</td>
        </tr>
    </tbody>
</table>

Google Play のデータセーフティガイドラインの対象外となる可能性がある Braze が収集するその他のデバイスデータの詳細については、[Android ストレージの概要][2]および [SDK データ収集オプション][5]を参照してください。

[1]: {{site.baseurl}}/api/data_retention/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/storage
[3]: https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform
[4]: https://support.google.com/googleplay/android-developer/answer/10787469
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration