import time
import requests
#detect if someone is in the scene

session = requests.Session()

def getData(list):
    ntopng_web_interface = session.get('http://localhost:3000')
    ip_cam = session.get('https://www.insecam.org/en/view/704630/')
    json_page = session.get('http://localhost:3000/lua/host_get_json.lua?ifid=0&host=187.132.30.175')

    data = json_page.json()

    print(str(round(data["throughput_bps"])) + " bps")
    list.append(data['throughput_bps'])

    #check for movement
    length = len(list)-1

    difference = list[length] - list[(length - 1)]

    #if throughput is above 100000 bps
    if list[length] >= 100000:
        if difference > 25000 and length !=1: #prevent false detection from first run
            print("person in frame has been detected at: " + time.strftime("%H:%M:%S"))

    #if throughput is between 50000 and 100000
    if list[length] >= 50000 and length < 100000:
        if difference > 17000 and length !=1:
            print("person in frame has been detected at: " + time.strftime("%H:%M:%S"))

    #if throughput is between 0 and 50000
    if list[length] >= 0 and list[length] < 50000:
        if difference > 10000 and length != 1:
            print("person in frame has been detected at: " + time.strftime("%H:%M:%S"))



def main():
    list = [0] #store throughput in a list

    t_end = time.time() + 60 * 15    #run for x amount of minutes
    while time.time() < t_end:
        getData(list)
        time.sleep(4)


main()





