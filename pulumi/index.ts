import * as yandex from "@pulumi/yandex"; 
import secrets from "./secrets.json";
import { readFileSync } from "fs";
const sshKey = readFileSync("C:\\Users\\Kosmo\\.ssh\\id_ed25519.pub", "utf-8").trim();

// const provider = new yandex.Provider("provider", {
//     zone: "ru-central1-a",
//     token: secrets.ya_token,
//     cloudId: secrets.ya_cloud_id,
//     folderId: secrets.ya_folder_id
// });

const disk = new yandex.ComputeDisk("boot-disk-1", {
    folderId: secrets.ya_folder_id,
    type: "network-hdd",
    zone: "ru-central1-a",
    size: 10,
    imageId: "fd8kiogst6b2vj84enm8"
});

const network = new yandex.VpcNetwork("network-1", {
    folderId: secrets.ya_folder_id,
    name: "network-1"
});

const subnet = new yandex.VpcSubnet("subnet-1", {
    folderId: secrets.ya_folder_id,
    zone: "ru-central1-a",
    networkId: network.id,
    v4CidrBlocks: ["192.168.10.0/24"]
});

const vm = new yandex.ComputeInstance("devops", {
    folderId: secrets.ya_folder_id,
    zone:"ru-central1-a",
    platformId: "standard-v2",
    resources: {
        cores: 2,
        memory: 2,
        coreFraction: 20
    },
    bootDisk: {
        diskId: disk.id
    },
    networkInterfaces: [{
        subnetId: subnet.id,
        nat: true
    }],
    metadata: {
        "ssh-keys": `ubuntu:${sshKey}`
    }
});

const secGroup = new yandex.VpcSecurityGroup("vm-group-1", {
    folderId: secrets.ya_folder_id,
    networkId: network.id,
    ingresses: [
        {
            description: "SSH",
            protocol: "TCP",
            v4CidrBlocks: ["0.0.0.0/0"],
            port: 22
        },
        {
            description: "Web",
            protocol: "TCP",
            v4CidrBlocks: ["0.0.0.0/0"],
            port: 80
        },
        {
            description: "Future",
            protocol: "TCP",
            v4CidrBlocks: ["0.0.0.0/0"],
            port: 5000
        }
    ]
});

export const interanIpVm1 = vm.networkInterfaces[0].ipAddress;
export const externalIpVm1 = vm.networkInterfaces[0].natIpAddress;