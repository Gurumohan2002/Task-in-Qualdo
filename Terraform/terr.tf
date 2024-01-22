provider "google" {
  credentials = file("C:\\Users\\HI\\Downloads\\bustling-syntax-405306-419798141eca.json")
  project     = "bustling-syntax-405306"
  region      = "us-central1"
}

resource "local_file" "state_file" {
  filename = "terraform.tfstate"
  content  = <<-EOT
    {
      "example": "local state content stores",
      "and": "then cloud state content stores"
    }
  EOT
}

resource "google_storage_bucket" "new_bucket" {
  name       = "my-new-bucket-30"
  location   = "US"
  depends_on = [local_file.state_file]
}

output "bucket_name" {
  value = google_storage_bucket.new_bucket
}
