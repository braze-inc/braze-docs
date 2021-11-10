module Jekyll
  module CustomMultiLangFilter
  	# Automatically convert urls starting with /docs/path to
  	# /docs/lang/path if the path is more than 2 characters
    def multi_lang(doc_url)
  		url_match = doc_url.match(/^\/docs\/\w{2}\//)
      lang_url = doc_url
  		site = @context.registers[:site]
      lang = site.config['language'] || 'en'
  		# If not english, and the url subpath is more than 2 characters,
  		# add language path
  		if ((lang != 'en') && !url_match)
  			lang_url.gsub!(/^\/docs\//, "\/docs\/#{lang}\/")
  		end
  		return lang_url
    end
  end
end

Liquid::Template.register_filter(Jekyll::CustomMultiLangFilter)