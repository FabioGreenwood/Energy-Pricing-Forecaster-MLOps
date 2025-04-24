resource "aws_ecs_task_definition" "return-prediction" {
  family                = "return-prediction"
  task_role_arn         = "${var.aws_account_id}"
  container_definitions = file("docker/return_prediction/container_definition.json")

  volume {
    name = "return-prediction"

    docker_volume_configuration {
      scope         = "task"
      autoprovision = true
      driver        = "local"

      driver_opts = {
        "type"   = "nfs"
        "device" = "${aws_efs_file_system.fs.dns_name}:/"
        "o"      = "addr=${aws_efs_file_system.fs.dns_name},rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport"
      }
    }
  }
}