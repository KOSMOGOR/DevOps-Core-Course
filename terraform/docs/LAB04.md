# Lab04

## Cloud Provider

I chose Yandex, since I already have an account and it was easy to deploy.

## Terraform Version

`v1.14.5`

## Resources Created

Ubuntu 24 VM with 2 cores (20% fraction), 2 GB RAM (minimum amount), at zone `ru-central1-a`. Also network and subnet for internet access.

## Terraform SSH connection

`$ ssh -l ubuntu 89.169.159.165`, but since VM is down, IP is no longer usable.

## Total Cost

0$ with free tier.

## `terraform plan` Output

```bash
$ terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8kiogst6b2vj84enm8"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 10
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                [PUBLIC-KEY] Kosmo@KOSMOGOR
            EOT
        }
      + name                      = "devops"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params (known after apply)
        }

      + metadata_options (known after apply)

      + network_interface {
          + index          = (known after apply)
          + ip_address     = (known after apply)
          + ipv4           = true
          + ipv6           = (known after apply)
          + ipv6_address   = (known after apply)
          + mac_address    = (known after apply)
          + nat            = true
          + nat_ip_address = (known after apply)
          + nat_ip_version = (known after apply)
          + subnet_id      = (known after apply)
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 20
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)
```

## `terraform apply` Output

```bash
$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8kiogst6b2vj84enm8"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 10
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                [PUBLIC-KEY] Kosmo@KOSMOGOR
            EOT
        }
      + name                      = "devops"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params (known after apply)
        }

      + metadata_options (known after apply)

      + network_interface {
          + index          = (known after apply)
          + ip_address     = (known after apply)
          + ipv4           = true
          + ipv6           = (known after apply)
          + ipv6_address   = (known after apply)
          + mac_address    = (known after apply)
          + nat            = true
          + nat_ip_address = (known after apply)
          + nat_ip_version = (known after apply)
          + subnet_id      = (known after apply)
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 20
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 4s [id=enpqdkfcrncld6oc16fj]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bodc1ms7d25ltdi42s]
yandex_compute_disk.boot-disk-1: Still creating... [00m10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=fhmikqn5rdv9ll4cbcr6]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [00m10s elapsed]
yandex_compute_instance.vm-1: Still creating... [00m20s elapsed]
yandex_compute_instance.vm-1: Creation complete after 30s [id=fhm0e4tnane9pqsadidj]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "89.169.159.165"
internal_ip_address_vm_1 = "192.168.10.14"
```

## `terraform destroy` Output

