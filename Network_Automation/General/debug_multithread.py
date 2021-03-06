from netmiko import ConnectHandler
import config_modules
from multiprocessing.dummy import Pool as ThreadPool
import threading
import time

num_threads = 6

def main():

    #saving starting time
    start = time.time()

    #creating 2 dictionaries, one of devices and one of devices and passwords, keys are IP addresses
    devices_dict = config_modules.read_devices('devices.txt')
    devices_creds = config_modules.get_device_creds_unencrypted('password.txt')

    #configuring multi-threading
    config_threads_list = []
    config_param_list = []
    #keys are ip addresses
    for device in devices_dict:

        session = ConnectHandler( device_type=devices_dict[device]['type'], ip=devices_dict[device]['ipaddr'] ,
                                    username=devices_creds[device]['username'], password=devices_creds[device]['password'])
        config_param_list.append( session )

    #limiting threads
    threads = ThreadPool( num_threads )

    arp_results = threads.map(config_modules.debug_arp_cache, config_param_list)
    running_config_results = threads.map(config_modules.debug_running_config, config_param_list)

    threads.close()
    threads.join()

    #printing elapsed time
    print ( 'Time elapsed: {} seconds'.format(time.time() - start))

if __name__ == "__main__":
    main()

