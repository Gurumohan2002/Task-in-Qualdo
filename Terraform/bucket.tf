provider "google" {
  credentials = file("C:\\Users\\HI\\Downloads\\bustling-syntax-405306-419798141eca.json")
  project     = var.project_id
  region      = var.region
}

resource "google_storage_bucket" "my_bucket_1" {
  name          = "terraform--task"
  location      = var.region
  force_destroy = var.force_destroy
}
