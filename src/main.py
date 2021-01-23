def lambda_handler(event, context):
    """
    Método inicial da api

    :param event:
        Evento vindo da AWS
    :param context:
        Contexto de execução da função
    :return:
        Um string com valor de `Hello`
    """

    return 'Hello'

def par():

    return 4

if __name__ == '__main__':
    event = None
    context = None

    print(lambda_handler(
        event=event,
        context=context
    ))
