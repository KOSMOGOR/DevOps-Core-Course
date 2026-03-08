# Lab 06

## 1. Overview

All roles refactored with blocks, docker replaced with docker-compose and Jinja2 templates.

Technologies used: Ansible, docker-compose, Jinja2, GItHub Actions.

## 2. Blocks & Tags

### `common` role

`block` installs packages, `rescue` forces cache update and `always` logs completition.

Tags: packages.

### `docker` role

`block` installs docker related packages, `rescue` forces cache update and `always` ensures everything is installed.

Tags: docker_install, docker_config.

### `web_app` role

`block` deploys app and `rescue` logs failure.

Tags: web_app_wipe, web_app_deploy.

### Example run

```text
$ ansible-playbook playbooks/provision.yml --tags "docker"
PLAY RECAP
lab05-server: ok=9  changed=0  (only docker tasks ran, common skipped)
```

## 3. Docker Compose Migration

### Template structure

Template includes app name, image name, ports, enviroment values and restart policy.

### Role dependencies

`web_app` role depends on `docker` role, since the last one installs essential packages.

### Before/after comparison

Before: manual docker-related calls (like pull, run, stop).
After: `docker compose up -d --pull always` manages everything.

## 4. Wipe Logic

### Implementation

`wipe.yml` task stops and remove container, removes docker-compose file, removes app directory, removes docker image and logs completition.

### Variable + tag

Controlled by variable `web_app_wipe` (default: `false`) and tag `web_app_wipe`.

### Test results

```text
$ ansible-playbook playbooks/deploy_python.yml -e "web_app_wipe=true" --tags web_app_wipe
TASK [web_app : Stop and remove containers]   changed
TASK [web_app : Remove docker-compose file]   changed
TASK [web_app : Remove app directory]         changed
TASK [web_app : Remove Docker image]          changed
TASK [web_app : Log wipe completion]          "Application devops-python wiped successfully"
PLAY RECAP: ok=7  changed=4
```

## 5. CI/CD Integration

### Workflow architecture

Workflow should deploy app on push to `master` branch. Workflow has 2 jobs: lint and deploy. Workflow triggers only if ansible-related thing changed or workflow.
