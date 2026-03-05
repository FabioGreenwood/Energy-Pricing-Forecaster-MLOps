resource "aws_cloudwatch_event_rule" "hourly-return-prediction" {
  name        = "hourly-return-prediction"
  description = "hourly forcast of prediction"
  schedule_expression = "rate(60 minutes)"
  role_arn = aws_iam_role.ML-tasks.arn
}

resource "aws_cloudwatch_event_target" "sns" {
  #this assigns a cloudwatch to the task?
  rule      = aws_cloudwatch_event_rule.hourly-return-prediction.name
  target_id = "aws_cloudwatch_event_target-target_id"
  arn       = aws_ecs_task_definition.return-prediction.arn # this will be the task definition of the return prediction
}

### the below must be rewrote
resource "aws_sns_topic" "aws_logins" {
  name = "aws-console-logins"
}

resource "aws_sns_topic_policy" "default" {
  arn    = aws_sns_topic.aws_logins.arn
  policy = data.aws_iam_policy_document.sns_topic_policy.json
}

data "aws_iam_policy_document" "sns_topic_policy" {
  statement {
    effect  = "Allow"
    actions = ["SNS:Publish"]

    principals {
      type        = "Service"
      identifiers = ["events.amazonaws.com"]
    }

    resources = [aws_sns_topic.aws_logins.arn]
  }
}