# Crear aplicaciones http

Se crea una aplicación HTTP con el provider de Kubernetes, el cual puede administrar recursos del API de Kubernetes (CR) para crear recursos como Rutas, DeploymentConfigs u operadores es necesario utilizar el modulo de (CRD) manualmente.

En este ejercicio se crea un modulo para automatizar la creación de aplicaciones httpd.

## Configuración de la versión del provider

Se define el provider de kubernetes `versions.tf`

## Añadir autenticación

Agregar dirección del API y token en el archivo `variables.tf` estos definen la autenticación en el archivo `provider.tf`

## Ejecutar terraform init

Se ejecuta el comando terraform init para inicializar el proyecto y los modulos.

terraform init

~~~ bash

terraform init

Initializing the backend...
Initializing modules...
- http_app in modules/http_app

Initializing provider plugins...
- Finding hashicorp/kubernetes versions matching ">= 2.0.0"...
- Installing hashicorp/kubernetes v2.28.1...
- Installed hashicorp/kubernetes v2.28.1 (signed by HashiCorp)

~~~

## Visualizar terraform plan
[https://github.com/hieven/terraform-visual?tab=readme-ov-file](https://github.com/hieven/terraform-visual?tab=readme-ov-file)
~~~ bash

terraform plan -out=plan.out
terraform show -json plan.out > plan.json
terraform-visual --plan plan.json
~~~ 