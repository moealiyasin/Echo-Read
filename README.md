# Echo Read 🎙️

Echo Read is a serverless AWS application that automatically converts uploaded text files into spoken audio using Amazon Polly.

## Overview

When a `.txt` file is uploaded to an Amazon S3 bucket:

1. Amazon S3 triggers an AWS Lambda function.
2. The Lambda function reads the text file.
3. Amazon Polly converts the text into speech.
4. The generated MP3 file is saved back into an S3 bucket.

This project demonstrates an event-driven serverless architecture using AWS.

---

## AWS Services Used

- AWS Lambda
- Amazon S3
- Amazon Polly
- AWS IAM
- Amazon CloudWatch

---

## Architecture

```text
Upload .txt file
        │
        ▼
   Amazon S3
        │
        ▼
 AWS Lambda Trigger
        │
        ▼
 Amazon Polly
        │
        ▼
Generate MP3
        │
        ▼
Amazon S3 Output Bucket
```

---

## Features

- Automatically processes uploaded text files
- Converts text into natural-sounding speech
- Stores generated MP3 files in Amazon S3
- Uses environment variables for configuration
- Uses IAM roles following AWS security best practices
- Logs execution with Amazon CloudWatch

---

## Technologies

- Python
- boto3
- AWS Lambda
- Amazon S3
- Amazon Polly

---

## Lessons Learned

This project helped me gain hands-on experience with:

- Event-driven serverless applications
- IAM roles and permissions
- S3 event triggers
- Lambda environment variables
- CloudWatch logging and debugging
- Integrating multiple AWS services into a complete workflow

---

## Future Improvements

- Add a web interface for file uploads
- Allow users to choose different Polly voices
- Support PDF and Word document conversion
- Deploy a frontend using Amazon S3 and CloudFront
- Add API Gateway for REST API access

---

## Author

**Mohamed Yasin**

AWS Certified Solutions Architect – Associate
