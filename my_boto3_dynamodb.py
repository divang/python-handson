import boto3

def create_dynamoDB_table():
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.wait_until_exists()

    # Print out some data about the table.
    print(table.item_count)

def insert_data_dynamoDB_table():
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table('users')

    # Print out some data about the table.
    # This will cause a request to be made to DynamoDB and its attribute
    # values will be set based on the response.
    print(table.creation_date_time)

    table.put_item(
       Item={
                'username': 'janedoe',
                'first_name': 'Jane',
                'last_name': 'Doe',
                'age': 25,
                'account_type': 'standard_user',
            }
    )

def get_data_dynamoDB_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    response = table.get_item(
    Key={
        'username': 'janedoe',
                'last_name': 'Doe'
            }
        )
    item = response['Item']
    print(item)


#create_dynamoDB_table()
#insert_data_dynamoDB_table()
get_data_dynamoDB_table()