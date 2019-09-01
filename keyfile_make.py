###################################################
# FD1094 Keyfile Maker rev1.0
#                      copyright 2019 @V9938
###################################################
# Extract EncryptionKey from ArcadeHacker's code.
# https://github.com/ArcadeHacker/ArcadeHacker_Sega_Hitachi
#
# Format: +0000-0FFF : Title
#         +1000-2FFF : FD1094 EncryptionKey
#               *4K Align for SD card access
import re

path = 'ArcadeHacker_Sega_FD1094.ino'
with open('cryptkey.dat',mode='bw') as binfile :
	with open(path,mode='r') as file:
		line = file.readline()
		while line :
			list = re.split('["{},]',line)
			if (list[0].find('*Game') != -1):
				ByteData = bytearray([0]) * 12288
				#Title part (0-FFF)
				s = list[1]
				for i in range(len(list[1])):
					ByteData[i] = ord(s[i])
				#EncryptionKey (1000-2FFF)
				for i in range(8192):
					s = list[3+i]
					ByteData[i+4096] = int(s,16)
				binfile.write(ByteData)
				ByteData.clear()
			line = file.readline()

