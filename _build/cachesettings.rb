class CacheSettings
  def initialize(app, pat)
    @app = app
    @pat = pat
  end

  def call(env)
    res = @app.call(env)
    path = env["REQUEST_PATH"]

    @pat.each do |pattern, data|
      if path =~ pattern && data.has_key?(:cache_control)
        res[1]["Cache-Control"] = data[:cache_control] 
        return res
      end
    end

    return res
  end
end
