terraform plan -out=plan.out
terraform show -json plan.out > plan.json
terraform-visual --plan plan.json