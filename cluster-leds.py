# This is the simple example provided in the Dispy documentation
# If this code runs, it means your OctaPi cluster is working correctly
# You should see a result similar to this:
#
#                           Node |  CPUs |    Jobs |    Sec/Job | Node Time Sec
#------------------------------------------------------------------------------
# 192.168.1.49 (raspberrypi)     |     4 |       4 |     16.040 |        64.160
# 192.168.1.202 (raspberrypi)    |     4 |       2 |     12.031 |        24.062
# 192.168.1.191 (raspberrypi)    |     4 |       2 |     13.029 |        26.058
# 192.168.1.223 (raspberrypi)    |     4 |       0 |      0.000 |         0.000
# 192.168.1.116 (raspberrypi)    |     4 |       2 |     10.025 |        20.050
# 192.168.1.27 (raspberrypi)     |     4 |       2 |     15.535 |        31.070
# 192.168.1.167 (raspberrypi)    |     4 |       4 |     14.537 |        58.148
# 192.168.1.50 (raspberrypi)     |     4 |       0 |      0.000 |         0.000
#
#Total job time: 223.548 sec, wall time: 20.245 sec, speedup: 11.042

# Dispy:
# Giridhar Pemmasani, "dispy: Distributed and parallel Computing with/for Python",
# http://dispy.sourceforge.net, 2016


# 'compute' is distributed to each node running 'dispynode'
def compute(n, colour):
    import time, socket, random

    # Make array of colors with values
    colours = {
        'red': [255, 0, 0],
        'orange': [255, 165, 0],
        'yellow': [255, 255, 0],
        'green': [0, 255, 0],
        'blue': [0, 0, 255],
        'indigo': [75, 0, 130],
        'violet': [238, 130, 238],
        'purple': [126, 25, 156]
    }

    sense = None
    sense_available = False
    error_msg = ""

    # Try to initialize Sense HAT and report if not available
    try:
        from sense_hat import SenseHat
        sense = SenseHat()
        sense_available = True
    except Exception as e:
        error_msg = f"[!] Sense HAT not available or failed to initialize: {e}"

    if sense_available:
        try:
            # Show custom pixel pattern
            #sense.show_message(f"{n}", text_colour=[0, 255, 0])
            #GREEN
            #sense.set_pixels([[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[5, 63, 0],[5, 63, 0],[9, 123, 0],[0, 173, 19],[0, 173, 19],[0, 173, 19],[0, 173, 19],[9, 123, 0],[5, 63, 0],[5, 63, 0],[9, 123, 0],[0, 173, 19],[15, 255, 0],[15, 255, 0],[0, 173, 19],[9, 123, 0],[5, 63, 0],[5, 63, 0],[9, 123, 0],[0, 173, 19],[15, 255, 0],[15, 255, 0],[0, 173, 19],[9, 123, 0],[5, 63, 0],[5, 63, 0],[9, 123, 0],[0, 173, 19],[0, 177, 16],[0, 173, 19],[0, 173, 19],[9, 123, 0],[5, 63, 0],[5, 63, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[9, 123, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0],[5, 63, 0]])
            #sense.set_pixels([[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[148, 35, 181],[148, 35, 181],[148, 35, 181],[148, 35, 181],[148, 35, 181],[148, 35, 181],[126, 25, 156],[126, 25, 156],[148, 35, 181],[186, 80, 217],[186, 80, 217],[186, 80, 217],[186, 80, 217],[148, 35, 181],[126, 25, 156],[126, 25, 156],[148, 35, 181],[186, 80, 217],[219, 125, 247],[219, 125, 247],[186, 80, 217],[148, 35, 181],[126, 25, 156],[126, 25, 156],[148, 35, 181],[186, 80, 217],[219, 125, 247],[219, 125, 247],[186, 80, 217],[148, 35, 181],[126, 25, 156],[126, 25, 156],[148, 35, 181],[186, 80, 217],[186, 80, 217],[186, 80, 217],[186, 80, 217],[148, 35, 181],[126, 25, 156],[126, 25, 156],[148, 35, 181],[148, 35, 181],[148, 35, 181],[148, 35, 181],[148, 35, 181],[148, 35, 181],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156],[126, 25, 156]])
            sense.set_pixels([[172,35,117],[157,39,110],[138,43,100],[118,40,87],[95,38,72],[73,31,56],[73,31,56],[73,31,56],[157,39,110],[73,31,56],[95,38,72],[90,13,59],[73,31,56],[157,39,110],[172,35,117],[73,31,56],[138,43,100],[95,38,72],[118,40,87],[73,31,56],[73,31,56],[172,35,117],[157,39,110],[73,31,56],[118,40,87],[118,40,87],[138,43,100],[157,39,110],[172,35,117],[157,39,110],[138,43,100],[95,38,72],[95,38,72],[138,43,100],[157,39,110],[172,35,117],[157,39,110],[138,43,100],[118,40,87],[118,40,87],[73,31,56],[157,39,110],[172,35,117],[73,31,56],[73,31,56],[118,40,87],[95,38,72],[138,43,100],[73,31,56],[172,35,117],[157,39,110],[73,31,56],[90,13,59],[95,38,72],[73,31,56],[157,39,110],[73,31,56],[73,31,56],[73,31,56],[95,38,72],[118,40,87],[138,43,100],[157,39,110],[172,35,117]])
    
            # Set background colour
            if colour == 'random':
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                sense.clear(r, g, b)
            elif colour in colours:
                sense.clear(colours[colour])
        except Exception as e:
            error_msg = f"[!] Error interacting with Sense HAT: {e}"
            sense_available = False  # Treat as failed state

    # Simulate a job by sleeping
    time.sleep(n)

    # Clear display if Sense HAT was used
    if sense_available:
        try:
            sense.clear()
        except Exception:
            pass

    host = socket.gethostname()
    # Return host and job duration; append error message if Sense HAT failed
    return (f"{host} (no Sense HAT)" if not sense_available else host, n, error_msg)


