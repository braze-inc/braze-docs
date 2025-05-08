---
nav_title: トラブルシューティング
article_title: Unity のトラブルシューティング
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "このリファレンス記事では、Unity プラットフォームのトラブルシューティングに関するトピックについて説明します。"

---

# トラブルシューティング

> この記事では、Unity のトラブルシューティングのシナリオをいくつか紹介します。

## 「ファイルを読み込めませんでした」エラー

以下のようなエラーは無視して問題ありません。アップルのソフトウェアはCgBIと呼ばれる独自のPNG拡張子を使用しているが、Unityはこれを認識しない。これらのエラーは、iOSのビルドやBrazeバンドルの関連画像の適切な表示には影響しない。

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
