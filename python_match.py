http_status = 200
 
match http_status:
    case 200 | 201:
        print('success')
    case 400:
        print('bad request')
    case  500 | 501:
        print('server error')
    case _:
        print('unknown ')