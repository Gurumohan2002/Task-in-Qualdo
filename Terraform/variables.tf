variable "project_id" {
description = "Google Project ID."
type        = string
}

variable "bucket_name" {
description = "GCS Bucket name. Value should be unique ."
type        = string
}

variable "region" {
description = "Google Cloud region"
type        = string
default     = "europe-west2"
}

variable "force_destroy" {
    description = "Force-Destroy Value"  
    type = bool
}