if __name__ == '__main__':
    import dispy, random, socket, argparse
    # fetch the IP address of the client
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80)) # doesn't matter if 8.8.8.8 can't be reached
    # Create the cluster and define IPs or a range
    cluster = dispy.JobCluster(compute,host=s.getsockname()[0], nodes=['192.168.*.*', '192.168.137.*'])

    # import dispy's httpd module, create http server for this cluster
    import dispy.httpd
    http_server = dispy.httpd.DispyHTTPServer(cluster)
    # Go to http://<CLIENT-IP>:8181 when cluster is running to see the status of the cluster

    # Argument Parser Setup
    # -----------------------
    # This part is responsible for parsing the command line arguments
    # ========================================================
    parser = argparse.ArgumentParser()
    parser.add_argument('--colour', type=str, help='colour', required=False, default='green')
    parser.add_argument('--clusterjobs', type=int, help='number of jobs', required=False, default=32)
    parser.add_argument('--jobslength', type=int, help='jobs length', required=False, default=0)
    args = parser.parse_args()
    # eg: print(args.colour)
    
    jobs = []
    for i in range(args.clusterjobs):
        # schedule execution of 'compute' on a node (running 'dispynode')
        # with a parameter (random number in this case)
        joblength = random.randint(1,5)
        if args.jobslength != 0:
            joblength = args.jobslength
        job = cluster.submit(joblength, args.colour)
        job.id = i # optionally associate an ID to job (if needed later)
        jobs.append(job)
    # cluster.wait() # waits for all scheduled jobs to finish
    for job in jobs:
        result = job()
        # Improved result handling
        if isinstance(result, tuple):
            if len(result) == 3:
                host, n, message = result
                if message:
                    print(f"[!] {host} ({job.ip_addr}) ran for {n} seconds: {message}")
                else:
                    print(f"[+] {host} ({job.ip_addr}) ran for {n} seconds successfully.")
            elif len(result) == 2:
                host, n = result
                print(f"[+] {host} ({job.ip_addr}) ran for {n} seconds successfully.")

    print('---------------------------------------------------------------------------------\n')    
    cluster.print_status()
    cluster.close()
