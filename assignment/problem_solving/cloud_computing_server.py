def cloud_computing_server(num_of_req, req_list):
    server1 = 0
    for i in range(num_of_req):
        if i%2 == 0:
            server1 += int(req_list[i])
    print('Total number of memory units allocated/deallocated in server1 :',server1)
num_of_req = int(input('Enter number of requests'))
req_list = (input('Enter the requests :')).split()
cloud_computing_server(num_of_req, req_list)

