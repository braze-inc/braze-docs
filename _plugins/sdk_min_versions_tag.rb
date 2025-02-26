# Usage:
# {% sdk_min_versions ios:3.2.3 android:8.0.0 web:1.2.3 %}
# Description:
# Renders a chip for each platform along with the changelog version as an href

module Jekyll
  module SdkMinVersions
    class SdkMinVersionsTag < Liquid::Tag

      def initialize(tag_name, text, tokens)
        super
        @legacy_ios = get_full_version(text, 'ios')
        @legacy_ios_changelog_ref = get_changelog_ref(@legacy_ios)

        @legacy_objc = get_full_version(text, 'objc')
        @legacy_objc_changelog_ref = get_changelog_ref(@legacy_objc)

        @swift = get_full_version(text, 'swift')
        @swift_changelog_ref = get_changelog_ref(@swift)

        @web = get_full_version(text, 'web')
        @web_changelog_ref = get_changelog_ref(@web)

        @android = get_full_version(text, 'android')
        @android_changelog_ref = get_changelog_ref(@android)

        @roku = get_full_version(text, 'roku')
        @roku_changelog_ref = get_changelog_ref(@roku)

        @flutter = get_full_version(text, 'flutter')
        @flutter_changelog_ref = get_changelog_ref(@flutter)

        @reactnative = get_full_version(text, 'reactnative')
        @reactnative_changelog_ref = get_changelog_ref(@reactnative)

        @unity = get_full_version(text, 'unity')
        @unity_changelog_ref = get_changelog_ref(@unity)

        @cordova = get_full_version(text, 'cordova')
        @cordova_changelog_ref = get_changelog_ref(@cordova)

        @xamarin = get_full_version(text, 'xamarin')
        @xamarin_changelog_ref = get_changelog_ref(@xamarin)

      end

      def render(context)
        site = context.registers[:site]
        converter = site.find_converter_instance(::Jekyll::Converters::Markdown)

        render_html = "<div id='sdk-versions'>"
        if !@legacy_ios.nil?
          render_html += "<a href='/docs/developer_guide/platforms/legacy_sdks/ios/changelog/swift_changelog/changelog/swift_changelog/##{@legacy_ios_changelog_ref}' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; iOS: #{@legacy_ios}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@legacy_objc.nil?
          render_html += "<a href='/docs/developer_guide/platforms/legacy_sdks/ios/changelog/swift_changelog/changelog/objc_changelog/##{@legacy_objc_changelog_ref}' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; iOS Objective-C: #{@legacy_objc} &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@swift.nil?
          render_html += "<a href='/docs/developer_guide/platforms/swift/changelog/##{@swift_changelog_ref}' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: #{@swift}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@web.nil?
          render_html += "<a href='/docs/developer_guide/platforms/web/changelog/##{@web_changelog_ref}' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: #{@web}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@android.nil?
          render_html += "<a href='/docs/developer_guide/platforms/android/changelog/##{@android_changelog_ref}' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: #{@android}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@roku.nil?
          render_html += "<a href='/docs/developer_guide/platforms/roku/changelog/##{@roku_changelog_ref}' class='sdk-versions--chip roku-sdk' target='_blank'><i class='fa-solid fa-tv'></i> &nbsp; Roku: #{@roku}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@flutter.nil?
          render_html += "<a href='/docs/developer_guide/platforms/flutter/changelog/##{@flutter_changelog_ref}' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: #{@flutter}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@unity.nil?
          render_html += "<a href='/docs/developer_guide/platforms/unity/changelog/##{@unity_changelog_ref}' class='sdk-versions--chip unity-sdk' target='_blank'>Unity: #{@unity}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@reactnative.nil?
          render_html += "<a href='/docs/developer_guide/platforms/react_native/changelog/##{@reactnative_changelog_ref}' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: #{@reactnative}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@cordova.nil?
          render_html += "<a href='/docs/developer_guide/platforms/cordova/changelog/##{@cordova_changelog_ref}' class='sdk-versions--chip cordova-sdk' target='_blank'>Cordova: #{@cordova}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        if !@xamarin.nil?
          render_html += "<a href='/docs/developer_guide/platforms/xamarin/changelog/##{@xamarin_changelog_ref}' class='sdk-versions--chip xamarin-sdk' target='_blank'>Xamarin: #{@xamarin}+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a>"
        end
        render_html += "</div>"
        return render_html
      end

      private

      def get_full_version(text, platform)
        query = /.*#{platform}:([\w\.\-]+) .*/
        match = text.match(query)
        if match.nil?
          return nil
        else
          return match[1]
        end
      end

      def get_changelog_ref(text)
        if text.nil?
          return ""
        end
        return text.gsub(".", "")
      end
    end
  end
end

Liquid::Template.register_tag('sdk_min_versions', Jekyll::SdkMinVersions::SdkMinVersionsTag)
