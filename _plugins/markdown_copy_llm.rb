# _plugins/markdown_copy_llm.rb
# frozen_string_literal: true

require 'jekyll'
require 'liquid'
require 'fileutils'

# --- Encoding helpers (no global Encoding overrides) ---
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

  class MdexpDetails < Liquid::Block
    def initialize(tag_name, markup, tokens)
      super
      @caption = markup
    end

    def render(context)
      caption = @caption.to_s.strip
      body = super
      # Convert to markdown-friendly format
      "**#{caption}**\n\n#{body}\n"
    end
  end

  # -------- Alert blocks: flatten to Markdown with a bolded label --------
  class MdexpAlert < Liquid::Block
    def initialize(tag_name, markup, tokens)
      super
      @type = markup.to_s.strip # e.g., "tip", "warning", "important"
    end

    def render(context)
      body = super
      type = @type.empty? ? "note" : @type
      "**#{type.capitalize}:**\n\n#{body}\n"
    end
  end

  # -------- Scrolly blocks: flatten to plain Markdown --------
  class MdexpScrolly < Liquid::Block
    def render(context)
      # Just return the content as plain markdown
      super
    end
  end

  # -------- Inline raw Markdown includes; reprocess with SAME pipeline (recursive) --------
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
      content = safe_utf8(data)

      # Apply the SAME export rewrites (tabs, alias tag names, details, alerts, etc.)
      content = Jekyll::MarkdownCopyLLM.apply_export_rewrites(content)

      # Re-render via Liquid with the SAME flags and context (allow recursion)
      depth = (context.registers[:_mdexp_depth] || 0)
      if depth >= 12
        return "<!-- export: include depth exceeded (#{depth}) for #{path} -->"
      end
      registers = context.registers.merge(_mdexp_depth: depth + 1)

      tpl = site.liquid_renderer
               .file(full)
               .parse(content)

      out = tpl.render!(
        context.environments.first,
        registers: registers,
        strict_filters: false,
        strict_variables: false
      )

      # IMPORTANT: Do NOT call resolve_site_variables here.
      # The outer pre_render pipeline will apply it once to the full page output.
      safe_utf8(out)
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
Liquid::Template.register_tag('mdexp_details',       MarkdownExport::MdexpDetails)
Liquid::Template.register_tag('mdexp_alert',         MarkdownExport::MdexpAlert)
Liquid::Template.register_tag('mdexp_scrolly',       MarkdownExport::MdexpScrolly)
Liquid::Template.register_tag('mdexp_multi_lang_include', MarkdownExport::MdexpMultiLangInclude)

