# NewRelic Java Agent (APM)

Master: [![Build Status](https://travis-ci.org/sansible/newrelic_agent_java.svg?branch=master)](https://travis-ci.org/sansible/newrelic_agent_java)
Develop: [![Build Status](https://travis-ci.org/sansible/newrelic_agent_java.svg?branch=develop)](https://travis-ci.org/sansible/newrelic_agent_java)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role installs Newrelic Java Agent.

For information how to enable newrelic.jar please check
https://docs.newrelic.com/docs/agents/java-agent/installation/include-java-agent-jvm-argument

Please have a look at [role var file](vars/main.yml) which contain all the default
agent settings. The `sansible_newrelic_agent_java_settings` dictionary is use to
extend `sansible_newrelic_agent_java_default_settings`.




## Installation and Dependencies

To install run `ansible-galaxy install sansible.newrelic_agent_java` or add this to
your `roles.yml`.

```YAML
- name: sansible.newrelic_agent_java
  version: v1.0.0-latest
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses tags: **build** and **configure**

* `build` - Downloads New Relic java agent
* `configure` - Configures New Relic java agent, requires a valid license key




## Examples

Download and configure New Relic Java agent in `/home/my_app/code/newrelic`
directory.

```YAML
- name: Install and configure newrelic java agent
  hosts: "somehost"

  roles:
    - role: sansible.newrelic_agent_java
      sansible_newrelic_agent_java_install_dir: /home/my_app/code/newrelic
      sansible_newrelic_agent_java_group: my_app
      sansible_newrelic_agent_java_user: my_app
      sansible_newrelic_agent_java_settings:
        app_name: My Application
        license_key: 123456789123456789123456789123456789
```
