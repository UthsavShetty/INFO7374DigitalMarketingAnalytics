resource "aws_s3_bucket" "log_bucket_info7374" {
  bucket = "log-bucket-info7374"
  acl    = "log-delivery-write"
}

resource "aws_s3_bucket" "storage" {
  bucket = "info7374s3alycefinalproject-terraform"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }

  versioning {
    enabled = true
  }

  logging {
    target_bucket = "${aws_s3_bucket.log_bucket_info7374.id}"
    target_prefix = "log/"
  }

}

data "aws_iam_policy_document" "initial-policy" {
  statement {
    sid = "1"

    actions = [
      "s3:ListAllMyBuckets",
      "s3:GetBucketLocation",
    ]

    resources = [
      "arn:aws:s3:::*",
    ]
  }

  statement {
    actions = [
      "s3:ListBucket",
    ]

    resources = [
      "arn:aws:s3:::${aws_s3_bucket.storage.id}",
    ]

    condition {
      test     = "StringLike"
      variable = "s3:prefix"

      values = [
        "",
        "home/",
        "home/&{aws:username}/",
      ]
    }
  }

  statement {
    actions = [
      "s3:*",
    ]

    resources = [
      "arn:aws:s3:::${aws_s3_bucket.storage.id}/home/&{aws:username}",
      "arn:aws:s3:::${aws_s3_bucket.storage.id}/home/&{aws:username}/*",
    ]
  }
}

resource "aws_iam_policy" "initial-policy" {
  name   = "policy"
  path   = "/"
  policy = "${data.aws_iam_policy_document.initial-policy.json}"
}

