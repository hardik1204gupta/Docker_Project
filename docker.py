

#This is the code for the docker project

import os
while True:
    print("""\n\n\t**************************************************************
        ################# WELCOME TO THE DOCKER PROJECT  ####################
          \n\t**************************************************************
        \n\n \t Press keys to perform actions :
            
               Press 1: Docker Installation 
               Press 2: Docker Compose Installation
               Press 3: To launch Wordpress Site
               Press 4: To see the docker images present in your docker.
               Press 5: To pull the image of fedora
               Press 6: To launch fedora with interactive terminal
               Press 7: To see the all commands in docker
               Press 0: EXIT
               
    """)
    choice= int(input("\t\tEnter  your  Choice :"))
    
    if choice == 1:
        os.system("yum install docker-ce --nobest")
        print("Docker community version is installed successfully")
        input('Press enter to continue')
        os.system("clear")
    elif choice == 2:
        os.system('curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        os.system("chmod +x /usr/local/bin/docker-compose")
        input('Press enter to continue')
        os.system("clear")
    elif choice == 3:
        os.system("docker-compose up -d")
        input('Press enter to continue')
        os.system("clear")
    elif choice == 4:
        os.system("docker images")
        input('Press enter to continue')
        os.system("clear")
        
    elif choice == 5:
        os.system("docker pull fedora")
        input('Press enter to continue')
        os.system("clear")        
    elif choice == 6:
        os.system("docker run -i -t fedora")
        input('Press enter to continue')
        os.system("clear")
    elif choice == 7:
        os.system("docker --help")
        input('Press enter to continue')
        os.system("clear")
    elif choice == 0:
        exit(0)
    else:
        print("Enter the correct choice")    
