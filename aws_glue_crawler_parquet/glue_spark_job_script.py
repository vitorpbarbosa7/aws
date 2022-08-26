import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="debo_db",
    table_name="iris_iris",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("sepal_length", "double", "sepal_length", "double"),
        ("sepal_width", "double", "sepal_width", "double"),
        ("petal_length", "double", "petal_length", "double"),
        ("petal_width", "double", "petal_width", "double"),
        ("class", "string", "class", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Amazon S3
AmazonS3_node1661548889617 = glueContext.getSink(
    path="s3://aws-glue-vpb/iris/parquet/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1661548889617",
)
AmazonS3_node1661548889617.setCatalogInfo(
    catalogDatabase="debo_db", catalogTableName="iris_parquet"
)
AmazonS3_node1661548889617.setFormat("glueparquet")
AmazonS3_node1661548889617.writeFrame(ApplyMapping_node2)
job.commit()