module Jekyll
  class MarkdownCopyLLM
    RAW_KEY = "__export_merged_md"
    PUBLIC_KEY = "llm_markdown_content"

    # ---- Shared export rewrites (reused by main render and includes) ----
    def self.export_replacements
      {
        # legacy sdktabs (idempotent: match both original and mdexp_ variants)
        /\{%-?\s*(sdktabs|mdexp_sdktabs)\b/               => '{% mdexp_sdktabs',
        /\{%-?\s*(endsdktabs|endmdexp_sdktabs)(?:\s+[^%]*)?\s*-?%\}/      => '{% endmdexp_sdktabs %}',
        /\{%-?\s*(sdktab|mdexp_sdktab)\b/                => '{% mdexp_sdktab',
        /\{%-?\s*(endsdktab|endmdexp_sdktab)(?:\s+[^%]*)?\s*-?%\}/       => '{% endmdexp_sdktab %}',

        # generic tabs used in many docs (idempotent)
        /\{%-?\s*(tabs|mdexp_tabs)\b/                  => '{% mdexp_tabs',
        /\{%-?\s*(endtabs|endmdexp_tabs)(?:\s+[^%]*)?\s*-?%\}/         => '{% endmdexp_tabs %}',
        /\{%-?\s*(tab|mdexp_tab)\b/                   => '{% mdexp_tab',
        /\{%-?\s*(endtab|endmdexp_tab)(?:\s+[^%]*)?\s*-?%\}/          => '{% endmdexp_tab %}',

        # sdk subtabs (idempotent)
        /\{%-?\s*(sdksubtabs|mdexp_sdksubtabs)\b/            => '{% mdexp_sdksubtabs',
        /\{%-?\s*(endsdksubtabs|endmdexp_sdksubtabs)(?:\s+[^%]*)?\s*-?%\}/   => '{% endmdexp_sdksubtabs %}',
        /\{%-?\s*(sdksubtab|mdexp_sdksubtab)\b/             => '{% mdexp_sdksubtab',
        /\{%-?\s*(endsdksubtab|endmdexp_sdksubtab)(?:\s+[^%]*)?\s*-?%\}/    => '{% endmdexp_sdksubtab %}',

        # generic subtabs (idempotent)
        /\{%-?\s*(subtabs|mdexp_subtabs)\b/               => '{% mdexp_subtabs',
        /\{%-?\s*(endsubtabs|endmdexp_subtabs)(?:\s+[^%]*)?\s*-?%\}/      => '{% endmdexp_subtabs %}',
        /\{%-?\s*(subtab|mdexp_subtab)\b/                => '{% mdexp_subtab',
        /\{%-?\s*(endsubtab|endmdexp_subtab)(?:\s+[^%]*)?\s*-?%\}/       => '{% endmdexp_subtab %}',

        # alerts (idempotent)
        /\{%-?\s*(alert|mdexp_alert)\b/                 => '{% mdexp_alert',
        /\{%-?\s*(endalert|endmdexp_alert)(?:\s+[^%]*)?\s*-?%\}/        => '{% endmdexp_alert %}',

        # scrolly (idempotent)
        /\{%-?\s*(scrolly|mdexp_scrolly)\b/                 => '{% mdexp_scrolly',
        /\{%-?\s*(endscrolly|endmdexp_scrolly)(?:\s+[^%]*)?\s*-?%\}/        => '{% endmdexp_scrolly %}',

        # multi_lang_include (idempotent)
        /\{%-?\s*(multi_lang_include|mdexp_multi_lang_include)\b/    => '{% mdexp_multi_lang_include',

        # details (idempotent)
        /\{%-?\s*(details|mdexp_details)\b/               => '{% mdexp_details',
        /\{%-?\s*(enddetails|endmdexp_details)(?:\s+[^%]*)?\s*-?%\}/      => '{% endmdexp_details %}'
      }
    end

    def self.apply_export_rewrites(str)
      s = String(str)
      export_replacements.each { |re, sub| s.gsub!(re, sub) }
      s
    end

    def self.init
      Jekyll.logger.info "MarkdownCopyLLM:", "export plugin loaded"

      # Capture export Markdown just before normal rendering
      Jekyll::Hooks.register [:pages, :documents], :pre_render do |item, payload|
        next unless should_capture?(item, item.site)
        processed_markdown = render_liquid_markdown_friendly(item, payload, item.site)
        item.data[RAW_KEY] = processed_markdown
        # Also store in a publicly accessible key for client-side access
        item.data[PUBLIC_KEY] = processed_markdown
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
        %w[_includes _layouts _data _plugins].none? { |d| item.path.start_with?(d) } &&
        is_developer_guide?(item)
    end

    def self.markdown?(item, site)
      ext = item.respond_to?(:extname) ? item.extname : File.extname(item.path)
      return true if %w[.md .markdown].include?(ext)
      # Uncomment if you use custom extensions that go through Markdown:
      # site.find_converter_instance(Jekyll::Converters::Markdown).matches(ext)
      false
    end

    def self.is_developer_guide?(item)
      # Check if the item belongs to the developer_guide collection
      return true if item.respond_to?(:collection) && item.collection.label == 'developer_guide'
      
      # Check if the path contains developer_guide
      return true if item.path.include?('developer_guide')
      
      # Check if the URL contains developer_guide
      return true if item.url.include?('developer_guide')
      
      false
    end

    # Rewrites certain tag names to export-only aliases, then renders Liquid.
    # Expands variables and inlines raw Markdown, while stripping tab HTML wrappers.
    def self.render_liquid_markdown_friendly(item, payload, site)
      content = safe_utf8(item.content.to_s)

      # Apply shared rewrites
      content = apply_export_rewrites(content)
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

      # Post-process to resolve site variables to absolute URLs
      out = resolve_site_variables(out, site)
      
      safe_utf8(out)
    end

    # Post-process content to resolve site variables to absolute URLs
    def self.resolve_site_variables(content, site)
      base_url = site.config['homeurl'] || "https://www.braze.com"
      base_path = site.config['baseurl'] || "/docs"
      
      # Resolve {{ site.baseurl }} to absolute URL
      content = content.gsub(/\{\{\s*site\.baseurl\s*\}\}/, "#{base_url}#{base_path}")
      
      # Resolve relative links that start with /docs to absolute URLs
      content = content.gsub(/\]\(\/docs\//, "](#{base_url}#{base_path}/")
      
      # Resolve any remaining relative links that start with / to absolute URLs
      content = content.gsub(/\]\(\/(?!\/)/, "](#{base_url}/")
      
      safe_utf8(content)
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

      Jekyll.logger.info "MarkdownCopyLLM:", "Exported #{copied} Markdown files from developer_guide collection"
    end

    def self.output_path_for(item)
      url_path = item.url.sub(%r{^/}, '').sub(%r{/$}, '')
      url_path.empty? ? 'index.md' : File.join(url_path, 'index.md')
    end

    def self.should_copy?(site)
        ENV['JEKYLL_ENV'] == 'production' || site.config['markdown_copies'] == true
    end
  end
end

Jekyll::MarkdownCopyLLM.init
