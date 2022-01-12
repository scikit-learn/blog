source "https://rubygems.org"

#gem "jekyll"

#gem "minimal-mistakes-jekyll", "~>4.0"
gem "minimal-mistakes-jekyll", :git => "https://github.com/mmistakes/minimal-mistakes.git", :tag => "4.24.0"
gem "webrick", "~> 1.7"
gem "jekyll-redirect-from"
gem "jekyll-sitemap"
gem "jekyll-archives"
gem "jekyll-target-blank"
gem "jekyll-paginate"
gem "jekyll-twitter-plugin"


# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.

gem "github-pages", group: :jekyll_plugins
gem "jekyll-include-cache", group: :jekyll_plugins


# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

