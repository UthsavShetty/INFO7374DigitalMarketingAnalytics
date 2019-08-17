//resource "aws_redshift_cluster" "default" {
//  cluster_identifier = "info7374clusteralycefinalproject-terraform"
//  database_name      = "mydb"
//  master_username    = "foo"
//  master_password    = "Mustbe8characters"
//  node_type          = "dc1.large"
//  cluster_type       = "single-node"
//  skip_final_snapshot = "true"
//}


resource "aws_redshift_cluster" "terraform" {
  cluster_identifier = "info7374clusteralycefinalproject-terraform1"
  database_name      = "info7374"
  master_username    = "testuser"
  master_password    = "T3stPass"
  node_type          = "dc2.large"
  cluster_type       = "single-node"
  cluster_subnet_group_name = "default"
  skip_final_snapshot = true
  publicly_accessible = true
  //iam_roles = ["${aws_iam_role.test_pipeline_role.arn}"]

}

//resource "aws_kinesis_firehose_delivery_stream" "test_pipeline_firehose" {
//  name        = "test_pipeline_firehose"
//  destination = "redshift"
//
//  s3_configuration {
//    role_arn   = "${aws_iam_role.info7374_try.arn}"
//    bucket_arn = "${aws_s3_bucket.storage.arn}"
//    buffer_interval = 60
//  }
//
//  redshift_configuration {
//    role_arn           = "${aws_iam_role.info7374_try.arn}"
//    cluster_jdbcurl    = "jdbc:redshift://${aws_redshift_cluster.terraform.endpoint}/${aws_redshift_cluster.terraform.database_name}"
//    username           = "${aws_redshift_cluster.terraform.master_username}"
//    password           = "${aws_redshift_cluster.terraform.master_password}"
//    data_table_name    = "data"
//    copy_options       = "json 's3://${aws_s3_bucket.storage.bucket}/${aws_s3_bucket_object.jsonpath_config.key}' region '${data.aws_region.current.name}' timeformat 'auto'"
//  }
//}