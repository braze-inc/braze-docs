module Jekyll
  module Tags
    class IncludeAbsoluteTagError < StandardError
      attr_accessor :path

      def initialize(msg, path)
        super(msg)
        @path = path
      end
    end

    class IncludeAbsoluteTag < Liquid::Tag
			VALID_SYNTAX = %r!
				([\w-]+)\s*=\s*
				(?:"([^"\\]*(?:\\.[^"\\]*)*)"|'([^'\\]*(?:\\.[^'\\]*)*)'|([\w.-]+))
      !x.freeze
      VARIABLE_SYNTAX = %r!
        (?<variable>[^{]*(\{\{\s*[\w\-.]+\s*(\|.*)?\}\}[^\s{}]*)+)
        (?<params>.*)
      !mx.freeze

      LANGUAGE_MAP = {
        'fr' => 'fr_fr',
        'pt-br' => 'pt_br',
      }
      FULL_VALID_SYNTAX = %r!\A\s*(?:#{VALID_SYNTAX}(?=\s|\z)\s*)*\z!.freeze
      VALID_FILENAME_CHARS = %r!^[\w/.\-()+~\#@]+$!.freeze
			INVALID_SEQUENCES = %r![./]{2,}!.freeze

			MULTI_LANG_PATH = '/_lang/[LANG]/'
      def initialize(tag_name, markup, tokens)
        super
        matched = markup.strip.match(VARIABLE_SYNTAX)
        if matched
          @file = matched["variable"].strip
          @params = matched["params"].strip
        else
          @file, @params = markup.strip.split(%r!\s+!, 2)
        end
				@file.gsub!(/\A'|'\Z/, '')

        validate_params if @params
        @tag_name = tag_name
      end

      def syntax_example
        "{% #{@tag_name} 'file.ext' param='value' param2='value' %}"
      end

      def parse_params(context)
        params = {}
        markup = @params

        while (match = VALID_SYNTAX.match(markup))
          markup = markup[match.end(0)..-1]

          value = if match[2]
                    match[2].gsub(%r!\\"!, '"')
                  elsif match[3]
                    match[3].gsub(%r!\\'!, "'")
                  elsif match[4]
                    context[match[4]]
                  end

          params[match[1]] = value
        end
        params
      end

			def validate_file_name(file)
				if INVALID_SEQUENCES.match?(file) || !VALID_FILENAME_CHARS.match?(file)
          raise ArgumentError, <<~MSG
            Invalid syntax for include tag. File contains invalid characters or sequences:
              #{file}
            Valid syntax:
              #{syntax_example}
          MSG
        end
      end

			def validate_params
        unless FULL_VALID_SYNTAX.match?(@params)
          raise ArgumentError, <<~MSG
            Invalid syntax for include tag:
            #{@params}
            Valid syntax:
            #{syntax_example}
          MSG
        end
      end

      # Grab file read opts in the context
      def file_read_opts(context)
        context.registers[:site].file_read_opts
      end

      # Render the variable if required
      def render_variable(context, file)
        if @file =~ VARIABLE_SYNTAX
          partial = context.registers[:site]
            .liquid_renderer
            .file("(variable)")
            .parse(file)
          partial.render!(context)
        end
      end

      def render(context)
        site = context.registers[:site]
	      lang = (
          LANGUAGE_MAP[site.config['language']] ?
            LANGUAGE_MAP[site.config['language']] :
            site.config['language']
        ) || 'en'
				include_prefix = ''
        lang_prefix = ''
				if (lang != 'en')

					lang_prefix = MULTI_LANG_PATH.gsub('[LANG]', lang)
          include_prefix = lang_prefix + '_includes/'
        else
          include_prefix = '_includes/'
				end

        file = render_variable(context, @file) || (include_prefix + @file)
        validate_file_name(file)

        source = File.expand_path(context.registers[:site].config['source']).freeze
        path = File.join(source, file)
        # Check if file exist, if not default to normal path
        if (!File.exist?(path))
          path.gsub!(lang_prefix, '/')
        end
        return unless path
        partial = Liquid::Template.parse(read_file(path, context))

        context.stack do
          context["include"] = parse_params(context) if @params
          begin
            partial.render!(context)
          rescue Liquid::Error => e
            e.template_name = path
            e.markup_context = "included " if e.markup_context.nil?
            raise e
          end
        end
      end

      def valid_include_file?(path, dir, safe)
        !outside_site_source?(path, dir, safe) && File.file?(path)
      end

      def outside_site_source?(path, dir, safe)
        safe && !realpath_prefixed_with?(path, dir)
      end

      def realpath_prefixed_with?(path, dir)
        File.exist?(path) && File.realpath(path).start_with?(dir)
      rescue StandardError
        false
      end

      # This method allows to modify the file content by inheriting from the class.
      def read_file(file, context)
        File.read(file, **file_read_opts(context))
      end

      private

      def could_not_locate_message(file, includes_dirs, safe)
        message = "Could not locate the included file '#{file}' in any of "\
          "#{includes_dirs}. Ensure it exists in one of those directories and"
        message + if safe
                    " is not a symlink as those are not allowed in safe mode."
                  else
                    ", if it is a symlink, does not point outside your site source."
                  end
      end
    end
  end
end

Liquid::Template.register_tag("multi_lang_include", Jekyll::Tags::IncludeAbsoluteTag)
