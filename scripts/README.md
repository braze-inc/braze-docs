# Unused ShortLink Cleaner

## Description
Shortlinks are the links at the bottom of most jekyll files.

```
[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration
```

When this link is unused/unreferenced in the actual file, this script will automatically delete it from the file itself. If given a directory, this script will recursively perform this cleaning on all child files of the directory, including inside child directories.

## Usage
```
ruby unused_link_cleaner.rb PATH/TO/FILE
ruby unused_link_cleaner.rb PATH/TO/DIRECTORY
```
