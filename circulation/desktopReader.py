import socket
import struct
import time

commands = 	{	'multiTagInventory': bytearray([10, 255, 2, 128, 117]), 
				'getTagData': bytearray([10, 255, 3, 65, 16, 163])
			}

def checkStatus(response):
	'''Fill with all status codes'''
	status = struct.unpack(">B", bytes([response[3]]))[0]
	if status != 0:
		raise Exception('Status failure.')

def sendCommand(cmd,readerIP, readerPort,s):
	
	print ('Sending:' + ' '.join('{:02x}'.format(x) for x in cmd))
	s.send(cmd)

	raw_response = s.recv(2048)
	response = bytearray(raw_response)
	print('Response: ' + ' '.join('{:02x}'.format(x) for x in response))
	checkStatus(raw_response)
	return raw_response


def getData(readerIP, readerPort):
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
                s.connect((readerIP, readerPort))
        except:
                raise Exception('NetworkError: Socket creation failed.')
        patron = ''
        books = []
        for i in range(5):
                response = sendCommand(commands['multiTagInventory'],readerIP, readerPort,s)
                count = struct.unpack(">h", bytes([response[4], response[5]]))[0]
	
                if count == 0:
                        continue
                        raise Exception('multiTagInventory failed: No tags in range')

                response = sendCommand(commands['getTagData'],readerIP, readerPort,s)[5:-1]


		## rewrite rest of the code using struct.unpack
                response = response[1:]
                for _ in range(count):
                    response = response[1:]
                    data = response[:12][::-1]
                    response = response[13:]
                    if bytearray(data[1])[0] == 0x9e:
                        raise Exception("WARNING: Attempted to read empty tag.")
                    if data[0] == 0x01:
                        data = data.decode()
                        if patron == '':
                         patron = ''.join([c if ord(c) != 0 else '' for c in data[1:]])
                    else:
                        data = data.decode()
                        data = ''.join([c if ord(c) != 0 else '' for c in data])
                        if data not in books:
                            books += [data]
        s.close()
        return {'patron':patron, 'books':books}

def getBooksList(readerIP, readerPort):
	return getData(readerIP, readerPort)['books']


def getPatronID(readerIP, readerPort):
	return getData(readerIP, readerPort)['patron']


def getPatronIDAndBooksList(readerIP, readerPort):
        r = getData(readerIP, readerPort)
        print(r['patron'])
        print(r['books'])
        return r



