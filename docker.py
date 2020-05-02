

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
               Press 7: To see all commands available for docker
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
        while True:
            os.system("clear")
            print("\n\nif you don't have wordpress and mysql image then follow these steps:\n\n")
            print("\n\t\tpress 1: for wordpress image ")
            print("\t\tpress 2: for mysql image")
            print("\n\n\tif you already have these images then follow to launch wordress ")
            print("\n\t\tpress 3: for launch wordpress server\n\n\n")
            print("\n\n\tpress 0: Back to main menu")
            choice1 = int(input("Enter your choice : "))
            if choice1 == 1:
                os.system("docker pull wordpress:5.1.1-php7.3-apache")
            elif choice1 == 2:
                os.system("docker pull mysql:5.1")
            elif choice1 == 3:
                os.system("docker-compose up -d")
            elif choice1 == 0:
                exit(1)
            else:
                print("oops wrong input try again.....................")
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
