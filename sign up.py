








while True:

    while True:

        print("form sabt nam")

    
        while True:

            esm = input("esme khod ra vared konid:")

            if esm == "" or esm == " " or esm == "  " or esm == "   ":
                print("esmo nazadi")
                continue

            if esm.isalpha() == False:
                print("gheir ghabel ghabool")
                continue

            if esm.islower() == False:
                print("gheir ghabel ghabool")
                continue

            if esm.isalpha() == True:
                if esm.islower() == True: 
                    print("ghabel ghabool")
                    break

                else:
                    print("gheir ghabel ghabool")
                    continue
                

                                                                 
        while True:

            phone_number = input("shomare tamas khod ra vared konid:")

            if phone_number == "" or phone_number == " " or phone_number == "  " or phone_number == "   ":
                print("shomare tamas nazadi")
                continue

            if phone_number.isalnum() == False:
                print("gheir ghabel ghabool")
                continue

            if len(phone_number) != 11:
                print("gheir ghabel ghabool")
                continue

            if phone_number.startswith("0") == False:
                print("gheir ghabel ghabool")
                continue

            if phone_number.isalnum() == True:
                if len(phone_number) == 11:
                    if phone_number.startswith ("0") == True:
                        print("ghabel ghabool")
                        break

                    else:
                        print("gheir ghabel ghabool")
                        continue

        while True:

            addres = input("addres khod ra vared konid:")

            if addres == "" or addres == " " or addres == "  " or addres == "   ":
                print("addres nazadi")
                continue

            if addres.isprintable() == False:
                print("gheir ghabel ghabool")
                continue

            if addres.isprintable() == True:
                print("ghabel ghabool")
                break

            else:
                print("gheir ghabel ghabool")
                continue

        while True:

            email = input("email khod ra vared konid:")

            if email == "" or email == " " or email == "  " or email == "   ":
                print("email nazadi")
                continue

            if email.endswith ("@gmail.com") == False:
                print("gheir ghabel ghabool")
                continue

            if email.endswith ("@gmail.com") == True:
                print("ghabel ghabool")
                break

            else:
                print("gheir ghabel ghabool")
                continue

        while True:            

            kod_posti = input("kod posti khod ra vared konid:")
           
            if kod_posti == "" or kod_posti == " " or kod_posti == "  " or kod_posti == "   ":
                print("kod posti nazadi")
                continue

            if kod_posti.isalnum() == False:
                print("gheir ghabel ghabool")
                continue

            if len(kod_posti) != 10:
                print("gheir ghabel ghabool")
                continue

            if kod_posti.isalnum() == True:
                if len(kod_posti) == 10:
                    print("ghabel ghabool")
                    break

                else:
                    print("gheir ghabel ghabool")
                    continue


                

        while True:

            kod_melli = input("kod melli khod ra vared konid:")

            if kod_melli == "" or kod_melli == " " or kod_melli == "  " or kod_melli == "   ":
                print("kod melli nazadi")
                continue

            if kod_melli.isalnum() == False:
                print("gheir ghabel ghabool")
                continue

            if len(kod_melli) != 10:
                print("gheir ghabel ghabool")
                continue

            if kod_melli.isalnum() == True:
                if len (kod_melli) == 10:
                    print("ghabel ghabool")
                    break

                else:
                    print("gheir ghabel ghabool")
                    continue

                

            
                

        










            



            






            

                

                

                    

                    




        
        