```bash
$ terraform destroy
yandex_vpc_network.network-1: Refreshing state... [id=enpqdkfcrncld6oc16fj]
yandex_compute_disk.boot-disk-1: Refreshing state... [id=fhmikqn5rdv9ll4cbcr6]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e9bodc1ms7d25ltdi42s]
yandex_compute_instance.vm-1: Refreshing state... [id=fhm0e4tnane9pqsadidj]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be destroyed
  - resource "yandex_compute_disk" "boot-disk-1" {
      - block_size  = 4096 -> null
      - created_at  = "2026-02-15T13:39:58Z" -> null
      - folder_id   = "b1gn076sma8ct5fdv1sn" -> null
      - id          = "fhmikqn5rdv9ll4cbcr6" -> null
      - image_id    = "fd8kiogst6b2vj84enm8" -> null
      - labels      = {} -> null
      - name        = "boot-disk-1" -> null
      - product_ids = [
          - "f2efpfu0cu4mpfovk95c",
        ] -> null
      - size        = 10 -> null
      - status      = "ready" -> null
      - type        = "network-hdd" -> null
      - zone        = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)

      - disk_placement_policy {
            # (1 unchanged attribute hidden)
        }

      - hardware_generation {
          - legacy_features {
              - pci_topology = "PCI_TOPOLOGY_V2" -> null
            }
        }
    }

  # yandex_compute_instance.vm-1 will be destroyed
  - resource "yandex_compute_instance" "vm-1" {
      - created_at                = "2026-02-15T13:40:08Z" -> null
      - folder_id                 = "b1gn076sma8ct5fdv1sn" -> null
      - fqdn                      = "fhm0e4tnane9pqsadidj.auto.internal" -> null
      - hardware_generation       = [
          - {
              - generation2_features = []
              - legacy_features      = [
                  - {
                      - pci_topology = "PCI_TOPOLOGY_V2"
                    },
                ]
            },
        ] -> null
      - id                        = "fhm0e4tnane9pqsadidj" -> null
      - labels                    = {} -> null
      - metadata                  = {
          - "ssh-keys" = <<-EOT
                [PUBLIC-KEY] Kosmo@KOSMOGOR
            EOT
        } -> null
      - name                      = "devops" -> null
      - network_acceleration_type = "standard" -> null
      - platform_id               = "standard-v2" -> null
      - status                    = "running" -> null
      - zone                      = "ru-central1-a" -> null
        # (5 unchanged attributes hidden)

      - boot_disk {
          - auto_delete = true -> null
          - device_name = "fhmikqn5rdv9ll4cbcr6" -> null
          - disk_id     = "fhmikqn5rdv9ll4cbcr6" -> null
          - mode        = "READ_WRITE" -> null

          - initialize_params {
              - block_size  = 4096 -> null
              - image_id    = "fd8kiogst6b2vj84enm8" -> null
              - name        = "boot-disk-1" -> null
              - size        = 10 -> null
              - type        = "network-hdd" -> null
                # (3 unchanged attributes hidden)
            }
        }

      - metadata_options {
          - aws_v1_http_endpoint = 1 -> null
          - aws_v1_http_token    = 2 -> null
          - gce_http_endpoint    = 1 -> null
          - gce_http_token       = 1 -> null
        }

      - network_interface {
          - index              = 0 -> null
          - ip_address         = "192.168.10.14" -> null
          - ipv4               = true -> null
          - ipv6               = false -> null
          - mac_address        = "d0:0d:71:3b:75:5d" -> null
          - nat                = true -> null
          - nat_ip_address     = "89.169.159.165" -> null
          - nat_ip_version     = "IPV4" -> null
          - security_group_ids = [] -> null
          - subnet_id          = "e9bodc1ms7d25ltdi42s" -> null
            # (1 unchanged attribute hidden)
        }

      - placement_policy {
          - host_affinity_rules       = [] -> null
          - placement_group_partition = 0 -> null
            # (1 unchanged attribute hidden)
        }

      - resources {
          - core_fraction = 20 -> null
          - cores         = 2 -> null
          - gpus          = 0 -> null
          - memory        = 2 -> null
        }

      - scheduling_policy {
          - preemptible = false -> null
        }
    }

  # yandex_vpc_network.network-1 will be destroyed
  - resource "yandex_vpc_network" "network-1" {
      - created_at                = "2026-02-15T13:39:58Z" -> null
      - default_security_group_id = "enp3j5beit10pgs8tt3c" -> null
      - folder_id                 = "b1gn076sma8ct5fdv1sn" -> null
      - id                        = "enpqdkfcrncld6oc16fj" -> null
      - labels                    = {} -> null
      - name                      = "network1" -> null
      - subnet_ids                = [
          - "e9bodc1ms7d25ltdi42s",
        ] -> null
        # (1 unchanged attribute hidden)
    }

  # yandex_vpc_subnet.subnet-1 will be destroyed
  - resource "yandex_vpc_subnet" "subnet-1" {
      - created_at     = "2026-02-15T13:40:01Z" -> null
      - folder_id      = "b1gn076sma8ct5fdv1sn" -> null
      - id             = "e9bodc1ms7d25ltdi42s" -> null
      - labels         = {} -> null
      - name           = "subnet1" -> null
      - network_id     = "enpqdkfcrncld6oc16fj" -> null
      - v4_cidr_blocks = [
          - "192.168.10.0/24",
        ] -> null
      - v6_cidr_blocks = [] -> null
      - zone           = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null

      - network_id     = "enpqdkfcrncld6oc16fj" -> null
      - v4_cidr_blocks = [
          - "192.168.10.0/24",
        ] -> null
      - v6_cidr_blocks = [] -> null
      - zone           = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null

          - "192.168.10.0/24",
        ] -> null
      - v6_cidr_blocks = [] -> null
      - zone           = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null

      - v6_cidr_blocks = [] -> null
      - zone           = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null

        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null


Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null


Changes to Outputs:
  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null

  - external_ip_address_vm_1 = "89.169.159.165" -> null
  - internal_ip_address_vm_1 = "192.168.10.14" -> null

  - internal_ip_address_vm_1 = "192.168.10.14" -> null


Do you really want to destroy all resources?
Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

yandex_compute_instance.vm-1: Destroying... [id=fhm0e4tnane9pqsadidj]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m10s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m20s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m30s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m40s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m20s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m30s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m40s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 00m50s elapsed]
yandex_compute_instance.vm-1: Still destroying... [id=fhm0e4tnane9pqsadidj, 01m00s elapsed]
yandex_compute_instance.vm-1: Destruction complete after 1m4s
yandex_vpc_subnet.subnet-1: Destroying... [id=e9bodc1ms7d25ltdi42s]
yandex_compute_disk.boot-disk-1: Destroying... [id=fhmikqn5rdv9ll4cbcr6]
yandex_compute_disk.boot-disk-1: Destruction complete after 0s
yandex_vpc_subnet.subnet-1: Destruction complete after 5s
yandex_vpc_network.network-1: Destroying... [id=enpqdkfcrncld6oc16fj]
yandex_vpc_network.network-1: Destruction complete after 1s

Destroy complete! Resources: 4 destroyed.
```

## Pulumi Detail

Pulumi had version `v3.220.0` and as language I used TS.

## Code Difference

Terraform's code is more declarative, while Pulumi's is more imperative.

