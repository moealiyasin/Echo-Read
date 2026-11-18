
import boto3
import json
import os
import logging
from urllib.parse import unquote_plus
from pathlib import PurePosixPath

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
s3 = boto3.client('s3')
polly = boto3.client('polly')


def lambda_handler(event, context):

    # Retrieve bucket names from environment variables
    source_bucket = os.environ['SOURCE_BUCKET']
    destination_bucket = os.environ['DESTINATION_BUCKET']

    # Process incoming S3 records
    for record in event.get('Records', []):

        try:
            # Extract and decode uploaded filename
            object_key = unquote_plus(
                record['s3']['object']['key']
            )

            logger.info(f"Received file: {object_key}")

            # Only process TXT files
            if not object_key.lower().endswith('.txt'):
                logger.info(f"Skipping non-text file: {object_key}")
                continue

            # Generate output filename
            audio_key = str(
                PurePosixPath(object_key).with_suffix('.mp3')
            )

            # Retrieve text file from S3
            logger.info(f"Reading file from S3: {object_key}")

            response = s3.get_object(
                Bucket=source_bucket,
                Key=object_key
            )

            text = response['Body'].read().decode('utf-8')

            if not text.strip():
                logger.warning("Text file is empty. Skipping.")
                continue

            # Convert text to speech using Amazon Polly
            logger.info("Sending text to Amazon Polly")

            polly_response = polly.synthesize_speech(
                Text=text,
                OutputFormat='mp3',
                VoiceId='Joanna'
            )

            # Upload generated audio directly to S3
            if 'AudioStream' in polly_response:

                audio_data = polly_response['AudioStream'].read()

                s3.put_object(
                    Bucket=destination_bucket,
                    Key=audio_key,
                    Body=audio_data,
                    ContentType='audio/mpeg'
                )

                logger.info(
                    f"Audio successfully uploaded: {audio_key}"
                )

            logger.info(
                f"Conversion completed: {object_key}"
            )

        except Exception as error:
            logger.exception(
                f"Failed to process S3 record: {str(error)}"
            )
            raise

    return {
        'statusCode': 200,
        'body': json.dumps(
            'Text-to-Speech processing completed.'
        )
    }
