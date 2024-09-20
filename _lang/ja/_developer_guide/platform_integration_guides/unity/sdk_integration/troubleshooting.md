---
nav_title: トラブルシューティング
article_title: ユニティのトラブルシューティング
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "このリファレンスでは、Unityプラットフォームのトラブルシューティングについて説明する。"

---

# トラブルシューティング

> この記事では、ユニティのトラブルシューティングのシナリオをいくつか紹介する。

## 「ファイルを読み込めませんでした」エラー

以下のようなエラーは無視して差し支えない。アップルのソフトウェアはCgBIと呼ばれる独自のPNG拡張子を使用しているが、Unityはこれを認識しない。これらのエラーは、iOSのビルドやBrazeバンドルの関連画像の適切な表示には影響しない。

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
