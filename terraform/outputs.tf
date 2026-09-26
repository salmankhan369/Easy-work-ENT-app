output "cluster_name" {
  value = aws_eks_cluster.eks.name
}

output "cluster_endpoint" {
  value = aws_eks_cluster.eks.endpoint
}

output "ecr_frontend_repository_url" {
  value = aws_ecr_repository.frontend_repo.repository_url
}

output "ecr_backend_repository_url" {
  value = aws_ecr_repository.backend_repo.repository_url
}