import requests
import json
import info_account

def get_ticket():
    url_ticket = info_account.base_url + "/ticket"
    header = {
            "Content-Type":"application/json"
        }
    body = json.dumps({                               # Ép kiểu dữ liệu về kiểu JSON 
            "username":info_account.username,
            "password":info_account.password
        })
    send_request = requests.post(url_ticket, headers = header, data=body, verify=False)
    response = send_request.json()
    ticket = response["response"]["serviceTicket"]
    return ticket
def get_list_networkdevice():
    url_networkdevice = info_account.base_url + "/network-device"
    headers = {
        "x-auth-token": get_ticket()
    }
    devices = requests.get(url_networkdevice, headers = headers, verify=False)
    response = json.dumps(devices.json(), indent=4)
    data = devices.json()
    return response
def get_device_config():
    url_networkdevice_config = info_account.base_url + "/network-device/config"
    headers = {
        "x-auth-token": get_ticket()
    }
    devices = requests.get(url_networkdevice_config, headers = headers, verify=False)
    response = json.dumps(devices.json(), indent=4)
    return response
def get_id_device():
    data = get_list_networkdevice()
    device_num = len(data["response"])
    for i in range(device_num):
        print(data["response"][i]["id"])
if __name__ == "__main__":
    # print(get_ticket())
    print(get_list_networkdevice())
    # print(get_device_config())
    # get_id_device()