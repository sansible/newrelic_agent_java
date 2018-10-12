import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config(host):
    newrelic_agent_config = host.file(
        '/opt/newrelic-test-agent-java/newrelic.yml'
    )

    assert 'license_key: 123456789123456789123456789123456789' \
        in newrelic_agent_config.content_string
    assert 'app_name: Test Application' \
        in newrelic_agent_config.content_string


def test_default_config(host):
    newrelic_agent_config = host.file(
        '/opt/newrelic-test-agent-java/newrelic.yml'
    )

    assert 'log_daily: true' \
        in newrelic_agent_config.content_string
