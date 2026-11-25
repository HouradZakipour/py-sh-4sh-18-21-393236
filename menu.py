






while True:

    print("khosh amadid")
    

    menu_restooran_hourad = input("1.noshidani       2.ghaza         3.exit")

    while True:

        match menu_restooran_hourad:
            case "1":
                menu_noshidani = input("1.doogh 100     2.nooshabe 120     3.exit")

                match menu_noshidani:
                    case"1":
                        tedad_doogh = int(input("chand ta doogh mikhay?"))
                        mablagh_doogh = tedad_doogh * 100
                        print(mablagh_doogh)
                        break

                    case"2":
                        tedad_noshabe = int(input("chand ta nooshabe mikhay?"))
                        mablagh_nooshabe = tedad_noshabe * 120
                        print(mablagh_nooshabe)
                        break

                    case"3":
                        break

            case "2":
                menu_ghaza = input("1.pizza 800   2.hotdog 400    3.exit")

                match menu_ghaza:
                    case "1":
                        tedad_pizza = int(input("chand ta pizza mikhay?"))
                        mablagh_pizza = tedad_pizza * 800
                        print(mablagh_pizza)
                        break

                    case "2":
                        tedad_hotdog = int(input("chand ta hotdog mikhay?"))
                        mablagh_hotdog = tedad_hotdog * 400
                        print(mablagh_hotdog)
                        break

                    case "3":
                        break

            case "3":
                break       


                



                    
                        
