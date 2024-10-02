---
nav_title: 再設定プッシュ権限
article_title: 再設定プッシュ権限
page_type: solution
description: "このヘルプ記事では、ブラウザのプッシュ権限とデータをリセットする方法について説明します。"
channel: push
---

# 再設定プッシュ権限

ブラウザーでプッシュ通知に問題が発生した場合は、サイトの通知権限を再設定し、サイトの記憶領域を消去する必要があります。ヘルプについては、これらのステップを参照してください。

## デスクトップのChrome をリセットする

1. Chrome ブラウザのURL の横にある**View Site Information** スライダアイコンをクリックします。
2. **Notifications**の下で、**Reset permission**をクリックします。
3. Chrome DevTools を開きます。オペレーティングシステムごとの関連するショートカットは次のとおりです。

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | キーボードショートカット                                                  |
| ------- | ------------------------------------------------------------------- |
| マック      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2}

{:start="4"}
4\.DevTools で、**Application** タブに移動します。
5. サイドバーで、**Storage** を選択します。
6. **サイトデータクリア**をクリックします。
7. 更新 d 設定 sをアプリするために、再度読み込むするように求められます。**Re 読み込む**を押します。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

## Android時のクロムの初期化

Android 通知ドロワーに通知が表示されている場合:

1. プッシュ通知から<i class="fas fa-cog" title="設定s"></i>をタップし、**Site 設定s**を選択します。
2. **サイト設定s**から**クリア&リセット**をタップします。

開封からの通知がない場合:

1. Androidでクロームを開きます。
2. <i class="fas fa-ellipsis-vertical"></i>メニューをタップします。
3. **Settings**> **Site Settings**> **Notifications**に移動します。
4. 通知が「&quot」に設定されていることを確認します。送信時に確認する(推奨)"。
5. リストからサイトを検索します。
6. エントリを選択し、**クリア&リセット**をタッチします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

## デスクトップのFirefox をリセットする

1. サイトURL の横にある<i class="fa-solid fa-circle-info" alt="info icon"></i> または<i class="fas fa-lock" alt="lock icon"></i> をクリックします。
2. **Permissions**で、**Receive 通知 s**の横にある<i class="fa-solid fa-circle-xmark" title="この権限をクリアし、再度"></i>に通知権限をクリアしてください。
3. 同じメニューで、**Clear Cookies and Site Data**を選択します。
4. 選択内容を確認するための画面がアプリされます。**OK**をクリックします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

## Android時にFirefox を初期化する

Androidのプッシュ権限を再設定するには、この[Mozilla サポート記事](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) を参照してください。

## macOS でのSafari のリセット

{% alert note %}
これらのステップはmacOS 専用です。Apple は、Windows ではWeb Push for Safari に対応していません。
{% endalert %}

1. Safari を開きます。
2. Macの[メニューバーから、**Safari**> **設定**> **Webサイト**> **通知**に進みます。
3. リストからサイトを選択します。
4. **Remove**を押すと、サイトの通知権限が削除されます。
5. 次に、**プライバシー**> **Webサイトデータ**に移動します。
6. リストからサイトを選択します。
7. **Remove**をクリックするか、すべてのサイトデータを削除するには、**Remove All**をクリックします。
8. **Done**をクリックします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。


*2024更新2月12日の昨日d*