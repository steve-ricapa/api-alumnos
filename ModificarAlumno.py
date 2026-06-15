import boto3


def lambda_handler(event, context):
    # Entrada (json)
    print(event)

    body = event['body']

    tenant_id = body['tenant_id']
    alumno_id = body['alumno_id']
    nombres = body['nombres']
    apellidos = body['apellidos']
    email = body['email']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression='SET nombres = :n, apellidos = :a, email = :e',
        ExpressionAttributeValues={
            ':n': nombres,
            ':a': apellidos,
            ':e': email
        }
    )

    # Salida (json)
    return {
        'statusCode': 200,
        'message': 'Alumno modificado correctamente',
        'alumno': {
            'tenant_id': tenant_id,
            'alumno_id': alumno_id,
            'nombres': nombres,
            'apellidos': apellidos,
            'email': email
        }
    }
