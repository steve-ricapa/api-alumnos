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

    table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    # Salida (json)
    return {
        'statusCode': 200,
        'message': 'Alumno eliminado correctamente',
        'alumno': {
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    }
