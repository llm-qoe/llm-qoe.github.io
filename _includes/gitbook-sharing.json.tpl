            "sharing": {
                "facebook": false,

                "google": false,

                "github": false,
              {% if site.github_username %}
                "github_link": "https://github.com/{{ site.github_username }}",
              {% else %}
                "github_link": "https://github.com/llm-qoe/llm-qoe.github.io",
              {% endif %}

                "telegram": false,
                "telegram_link": "https://t.me",

                "instapaper": false,

                "twitter": true,
              {% if site.twitter_username %}
                "twitter_link": "https://twitter.com/JIACHENLIU8",
              {% endif %}

                "vk": false,

                "weibo": false,

                "all": ["facebook", "google", "twitter", "weibo", "instapaper", "github", "telegram"]
            },
