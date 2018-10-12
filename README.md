# NewRelic Java Agent (APM)

Master: [![Build Status](https://travis-ci.org/sansible/newrelic_agent_java.svg?branch=master)](https://travis-ci.org/sansible/newrelic_agent_java)
Develop: [![Build Status](https://travis-ci.org/sansible/newrelic_agent_java.svg?branch=develop)](https://travis-ci.org/sansible/newrelic_agent_java)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role ...


## Installation and Dependencies

To install run `ansible-galaxy install sansible.newrelic_agent_java` or add this to your
`roles.yml`.

```YAML
- name: sansible.newrelic_agent_java
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses tags: **build** and **configure**

* `build` - Installs ...
* `configure` - Configures ...


## Examples

Simply include role in your playbook

```YAML
- name: Install and Configure newrelic_agent_java
  hosts: somehost

  roles:
    - role: sansible.newrelic_agent_java
```
