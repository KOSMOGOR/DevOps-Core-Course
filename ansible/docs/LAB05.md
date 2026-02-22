# Lab 05

## 1. Architecture Overview

### Ansible version

core 2.16.3

### Target VM OS

Ubuntu 24.04

### Role structure

```text
roles/
├── common/
├── docker/
└── app_deploy/
```

### Why roles instead of monolithic playbooks?

Roles are helping in building clean structure, where role hides its functionality inside, like in OOP.

## 2. Roles Documentation

### `common` role

- **Purpose**: setups necessary packages
- **Variables**: list of necessary packages

### `docker` role

- **Purpose**: setups docker-related staff
- **Variable**: name of Docker user, list of Docker packages, Docker repo
- **Handlers**: `restart docker` triggers when Docker needs to be restarted
- **Dependencies**: intended to be run after `common` role, but not really depends on it

### `deploy_app` role

- **Purpose**: deploys containerized app
- **Variable**: app restart policy, path for checking health, enviroment for apps
- **Handlers**: `restart app` triggers when app needs to be restarted
- **Dependencies**: needs to be run after `docker` role

## 3. Idempotency Demonstration

### Terminal output after `provision.yml` runs

First run:

```bash
PLAY RECAP
lab05-server: ok=12 changed=8 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

Second run:

```bash
PLAY RECAP
lab05-server: ok=11 changed=0 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

### Changes analysis

First run changed host from initial state to needed bt playbook. Second run changed nothing.

## Ansible Vault

### Secrets storing

I store secrets using `ansible-vault` in `group_vars/all.yml`. Password is stored in `.vault_pass`.

### Encrypted file proof

File starts with:

```text
$ANSIBLE_VAULT;1.1;AES256
```

### Why Ansible vault is important

It helps store secrets with safe way of pushing it to repo.

## 5. Deployment Verification

## Terminal output after `deploy.yml`

```bash
PLAY RECAP
lab05-server: ok=8 changed=3 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

### Terminal output after `docker ps`

```text
CONTAINER ID   IMAGE                    COMMAND           CREATED              STATUS          PORTS
4ab97e5d843f   kosmogor/devops:latest   "python app.py"   About a minute ago   Up 42 seconds   0.0.0.0:5000->5000/tcp
```

### Terminal output after `curl`

```json
{"status":"healthy","timestamp":"2026-02-22T12:18:05.615222+00:00","uptime_seconds":51}
```

### Handlers

`app_deploy` handler `restart app` was triggered after application deployment.

## 6. Key Decisions

## Why use roles instead of plain playbooks?

It creates cleaner structure.

## How do roles improve reusability?

One role can be used in multiple playbooks, which decreases duplicated code.

## What makes a task idempotent?

Use of `state`, so some tasks would not be repeated after second run.

## How do handlers improve efficiency?

Handlers run after playbook, only if was notified and only once.

## Why is Ansible Vault necessary?

It helps store credential in a safe way.
