import requests
import time
import pickle


session = requests.Session()


def getData(list):
    ntopng_web_interface = session.get('http://localhost:3000')
    ip_cam = session.get('https://www.insecam.org/en/view/704779/')
    json_page = session.get('http://localhost:3000/lua/host_get_json.lua?ifid=0&host=187.170.90.179')


    data = json_page.json()

    print(round(data["throughput_bps"]) , ('{:>11}'.format(time.strftime("%H:%M:%S"))))
    #list[(round(data["throughput_bps"]))] = time.strftime("%H:%M:%S")
    return list.update({ data["throughput_bps"] : time.strftime("%H:%M:%S") })


def main():
    list = {} #store throughput in a list

    print ('{:10}'.format('Throughput') + "Time")

    t_end = time.time() + 60 * 1    #run for x amount of minutes
    while time.time() < t_end:
        getData(list)
        time.sleep(10)

    with open("CSC495data.json", "wb") as fp:
        pickle.dump(list,fp)

    print("Data collection completed")

main()


# these values are nested not sure how to access them
#print lookup(data, *['ndpiStats', 'categories', 'Unspecified', 'bytes_sent'])
#print(data["bytes_rcvd"])



