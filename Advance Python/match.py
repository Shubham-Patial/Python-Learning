def color(fav_color): 
    match fav_color:  
        case "red": 
            return "Red is my favourite color" 
        case "blue": 
            return "Blue is my favourite color" 
        case "black": 
            return "Black is my favourite color" 
        case _: 
            return "No favourite color"  


print(color("red"))