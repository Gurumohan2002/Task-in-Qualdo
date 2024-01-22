# terraform {
#   backend "gcs" {
#     bucket = "terraform_task"  
#     prefix = "new-one"
#   }
# }

terraform {
  backend "gcs" {
    bucket = "my-new-bucket-15"
    prefix = "terraform/state"
  }
}
