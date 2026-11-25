






import os

while True:

    menu_gym = (input("1.roze zoge    2.roze fard     3.exit:"))

    while True:
        match menu_gym:
            case "1":

                roze_zoge = input("1.badansazi mahi 700    2.airobik mahi 500   3.trx mahi 600    4.exit")

                match roze_zoge:
                    case "1":

                        mah_badansazi = int(input("chand mah?"))

                        morabi_badansazi = input("1.ba morabi + 200     2.bi morabai")

                        match morabi_badansazi:
                            case "1":

                                mablagh_badansazi = mah_badansazi * 700 + 200

                                print(mablagh_badansazi)
                                break

                            case "2":

                                mablagh_badansazi = mah_badansazi * 700
                                print(mablagh_badansazi)
                                break

                    case "2":

                        mah_airobik = int(input("chand mah?"))
                        
                        morabi_airobik = input("1.ba morabi + 200     2.bi morabai")
                        
                        match morabi_airobik:
                            case "1":
                        
                                mablagh_airobik = mah_airobik * 500 + 200
                        
                                print(mablagh_airobik)
                                break
                        
                            case "2":
                        
                                mablagh_airobik = mah_airobik * 500
                                print(mablagh_airobik)
                                break

                    case "3":

                        mah_trx = int(input("chand mah?"))
                        
                        morabi_trx = input("1.ba morabi + 200     2.bi morabai")
                        
                        match morabi_trx:
                            case "1":
                        
                                mablagh_trx = mah_trx * 600 + 200
                        
                                print(mablagh_trx)
                                break
                        
                            case "2":
                        
                                mablagh_trx = mah_trx * 600
                                print(mablagh_trx)
                                break

                    case "4":
                        os.system("cls")
                        break

            case "2":
                

                roze_fard = input("1.badansazi mahi 700    2.airobik mahi 500   3.trx mahi 600    4.exit")
                
                match roze_fard:
                    case "1":
                
                        mah_badansazi = int(input("chand mah?"))
                
                        morabi_badansazi = input("1.ba morabi + 200     2.bi morabai")
                
                        match morabi_badansazi:
                            case "1":
                
                                mablagh_badansazi = mah_badansazi * 700 + 200
                
                                print(mablagh_badansazi)
                                break
                
                            case "2":
                
                                mablagh_badansazi = mah_badansazi * 700
                                print(mablagh_badansazi)
                                break
                
                    case "2":
                
                        mah_airobik = int(input("chand mah?"))
                
                        morabi_airobik = input("1.ba morabi + 200     2.bi morabai")
                
                        match morabi_airobik:
                            case "1":
                
                                mablagh_airobik = mah_airobik * 500 + 200
                
                                print(mablagh_airobik)
                                break
                
                            case "2":
                
                                mablagh_airobik = mah_airobik * 500
                                print(mablagh_airobik)
                                break
                
                    case "3":
                
                        mah_trx = int(input("chand mah?"))
                
                        morabi_trx = input("1.ba morabi + 200     2.bi morabai")
                
                        match morabi_trx:
                            case "1":
                
                                mablagh_trx = mah_trx * 600 + 200
                
                                print(mablagh_trx)
                                break
                
                            case "2":
                
                                mablagh_trx = mah_trx * 600
                                print(mablagh_trx)
                                break
                
                    case "4":
                        os.system("cls")
                        break

            case "3":
                os.system("cls")
                break 

    





                                        




                       

                        
                         

                        
                    

                        



                         


                        



                        



