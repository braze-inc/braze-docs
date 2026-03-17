{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## トラッキングを無効にする

データ収集を無効にするには、メソッド`disableSDK`を使用する。このメソッドを呼び出した後、Braze SDKはBrazeサーバーへのデータ送信を停止する。

```javascript
Braze.disableSDK();
```

## データトラッキングを再開する

データ収集を無効化した後に再開するには、メソッド`enableSDK`を使用する。

```javascript
Braze.enableSDK();
```

## データを消去する

デバイス上にローカル保存されているBraze SDKデータを全て削除するには、\``wipeData`deleteAllData`メソッドを使用する。このメソッドを呼び出した後、SDKは無効化される。再度イネーブルメントするには\`.\`を使用する必要がある`enableSDK`。

```javascript
Braze.wipeData();
```

## データをフラッシュする

保留中のデータを直ちにBrazeサーバーに送信するには、を使用する`requestImmediateDataFlush`。

```javascript
Braze.requestImmediateDataFlush();
```

## 広告トラッキングのイネーブルメント

この端末で広告トラッキングのイネーブルメントが有効かどうかをBrazeに通知するには、\``setAdTrackingEnabled``メソッドを使用する。SDKはこのデータを自動的に収集しない。

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

二つ目のパラメータはGoogle広告IDであり、Androidでのみ使用される。

## トラッキングプロパティの許可リストを更新する（iOSのみ）

トラッキング用に宣言されたデータ型のリストを更新するには、. を使用する`updateTrackingPropertyAllowList`。これはAndroidでは何もしない操作だ。

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

詳細については、[プライバシー・マニフェスト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/)を参照せよ。
