resource "aws_dynamodb_table" "dynamodb-table-service" {
  name           = "FinalAlyce_services_try"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "service_id"
  range_key      = "service_name"

  attribute {
    name = "service_id"
    type = "N"
  }

  attribute {
    name = "service_name"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

//  global_secondary_index {
//    name               = "NameIndex"
//    hash_key           = "service_name"
//    range_key          = "TopScore"
//    write_capacity     = 10
//    read_capacity      = 10
//    projection_type    = "INCLUDE"
//    non_key_attributes = ["UserId"]
//  }

}

resource "aws_dynamodb_table" "dynamodb-table-gift" {
  name           = "FinalAlyce_gift_try"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "gift_id"
  range_key      = "gift_name"

  attribute {
    name = "gift_id"
    type = "N"
  }

  attribute {
    name = "gift_name"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  //  global_secondary_index {
  //    name               = "NameIndex"
  //    hash_key           = "service_name"
  //    range_key          = "TopScore"
  //    write_capacity     = 10
  //    read_capacity      = 10
  //    projection_type    = "INCLUDE"
  //    non_key_attributes = ["UserId"]
  //  }

}

resource "aws_dynamodb_table" "dynamodb-table-client" {
  name           = "FinalAlyce_client_try"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "client_id"
  range_key      = "client_name"

  attribute {
    name = "client_id"
    type = "N"
  }

  attribute {
    name = "client_name"
    type = "S"
  }

  attribute {
    name = "client_sector"
    type = "S"
  }

  attribute {
    name = "client_city"
    type = "S"
  }

  attribute {
    name = "client_statecode"
    type = "S"
  }

  attribute {
    name = "client_zipcode"
    type = "N"
  }

  attribute {
    name = "if_present?"
    type = "S"
  }

  attribute {
    name = "if_not_present?"
    type = "S"
  }

  attribute {
    name = "recommend?"
    type = "N"
  }

  attribute {
    name = "client_subscription"
    type = "S"
  }

  attribute {
    name = "client_acquisition_source"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  //  global_secondary_index {
  //    name               = "NameIndex"
  //    hash_key           = "service_name"
  //    range_key          = "TopScore"
  //    write_capacity     = 10
  //    read_capacity      = 10
  //    projection_type    = "INCLUDE"
  //    non_key_attributes = ["UserId"]
  //  }

}

