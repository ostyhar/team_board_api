# AWS Account Setup Notes

## Purpose

This document captures the Slice 1 AWS task for TeamBoard API.

The goal is **cost safety and account readiness**, not deployment.

TeamBoard API will eventually use AWS for deployment architecture, PostgreSQL hosting, file storage, background jobs, logs, secrets, and reliability practice. But in Slice 1, AWS work is intentionally limited to safe setup notes.

---

## Slice 1 boundary

For Slice 1:

```text
AWS work = account safety + documentation only
```

Do not deploy TeamBoard API to AWS yet.

Do not create production infrastructure yet.

Do not create RDS, ECS, ALB, NAT Gateway, S3 production buckets, or Route 53 records yet unless a later slice explicitly requires it.

---

## Cost-safety checklist

Before doing AWS labs, verify:

```text
[ ] Root account is secured
[ ] MFA is enabled on the root account
[ ] Daily work does not use the root account
[ ] Budget alert is configured
[ ] Billing access is available
[ ] AWS region choice is understood
[ ] AWS CLI or CloudShell access is checked
[ ] No long-running paid resources are left after labs
```

---

## Recommended initial AWS safety steps

### 1. Secure root account

Use the root account only for account-level tasks.

Root account should not be used for daily learning or development.

Checklist:

```text
[ ] Strong password
[ ] MFA enabled
[ ] Recovery options configured
[ ] Root access keys not created
```

If root access keys exist and are not required, remove them.

---

### 2. Enable MFA

Enable MFA for:

```text
root account
admin IAM user, if created
```

Reason:

```text
MFA protects the account if a password is leaked.
```

---

### 3. Create budget alert

Create an AWS Budget to avoid surprise charges.

Suggested first budget:

```text
Monthly cost budget: low amount appropriate for learning
Alert threshold: 50%, 80%, 100%
Email notification: enabled
```

The exact amount depends on personal preference, but the important part is that alerts exist before hands-on labs become larger.

---

### 4. Avoid root user for daily work

Use root only for account setup.

For daily work, use one of:

```text
IAM admin user for learning
IAM Identity Center user
CloudShell with appropriate permissions
```

Later, production-style access should use least privilege, not broad admin permissions.

---

### 5. Prefer temporary learning resources

When doing labs later:

```text
create resource
test concept
write notes
delete resource
confirm billing-sensitive services are stopped
```

Pay special attention to resources that can create ongoing cost:

```text
NAT Gateway
RDS instances
EC2 instances
Load Balancers
EBS volumes
Elastic IPs
CloudWatch logs at high volume
S3 storage and requests
```

---

## Services to avoid creating in Slice 1

Do not create these yet for TeamBoard:

```text
RDS PostgreSQL
ECS cluster
ALB
NAT Gateway
Route 53 hosted zone
CloudFront distribution
Production S3 buckets
SQS queues
Secrets Manager secrets
KMS customer-managed keys
```

Reason:

```text
Slice 1 is local FastAPI skeleton and tooling. AWS deployment and managed services come later.
```

---

## Future TeamBoard AWS architecture

Target direction later:

```text
User / API Client
  -> Route 53
  -> ALB
  -> ECS Fargate or EC2
  -> FastAPI app
  -> RDS PostgreSQL
  -> S3 for task files
  -> SQS for background jobs
  -> Worker service
  -> CloudWatch logs and alarms
  -> Secrets Manager / SSM Parameter Store
  -> KMS encryption
```

This future architecture should be introduced gradually through later slices.

---

## AWS topics mapped to TeamBoard later

```text
IAM
  -> least privilege, roles, no hardcoded access keys

VPC
  -> public/private subnets, private RDS

EC2
  -> simple first deployment option

ECS/Fargate
  -> portfolio-ready container deployment option

RDS
  -> managed PostgreSQL for TeamBoard data

S3
  -> task file attachments

SQS
  -> background jobs and notifications

CloudWatch
  -> logs, metrics, alarms

Secrets Manager / SSM Parameter Store
  -> database credentials and app secrets

KMS
  -> encryption

ALB
  -> public HTTP entry point

Route 53
  -> DNS
```

---

## Current Slice 1 AWS decision

For Slice 1:

```text
No AWS deployment.
No paid infrastructure.
Only account safety notes and future architecture awareness.
```

Reasoning:

```text
The local FastAPI skeleton must be stable before cloud deployment is useful.
```

---

## Later AWS learning artifacts

Later slices should create or update:

```text
docs/aws/teamboard-compute-options.md
docs/aws/networking-design.md
docs/aws/teamboard-rds-design.md
docs/aws/teamboard-s3-files.md
docs/aws/teamboard-async-jobs.md
docs/aws/teamboard-security.md
docs/aws/teamboard-observability.md
docs/aws/teamboard-dr-plan.md
docs/aws/teamboard-cost-notes.md
docs/aws/teamboard-aws-architecture.md
```

For now, this file is enough.

---

## Slice 1 done criteria related to AWS

This AWS part is done when:

```text
[ ] account safety checklist exists
[ ] MFA/budget/root-user principles are documented
[ ] no AWS deployment is attempted
[ ] future AWS direction is briefly captured
```
