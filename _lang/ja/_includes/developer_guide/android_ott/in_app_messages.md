{% multi_lang_include developer_guide/prerequisites/android.md %}

## TVとOTTのサポートについて

Android Braze SDKは、Android TVやFire StickのようなOTTデバイスでのアプリ内メッセージ表示をネイティブにサポートしている。しかし、Androidネイティブとアプリ内メッセージにはいくつかの重要な違いがある。OTT デバイスの場合:

- スライドアップなどのタッチモードを必要とするアプリ内メッセージは、OTT で無効になります。
- 閉じるボタンなど、現在選択されている項目またはフォーカスされている項目がハイライト表示されます。
- ボタン上ではなく、アプリ内メッセージ自体の本文をクリックすることはサポートされていません。