## `pulumi preview` Output

```bash
$ pulumi version
v3.220.0

Kosmo@KOSMOGOR MINGW64 ~/Documents/_Programming/IU/DevOps/pulumi (lab04)
$ pulumi preview
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/KOSMOGOR-org/project/dev/previews/e88ebc7a-cf97-407c-acf7-5280ba5f0337

     Type                              Name         Plan
 +   pulumi:pulumi:Stack               project-dev  create
 +   ├─ yandex:index:VpcNetwork        network-1    create
 +   ├─ yandex:index:ComputeDisk       boot-disk-1  create
 +   ├─ yandex:index:VpcSubnet         subnet-1     create
 +   ├─ yandex:index:ComputeInstance   devops       create
 +   └─ yandex:index:VpcSecurityGroup  vm-group-1   create
Outputs:
    externalIpVm1: [unknown]
    interanIpVm1 : [unknown]

Resources:
    + 6 to create
```

## `pulumi up` Output

```bash
$ pulumi up
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/KOSMOGOR-org/project/dev/previews/fec61157-cf60-4b6f-a295-cd5f4052abe0

     Type                              Name         Plan
 +   pulumi:pulumi:Stack               project-dev  create
 +   ├─ yandex:index:VpcNetwork        network-1    create
 +   ├─ yandex:index:ComputeDisk       boot-disk-1  create
 +   ├─ yandex:index:VpcSubnet         subnet-1     create
 +   ├─ yandex:index:VpcSecurityGroup  vm-group-1   create
 +   └─ yandex:index:ComputeInstance   devops       create
Outputs:
    externalIpVm1: [unknown]
    interanIpVm1 : [unknown]

Resources:
    + 6 to create

Do you want to perform this update? yes
Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/KOSMOGOR-org/project/dev/updates/5

     Type                              Name         Status
 +   pulumi:pulumi:Stack               project-dev  created (54s)
 +   ├─ yandex:index:VpcNetwork        network-1    created (6s)
 +   ├─ yandex:index:ComputeDisk       boot-disk-1  created (14s)
 +   ├─ yandex:index:VpcSecurityGroup  vm-group-1   created (3s)
 +   ├─ yandex:index:VpcSubnet         subnet-1     created (1s)
 +   └─ yandex:index:ComputeInstance   devops       created (33s)
Outputs:
    externalIpVm1: "93.77.185.81"
    interanIpVm1 : "192.168.10.17"

Resources:
    + 6 created

Duration: 1m3s
```

## `pulumi destroy` Output

```bash
$ pulumi destroy
Previewing destroy (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/KOSMOGOR-org/project/dev/previews/dffec595-a3d6-4afc-803c-ab9ab8a09751

     Type                              Name         Plan                                                                                                                                                                    
 -   pulumi:pulumi:Stack               project-dev  delete                                                                                                                                                                  
 -   ├─ yandex:index:ComputeInstance   devops       delete                                                                                                                                                                  
 -   ├─ yandex:index:VpcSubnet         subnet-1     delete                                                                                                                                                                  
 -   ├─ yandex:index:VpcSecurityGroup  vm-group-1   delete                                                                                                                                                                  
 -   ├─ yandex:index:ComputeDisk       boot-disk-1  delete                                                                                                                                                                  
 -   └─ yandex:index:VpcNetwork        network-1    delete                                                                                                                                                                  
Outputs:
  - externalIpVm1: "93.77.189.178"
  - interanIpVm1 : "192.168.10.8"

Resources:
    - 6 to delete

Do you want to perform this destroy? yes
Destroying (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/KOSMOGOR-org/project/dev/updates/16

     Type                              Name         Status
 -   pulumi:pulumi:Stack               project-dev  deleted (0.54s)
 -   ├─ yandex:index:ComputeInstance   devops       deleted (75s)
 -   ├─ yandex:index:VpcSubnet         subnet-1     deleted (3s)
 -   ├─ yandex:index:VpcSecurityGroup  vm-group-1   deleted (1s)
 -   ├─ yandex:index:VpcNetwork        network-1    deleted (1s)
 -   └─ yandex:index:ComputeDisk       boot-disk-1  deleted (0.86s)
Outputs:
  - externalIpVm1: "93.77.189.178"
  - interanIpVm1 : "192.168.10.8"

Resources:
    - 6 deleted

Duration: 1m24s

The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained. 
If you want to remove the stack completely, run `pulumi stack rm dev`.
```

## Pulumi SSH connection

`$ ssh -l ubuntu 93.77.189.178`, but since VM is down, IP is no longer usable.

## Comparison

- Ease of learning - probably Pulumi, since I was learning it after knowing Terraform
- Code readability - Pulumi is more readable for me
- Debugging - Pulumi has website, that can really help with debugging, while Terraform has only console output
- Documentation - at the lecture was said, that Terraform has bigger comunity, so I thing it has larger documentation
- in most cases I will use Pulumi, since I like it style more that Terraform
