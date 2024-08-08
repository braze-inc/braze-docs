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

> この記事では、Unity のトラブルシューティング シナリオをいくつか紹介します。

## 「ファイルを読み取れませんでした」エラー

次のようなエラーは無視しても問題ありません。Apple ソフトウェアは CgBI と呼ばれる独自の PNG 拡張子を使用しますが、Unity はこれを認識しません。これらのエラーは、iOS ビルドや Braze バンドル内の関連画像の適切な表示には影響しません。

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
