# _plugins/markdown_copy_llm.rb
require 'jekyll'
require 'liquid'

# --- Encoding helpers (fix UTF-8 vs US-ASCII issues in hosted builds like Vercel) ---
Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

def safe_utf8(str)
  s = String(str || "")
  s = s.dup
  # If string already claims UTF-8, keep it; otherwise coerce/repair
  if s.encoding != Encoding::UTF_8
    s.force_encoding(Encoding::UTF_8)
  end
  s.valid_encoding? ? s : s.encode("UTF-8", "binary", invalid: :replace, undef: :replace, replace: "")
end

def deep_utf8(obj)
  case obj
  when String then safe_utf8(obj)
  when Array  then obj.map { |e| deep_utf8(e) }
  when Hash   then obj.transform_values { |v| deep_utf8(v) }
  else obj
  end
end

module MarkdownExport
  # -------- No-op blocks: pass through inner Markdown (drop HTML wrappers) --------
  class MdexpSdkTabs < Liquid::Block
    def render(context)
      super
    end
  end

  class MdexpSdkTab < Liquid::Block
    def render(context)
      super
    end
  end

  class MdexpTab < Liquid::Block
    def render(context)
      super
    end
  end

  class MdexpSubtabs < Liquid::Block
    def render(context)
      super
    end
  end

  class MdexpSubtab < Liquid::Block
    def render(context)
      super
    end
  end

  class MdexpSdkSubtabs < Liquid::Block
    def render(context)
      super
    end
  end

  class MdexpSdkSubtab < Liquid::Block
    def render(context)
      super
    end
  end

  class MdexpTabs < Liquid::Block
    def render(context)
      super
    end
  end

  # -------- Inline raw Markdown includes; tolerate empty/variable/extra args --------
  class MdexpMultiLangInclude < Liquid::Tag
    def initialize(tag_name, markup, tokens)
      super
      @markup = (markup || "").strip
    end

    def render(context)
      site = context.registers[:site]
      path = resolve_first_positional(@markup, context).to_s.strip
      return "<!-- export: empty multi_lang_include -->" if path.empty?

      src   = site.source
      inc_d = site.config['includes_dir'] || '_includes'

      # Candidate search paths
      bases = [src, File.join(src, inc_d)]

      candidates = []
      bases.each do |base|
        candidates << File.expand_path(path, base)
        if path.start_with?('_includes/')
          # Support authors who wrote `_includes/foo.md`
          candidates << File.expand_path(path.sub(%r{\A_includes/}, ''), File.join(src, inc_d))
        end
      end

      full = candidates.find { |p| File.file?(p) }
      unless full
        return "<!-- export: not found #{path} tried: #{candidates.join(' | ')} -->"
      end

      # Read as binary then coerce to UTF-8 safely
      data = File.binread(full)
      safe_utf8(data)
    rescue => e
      Jekyll.logger.error "MarkdownCopyLLM:", "Failed to inline #{@markup}: #{e.class}: #{e.message}"
      "<!-- export: failed to inline #{@markup}: #{e.class}: #{e.message} -->"
    end

    private

    # Extract the first positional token as a path (ignore key=value args).
    # Supports quoted strings, bare words, or Liquid outputs.
    def resolve_first_positional(markup, context)
      return "" if markup.empty?

      # If it contains Liquid output, render that whole expression
      if markup.include?('{{')
        rendered = Liquid::Template.parse(markup).render(context)
        return rendered.strip
      end

      token = markup.split(/\s+/).find { |t| !t.include?('=') } || ""
      token.gsub(/\A['"]|['"]\z/, '')
    end
  end
end

# Register export-only tag names (do NOT override your production tags)
Liquid::Template.register_tag('mdexp_sdktabs',       MarkdownExport::MdexpSdkTabs)
Liquid::Template.register_tag('mdexp_sdktab',        MarkdownExport::MdexpSdkTab)
Liquid::Template.register_tag('mdexp_tab',           MarkdownExport::MdexpTab)
Liquid::Template.register_tag('mdexp_tabs',          MarkdownExport::MdexpTabs)
Liquid::Template.register_tag('mdexp_subtabs',       MarkdownExport::MdexpSubtabs)
Liquid::Template.register_tag('mdexp_subtab',        MarkdownExport::MdexpSubtab)
Liquid::Template.register_tag('mdexp_sdksubtabs',    MarkdownExport::MdexpSdkSubtabs)
Liquid::Template.register_tag('mdexp_sdksubtab',     MarkdownExport::MdexpSdkSubtab)
Liquid::Template.register_tag('mdexp_multi_lang_include', MarkdownExport::MdexpMultiLangInclude)

module Jekyll
  class MarkdownCopyLLM
    RAW_KEY = "__export_merged_md"

    def self.init
      Jekyll.logger.info "MarkdownCopyLLM:", "export plugin loaded"

      # Capture export Markdown just before normal rendering
      Jekyll::Hooks.register [:pages, :documents], :pre_render do |item, payload|
        next unless should_capture?(item, item.site)
        item.data[RAW_KEY] = render_liquid_markdown_friendly(item, payload, item.site)
      end

      # Emit files after normal site write
      Jekyll::Hooks.register :site, :post_write do |site|
        copy_markdown_files(site)
      end
    end

    # ---------- helpers ----------

    def self.should_capture?(item, site)
      markdown?(item, site) &&
        !item.path.include?('_site/') &&
        !item.path.start_with?('_') &&
        %w[_includes _layouts _data _plugins].none? { |d| item.path.start_with?(d) }
    end

    def self.markdown?(item, site)
      ext = item.respond_to?(:extname) ? item.extname : File.extname(item.path)
      return true if %w[.md .markdown].include?(ext)
      # Uncomment if you use custom extensions that go through Markdown:
      # site.find_converter_instance(Jekyll::Converters::Markdown).matches(ext)
      false
    end

    # Rewrites certain tag names to export-only aliases, then renders Liquid.
    # Expands variables and inlines raw Markdown, while stripping tab HTML wrappers.
    def self.render_liquid_markdown_friendly(item, payload, site)
      content = safe_utf8(item.content.to_s)

      # Robust rewrites: handle {% ... %} and {%- ... -%} and whitespace
      replacements = {
        # legacy sdktabs
        /\{%-?\s*sdktabs\b/               => '{% mdexp_sdktabs',
        /\{%-?\s*endsdktabs\s*-?%\}/      => '{% endmdexp_sdktabs %}',
        /\{%-?\s*sdktab\b/                => '{% mdexp_sdktab',
        /\{%-?\s*endsdktab\s*-?%\}/       => '{% endmdexp_sdktab %}',

        # generic tabs used in many docs
        /\{%-?\s*tabs\b/                  => '{% mdexp_tabs',
        /\{%-?\s*endtabs\s*-?%\}/         => '{% endmdexp_tabs %}',
        /\{%-?\s*tab\b/                   => '{% mdexp_tab',
        /\{%-?\s*endtab\s*-?%\}/          => '{% endmdexp_tab %}',

        # sdk subtabs
        /\{%-?\s*sdksubtabs\b/            => '{% mdexp_sdksubtabs',
        /\{%-?\s*endsdksubtabs\s*-?%\}/   => '{% endmdexp_sdksubtabs %}',
        /\{%-?\s*sdksubtab\b/             => '{% mdexp_sdksubtab',
        /\{%-?\s*endsdksubtab\s*-?%\}/    => '{% endmdexp_sdksubtab %}',

        # generic subtabs
        /\{%-?\s*subtabs\b/               => '{% mdexp_subtabs',
        /\{%-?\s*endsubtabs\s*-?%\}/      => '{% endmdexp_subtabs %}',
        /\{%-?\s*subtab\b/                => '{% mdexp_subtab',
        /\{%-?\s*endsubtab\s*-?%\}/       => '{% endmdexp_subtab %}',

        # multi_lang_include
        /\{%-?\s*multi_lang_include\b/    => '{% mdexp_multi_lang_include'
      }
      replacements.each { |re, sub| content.gsub!(re, sub) }
      content = safe_utf8(content) # ensure still UTF-8 after gsubs

      page_drop      = item.to_liquid
      liquid_payload = site.site_payload.merge({ 'page' => page_drop })
      liquid_payload = deep_utf8(liquid_payload)

      registers = { site: site, page: page_drop }

      tpl = site.liquid_renderer
               .file(item.relative_path)
               .parse(content)

      out = tpl.render!(liquid_payload,
                        registers: registers,
                        strict_filters: false,
                        strict_variables: false)

      safe_utf8(out)
    end

    def self.copy_markdown_files(site)
      return unless should_copy?(site)

      all    = site.pages + site.collections.flat_map { |_, c| c.docs }
      copied = 0

      all.each do |item|
        next unless should_capture?(item, site)
        merged = item.data[RAW_KEY].to_s
        next if merged.empty?

        dest = File.join(site.dest, output_path_for(item))
        FileUtils.mkdir_p(File.dirname(dest))
        File.write(dest, merged)
        copied += 1
      end

      Jekyll.logger.info "MarkdownCopyLLM:", "Exported #{copied} merged Markdown files"

      # Generate llms.txt after markdown files are created (if you have a generator defined)
      if defined?(Jekyll::LlmsTxtGenerator)
        Jekyll::LlmsTxtGenerator.generate_llms_txt(site)
      end
    end

    def self.output_path_for(item)
      url_path = item.url.sub(%r{^/}, '').sub(%r{/$}, '')
      url_path.empty? ? 'index.md' : File.join(url_path, 'index.md')
    end

    def self.should_copy?(site)
      site.config['markdown_copies'] != false &&
        (ENV['JEKYLL_ENV'] == 'production' || site.config['markdown_copies'] == true)
    end
  end
end

Jekyll::MarkdownCopyLLM.init
