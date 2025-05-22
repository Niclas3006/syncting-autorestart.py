import datetime, time, requests
from time import sleep


syncthing_api_key= ""
restart_url= "http://0.0.0.0:8384/rest/system/restart" # syncthing is started to bind to 0.0.0.0:8384
ping_url= "http://0.0.0.0:8384/rest/system/ping"



terminate = False
last_poll = 404
print("\n\n\n\n\n\n")

def status_print(action,status="Active"):
    global terminate  
    global last_poll
    
    print(f" ====== \nStatus: {status}\t\t\nAction: {action}\t\t\nPolled: {last_poll}\t\t\nTerminate: {terminate}\t\t\nTimestamp: {datetime.datetime.now()}\t\t\n ======",end = '')
    #print(f'\x1b[6A\r', end='')





def main():
    global terminate  
    global last_poll
    while not terminate:
        while (not terminate) and not ((datetime.datetime.now().second <= 5) and (datetime.datetime.now().minute == 0)):
            try:
                status_print("running")
                time.sleep(60- datetime.datetime.now().second)
                last_poll=requests.post(url=ping_url,headers={"X-API-Key":syncthing_api_key}).status_code
            except requests.exceptions.ConnectionError as e:    # This is the correct syntax
                print(e)
                terminate = True   

        try:
            status_print("restarting")
            print(requests.post(url=restart_url,headers={"X-API-Key":syncthing_api_key}))
        except requests.exceptions.ConnectionError as e:    # This is the correct syntax
           # print(e)
            pass #terminate = True 
        sleep(10)
    status_print("terminating","terminated")
    sleep(60)

main()
