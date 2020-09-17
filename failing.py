def lambda_handler(event, context):
    print_record_keys(event)
    return 'OK'

def print_record_keys(event):
    for r in event['Records'] #contains syntax error here
        print(r['dynamodb']['Keys'])

