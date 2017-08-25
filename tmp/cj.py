#!/usr/bin/python
#coding:utf-8
import paramiko, os

host = '10.0.0.93'
username = 'xieyifan'
key_file = '~/Documents/keys/xieyifan'
key_file_pwd = 'a8GWxQ0HhgnYoU0y'
paramiko.util.log_to_file('ssh_key-log.log')
privatekey = os.path.expanduser(key_file)
try:
	key = paramiko.RSAKey.from_private_key(privatekey)
except paramiko.PasswordRequiredException:
	## 需要密码口令
	key = paramiko.RSAKey.from_private_key_file(privatekey, key_file_pwd)
ssh = paramiko.SSHClient()
ssh.load_system_host_keys(filename='/root/.ssh/known_hosts')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,username=username,pkey=key)

global:
  # The smarthost and SMTP sender used for mail notifications.
  #smtp_smarthost: 'localhost:25'
  #smtp_from: 'alertmanager@example.org'
  # The auth token for Hipchat.
  #hipchat_auth_token: '1234556789'
  # Alternative host for Hipchat.
  #hipchat_url: 'https://hipchat.foobar.org/'
  resolve_timeout: 20m

# The directory from which notification templates are read.
templates: 
- 'alertmanager.tmpl'

# The root route on which each incoming alert enters.
route:
  group_by: ['alertname','node','device']
  group_wait: 20s
  group_interval: 30s
  repeat_interval: 30m 
  receiver: lingxin-prometheus 

  routes:
  - match_re:
      alertname: ^(my|MY).*
    receiver: lingxin-recv
    routes:
      - match_re:
          alertname: .*_5m_.*
        repeat_interval: 5m 
      - match_re:
          alertname: .*_15m_.*
        repeat_interval: 15m
      - match_re:
          alertname: .*_30m_.*
        repeat_interval: 30m 
      - match_re:
          alertname: .*_1h_.*
        repeat_interval: 1h 
      - match_re:
          alertname: .*_6h_.*
        repeat_interval: 6h 
      - match_re:
          alertname: .*_1d_.*
        repeat_interval: 1d 

inhibit_rules:
- source_match:
    severity: 'critical'
  target_match:
    severity: 'warning'
  equal: ['alertname']

receivers:
- name: 'lingxin-sample'
  slack_configs:
    - api_url: "https://hooks.pubu.im/services/xxxxxx"
      text: '{{ template "xxx.description" .Alerts}}'
      channel: '#test'
    send_resolved: true
- name: 'lingxin-recv'
  webhook_configs:
    - url: "http://127.0.0.1:7788"
    send_resolved: true