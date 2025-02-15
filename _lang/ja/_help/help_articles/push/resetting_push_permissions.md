---
nav_title: 再設定プッシュ権限
article_title: 再設定プッシュ権限
page_type: solution
description: "このヘルプ記事では、ブラウザのプッシュ権限とデータをリセットする方法について説明します。"
channel: push
---

# プッシュ権限のリセット

ブラウザーでプッシュ通知の問題が発生した場合は、サイトの通知権限をリセットし、サイトのストレージをクリアする必要がある場合があります。サポートが必要な場合は、以下のステップを参照してください。

## デスクトップのChrome をリセットする

1. Chrome ブラウザのURL の横にある**View Site Information** スライダアイコンをクリックします。
2. [**通知**] で、[**権限をリセット**] をクリックします。
3. Chrome DevTools を開きます。オペレーティングシステムごとの関連するショートカットは次のとおりです。

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | キーボードショートカット                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\.DevTools で、**Application** タブに移動します。
5. サイドバーで、**Storage** を選択します。
6. [**サイトデータをクリア**] をクリックします。
7. 更新された設定を適用するために、Chrome でページの再読み込みを求められます。[**再読み込み**] をクリックします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

## Android で Chrome をリセットする

Android 通知ドロワーにサイトからの通知が表示されている場合:

1. プッシュ通知から<i class="fas fa-cog" title="設定s"></i>をタップし、**Site 設定s**を選択します。
2. **サイト設定s**から**クリア&リセット**をタップします。

サイトからの通知が開かれていない場合:

1. Android で Chrome を開きます。
2. <i class="fas fa-ellipsis-vertical"></i>メニューをタップします。
3. [**設定**] > [**サイトの設定**] > [**通知**] に移動します。
4. 通知が [送信前に確認する (推奨)] に設定されていることを確認します。
5. リストでサイトを見つけます。
6. エントリを選択し、[**クリアしてリセット**] をタップします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

## デスクトップのFirefox をリセットする

1. サイトURL の横にある <i class="fa-solid fa-circle-info" alt="info icon"></i> または <i class="fas fa-lock" alt="lock icon"></i> をクリックします。
2. [**権限**] で、[**通知を受信**] の横にある [<i class="fa-solid fa-circle-xmark" title="この権限をクリアして再度確認"></i>] を選択して通知権限をクリアします。
3. 同じメニューで、**Clear Cookies and Site Data**を選択します。
4. 選択内容を確認するための画面がアプリされます。**OK**をクリックします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

## Android時にFirefox を初期化する

Androidのプッシュ権限を再設定するには、この[Mozilla サポート記事](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) を参照してください。

## macOS での Safari のリセット

{% alert note %}
これらのステップは macOS 専用です。Apple は、Windows では Safari の Web プッシュをサポートしていません。
{% endalert %}

1. Safari を開きます。
2. [Macのメニューバー](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac)から、**Safari**> **設定**> **Webサイト**> **通知**に進みます。
3. リストからサイトを選択します。
4. **Remove**を押すと、サイトの通知権限が削除されます。
5. 次に、[**プライバシー**] > [**Web サイトデータを管理**] に移動します。
6. リストからサイトを選択します。
7. **Remove**をクリックするか、すべてのサイトデータを削除するには、**Remove All**をクリックします。
8. [**完了**] をクリックします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。


*最終更新日: 2024年2月12日*