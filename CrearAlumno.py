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

    table.put_item(
        Item={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id,
            'nombres': nombres,
            'apellidos': apellidos,
            'email': email
        }
    )

    # Salida (json)
    return {
        'statusCode': 200,
        'message': 'Alumno creado correctamente',
        'alumno': {
            'tenant_id': tenant_id,
            'alumno_id': alumno_id,
            'nombres': nombres,
            'apellidos': apellidos,
            'email': email
        }
    }
