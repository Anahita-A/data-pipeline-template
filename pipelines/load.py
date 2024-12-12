import boto3
from io import BytesIO
from pipelines.params import Params

class Load():

    def write(self, csv, bucket: str, table: str) -> None:
        """
        Write Dataframe table to S3.

        Args:
            csv : The csv to be written.
            bucket (str): The name of the S3 bucket.
            table (str): The name of the file.

        Returns:
            None
        """

        # Initialize the MinIO client (boto3)
        minio_client = boto3.client(
            "s3",
            endpoint_url="http://10.7.0.5:9000",
            aws_access_key_id=Params.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Params.AWS_SECRET_ACCESS_KEY
        )
        
        try:
            minio_client.put_object(
                Bucket=bucket,
                Key=table,
                Body=BytesIO(csv),
                ContentLength=len(csv),
                ContentType="application/csv"
            )

        except Exception as e:
            print(e)

        return None