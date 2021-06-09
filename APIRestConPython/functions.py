import jwt
from APIRestConPython.settings import SIMPLE_JWT

def get_data_from_header(auth_header):
    auth_header = auth_header.split('Bearer ')[1]
    res = jwt.decode(auth_header, SIMPLE_JWT['SIGNING_KEY'], algorithms=[SIMPLE_JWT['ALGORITHM']],)
    print(res)
    return res