# 1. Define the Variable
variable "project_id" {
  description = "The ID of the Google Cloud project"
  type        = string
}

provider "google" {
  project = var.project_id
  region  = "us-central1"
}

# 2. Create a VPC Network
resource "google_compute_network" "vpc" {
  name                    = "genai-vpc"
  auto_create_subnetworks = false
}

# 3. Create a Subnet
resource "google_compute_subnetwork" "subnet" {
  name          = "genai-subnet"
  region        = "us-central1"
  network       = google_compute_network.vpc.name
  ip_cidr_range = "10.10.0.0/24"
}

# 4. Create the GKE Cluster
resource "google_container_cluster" "primary" {
  name     = "genai-cluster"
  location = "us-central1-a"

  # We want a small cluster to start (Cost efficient)
  initial_node_count = 1

  network    = google_compute_network.vpc.name
  subnetwork = google_compute_subnetwork.subnet.name

  # Enabling Workload Identity (Make sure this appears ONLY ONCE)
  workload_identity_config {
    workload_pool = "${var.project_id}.svc.id.goog"
  }
  
  deletion_protection = false
}

# 5. Create the Node Pool (The actual VMs)
resource "google_container_node_pool" "primary_nodes" {
  name       = "genai-node-pool"
  location   = "us-central1-a"
  cluster    = google_container_cluster.primary.name
  node_count = 2

  node_config {
    machine_type = "e2-standard-4"
    
    # Reduced disk size to fit your regional quota (Fixes the 403 Error)
    disk_size_gb = 60
    
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
