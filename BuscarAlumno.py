import boto3


def lambda_handler(event, context):
    # Entrada (json)
    print(event)

    body = event['body']
    tenant_id = body['tenant_id']
    alumno_id = body['alumno_id']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    item = response.get('Item')

    if not item:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }

    # Salida (json)
    return {
        'statusCode': 200,
        'alumno': item
    }
