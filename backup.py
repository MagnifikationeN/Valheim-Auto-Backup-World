import os,os.path,sys,shutil,time
from datetime import datetime
from os import path

user = sys.argv[1]
worldName = sys.argv[2]

if path.exists('C:/Users/' + user + '/AppData/LocalLow/IronGate/Valheim/Backup/'):
    True
else:
    print('Created Backup folder in C:/Users/' + user + '/AppData/LocalLow/IronGate/Valheim/')
    os.mkdir('C:/Users/' + user + '/AppData/LocalLow/IronGate/Valheim/Backup/')

while True:
    
    timern = datetime.now()
    location = 'C:/Users/' + user + '/AppData/LocalLow/IronGate/Valheim/Backup/'
    foldername = timern.strftime("%Y-%m-%d,%H-%M-%S")

    finalDir = location + foldername

    os.mkdir(finalDir)
    os.chmod(finalDir,0o666)

    worldDb = r'C:/Users/' + user + '/AppData/LocalLow/IronGate/Valheim/worlds/'+ worldName +'.db'
    worldFwl = r'C:/Users/' + user + '/AppData/LocalLow/IronGate/Valheim/worlds/'+ worldName +'.fwl'

    shutil.copyfile(worldDb, finalDir + '/' + worldName + '.db')
    shutil.copyfile(worldFwl, finalDir + '/' + worldName + '.fwl')

    print(f'Created backup: {foldername}')
    time.sleep(3600)

