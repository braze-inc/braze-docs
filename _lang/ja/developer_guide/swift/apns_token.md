Brazeを使ってiOSプッシュ通知を送信する前に、[Appleの開発者向けドキュメントに](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns)記載されているように、`.p8` プッシュ通知ファイルをアップロードする必要がある：

1. Apple 開発者アカウントで、［[**証明書、識別子 & プロファイル**](https://developer.apple.com/account/ios/certificate)］ を開きます。
2. [**キー**] で [**すべて**] を選択し、右上の追加ボタン (+) をクリックします。
3. [**キーの説明**]で、署名キーの一意の名前を入力します。
4. [**キーサービス**] で [**Apple プッシュ通知サービス (APNs)**] チェックボックスをオンにし、[**続行**] をクリックします。[**確認**] をクリックします。
5. キー ID をメモしておきます。[**ダウンロード**] をクリックして、キーを生成してダウンロードします。ダウンロードしたファイルは、何度もダウンロードできませんので、安全な場所に保存してください。
6. Braze で、[**設定**] > [**アプリ設定**] に移動し、[**Apple プッシュ通知証明書**] で `.p8` ファイルをアップロードします。開発用または実稼働用のプッシュ証明書のいずれかをアップロードできます。アプリが　App Store で公開された後にプッシュ通知をテストするには、アプリの開発バージョン用に別のワークスペースを設定することをお勧めします。
7. プロンプトが表示されたら、アプリの[バンドルID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier)、[キーID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/)、[チームIDを](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id)入力する。また、アプリの開発環境と本番環境のどちらに通知を送るかを指定する必要があるが、これはアプリのプロビジョニング・プロファイルによって定義される。 
8. 完了したら、[**保存**] を選択します。

